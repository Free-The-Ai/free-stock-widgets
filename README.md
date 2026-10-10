<p align="center">
  <a href="https://free-the-ai.github.io/free-stock-widgets/"><img src=".github/banner.jpg" alt="FreeTheAI Stock Widgets" width="100%"></a>
</p>

<p align="center">
  <a href="https://stocks.freetheai.org"><img src="https://img.shields.io/badge/FreeTheAI-Stocks-111111" alt="FreeTheAI Stocks"></a>
  <a href="https://stocks.freetheai.org/docs"><img src="https://img.shields.io/badge/embeds-no%20key%20needed-111111" alt="No key needed"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-111111" alt="MIT license"></a>
  <a href="https://discord.gg/secrets"><img src="https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <b><a href="https://free-the-ai.github.io/free-stock-widgets/">Documentation with live demos</a></b> ·
  <a href="https://stocks.freetheai.org/docs">Official embed docs</a> ·
  <a href="https://stocks.freetheai.org">FreeTheAI Stocks</a> ·
  <a href="https://freetheai.org">freetheai.org</a>
</p>

# FreeTheAI Stock Widgets

Show live stock, crypto, and currency prices on your own site, with no account and no API key. FreeTheAI Stocks offers a price card you can embed in any page that allows iframes, static SVG charts you can drop into an `<img>` tag, news feeds in RSS and Markdown, and share images for social cards.

This repository shows how to use all of it: copy-ready examples for plain HTML, WordPress and Ghost, Markdown, React, Vue, and Python, and a demo site with live embeds.

## Quick start

Paste this into any HTML page, or into a WordPress or Ghost HTML block:

```html
<iframe src="https://stocks.freetheai.org/embed/NASDAQ-AAPL" width="340" height="170"
  style="border:0;max-width:100%" loading="lazy" title="Apple Inc. (AAPL) price - FreeTheAI Stocks"></iframe>
<p style="font-size:12px"><a href="https://stocks.freetheai.org/symbols/NASDAQ-AAPL">AAPL stock price</a> by FreeTheAI Stocks</p>
```

Keep the link back to the symbol page. It is how readers find the full quote, the chart, and the news for that symbol.

## What you can embed

| Widget | Address | Notes |
| --- | --- | --- |
| Live price card | `https://stocks.freetheai.org/embed/EXCHANGE-SYMBOL` | Price, today's move, and a line chart. `theme=light` or `theme=dark`; `range=5D`, `1M` (default), `6M`, `1Y`, or `5Y`. |
| Chart image | `https://stocks.freetheai.org/chart/EXCHANGE-SYMBOL.svg?range=6M` | A sharp SVG, a few kilobytes. `range` is `5D`, `1M`, `6M` (default), `1Y`, or `5Y`. |
| Sparkline | `https://stocks.freetheai.org/chart/EXCHANGE-SYMBOL.svg?range=1M&mini=1` | Only the line, for tables and cards. |
| News feed | `https://stocks.freetheai.org/news/rss.xml` | Every write-up, newest first. |
| Write-up as Markdown | `https://stocks.freetheai.org/news/<slug>.md` | The full text of one write-up. |
| Share image | `https://stocks.freetheai.org/og/symbols/EXCHANGE-SYMBOL.png` | A 1200 by 630 preview with the live price. |

Symbols use the same `EXCHANGE-SYMBOL` format as their page address, for example `NASDAQ-NVDA`, `NYSE-KO`, or `BITSTAMP-BTCUSD`.

## Examples

| Folder | What it shows |
| --- | --- |
| [`examples/plain-html`](examples/plain-html/) | A single HTML page with a price card, a chart, and a headline list |
| [`examples/wordpress-ghost`](examples/wordpress-ghost/) | The HTML block to paste into WordPress or Ghost |
| [`examples/markdown`](examples/markdown/) | Chart and card markup for a README, a blog post, or a wiki |
| [`examples/react`](examples/react/) | A `PriceCard` component |
| [`examples/vue`](examples/vue/) | A `PriceCard` component |
| [`examples/python`](examples/python/) | A script that reads the RSS feed and prints the latest headlines |

## Languages

Write-ups are also published in Spanish, French, German, Portuguese, Japanese, Chinese, and Arabic. Each language has its own address, for example `https://stocks.freetheai.org/es/news/<slug>` or `https://stocks.freetheai.org/ja/news/<slug>`. Language codes: `es`, `fr`, `de`, `pt`, `ja`, `zh`, `ar`.

## For AI agents

- `https://stocks.freetheai.org/llms.txt` describes the site for AI assistants.
- `https://stocks.freetheai.org/llms-full.txt` carries the newest write-ups in full.
- Sitemaps: `https://stocks.freetheai.org/sitemap.xml`, `https://stocks.freetheai.org/news-sitemap.xml`, `https://stocks.freetheai.org/sitemap-symbols.xml`.

## Usage terms

- Free to use on any site, with no key and no sign-up.
- Keep the link back to the symbol page.
- Embeds and images are cached for about a minute. Do not request them in tight loops.
- Prices and charts can be delayed or wrong. They are for information only.
- Nothing here is financial advice.

The write-ups are written by our own AI models, which gather expert market information from across the web. Each write-up lists the symbols it names.

## Documentation

The [documentation site](https://free-the-ai.github.io/free-stock-widgets/) has the same details with live demos of every widget: [live price cards](https://free-the-ai.github.io/free-stock-widgets/live-price-card/), [chart images](https://free-the-ai.github.io/free-stock-widgets/chart-images/), [news feeds](https://free-the-ai.github.io/free-stock-widgets/news-feeds/), [languages](https://free-the-ai.github.io/free-stock-widgets/languages/), [share images](https://free-the-ai.github.io/free-stock-widgets/share-images/), [for AI agents](https://free-the-ai.github.io/free-stock-widgets/for-ai-agents/), and [usage](https://free-the-ai.github.io/free-stock-widgets/usage/).

## More from FreeTheAI

- [Python SDK](https://github.com/Free-The-Ai/freetheai-python), [JavaScript SDK](https://github.com/Free-The-Ai/freetheai-js), and [Go SDK](https://github.com/Free-The-Ai/freetheai-go) for the free AI API
- [Cookbook](https://github.com/Free-The-Ai/freetheai-cookbook): runnable examples
- [freetheai.org](https://freetheai.org): the free AI API behind the write-ups

## License

MIT. Built by [Vibhek Soni](https://vibheksoni.com).
