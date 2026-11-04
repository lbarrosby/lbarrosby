import json
import urllib.parse
import os
import re
import urllib.request

USER = os.environ.get("GH_USER", "lbarrosby")
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def search():
    q = f"author:{USER} type:pr -user:{USER}"
    url = "https://api.github.com/search/issues?per_page=100&sort=created&order=desc&q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {TOKEN}"} if TOKEN else {})
    return json.load(urllib.request.urlopen(req))["items"]


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
    lines = [
        " ".join(badges),
        "",
        "| Project | Latest pull request | |",
        "|---|---|---|",
    ]
    for repo, items in sorted(repos.items(), key=lambda kv: kv[1][0]["created_at"], reverse=True):
        p = items[0]
        title = p["title"].replace("|", "\\|")
        more = f" · +{len(items) - 1} more" if len(items) > 1 else ""
        lines.append(f"| [{repo}](https://github.com/{repo}) | [{title}]({p['html_url']}){more} | `{status(p)}` |")
    block = "\n".join(lines)
    readme = open("README.md").read()
    readme = re.sub(r"(<!--START_SECTION:activity-->\n).*?(<!--END_SECTION:activity-->)", lambda m: m.group(1) + block + "\n" + m.group(2), readme, flags=re.S)
    open("README.md", "w").write(readme)


if __name__ == "__main__":
    main()
