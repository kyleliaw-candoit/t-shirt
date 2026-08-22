# Phase B Cloudflare Pages + D1 setup

The site remains a no-build Cloudflare Pages project rooted at this directory. Pages Functions expose
`POST /api/events` and `POST /api/leads`; both require a D1 binding named `DB`.

## Database inventory and Pages bindings

Both databases are provisioned and their environment-specific Pages bindings are active and confirmed:

| Pages environment | Binding | D1 database | Database ID | Current status |
|---|---|---|---|---|
| Preview | `DB` | `worth-the-detour-mvv-preview` | `578c688c-e434-42f6-8924-e12a229ba0de` | Active and confirmed |
| Production | `DB` | `worth-the-detour-mvv-production` | `78f0c8f2-c7a5-44fd-8d6e-a29c1d6b6fbe` | Active and confirmed; migration not applied |

In the Cloudflare Pages project **worth-the-detour**, configure the D1 binding separately in each environment:

- Preview: `DB` → `worth-the-detour-mvv-preview`
- Production: `DB` → `worth-the-detour-mvv-production`

Do not bind the production database to Preview. Keep the existing Pages settings: root
`sites/worth-the-detour`, blank build command, output `.`, production branch `main`, compatibility date
`2026-08-15`, no flags, Default placement, and Fail open.

## Inspect and apply versioned migrations

Preview initialization:

```sh
npx wrangler d1 migrations list worth-the-detour-mvv-preview --remote
npx wrangler d1 migrations apply worth-the-detour-mvv-preview --remote
```

Production rollout, only after explicit Founder approval:

```sh
npx wrangler d1 migrations list worth-the-detour-mvv-production --remote
npx wrangler d1 migrations apply worth-the-detour-mvv-production --remote
```

Use Wrangler's migration commands rather than executing the migration file directly. Wrangler records applied
migrations in `d1_migrations`, preserving a consistent migration history across Preview and Production. Do not run
either remote migration sequence until its authorized rollout step.

## Local development and tests

Apply the versioned migration to a local D1 database, then serve the Pages project with the `DB` binding:

```sh
npx wrangler d1 migrations list worth-the-detour-mvv-preview --local
npx wrangler d1 migrations apply worth-the-detour-mvv-preview --local
npx wrangler pages dev . --d1 DB=worth-the-detour-mvv-preview --compatibility-date=2026-08-15
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
npx wrangler d1 execute worth-the-detour-mvv-preview --remote --command="SELECT lead_id, design_id, attribution_json FROM leads ORDER BY server_received_at DESC LIMIT 5"
npx wrangler d1 execute worth-the-detour-mvv-preview --remote --command="SELECT event_id, event_name, attribution_json, properties_json FROM events ORDER BY server_received_at DESC LIMIT 20"
```

Confirm that `creative_id` remains `CR_TEST_A`, the selected `design_id` is `Type-Led-4`, Meta IDs remain
separate, the `lead_submit` event contains no email, duplicate IDs produce one row, and success is never shown
for a failed `/api/leads` response. Repeat image enlargement, CTA/dialog, validation, successful submission,
and close/backdrop interactions at desktop and compact-mobile widths before production rollout.
