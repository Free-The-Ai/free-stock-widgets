// A FreeTheAI Stocks price card for React. Works in any React app (Vite, Next.js, Remix).
// Usage: <PriceCard symbol="NASDAQ-AAPL" name="Apple Inc. (AAPL)" theme="light" range="1M" />

export function PriceCard({
  symbol,
  name,
  theme = "light",
  range = "1M",
  width = 340,
  height = 170,
}) {
  const src = `https://stocks.freetheai.org/embed/${encodeURIComponent(symbol)}?theme=${theme}&range=${range}`;
  const page = `https://stocks.freetheai.org/symbols/${encodeURIComponent(symbol)}`;

  return (
    <figure style={{ margin: "1.5rem 0" }}>
      <iframe
        src={src}
        width={width}
        height={height}
        style={{ border: 0, maxWidth: "100%" }}
        loading="lazy"
        title={`${name} price - FreeTheAI Stocks`}
      />
      <figcaption style={{ fontSize: 12 }}>
        <a href={page}>{name}</a> by FreeTheAI Stocks. Prices can be delayed. Not financial advice.
      </figcaption>
    </figure>
  );
}

// Example page:
//
// import { PriceCard } from "./PriceCard";
//
// export default function Markets() {
//   return (
//     <>
//       <PriceCard symbol="NASDAQ-AAPL" name="Apple Inc. (AAPL)" />
//       <PriceCard symbol="BITSTAMP-BTCUSD" name="Bitcoin" theme="dark" range="1Y" />
//     </>
//   );
// }
