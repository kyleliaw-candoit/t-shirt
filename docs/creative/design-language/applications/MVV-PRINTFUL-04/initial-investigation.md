# MVV production-quality repair investigation

October 23, 2026. All ten designs were approved and PR142 merged. Approval of creative designs is preserved; no approved artwork has been replaced.

## Audit

See source-audit.json. Nine enlarged designs have native resolution below 150 PPI at the approved widths; Type-Led-4 is approximately 105 PPI at 10.5 inches. Partial-alpha percentages count all nonzero pixels below alpha 250 and include antialiasing; this is a screening measure, not proof that every counted pixel is a print defect. C3B already exceeds 150 PPI for its original graphic and caption.

## Restoration trial — rejected before founder feedback

Built-in image generation was asked to restore Type-Led-4 faithfully, with about 3200 visible pixels across, opaque ink and transparent exterior. The output was only 1213 × 1296 pixels with 1116 visible pixels across (106.29 PPI at 10.5 inches). Partial alpha fell from about 50.14% to 24.20%, but lettering shapes, spacing and ink appearance changed. It therefore fails resolution and strict fidelity acceptance. It must not replace the approved master or be described as production-ready. Repeating this approach across all nine designs is not justified by this trial.

## Recommended next execution

For flat lettering/linework: controlled vector reconstruction, visually checked against the approved original. For textured illustrations: a dedicated high-resolution restoration/upscaling workflow with comparison at final print size; do not promise recovered original detail or treat new pixels as proof of quality. Maintain exact approved dimensions/placement and verify opacity, small details and provider rendering. Physical samples remain a separate purchase decision.

Provider references checked October 23, 2026:
- https://help.printful.com/hc/en-us/articles/50264019148177-How-should-I-prepare-my-print-file-for-the-best-results
- https://help.printful.com/hc/en-us/articles/50264138559377-Is-there-a-difference-in-quality-between-150-and-300-DPI
- https://www.printful.com/transparency-in-dtg-files

Status: audit complete; attempted restoration rejected; production issue remains open. No new production files uploaded or storefront changes made.
