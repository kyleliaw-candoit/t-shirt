---
title: TRACE-PILOT-001 — Broad Bestseller Scan and Method Calibration
owner: Creative Director
status: Complete — revise and retest
pilot_id: TRACE-PILOT-001
methodology_version: TRACE v0.2
methodology_frozen_commit: c383e2d90619e594b38b65dbd3508638d6e845d0
started: 2026-09-25
completed: 2026-09-25
last_updated: 2026-09-25
final_recommendation: REVISE-AND-RETEST
---

# TRACE-PILOT-001

## Purpose

Execute the first calibration pilot of the [TRACE Bestseller Creative Intelligence Methodology](../../../company/TRACE-Bestseller-Creative-Intelligence-Methodology.md).

This record must preserve the distinction between:

- the methodology frozen before source selection;
- observed marketplace evidence;
- analyst interpretation;
- proposed methodology changes arising from execution.

## Frozen methodology anchor

TRACE v0.2 was committed before any pilot source selection:

- Commit: `c383e2d90619e594b38b65dbd3508638d6e845d0`
- Date: 2026-09-25
- Branch: `docs/trace-bestseller-recipe-method`

Later edits must not imply that revised rules governed the original scan.

## Preregistered sample

Target 36 eligible design families:

- 12 Amazon;
- 12 Etsy;
- 12 Shopify/DTC.

No target-niche searches are permitted during initial discovery.

Do not backfill an incomplete platform stratum from another platform.

## Result

| Platform | Target families | Selected at execution | Final qualifying | Status |
|---|---:|---:|---:|---|
| Amazon | 12 | 0 | 0 | `BLOCKED` — complete ranked pools were inaccessible |
| Etsy | 12 | 12 | 1 | `PARTIAL-AFTER-AUDIT` — eleven selected expressions were provenance-quarantined |
| Shopify/DTC | 12 | 10 | 4 | `PARTIAL-AFTER-AUDIT` — four selected expressions were provenance-quarantined, two were brand-excluded, and two locked stores had already failed |
| **Total** | **36** | **22** | **5** | **Partial pilot sample** |

No failed or audit-removed quota was backfilled. Final QA found 17 execution-time Gate 0 failures—15 unresolved expression-origin or artwork-provenance conflicts and two DTC brand exclusions—and removed them from all recipe, grammar, and maturity support. This is a contamination screen, not an infringement finding. No known third-party franchise, celebrity, sports, unresolved repeated expression, or brand-dependent source supports any surviving candidate finding.

## Pilot artifacts

1. [Etsy scan and Source Decode Cards](./TRACE-PILOT-001-Etsy-Scan-and-Decodes.md)
2. [Etsy raw scan register](./TRACE-PILOT-001-Etsy-Scan-Register.csv)
3. [Shopify/DTC scan, raw ranked pools, and Source Decode Cards](./TRACE-PILOT-001-Shopify-DTC-Scan-and-Decodes.md)
4. [Recipe synthesis and transfer test](./TRACE-PILOT-001-Recipe-Synthesis-and-Transfer-Test.md)
5. [Execution log, friction register, debrief, and v0.3 change map](./TRACE-PILOT-001-Execution-Log-and-Debrief.md)

## Final state

- Methodology frozen before selection: complete
- Platform scans: complete at 22 execution selections and 5/36 final qualifying families, with shortfalls preserved
- Source decoding: complete for 5 final eligible families; 17 removed selections remain as audit records only
- Recipe clustering: complete
- Recipe outcome: zero `CORROBORATED` and zero `PROVISIONALLY-CORROBORATED` recipes; Concrete Semantic Resolution remains a `CANDIDATE` on one eligible support (`TRACE-P001-DTC-07`)
- Transfer/originality stress test: three active noncommercial diagnostics and three active originality comparisons for the candidate recipe; six earlier diagnostics retained only as Gate-0-invalidated audit records
- Debrief and v0.3 recommendation: complete
- Final recommendation: `REVISE-AND-RETEST`

The pilot supports methodology calibration and candidate-recipe learning from the accessible sample. It does not support a claim of comprehensive cross-platform coverage, Amazon prevalence, causal explanation, or production/legal clearance.

## Execution integrity rule

If live marketplace access, personalization, dynamic rendering, unavailable ranks, review pooling, or other platform behavior prevents the preregistered procedure from being completed, record the limitation. Do not fabricate evidence, silently substitute a different procedure, or select preferred designs by taste.
