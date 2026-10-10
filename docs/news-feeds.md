---
description: Follow FreeTheAI Stocks news with the RSS feed, Markdown write-ups, and sitemaps. Feed readers, newsletters, and site builders can pick up every write-up.
---

# News feeds

Every write-up is available as RSS, as Markdown, and in sitemaps, so news readers, newsletters, and site builders can follow along.

## RSS

```
https://stocks.freetheai.org/news/rss.xml
```

The feed lists the newest write-ups first, with the title, link, summary, date, and category. Each item links to the write-up on the site.

To read it from code, see [`examples/python/read_rss.py`](https://github.com/Free-The-Ai/free-stock-widgets/blob/main/examples/python/read_rss.py), which prints the newest headlines with the standard library.

## One write-up as Markdown

Add `.md` to any write-up address:

```
https://stocks.freetheai.org/news/<slug>.md
```

The Markdown version has the same text, which is handy for a blog import or a static site generator.

## Categories

Filter the news list with `?category=<name>`, for example `https://stocks.freetheai.org/news?category=earnings`. Categories include `earnings`, `dividends`, `mergers`, `ipo`, `analyst_ratings`, `macro`, `central_banks`, `crypto`, `regulation`, `commodities`, `forex`, `technology`, `energy`, `markets`, and `company_news`.

## Sitemaps

```
https://stocks.freetheai.org/sitemap.xml
https://stocks.freetheai.org/news-sitemap.xml
https://stocks.freetheai.org/sitemap-symbols.xml
```

The news sitemap is in the format news search engines read. The symbol sitemap lists every symbol page.

## Good to know

- Write-ups are written by our own AI models, which gather expert market information from across the web. Each write-up lists the symbols it names.
- Prices in a write-up can be delayed. Nothing here is financial advice.
- Cache the feed on your side. The server caches it for about a minute, so polling it more often does not help.
