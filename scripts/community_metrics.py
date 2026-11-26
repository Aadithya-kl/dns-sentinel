"""Report unique external authors of merged PRs in the last 12 months."""

from __future__ import annotations

import datetime as dt
import json
import os
import urllib.error
import urllib.parse
import urllib.request


def main() -> int:
    repository = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    owner = repository.split("/", maxsplit=1)[0].casefold()
    cutoff = (dt.datetime.now(dt.timezone.utc).date() - dt.timedelta(days=365)).isoformat()
    query = urllib.parse.urlencode(
        {"q": f"repo:{repository} is:pr is:merged merged:>={cutoff}", "per_page": "100"}
    )
    url = f"https://api.github.com/search/issues?{query}"
    authors: set[str] = set()
    total_merged = 0

    while url:
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                page = json.load(response)
                next_link = response.headers.get("Link", "")
        except (OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
            raise SystemExit(f"Could not read merged PRs from GitHub: {exc}") from exc

        total_merged = max(total_merged, int(page.get("total_count", 0)))
        for pull_request in page.get("items", []):
            user = pull_request.get("user") or {}
            login = str(user.get("login", ""))
            if (
                login
                and login.casefold() != owner
                and user.get("type") != "Bot"
                and not login.casefold().endswith("[bot]")
            ):
                authors.add(login.casefold())

        url = ""
        if 'rel="next"' in next_link:
            for link in next_link.split(","):
                if 'rel="next"' in link:
                    url = link[link.find("<") + 1 : link.find(">")]
                    break

    count = len(authors)
    summary = (
        "## DNS Sentinel project health\n\n"
        f"- Merged PRs found in the last 365 days: {total_merged}\n"
        f"- Unique external, non-bot PR authors: {count}/20\n"
        f"- Remaining contributors for the community-builder threshold: {max(0, 20 - count)}\n"
        f"- Window starts: {cutoff} (UTC)\n\n"
        "This count excludes the repository owner and bot accounts. It does not claim that a "
        "qualification has been awarded. Review merged PR history if authorship is ambiguous.\n"
    )
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as report:
        report.write(summary)
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
