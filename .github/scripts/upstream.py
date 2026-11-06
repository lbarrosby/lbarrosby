import json
import urllib.parse
import os
import re
import urllib.request

USER = os.environ.get("GH_USER", "lbarrosby")
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def search():
    q = f"author:{USER} type:pr -user:{USER}"
    items = []
    for page in range(1, 11):
        url = f"https://api.github.com/search/issues?per_page=100&page={page}&sort=created&order=desc&q=" + urllib.parse.quote(q)
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {TOKEN}"} if TOKEN else {})
        batch = json.load(urllib.request.urlopen(req))["items"]
        items += batch
        if len(batch) < 100:
            break
    return items


SHARED_ORGS = {"nvidia", "kubernetes", "kubernetes-sigs"}
EXTRA_ORGS = {"prometheus-community": ("graduated", "Prometheus")}
RANK = {"sandbox": 1, "incubating": 2, "graduated": 3}


def cncf_levels():
    try:
        data = json.load(urllib.request.urlopen("https://landscape.cncf.io/data/full.json", timeout=60))
    except Exception:
        return {}, {}
    repos, orgs = {}, {}
    for item in data["items"]:
        level = item.get("maturity")
        if level not in RANK:
            continue
        for r in item.get("repositories") or []:
            parts = r["url"].rstrip("/").lower().split("github.com/")[-1].split("/")
            if len(parts) < 2:
                continue
            repos["/".join(parts[:2])] = (level, item["name"])
            if RANK[level] > RANK.get(orgs.get(parts[0], ("", ""))[0], 0):
                orgs[parts[0]] = (level, item["name"])
    for org in SHARED_ORGS:
        orgs.pop(org, None)
    orgs.update(EXTRA_ORGS)
    return repos, orgs


def cncf_label(repo, repos, orgs):
    name = repo.lower()
    org = name.split("/")[0]
    if org in ("kubernetes", "kubernetes-sigs"):
        level, project = "graduated", "Kubernetes"
    elif name in repos:
        level, project = repos[name]
    elif org in orgs:
        level, project = orgs[org]
    else:
        return ""
    return f"CNCF {level.capitalize()} ({project})"


COLORS = {"graduated": "0086FF", "incubating": "8957E5", "sandbox": "6E7781"}


def cncf_badge(repo, repos, orgs):
    label = cncf_label(repo, repos, orgs)
    if not label:
        return ""
    level = label.split()[1].lower()
    project = label.split("(", 1)[1].rstrip(")")
    return f'<img src="https://img.shields.io/badge/CNCF-{level.capitalize()}-{COLORS[level]}?style=flat-square&logo=cncf&logoColor=white" alt="CNCF {level}" title="{project}: CNCF {level}">'


def status(pr):
    if pr["pull_request"].get("merged_at"):
        return "merged"
    return "open" if pr["state"] == "open" else "closed"


def main():
    prs = [p for p in search() if status(p) != "closed"]
    repos = {}
    for p in prs:
        repo = p["repository_url"].split("/repos/")[1]
        repos.setdefault(repo, []).append(p)
    merged = sum(1 for p in prs if status(p) == "merged")
    badges = [f'<img src="https://img.shields.io/badge/upstream%20PRs-{len(prs)}-1F6FEB?style=flat-square" alt="Upstream PRs">']
    if merged:
        badges.append(f'<img src="https://img.shields.io/badge/merged-{merged}-8957E5?style=flat-square" alt="Merged">')
    badges.append(f'<img src="https://img.shields.io/badge/projects-{len(repos)}-2EA043?style=flat-square" alt="Projects">')
    repos_cncf, orgs_cncf = cncf_levels()
    graduated = sum(1 for p in prs if status(p) == "merged" and "Graduated" in cncf_label(p["repository_url"].split("/repos/")[1], repos_cncf, orgs_cncf))
    if graduated:
        badges.append(f'<img src="https://img.shields.io/badge/merged%20in%20CNCF%20graduated-{graduated}-0086FF?style=flat-square" alt="Merged in CNCF graduated projects">')
    lines = [" ".join(badges), ""]
    done = [p for p in prs if status(p) == "merged"]
    if done:
        lines += ["**Merged**", ""]
        for p in sorted(done, key=lambda p: p["pull_request"]["merged_at"], reverse=True):
            repo = p["repository_url"].split("/repos/")[1]
            title = p["title"].replace("|", "\\|")
            badge = cncf_badge(repo, repos_cncf, orgs_cncf)
            tag = f" {badge}" if badge else ""
            lines.append(f"- [{repo}](https://github.com/{repo}){tag}: [{title}]({p['html_url']})")
        lines.append("")
    open_repos = {r: [p for p in items if status(p) == "open"] for r, items in repos.items()}
    open_repos = {r: items for r, items in open_repos.items() if items}
    ordered = sorted(open_repos.items(), key=lambda kv: kv[1][0]["created_at"], reverse=True)
    lines += ["**In review**", "", "| Project | CNCF | Pull requests |", "|---|---|---|"]
    for repo, items in ordered:
        links = "<br>".join(f"[{p['title'].replace('|', chr(92) + '|')}]({p['html_url']})" for p in items)
        badge = cncf_badge(repo, repos_cncf, orgs_cncf)
        lines.append(f"| [{repo}](https://github.com/{repo}) | {badge} | {links} |")
    block = "\n".join(lines)
    readme = open("README.md").read()
    readme = re.sub(r"(<!--START_SECTION:activity-->\n).*?(<!--END_SECTION:activity-->)", lambda m: m.group(1) + block + "\n" + m.group(2), readme, flags=re.S)
    open("README.md", "w").write(readme)


if __name__ == "__main__":
    main()
