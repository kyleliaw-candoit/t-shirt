---
title: TRACE-PILOT-001 — Etsy + Shopify/DTC Recipe Synthesis and Transfer Stress Test
status: Complete — strict provenance re-audit; limited noncommercial diagnostic
owner: Creative Director
pilot_id: TRACE-PILOT-001
methodology_version: TRACE v0.2
methodology_frozen_commit: c383e2d90619e594b38b65dbd3508638d6e845d0
date: 2026-09-25
source_families: 5
selected_at_execution_families: 22
post_selection_audit_reclassifications: 17
ip_quarantine_families: 15
brand_excluded_families: 2
---

# TRACE-PILOT-001 — Etsy + Shopify/DTC Recipe Synthesis and Transfer Stress Test

## Scope and controls

This synthesis uses only:

- 1 synthesis-eligible Etsy family from [Etsy Scan and Source Decodes](./TRACE-PILOT-001-Etsy-Scan-and-Decodes.md) and the [Etsy Scan Register](./TRACE-PILOT-001-Etsy-Scan-Register.csv), plus 11 selected-at-execution families retained only as final `IP-QUARANTINE` audit records;
- 4 synthesis-eligible Shopify/DTC families from [Shopify/DTC Scan and Source Decodes](./TRACE-PILOT-001-Shopify-DTC-Scan-and-Decodes.md), plus 4 selected-at-execution families retained only as final `IP-QUARANTINE` audit records and 2 retained only as final `BRAND-EXCLUDED` audit records;
- the rules frozen in TRACE v0.2 at commit `c383e2d90619e594b38b65dbd3508638d6e845d0`.

The execution selected 22 families before the strict frozen-v0.2 provenance re-audit: 12 Etsy and 10 Shopify/DTC. Final Gate 0 disposition leaves only 5 synthesis-eligible families: `TRACE-P001-ETSY-12`, `TRACE-P001-DTC-01`, `TRACE-P001-DTC-03`, `TRACE-P001-DTC-06`, and `TRACE-P001-DTC-07`. Fifteen families are final `IP-QUARANTINE`, and two are final `BRAND-EXCLUDED`. Quarantine records uncertainty and is not a finding of infringement.

The source set is incomplete relative to the preregistered 36-family pilot: no Amazon families are included, and the Shopify/DTC stratum produced 10 selected-at-execution rather than 12. No conclusion below should be described as full-pilot or three-platform recurrence.

Etsy and DTC demand evidence is not directly comparable. Etsy sources are recent platform-badged observations; DTC sources are lifetime within-store sales-order observations. Recipe maturity records independent mechanism support, not causal proof that the mechanism drove sales.

The frozen maturity rules applied here are:

| State | TRACE v0.2 requirement |
|---|---|
| `CANDIDATE` | Extracted from one eligible design family |
| `REPEATED-EXPRESSION` | Clones or trivial template swaps exist; spread/saturation evidence, not corroboration |
| `PROVISIONALLY-CORROBORATED` | At least two non-derivative mechanism analogues from unrelated niches and independent sellers |
| `CORROBORATED` | At least three non-derivative families across at least two unrelated niches and two independent sellers |
| `INTERNALLY-TESTED` | One original instantiation received a predeclared behavioral test |
| `REPLICATED` | At least two materially different original concepts or niche-truth inputs show the relevant behavior |

Nine historical concept seeds are preserved below. Only `TRACE-P001-XFR-04` through `TRACE-P001-XFR-06` remain active noncommercial transfer/originality diagnostics; the other six are invalidated by final Gate 0 source disposition and remain audit records only. None is a behavioral test, so no recipe becomes `INTERNALLY-TESTED` or `REPLICATED`.

## Family-level clustering

| Source family | Primary mechanism cluster | Synthesis treatment | Independence, derivative, or grammar note |
|---|---|---|---|
| `TRACE-P001-ETSY-01` — Salty Girl | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-02` — Three Raccoons | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-03` — Huzzah Frog | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-04` — Mitochondria | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-05` — Gangster Cats | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Unresolved artwork origin/template relationship; no recipe or grammar support |
| `TRACE-P001-ETSY-06` — Rock Star Cat | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-07` — Fighting Leopards | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-08` — Poker Cats | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Unresolved origin and relationship with `TRACE-P001-ETSY-05`; no recipe or grammar support |
| `TRACE-P001-ETSY-09` — Everything Is Temporary | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-10` — Wife’s Choices | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-11` — Boho Sun | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-ETSY-12` — ART | Form enacts proposition | `CANDIDATE` | Sole eligible Etsy source; one-family mechanism only |
| `TRACE-P001-DTC-01` — Ban the Fascists / Save the Books | Two-imperative moral compression | `CANDIDATE` | One eligible family; current political salience remains a major confounder |
| `TRACE-P001-DTC-02` — You Make Me Feel Alive | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-DTC-03` — Lunar Canyon | Terrestrial-path-to-cosmic-scale fusion | `CANDIDATE` | One eligible family; aesthetic-art demand remains a strong alternative |
| `TRACE-P001-DTC-04` — F Bombs | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-DTC-05` — Ninja Disguise | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |
| `TRACE-P001-DTC-06` — Coastal Waves | Natural-force trait metaphor | `CANDIDATE` | One eligible family; front-hit/back-poster grammar recurs, but the semantic mechanism does not |
| `TRACE-P001-DTC-07` — Puff Puff Pass | R2 — Concrete semantic resolution | `CANDIDATE` | Sole eligible family for the mechanism; same-titled raw-rank-5 product remains one family |
| `TRACE-P001-DTC-08` — Blue Marlin | Not synthesized | Ineligible audit record — final `BRAND-EXCLUDED` | House-brand dependence prevents concept or grammar support |
| `TRACE-P001-DTC-09` — Built for the Salt | Not synthesized | Ineligible audit record — final `BRAND-EXCLUDED` | Visually dominant house brand prevents concept or grammar support |
| `TRACE-P001-DTC-10` — Out of Breath Hiking Society | Not synthesized | Ineligible audit record — final `IP-QUARANTINE` | Strict provenance re-audit did not clear the source for synthesis; no recipe or grammar support |

Accounting: five eligible families each supply one-family `CANDIDATE` mechanisms. Fifteen additional selected-at-execution families are final `IP-QUARANTINE`, and two are final `BRAND-EXCLUDED`; all 17 are audit records only and supply no concept, grammar, or maturity support. Total: 5 synthesis-eligible families plus 17 post-selection audit reclassifications.

## Duplicate, derivative, and template controls

| Relationship | Finding | Maturity treatment |
|---|---|---|
| Etsy repeat appearances and same-print garment variants | Exact listing IDs recur across query/sort scans; variants are already collapsed | Audit lineage only; duplicate handling does not restore Gate 0 eligibility |
| `TRACE-P001-DTC-05` youth version | Same print reappears at raw rank 3 | Final `IP-QUARANTINE`; audit relationship only |
| `TRACE-P001-DTC-07` second same-titled product | Likely same family, with artwork verification still pending | Conservatively one eligible family |
| `TRACE-P001-ETSY-05` ↔ `TRACE-P001-ETSY-08` | Similar cat ensemble, central smoking figure, dark photographic treatment, adjacent human-social archetypes, and unresolved artwork origin | Both are final `IP-QUARANTINE` audit records; preserve the relationship for audit only, with no recipe, maturity, or grammar support |
| `TRACE-P001-DTC-06` ↔ `TRACE-P001-DTC-07` | Small front mark plus large back coastal poster recurs among the eligible families | Apparel-grammar convergence only; no distinctive shared sentence scaffold or demonstrated copied family |
| `TRACE-P001-DTC-08` and `TRACE-P001-DTC-09` | Both were selected at execution before final house-brand-dependency review | Final `BRAND-EXCLUDED` audit records; no recipe, maturity, or grammar support |
| Final Gate 0 provenance audit | Etsy 01–11 and DTC 02, 04, 05, and 10 did not clear strict provenance review | Final `IP-QUARANTINE`; earlier decodes and relationships are historical audit records, not synthesis inputs |
| Cross-platform copying | None demonstrated in the supplied records | No copied design is counted as cross-platform support |

## Apparel-grammar findings kept separate from recipes

The grammar IDs below remain stable join keys. `Joined eligible source families` includes only the five final Gate 0-eligible records. Withdrawn rows preserve the identifier but provide no active grammar evidence.

| Grammar ID | Grammar finding | Joined eligible source families | Treatment |
|---|---|---|---|
| `TRACE-P001-AGR-01` | Small front hit plus large back poster | `TRACE-P001-DTC-06`, `TRACE-P001-DTC-07` | Active two-family DTC grammar observation only; exact compositions, palettes, and source scenes remain prohibited |
| `TRACE-P001-AGR-02` | Retro institutional, civic, academic, or club badge | `TRACE-P001-DTC-01` | Active one-family grammar finding; retain for later recurrence checks, not as a recipe |
| `TRACE-P001-AGR-03` | Large no-text dramatic tableau | `TRACE-P001-DTC-03` | Active one-family grammar finding; retain for later recurrence checks, not as a recipe |
| `TRACE-P001-AGR-04` | Centered single icon with strong negative space | — | `WITHDRAWN-AUDIT-ONLY`; no eligible source support remains |
| `TRACE-P001-AGR-05` | Oversized manipulated word used as the graphic | `TRACE-P001-ETSY-12` | One-family grammar finding; semantic mechanism remains separately classified |
| `TRACE-P001-AGR-06` | Compact stacked type-led fast read | — | `WITHDRAWN-AUDIT-ONLY`; no eligible source support remains |

Only `TRACE-P001-AGR-01`, `TRACE-P001-AGR-02`, `TRACE-P001-AGR-03`, and `TRACE-P001-AGR-05` remain active findings. They describe presentation architecture only and do not increase concept-recipe maturity.

## Unpromoted recipe clusters

| Candidate | Support | Exact maturity | Decision |
|---|---|---|---|
| Form enacts proposition | `TRACE-P001-ETSY-12` | `CANDIDATE` | One eligible family remains after provenance audit; style may explain demand |
| Two-imperative moral compression | `TRACE-P001-DTC-01` | `CANDIDATE` | Retain; current political salience is a major confounder |
| Terrestrial path fused with impossible scale | `TRACE-P001-DTC-03` | `CANDIDATE` | Retain; aesthetic demand may dominate |
| Natural force embodies a desired trait | `TRACE-P001-DTC-06` | `CANDIDATE` | Retain; premium garment and brand effects are substantial |
| Concrete semantic resolution | `TRACE-P001-DTC-07` | `CANDIDATE` | One eligible family remains after provenance audit; no cross-platform recurrence is claimed |

# Recipe definitions and audit dispositions

## `TRACE-P001-CR-01 v0.1` — Owned-Friction Reversal — `WITHDRAWN-AUDIT-ONLY`

> Given a recognizable judgment, limitation, or rule that could lower the wearer’s status, make the wearer voluntarily become its final referent, then reclassify that exposure as evidence of belonging, affection, honest competence, or agency.

Final disposition: withdrawn from the active recipe library. The definition below is retained only to preserve pilot lineage; it has no active maturity state after Gate 0 re-audit.

### Mechanism fingerprint

| Field | Definition |
|---|---|
| Familiar frame | A criticism, limitation, or evaluative rule |
| Operation | Self-reference followed by evaluative reversal |
| Tension | Exposure or diminished status versus voluntary ownership |
| Reveal | The wearer becomes the relevant example and changes what that fact means |
| Payoff | Self-recognition, defiant warmth, solidarity, or affectionate self-deprecation |

### Ingredients

**Required**

- An independently documented friction, limitation, or evaluative rule.
- A voluntary self-reference; the target cannot merely be mocked from outside.
- A real evaluative turn that creates dignity, belonging, affection, or competence.
- Respect for the target truth; the recipe cannot pretend genuine harm is desirable.

**Tunable**

- First-person, collective, or implicit voice.
- Direct statement, label, credential, or visual reclassification.
- Dry, warm, defiant, or affectionate tone.
- Text-led or image-supported execution.

**Optional**

- One compact contextual symbol.
- A two-beat setup/reveal.
- Understatement or mild exaggeration.

**Anti-ingredients**

- Generic “chaos” language without a documented truth.
- Ridicule directed at someone other than the consenting wearer.
- A noun swap into a faux club or society.
- A confession with no evaluative reversal.
- Any source sentence scaffold, punchline logic, or recognizable composition.

### Wearability and failure conditions

The reversal should parse in no more than two beats, with one dominant anchor. A long explanation, a list requiring close reading, or an insult that remains an insult fails the recipe. A concept also fails if the claimed friction is not independently documented.

### Source support and maturity

Former lineage, now invalidated:

- `TRACE-P001-ETSY-01` — final `IP-QUARANTINE`.
- `TRACE-P001-ETSY-10` — final `IP-QUARANTINE`.
- `TRACE-P001-DTC-10` — final `IP-QUARANTINE`.

The strict frozen-v0.2 provenance re-audit leaves zero eligible supporting families. The earlier `CORROBORATED` conclusion is retracted; `TRACE-P001-CR-01 v0.1` is an audit record only, and `TRACE-P001-XFR-01` through `TRACE-P001-XFR-03` are invalidated Gate 0 diagnostics.

### Historical source carryover prohibitions

- The flavor accusation, `SALTY` reveal, raincoat, umbrella, rain scene, and `TRACE-P001-ETSY-01` hierarchy.
- The wife’s-choice sentence, logical path, punchline, and stacked quote treatment.
- `OUT OF BREATH`, `HIKING SOCIETY`, the delayed-arrival punchline, and `TRACE-P001-DTC-10` badge composition.

### Saturation and test history

Self-deprecation, faux clubs, and identity badges are crowded. A generic “___ Society” noun swap should be rejected even when the abstract reframe is valid.

Internal behavioral test history: none.

## `TRACE-P001-CR-02 v0.1` — Concrete Semantic Resolution — `CANDIDATE`

> Given a familiar expression or abstract relation whose key idea supports a concrete physical reading, choose a target whose documented property can enact that reading, then let the image supply the second meaning without explaining the joke.

### Mechanism fingerprint

| Field | Definition |
|---|---|
| Familiar frame | An idiom, euphemism, phrase, or abstract relationship |
| Operation | Literalization or physical embodiment of its key term |
| Tension | Expected figurative meaning versus a surprising concrete reading |
| Reveal | The target’s real property or action performs the second meaning |
| Payoff | Fast recognition, semantic satisfaction, or cheeky insider wit |

### Ingredients

**Required**

- A phrase or relationship with two genuinely resolvable readings.
- A target property independently grounded in the niche truth.
- An image that closes the semantic loop.
- Enough distance that the result is not a source phrase with a substituted noun.

**Tunable**

- Phrase-first or image-first reading order.
- Idiom, euphemism, procedural language, or borrowed system frame.
- Deadpan, tender, technical, or mischievous tone.

**Optional**

- Omission of the implied word.
- A single contradiction or impossible condition.
- One repeated glyph when it is necessary to the semantic resolution.

**Anti-ingredients**

- Arbitrary mascot substitution.
- A visual that merely illustrates the phrase literally without creating a second meaning.
- Explanatory copy required to understand the joke.
- Dependence on taboo content alone.
- Any supporting source’s phrase, subject/action pairing, or composition.

### Wearability and failure conditions

The figurative and concrete readings should resolve from one dominant image and a short verbal anchor, if text is needed at all. If a caption must explain why the image is clever, the recipe fails.

### Source support and maturity

- `TRACE-P001-DTC-07` — SeaMonkey Apparel; cannabis/coastal word embodiment.

Only one eligible family supports the mechanism, so the recipe is `CANDIDATE` under the frozen rule. No Etsy or Amazon recurrence is claimed.

`TRACE-P001-DTC-02` and `TRACE-P001-DTC-04`, the former additional inputs, are final `IP-QUARANTINE` and supply no definition, grammar, or maturity support.

### Prohibited source carryover

- The bomber, F-marked bombs, diagonal drop, source euphemism, and military treatment.
- `PUFF PUFF PASS`, pufferfish pairing, tropical scene, headline/mascot/footer layout, and palette.

The quarantined `TRACE-P001-DTC-02` and `TRACE-P001-DTC-04` source executions are not inputs and must not be used as generation references.

### Saturation and test history

Animal-name puns, taboo euphemisms, and obvious visual rebuses are highly saturated. The target property must do semantic work beyond a noun substitution.

Internal behavioral test history: none.

## `TRACE-P001-CR-03 v0.1` — Earned Archetype Recasting — `WITHDRAWN-AUDIT-ONLY`

> Given a modest or familiar subject whose documented behavior matches the functional traits of a dramatic or status-coded archetype, recast it into that role while retaining native evidence that lets the audience infer why the casting fits.

Final disposition: withdrawn from the active recipe library. The tightened definition below is retained only to preserve pilot lineage; it has no active maturity state after Gate 0 re-audit.

### Mechanism fingerprint

| Field | Definition |
|---|---|
| Familiar frame | A legible heroic, performance, expert, or high-drama archetype |
| Operation | Trait-grounded role recasting |
| Tension | Ordinary scale or status versus an outsized role |
| Reveal | Native behavior proves the casting is more than costume |
| Payoff | Affectionate grandeur, competence recognition, absurd swagger, or courage |

### Ingredients

**Required**

- An independently documented target trait.
- A generic archetype with at least two functional correspondences to that trait.
- Native target cues retained inside the recast.
- A mismatch that creates recognition rather than random novelty.

**Tunable**

- Solo versus ensemble.
- Cute, epic, deadpan, or technically competent tone.
- Text-free scene or one compact authenticating utterance.
- Degree of visual grandeur.

**Optional**

- One archetype-specific prop.
- A scale contrast.
- A restrained environment cue.

**Anti-ingredients**

- Costume-only mashups.
- Famous characters, celebrities, bands, teams, or protected worlds.
- A source animal, role, pose, prop set, or composition.
- Mockery that erases the target’s genuine competence.
- Generic “epic” styling without a documented trait match.

### Wearability and failure conditions

One archetype and one to three native target cues should carry the concept. An encyclopedic scene, unexplained costume, or dependence on a famous reference fails.

### Source support and maturity

Former candidate lineage, now invalidated:

- `TRACE-P001-ETSY-02` — final `IP-QUARANTINE`.
- `TRACE-P001-ETSY-03` — final `IP-QUARANTINE`.
- `TRACE-P001-ETSY-06` — final `IP-QUARANTINE`.

Even before the provenance re-audit, these families established only broad, saturated animal/archetype recasting, not the tightened recipe's defining two-correspondence and native-evidence constraint. Final Gate 0 disposition now leaves zero eligible inputs. The prior `CANDIDATE` disposition is withdrawn, and `TRACE-P001-CR-03 v0.1` remains an audit record only.

`TRACE-P001-XFR-07` through `TRACE-P001-XFR-09` are invalidated Gate 0 diagnostics. They may be read only as historical probes of the tightened hypothesis and do not add external corroboration.

### Historical source carryover prohibitions

- The three-raccoon cast, full moon, triangular montage, poses, and photographic assets.
- The frog, sword, cape, `HUZZAH`, pose, embroidery treatment, and placement.
- The cat/electric-guitar pairing, pose, eye treatment, frame, and distressed illustration.

### Saturation and test history

Animals acting like humans are broadly saturated. The recipe should survive without an animal subject and without a famous archetype reference; otherwise it has not been abstracted far enough.

Internal behavioral test history: none.

# Target-truth panel — procedural lock

The panel was prepared independently in a separate workstream before final recipe synthesis. The pilot record does not contain an independently timestamped panel lock that proves it preceded clustering, however. The ordering claim is therefore procedural and qualified: separate-workstream preparation supports independence, but does not guarantee or independently audit temporal precedence.

| Truth ID | Canonical source anchor | Verified blob |
|---|---|---|
| `NT-R010-01-ROLE-COLLISION` | [R010 §3.1](../../../Researches/R010-Remote-Working-Parents.md#31-role-collision) | `63ddb200a51f7c60ad4844317f80fb227662e362` |
| `NT-R021-01-DELAYED-OUTCOME-RISK` | [R021 §4.3](../../../Researches/R021-Pottery-Ceramics-Makers.md#43-uncertainty-and-kiln-outcomes) | `c1ffb071db60d3dfee079a6f431bbfbdae518a0e` |
| `NT-R027-03-LAYERED-DISCOVERY` | [R027 §4.3](../../../Researches/R027-Old-House-Restorers-Historic-Home-People.md#43-discovery-and-the-house-archaeology-reward) | `504d9bec9a3787e480764558b7f29d7615cea0af` |

For the nine historical diagnostics, the independent-truth check is `PROCEDURALLY-SUPPORTED / NOT INDEPENDENTLY TIME-AUDITED`. It is not conclusive proof that recipe clustering could not have influenced panel selection, and it does not cure an ineligible source lineage. Only `TRACE-P001-XFR-04` through `TRACE-P001-XFR-06` remain active after Gate 0 re-audit.

# Transfer and originality stress test

## Recipe 1 — Owned-Friction Reversal (`WITHDRAWN-AUDIT-ONLY`)

| Transfer-test ID | Recipe ID | Truth ID | Noncommercial diagnostic concept seed | T-shirt-fit gate | Originality disposition | Result |
|---|---|---|---|---|---|---|
| `TRACE-P001-XFR-01` | `TRACE-P001-CR-01 v0.1` | `NT-R010-01-ROLE-COLLISION` | An organizational roster in which one central nameplate spans several work-and-care departments. The evaluative turn treats repeated switching as honest cross-functional capability without pretending overload is desirable. | Conditional pass: compress to one anchor and a few role cues; the complete six-role list would become chart-like. | Historical distance record only; parent recipe has no eligible source support. | `INVALIDATED-GATE0`; audit record only |
| `TRACE-P001-XFR-02` | `TRACE-P001-CR-01 v0.1` | `NT-R021-01-DELAYED-OUTCOME-RISK` | A signed maker process record in which every controllable step is complete while the final result remains explicitly unknown. Accepting that uncertainty becomes evidence of mature practice rather than a failure joke. | Pass if the record reduces to one status line and a short process sequence. | Historical distance record only; parent recipe has no eligible source support. | `INVALIDATED-GATE0`; audit record only |
| `TRACE-P001-XFR-03` | `TRACE-P001-CR-01 v0.1` | `NT-R027-03-LAYERED-DISCOVERY` | A wall or floor cross-section presented as a steward’s field log. Visibly unfinished layers become evidence being read rather than a shameful unfinished-home condition. | Conditional pass: use one cross-section and minimal labels. | Historical distance record only; parent recipe has no eligible source support. | `INVALIDATED-GATE0`; audit record only |

**Historical rejection probe:** “Out of Breath Pottery Society” or an equivalent niche swap into the quarantined `TRACE-P001-DTC-10` sentence-and-badge scaffold must be rejected. The probe is retained for audit only; it is not an active recipe instantiation.

## Recipe 2 — Concrete Semantic Resolution (`CANDIDATE`)

| Transfer-test ID | Recipe ID | Truth ID | Noncommercial diagnostic concept seed | T-shirt-fit gate | Originality disposition | Result |
|---|---|---|---|---|---|---|
| `TRACE-P001-XFR-04` | `TRACE-P001-CR-02 v0.1` | `NT-R010-01-ROLE-COLLISION` | One physical ID-badge holder is forced to contain two active role cards at once, making “role collision” concrete without depicting generic household chaos. | Pass: one object, two labels, immediate collision. | Diagnostic distance retained; final copy, styling, and overall-impression checks remain open. | `ACTIVE-NONCOMMERCIAL-DIAGNOSTIC` |
| `TRACE-P001-XFR-05` | `TRACE-P001-CR-02 v0.1` | `NT-R021-01-DELAYED-OUTCOME-RISK` | A kiln door behaves as a speech bubble or editorial mark applying the “final say” to otherwise finished vessels, making the kiln’s outcome-changing role visible. Wording remains placeholder, not final copy. | Pass if limited to one kiln, a short vessel row, and one dominant mark. | Diagnostic distance retained; final copy, styling, and overall-impression checks remain open. | `ACTIVE-NONCOMMERCIAL-DIAGNOSTIC` |
| `TRACE-P001-XFR-06` | `TRACE-P001-CR-02 v0.1` | `NT-R027-03-LAYERED-DISCOVERY` | A wall/floor cutaway is treated as an archaeological stratigraphy panel, with later layers above original fabric and neutral catalog markers. | Conditional pass: no more than a few distinct layers; avoid dense archival annotation. | Diagnostic distance retained; final copy, styling, and overall-impression checks remain open. | `ACTIVE-NONCOMMERCIAL-DIAGNOSTIC` |

**Rejection probe:** Any `PUFF PUFF [new noun]` construction or F-marked substitute objects must be rejected as source drift. The quarantined `TRACE-P001-DTC-02` and `TRACE-P001-DTC-04` families are not inputs.

## Recipe 3 — Earned Archetype Recasting (`WITHDRAWN-AUDIT-ONLY`)

| Transfer-test ID | Recipe ID | Truth ID | Noncommercial diagnostic concept seed | T-shirt-fit gate | Originality disposition | Result |
|---|---|---|---|---|---|---|
| `TRACE-P001-XFR-07` | `TRACE-P001-CR-03 v0.1` | `NT-R010-01-ROLE-COLLISION` | Cast the role-switching parent as a stage manager coordinating simultaneous cues. Calendar handoff, work call, meal, and pickup signals establish why the casting fits; no costume-only heroism. | Pass with a single figure and three cues. | Historical distance record only; parent recipe has no eligible source support. | `INVALIDATED-GATE0`; audit record only |
| `TRACE-P001-XFR-08` | `TRACE-P001-CR-03 v0.1` | `NT-R021-01-DELAYED-OUTCOME-RISK` | Cast the potter awaiting a closed kiln as a generic launch director awaiting telemetry. Test tile, firing cone, and kiln indicators supply native evidence; no real space-agency marks. | Pass if the scene is reduced to one controller, one kiln indicator, and one native ceramic cue. | Historical distance record only; parent recipe has no eligible source support. | `INVALIDATED-GATE0`; audit record only |
| `TRACE-P001-XFR-09` | `TRACE-P001-CR-03 v0.1` | `NT-R027-03-LAYERED-DISCOVERY` | Cast the old-house steward as a forensic conservator reading building evidence. Saved hardware, one labeled layer, and a historic plan establish the functional match. | Conditional pass: retain only the evidence needed to communicate the role. | Historical distance record only; parent recipe has no eligible source support. | `INVALIDATED-GATE0`; audit record only |

**Historical rejection probe:** A frog with a restoration tool and period cheer, three target mascots before a full moon, or a target animal holding an electric guitar must be rejected. The probe is retained for audit only; each expression keeps a distinctive element from quarantined lineage rather than only the abstract operation.

## Source-by-dimension originality audit

The matrix preserves all 27 historical source-by-seed comparisons for audit lineage. Final Gate 0 disposition leaves only 3 active required comparisons: `TRACE-P001-XFR-04` through `TRACE-P001-XFR-06`, each compared with eligible source `TRACE-P001-DTC-07`. The other 24 comparisons are invalidated and cannot support a recipe, grammar finding, transfer claim, or maturity decision.

| Transfer-test set | Compared family set | Historical comparisons | Final status |
|---|---|---:|---|
| `TRACE-P001-XFR-01..03` | `TRACE-P001-ETSY-01`, `TRACE-P001-ETSY-10`, `TRACE-P001-DTC-10` | 9 | `INVALIDATED-GATE0`; every compared source is final `IP-QUARANTINE` |
| `TRACE-P001-XFR-04..06` | `TRACE-P001-DTC-02`, `TRACE-P001-DTC-04` | 6 | `INVALIDATED-GATE0`; every compared source is final `IP-QUARANTINE` |
| `TRACE-P001-XFR-04..06` | `TRACE-P001-DTC-07` | 3 | `ACTIVE-NONCOMMERCIAL-DIAGNOSTIC`; only active required comparisons |
| `TRACE-P001-XFR-07..09` | `TRACE-P001-ETSY-02`, `TRACE-P001-ETSY-03`, `TRACE-P001-ETSY-06` | 9 | `INVALIDATED-GATE0`; every compared source is final `IP-QUARANTINE` |

Dimension codes follow the eight-part originality gate frozen in TRACE v0.2. Values on invalidated rows are retained historical observations only.

| Code | Meaning |
|---|---|
| `D` | Described seed is materially different from the source at this concrete-expression dimension |
| `M` | Only the abstract recipe mechanism overlaps; no source-specific setup/reveal expression is described as retained |
| `P` | Provisional: the seed does not yet instantiate final copy, typography/styling, or a finished overall impression, so this dimension must be rerun |
| `X` | Unresolved source-specific overlap; reject or redesign before proceeding |

Dimension columns: `W` = wording and syntax; `S` = subject and prop; `I` = scenario and insider truth; `R` = setup/reveal relationship; `V` = visual metaphor; `C` = pose and composition; `T` = typography and styling; `O` = overall commercial impression.

| Transfer-test ID | Historical compared source/input family | W | S | I | R | V | C | T | O |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `TRACE-P001-XFR-01` | `TRACE-P001-ETSY-01` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-01` | `TRACE-P001-ETSY-10` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-01` | `TRACE-P001-DTC-10` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-02` | `TRACE-P001-ETSY-01` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-02` | `TRACE-P001-ETSY-10` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-02` | `TRACE-P001-DTC-10` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-03` | `TRACE-P001-ETSY-01` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-03` | `TRACE-P001-ETSY-10` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-03` | `TRACE-P001-DTC-10` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-04` | `TRACE-P001-DTC-02` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-04` | `TRACE-P001-DTC-04` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-04` | `TRACE-P001-DTC-07` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-05` | `TRACE-P001-DTC-02` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-05` | `TRACE-P001-DTC-04` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-05` | `TRACE-P001-DTC-07` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-06` | `TRACE-P001-DTC-02` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-06` | `TRACE-P001-DTC-04` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-06` | `TRACE-P001-DTC-07` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-07` | `TRACE-P001-ETSY-02` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-07` | `TRACE-P001-ETSY-03` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-07` | `TRACE-P001-ETSY-06` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-08` | `TRACE-P001-ETSY-02` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-08` | `TRACE-P001-ETSY-03` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-08` | `TRACE-P001-ETSY-06` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-09` | `TRACE-P001-ETSY-02` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-09` | `TRACE-P001-ETSY-03` | P | D | D | M | D | D | P | P |
| `TRACE-P001-XFR-09` | `TRACE-P001-ETSY-06` | P | D | D | M | D | D | P | P |

None of the three active comparison rows contains an `X` at the seed-description level. That is a narrow diagnostic finding, not an eight-dimension pass: wording/syntax, typography/styling, and overall commercial impression remain `P` until final executions exist, and the setup/reveal relationship deliberately retains only the abstract mechanism (`M`). The independent-truth evidence is also procedural and not independently time-audited. Values on the 24 invalidated comparisons have no active evidentiary effect.

Accordingly, only `TRACE-P001-XFR-04`, `TRACE-P001-XFR-05`, and `TRACE-P001-XFR-06` remain active noncommercial diagnostics. The other six transfer tests are invalidated audit records. Nothing here is production-cleared, behaviorally validated, or legally cleared. Exact-phrase and close-variant marketplace/web searches, appropriate trademark checks, artwork-provenance review, and a fresh eight-dimension comparison against every eligible supporting source remain mandatory for any final concept. No source artwork should be supplied as a generation reference.

# Promotion decision

Promote zero recipes to `CORROBORATED` and zero recipes to `PROVISIONALLY-CORROBORATED`.

Retain `TRACE-P001-CR-02 v0.1` — Concrete Semantic Resolution — at `CANDIDATE`, supported by the sole eligible family `TRACE-P001-DTC-07`.

Withdraw `TRACE-P001-CR-01 v0.1` and `TRACE-P001-CR-03 v0.1` from the active recipe library because each has zero eligible supporting families. Preserve both as `WITHDRAWN-AUDIT-ONLY` records, along with their six invalidated transfer tests.

Retain Form Enacts Proposition, Two-Imperative Moral Compression, Terrestrial-Path-to-Cosmic-Scale Fusion, and Natural-Force Trait Metaphor at `CANDIDATE`, each with one eligible family. Together with Concrete Semantic Resolution, the pilot therefore retains five one-family candidates. Retain the four active eligible-source apparel-grammar findings separately from concept recipes.

The final evidence base is 5 eligible families, all but one from DTC. No recipe has Amazon support, causal validation, a predeclared behavioral test, internal validation, or replication.
