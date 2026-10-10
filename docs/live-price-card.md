---
description: Embed a live FreeTheAI Stocks price card in any page that allows iframes. Choose the light or dark theme, a one-year or five-year line, and keep the link back.
---

# Live price cards

A price card shows the price, today's move, and a line chart for any symbol. It runs no scripts, refreshes itself about every minute, and links readers to the full symbol page.

## Copy this

```html
<iframe src="https://stocks.freetheai.org/embed/NASDAQ-AAPL" width="340" height="170"
  style="border:0;max-width:100%" loading="lazy" title="Apple Inc. (AAPL) price - FreeTheAI Stocks"></iframe>
<p style="font-size:12px"><a href="https://stocks.freetheai.org/symbols/NASDAQ-AAPL">AAPL stock price</a> by FreeTheAI Stocks</p>
```

## Live demos

Default card (light, one month):

<iframe src="https://stocks.freetheai.org/embed/NASDAQ-AAPL" width="340" height="170" style="border:0;max-width:100%" loading="lazy" title="Apple Inc. (AAPL) price - FreeTheAI Stocks"></iframe>

Dark card, one-year line:

<iframe src="https://stocks.freetheai.org/embed/BITSTAMP-BTCUSD?theme=dark&range=1Y" width="340" height="170" style="border:0;max-width:100%" loading="lazy" title="Bitcoin price - FreeTheAI Stocks"></iframe>

Five-day line for a stock:

<iframe src="https://stocks.freetheai.org/embed/NASDAQ-NVDA?range=5D" width="340" height="170" style="border:0;max-width:100%" loading="lazy" title="NVIDIA (NVDA) price - FreeTheAI Stocks"></iframe>

## Options

| Option | Values | Default |
| --- | --- | --- |
| `theme` | `light`, `dark` | Follows the reader's system setting when left out |
| `range` | `5D`, `1M`, `6M`, `1Y`, `5Y` | `1M` |

The address is `https://stocks.freetheai.org/embed/EXCHANGE-SYMBOL`, with the options as a query string. The `EXCHANGE-SYMBOL` format is the same as the symbol page address: `NASDAQ-NVDA`, `NYSE-KO`, `BITSTAMP-ETHUSD`.

## Size

The card fills the iframe, so any size from about 260 by 140 pixels upward works. 340 by 170 is a good default for a sidebar or a grid. Set `max-width:100%` so it fits narrow screens.

## The link back

Keep a link to the symbol page under the card. Readers use it to reach the full quote, the chart, and the write-ups for that symbol. Every symbol page also has an Embed panel that builds this code for you.

## Good to know

- Prices can be delayed or wrong. The card is for information only. Nothing here is financial advice.
- Cards are cached for about a minute. Do not reload them in a tight loop.
