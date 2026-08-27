# MVV-001 Phase B Retrospective

**Project:** Worth the Detour MVV #1 Landing Page  
**Phase:** Phase B — lead capture, attribution, analytics, D1, and Production rollout  
**Execution window:** 2026-08-22 through 2026-08-27  
**Status:** Completed  
**Owner:** Knowledge Librarian

## Purpose

Capture what the first end-to-end technical MVV delivery taught the company. This retrospective separates Worth the Detour evidence from reusable working standards so the next MVV can move faster without importing project-specific IDs, data, or history into company methodology.

Phase B was successful. The landing page now records product-specific engagement and leads while preserving independent acquisition attribution, keeping PII out of analytics, and maintaining isolated Preview and Production data. The major cost was coordination friction across GitHub, Codex execution environments, Cloudflare Pages, D1, Wrangler, browser surfaces, credentials, approvals, and evidence reconciliation.

## Outcome

- PR #85 implemented two Pages Functions, one versioned D1 migration, browser telemetry, lead capture, retry/idempotency behavior, public-only packaging, and tests across 13 changed files.
- The final implementation head had 17/17 local tests passing and was independently reviewed with no Blocking or Important findings.
- Preview and Production D1 were migrated separately through Wrangler and verified independently.
- Preview desktop/mobile QA proved the deliberate `creative_id = CR_TEST_A` → `design_id = Type-Led-4` mismatch remained correctly separated.
- Production smoke testing created one tagged `Type-Led-4` lead, 12 unique tagged events, and zero email-like analytics rows.
- PR #85 merged as `2902693dc327af40bee729cc8d6442ad72157e71`; final documentation PRs #88 and #89 recorded the Production migration and rollout.
- The final Production deployment for PR #89 completed successfully at merge commit `001353e1104d5c46f6efb0746fe687a520b15605`.
- Issue #55 closed as completed on 2026-08-27.

The site-specific configuration, database IDs, migration hashes, deployment IDs, and detailed QA evidence remain canonical in `sites/worth-the-detour/PHASE-B-SETUP.md` and Issue #55.

## What worked well

### The experiment contract was strong

The canonical event schema and acquisition-vs-product rule prevented a common analytical error. Incoming acquisition `creative_id` was never treated as the visitor's selected product. The deliberate mismatch test made the contract observable rather than relying on code inspection.

### The architecture stayed proportionate

Plain browser JavaScript, two narrow Pages Functions, D1, one migration, and no framework were sufficient. The implementation avoided Shopify, checkout, Meta CAPI, a warehouse/CDP, fingerprinting, session replay, and generalized analytics infrastructure.

### Database-enforced idempotency protected the strongest signal

Unique lead/event IDs, exact-retry acceptance, conflict rejection, and atomic lead + `lead_submit` creation gave the lead signal stronger delivery guarantees without building a general browser queue.

### Preview and Production isolation was real, not nominal

Separate databases, bindings, migrations, credentials, approvals, and verification steps prevented Preview activity from touching Production. Production schema changes did not implicitly authorize deployment.

### Safety gates caught mistakes before damage

- Wrangler's inability to resolve an absent configuration stopped rather than guessing a target.
- Automatic Production deployments were disabled while Production schema and approvals were incomplete.
- Exact-SHA review and merge guards protected the reviewed implementation.
- Migration hashes proved the applied file matched the canonical repository file.
- Read-only verification excluded the email column and separately checked analytics for email-like values.

These were productive stops, not failures.

### Public allowlisting solved a real deployment risk

Building `dist/` from an explicit allowlist prevented migrations, tests, setup documentation, package metadata, and scripts from becoming public while preserving root-level Pages Functions.

### Automated tests and live QA complemented each other

The test suite exercised validation, retry/idempotency, collisions, PII rejection, attribution, browser timing, dialog/form behavior, session summaries, and packaging. Live Preview QA then tested actual Functions, bindings, D1 rows, desktop/mobile behavior, and tagged attribution chains.

### Tagged test data made Production proof auditable

`CR_TEST_A`/`mvv-test` identified Preview records; `CR_CANONICAL_CHECK`/`deployment-smoke` identified Production records. Keeping those rows with durable exclusion tags preserved evidence without contaminating live analysis.

### Independent Technical Review added confidence without demanding unearned complexity

The reviewer found no Blocking or Important issues and correctly treated best-effort non-lead analytics and cumulative `page_exit` snapshots as genuine but acceptable MVV limitations.

### Founder approval stayed granular and meaningful

Implementation merge, Production migration, Production deployment, and controlled Production lead creation were separately approved. No AI role converted a technical recommendation into authority to ship.

## What created avoidable friction

### Execution capability was discovered too late

Different environments could inspect GitHub, push commits, operate Cloudflare APIs, run Wrangler, or open `pages.dev`—but no single surface reliably did all of them. The Cloudflare operator correctly stopped because it lacked a checkout, migration file, Wrangler, and shell. Other Codex environments lacked a usable Git remote or network path for pushing.

**Lesson:** perform a day-zero capability matrix and choose the execution/review surface for each stage before coding.

### The remote migration configuration was not ready

The repository intentionally did not include a Wrangler configuration. During rollout, Wrangler required an explicit configuration, so a temporary single-target config had to be designed, copied, hashed, and passed by absolute path.

The recovery was safe, but it happened later than it should have.

**Lesson:** decide and review the migration configuration strategy before implementation reaches Preview. Keep target resolution explicit.

### Long manual shell sequences increased confusion

Credentials, temporary directories, copied migrations, generated JSON, hashes, config variables, and Wrangler commands were manually relayed. At one point an output line appeared to be waiting after `Copied migration SHA-256: >`, requiring a smaller follow-up command to establish the actual state.

**Lesson:** prefer short atomic commands with one observable purpose. A reviewed helper/template is now earned; full migration automation is not.

### A successful Preview deployment was not necessarily the right deployment

The latest Preview initially predated the corrected root/build/`dist` configuration. A later documentation commit triggered a new build with the corrected configuration.

**Lesson:** deployment success must be tied to both exact commit and exact project configuration. Never infer runtime provenance from a green status alone.

### Browser access differed by tool

Automated web/browser surfaces blocked direct `pages.dev` access before requests reached the site. Deployment metadata and build logs could prove Functions/packaging, but the Founder had to perform interactive desktop/mobile checks.

**Lesson:** separate machine-verifiable deployment evidence from human browser QA and assign both explicitly.

### `page_exit` behaved exactly like a best-effort signal

Closing an entire incognito window did not produce an exit event. Navigating the same tab to `about:blank` did.

**Lesson:** keep `page_exit` diagnostic and best-effort; use same-tab navigation for a reliable QA trigger.

### Session-rich QA could look like a product-association defect

Multiple intentional Type-Led submissions occurred in the same session. An earlier row initially looked inconsistent until the event chain was isolated by timestamp, IDs, and selected product.

**Lesson:** record intended QA actions and isolate exact session/event/lead chains before declaring association defects.

### Documentation commits changed the PR head after executable QA

QA ran at `6812b15c...`; the final reviewed head `60df3e55...` added only `PHASE-B-SETUP.md`. This was safe only because the reviewer compared the two SHAs and confirmed no executable, SQL, packaging, HTML, or test change.

**Lesson:** freeze the runtime candidate before QA. If evidence documentation must advance the branch, explicitly prove code equivalence.

### The project issue and setup document required repeated reconciliation

The long Issue #55 checklist and `PHASE-B-SETUP.md` became stale while work advanced through chat and live operations. Several documentation-only updates were needed to restore canonical truth.

**Lesson:** update canonical state at major gates, not after every message; then run one final reconciliation before approval/closure.

### Independent review capacity was a dependency

The first delegated reviewer hit a usage limit. The exact head and review prompt had to be transferred to the established Technical Reviewer thread.

**Lesson:** reserve the review surface/capacity before the merge gate and preserve a self-contained review brief.

### No CI status existed

The suite passed locally and the reviewer inspected it, but GitHub had no workflow run or required status check. That increased reliance on manually reported evidence.

**Lesson:** the existing stable suite has now earned a lightweight GitHub Actions workflow, subject to separate implementation review.

## What did not need fixing

- The branch was 44 commits behind `main`, but the divergence was unrelated research/strategy documentation and GitHub still reported the PR mergeable. A ceremonial rebase would have added risk without improving Phase B.
- Non-lead analytics remained best-effort. A durable browser retry queue would have been disproportionate for MVV #1.
- Multiple cumulative `page_exit` rows per session remained acceptable because downstream analysis can use the latest/maximum snapshot and the event is not a primary success metric.
- Manual Founder-mediated handoffs remained workable. The friction is worth monitoring, but a generalized multi-agent orchestration system is not yet earned.

## Process changes to adopt now

### 1. Add a day-zero technical capability preflight

Before implementation, record which surface can:

- fetch/push GitHub;
- run tests and Wrangler;
- mutate/read Cloudflare;
- access Preview/canonical domains;
- perform independent review.

### 2. Use the reusable technical-delivery playbook

Adopt `docs/company/MVV-Technical-Delivery-Playbook.md` as the default sequence for future instrumented MVVs. Each project should instantiate its own site setup record and issue checklist rather than copying WTD IDs/history.

### 3. Prepare migration targeting before Preview

Review the committed/ephemeral configuration strategy, exact database mappings, token permissions, and cleanup procedure before the migration gate.

### 4. Freeze and name the QA candidate

Run end-to-end QA against one exact executable SHA. Keep evidence-only changes out of that branch when practical; otherwise prove code equivalence.

### 5. Make evidence requirements part of the issue from the start

Track hashes, deployments, bindings, packaging, tagged QA, PII checks, review outcome, approvals, and cleanup as expected deliverables—not ad hoc discoveries.

### 6. Add lightweight CI for tests and packaging

The 17-test suite and public-allowlist check are stable enough to run automatically on relevant PRs. CI should support review, not replace Preview QA or Founder approval.

## Small automation to pilot next

- A reviewed migration-preflight helper/template that prints repository SHA, clean status, source/copied migration hashes, config path, target name/ID, and pending migrations.
- Reusable read-only D1 verification queries that omit PII by construction.
- A GitHub issue template derived from the playbook's gates and approval matrix.

Do not yet automate Production migration confirmation, Production deployment approval, or controlled Production lead creation.

## Knowledge Librarian disposition

### Promote to company working standard

- Day-zero capability/target preflight.
- Separate Preview migration, implementation merge, Production migration, Production deployment, and Production-write approvals.
- Exact-SHA provenance for QA, review, and merge.
- Versioned migrations with explicit target configuration and hash verification.
- Public asset allowlisting with Functions kept at the Pages project root.
- Deliberate acquisition/product mismatch QA and PII-isolation verification.
- Tagged test records that can be excluded from analysis.
- Evidence reconciliation and retrospective before project closure.

### Pilot before standardizing further

- GitHub Actions for the current tests/packaging.
- Migration preflight helper/template.
- Reusable issue template and read-only verification query set.

### Keep on the scaling watchlist

- Founder as the message bus between specialist chats and execution agents.
- Review capacity/usage limits.
- Repeated manual copying of live evidence into GitHub.

### Do not add yet

- A generalized analytics platform or warehouse.
- Guaranteed delivery/retry infrastructure for every browser event.
- Automated Production migrations or approvals.
- A generalized multi-agent orchestration layer.
- A separate deployment platform or frontend framework.

## References

- Issue #55 — Worth the Detour MVV #1 Landing Page
- PR #85 — Phase B implementation
- PR #88 — Production D1 migration evidence
- PR #89 — Production deployment and smoke evidence
- `sites/worth-the-detour/PHASE-B-SETUP.md`
- `docs/mvv/worth-the-detour/MVV-001-Event-Schema.md`
- `docs/mvv/worth-the-detour/MVV-001-Acquisition-vs-Product-Validation.md`
- `docs/mvv/worth-the-detour/MVV-001-Phase-A-Sprint-Retrospective.md`
- `docs/company/MVV-Technical-Delivery-Playbook.md`

