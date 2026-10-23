# MVV production-quality repair candidates

October 23, 2026 · Nine repaired candidates complete; independent digital review passed for provider/sample evaluation. Not yet provider-verified or physically sample-approved.

All ten creative designs remain Founder-approved. This round preserves their wording, composition, garment choice, colour and placement while creating separate repair candidates. C3B stays on its approved [round03 layout](../MVV-PRINTFUL-03/layouts/MVV3-C3B-above-12x16.png).

## What to review

1. [Type-Led-4 before/after](review/Type-Led-4-comparison.jpg): script fidelity and cleanup.
2. [Type-Led-3 before/after](review/Type-Led-3-comparison.jpg): retained distressed texture.
3. [All nine at shirt scale](review/whole-shirt-comparison.jpg) and [saved-export proof](review/export-proof.jpg).

The [independent assessment](repair-assessment.md) was recorded before Founder feedback and has a SHA-256 record. The [original failed generative trial](initial-investigation.md) is preserved.

| Design | Repair | Comparison | 300-PPI export |
|---|---|---|---|
| B2 | FSRCNN restoration | [Before/after](review/B2-comparison.jpg) | [PNG](layouts/MVV4-B2-300ppi.png) |
| A1 | FSRCNN restoration | [Before/after](review/A1-comparison.jpg) | [PNG](layouts/MVV4-A1-300ppi.png) |
| A3 | FSRCNN restoration | [Before/after](review/A3-comparison.jpg) | [PNG](layouts/MVV4-A3-300ppi.png) |
| YIF-M | FSRCNN restoration | [Before/after](review/YIF-M-comparison.jpg) | [PNG](layouts/MVV4-YIF-M-300ppi.png) |
| YIF-F | FSRCNN restoration | [Before/after](review/YIF-F-comparison.jpg) | [PNG](layouts/MVV4-YIF-F-300ppi.png) |
| C2 | FSRCNN restoration | [Before/after](review/C2-comparison.jpg) | [PNG](layouts/MVV4-C2-300ppi.png) |
| Fashion-1D-F | Vector contours | [Before/after](review/Fashion-1D-F-comparison.jpg) | [PNG](layouts/MVV4-Fashion-1D-F-300ppi.png) |
| Type-Led-3 | Vector contours | [Before/after](review/Type-Led-3-comparison.jpg) | [PNG](layouts/MVV4-Type-Led-3-300ppi.png) |
| Type-Led-4 | Vector contours | [Before/after](review/Type-Led-4-comparison.jpg) | [PNG](layouts/MVV4-Type-Led-4-300ppi.png) |

## Methods and honest limits

- Three typography/flat-art masters were traced into scalable, outlined vector paths with a 64-tone palette. The `.svgz` files in `vectors/` are gzip-compressed SVG, contain no embedded bitmaps, and need no installed fonts. Decompress with `gzip -dc file.svgz > file.svg` if an editor requires plain SVG. These are source-derived vector reconstructions, not newly invented lettering. Small distress paths are deliberately retained; files are more complex than clean logo vectors.
- Six textured illustrations use the bundled FSRCNN x4 model, blended 65% with learned reconstruction and 35% with bicubic rendering, then reduced to their final physical size. This is dedicated super-resolution processing, not only changing DPI metadata. It still cannot prove recovery of missing original detail.
- Alpha cleanup yields opaque ink / clear exterior. Near-opaque colour was matched to the approved Ivory reference. This does not create a background rectangle. Pale texture can print as pale ink and needs sample assessment.
- PNG exports use a 255-colour palette plus transparency. Quantization error is measured in repair-results.json; mean channel error on ink is under 1.5/255. No ICC or alpha is discarded.
- Actual visible bounds differ by less than 0.025 inch from the approved placement rectangles. Geometry, opacity, profile, vector structure and file hashes are checked in [validation.json](validation.json). Similarity metrics record fidelity, not proof of improved printed quality.

## Reproduce

```sh
python -m pip install -r requirements.txt
python repair.py --model models/FSRCNN_x4.pb
```

Run from this directory. The script locates approved source files relative to itself. Versions are pinned; model provenance, license and digest are in `models/`. Outputs are native scalable paths for three designs and reconstructed raster exports for six; original source PPI remains recorded in [repair-results.json](repair-results.json). Rendering libraries may produce byte differences across platforms; the committed hashes identify the reviewed files.

No new provider upload, sample purchase, storefront publication or merge is included in this checkpoint. Next: apply the selected repair files in Printful and inspect physical samples before production release.
