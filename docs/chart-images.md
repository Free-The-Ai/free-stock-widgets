---
description: Static SVG price charts and sparklines for any FreeTheAI Stocks symbol, sharp at any size and a few kilobytes, with ranges from five days to five years.
---

# Chart images

Every symbol has a static SVG price chart. It is sharp at any size, a few kilobytes, and cached for about five minutes. Wrap it in a link to the symbol page so readers can see more.

## Six-month chart

<a href="https://stocks.freetheai.org/symbols/NASDAQ-AAPL"><img src="https://stocks.freetheai.org/chart/NASDAQ-AAPL.svg?range=6M" width="720" height="260" alt="Apple Inc. (AAPL) six-month price chart" loading="lazy" style="max-width:100%;height:auto"></a>

```html
<a href="https://stocks.freetheai.org/symbols/NASDAQ-AAPL">
  <img src="https://stocks.freetheai.org/chart/NASDAQ-AAPL.svg?range=6M" width="720" height="260"
    alt="Apple Inc. (AAPL) six-month price chart" loading="lazy">
</a>
```

## Sparkline (no axes)

<img src="https://stocks.freetheai.org/chart/NASDAQ-NVDA.svg?range=1M&mini=1" width="240" height="64" alt="NVIDIA one-month price line">

```html
<img src="https://stocks.freetheai.org/chart/NASDAQ-NVDA.svg?range=1M&mini=1" width="240" height="64"
  alt="NVIDIA one-month price line">
```

## Options

| Option | Values | Default |
| --- | --- | --- |
| `range` | `5D`, `1M`, `6M`, `1Y`, `5Y` | `6M` |
| `mini` | `1` | Off. `mini=1` draws only the line, with no axes, for tables and cards. |

The address is `https://stocks.freetheai.org/chart/EXCHANGE-SYMBOL.svg`, with the options as a query string.

For a Markdown README or wiki, use the image with a link as shown in [`examples/markdown`](https://github.com/Free-The-Ai/free-stock-widgets/tree/main/examples/markdown).
