---
title: Shopify Commerce Feasibility Spike
owner: Technical Lead / PM
reviewers:
  - Creative Director
  - Brand Manager
  - Technical Reviewer
  - Knowledge Librarian
status: Approved scope; not started
version: 0.1
last_updated: 2026-09-15
approved_by: Founder
---

# Shopify Commerce Feasibility Spike

## Purpose

This is a bounded platform feasibility experiment. It will test whether the approved [Shopify Commerce Architecture](../../company/Shopify-Commerce-Architecture.md) can produce a reviewable, private, checkout-ready two-product storefront with materially less Founder effort than the Worth the Detour custom Cloudflare build.

It is not a new customer-facing wedge, a WTD relaunch, or permission to accept payments.

## Decision to be informed

Should Shopify become the default MVV storefront for future commerce wedges, with custom Cloudflare storefronts used only when a specific experiment requirement justifies them?

## Hypothesis and exit rule

**Hypothesis:** Shopify + Printful can reach a reviewed, private, transaction-ready two-product state while preserving company identity/measurement semantics and using materially less Founder and implementation effort than the WTD custom stack.

**Pass:** Same or better customer experience and measurement integrity, materially less Founder intervention, materially shorter build-to-review time, and no material creative-control, Printful, or operational limitation that negates the savings. Shopify becomes the default architecture for the next commerce wedge.

**Conditional pass:** A narrow limitation exists with a low-cost, repeatable workaround. Record the workaround and its ongoing cost before deciding whether Shopify is still the default.

**Fail:** A material limitation in measurement, creative control, Printful synchronization, customer experience, or operating overhead negates the expected savings. Record the evidence and retain Cloudflare or another path as the default until the limitation is resolved.

## Test fixtures

Use two existing WTD designs only as non-public test fixtures:

- `Type-Led-4`
- `B2`

They are already familiar, visually different, and were the representative products in the Meta attribution work. Using them isolates the platform question from a new brand-development question.

Their use does not relaunch Worth the Detour, change the current WTD MVV, or authorize public exposure.

## Required canonical inputs

Before Shopify implementation begins, create or confirm a compact Store Build Packet containing:

- spike ID and decision contract;
- approved test-fixture asset references;
- creative and brand presentation requirements;
- two-product manifest with canonical `design_id` values;
- proposed Shopify metafield namespace/key;
- one standardized T-shirt production recipe;
- Tier 2 and checkout-ready behavior;
- measurement/privacy contract;
- mobile and desktop acceptance criteria;
- authority boundaries and stop conditions.

Use a GitHub issue for mutable execution state, owners, blockers, approvals, and evidence links. Keep this README as the stable charter. Use PRs for reviewable changes. Create a retrospective only after the spike completes and produces evidence.

## In scope

1. Create or configure one Shopify store and keep the customer surface private/password-protected.
2. Create one unpublished working theme from a generated or selected starting direction.
3. Create two representative physical T-shirt products with realistic titles, descriptions, prices, variants, and approved imagery.
4. Attach each product's company-owned `design_id` as a Shopify custom-ID metafield; treat Shopify and Printful IDs as implementation IDs.
5. Define one standardized Printful production recipe: blank, print technique, placement, artwork dimensions, supported colors, and sizes.
6. Synchronize/map both products and representative variants so Printful reports them as fulfillment-ready.
7. Configure a checkout-ready but non-public experience and execute a controlled, non-charge checkout proof if prerequisites and authority permit.
8. Prove product mapping/order-routing behavior separately from any paid fulfillment.
9. Implement and query the minimum measurement contract.
10. Obtain rendered Creative Director and Brand Manager review on representative desktop and compact-mobile viewports.
11. Obtain independent Technical Review of implementation, integration, measurement, privacy, failure modes, and evidence.
12. Measure effort, cost, repeatability, and Founder involvement.

The first run should deliberately use the ChatGPT–Shopify integration wherever it saves time while establishing the minimum GitHub/API/CLI control layer. This is not a vendor bake-off. The test should reveal which tasks truly require deterministic tooling and which can remain conversational.

## Out of scope and not authorized

- public launch or public theme publication;
- real customer purchasing;
- live payment activation;
- real POD production or fulfillment charge;
- automatic paid Printful fulfillment;
- business, identity, or banking verification unless separately approved;
- tax, legal, privacy, returns, or customer-service commitments;
- production-domain connection;
- material recurring app/platform expense beyond a separately approved experiment cost;
- a full 10–12 product assortment;
- migration or modification of the current WTD Production site, database, analytics, or Meta campaign;
- a generalized Shopify automation platform or dedicated permanent Shopify Operator role.

Documentation of the spike does not authorize its execution. The execution issue must identify each consequential action and its approval state.

## Critical implementation hypotheses

### Private store versus product status

Printful currently states that Shopify draft or archived products do not sync. The expected test arrangement is therefore:

- products active/published as required for the integration;
- storefront private/password-protected;
- working theme unpublished;
- no public customer purchasing path.

Treat this as an implementation hypothesis to verify against the actual store and current vendor behavior, not as a guaranteed permanent platform fact.

### Checkout proof versus fulfillment proof

These are separate gates:

1. **Checkout proof:** a supported test-mode or simulated order demonstrates price, variant, shipping, and checkout behavior without a real customer charge.
2. **Mapping/routing proof:** the order and product mapping identify Printful as the intended fulfillment location/provider.
3. **Paid fulfillment proof:** Printful actually accepts and produces an order.

Only the first two are in scope by default. Keep downstream fulfillment manual and disable any automatic import/fulfillment behavior before creating a test order. A real Printful charge requires separate Founder authorization.

Shopify Payments test mode currently requires Shopify Payments setup. If using it would require business/identity verification beyond the approved scope, stop and use another supported no-charge proof or record the blocked prerequisite. Do not convert a technical test into payment-activation authority.

## Minimum identity and measurement contract

The spike must prove:

1. incoming `creative_id`, UTMs, and source-card/source-product identity survive into the Shopify session;
2. the canonical `design_id` is stored on and recoverable from the Shopify product;
3. downstream product engagement uses the product actually viewed/selected;
4. engaging with a product different from the source product does not overwrite acquisition identity;
5. product view, engagement, intent, checkout start, and test-order outcome are queryable at the granularity needed for the decision;
6. Shopify/Printful IDs remain available for reconciliation but do not replace company IDs;
7. PII remains separated from behavioral analytics and is not written to GitHub;
8. retry, duplicate, consent, and failure behavior are explicit enough for an independent review.

Do not decide the analytics backend in advance. Compare:

- the existing D1 event/lead backend;
- Shopify Customer Events/pixels;
- the smallest useful hybrid, with Shopify handling commerce-native events and a company endpoint preserving the MVV-specific diagnostic chain.

Choose the minimum architecture that preserves analytical independence and privacy.

## Work sequence and gates

| Gate | Owner | Required evidence |
|---|---|---|
| 1. Store Build Packet ready | Strategy + Brand + Creative + Technical Lead / PM | Canonical packet and two-product manifest reviewed |
| 2. Cost/access preflight | Technical Lead / PM | Store/plan state, connector/API/CLI access, exact approved cost, and no-charge safeguards |
| 3. Private implementation | Implementation agent | Private store, unpublished theme, two configured products, canonical metadata, and Printful mapping |
| 4. Measurement proof | Implementation agent | Queryable mismatch test preserving acquisition/product independence and PII separation |
| 5. Rendered creative review | Creative Director | Desktop and compact-mobile rendered acceptance or focused revision list |
| 6. Brand review | Brand Manager | Category/identity comprehension and brand acceptance |
| 7. Independent technical review | Technical Reviewer | Findings classified as Blocking, Important, or Minor; explicit readiness outcome |
| 8. Architecture decision | Strategy Advisor + Founder | Evidence-based Pass, Conditional pass, or Fail disposition |

The implementation agent may correct ordinary defects inside the approved packet. Return experiment, brand, financial, legal, privacy, or publication decisions to their owners.

## Metrics to capture

| Dimension | Required measure |
|---|---|
| Cycle time | Elapsed time from complete packet to first reviewable storefront and to accepted candidate |
| Labor | AI/operator minutes by stage and Founder minutes |
| Manual burden | Number of Founder UI actions, agent UI actions, repeated fields, and recoveries from partial operations |
| Product throughput | Time for first product and incremental time for second product; projected repeatability for 10–12 products |
| Cost | Shopify, app, connector, test-order, and any other incurred cost; separate fixed from variable |
| Reuse | Templates, manifests, scripts, theme components, POD recipe, and checks reusable by the next wedge |
| Consistency | Print placement, variants, price, metadata, image treatment, and product-page consistency |
| Experience | Creative/Brand acceptance on desktop and compact mobile |
| Measurement | Attribution persistence, `creative_id`/`design_id` independence, event queryability, and PII isolation |
| Portability | Work that required ChatGPT versus work reproducible through GitHub/API/CLI |

Compare the result with WTD only where the work is reasonably analogous. Founder minutes and build-to-review time are primary success measures, not decorative observations.

## Evidence checklist

- [ ] Exact repository base commit and execution issue recorded.
- [ ] Scope, cost ceiling, and access permissions approved before mutation.
- [ ] Store confirmed private/password-protected.
- [ ] Working theme confirmed unpublished.
- [ ] `Type-Led-4` and `B2` product records reconcile with the GitHub manifest.
- [ ] Canonical `design_id` values are stored and queryable.
- [ ] Printful production recipe and variant mapping are recorded.
- [ ] Automatic paid fulfillment is disabled before any test order.
- [ ] Checkout and routing proofs are separated in the evidence.
- [ ] Controlled acquisition/product mismatch test passes.
- [ ] PII isolation is verified.
- [ ] Desktop and compact-mobile rendered reviews pass or findings are resolved.
- [ ] Technical Reviewer inspects actual evidence and exact implementation state.
- [ ] Actual cost, elapsed time, operator time, and Founder time are recorded.
- [ ] Pass / Conditional pass / Fail decision is documented.

## Stop conditions

Stop and return to the Founder before:

- entering a paid plan or incurring an unapproved charge;
- completing payment, banking, business, identity, tax, or domain setup;
- exposing the storefront publicly;
- enabling automatic fulfillment;
- submitting an order that could charge Printful;
- expanding beyond two products;
- weakening the canonical identity or privacy contract;
- adopting a paid app or custom integration not included in the approved cost envelope.

## Current state

As of 2026-09-15:

- scope is Founder-approved;
- execution has not started;
- the Shopify storefront architecture remains a candidate default, not settled company policy;
- no store creation, connector setup, paid plan, payment activation, public launch, or Printful charge is authorized by this record;
- promotional terms observed during planning are dynamic and must be reverified rather than treated as a durable cost assumption.

## Current platform references

Recheck current vendor behavior before execution:

- [Shopify plugin for ChatGPT](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/shopify-plugin-for-chatgpt)
- [Authorizing Shopify AI-tool access](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/authorizing-access)
- [Shopify GitHub theme integration](https://shopify.dev/docs/storefronts/themes/tools/github)
- [Shopify CLI `theme push`](https://shopify.dev/docs/api/shopify-cli/theme/theme-push)
- [Shopify custom IDs](https://shopify.dev/docs/apps/build/metafields/working-with-custom-ids)
- [Shopify payment test mode](https://help.shopify.com/en/manual/checkout-settings/test-orders/payments-test-mode)
- [Printful Shopify product import/sync requirements](https://help.printful.com/hc/en-us/articles/360014066459-Why-don-t-my-Shopify-products-show-up-in-my-Printful-Dashboard)
- [Printful Shopify order processing and fulfillment](https://help.printful.com/hc/en-us/articles/6148086204316-How-do-I-manage-order-processing-and-fulfillment-in-Shopify)
