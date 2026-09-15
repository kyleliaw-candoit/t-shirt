# Meta MVV Campaign Operations Playbook

**Owner:** Campaign / MVV Operator  
**Primary users:** Founder, Campaign / MVV Operator, Creative Director, Brand Manager, Technical Reviewer  
**Status:** Working standard derived from Worth the Detour MVV-001  
**Last updated:** 2026-09-15

## Purpose

Use this playbook to prepare, build, verify, publish-off, activate, monitor, and close a small Meta acquisition test without losing attribution integrity or accidentally authorizing spend.

It captures reusable operating lessons. Campaign-specific creative, targeting, URLs, budgets, schedules, and platform observations belong in the experiment's own documents and issue. Meta changes its interface and eligibility requirements frequently, so verify the live interface before every launch.

## Governing controls

1. **Separate preparation from spend.** Building or publishing an off campaign is not authorization to deliver it.
2. **Treat campaign, ad set, and ad as three independently controlled objects.** Confirm all three states at every gate.
3. **Treat draft state, publication state, review state, and delivery state as different things.** An object may be published but off, or contain unpublished edits while its delivery toggle is off.
4. **Do not let platform prompts expand the experiment.** Business Verification, billing changes, ownership changes, new accounts, broader placements, and new optimization signals require their own review.
5. **Preserve acquisition identity separately from downstream product identity.** An ad or carousel card explains where a visitor came from; landing-page behavior identifies what the visitor later engaged with.
6. **Use explicit Founder authorization for spend, schedule changes, and activation.** Record the exact scope, limit, and monitoring window.
7. **Stop on ambiguity.** A failed publish, unexplained verification prompt, unexpected placement, stale schedule, or missing metric is a blocker—not a reason to keep clicking.

## Record boundaries

| Record | Purpose |
|---|---|
| Company playbook | Reusable sequence, gates, evidence, failure recovery |
| Campaign-specific production requirements | Objective, placements, format, optimization, asset rules |
| Creative manifest | Stable creative/card IDs, files, copy, destinations, status |
| Event schema / analytics record | Attribution semantics, privacy, downstream measurement |
| Project issue | Current state, approvals, blockers, next authorized action |
| Campaign retrospective | What happened in one campaign and which lessons are reusable |

## Stage 0 — capability and account readiness

Complete account prerequisites before investing in full asset export or entering a time-sensitive schedule.

Verify and record:

- Business portfolio and its durable administrative owner.
- Facebook Page and Instagram professional account, including their portfolio connections.
- Intended ad account name and numeric ID.
- User permissions on the ad account.
- Two-factor authentication required by the portfolio.
- Ad account country, currency, and timezone.
- Payment method readiness, without exposing payment data.
- Account spending limit and current amount spent.
- Account Status / Business Support Home issues.
- Any ad-account-specific phone-verification requirement exposed by Meta.

A verified phone on a personal Facebook profile, in Account Information, or in general business details may not prove that the ad account recognizes the required state. Do not assume that formal Business Verification is required merely because the Security Center says the business is eligible. Only begin formal verification when Meta explicitly requires it for the affected account and the Founder separately approves the legal identity, documents, privacy implications, and purpose.

### Account-readiness stop conditions

Stop if Meta requests or implies any unapproved:

- formal Business Verification;
- incorporation, tax, identity, address, domain, or business documents;
- beneficiary/payer, billing, ownership, or spending-limit change;
- creation of another ad account;
- use of a different phone number solely as a workaround.

## Stage 1 — freeze the campaign contract outside Ads Manager

Prepare a one-page campaign decision record before using the builder:

- experiment ID and decision to be informed;
- objective and destination;
- performance goal and why it matches available optimization signals;
- audience and geography;
- placements;
- format and card count;
- budget, spending cap, and kill rules;
- exact start/end time and timezone;
- naming convention;
- creative, card, and downstream product identity rules;
- production and QA URL conventions;
- roles and approvals.

Do not choose settings merely because Meta recommends them. Recommendation auto-apply should be off unless deliberately approved. Confirm that no automated rule can alter delivery or budget.

## Stage 2 — prepare the full operator packet

Prepare copy-and-paste values outside Ads Manager so the operator is not designing the experiment in the interface.

The packet should include:

- exact campaign, ad-set, and ad names;
- primary text, headline, description, and CTA;
- placement-specific media filenames and dimensions;
- initial card order;
- card-to-media mapping;
- card-specific Website URLs;
- carousel-level See more URL, when used;
- shared URL-parameter string;
- targeting, optimization, budget, and schedule values;
- a verification checklist.

For carousel attribution, bind stable source identity to each card's Website URL. Use the shared URL-parameters field only for values that truly apply to every card, and verify that Meta appends rather than replaces card parameters.

Never construct a Meta click ID. Preserve it only when Meta supplies it.

## Stage 3 — use a representative-card gate before bulk production

Before exporting an entire carousel:

1. Produce one representative asset for every intended placement ratio.
2. Verify that the manual builder accepts the format.
3. Confirm placement customization works as intended.
4. Inspect realistic mobile previews for crop, legibility, and truncation.
5. Add a second real card if card-specific URL behavior or reordering must be tested.
6. Verify card media remains paired with its own destination when automatic ordering is enabled.

If the interface cannot preserve the intended mapping, stop before bulk export and choose the smallest reliable structure.

## Stage 4 — build in dependency order

Build and verify in this order:

1. **Campaign:** objective, special-category status if applicable, buying type, campaign-level budget controls.
2. **Ad set:** destination/conversion location, performance goal, audience, placements, budget owner, schedule owner.
3. **Ad:** identities, format, media, copy, CTA, card order, card URLs, See more URL, tracking parameters.

After each layer, record the object's numeric ID. Before navigating away, verify that the intended values were retained.

Meta may place budget or schedule controls at a different layer depending on configuration. Record the actual owner instead of assuming.

## Stage 5 — validate URLs and previews without confusing them with delivery

For each representative card and placement:

- Open its editor and inspect the complete destination URL.
- Confirm static parameters and stable source-card identity.
- Confirm the generic carousel-level destination is intentionally distinct.
- Leave an optional display-link field blank if the interface permits and no display override is needed.
- Inspect Facebook and Instagram placement previews independently.
- Confirm the selected placement-specific media is still assigned.

A preview may not provide a clickable link. Use only the smallest approved alternative preview route. Do not activate a campaign merely to obtain a preview.

When controlled clicks are authorized:

- use a distinct QA marker such as `utm_source=meta_qa`;
- take a fresh private/incognito session per source card when attribution is first-touch;
- confirm the landing URL;
- confirm source attribution remains independent from the downstream product selected;
- verify server-side evidence read-only;
- exclude only explicitly marked QA records from live analysis.

## Stage 6 — publish-off gate

Before publishing any draft:

- campaign off;
- ad set off;
- ad off;
- no unapproved changes;
- intended account selected;
- budget and schedule rechecked;
- payment and account requirements understood;
- destination URLs and macros rechecked;
- explicit authorization to publish the exact objects while off.

After publishing:

- confirm all three objects still show off;
- confirm no `Review and publish (1)` or unpublished-edits indicator remains;
- confirm Delivery is Off at all three levels;
- record all three object IDs;
- verify the ad review/approval state;
- verify results, impressions, reach, and amount spent are zero over a date range that includes the entire campaign lifetime.

Do not interpret a gray Review and publish button as missing work. It normally means there are no unpublished edits.

## Stage 7 — activation preflight

Run immediately before activation, not hours or days earlier.

Confirm:

- correct ad account and all three exact object IDs;
- campaign, ad set, and ad off;
- ad approved;
- no unpublished edits;
- no automated rules;
- recommendation auto-apply off;
- schedule is future-valid and explicitly authorized in the account timezone;
- exact budget and account spending limit;
- amount spent, impressions, reach, results, and delivery all zero;
- production URLs and dynamic macros unchanged;
- uninterrupted monitoring window available;
- Production analytics query and rollback/stop procedure ready.

Take the Production data watermark immediately before activation. An older watermark is not the activation baseline.

Activation authorization must name:

- objects;
- maximum actual spend;
- maximum elapsed time;
- purpose of the gate;
- start/end schedule and timezone;
- stop conditions;
- person monitoring.

## Stage 8 — guarded activation and monitoring

Activate only the authorized object sequence and immediately confirm effective delivery state at every level. Meta may require parent objects to be on before a child can deliver; follow the pre-approved sequence and do not improvise.

During the window, monitor:

- Delivery state and warnings;
- amount spent against both experiment cap and account spending limit;
- impressions, reach, results/link clicks;
- landing-page events and attribution integrity;
- unexpected placements, URLs, or automated changes.

Stop immediately on:

- verification or publication error;
- spend above the authorized cap;
- wrong URL or attribution;
- unintended placement;
- schedule mismatch;
- inability to observe delivery;
- platform request for a materially broader account change.

A failed toggle or publish does not start the monitoring window if no object became active and no delivery occurred.

## Stage 9 — closure

At the end of the authorized window:

1. Turn off all three objects.
2. Confirm the changes are applied and no unpublished edits remain.
3. Confirm final delivery metrics and spend.
4. Query analytics using the recorded watermark.
5. Separate acquisition performance by `creative_id` from product intent by `design_id`.
6. Retain the source-card-to-downstream-product path where sample size permits.
7. Record anomalies and unresolved platform issues.
8. Update the project issue and campaign retrospective.

Do not reuse an expired schedule. A replacement schedule is a new Founder decision and must identify the exact owner object, times, and timezone. Keep every object off while an administrative schedule edit is reviewed and published; then repeat the entire activation preflight.

## Ads Manager interface traps learned from MVV-001

| Observation | Operating response |
|---|---|
| Preview links may be non-clickable | Do not assume the URL is wrong; use an approved preview surface or controlled delivery gate. |
| Payment can block publication even when all toggles are off | Treat payment readiness as a publish-off prerequisite. |
| Phone verification may be accepted in one settings surface but not recognized by the ad account | Capture the exact error; check account status; report a probable synchronization defect; do not expand into formal verification without approval. |
| `Fix errors` may redirect without exposing the needed control | Stop repeated attempts and use official support/reporting paths. |
| A feedback report may not create a trackable support case | Capture any confirmation and timestamp; check Business Support Home later; do not submit repeatedly. |
| Reporting date ranges can hide historical spend | Use a range covering the complete campaign lifetime when establishing zero metrics. |
| Optional display-link fields can be blank | Validate the actual Website URL; do not invent a display link solely to fill the field. |
| Shared URL parameters are separate from per-card Website URLs | Keep card identity on the card URL and common dynamic IDs in the shared field only after live validation. |
| The interface can preserve an expired end date | Schedule validity is a distinct preflight gate; resolution of another blocker does not authorize schedule repair. |
| A toggle action can fail without changing delivery | Reconfirm all three levels, unpublished edits, metrics, and spend before classifying the outcome. |

## Verification-state mismatch recovery

When Meta says a phone number is required after SMS verification succeeded:

1. Capture the complete error with account/ad identity and timestamp.
2. Revert or confirm all campaign objects off.
3. Confirm no unpublished edits and zero delivery/spend.
4. Check Account Information, Account Status, and Business Support Home read-only.
5. Allow a short synchronization interval, sign back in, and hard refresh once.
6. If still blocked, report the Ads Manager bug under **Ad account settings → Ad Account**, attach the redacted error, and request synchronization/reset of the ad-account phone-verification state.
7. Do not include the full phone number, SMS code, payment data, or identity documents in a general report.
8. Do not repeatedly reproduce the error or resubmit an untrackable form.
9. Keep the live gate deferred until Meta clears the flag, exposes an ad-account-specific verification step, or explicitly states that formal Business Verification is mandatory.

## Evidence checklist

Retain redacted evidence of:

- account and object names/IDs;
- objective, performance goal, placements, budget owner, and schedule owner;
- complete destination URLs and shared macros;
- rendered placement previews;
- all three delivery states;
- unpublished-edits state;
- approval status;
- full-lifetime zero baseline metrics;
- account spending limit and amount spent;
- account warnings or verification errors;
- Account Status and Business Support Home state;
- support report/conversation, confirmation number if any, and timestamp;
- activation authorization and monitoring window;
- Production watermark taken immediately before activation;
- final metrics, D1 evidence, and shutdown state.

Do not retain phone numbers, SMS codes, authentication secrets, recovery codes, payment details, or identity documents in GitHub.

## Reusable operator checklist

### Before builder work

- [ ] Account readiness confirmed.
- [ ] Campaign decision sheet approved.
- [ ] Operator packet complete.
- [ ] Representative assets pass live-format verification.
- [ ] Attribution contract and QA marker approved.

### Before publish-off

- [ ] Exact account and object names confirmed.
- [ ] All three toggles off.
- [ ] Budget, schedule, placements, creative, copy, URLs, and macros confirmed.
- [ ] Publish-off authorization recorded.

### After publish-off

- [ ] All three objects off.
- [ ] No unpublished edits.
- [ ] IDs recorded.
- [ ] Ad status reviewed.
- [ ] Full-lifetime metrics and spend zero.

### Before activation

- [ ] Fresh full preflight passed.
- [ ] Schedule is valid and authorized.
- [ ] Spending limit reconfirmed.
- [ ] Monitoring window available.
- [ ] Fresh Production watermark taken.
- [ ] Exact activation authorization recorded.

### After the gate

- [ ] All three objects off and applied.
- [ ] Final Meta and first-party evidence captured.
- [ ] Acquisition and product-intent findings kept separate.
- [ ] Project issue and retrospective updated.
