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
    project = label.split("(", 1)[1][:-1]
    if "(" in project:
        project = project.split("(", 1)[1].rstrip(")")
    name = urllib.parse.quote(project.replace("-", "--").replace("_", "__"))
    return f'<img src="https://img.shields.io/badge/{name}-CNCF%20{level.capitalize()}-{COLORS[level]}?style=flat-square&logo=cncf&logoColor=white" alt="{project}: CNCF {level}" title="{project}: CNCF {level}">'


BOTS = {"poiana", "k8s-ci-robot", "codecov-commenter", "coveralls", "netlify", "vercel", "linux-foundation-easycla"}
THANKS = re.compile(r"thank|thx|appreciate|great|awesome|nice|good catch|well done|excellent|🙏|💚|❤", re.I)
CACHE = ".github/data/merged.json"


def api(path):
    req = urllib.request.Request("https://api.github.com/" + path, headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {TOKEN}"} if TOKEN else {})
    return json.load(urllib.request.urlopen(req, timeout=60))


def human(u):
    return u and u.get("type") != "Bot" and u["login"] != USER and u["login"].lower() not in BOTS


def short(text):
    text = re.sub(r"`|\*|_|<[^>]+>|\[|\]\([^)]*\)|@" + USER, "", text)
    text = re.sub(r"(^|\s)/[a-z-]+", " ", text)
    text = re.sub(r"\s+([,.!?])", r"\1", " ".join(text.split()))
    text = re.sub(r",([.!?])", r"\1", text)
    parts = [x.strip() for x in re.split(r"(?<=[.!?])\s", text) if x.strip()]
    hits = sorted((x for x in parts if THANKS.search(x)), key=lambda x: THANKS.search(x).start())
    first = hits[0] if hits else (parts[0] if parts else "")
    m = THANKS.search(first)
    if len(first) > 90 and m and m.start() > 40:
        first = first[m.start():]
        first = first[0].upper() + first[1:]
    if len(first) > 90:
        first = first[:87].rsplit(" ", 1)[0] + "…"
    return first.replace("|", "/").replace('"', "'")


def details(pr, cache):
    url = pr["html_url"]
    if url in cache:
        return cache[url]
    repo = pr["repository_url"].split("/repos/")[1]
    n = pr["number"]
    info = {"merged_by": "", "thanks": None}
    try:
        info["merged_by"] = (api(f"repos/{repo}/pulls/{n}").get("merged_by") or {}).get("login", "")
        notes = [(c["user"], c["body"] or "", c["html_url"]) for c in api(f"repos/{repo}/issues/{n}/comments?per_page=100")]
        notes += [(r["user"], r["body"] or "", r["html_url"]) for r in api(f"repos/{repo}/pulls/{n}/reviews?per_page=100")]
        for user, body, link in notes:
            if human(user) and THANKS.search(body) and "first PR" not in body:
                info["thanks"] = {"login": user["login"], "quote": short(body), "url": link}
                break
    except Exception:
        return info
    cache[url] = info
    return info


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
    site = "https://lbarrosby.github.io/lbarrosby/"
    badges.append(f'<a href="{site}"><img src="https://img.shields.io/badge/filter%20%26%20search-all%20PRs-F78166?style=flat-square&logo=githubpages&logoColor=white" alt="Filter and search all PRs"></a>')
    lines = [" ".join(badges), ""]
    done = [p for p in prs if status(p) == "merged"]
    try:
        cache = json.load(open(CACHE))
    except Exception:
        cache = {}
    info = {p["html_url"]: details(p, cache) for p in done}
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(cache, open(CACHE, "w"), indent=1, sort_keys=True, ensure_ascii=False)
    thanked = sum(1 for v in info.values() if v["thanks"])
    if thanked:
        lines[0] += f' <img src="https://img.shields.io/badge/thanked%20by%20maintainers-{thanked}-DB61A2?style=flat-square" alt="Thanked by maintainers">'

    def level(repo):
        label = cncf_label(repo, repos_cncf, orgs_cncf)
        return label.split()[1].lower() if label else "other"

    groups = [("graduated", "CNCF Graduated"), ("incubating", "CNCF Incubating"), ("sandbox", "CNCF Sandbox"), ("other", "Other projects")]

    def merged_row(p):
        repo = p["repository_url"].split("/repos/")[1]
        title = p["title"].replace("|", "\\|")
        badge = cncf_badge(repo, repos_cncf, orgs_cncf)
        tag = f"{badge}<br>" if badge else ""
        d = info[p["html_url"]]
        by = d["merged_by"]
        who = f"[@{by}](https://github.com/{by})" if by and not by.endswith("[bot]") else ("Prow" if by else "")
        words = ""
        if d["thanks"]:
            t = d["thanks"]
            words = f'🙏 [@{t["login"]}]({t["url"]}): <i>"{t["quote"]}"</i>'
        return f"| {tag}[{repo}](https://github.com/{repo}) | [{title}]({p['html_url']}) | {p['pull_request']['merged_at'][:10]} | {who} | {words} |"

    if done:
        lines += [f"**Merged** · sorted by CNCF maturity · [filter and search]({site})", ""]
        for key, name in groups:
            items = [p for p in done if level(p["repository_url"].split("/repos/")[1]) == key]
            if not items:
                continue
            items.sort(key=lambda p: p["pull_request"]["merged_at"], reverse=True)
            items.sort(key=lambda p: p["repository_url"].split("/repos/")[1].lower())
            nrepos = len({p["repository_url"] for p in items})
            opened = " open" if key == "graduated" else ""
            lines += [f"<details{opened}><summary><b>{name}</b> · {len(items)} merged in {nrepos} repos</summary>", "", "| Project | Pull request | Merged | Merged by | Kind words |", "|---|---|---|---|---|"]
            lines += [merged_row(p) for p in items]
            lines += ["", "</details>", ""]
    open_repos = {r: [p for p in items if status(p) == "open"] for r, items in repos.items()}
    open_repos = {r: items for r, items in open_repos.items() if items}
    lines += ["**In review** · sorted by CNCF maturity", ""]
    for key, name in groups:
        sel = sorted((kv for kv in open_repos.items() if level(kv[0]) == key), key=lambda kv: kv[0].lower())
        if not sel:
            continue
        n = sum(len(v) for _, v in sel)
        lines += [f"<details><summary><b>{name}</b> · {n} open in {len(sel)} repos</summary>", "", "| Project | Pull requests |", "|---|---|"]
        for repo, items in sel:
            links = "<br>".join(f"[{p['title'].replace('|', chr(92) + '|')}]({p['html_url']})" for p in items)
            badge = cncf_badge(repo, repos_cncf, orgs_cncf)
            tag = f"{badge}<br>" if badge else ""
            lines.append(f"| {tag}[{repo}](https://github.com/{repo}) | {links} |")
        lines += ["", "</details>", ""]
    rows = []
    for p in prs:
        repo = p["repository_url"].split("/repos/")[1]
        label = cncf_label(repo, repos_cncf, orgs_cncf)
        d = info.get(p["html_url"], {})
        t = d.get("thanks") or {}
        by = d.get("merged_by", "")
        rows.append({
            "repo": repo, "org": repo.split("/")[0], "title": p["title"], "url": p["html_url"], "status": status(p),
            "level": level(repo), "project": label.split("(", 1)[1].rstrip(")") if label else "",
            "opened": p["created_at"][:10], "merged": (p["pull_request"].get("merged_at") or "")[:10],
            "merged_by": "Prow" if by.endswith("[bot]") else by,
            "thanks_by": t.get("login", ""), "thanks": t.get("quote", ""), "thanks_url": t.get("url", ""),
        })
    os.makedirs("docs", exist_ok=True)
    json.dump(rows, open("docs/data.json", "w"), indent=0, ensure_ascii=False)
    block = "\n".join(lines)
    readme = open("README.md").read()
    readme = re.sub(r"(<!--START_SECTION:activity-->\n).*?(<!--END_SECTION:activity-->)", lambda m: m.group(1) + block + "\n" + m.group(2), readme, flags=re.S)
    open("README.md", "w").write(readme)


if __name__ == "__main__":
    main()
