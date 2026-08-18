---
title: MVV-001 Landing Page Designer-Developer Workflow
brand: Worth the Detour
experiment_id: mvv-r012-001
status: Proposed
version: 0.2
last_updated: 2026-08-18
related_issue: 55
---

# MVV-001 Landing Page Designer-Developer Workflow

## Purpose

This document defines the collaboration loop for creating the customer-facing Worth the Detour MVV #1 landing page.

The objective is to let specialized AI roles collaborate without blurring decision rights:

- **Creative Director** owns visual / creative intent and acts as the landing-page UI / visual designer.
- **Project Manager / Technical Lead** translates approved cross-functional inputs into an implementation-ready brief, sequences the work, resolves handoffs, and protects MVV scope.
- **Codex / Front-End Implementation Engineer** acts as the UI developer: it implements the approved design in code but does not redefine the design, brand, product assortment, or experiment.
- **Brand Manager** reviews material brand fidelity.
- **Technical Reviewer** independently reviews implementation quality and technical risk.
- **Founder** retains final approval and merge authority.

GitHub is the canonical handoff layer. Important requirements, assets, implementation changes, review decisions, and issue status should be represented in GitHub rather than relying on one chat thread as the source of truth.

---

## 1. Core collaboration principle

> **Designer specifies intent and guardrails. Developer implements faithfully. The rendered page returns to the designer for visual review.**

The loop is:

**Creative Director specification / assets**

→ **Project Manager / Technical Lead implementation brief**

→ **Codex implementation**

→ **Reviewable rendered page / preview**

→ **Creative Director visual review**

→ **Codex revisions when required**

→ **Brand Manager + Technical Reviewer review**

→ **Founder approval / merge**

This is intentionally a loop rather than a one-way handoff. The rendered product may expose implementation issues that are not obvious from a written design specification.

---

## 2. Role boundaries

### Creative Director — UI / visual designer

Owns:

- product assortment from approved / locked designs;
- authoritative product and presentation assets;
- product-image / mockup standard;
- visual hierarchy and creative presentation intent;
- brand treatment and creative copy package within Brand Manager constraints;
- design-specific inspection needs;
- fair-comparison guardrails across products;
- material visual decisions that could affect product interpretation or experiment validity;
- review of the actual rendered page, especially mobile.

Does not own:

- HTML / CSS / JavaScript architecture;
- analytics implementation;
- deployment mechanics;
- technical accessibility implementation;
- Git / branching / PR mechanics;
- experiment strategy outside Creative Director scope.

### Project Manager / Technical Lead

Owns:

- Issue #55 as the working project checklist;
- confirming upstream canonical inputs are complete enough to begin implementation;
- translating Strategy Advisor, Brand Manager, Creative Director, and event-schema requirements into a concise implementation brief;
- separating design decisions from developer-discretion decisions;
- sequencing handoffs and reviews;
- surfacing unresolved ambiguity to the appropriate role / Founder;
- protecting earned complexity and MVV scope;
- deciding whether a requested change is a creative revision, technical implementation change, or experiment / brand decision;
- maintaining a clear record of blockers and decisions.

Does not replace the Creative Director's design authority or the Technical Reviewer's independent review.

### Codex — Front-End Implementation Engineer / UI developer

Owns:

- semantic HTML;
- CSS implementation;
- responsive / mobile behavior;
- JavaScript interactions;
- accessibility basics;
- implementation of approved inspection / detail behavior;
- CTA and form UI states;
- later, when specifically authorized, attribution, analytics, event instrumentation, and lead-capture implementation;
- implementation testing and self-review;
- exact diff review and clear reporting of assumptions / validation.

May make ordinary implementation-level decisions needed to make the approved design work across browsers and screen sizes.

Does **not** own:

- product assortment;
- locked artwork changes;
- brand positioning or messaging invention;
- experiment hypotheses;
- canonical ID changes;
- material visual reinterpretation;
- acquisition-creative selection;
- final merge / launch approval.

If an unspecified choice could materially affect brand presentation, product fairness, visual hierarchy, or experiment validity, Codex should **surface the ambiguity instead of silently deciding**.

### Brand Manager

Reviews the rendered page for material brand / message fidelity against canonical landing-page brand requirements and checklist. The Brand Manager should not use this review to override ordinary implementation or aesthetic decisions that fall within Creative Director / developer authority.

### Technical Reviewer

Independently reviews the actual implementation PR and canonical requirements. The Technical Reviewer evaluates correctness, responsive / accessibility basics, attribution / analytics integrity when applicable, privacy, deployment risk, failure modes, and unnecessary complexity.

### Founder

Makes final business / merge decisions after the relevant reviews. No AI role's recommendation alone authorizes merge.

---

## 3. Required Creative Director handoff

Before Phase A coding begins, the Creative Director should provide or approve enough of the following to prevent Codex from inventing material design choices:

1. **Assortment manifest**
   - included canonical `design_id` values;
   - authoritative locked sources;
   - product display names if applicable;
   - any holdouts / exclusions.

2. **Customer-facing product assets**
   - one approved primary product image per included design;
   - detail / inspection images only where they materially improve fair comprehension;
   - each primary product image must have passed the canonical `MVV-001-LP-Product-Image-Standard.md` review gate before it is treated as approved.

3. **Creative Presentation Specification**
   - intended product presentation;
   - hierarchy / emphasis;
   - mobile considerations where material;
   - inspection behavior where material;
   - fair-comparison guardrails;
   - design-specific caveats;
   - prohibited transformations.

4. **Minimum creative copy package**
   - brand treatment;
   - identity line;
   - category-decoding support where needed;
   - product / collection section language;
   - product display names;
   - necessary microcopy.

5. **Visual reference when layout intent matters**
   - preferably one mobile reference and one desktop reference;
   - may be a rough mockup, wireframe, annotated screenshot, or other visual reference;
   - does not need to be a full pixel-perfect Figma design for MVV #1.

A visual reference is strongly preferred when prose alone would leave Codex with wide latitude over hierarchy or presentation.

### Product-image creation / review gate

For every LP primary product image, the Creative Director must follow the canonical product-image sequence:

**Create candidate → review against the exact locked source and `MVV-001-LP-Product-Image-Standard.md` → refine material failures → recommend approval → Founder approves → archive / verify in GitHub.**

The review step is mandatory even when the first candidate looks acceptable. It is acceptable for the Creative Director to conclude that no refinement is needed, but the review itself should not be skipped.

The review should explicitly check, at minimum:

- locked-design fidelity, including print size and placement;
- garment / material realism;
- focal hierarchy and background subordination;
- appropriate audience / gender-expression merchandising where relevant;
- fair presentation relative to the assortment;
- mobile inspectability.

An approved LP primary image is not canonical until its archive record and binary asset are represented and verified in GitHub.

---

## 4. Project Manager implementation brief

After the Creative Director handoff is complete enough, the Project Manager / Technical Lead produces a concise developer-facing brief derived from canonical sources.

The brief should identify:

- exact canonical documents to read;
- exact assets and IDs to use;
- page sections and content hierarchy;
- product order / layout rules;
- inspection / interaction behavior;
- CTA placement and states;
- mobile behavior that is materially important;
- accessibility / technical requirements;
- what Codex may decide autonomously;
- what Codex must not reinterpret;
- explicit out-of-scope work;
- validation expected before PR review.

The brief should not duplicate all canonical documentation. It should act as an execution map that points Codex to the authoritative sources.

---

## 5. Developer execution rules

For each implementation task, Codex should:

1. begin from current `main`;
2. read Issue #55 and all referenced canonical requirements before editing;
3. inspect the current site implementation and authoritative assets;
4. use canonical IDs and assets; never invent parallel identifiers;
5. create / work on a fresh feature branch rather than modifying `main` directly;
6. change only authorized files / scope;
7. preserve approved creative intent while making normal implementation-level decisions;
8. stop and report material ambiguity rather than resolving strategic / brand / creative uncertainty silently;
9. test responsive behavior and interactions where practical;
10. review the exact diff against `main`;
11. report assumptions, tests performed, known limitations, and unresolved questions;
12. open a draft PR for review;
13. never merge its own work.

Phase A should remain free of analytics / instrumentation code unless technically necessary for basic customer-facing behavior. Phase B should remain separately reviewable so attribution and data-quality logic can receive focused review.

---

## 6. Render-review-revise loop

After Codex produces a reviewable Phase A implementation:

### Step 1 — Render

Provide a reviewable rendered page, preferably through the existing Cloudflare Pages workflow / preview or another low-friction representation sufficient for review.

### Step 2 — Creative Director review

The Creative Director reviews the actual rendered page, with mobile treated as a primary surface, and checks:

- product legibility;
- visual hierarchy;
- breathing room;
- image treatment consistency;
- fair product comparison;
- assortment range;
- slower-read design comprehension;
- fidelity to approved creative intent.

The Creative Director issues one of:

- `Creative ready`
- `Ready with minor observations`
- `Creative revisions required`

### Step 3 — Classify requested changes

The Project Manager / Technical Lead classifies review feedback:

- **implementation correction** — Codex can fix directly;
- **creative revision** — Creative Director must specify / approve the changed intent or asset;
- **brand decision** — route to Brand Manager;
- **experiment decision** — route to Strategy Advisor / Founder as appropriate;
- **technical-risk decision** — route to Technical Reviewer when appropriate.

This prevents Codex from being asked to resolve a disagreement that belongs to another role.

### Step 4 — Revise

Codex makes the authorized corrections and updates the same implementation branch / PR where appropriate.

Repeat the loop only for material issues. Do not chase cosmetic perfection that does not improve customer comprehension, experiment validity, or launch readiness.

---

## 7. Source-of-truth priority

When inputs conflict, use the following behavior rather than guessing:

1. Stop the affected implementation decision.
2. Identify the conflicting canonical sources / instructions.
3. Escalate to the Project Manager / Technical Lead.
4. Route the conflict to the role that owns the decision.
5. Update canonical documentation first when the approved resolution changes a governing requirement.
6. Resume implementation only after the conflict is resolved enough to proceed safely.

Chat discussion can clarify work, but merged GitHub documentation / approved issue decisions should remain the persistent reference for downstream roles.

---

## 8. Review and merge sequence

For Phase A customer-facing implementation, the expected sequence is:

**Codex self-review**

→ **Creative Director rendered-page review**

→ **Brand Manager pre-launch brand review**

→ **Technical Reviewer implementation review**

→ **Founder merge decision**

For Phase B analytics / lead-capture implementation, Creative Director review is only required if Phase B materially changes the visible experience. Technical Reviewer review is required because data correctness, attribution, privacy, and event semantics are central to the change.

The Founder explicitly approves each merge.

---

## 9. Completion signal for the designer-developer loop

The Phase A loop is complete when:

- the Creative Director's required assets / specification are represented in canonical GitHub inputs;
- every canonical LP primary product image has passed the product-image standard review gate and has been Founder-approved / archived as required;
- Codex has implemented the approved experience without material undocumented reinterpretation;
- the rendered page has been reviewed by the Creative Director;
- material creative / implementation issues are resolved;
- Brand Manager and Technical Reviewer reviews required by Issue #55 are complete;
- Founder has explicitly approved the merge.

This workflow should remain lightweight. Add process only when actual execution reveals a recurring coordination problem that the current loop does not solve.
