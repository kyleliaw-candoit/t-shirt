# Printful setup evidence — October 21, 2026

Scope: Comfort Colors 1717, DTG, front, Ivory, public guest Design Maker, United States delivery context. This is a design/provider preview check; no order, product publication or sample purchase.

## Observed product settings

- Current product page: https://www.printful.com/custom/brands/comfort-colors/unisex-garment-dyed-heavyweight-shirt-comfort-colors-1717?technique=T-SHIRT&color=Pepper&size=S#guidelines (page state subsequently changed to Ivory; URL is not evidence of the selected editor color).
- Editor product title: Unisex Garment-Dyed Heavyweight T-Shirt | Comfort Colors 1717.
- DTG printing radio checked; Ivory #fff4d9 pressed; S/L/2XL enabled in expanded Product panel. This verifies selectable variants in the observed US context, not inventory reservation or every fulfillment country.
- Front/back DTG table: all sizes, maximum/recommended canvas 12 × 16 inches. PNG/JPEG, at least 150 DPI, sRGB. No guide layers. Avoid semitransparent design elements. Borders may distort slightly during production.
- Supplier flat widths: S 18.25, L 22, 2XL 26 inches. Lengths: S 26.625, L 29.375, 2XL 31.625 inches. Source: current Size guide, product measurements (retained in size-chart.txt). Supplier warns measurements can vary by up to 2 inches.

## Size scaling reconciliation

The product page has a generic footnote saying graphics scale according to product size. The more specific current [Printful Help Center explanation](https://help.printful.com/hc/en-us/articles/50264397552657-How-is-my-design-scaled-for-different-garment-sizes) says dimensions generally remain fixed, with automatic downscaling indicated by smaller maximum print areas in the product's file guidelines. Its [large-area article](https://help.printful.com/hc/en-us/articles/50263171283217-What-should-I-know-about-the-standard-15-18-print-placement-for-DTG-products) identifies the 15 × 18 exception products; 1717 is not listed.

**Working conclusion from these combined sources:** retain fixed artwork inches for 1717 S/L/2XL because its current table lists 12 × 16 for all sizes. Do not apply the Bella+Canvas 3001 11.5/15 downscale ratio to this product. This resolves the earlier desk-level ambiguity enough to calculate proportions. It is an inference from published rules, not a measured physical production result.

## Geometry and evidence limits

Each transparent upload is 1800 × 2400 at 150 DPI, carrying the entire 12 × 16 canvas. Visible ink dimensions/offsets are in layout-specs.json. Center horizontally; top is measured from the print-canvas origin. The editor's 12 × 16 layer dimensions include padding and are not the ink footprint.

Local layouts reuse the round04 provisional geometry. Neither a selected size button nor the generic mockup proves the photographed shirt's size. S/L/2XL checks use supplier dimensions and the fixed-print inference; they do not establish worn drape or exact physical neckline offsets. Provider previews are inspected for collar clearance, vertical balance, clipping and contrast; they are not samples.

## File quality limits

Native artwork effective PPI is measured from alpha≥16 visible bounds and exceeds 150 for all selected footprints. Exports embed sRGB and preserve aspect ratio. Original generated alpha is preserved. Masters contain near-opaque ink and partial-alpha edge/distress pixels; the complete alpha distribution is recorded separately. The green editor quality badge is only a raster-resolution/upload check. Sample print fidelity and any necessary opacity preparation remain distinct from garment/color/scale acceptance.
