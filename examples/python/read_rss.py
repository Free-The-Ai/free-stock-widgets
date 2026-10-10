"""Read the FreeTheAI Stocks news feed and print the newest headlines.

Uses only the standard library. The feed is free, needs no key, and is cached
on the server for about a minute, so run this once in a while, not in a loop.

    python read_rss.py            # newest 10 headlines
    python read_rss.py 25         # newest 25
"""

from __future__ import annotations

import sys
import urllib.request
import xml.etree.ElementTree as ET

FEED_URL = "https://stocks.freetheai.org/news/rss.xml"
USER_AGENT = "free-stock-widgets-example/1.0 (+https://github.com/Free-The-Ai/free-stock-widgets)"


def fetch_feed(url: str = FEED_URL, timeout: float = 20.0) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def parse_items(xml_bytes: bytes) -> list[dict[str, str]]:
    root = ET.fromstring(xml_bytes)
    items = []
    for item in root.iter("item"):
        items.append(
            {
                "title": (item.findtext("title") or "").strip(),
                "link": (item.findtext("link") or "").strip(),
                "published": (item.findtext("pubDate") or "").strip(),
                "category": (item.findtext("category") or "").strip(),
            }
        )
    return items


def main() -> None:
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    items = parse_items(fetch_feed())[:limit]
    for item in items:
        print(f"{item['published']}  [{item['category']}]")
        print(f"  {item['title']}")
        print(f"  {item['link']}")
        print()
    print("Prices can be delayed. Nothing here is financial advice.")


if __name__ == "__main__":
    main()
