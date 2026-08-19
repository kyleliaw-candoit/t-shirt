# MVV-001 Phase A Sprint Retrospective

**Project:** Worth the Detour MVV #1 Landing Page  
**Phase:** Phase A — customer-facing landing page  
**Date:** 2026-08-19  
**Status:** Sprint retrospective notes  
**Owner:** Knowledge Librarian

## Purpose

Capture the most useful operating lessons from the first end-to-end Worth the Detour landing-page implementation cycle. This is intentionally concise rather than comprehensive.

The goal is to improve the AI-native operating system through evidence from actual execution while preserving the company's earned-complexity principle: adopt small process changes that clearly reduce repeat friction, and do not turn every observation into new machinery.

## 1. What worked well and should become standard?

### Pair the primary project lead role with Project Manager responsibility by default

Assigning the Technical Lead to also act as Project Manager worked better than expected. Because the same AI role understood the implementation deeply enough to sequence the work intelligently, it could coordinate specialist reviews, route feedback correctly, maintain Issue #55, surface blockers, and keep the project moving toward launch without requiring a separate PM role.

**Future working principle:** for substantial bodies of work, assign Project Manager responsibility to the primary AI role leading that project by default. That role owns sequencing, handoffs, blocker escalation, and source-of-truth maintenance. Separate the PM function only when workload or organizational scale demonstrates that the combined role has become a bottleneck.

### Clear specialist ownership improved decisions

The Creative Director owned rendered-page creative judgment; Brand Manager owned brand and experiment integrity; Codex owned implementation; Technical Reviewer independently checked technical correctness and behavior; Founder retained final merge authority. Respecting those boundaries reduced duplicated judgment and made feedback easier to route.

### Review the actual artifact appropriate to each role

Rendered-page review was more informative than reviewing prose specifications or code alone. The Creative Director caught the mobile above-the-fold problem only after inspecting the actual deployed page. The implementation → Cloudflare preview → Creative review → targeted correction → recheck loop worked well.

The Technical Reviewer similarly benefited from checking actual interactive behavior rather than limiting review to static code inspection.

### GitHub worked well as the shared handoff layer

PR #73 became the canonical implementation and review surface. Issue #55 tracked overall project state, sequencing, decisions, and dependencies. Recording specialist feedback on the PR allowed later roles to inspect the actual review record instead of depending on cross-chat memory.

### Distinguishing blockers from observations prevented endless polish

Creative Director and Brand Manager explicitly separated required acceptance issues from non-blocking refinements. This prevented a passing implementation from repeatedly returning to Codex for optional polish.

### Earned-complexity discipline kept the project moving

The project did not add a frontend framework, deployment redesign, ecommerce stack, general design system, or broader infrastructure before those capabilities were needed. Plain HTML/CSS/JS and the existing Cloudflare Pages deployment were sufficient for Phase A.

### Independent technical review closed a real functional gap

The Technical Reviewer explicitly exercised product-image enlargement, `I want this` interactions, dialog behavior, form validation/success states, and basic keyboard/focus behavior. This clarified that functional QA belongs outside Creative/Brand review even though it is part of the customer-facing acceptance bar.

### Founder approval remained a meaningful final gate

AI roles recommended, implemented, and reviewed; none converted its own recommendation into permission to ship. Founder approval remained required before merge.

## 2. What created avoidable friction or rework?

### Cross-chat and ChatGPT ↔ Codex communication is still manually mediated

The Founder currently acts as the human message bus between specialist chats and Codex by copying prompts, responses, and status updates. During Phase A this was manageable and not a meaningful blocker, so automating it now would likely be premature.

However, it could become a throughput bottleneck as the company runs more concurrent projects and faster iteration loops. The Founder should not eventually need to relay routine operational information between every AI role.

**Current disposition:** monitor this as a scaling signal rather than solve it now. Revisit shared structured handoffs or more direct agent-to-agent workflows when manual communication materially slows execution or causes missed handoffs.

### Agent execution environments were inconsistent

Codex completed the implementation but could not push to GitHub because of network restrictions, and Chromium installation was blocked in that environment. The PM/Technical Lead successfully recovered and reconstructed the artifact, but this consumed disproportionate coordination effort.

This is worth remembering as an environment limitation, not evidence that we need recovery infrastructure now.

### The correct review surface was not obvious at first

The Creative Director's ordinary chat environment could not reliably access the Cloudflare preview. Screenshot-only review would have been insufficient for interactive UI. Moving the review into a browser-capable Work environment solved the problem.

Future implementation handoffs should identify the execution/review surface needed by the specialist, not merely provide the right prompt.

### The first mobile acceptance criterion was too literal

"First product image visible above the fold" was initially satisfied by only a shallow hanger/background strip. The real user-facing criterion was that a **recognizable portion of the T-shirt itself** should be visible without scrolling.

Outcome-oriented acceptance criteria are preferable to pixel-presence criteria when the purpose is customer comprehension.

### Functional QA ownership was initially implicit

Creative Director correctly identified interaction verification as outside Creative scope, but the first Technical Reviewer brief did not explicitly enumerate the customer-facing interaction checks. The gap was caught before final review, but future implementation work should name the functional-verification owner up front.

### Issue #55's body became stale while comments reflected current truth

The project continued to move efficiently through status comments rather than repeatedly editing the long issue checklist. That was a reasonable trade-off, but stale unchecked items can confuse later agents if they do not read the latest comments.

Do not introduce checklist-maintenance ceremony solely to avoid this. Prefer concise status updates during execution and clean up durable workflow documentation when the sprint is complete.

## 3. What did we learn about role boundaries, handoffs, and canonical GitHub records?

### Role boundaries need an explicit handoff contract

"Creative Director reviews Codex" is not sufficiently operational. A useful handoff specifies:

1. what artifact the role should inspect;
2. where findings should be recorded;
3. what decision/outcome vocabulary it should use.

For Phase A, this became: inspect the rendered preview, record implementation-specific feedback on PR #73, and state whether the result is ready, ready with observations, or requires revisions.

### Issue and PR serve different purposes

**Issue:** overall project state, sequencing, dependencies, decisions, and next owner.  
**PR:** implementation artifact, implementation-specific review feedback, required corrections, and merge readiness.

Detailed implementation review feedback should normally live on the PR rather than only in a specialist chat or the project issue.

### Conversation memory should not be an operating dependency

If a behavior matters across sessions, agents, or handoffs, encode it in the shared operating system or canonical project artifact rather than assuming another chat will remember it.

### Feedback should be classified before routing

Useful categories during Phase A included implementation correction, creative revision, brand decision, experiment decision, technical-risk finding, and non-blocking refinement. Classification helped prevent Codex from making creative/brand decisions and prevented specialists from reopening unrelated work.

### Specialists should inspect the artifact appropriate to their role

Creative Director should inspect the rendered customer experience. Technical Reviewer should inspect the actual diff/code and exercise relevant functionality. Brand Manager should review the rendered experience against canonical brand requirements. One review surface is not sufficient for every specialist role.

### Latest authoritative review outcomes supersede earlier states

A prior `Creative revisions required` result should not remain active after the same reviewer has rechecked the corrected artifact and recorded `Ready with minor observations`. Downstream agents should identify the latest authoritative decision rather than treating historical comments as simultaneously active.

### Non-blocking observations should stay non-blocking

Optional polish should not automatically become a new gate because another role notices or agrees with it. Reclassification should be explicit and based on material risk to the experiment, customer experience, brand, or technical correctness.

## 4. Process changes to adopt before Phase B

### Change 1 — Make artifact, review location, and outcome explicit in every specialist handoff

Before a specialist review begins, the PM/lead brief should state:

> **What to inspect → where to record findings → what outcome vocabulary to use.**

This is a lightweight standard that directly addresses a failure mode observed in Phase A without adding another approval layer.

### Change 2 — Explicitly assign functional acceptance for interactive implementation work

For interactive customer-facing work, the implementation/review plan should name who verifies actual behavior, not merely code presence.

For Phase B, this should include an end-to-end test such as:

> incoming acquisition `creative_id` is preserved → visitor engages a different LP `design_id` → correct product intent/event is recorded → lead remains associated with the correct product → no PII appears in analytics payloads.

Codex remains responsible for implementation and self-test. The Technical Reviewer independently verifies correctness. The project lead/PM ensures the acceptance checks are actually completed before Founder approval.

## Knowledge Librarian disposition

### Promote to working standard now

- For substantial projects, combine the primary AI project-lead role with Project Manager responsibility by default; split them only when scale earns the separation.
- Specialist handoffs should identify the review artifact, canonical feedback location, and expected outcome vocabulary.
- Interactive implementation work needs an explicit functional-acceptance owner.
- PRs should hold implementation-specific review feedback; project issues should hold overall state and decisions.

### Keep on the scaling watchlist

- Founder-mediated copy/paste between chats and Codex is acceptable at the current stage but may become an orchestration bottleneck later.
- Do not build a multi-agent orchestration system until actual communication overhead materially limits speed or reliability.

### Do not add yet

- Separate standalone Project Manager agents for every project.
- New approval roles or broad review-governance machinery.
- General-purpose agent-recovery infrastructure because one environment could not push/install Chromium.
- Mandatory mockups or design-system artifacts for every UI task.

## References

- Issue #55 — Worth the Detour MVV #1 Landing Page
- PR #73 — Build the Worth the Detour Phase A landing page
- `docs/company/AI-Operating-System.md`
- `docs/mvv/worth-the-detour/MVV-001-Landing-Page-Designer-Developer-Workflow.md`
