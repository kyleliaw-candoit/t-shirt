---
title: Worth the Detour Phase B Cloudflare Pages + D1 Setup
owner: Project Lead / PM
status: Active production record
version: 1.0
last_verified: 2026-08-27
---

# Phase B Cloudflare Pages + D1 setup

The site is a Cloudflare Pages project rooted at this directory. Pages Functions expose
`POST /api/events` and `POST /api/leads`; both require a D1 binding named `DB`.

Related durable knowledge:

- [MVV Technical Delivery Playbook](../../docs/company/MVV-Technical-Delivery-Playbook.md) — reusable cross-MVV delivery and blocker-recovery sequence.
- [MVV-001 Phase B Retrospective](../../docs/mvv/worth-the-detour/MVV-001-Phase-B-Retrospective.md) — Worth the Detour execution lessons and methodology disposition.

This file remains the source of truth for Worth the Detour-specific configuration, resource IDs, migration state, and rollout evidence.

## Required Pages configuration

Use these settings at each environment's authorized rollout stage:

| Setting | Required value |
|---|---|
| Root directory | `sites/worth-the-detour` |
| Build command | `sh build-static-assets.sh` |
| Build output directory | `dist` |
| Functions directory | `functions` at the Pages project root |
| Production branch | `main` |
| Compatibility date | `2026-08-15` |
| Compatibility flags | none |

The project-wide Cloudflare Pages build configuration above is active and confirmed. Automatic Production
deployments were enabled on 2026-08-27 after separate Founder approval and remain enabled for future `main`
commits. Keep `functions/` at the project root; do not copy it into `dist/`, so Pages continues to compile the
`/api/events` and `/api/leads` file-based routes.

## Database inventory and Pages bindings

Both databases are provisioned and their environment-specific Pages bindings are active and confirmed:

| Pages environment | Binding | D1 database | Database ID | Current status |
|---|---|---|---|---|
| Preview | `DB` | `worth-the-detour-mvv-preview` | `578c688c-e434-42f6-8924-e12a229ba0de` | Active; `0001_mvv_phase_b.sql` applied and verified 2026-08-26 |
| Production | `DB` | `worth-the-detour-mvv-production` | `78f0c8f2-c7a5-44fd-8d6e-a29c1d6b6fbe` | Active; `0001_mvv_phase_b.sql` applied and verified 2026-08-27 |

In the Cloudflare Pages project **worth-the-detour**, configure the D1 binding separately in each environment:

- Preview: `DB` → `worth-the-detour-mvv-preview`
- Production: `DB` → `worth-the-detour-mvv-production`

Do not bind the production database to Preview. Both environment-specific migrations were applied through
Wrangler and are recorded independently in each database's `d1_migrations` table. Preview and Production remain
isolated; applying the Production migration did not authorize or trigger a Production Pages deployment.

## Inspect and apply versioned migrations

This repository does not commit a Wrangler configuration file. For every remote D1 operation, create an
ephemeral configuration outside the repository that binds only the database authorized for that rollout stage,
sets `migrations_dir` to the copied migration directory, and pass its absolute path with `--config`. Never rely
on implicit database-name resolution.

Preview rollout status: completed and verified on 2026-08-26. With `WTD_PREVIEW_CONFIG` set to the absolute
path of an ephemeral Preview-only configuration, the versioned commands are:

```sh
npx --yes wrangler@latest d1 migrations list worth-the-detour-mvv-preview --remote --config "$WTD_PREVIEW_CONFIG"
npx --yes wrangler@latest d1 migrations apply worth-the-detour-mvv-preview --remote --config "$WTD_PREVIEW_CONFIG"
```

The post-apply migration list reported no pending migrations.

Production rollout status: completed and verified on 2026-08-27 following separate explicit Founder approval.
The rollout used a separate ephemeral configuration mapping `DB` only to
`worth-the-detour-mvv-production` and reverified the resolved database before applying:

```sh
npx --yes wrangler@latest d1 migrations list worth-the-detour-mvv-production --remote --config "$WTD_PRODUCTION_CONFIG"
npx --yes wrangler@latest d1 migrations apply worth-the-detour-mvv-production --remote --config "$WTD_PRODUCTION_CONFIG"
```

Use Wrangler's migration commands rather than executing the migration file directly. Wrangler records applied
migrations in `d1_migrations`, preserving a consistent migration history across Preview and Production. Both
migration sequences are complete and report no pending migrations. Do not rerun either migration; the separate
Production Pages deployment approval and completed rollout are documented below.

## Local development and tests

From the Pages project root, build the allowlisted public directory, apply the versioned migration only to a
local instance of the Preview D1 database, then serve `dist/` from that same root so `functions/` remains
discoverable:

```sh
sh build-static-assets.sh
npx wrangler d1 migrations list worth-the-detour-mvv-preview --local
npx wrangler d1 migrations apply worth-the-detour-mvv-preview --local
npx wrangler pages dev dist --d1 DB=worth-the-detour-mvv-preview --compatibility-date=2026-08-15
npm test
```

The automated suite uses an in-memory D1-compatible test double and requires no Cloudflare credentials.

## Preview verification

Open a non-production branch preview with this deliberate mismatch:

```text
/?creative_id=CR_TEST_A&utm_source=meta&utm_medium=paid-social&utm_campaign=mvv-test&utm_content=creative-a&utm_term=antiques&fbclid=fb-test&meta_campaign_id=mc-1&meta_adset_id=mas-1&meta_ad_id=ma-1
```

Enlarge and select `Type-Led-4`, then submit a non-production test email. Inspect browser Network requests and
query the preview database:

```sh
npx --yes wrangler@latest d1 execute worth-the-detour-mvv-preview --remote --config "$WTD_PREVIEW_CONFIG" --command="SELECT lead_id, design_id, attribution_json FROM leads ORDER BY server_received_at DESC LIMIT 5"
npx --yes wrangler@latest d1 execute worth-the-detour-mvv-preview --remote --config "$WTD_PREVIEW_CONFIG" --command="SELECT event_id, event_name, attribution_json, properties_json FROM events ORDER BY server_received_at DESC LIMIT 20"
```

Confirm that `creative_id` remains `CR_TEST_A`, the selected `design_id` is `Type-Led-4`, Meta IDs remain
separate, the `lead_submit` event contains no email, duplicate IDs produce one row, and success is never shown
for a failed `/api/leads` response. Repeat image enlargement, CTA/dialog, validation, successful submission,
and close/backdrop interactions at desktop and compact-mobile widths before production rollout.

## Verified Preview QA evidence (2026-08-26)

The corrected-config Preview deployment at PR head `6812b15c21c3bf02da653861428e2cc18c2f32c2`
passed the runtime and end-to-end QA gate:

- Pages detected and compiled `functions/`; both `/api/events` and `/api/leads` operated against the
  isolated Preview `DB` binding.
- The public build contained only the 13 allowlisted customer-facing assets. Repository-only setup
  documentation, migrations, tests, package metadata, and the build script were not published.
- Desktop QA passed image enlargement, CTA/dialog behavior, two intentional product-specific submissions,
  and a deliberate attribution mismatch. Acquisition remained `creative_id = CR_TEST_A` while the selected
  lead remained `design_id = Type-Led-4`.
- Compact-mobile QA passed at a 375-pixel viewport: immediate brand/apparel/treasure-hunting orientation,
  visible first-product transition, no horizontal clipping, image enlargement, CTA/form behavior, successful
  `Type-Led-4` submission, and the same attribution separation.
- The verified `Type-Led-4` lead matched its `lead_submit` event, session, CTA, form, and attribution.
  Exactly one unique `Type-Led-4` lead row was created by the controlled mobile test.
- Analytics event IDs were unique, and no email-like value appeared in analytics rows. Email remained isolated
  to the `leads` table.
- Best-effort `page_exit` was verified by same-tab navigation on desktop and was also captured on mobile.
  The mobile summary recorded 100% maximum scroll depth, eight designs viewed, and session-scoped engagement
  and duration values.

## Verified Production migration evidence (2026-08-27)

After PR #85 merged as `2902693dc327af40bee729cc8d6442ad72157e71`, the Founder separately approved
the Production D1 migration. The guarded rollout verified:

- Canonical migration: `0001_mvv_phase_b.sql`; file SHA-256
  `8bd743a0e874ebb30db4894aff25c6b99c7f8fe5eadcdce592c7c89810cd99ec`; Git blob
  `b94a1818a2784cf1e78d515a7d785b840d7dd2ba`.
- Exact target: `worth-the-detour-mvv-production`
  (`78f0c8f2-c7a5-44fd-8d6e-a29c1d6b6fbe`), matching the Production Pages `DB` binding.
- Wrangler `4.126.0` listed only `0001_mvv_phase_b.sql` pending, applied it successfully by executing five
  migration commands, and then reported no migrations remaining.
- Read-only post-apply inspection confirmed `d1_migrations`, `events`, `leads`,
  `events_name_design_idx`, and `events_session_id_idx`; the verification wrote zero rows.
- Automatic Production deployments remained disabled. The PR #85 merge deployment record remained skipped with
  reason `production_deployments_disabled`; no clone, build, or deploy stage ran.
- The ephemeral Wrangler configuration and terminal credentials were removed, the repository remained clean,
  and the short-lived Production migration token was deleted.

The Production schema was ready before deployment; the separately approved Production Pages rollout and smoke
evidence are documented below.

## Verified Production deployment and smoke evidence (2026-08-27)

After documentation PR #88 merged as `d8b8a902a176810c5e59fce91e822097b925824e`, the Founder separately
approved the Production Pages rollout. The guarded rollout verified:

- Automatic Production deployments were enabled while preserving the GitHub source settings, Preview behavior,
  root `sites/worth-the-detour`, build command `sh build-static-assets.sh`, output `dist`, compatibility date
  `2026-08-15`, no compatibility flags, and the Production `DB` binding.
- Cloudflare retried only the skipped exact-`main` deployment. Production deployment
  `c8cfe38c-9a59-418c-9ccb-69abf030f5e4` completed every stage successfully at commit
  `d8b8a902a176810c5e59fce91e822097b925824e`.
- Pages compiled Functions and published exactly the 13 allowlisted customer-facing assets. The deployment
  attached `https://worth-the-detour.com` and `https://www.worth-the-detour.com` and retained the isolated
  Production D1 binding `78f0c8f2-c7a5-44fd-8d6e-a29c1d6b6fbe`.
- Browser verification confirmed that `www` redirects to apex while preserving query parameters, the landing
  page and `Type-Led-4` image/CTA/dialog work, and `GET /api/events` reaches the Function and returns
  `method_not_allowed`.
- The separately approved controlled Production test created exactly one `Type-Led-4` lead and its matching
  `lead_submit` event while preserving `creative_id = CR_CANONICAL_CHECK`. Lead/event/session, CTA, and form
  association matched; analytics contained zero email-like values.
- The tagged Production session recorded 12 unique events: one `landing_view`, six `design_view`, one
  `design_engagement`, two `intent_click`, one `lead_submit`, and one `page_exit`. The exit summary
  recorded 100% maximum scroll depth, six designs viewed, 576.760 seconds of session duration, and first
  meaningful engagement at 55.321 seconds.

The controlled Production records remain intentionally identifiable by
`creative_id = CR_CANONICAL_CHECK` and `utm_source = deployment-smoke` so analysis can exclude them. No
test/debug defaults are embedded in the deployed client. The Production deployment and end-to-end Phase B smoke
gate are complete.

The controlled Preview records remain identifiable by `creative_id = CR_TEST_A` and
`utm_campaign = mvv-test`. Preview and Production D1 remain isolated, and both rollout evidence sets are
explicitly tagged for exclusion from live MVV analysis.

## Final documentation deployment verification (2026-08-27)

Founder approved final documentation-only PR #89 at exact head
`65b8095195f92ec435034ebdcd2a02753c626786`. It merged as
`001353e1104d5c46f6efb0746fe687a520b15605` and automatically created Production deployment
`596a960d-d1b6-421c-9d3f-aa000450a084`.

The deployment completed queue, initialization, clone, build, and deploy stages successfully at the exact merge
commit. It compiled Pages Functions, retained the Production `DB` binding
`78f0c8f2-c7a5-44fd-8d6e-a29c1d6b6fbe`, published exactly 13 allowlisted customer-facing assets, and attached
the apex and `www` aliases. Issue #55 was then closed as completed.
