<!--
  A FreeTheAI Stocks price card for Vue 3 (Vite or Nuxt).
  Usage: <PriceCard symbol="NASDAQ-AAPL" name="Apple Inc. (AAPL)" theme="light" range="1M" />
-->
<script setup>
const props = defineProps({
  symbol: { type: String, required: true },
  name: { type: String, required: true },
  theme: { type: String, default: "light" },
  range: { type: String, default: "1M" },
  width: { type: Number, default: 340 },
  height: { type: Number, default: 170 },
});

const src = `https://stocks.freetheai.org/embed/${encodeURIComponent(props.symbol)}?theme=${props.theme}&range=${props.range}`;
const page = `https://stocks.freetheai.org/symbols/${encodeURIComponent(props.symbol)}`;
</script>

<template>
  <figure style="margin: 1.5rem 0">
    <iframe
      :src="src"
      :width="width"
      :height="height"
      style="border: 0; max-width: 100%"
      loading="lazy"
      :title="`${name} price - FreeTheAI Stocks`"
    />
    <figcaption style="font-size: 12px">
      <a :href="page">{{ name }}</a> by FreeTheAI Stocks. Prices can be delayed. Not financial advice.
    </figcaption>
  </figure>
</template>
