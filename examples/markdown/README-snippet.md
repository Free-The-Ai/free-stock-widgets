# Markdown snippets

Markdown does not run iframes, so use the chart image for a README, a wiki, or a blog post that renders Markdown. Wrap it in a link so readers can open the symbol page.

## A six-month chart

```markdown
[![Apple (AAPL) six-month price chart](https://stocks.freetheai.org/chart/NASDAQ-AAPL.svg?range=6M)](https://stocks.freetheai.org/symbols/NASDAQ-AAPL)

[AAPL on FreeTheAI Stocks](https://stocks.freetheai.org/symbols/NASDAQ-AAPL). Prices can be delayed. Not financial advice.
```

## A sparkline in a table

```markdown
| Symbol | One month | Price page |
| --- | --- | --- |
| NVDA | ![NVIDIA one-month line](https://stocks.freetheai.org/chart/NASDAQ-NVDA.svg?range=1M&mini=1) | [NVDA](https://stocks.freetheai.org/symbols/NASDAQ-NVDA) |
| KO | ![Coca-Cola one-month line](https://stocks.freetheai.org/chart/NYSE-KO.svg?range=1M&mini=1) | [KO](https://stocks.freetheai.org/symbols/NYSE-KO) |
```

## A link to the latest write-up

Write-ups are also available as Markdown: add `.md` to the address.

```markdown
Read the write-up: [Quantum computing stocks hit 52-week lows](https://stocks.freetheai.org/news/quantum-computing-stocks-hit-52-week-lows-amid-sector-cash-burn-and-macro-risks-5709b8)
```

The Markdown version of the same page is at `https://stocks.freetheai.org/news/quantum-computing-stocks-hit-52-week-lows-amid-sector-cash-burn-and-macro-risks-5709b8.md`.
