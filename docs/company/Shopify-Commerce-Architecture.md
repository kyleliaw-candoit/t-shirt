---
title: Shopify Commerce Architecture
owner: Knowledge Librarian
primary_users:
  - Strategy Advisor
  - Brand Manager
  - Creative Director
  - Technical Lead / PM
  - Operations Manager
  - Implementation Agent
  - Technical Reviewer
status: Approved target architecture; Shopify-default adoption remains conditional on the feasibility spike
version: 0.2
last_updated: 2026-09-25
reviewed_by: Founder
---

# Shopify Commerce Architecture

## Purpose

This document defines the approved target architecture for AI-assisted Shopify storefronts and print-on-demand commerce.

It records the durable company design: where truth lives, which systems perform which jobs, how AI roles collaborate, and which actions remain under Founder authority. It does not authorize a Shopify launch or claim that Shopify has passed the company's feasibility test.

The accompanying [Shopify feasibility spike](../mvv/shopify-feasibility-spike/README.md) will determine whether Shopify becomes the default storefront architecture for future commerce wedges.

## Decision summary

> **GitHub remembers. Shopify runs. ChatGPT operates.**

The company will use provider-neutral canonical specifications and Git history as its architectural foundation. The Shopify plugin for ChatGPT may be the preferred operating surface whenever it is the fastest reliable way to execute routine store work.

This is not a choice between portability and convenience:

- **Canonical architecture:** specifications + GitHub + Shopify APIs/CLI and theme integration.
- **Preferred operating experience:** ChatGPT + Shopify integration.
- **Fallback:** another capable agent reconstructs the work from canonical GitHub records and operates through Shopify-supported connectors or APIs/CLI.

The AI operator is replaceable. The business's durable intent must not exist only in conversation history.

## Decision record

**Decision date:** 2026-09-15  
**Decision owner:** Founder  
**Decision state:** Approved target architecture; adoption gate not yet passed

The company considered two approaches:

| Approach | Strength | Material weakness | Decision |
|---|---|---|---|
| Canonical specs + GitHub + Shopify APIs/CLI | Reproducible, reviewable, multi-model, suitable for deterministic bulk work and recovery | More setup and sometimes slower for routine operations | Architectural foundation |
| ChatGPT–Shopify integration as the foundation | Fast, conversational, low Founder effort, and well aligned with preparation of unpublished work | Vendor-specific, weaker as a durable change record, limited for some settings and bulk operations | Preferred operator, not source of truth |

The company accepts practical dependency on ChatGPT when it produces substantial operating leverage. It does not accept irreversible dependency where another capable operator could not understand or reproduce the intended store state.

## Source-of-truth boundaries

| Layer | System / owner | Canonical responsibility |
|---|---|---|
| Experiment and brand truth | GitHub | Experiment contract, brand requirements, creative direction, copy, approved assets, and acceptance criteria |
| Configuration and institutional memory | GitHub | Product manifest, company IDs, POD recipe, measurement contract, customized theme code, decisions, and verification records |
| Commerce runtime | Shopify | Products, variants, collections, prices, store configuration, operational inventory, customers, checkout, and orders |
| Fulfillment runtime | Printful or selected POD provider | Production catalog mapping, print files, fulfillment state, shipment, and tracking |
| Operations ownership | Operations Manager | Owns approved routine Shopify, Printful, catalog, fulfillment, reconciliation, and operational-evidence work; Strategy Advisor carries this as an explicit interim hat until a separate role is earned |
| Primary operating surface | ChatGPT | Executes approved routine work through the Shopify integration or other authorized tools |
| Deterministic control / escape layer | Shopify APIs, CLI, and GitHub theme integration | Repeatable theme work, validation, reconciliation, bulk operations, and recovery |
| Cold-standby operator | Claude or another capable agent | Resumes from GitHub when the primary operator is unavailable or unsuitable |
| Governance authority | Founder | Consequential publication, financial, legal, privacy, tax, domain, and brand-safety decisions |

GitHub should record what Shopify and the POD provider **are supposed to contain** and enough evidence to verify important state. It should not duplicate all runtime data.

Do not place customer records, orders, operational inventory snapshots, payment data, or other runtime PII in GitHub.

## Canonical Store Build Packet

Shopify creation begins only after Strategy, Brand, and Creative have produced a compact Store Build Packet. Operations validates that the packet can be implemented with current Shopify and POD facts; Finance validates the relevant economics. At minimum it should contain:

1. experiment identity, hypothesis, decision, and commerce mode;
2. brand requirements and category-comprehension goal;
3. creative presentation specification and approved assets;
4. product manifest with canonical company `design_id` values;
5. product copy, price assumptions, variant policy, and assortment rules;
6. standardized POD production recipe;
7. measurement and privacy contract;
8. mobile and desktop acceptance criteria;
9. review gates, current status, and authority limits.

The packet controls the implementation. Shopify AI storefront previews, Sidekick suggestions, connector output, theme-editor state, and generated copy are candidates until reconciled with it.

## Identity and measurement contract

Company experiment identities remain independent of vendor resource identities.

- `design_id` is the canonical company identity for a product design.
- `creative_id` identifies the acquisition creative.
- source-card/source-product identity describes what brought the visitor to the store.
- Shopify product, variant, collection, theme, and order IDs are implementation/runtime identifiers.
- Printful product, variant, template, and order IDs are fulfillment identifiers.

The intended diagnostic chain is:

> `creative_id` → source card/source product → visit → independent downstream `design_id` → engagement/intent → lead or order

Shopify supports custom resource IDs through metafields, so the architecture expects the canonical `design_id` to be attached to the Shopify product and used for cross-system reconciliation. The exact namespace, schema, and event implementation must be defined and reviewed in the experiment's measurement contract.

## Store creation and review workflow

The target workflow is:

> **Strategy / Brand / Creative specification → Operations validation and implementation → private Shopify store, Printful state, and unpublished theme → rendered and operational review → revision → independent technical review → Founder-controlled consequential action**

### Strategy, Brand, and Creative

- Strategy defines the experiment purpose, evidence requirement, offer, and decision boundary.
- Brand Manager defines the positioning and category/customer comprehension requirements.
- Creative Director owns the builder prompt/specification, evaluates generated directions, selects the starting direction, defines assortment presentation and imagery, and specifies material changes.
- The Founder should not routinely choose typography, spacing, section arrangement, hero treatment, product-card design, or ordinary image presentation.

### Operations Manager and implementation agent

The Operations Manager owns the business-operating state. An authorized implementation agent or Technical Lead may perform bounded technical work without becoming the owner of strategy, brand, creative, finance, or routine operations.

Within an approved packet, Operations and its implementation agent may autonomously:

- validate current Shopify and POD availability, costs, variants, print constraints, and fulfillment facts;
- generate or select an initial Shopify direction within the approved creative specification;
- create and configure non-public products, collections, pages, and navigation;
- map approved products and print files in Printful or the selected provider;
- create or modify an unpublished theme;
- add approved assets and canonical metadata;
- implement approved prices, assortment rules, product disclosures, and size/care information;
- run validation and create rendered and operational evidence;
- correct ordinary implementation defects;
- reconcile Shopify and the POD provider against the canonical manifest and report exceptions.

ChatGPT is the preferred operating surface when it can complete a task safely and reliably. APIs/CLI should be used where deterministic bulk behavior, theme code, automated validation, recovery, or connector limitations make them more appropriate.

The Operations Manager role is defined but not yet separately staffed. Until recurring operations earn a specialist, Strategy Advisor is the interim accountable owner under an explicitly labeled **Operations** hat. Strategy and Operations outputs must remain separate, as defined in the [Operations Manager Methodology](./Operations-Manager-Methodology.md).

### Review

- Creative Director reviews the real rendered storefront and product presentation on representative mobile and desktop sizes.
- Brand Manager reviews brand and category comprehension.
- Operations Manager reviews catalog, POD mapping, variants, costs, disclosures, fulfillment assumptions, and reconciliation evidence.
- Finance Analyst reviews material unit-economics inputs when they change.
- Technical Reviewer independently checks implementation, measurement, privacy, integration behavior, failure modes, and scope.
- Operations or the implementation agent may fix routine defects without returning ordinary presentation choices to the Founder.

## Governance boundary

Creative and implementation autonomy does not grant publishing, financial, legal, privacy, or brand-safety authority.

The following require explicit Founder authorization for the exact action:

- making a storefront or theme public;
- enabling real customer purchasing when not already authorized;
- activating real payments or completing business/identity verification;
- authorizing a real POD fulfillment charge or automatic paid fulfillment;
- configuring or changing tax, legal, privacy, returns, or customer-service commitments;
- connecting or changing production domains;
- accepting material recurring platform/app expense;
- making an exceptional brand-safety decision.

Shopify's current AI integrations reinforce part of this boundary by preventing connected AI tools from editing or publishing the live theme and from changing settings such as payments, taxes, domains, or plan. Those vendor controls are helpful safeguards, not substitutes for company governance.

## Shopify AI Builder and Sidekick

Shopify AI storefront generation is a bootstrapping tool, not a source of truth. The Creative Director may ask it for multiple directions, evaluate the rendered candidates against explicit criteria, choose one, and revise it without altering locked product artwork.

Sidekick is an optional execution assistant for ad-hoc store and theme-editor work. It does not own brand or experiment decisions. Creative Director decides what should happen; Sidekick, ChatGPT, Codex, Claude, or another implementation agent may perform the approved change.

Customized theme code should be brought under Git control after a starting direction is selected. Shopify's GitHub theme integration can synchronize both GitHub-originated changes and Shopify-admin edits for connected branches, including unpublished themes. Shopify CLI can push and validate unpublished themes and return shareable preview information.

## Commerce modes on one customer surface

The same Shopify product and storefront substrate should support progressive evidence without a rebuild:

| Mode | Customer action | Operational state |
|---|---|---|
| Tier 2 intent | “I want this” / notify me | Products and presentation exist; purchasing remains unavailable |
| Checkout-ready private | Test checkout and fulfillment mapping only | Prices, variants, shipping, and POD mapping are prepared; store remains non-public and real charges are blocked |
| Tier 3 real-money | Purchase / preorder | Founder has separately authorized commerce activation and the required operating obligations are ready |

Preparing a checkout-ready backend is not permission to transact. The stronger purchase signal must be weighed against payment setup, tax and policy obligations, customer service, returns/replacements, and POD working-capital exposure. Current cost assumptions and formulas belong in the [Shopify and Meta Unit Economics Planning Model](../finance/Shopify-Meta-Unit-Economics-Planning-Model.md).

## Platform routing rule

Shopify is the **candidate default** for future T-shirt and other commerce wedges because the customer surface can progress from intent validation to purchasing without a later storefront rebuild.

Shopify becomes the default only if the feasibility spike demonstrates:

- same or better customer experience;
- preserved measurement integrity;
- materially less Founder intervention;
- materially shorter build-to-review time;
- acceptable creative control and Printful workflow.

Cloudflare remains the custom-store path when an experiment needs an unusual non-commerce experience, radically custom interaction, exceptional instrumentation control, or another requirement Shopify cannot meet efficiently. Historical WTD documents remain accurate records of the first custom Cloudflare MVV.

## Operator portability and recovery

Model portability means another capable agent can resume from canonical state. It does not require maintaining several fully active operator stacks.

After the feasibility spike succeeds, run one cold-standby reconstruction check: give another capable agent the canonical GitHub records and ask it to explain the experiment, identify the test products and `design_id` values, state the current authorization boundary, and name the next allowed action. Store access is not required for this first recovery proof.

Do not defer this proof until an outage. After it passes, maintain ChatGPT as the primary operator and reconnect another provider only when needed.

## Adoption state and unresolved questions

As of 2026-09-25:

- the target architecture and governance model are Founder-approved;
- Operations Manager is defined as the eventual commerce-operations owner but is not yet separately staffed; Strategy Advisor is the interim accountable owner;
- Shopify has not yet passed the platform feasibility spike;
- no Shopify store creation, connector authorization, paid plan, payment activation, or Printful charge is authorized by this document;
- the measurement implementation remains deliberately unresolved among existing D1, Shopify Customer Events, or a minimal hybrid;
- the first standardized POD recipe and product metafield schema remain to be tested;
- the exact division of connector work versus API/CLI work should be learned through execution, not predetermined for architectural purity.

## Current platform references

These vendor capabilities are implementation evidence and may change. Recheck them before execution:

- [Shopify plugin for ChatGPT: supported actions and limitations](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/shopify-plugin-for-chatgpt)
- [Shopify AI-tool authorization and store switching](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/authorizing-access)
- [Shopify GitHub integration for themes](https://shopify.dev/docs/storefronts/themes/tools/github)
- [Shopify CLI `theme push`](https://shopify.dev/docs/api/shopify-cli/theme/theme-push)
- [Shopify custom IDs through metafields](https://shopify.dev/docs/apps/build/metafields/working-with-custom-ids)

