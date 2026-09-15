# MVV-001 Meta Campaign Setup and Phone-Verification Retrospective

**Project:** Worth the Detour MVV #1 Meta acquisition campaign  
**Issue:** #56  
**Status:** Blocked by Meta backend phone-verification state mismatch; live-delivery attribution gate deferred  
**Last updated:** 2026-09-15  
**Account timezone:** America/Chicago

## Executive summary

The team successfully established the Meta business assets, built and published-off a representative two-card Traffic carousel, verified its critical URLs and attribution design, obtained ad approval, and prepared a tightly guarded live-delivery attribution gate capped by a $1 account spending limit.

The gate did not start. When the Founder attempted the authorized ad-level activation, Meta rejected the update with a phone-number-required error. A Founder-controlled phone number was then entered in Account Information and successfully verified by SMS, but Ads Manager continued returning the same error. Account Status and Business Support Home showed no restriction, issue, or support case. Meta Business Support characterized the condition as a probable backend synchronization mismatch.

Formal Business Verification is not authorized. The campaign's September 12, 2026 end time has expired and cannot be reused or edited without new Founder authorization. All three objects remain off; no delivery or spend occurred.

## Final safe state

| Item | State |
|---|---|
| Business portfolio | `Taukay LLC` |
| Ad account | `Taukay LLC — MVV Ads` |
| Ad account ID | `1053148414264950` |
| Campaign | `WTD-MVV001-Traffic-01` — ID `52598753019423` — Off |
| Ad set | `WTD-MVV001-US-Feeds-01` — ID `52598753019623` — Off |
| Ad | `WTD-MVV001-CAR-01` — ID `52598753019823` — Off |
| Unpublished edits | None |
| Results / impressions / reach / spend | Zero |
| Account spending limit | $1 |
| Actual spend | $0 |
| Live gate | Not started |
| Production D1 watermark for live gate | Not taken; none required |
| Schedule | Expired: September 12, 2026 at 8:00 p.m. America/Chicago |
| Current blocker | Meta does not recognize completed SMS phone verification at the ad-account publishing gate |

## What was successfully completed

### Account and asset setup

- Created the Taukay LLC Business Portfolio.
- Created and connected the Worth the Detour Facebook and Instagram identities.
- Created the ad account and secured the administrator profile with two-factor authentication.
- Added the required payment method when Meta made it a publication prerequisite.
- Set and repeatedly confirmed a $1 account spending limit for the controlled attribution gate.
- Confirmed the relevant user had ads permission on the affected ad account.

### Campaign structure

The representative setup used:

- Traffic objective;
- Website destination;
- Maximize number of link clicks;
- manual Facebook Feed and Instagram Feed placements only;
- manually assembled image carousel;
- placement-specific 1:1 Facebook and 4:5 Instagram assets;
- automatic predicted-best-performing card ordering where exposed;
- two representative real cards: `C01 / Type-Led-4` and `C02 / B2`.

The campaign, ad set, and ad were published while off and the ad became approved.

### Attribution configuration

Card-specific Website URLs preserved the acquisition execution and source-card identity:

- `creative_id=WTD-MVV001-CAR-01`
- `utm_source=meta_qa` for controlled QA
- `utm_medium=paid-social`
- `utm_campaign=mvv-r012-001`
- `utm_content=C01~Type-Led-4` or `C02~B2`

The shared URL-parameters field contained only:

`meta_campaign_id={{campaign.id}}&meta_adset_id={{adset.id}}&meta_ad_id={{ad.id}}`

The carousel-level See more destination used `utm_content=carousel-see-more`.

The operator manually confirmed the Facebook Feed and Instagram Feed destination URLs for both representative cards. The same card-specific identities were present in each placement. The optional See more display-link field was blank; the actual Website URL was populated.

### Controlled preview evidence

A production D1 pre-click watermark was captured at `2026-09-10T18:11:01.793Z`. A controlled Facebook preview click for C01 reached the canonical landing page with the expected QA attribution.

A later Instagram-device attempt used a new watermark, `2026-09-10T18:45:11.114Z`, and opened only C01. The session did not preselect a product, preserving the acquisition-versus-product identity contract.

These preview checks were useful but did not substitute for the planned live-delivery attribution gate.

## Where time was spent

The main sources of operational friction were:

1. Meta's preview surfaces were inconsistent; several preview routes displayed the ad without a clickable destination.
2. Publishing-off initially encountered a payment-method requirement even though no delivery was intended.
3. The live gate required repeated three-level state checks because Meta separates campaign, ad-set, and ad toggles.
4. Metrics required a reporting date range that actually included the campaign's lifetime.
5. The phone-verification error appeared only at the publishing/activation boundary.
6. Meta exposed multiple phone/business-verification surfaces whose meanings were not equivalent.
7. The Beneficiary/Payer Inquiry form failed with a refresh-or-close warning and did not create a case.
8. Personal Support Inbox and Business Support Home were different surfaces; neither displayed a new case.
9. The support assistant suggested formal/business information paths that were broader than the narrow blocker.
10. While the blocker was investigated, the campaign schedule expired.

## Phone-verification incident chronology

1. Founder authorized a live-delivery attribution gate of up to $1 actual spend for no more than 24 hours.
2. Preflight confirmed all three objects off, zero metrics/spend, $1 account spending limit, no rules, no pending edits, and expected IDs/URLs.
3. Turning on the ad failed. Meta displayed:
   > Phone number required: You need to verify a phone number for this ad account before you can run ads.
4. The attempted change did not publish. All three objects were reconfirmed off.
5. Account Information showed a blank phone field. The Founder entered a personally controlled number and completed SMS verification privately.
6. After waiting and refreshing, the same ad-account error persisted.
7. Account Status showed the profile/Page in good standing but no ad-account phone-verification entry.
8. Business Support Home showed no account/asset issues and no active or resolved case.
9. Meta Business Support reported correct ads permission, no active restriction signal, US registration, and a probable verification-state synchronization defect.
10. The official advertiser/payer review route opened a Beneficiary/Payer Inquiry form. Submission produced a warning directing refresh/close; afterward the form was blank and no case existed.
11. Business Suite showed an empty Business phone field, but editing it required completion of the broader legal-business profile.
12. Security Center showed Taukay LLC as eligible for formal Business Verification.
13. Technical Review concluded that formal Business Verification was a separate, materially broader process and was not authorized as a workaround.
14. A redacted Ads Manager bug report was submitted through **Report a problem → Ad account settings → Ad Account**, including the exact error and affected account ID. No trackable case number has been recorded.
15. The campaign schedule expired during the unresolved incident.

## Root-cause assessment

The best current assessment is:

> Meta accepted the SMS verification in one account-information context but did not associate or synchronize that verified state with ad account `1053148414264950` at the publishing gate.

This is an evidence-based diagnosis, not a confirmed platform root cause. Supporting evidence:

- SMS verification succeeded.
- The identical ad-account error persisted afterward.
- The user had ads permission.
- Account Status and Business Support Home showed no restriction.
- Meta support found no active support signal and independently identified a likely synchronization issue.
- No alternative ad-account-specific verification control was exposed.

## Decisions and stop conditions

### Decisions

- Live-delivery attribution gate is deferred without a deadline.
- Formal Business Verification is not authorized.
- No schedule edit is authorized.
- No additional toggle/publication attempt is authorized to reproduce the error.
- Do not repeatedly submit the Beneficiary/Payer Inquiry form without a trackable Meta-supported route.
- Keep all three objects off.
- No new Production D1 watermark or cleanup is required.

### Conditions required before work resumes

Resume only if Meta:

- clears the phone-verification flag;
- exposes an official ad-account-specific verification step; or
- explicitly states that formal Business Verification is mandatory for this account.

If formal verification is required, stop for a new Founder decision covering exact documents, legal identity, purpose, data retention, and privacy implications.

## What worked well

- The campaign contract, attribution convention, creative IDs, and two-card operator values were decided before live delivery.
- Static card identity lived on each card URL; shared Meta ID macros remained separate.
- The $1 account spending limit created a hard financial backstop.
- Repeated three-level checks prevented an ambiguous failed toggle from being mistaken for delivery.
- The use of `meta_qa` made controlled visits distinguishable from future live traffic.
- The Technical Reviewer prevented a narrow phone-state defect from expanding into unapproved formal Business Verification.
- No credentials, SMS codes, payment details, full phone number, or identity documents were added to GitHub.
- The team stopped rather than repeatedly changing settings in an attempt to clear an opaque platform state.

## What should change next time

### Front-load account prerequisites

Before setting the campaign schedule or producing the full creative set:

1. Create/connect all business assets.
2. Confirm payment readiness.
3. Confirm ad-account user permission.
4. Check whether the ad account exposes phone verification.
5. Perform a minimal publish-off readiness test with placeholder-safe representative creative if authorized.
6. Resolve account-level blockers before setting a near-term schedule.

This would not guarantee detection of a defect that appears only at activation, but it would reduce schedule pressure and prevent late discovery of payment/account requirements.

### Set the schedule later

Do not set a short end date during initial construction. Set or finalize the exact schedule only after:

- the ad is approved;
- account-level prerequisites are satisfied;
- URLs and macros are verified;
- the Founder can provide an uninterrupted monitoring window.

Every schedule authorization must name its owner object and account timezone.

### Use an operator packet

Prepare exact values in a checklist before entering Ads Manager. This reduces repeated navigation and makes it easy to compare retained values after Meta reformats the interface.

### Separate evidence gates

Use distinct evidence packets for:

1. builder configuration;
2. publish-off state;
3. preview/QA attribution;
4. activation preflight;
5. live delivery;
6. closure.

A watermark belongs to one specific controlled analytics action. Do not reuse it for a later activation.

### Avoid broad support paths

When a narrow platform state is inconsistent:

- capture the exact error and affected account;
- use the closest bug-report category;
- ask for synchronization/reset or the official account-specific route;
- avoid general payer, billing, legal-business, or verification flows unless Meta explicitly confirms relevance;
- stop if no trackable case is created rather than resubmitting repeatedly.

## Reusable preparation packet for the next campaign

Prepare this before opening Ads Manager:

| Category | Required value |
|---|---|
| Account | Portfolio, ad account name/ID, Page, Instagram identity, timezone |
| Structure | Campaign/ad-set/ad names and intended object IDs after creation |
| Goal | Objective, destination, performance goal |
| Delivery | Audience, placements, budget owner, schedule owner |
| Creative | Format, card count/order, placement-specific files |
| Copy | Primary text, headlines, description, CTA |
| Attribution | Creative ID, per-card source identity, production/QA UTMs, shared macros |
| Controls | Spending limit, rules, recommendation auto-apply |
| Evidence | Full-lifetime date range, required columns, screenshots, analytics queries |
| Authorization | Publish-off scope, activation scope, spend/time cap, stop conditions |

## Restart procedure for MVV-001

If Meta clears the blocker, do not activate immediately.

1. Confirm the campaign, ad set, and ad remain off.
2. Confirm no unpublished edits.
3. Obtain explicit Founder authorization for a replacement start/end time and America/Chicago timezone.
4. Identify which object owns the schedule and change only that object.
5. Keep all objects off while the schedule edit is reviewed and published.
6. Confirm the ad remains approved and all objects remain off.
7. Repeat the complete activation preflight from the beginning.
8. Reconfirm the $1 account spending limit, $0 spend, zero baseline metrics, no rules, no pending edits, and unchanged URLs/macros.
9. Ensure an uninterrupted monitoring window.
10. Take a new Production D1 watermark immediately before activation.
11. Obtain fresh exact activation authorization.

## Methodology disposition

Promote these lessons to the company playbook:

- separate all Meta object, edit, publication, and delivery states;
- front-load account readiness;
- prepare an operator packet;
- verify representative assets before bulk production;
- set short schedules only after readiness;
- require full-lifetime zero metrics;
- take the Production watermark immediately before activation;
- treat business verification and account-specific phone verification as different scopes;
- stop on opaque verification mismatches and use narrow support reporting.

Keep these details campaign-specific:

- exact Worth the Detour object/account IDs;
- two-card asset identities and URLs;
- September 2026 timestamps and expired schedule;
- Meta's specific support/UI behavior observed during this incident;
- the current phone-verification mismatch.
