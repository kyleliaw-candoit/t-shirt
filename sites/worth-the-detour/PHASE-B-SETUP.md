# Phase B Cloudflare Pages + D1 setup

The site is a Cloudflare Pages project rooted at this directory. Pages Functions expose
`POST /api/events` and `POST /api/leads`; both require a D1 binding named `DB`.

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
deployments are disabled while the Preview rollout and review remain in progress; keep them disabled until the
separate Production approval gate. Keep `functions/` at the project root; do not copy it into `dist/`, so Pages
continues to compile the `/api/events` and `/api/leads` file-based routes.

## Database inventory and Pages bindings

Both databases are provisioned and their environment-specific Pages bindings are active and confirmed:

| Pages environment | Binding | D1 database | Database ID | Current status |
|---|---|---|---|---|
| Preview | `DB` | `worth-the-detour-mvv-preview` | `578c688c-e434-42f6-8924-e12a229ba0de` | Active; `0001_mvv_phase_b.sql` applied and verified 2026-08-26 |
| Production | `DB` | `worth-the-detour-mvv-production` | `78f0c8f2-c7a5-44fd-8d6e-a29c1d6b6fbe` | Active and confirmed; migration not applied |

In the Cloudflare Pages project **worth-the-detour**, configure the D1 binding separately in each environment:

- Preview: `DB` → `worth-the-detour-mvv-preview`
- Production: `DB` → `worth-the-detour-mvv-production`

Do not bind the production database to Preview. The Preview migration was applied through Wrangler and is
recorded in `d1_migrations`; the Production migration has not been run and requires explicit Founder approval.

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

Production rollout requires separate explicit Founder approval. Use a separate ephemeral configuration that
maps `DB` only to `worth-the-detour-mvv-production` and reverify the resolved database before applying:

```sh
npx --yes wrangler@latest d1 migrations list worth-the-detour-mvv-production --remote --config "$WTD_PRODUCTION_CONFIG"
npx --yes wrangler@latest d1 migrations apply worth-the-detour-mvv-production --remote --config "$WTD_PRODUCTION_CONFIG"
```

Use Wrangler's migration commands rather than executing the migration file directly. Wrangler records applied
migrations in `d1_migrations`, preserving a consistent migration history across Preview and Production. The
Preview sequence is complete; do not run the Production sequence without explicit Founder approval.

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
