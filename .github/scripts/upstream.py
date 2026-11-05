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
    lines = [" ".join(badges), ""]
    done = [p for p in prs if status(p) == "merged"]
    if done:
        lines += ["**Merged**", ""]
        for p in sorted(done, key=lambda p: p["pull_request"]["merged_at"], reverse=True):
            repo = p["repository_url"].split("/repos/")[1]
            title = p["title"].replace("|", "\\|")
            lines.append(f"- [{repo}](https://github.com/{repo}): [{title}]({p['html_url']})")
        lines.append("")
    open_repos = {r: [p for p in items if status(p) == "open"] for r, items in repos.items()}
    open_repos = {r: items for r, items in open_repos.items() if items}
    ordered = sorted(open_repos.items(), key=lambda kv: kv[1][0]["created_at"], reverse=True)
    lines += ["**In review**", "", "| Project | Pull requests |", "|---|---|"]
    for repo, items in ordered:
        links = "<br>".join(f"[{p['title'].replace('|', chr(92) + '|')}]({p['html_url']})" for p in items)
        lines.append(f"| [{repo}](https://github.com/{repo}) | {links} |")
    block = "\n".join(lines)
    readme = open("README.md").read()
    readme = re.sub(r"(<!--START_SECTION:activity-->\n).*?(<!--END_SECTION:activity-->)", lambda m: m.group(1) + block + "\n" + m.group(2), readme, flags=re.S)
    open("README.md", "w").write(readme)


if __name__ == "__main__":
    main()
