---
title: TRACE Bestseller Creative Intelligence Methodology
owner: Creative Director
maintainer: Knowledge Librarian
status: Approved for calibration-first use — TRACE-PILOT-002 in progress
version: 0.3
last_updated: 2026-09-25
reviewed_by: Founder approved v0.3 for calibration-first actual run
---

# TRACE Bestseller Creative Intelligence Methodology

## Purpose

TRACE converts public evidence of probable T-shirt winners into reusable, original creative intelligence.

The method is designed to:

- scan broad winner pools without beginning from a target niche;
- distinguish sales-grounded evidence from reviews, search position, promotion, and other weaker signals;
- separate source-specific insider truths from transferable creative mechanisms;
- group copies and trivial variations before judging recurrence;
- preserve the difference between concept logic and apparel execution;
- generate original concepts rather than noun-swapped copies;
- connect every internal concept and test result back to its recipe lineage;
- improve through execution rather than becoming permanent doctrine before it is tested.

TRACE does **not** prove why an external product sold. Public marketplace evidence usually supports only:

> This is an eligible probable winner worth studying, and this is a candidate explanation for its resonance.

The method complements the [Creative Director Methodology](./Creative-Director-Methodology.md), [Creative Director T-shirt Design Playbook](./Creative-Director-Tshirt-Design-Playbook.md), [Research Methodology](./Research-Methodology.md), and [Minimum Viable Validation Methodology](./Minimum-Viable-Validation-Methodology.md).

## Status and version rule

Version 0.2 was frozen before the first calibration pilot at commit `c383e2d90619e594b38b65dbd3508638d6e845d0`. `TRACE-PILOT-001` executed against that commit, not this revision.

Version 0.3 is the evidence-backed revision approved for calibration-first use after the pilot. It is not considered calibrated until a retest executes its changed selection and record rules.

Never silently rewrite the rule set that governed an earlier scan. Record:

1. what the frozen rule required;
2. what occurred during execution;
3. any deviation and its reason;
4. the proposed change;
5. the evidence supporting that change.

## v0.3 change log

`TRACE-PILOT-001` justified the following minimum corrections:

- require a complete, timestamped sampling frame before ranked selection and stop deterministically when access fails;
- allocate Amazon sampling separately across Men's and Women's lists and preserve list/detail identifiers;
- make Etsy traversal, loading, review scope, recency, and evidence cohorts deterministic;
- require a timestamped Shopify/DTC panel lock, stronger native-sort verification, raw-rank preservation, and explicit store-failure states;
- require a recorded cross-market phrase/title/composition check and a closed provenance decision before any selected source is decoded;
- separate expression families, template clusters, mechanism clusters, and derivative saturation;
- permit `GRAMMAR-ONLY` and `NO-TRANSFERABLE-MECHANISM` outcomes instead of forcing every source into a semantic recipe;
- freeze independently sourced target truths before recipe clustering;
- label pilot concept seeds as noncommercial diagnostics subject to the normal Brand Handoff gate before advancement.

The execution evidence and change rationale are recorded in [`TRACE-PILOT-001`](../creative/trace/pilots/TRACE-PILOT-001.md).

---

# 1. Core architecture

TRACE keeps source evidence, niche truth, transferable mechanism, visual grammar, and internal outcomes separate.

## External learning path

> **Source evidence → Source Decode Card → Niche-agnostic Concept Recipe**

The Source Decode Card may contain the source design's niche, customer identity, and insider truth.

The Concept Recipe must remove those source-specific inputs.

## Internal creation path

> **Concept Recipe + independently documented Target-Niche Truth + Apparel Grammar → Original Concept → Market Test**

This distinction corrects a potentially misleading use of the word *recipe*.

The following is a **Concept Instantiation Brief**, not a pure recipe:

> For **[target micro-identity]** in **[recognizable situation]**, combine **[familiar frame]** with **[target-niche truth]** through **[concept mechanism]** to produce **[emotional/social payoff]**, expressed through **[apparel grammar]**.

The reusable recipe itself is narrower:

> Given **[a familiar cognitive frame]** and an input with **[an abstract property, constraint, or behavior]**, apply **[operation]** so the audience resolves **[tension]** into **[payoff]**.

The source insider truth never becomes a fixed ingredient of the recipe.

---

# 2. Gate 0 — Eligibility and contamination filter

Every encountered listing receives an eligibility disposition before semantic decoding.

## 2.1 Dispositions

| Disposition | Meaning | Downstream use |
|---|---|---|
| `ELIGIBLE` | Fixed graphic T-shirt with sufficiently attributable public demand evidence and no disqualifying dependency | May enter evidence qualification and decoding |
| `IP-EXCLUDED` | Demand plausibly depends materially on third-party fandom, fame, protected expression, or another excluded source | Keep a minimal audit record; do not decode or cluster |
| `IP-QUARANTINE` | Ownership, origin, quotation, character, meme, or licensing dependency cannot be resolved confidently | Cannot support a recipe until resolved |
| `BRAND-EXCLUDED` | Demand plausibly depends materially on the source seller's own established logo or brand equity rather than the transferable design concept | Keep a minimal audit record; do not decode or cluster |
| `EVIDENCE-QUARANTINE` | Sampling-frame, identifier, sales-floor, or other evidence conflict prevents reliable selection | Preserve the conflict; cannot support a recipe until resolved |
| `DUPLICATE-FAMILY` | The artwork or commercial expression belongs to an already recorded expression family | Retain as spread/saturation evidence only |
| `ATTRIBUTION-EXCLUDED` | Reviews, sales signal, or listing structure cannot be attributed to the visible design | Keep a minimal audit record; do not decode |
| `PRODUCT-EXCLUDED` | Plain apparel, digital file, template, multipack, personalized blank, or other product outside the fixed graphic-shirt unit | Keep a minimal audit record; do not decode |

## 2.2 Hard IP and brand-dependency exclusion

Exclude even when the seller may hold a valid license. TRACE is not deciding whether a listing infringes; it is preventing brand-driven demand from contaminating creative inference.

Use `IP-EXCLUDED` for third-party fame, fandom, protected-expression, or organization dependence. Use `BRAND-EXCLUDED` when the source seller's own established logo or brand equity is the primary demand mechanism.

Automatically exclude:

- recognizable entertainment franchises, characters, films, television, games, comics, and anime;
- sports teams, leagues, colleges, and identifiable organization insignia;
- musicians, bands, celebrities, athletes, influencers, and their associated catchphrases;
- corporate logos, branded slogans, mascots, and recognizable trade dress;
- song lyrics, movie or book quotations, album or poster art, and famous photographs;
- fan art, mashups, "inspired by" goods, and seller-claimed parody;
- products whose primary appeal is an established seller or lifestyle-brand logo;
- apparent pirated copies or disputed source artwork.

Quarantine rather than guess when:

- a phrase may originate in entertainment, music, sports, or a public personality;
- a supposedly generic design appears across many sellers and its origin is unclear;
- a public-domain subject uses a potentially protected modern adaptation;
- stock art, photograph, or illustration ownership is unclear;
- licensing or parody is asserted but not verifiable.

A useful screening question is:

> Would the product's appeal remain intelligible if every famous name, character, logo, quotation, and brand association disappeared?

If no, exclude. If uncertain, quarantine.

Excluded and quarantined designs receive no mechanism tags, Source Decode Card, or corroboration credit. If a source is later found to be IP-dependent, remove its support from every affected recipe.

Record a basis for every provenance-confidence value. `UNRESOLVED` always maps to `IP-QUARANTINE`. `LOW` may remain `ELIGIBLE` only when the record explains why no concrete third-party, copy-family, disputed-artwork, or protected-adaptation signal was observed; otherwise quarantine it. `MEDIUM` and `HIGH` also require a stated basis, such as a seller authorship claim, documented commission, or traceable original source. These values are research controls, not copyright ownership findings or legal clearance.

When later audit changes an execution-time eligibility decision, preserve the original observation and selection state, add the controlling final disposition, remove the source from downstream support, and do not backfill unless the preregistered procedure defined a deterministic backfill rule.

## 2.3 Required cross-market origin check

Before marking a candidate `ELIGIBLE`, assigning an SDC, or using it for apparel grammar, run and record all three searches:

1. the exact distinctive wording in quotation marks, when text exists;
2. the exact or minimally cleaned distinctive product title, excluding generic garment and gift terms;
3. a concise query for the distinctive subject/action/composition or visual metaphor.

Search the source platform and either the open web or at least one unrelated marketplace. Record the queries, date, representative URLs, and the analyst's comparison. A reverse-image search may supplement this check when available, but it is not required for the first v0.3 retest.

Apply these decisions:

- materially matching wording plus subject, action, composition, or punchline across unrelated sellers with no traceable origin: `IP-QUARANTINE`;
- a distinctive quotation, meme, illustration, photograph, or stock design whose creator or rights source remains unresolved: `IP-QUARANTINE`;
- a traceable entertainment, celebrity, sports, organization, or other fame-dependent source: `IP-EXCLUDED`, even when licensed;
- a seller authorship claim may support provenance, but it does not override contradictory earlier publication, stock-library evidence, or unresolved cross-seller recurrence;
- recurrence alone is not an infringement finding. It is a contamination signal that prevents TRACE from treating the expression as independent creative evidence.

Quarantine may be cleared only when the record identifies a traceable creator/rights source or demonstrates that the candidate's expression is materially distinct from the recurring results. Record who made that decision and the evidence used.

Close the final Gate 0 disposition before SDC creation and mechanism clustering. Do not use a quarantined/excluded source for recipe, grammar, maturity, or transfer support. Do not replace an audit failure after synthesis unless a deterministic backfill rule was preregistered.

## 2.4 Other confounders

The following do not automatically disqualify a source, but must be tagged:

- holiday, election, news, or event timing;
- personalization;
- exceptional discounting;
- unusually strong seller or influencer audience;
- cause affiliation;
- garment-quality or price advantage;
- advertising or privileged placement;
- listing age;
- review pooling;
- seasonality;
- seller-written bestseller claims.

---

# 3. T — Triangulate probable winners

## 3.1 Governing rules

1. Start with broad T-shirt winner pools, not target niches.
2. Use each platform's strongest available product-level demand signal.
3. Preserve raw platform evidence instead of forcing unlike signals into one numerical score.
4. Record all inspected results and exclusion reasons.
5. Do not choose sources because the analyst finds them clever or attractive.
6. Freeze UTC start/end times, observation date, locale, query, sort, position, final URL, access/render mode, and source freshness.
7. Repeated presence across nonadjacent scans strengthens confidence but still does not prove causality.
8. Call products *probable* or *apparent* winners unless actual sales are known.
9. A ranked pool may contribute selections only when its complete protocol-defined frame is retrievable and timestamped. Preserve a partial or failed pool as audit evidence with zero selections; other independent precommitted pools may continue when their platform protocol permits, but the missing quota stays empty.
10. Search snippets, cached fragments, isolated product pages, third-party roundups, and partial search results may corroborate fields but must not reconstruct a ranked pool.
11. After one direct retrieval and one ordinary browser retrieval fail in the same execution window, allow at most one ordinary reload, mark the pool `BLOCKED`, log the responses, and stop. Do not evade access restrictions or backfill the quota elsewhere.

## 3.2 Amazon protocol

Primary source pools:

- Amazon Best Sellers — Men's Novelty T-Shirts;
- Amazon Best Sellers — Women's Novelty T-Shirts.

For each scan:

1. satisfy the complete-frame access prerequisite for both Top 100 pools in the United States store;
2. timestamp the list capture and preserve every traversed rank, including exclusions;
3. record the list-surface item ID/link, parent ASIN when exposed, selected child ASIN, displayed list rank, detail-page BSR/category, and capture timestamps;
4. when a list identifier/badge and detail-page identifier/BSR cannot be reconciled, assign `EVIDENCE-QUARANTINE` rather than choosing the more convenient value;
5. record any displayed recent-purchase band, such as an `X+ bought in past month` estimate;
6. record rating and review count only as corroboration and inspect whether they are pooled across different graphics;
7. collapse sizes, colors, fits, duplicate ASINs, sellers, and copied art into one expression family while preserving every raw rank;
8. exclude plain basics, category pollution, licensed/IP-dependent goods, brand merchandise, and mixed-design variation families;
9. record seller of record, manufacturer, fulfillment service, and commercial design source separately;
10. apply the three-family cap to the visibly responsible independent commercial design source/brand/store; if that commercial source cannot be attributed, use `ATTRIBUTION-EXCLUDED`, while unresolved artwork or expression provenance remains `IP-QUARANTINE`;
11. never treat keyword-search order, sponsored placement, snippets, or third-party estimates as a sales rank.

The Amazon target is six eligible expression families from Men's and six from Women's. These are separate ordinals: process Men's first and Women's second, never compare their raw rank numbers, and never transfer unused quota between them. Within each pool, traverse rank order until six expression families unique across the combined Amazon sample are selected or the complete pool is exhausted. An expression family already selected from the other pool is recorded as a duplicate and does not satisfy the second quota.

Amazon sources:

- https://www.amazon.com/Best-Sellers-Men%27s-Novelty-T-Shirts/zgbs/fashion/9056987011
- https://www.amazon.com/Best-Sellers-Women%27s-Novelty-T-Shirts/zgbs/fashion/9056923011
- https://sell.amazon.com/blog/amazon-best-sellers-rank
- https://sell.amazon.com/blog/product-ideas

Amazon is the pilot's closest approximation to a broad sales-ranked census. Rank is still category-, marketplace-, and time-specific.

## 3.3 Etsy protocol

Etsy exposes no public best-selling sort. It is therefore a structured candidate search, not a complete market census.

Use this fixed non-niche query bank:

1. `graphic t shirt`
2. `funny t shirt`
3. `novelty t shirt`
4. `text t shirt`
5. `illustrated t shirt`
6. `retro graphic t shirt`

Execute query-major in the listed order: `Most relevant`, then `Top reviews`, before advancing to the next query. Freeze `instant_download=false` so digital items are excluded intentionally rather than through accidental session state.

For each query/sort surface:

1. use a signed-out/private United States session;
2. preserve country, language, currency, ship-to location, full result URL, and timestamp;
3. capture the first 12 organic results, recording interleaved ads separately and excluding ad positions from demand inference;
4. if fewer than 12 organic cards load, perform no more than three ordinary scroll/wait cycles of up to five seconds each; if the surface still falls short, mark it `PARTIAL`, retain its cards as audit evidence only, and give the surface zero selection or first-occurrence credit; other complete frozen surfaces may continue, but do not substitute results or transfer the missing quota;
5. make a title/thumbnail Gate 0 disposition for every captured organic result and open every candidate not objectively excluded at that surface;
6. distinguish item-specific counts and dates from same-print, mixed-listing, and shop-wide reviews;
7. record Etsy's own Bestseller badge when present, item-specific review volume, latest displayed item-review date, and provenance confidence;
8. treat favorites, cart notices, views, search position, and shop totals as discovery/context only;
9. exclude digital art files, personalization services, mixed-design listings, IP-dependent goods, and unclear review pools.

Select two six-family evidence cohorts, subject to the commercial-source cap:

1. `RECENT-SALES-BADGE`: six eligible official-Bestseller expression families, ordered by item-specific review count descending, latest displayed item-review date descending, cleaner design attribution, then earlier first occurrence;
2. `ITEM-REVIEW-DEPTH`: six eligible non-badged expression families with at least 100 item-specific reviews and an item review displayed within the previous 180 days, ordered by review count descending, latest review date descending, cleaner attribution, then earlier first occurrence.

Do not compare the two cohorts as one sales ranking or transfer unused quota between them. A shortfall remains incomplete. This stratification preserves Etsy's recent-sales badge without allowing it to erase deeper item-attributed evidence.

Etsy sources:

- https://help.etsy.com/hc/en-us/articles/115015627947-How-to-Search-for-Items-and-Shops-on-Etsy
- https://www.etsy.com/legal/policy/search-advertisement-recommendation/899478564529
- https://help.etsy.com/hc/en-us/articles/115015745808-How-Ads-Are-Placed-in-Etsy-Search
- https://help.etsy.com/hc/en-us/articles/360000572708-How-the-Review-System-Works-for-Sellers

Search position, `Top reviews` position, Star Seller status, shop totals, and seller-written "bestseller" claims are discovery or context only. Generic cause language may remain eligible with a cause-affiliation confounder; dependence on a named public figure, organization, entertainment property, or protected mark is excluded or quarantined under Gate 0.

## 3.4 Shopify / DTC protocol

There is no cross-store Shopify bestseller leaderboard. Use a precommitted panel of independent, T-shirt-led stores.

Store eligibility:

- sells a meaningful fixed graphic-T-shirt assortment;
- is not principally a licensed-franchise, sports, celebrity, or logo-merchandise business;
- exposes a broad tees/all-products collection;
- provides a verifiable native `Best selling` order or an equivalently documented sales-grounded order;
- is selected before inspecting which individual designs appear first.

Before ranked-product inspection, lock a timestamped panel of 12 eligible independent stores containing store, URL, eligibility basis, intended broad collection, and expected native-sort verification. Assortment/category inspection is allowed only to establish panel eligibility; ranked-result inspection begins only after all 12 stores are locked.

Process stores in the locked order. Select at most one expression family per store: the highest-ranked family within the captured pool that clears final Gate 0 and family deduplication. A store that becomes inaccessible, fails native-sort verification, changes assortment, or yields no eligible family leaves an empty slot. Do not substitute another store, take a second family from a successful store, or move the unused quota to another platform.

For each eligible store:

1. use the broadest genuine T-shirt collection, or the all-products collection when necessary;
2. verify all three native-sort conditions: broad collection scope, an explicit `sort_by=best-selling` request, and a returned interface/HTML state showing `Best selling` active, selected, or checked;
3. do not rely on a page title or merchant-curated "Bestsellers" collection alone;
4. capture the first 24 raw product cards, or document that the complete broad collection contains fewer than 24, and preserve `RAW_PRODUCT_RANK` before eligibility or family collapse; an incomplete, unbounded capture contributes no selection;
5. assign `FAMILY_FIRST_RANK` and record all `DUPLICATE_RANKS`; continue past rank 24 only when a separately preregistered distinct-family quota requires it;
6. record store, collection scope, URL, observation date/time, and access mode (`LIVE-HTML`, `SEARCH-INDEX`, or `BLOCKED`);
7. record product-review scope as `ITEM-VISIBLE`, `ITEM-STRUCTURED`, `SAME-FAMILY`, `SHOP-WIDE`, or `UNCLEAR`, preserving conflicting counts separately;
8. record `NONZERO-SALES-CORROBORATION` as `YES`, `NO`, or `UNVERIFIED`; an uncorroborated rank may be decoded but cannot independently raise recipe maturity;
9. never compare a #1 rank in one store numerically with a #1 rank in another.

If a locked store later fails, record exactly one primary failure code: `ACCESS`, `SORT-UNVERIFIED`, `NO-BROAD-COLLECTION`, `ASSORTMENT-CHANGED`, or `NO-ELIGIBLE-FAMILY`. Do not replace it after ranked results have been inspected.

Shopify documents native `Best selling` as the all-time number of orders containing the product. It is a meaningful within-store lifetime ordinal signal, not recent velocity, unit sales, revenue, margin, or global demand. When no products have sales, the order can fall back to creation date; this is why nonzero-sales corroboration is recorded separately.

Use the following acceptance rule:

| Value | Minimum recorded basis | Downstream effect |
|---|---|---|
| `YES` | Product- or same-expression-family evidence that necessarily implies at least one completed order, such as an attributable verified-buyer review, a platform-provided sold/order count, or another documented first-party sales statement | May contribute Shopify/DTC support to recipe maturity when every other eligibility and independence rule passes |
| `NO` | Reliable first-party or platform evidence that the product has no completed orders | May be retained as a ranked observation, but cannot become a Source Decode Card or support maturity |
| `UNVERIFIED` | No reliable product/family evidence resolves whether the native rank reflects a nonzero order count; shop-wide reviews, page views, likes, and rank alone do not qualify | May be decoded as a hypothesis when otherwise eligible, but cannot independently raise recipe maturity |

Record the evidence type, scope, and URL or field used for `YES` or `NO`. Do not infer `YES` merely because a product appears first in a native best-selling collection.

Shopify source:

- https://help.shopify.com/en/manual/products/collections/collection-layout

For a custom or headless storefront that does not honor native sorting, mark the order unverified. A merchant-curated "Bestsellers" page is moderate evidence at most and does not satisfy the frozen native-sort panel without an explicitly preregistered alternate cohort.

## 3.5 Evidence vector

Do not collapse unlike platform signals into one synthetic score.

Record four independent dimensions:

| Dimension | Values |
|---|---|
| Demand signal | `SALES-RANKED`, `PLATFORM-BADGED`, `WITHIN-STORE-SALES-ORDER`, `STRONG-PROXY`, `DISCOVERY-ONLY` |
| Design attribution | `EXACT`, `SAME-PRINT-VARIANTS`, `MIXED`, `SHOP-LEVEL`, `UNCLEAR` |
| Currency | `RECENT`, `LIFETIME`, `CURRENT-SNAPSHOT-UNKNOWN-WINDOW`, `STALE` |
| Persistence | `SINGLE-SNAPSHOT`, `REPEATED`, `UNKNOWN` |

Also record, without folding them into the vector:

- review scope;
- provenance confidence: `HIGH`, `MEDIUM`, `LOW`, or `UNRESOLVED`;
- access/render mode;
- identifier alignment when a platform exposes parent/child or list/detail IDs;
- commercial design source separately from seller of record;
- nonzero-sales corroboration where the platform order can contain a zero-sale fallback.

Core decoding normally requires:

- a sales-grounded signal or unusually strong item-specific corroboration; and
- `EXACT` or defensible `SAME-PRINT-VARIANTS` attribution.

Evidence qualifies a source for study. It does not establish that the decoded mechanism caused sales.

## 3.6 Expression families and derivative clusters

The evidence lineage is:

> `POOL → observation → expression family → Source Decode Card → template cluster (optional) → mechanism cluster → recipe → transfer test`

Assign stable IDs at each joining level used downstream:

- `OBSERVATION_ID` identifies one captured ranked/search occurrence;
- `EXPRESSION_FAMILY_ID` joins every occurrence of the same commercial expression;
- `SDC_ID` identifies the single Source Decode Card created from an eligible selected expression family.

Selection fields belong only to the canonical observation chosen to represent an expression family. Recipe and grammar records join through `EXPRESSION_FAMILY_ID` and `SDC_ID`, never through a title or mutable rank alone.

- Same art/expression across sizes, colors, fits, ASINs, listings, or sellers: one expression family.
- Cosmetic redraws preserving the same central wording, subject, joke, and composition: one clone-linked expression family for sampling, with the relationship recorded.
- A noun-swapped sentence, subject substitution, or other reusable scaffold creates a separate expression family linked to a shared template cluster.
- Different wording, scenario, niche truth, and visual expression using the same abstract cognitive operation: a potential independent mechanism analogue.

Sample quotas count eligible expression families. Clone and template-derivative recurrence indicates spread or saturation; it never independently corroborates a recipe.

Use the normative Gate 0 disposition values in new records. If historical execution evidence contains a local label, preserve it and add an explicit crosswalk to the normative value; do not silently rewrite the raw observation.

---

# 4. R — Reverse-engineer resonance

Create one Source Decode Card for each selected eligible expression family.

Separate observed facts from analytical hypotheses.

Every card receives exactly one primary outcome:

| Outcome | Meaning | Downstream use |
|---|---|---|
| `RECIPE-CANDIDATE` | Supports a discriminating frame/operation/tension/reveal hypothesis | May support a mechanism cluster and recipe |
| `GRAMMAR-ONLY` | Supports an apparel-grammar hypothesis but no defensible semantic recipe | May support apparel grammar only |
| `NO-TRANSFERABLE-MECHANISM` | Observed demand cannot be translated into a useful transferable mechanism | Retain the source record; do not force abstraction |

Optional secondary tags do not change the primary outcome. Only `RECIPE-CANDIDATE` cards may independently support a concept recipe.

## 4.1 Required fields

### Source and evidence

- SDC ID
- Expression-family ID
- Canonical observation ID
- Platform
- Seller / store
- Listing title and URL
- Observation date and UTC capture time
- Access/render mode and source freshness
- Raw rank, query, sort, and position
- Evidence vector
- Eligibility disposition
- Final Gate 0 reviewer and closeout time
- Provenance confidence and rationale
- Cross-market origin-check queries and representative URLs
- Duplicate/template-family relationship
- Primary outcome
- Template-cluster relationship, when any
- Known limitations

### Observed expression

- Exact or minimally necessary wording
- Subject and imagery
- Props and setting
- Graphic hierarchy
- Typography role
- Architecture, scale, palette, texture, and garment integration
- What reads first at feed or ten-foot distance
- What rewards closer inspection

### Source-specific context

- Apparent micro-identity or niche, when useful
- Recognizable behavior, ritual, situation, frustration, or worldview
- Source-specific insider truth, when it actually powers the concept
- Public identity signal
- Emotional or social payoff
- Wearability, giftability, and social-risk level

### Candidate explanation

- Setup and reveal
- Candidate semantic or visual mechanism
- Likely role: attention, recognition, product desire, gifting, aesthetic desire, or mixed
- Alternative explanations for apparent success
- Analyst confidence

### Transfer prohibition

Record the source-specific elements that may not move into creative generation:

- wording or close paraphrase;
- phrase scaffold when distinctive;
- subject/action pairing;
- character, pose, props, or scene;
- central punchline;
- recognizable visual metaphor;
- composition or illustration;
- distinctive palette, lettering, or overall commercial impression.

The source niche and insider truth remain on this card. They do not become fixed recipe ingredients.

## 4.2 Five-card calibration gate

After the first five eligible Source Decode Cards, pause before creating the sixth card or beginning mechanism clustering. Record the UTC checkpoint time, reviewer, and outcome, then verify:

- observed facts and analytical hypotheses remain visibly separate;
- source-specific truths remain attached to their source niche;
- mechanism labels discriminate rather than restate broad style or humor;
- Gate 0, provenance, identity, and primary-outcome fields are complete and usable;
- no excluded or quarantined source has received decode, grammar, or recipe credit.

Do not change the frozen sampling or selection rules at this checkpoint. Log any proposed methodology change for the debrief and continue only after the checkpoint record is complete.

---

# 5. A — Abstract the recipe

TRACE maintains three different reusable resources.

## 5.1 Concept Recipe Library

Contains niche-agnostic cognitive or emotional mechanisms.

## 5.2 Niche Truth Registry

Contains evidence-backed, community-specific behaviors, rituals, tensions, frustrations, worldview, language, and competence signals.

A truth record must include its ID, canonical niche/R-ID, exact evidence citation, source blob or commit, provenance type, observation/inference status, and independence status.

A source-decoded truth remains a hypothesis attached to its source niche. It cannot be used as an independent transfer input until it is supported in canonical community research.

Before recipe clustering, freeze the transfer panel. For TRACE, "unrelated" normally means distinct canonical R-IDs. Each promoted recipe is tested once against every frozen panel identity; convenient truths may not be chosen after seeing the recipe.

## 5.3 Apparel Grammar Library

Contains transferable visual structures and presentation choices, including:

- architecture;
- scale;
- hierarchy;
- typography role;
- palette relationship;
- texture logic;
- garment integration;
- feed comprehension.

Style is not assumed to be causal and is not automatically bundled into a concept recipe.

## 5.4 Recipe template

> Given **[a familiar cognitive frame]** and an input possessing **[an abstract property, constraint, or behavior]**, apply **[reversal, removal, escalation, contradiction, literalization, compression, juxtaposition, etc.]** so the audience resolves **[tension or incongruity]** into **[emotional/social payoff]**.

## 5.5 Recipe validity tests

A valid recipe must:

1. contain no source niche, identity label, animal, profession, hobby, character, exact wording, punchline, or distinctive composition;
2. describe the transformation that creates the payoff;
3. be specific enough to generate and reject concepts;
4. be instantiable with at least three unrelated niche truths;
5. survive the **source-erasure test**: a reader should not reconstruct the source shirt from the recipe;
6. distinguish required, tunable, optional, and prohibited ingredients;
7. be more informative than "use humor," "make it relatable," or "make it vintage."

## 5.6 Recipe fields

- Recipe ID and version
- Neutral label
- Mechanism fingerprint: frame, operation, tension, reveal, payoff
- Required ingredients
- Tunable ingredients
- Optional ingredients
- Anti-ingredients
- Compatible emotional payoffs
- T-shirt comprehension and wearability constraints
- Failure conditions
- Supporting expression-family IDs and SDC IDs
- Independence/derivative assessment
- Source-specific elements prohibited from transfer
- Derivative saturation: `NONE`, `LOW`, `MEDIUM`, `HIGH`, or `UNKNOWN`
- Maturity state
- Internal test history

## 5.7 Maturity states

| State | Requirement |
|---|---|
| `CANDIDATE` | Extracted from one eligible expression family and its Source Decode Card |
| `PROVISIONALLY-CORROBORATED` | At least two non-derivative mechanism analogues from unrelated niches and independent sellers |
| `CORROBORATED` | At least three non-derivative expression families across at least two unrelated niches and two independent sellers |
| `INTERNALLY-TESTED` | One original instantiation received a predeclared behavioral test |
| `REPLICATED` | At least two materially different original concepts or niche-truth inputs show the relevant behavior |
| `RETIRED` | Weak internal results, saturation, originality risk, or loss of relevance |

Cross-platform support strengthens confidence but is not required. The same copied design across platforms remains one family.

Corroboration maturity and derivative saturation are separate dimensions. Clones, template derivatives, and repeated expressions can raise saturation but never maturity.

External recurrence supports the existence of a pattern. It does not prove causality.

Before assigning or raising maturity, maintain a support-audit matrix with one row per credited SDC and one column per required recipe ingredient. Every credited source must demonstrate every required ingredient in its observed record. An ingredient introduced, tightened, or clarified during transfer testing is a new candidate refinement; it cannot retroactively increase external maturity. Reclassify unsupported ingredients or remove the source, then recalculate maturity.

---

# 6. C — Create at a safe distance

Creative work begins with an independently documented target-niche truth, not a noun swap from the source.

## 6.1 Clean handoff

The concept-generation input should contain:

- the abstract recipe;
- the target-niche truth;
- a selected apparel grammar;
- intended identity signal and payoff;
- the source-prohibited-elements list.

Do not provide competitor artwork as an image-generation reference or ask for work "in the style of" a seller, artist, or brand.

Method-calibration concept seeds are **noncommercial diagnostic slot-fills**. They are not product recommendations, MVV inputs, production-cleared designs, or legal clearance. Any seed proposed for advancement must first pass the [Creative Director Methodology](./Creative-Director-Methodology.md) Brand Handoff Integrity Check and the normal concept, design, clearance, and validation gates.

## 6.2 Concept Lineage Card

Record:

- Recipe ID/version
- Target niche and truth ID
- How abstract slots were instantiated
- Proposed wording and imagery
- Apparel grammar
- Intended identity signal and payoff
- Intended role: attention, wearability, gifting, aesthetic desire, or product desire
- Supporting expression-family and SDC lineage
- Originality-distance assessment
- Test hypothesis and required evidence

## 6.3 Originality gate

Compare the proposed concept with every supporting source across:

- wording and syntax;
- subject and prop;
- scenario and insider truth;
- setup/reveal relationship;
- visual metaphor;
- pose and composition;
- typography and styling;
- overall commercial impression.

Reject when the result preserves a distinctive phrase scaffold, signature subject/action pairing, central punchline, or recognizable composition.

Use two practical tests:

### Back-reference test

Would a person familiar with the source call the result "a version of that shirt"?

If yes, reject.

### Independent-truth test

Did the target truth exist in the Niche Truth Registry independently of this source?

If no, investigate noun-swap or source-drift risk.

Also apply the concept-stage recognition, wearability, distinctiveness, feed-comprehension, and garment-integration checks in the [Creative Director T-shirt Design Playbook](./Creative-Director-Tshirt-Design-Playbook.md). A transfer test that passes source distance can still fail as a T-shirt.

Before production, run exact-phrase and close-variant marketplace/web searches, appropriate trademark searches, and artwork-provenance checks. These are operational safeguards, not legal advice or a legal safe harbor.

Relevant references:

- https://www.copyright.gov/circs/circ33.pdf
- https://www.uspto.gov/trademarks/search/likelihood-confusion
- https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks

Avoid storing full-resolution competitor artwork in the public repository. Preserve URLs, timestamps, factual notes, and only the minimum reference evidence needed.

---

# 7. E — Experiment and evolve

Every internal test preserves this lineage:

> `recipe_version + target_truth_id + apparel_grammar_id → concept_id → design_id → creative_id/source card → downstream behavior`

Do not collapse all evidence into "winner."

| Evidence facet | Example observations | What it can support |
|---|---|---|
| Attention | Delivery, thumb-stop behavior, CTR | Acquisition/attention hypothesis |
| Product interest | Design view, enlargement, product interaction, opt-in | Downstream product-interest hypothesis |
| Purchase intent | Preorder or transaction | Purchasing hypothesis |
| Wearability | Qualitative identity recognition and objections | Wearability/identity hypothesis |

A high-CTR acquisition creative may support an attention mechanism without validating shirt demand. Meta delivery or carousel reordering is not product preference.

Promote a recipe's maturity only when the behavior relevant to that recipe is replicated across materially different original applications.

Preserve recipe versions and historical outcomes rather than overwriting inconvenient evidence.

---

# 8. Minimum logical records

These may begin as Markdown and CSV files. Separate databases are not required.

| Record | Function |
|---|---|
| Bestseller Scan Register | Raw observations, platform evidence, dates, IP status, provenance-search queries/URLs, final dispositions, observation IDs, expression-family IDs, and limitations |
| Source Decode Cards | Source-specific truth, observed expression, candidate mechanism, apparel grammar, payoff, and confounders |
| Concept Recipe Library | Niche-agnostic mechanisms, ingredients, supporting independent expression families and SDCs, maturity, and versions |
| Niche Truth Registry | Niche-specific observations maintained independently of recipes |
| Apparel Grammar Library | Transferable visual hierarchies and presentation structures |
| Concept Lineage and Test Log | Recipe/truth/grammar pairing, originality check, resulting design/creative, and separated outcomes |

---

# 9. Historical appendix — TRACE-PILOT-001 v0.2 preregistration

This section preserves the first pilot's frozen rules for auditability. It is historical and must not be read as overriding the v0.3 procedures above. The exact governing version remains commit `c383e2d90619e594b38b65dbd3508638d6e845d0`.

## 9.1 Objective

Test whether v0.2 can:

1. identify eligible probable winners reproducibly;
2. keep source truths separate from recipes;
3. distinguish copies from independent analogues;
4. produce recipes specific enough to guide and reject concepts;
5. produce original applications without source drift;
6. remain operationally manageable.

## 9.2 Frozen sample

Target **36 eligible design families**:

- 12 Amazon;
- 12 Etsy;
- 12 Shopify/DTC.

Rules:

- no target-niche searching in the initial discovery scan;
- no more than three eligible families from one seller/store;
- use only predeclared platform procedures;
- preserve all inspected exclusions;
- do not replace weak or inconvenient sources with preferred designs;
- do not backfill a failed platform quota from another platform;
- if a platform cannot produce 12 defensible families within its frozen scan, record an incomplete stratum as a methodology finding.

### Amazon selection

Inspect both complete Top 100 pools. After exclusions and family deduplication, choose the 12 highest-ranked eligible distinct families using the best displayed qualifying rank. Break ties by stronger design attribution, then by recent-demand corroboration. Do not use analyst taste as a tiebreaker.

### Etsy selection

The frozen query bank and result depth create at most 144 raw organic observations before deduplication: six queries × two sorts × first 12 organic results. Select up to 12 eligible families by:

1. official Etsy Bestseller badge;
2. stronger item-specific review evidence and recency;
3. cleaner design attribution;
4. earlier first occurrence in the frozen scan order.

### Shopify/DTC selection

Preselect 12 eligible independent stores before inspecting their best-selling designs. Capture the first 24 design families from each verified broad best-selling collection. Select the highest-ranked eligible family from each store first. If a store yields no eligible source, record that failure rather than substituting a design based on taste. A second family may be taken from a store only if needed after every preselected store has been processed, subject to the three-family cap.

## 9.3 Calibration checkpoint

After five Source Decode Cards:

- inspect whether observed facts and interpretations are separated;
- check whether insider truths remain source-bound;
- check whether mechanism labels are discriminating rather than vague;
- check whether the record is usable without adding unregistered fields.

Do not change selection rules at this checkpoint. Log proposed methodology changes for the debrief.

## 9.4 Pilot synthesis

After all available eligible families are decoded:

1. cluster by mechanism fingerprint;
2. identify clones and template derivatives separately;
3. create candidate recipes;
4. promote no more than the three best-supported recipes;
5. test each promoted recipe against three unrelated target-niche truths;
6. include at least one truth from [R027 — Preservation-Minded Old-House People](../Researches/R027-Old-House-Restorers-Historic-Home-People.md);
7. apply the originality and T-shirt-fit gates;
8. create no final artwork or commercial listing during this methodology pilot.

## 9.5 Pilot success criteria

The pilot succeeds when it produces an auditable answer to each question below, even if no recipe reaches corroborated status.

- Could another reviewer reproduce why each source was included or excluded?
- Did any IP-dependent or brand-driven source contaminate recipe support?
- Were copies prevented from masquerading as independent confirmations?
- Did the Source Decode Cards preserve niche truths without binding them to recipes?
- Could recipes be instantiated across unrelated truths?
- Could the method reject derivative or unwearable concepts?
- Which fields were consistently useful, unused, ambiguous, or unavailable?
- What should change in v0.3?

## 9.6 Required outputs

- frozen v0.2 commit reference;
- scan register;
- source decode cards;
- recipe library;
- niche-truth and apparel-grammar references used in the transfer test;
- pilot debrief;
- proposed v0.3 change log, if warranted;
- clear recommendation: adopt, revise and retest, or retire TRACE.

---

# 10. Principal failure modes

Guard against:

- mistaking visible popularity for causal proof;
- counting copies as independent winners;
- letting licensed or famous IP contaminate mechanism evidence;
- assigning shop-wide or pooled reviews to one design;
- treating search position or advertising as sales rank;
- comparing unlike platform metrics on one scale;
- cherry-picking witty or aesthetically preferred designs;
- interpreting a style as the entire reason for demand;
- overabstracting a recipe into a platitude;
- leaving the original niche or insider truth inside the recipe;
- carrying a distinctive phrase scaffold into another niche;
- confusing saturation with opportunity;
- confusing acquisition attention with product desire;
- ignoring price, audience, promotion, age, seasonality, or seller strength;
- allowing undocumented methodology or recipe drift;
- generating a noun-swapped copy and calling it original.

---

# 11. Evolution rule

TRACE should remain minimum-sufficient.

Add complexity only when the pilot exposes a recurring decision problem that the existing records cannot resolve.

A methodology revision should name:

- the observed problem;
- affected pilot records;
- why the existing rule was insufficient;
- the smallest proposed correction;
- whether existing evidence must be reclassified.

The company is building a learning system, not a permanent taxonomy.

> **Study provenance-cleared probable winners to identify candidate demand mechanisms and apparel grammar; separate those mechanisms from source-specific truths; recombine them with independently earned target truths; preserve originality and lineage; and let the company's own behavior data revise the recipes.**
