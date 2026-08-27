# MVV Technical Delivery Playbook

**Owner:** Knowledge Librarian  
**Primary users:** Project Lead / PM, Codex, Technical Reviewer, Founder  
**Status:** Working standard proposed from the first completed instrumented MVV  
**Last updated:** 2026-08-27

## Purpose

Use this playbook when an MVV landing page needs real lead capture, attribution, analytics, a remote database, and a guarded Production rollout.

It converts the lessons from the company’s first completed instrumented MVV into a repeatable operating sequence. It is intentionally technology-specific where the company has earned a current default—GitHub, Cloudflare Pages, Pages Functions, D1, and Wrangler—but it is not a substitute for the experiment's own event schema or site-specific setup record.

The governing objective is:

> Produce credible market evidence without losing attribution integrity, exposing PII, targeting the wrong environment, or deploying more infrastructure than the experiment has earned.

## Document boundaries

Keep these records separate:

| Record | Purpose | What belongs there |
|---|---|---|
| Company playbook | Reusable process | Gates, checklists, blocker recovery, evidence requirements |
| MVV event schema | Experiment contract | Event names, IDs, required fields, semantics, privacy rules |
| Site setup record | Live implementation truth | Project root, build/output paths, binding names, database IDs, migration status |
| Project issue | Current execution state | Owner, next gate, approvals, blockers, completion checklist |
| Pull request | Reviewable change | Diff, tests, implementation review, merge readiness |
| MVV retrospective | Local learning | What happened, why, results, and proposed methodology changes |

Do not copy live IDs or current deployment status into the company playbook. Link to the site setup record instead.

## Non-negotiable contracts before coding

Write and review these contracts before implementation begins:

1. **Experiment contract:** what decision the MVV should inform and which signals are primary versus diagnostic.
2. **Identity contract:** incoming acquisition `creative_id` remains independent from landing-page product `design_id`.
3. **Event contract:** names, triggers, timestamps, event-specific fields, session behavior, and duplicate rules.
4. **Lead contract:** selected product association, retry identity, idempotency, conflict behavior, and success/error UI.
5. **Privacy contract:** PII belongs only in the approved lead store; analytics payloads must not contain email or other prohibited PII.
6. **Environment contract:** Preview and Production databases are separate, separately bound, separately migrated, and separately approved.
7. **Publication contract:** only allowlisted customer-facing assets enter the static output directory; Functions remain outside that directory at the Pages project root.

If any contract is materially ambiguous, stop and return it to the role that owns the decision. Codex should not invent experiment, brand, privacy, or canonical-ID rules.

## Day-zero capability and target preflight

Run this before implementation or rollout planning. Record the answers in the project issue.

### Repository and GitHub

- Confirm the canonical repository, base branch, site path, issue, and implementation PR.
- Confirm the execution environment has a real checkout, the expected remote, and permission to fetch, commit, push, and open/update PRs.
- Confirm whether branch protection or CI checks exist.
- Record the exact starting commit.

### Cloudflare

- Confirm the account and Pages project.
- Record root directory, build command, output directory, Production branch, compatibility date/flags, and Preview/Production deployment settings.
- Record Preview and Production D1 database names and IDs.
- Confirm each Pages environment binds `DB` to the correct database.
- Confirm whether the available Cloudflare connection can inspect settings, mutate settings, query D1, or run Wrangler. These are different capabilities.

### Local/runtime tools

- Confirm Node/npm, Wrangler, shell behavior, and browser availability.
- Confirm which environment can access `pages.dev` and canonical domains.
- Confirm the independent Technical Reviewer can inspect the actual diff and has enough usage capacity to finish the review.

### Configuration strategy

Choose the remote-migration configuration approach before rollout:

- a reviewed project configuration with explicit environment mappings; or
- a reviewed migration-only template used to create an ephemeral, single-target configuration outside the repository.

Never discover during migration time that Wrangler has no configuration capable of resolving the intended database. Never rely on database-name inference when Preview and Production both exist.

## Recommended delivery sequence

### 1. Implement against a stable contract

- Use narrow endpoints and the existing Pages architecture unless evidence requires more.
- Validate payload shape, event names, IDs, lengths, timestamps, attribution fields, and event-specific properties on the server.
- Enforce uniqueness and idempotency at the database layer, not only in browser state.
- Preserve the same lead/event identity after an ambiguous failure so an exact retry is safe.
- Treat changed email or changed product selection as a new lead attempt.
- Create the lead and matching `lead_submit` event atomically.
- Keep non-lead analytics best-effort unless stronger delivery is necessary for the decision.
- Treat `page_exit` as a cumulative, best-effort diagnostic snapshot—not a session count or primary conversion metric.

### 2. Build a public allowlist

For a framework-free Pages site, build a clean static directory containing only customer-facing files. Keep migrations, tests, documentation, package metadata, scripts, and `functions/` out of the static output.

Cloudflare requires the `/functions` directory at the Pages project root rather than inside a static root such as `/dist`: [Pages Functions—Get started](https://developers.cloudflare.com/pages/functions/get-started/). Root, build command, and output directory have separate meanings in Pages: [Build configuration](https://developers.cloudflare.com/pages/configuration/build-configuration/).

Add an automated packaging test that compares the built file list to the expected allowlist.

### 3. Test locally before remote work

The minimum automated suite should cover:

- accepted events and leads;
- invalid/missing fields and request limits;
- PII rejection from analytics;
- exact duplicate acceptance;
- conflicting ID reuse rejection;
- cross-endpoint event-ID collision;
- lead + `lead_submit` atomicity;
- ambiguous retry identity reuse;
- changed-input identity replacement;
- first-touch attribution persistence;
- `creative_id` / `design_id` separation;
- visibility-timed `design_view`;
- dialog/CTA/form success and failure states;
- cumulative session summary behavior;
- desktop and compact-mobile interactions;
- public asset allowlist.

Record the exact command, pass count, and commit SHA. CI is preferable once the suite exists, but lack of CI does not make a manually captured run equivalent to an untested change.

### 4. Freeze the Preview candidate

Before remote migration or end-to-end QA:

- identify the exact candidate SHA;
- confirm the working tree is clean;
- confirm migration filename and cryptographic hash;
- confirm the Pages deployment will use the intended root/build/output configuration;
- avoid mixing executable changes with QA evidence updates.

If a later commit changes only documentation, compare it to the QA'd SHA and record that no executable, migration, test, or packaging file changed.

### 5. Run the Preview migration gate

Use Cloudflare's versioned migration mechanism. Cloudflare documents migrations as tracked `.sql` files and exposes `d1 migrations list/apply` through Wrangler: [D1 migrations](https://developers.cloudflare.com/d1/reference/migrations/) and [Wrangler D1 commands](https://developers.cloudflare.com/d1/wrangler-commands/).

#### Read-only preflight

1. Create/load credentials without printing the token.
2. Verify the token is active.
3. Verify repository branch, commit, clean state, migration filename, and source hash.
4. Create the single-target config outside the repository if using the ephemeral approach.
5. Hash the copied migration separately and compare it to the source.
6. Run `d1 migrations list` with `--remote` and the explicit `--config` path.
7. Confirm the resolved database name/ID and that the expected migration is the only pending migration.
8. Stop for explicit Preview apply approval.

#### Apply and verify

1. Apply only after approval and recheck the database shown in Wrangler's confirmation.
2. Run the migration list again; it must report no pending migrations.
3. Query schema/table/index metadata read-only.
4. Confirm verification wrote zero application rows.
5. Unset credentials, delete temporary configuration, confirm a clean repository, and delete the temporary token.

Use least-privilege, resource-scoped, short-lived API tokens. Cloudflare supports resource restrictions and TTL constraints and provides a token verification endpoint: [Create API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) and [Restrict tokens](https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/).

### 6. Verify the Preview deployment

Do not assume an old successful deployment represents new project settings. Confirm that the deployment was created after the intended configuration and at the exact candidate SHA.

Verify:

- every build/deploy stage succeeded;
- Pages found and compiled `functions/`;
- Preview uses the Preview D1 binding;
- root/build/output and compatibility settings are correct;
- the public file manifest exactly matches the allowlist;
- repository-only files are not publicly retrievable.

### 7. Run controlled Preview QA

Use fresh private/incognito sessions and deliberately tagged non-production attribution values.

Required checks:

1. A mismatch test where acquisition `creative_id` differs from selected `design_id`.
2. Desktop image enlargement, CTA/dialog, validation, failure handling, successful lead, and close behavior.
3. Compact-mobile orientation, no clipping, enlargement, CTA/form, and success behavior.
4. Read-only D1 verification of lead/event/session association and attribution preservation.
5. Query analytics without selecting the email column; separately test analytics JSON/text for email-like values.
6. Confirm event and lead IDs are unique and duplicates are suppressed.
7. Trigger `page_exit` by navigating the same tab to `about:blank`; closing an entire private window may terminate before the beacon completes.

Keep the controlled Preview tab/session identifiers and tag values in the evidence record so multiple intentional submissions are not mistaken for association defects.

### 8. Independent Technical Review and Founder merge gate

The reviewer must inspect the actual diff and relevant canonical documents, not only a PR summary. Require severity classification—Blocking, Important, Minor—and one explicit merge-readiness outcome.

The project lead then:

- confirms the reviewed head is still the PR head;
- resolves Blocking/Important findings and reruns affected tests;
- records accepted Minor observations;
- rechecks Preview evidence provenance;
- requests Founder approval for one exact head SHA;
- uses a SHA-guarded merge.

### 9. Run the Production D1 gate separately

Merging implementation does not authorize a Production migration.

Repeat the migration identity and target preflight against merged `main`, using a Production-only configuration and separate explicit Founder approval. Verify the Production database name/ID shown by Wrangler before confirming apply. Afterward, confirm no migrations remain, inspect schema/indexes read-only, clean credentials/configuration, and delete the temporary token.

When possible, keep automatic Production deployments disabled until the Production schema is ready and the deployment itself has separate approval. A skipped deployment record is acceptable evidence that the safeguard worked; it is not a successful rollout.

### 10. Run the Production deployment gate separately

Before enabling/retrying Production deployment, verify:

- exact merged commit;
- Production D1 migration complete;
- Production `DB` binding still correct;
- root/build/output and compatibility settings unchanged;
- Preview behavior preserved;
- explicit Founder deployment approval.

After deploy, confirm all stages succeeded, `uses_functions` is true, the public manifest is correct, canonical apex/`www` aliases are attached, and the deployed commit is exact.

### 11. Run one tagged Production smoke test

First use non-writing checks:

- canonical redirect behavior preserves query parameters;
- landing page and representative product interaction work;
- `GET` to a POST-only Function route returns the Function-level method error.

Then request separate approval for one controlled lead submission. Use a unique tag such as `creative_id` plus `utm_source` that downstream analysis can exclude. Verify the lead, `lead_submit`, attribution/product separation, event uniqueness, PII isolation, and `page_exit`. Do not delete the records if the durable tag is the agreed exclusion mechanism.

### 12. Close the project with evidence

- Update the site setup record with final migration/deployment state.
- Update the project issue with exact PR head, merge commit, deployment ID, QA result, accepted limitations, and remaining follow-up.
- Merge documentation through normal review.
- Close the issue after the last Phase B delivery/evidence commit's deployment is verified when documentation changes automatically deploy. Later retrospective-only documentation is outside the completed rollout and should not reopen it.
- Write a retrospective and promote only earned, reusable lessons into company methodology.

## Approval matrix

| Action | Default gate |
|---|---|
| Inspect GitHub/Cloudflare state | Read-only authorization |
| List remote migrations | Read-only authorization |
| Query schema/data with `SELECT` only | Read-only authorization; avoid retrieving PII |
| Change Pages configuration | Explicit approval |
| Apply Preview migration | Explicit Preview-only approval |
| Create controlled Preview rows | Explicit Preview-test approval |
| Mark PR ready or merge | Exact-SHA Founder approval |
| Apply Production migration | Separate exact-target Founder approval |
| Enable/retry Production deployment | Separate Founder approval |
| Create controlled Production rows | Separate Production-test approval |
| Close the project issue | Completion criteria satisfied and authorized |

## Blocker playbook

| Symptom | Likely cause | Recovery |
|---|---|---|
| Cloudflare operator cannot run migration | API connector has no repo checkout, migration file, Wrangler, or shell | Stop safely; use an authenticated Codespace/terminal with the canonical repo and short-lived token |
| Wrangler cannot resolve database/config | No committed config or wrong working directory | Use an explicit, reviewed single-target config and pass its absolute path with `--config` |
| Hash command appears to wait for input | A long pasted shell block or quoting construct is incomplete | Cancel if necessary; run small atomic commands and hash source/copy separately |
| Successful Preview is stale | It predates the current project config or candidate SHA | Trigger/retry a Preview build at the exact candidate SHA and verify deployment metadata |
| Browser agent cannot open `pages.dev` | Tool/network policy blocks the domain before origin | Use deployment metadata/build logs for non-interactive checks and Founder browser for interactive QA |
| No `page_exit` after closing private window | Browser terminated before beacon completion | Re-test in a fresh session by navigating the same tab to `about:blank` |
| Apparent wrong product association | Multiple intentional actions share a session | Isolate by session, timestamp, event/lead ID, and exact event chain before classifying a defect |
| PR head moved after QA | Documentation/evidence commit advanced the branch | Compare SHAs; rerun QA if executable scope changed, otherwise record code equivalence |
| Reviewer cannot finish | Usage/environment limitation | Preserve exact review prompt and head SHA; move to the established independent reviewer surface |
| Branch is behind `main` | Unrelated work landed during a long rollout | Compare changed paths and mergeability; do not rebase ceremonially if divergence is unrelated and safe |
| Issue body is stale | Progress lived only in comments/chats | Update the issue at major gates and perform a final reconciliation before closure |

## Evidence package checklist

Before declaring Phase B complete, the canonical record should contain:

- implementation PR and reviewed head;
- test command/result and packaging manifest;
- migration filename and hash;
- Preview/Production database names and IDs;
- migration list/apply/post-list outputs;
- schema/index verification;
- Preview and Production deployment IDs, commit SHAs, stages, aliases, Functions state, and bindings;
- tagged desktop/mobile mismatch QA;
- controlled Production smoke evidence;
- PII-isolation result;
- Technical Review outcome and accepted observations;
- each Founder approval and the exact action it authorized;
- credential/config cleanup confirmation;
- retrospective and methodology disposition.

## Earned automation backlog

Adopt only after the manual workflow is understood:

1. GitHub Actions for the existing test suite and public-package allowlist.
2. A reviewed script/template that creates a single-target migration config and prints target/hash/preflight evidence.
3. A repeatable read-only D1 verification query set that excludes PII by construction.
4. A reusable issue/PR checklist derived from this playbook.

Do not automate Production migration or deployment approval away. Human authorization is a control, not toil to eliminate.
