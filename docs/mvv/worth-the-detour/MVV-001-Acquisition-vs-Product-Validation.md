---
title: MVV-001 Acquisition vs Product Validation
brand: Worth the Detour
experiment_id: mvv-r012-001
status: Proposed
version: 0.1
last_updated: 2026-08-17
governing_methodology: docs/company/Minimum-Viable-Validation-Methodology.md
related_schema: docs/mvv/worth-the-detour/MVV-001-Event-Schema.md
---

# MVV-001 Acquisition vs Product Validation

## Purpose

This document records a specific operating principle for **Worth the Detour MVV #1**:

> **Do not assume that the T-shirt designs that perform best as Meta ads will also be the T-shirt designs customers most want once they can inspect them properly.**

A design can be a strong product but a weak acquisition creative.

Some T-shirt designs may require a few seconds of attention, closer inspection, or larger presentation before their idea becomes clear. Those designs may perform poorly during fast mobile social scrolling even if customers like them once they see them properly on the landing page or in a store.

MVV #1 should therefore evaluate **acquisition performance and product appeal separately**.

This is an experiment-specific operating rule, not yet a company-wide validated principle. If repeated evidence supports it, the Knowledge Librarian may later propose promoting the learning into the general MVV methodology.

---

## 1. What Meta Ads Should Test

Meta ads should primarily answer:

> **Which creative executions can efficiently attract relevant R012 customers and earn the click?**

For acquisition creative, scroll readability and communication speed matter.

A strong Meta ad should make enough sense on a small mobile screen, during a fast scroll, that the intended treasure-hunter customer recognizes something relevant and wants to learn more.

MVV #1 should **not require every approved T-shirt design to compete independently as an ad**.

Some designs may be better suited to being products than traffic-driving creatives.

CTR should therefore be interpreted primarily as evidence about the **ad creative's ability to acquire attention**, not as the definitive T-shirt winner metric.

---

## 2. What the Landing Page Should Test

The landing page should answer a different question:

> **Once relevant visitors are paying attention, which actual T-shirt designs do they want?**

The landing-page assortment may therefore be broader than the set of designs used in ads.

A design that is not especially readable in a Meta feed should still receive a fair product test if Creative believes it is a credible, desirable shirt when presented properly.

The landing page should make those designs large and clear enough to inspect and should capture behavior such as:

- meaningful design views;
- deliberate design engagement;
- product-specific intent;
- lead submission associated with product interest.

The existing MVV-001 event schema supports this separation by preserving `creative_id` separately from `design_id`.

The intended diagnostic chain is:

> **acquisition creative → landing visit → design exposure → design engagement → product-specific intent → lead**

---

## 3. Do Not Use CTR as the T-Shirt Winner Metric

A possible outcome is:

> D002 drives traffic efficiently, while D007 performs poorly when used as an ad but becomes one of the most desired products once customers see it clearly on the landing page.

That result is not contradictory.

It would mean:

- D002 is a strong **acquisition creative**;
- D007 is a strong **product**.

Those are different commercial jobs.

Do not conclude that a weaker-CTR product reflects weak product appeal or weak brand resonance unless it also receives a fair downstream product test.

---

## 4. Three Different Kinds of Winners

MVV should distinguish three possible leaderboards.

### Acquisition winners

Designs or other creative executions that are especially effective at bringing relevant customers to the landing page.

### Intent winners

Products that generate the strongest desire once visitors can inspect them properly.

### Purchase winners*

Products that eventually generate actual paid purchases during Tier 3 validation.

\* **MVV #1 will not evaluate purchase winners because customers will not be able to complete a purchase from the MVV landing page. Purchase behavior belongs to a later real-money validation stage.**

These groups may overlap, but MVV should not assume that they will.

---

## 5. Role Implications

### Brand Manager

Preserve the distinction between **what efficiently communicates the brand / identity in acquisition** and **what constitutes a desirable product assortment**.

Do not conclude that a weaker-CTR product reflects weak brand resonance unless the product received a fair downstream test.

### Creative Director

Do not optimize every T-shirt solely for Meta-feed readability.

Create good, wearable products first.

Separately identify which approved designs or creative executions are best suited to become acquisition creatives because they communicate quickly on a small mobile screen.

A harder-to-read design should not be eliminated merely because it is a poor ad object if it remains a strong apparel design.

### MVV Landing-Page Developer

Do not assume the incoming `creative_id` and the products deserving evaluation are the same thing.

Preserve persistent attribution from the incoming ad, but instrument **each landing-page design separately** so downstream product behavior can be attributed correctly.

The landing page must present products clearly enough that designs disadvantaged by small-feed presentation receive a fair product evaluation.

---

## 6. Working Rule for MVV #1

> **Use scroll-legible creative to acquire relevant attention. Use the landing page to discover which products customers actually want. Do not force every T-shirt to prove that it can do both jobs.**

This protects potentially strong products from being discarded simply because they are difficult to communicate during a fast Meta scroll.

It also improves learning efficiency: paid impressions can identify acquisition creatives while those same visitors evaluate a broader assortment downstream.

---

## 7. Knowledge-Librarian Status

Treat this principle as an **MVV #1 working hypothesis / operating rule** until supported by market evidence.

After MVV #1, review whether the evidence supports a reusable company-level principle such as:

> Acquisition creative performance and product-selling performance should be measured separately when the acquisition environment materially constrains product comprehension.

Do not promote that statement into company-wide methodology solely because it is strategically plausible.
