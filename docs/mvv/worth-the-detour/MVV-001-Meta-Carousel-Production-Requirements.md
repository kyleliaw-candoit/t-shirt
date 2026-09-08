---
title: MVV-001 Meta Carousel Production Requirements
brand: Worth the Detour
experiment_id: mvv-r012-001
owner: Strategy Advisor / Campaign Lead
status: Working — campaign plan approved; live Ads Manager verification pending
verified_on: 2026-09-03
attribution_reviewed_on: 2026-09-08
platform: Meta Ads Manager
related_issue: 56
---

# MVV-001 Meta Carousel Production Requirements

## 1. Purpose

This document is the experiment-specific production and QA reference for Worth the Detour MVV #1 Meta carousel advertising.

It exists so the Creative Director, Campaign / MVV Operator, Brand Manager, and Technical Reviewer work from the same current platform constraints.

This is not a permanent company-wide Meta specification. Meta capabilities, placements, and requirements can change. The Campaign / MVV Operator must verify the live Ads Manager configuration before final asset export and again before launch.

## 2. Governing campaign model

The primary acquisition candidate is an automatically reorderable, image-only carousel containing all 10 executable MVV #1 landing-page products.

Meta's delivery and card-order optimization are intended parts of the commercial model. Equal card exposure is not required.

The intended analytical chain is:

> `creative_id → source card / source product → landing visit → downstream design exposure → design engagement → product-specific intent → lead`

The carousel-level `creative_id`, source-card / source-product identity, and downstream landing-page `design_id` must remain separate.

## 3. Approved MVV #1 campaign plan

The Strategy Advisor / Campaign Lead approves the following minimum first-run configuration, subject to the live verification gate in Section 8:

| Decision | Approved first-run setting | Reason |
|---|---|---|
| Campaign objective | Traffic | The immediate paid-media job is to acquire relevant visits to the MVV landing page, not to optimize a purchase or Meta-hosted lead event. |
| Conversion location / destination | Website | Every carousel card must land on the deployed MVV landing page with its own preserved source-card parameters. |
| Initial performance goal | Maximize number of link clicks | The current first-party landing-page instrumentation is not a Meta Pixel/CAPI optimization signal. Link clicks let Meta optimize an observable ad-platform event while D1 measures post-click quality. |
| Creative format | Image-only, manually assembled 10-card carousel | This tests the complete assortment without requiring Shopify or a Meta product catalog. |
| Placements | Manual placements: Facebook Feed and Instagram Feed only | These are the two deliberate feed environments for the first MVV. Restricting scope avoids unplanned crops and extra 9:16 production. |
| Card ordering | Enable “show best-performing cards first” if available | Algorithmic card matching is part of the intended commercial model. |
| Complementary concept | At most one approved non-carousel behavioral-scene ad | Include only if it adds a meaningfully different acquisition mechanism; it uses the same feed matrix. |

Do not switch to landing-page-view, lead, or sales/conversion optimization merely because the option is visible. Such a change requires a documented Meta Pixel/CAPI signal plan, validation of the selected event, and Strategy Advisor approval.

## 4. Minimum format and export matrix

This matrix resolves the prior wording tension. “Export only ratios required by confirmed placements” and “at minimum 1:1 and 4:5” now describe the same approved two-placement plan.

| Placement | Media | Ratio | Export canvas | Minimum deliverable |
|---|---|---:|---:|---|
| Facebook Feed | JPG or PNG | 1:1 | 1080 × 1080 px or larger at 1:1 | One card image per approved carousel card; one version per approved non-carousel concept |
| Instagram Feed | JPG or PNG | 4:5 | 1080 × 1350 px or larger at 4:5 | One card image per approved carousel card; one version per approved non-carousel concept |

Additional production rules:

- Image file size must not exceed 30 MB.
- Keep the two ratio variants compositionally equivalent; they are placement adaptations of the same creative, not separate concepts.
- Preserve the same carousel-level `creative_id` across its placement adaptations. Distinguish files by placement / ratio in the manifest.
- Essential garment art, category decoding, and on-image copy must remain legible without relying on automatic crop.
- Do not export 9:16 Stories or Reels assets for the first run.
- Do not create video variants for the first run.
- Before producing the full set, make one representative card in both ratios and pass it through the live Ads Manager preview.
- Confirm that the selected manual-carousel workflow supports the intended placement-specific media assignment. If it does not, stop before bulk export and choose either one verified compatible ratio / placement or the smallest reliable campaign-structure change; document the decision rather than accepting an uncontrolled crop.

## 5. Confirmed Meta carousel capabilities and limits

Verified against official Meta documentation on 2026-09-03:

| Requirement / capability | Current confirmed rule |
|---|---|
| Carousel size | 2–10 cards |
| Card media | Images or videos |
| Card-specific fields | Each card can have its own headline, description, destination link, and call to action |
| Manual creation | A standard carousel can be assembled manually in Meta Ads Manager; Shopify or a product catalog is not required |
| Image maximum file size | 30 MB |
| Video maximum file size | 4 GB |
| Automatic card ordering | Meta supports showing predicted best-performing cards first |
| Facebook Feed traffic carousel | 1:1; at least 1080 × 1080 pixels |
| Instagram Feed traffic carousel | 4:5 for image-only carousels; Meta currently reports 1:1 for carousels containing video |
| Manual placements | Ads Manager permits the advertiser to choose specific placements |
| Stories / Reels | Placement requirements differ from Feed, including 9:16 references; these placements are excluded from the first run |

## 6. Official Meta sources

- [Traffic ad objective](https://www.facebook.com/business/ads/ad-objectives/traffic)
- [Ad objectives](https://www.facebook.com/business/ads/ad-objectives)
- [Design specifications for carousel ads](https://www.facebook.com/business/help/1114358518575630)
- [Create a carousel ad from Meta Ads Manager](https://www.facebook.com/business/help/1375829326076396)
- [Facebook Feed traffic carousel specifications](https://www.facebook.com/business/ads-guide/update/carousel/facebook-feed/traffic/mobile-app)
- [Instagram Feed traffic carousel specifications](https://www.facebook.com/business/ads-guide/update/carousel/instagram-feed/link-clicks)
- [Choose ad placements in Meta Ads Manager](https://www.facebook.com/business/help/175741192481247)
- [Customize ad creative for placements](https://www.facebook.com/business/help/127128577862845)
- [Show predicted best-performing cards first](https://www.facebook.com/business/help/120435098301466)
- [View carousel-ad metrics](https://www.facebook.com/business/help/1609310829322538)

## 7. Remaining execution decisions

The campaign plan and minimum format matrix are approved. The following execution details still require the indicated owner:

- shared primary text, card-level headline, optional description, and CTA conventions — Creative Director proposes; Strategy Advisor approves campaign-level choices;
- initial supplied card order — Creative Director;
- exact `creative_id`, source-card, and source-product URL-parameter convention — approved on 2026-09-08; see Section 10;
- whether the optional non-carousel behavioral-scene execution is production-worthy — Creative Director recommends; Strategy Advisor approves;
- live availability of best-performing-card-first and placement media customization — Campaign / MVV Operator;
- founder budget and launch authorization — Founder.

## 8. Creative Director requirements

Before creating the full finished-asset package, the Creative Director must:

1. Read Issue #56, this document, the Brand Acquisition Brief, the Brand Review Checklist, and the canonical assortment manifest.
2. Design every carousel card for realistic mobile-feed comprehension.
3. Create and submit one representative card in both approved ratios for the operator's live preview check before bulk export.
4. Keep essential product meaning within the visible image area and avoid depending on interface text that may truncate.
5. Use the approved product assets and canonical `design_id` values.
6. Treat the 10 cards as one coherent acquisition execution while preserving each card's product identity.
7. Supply the initial card order, while assuming Meta may reorder cards.
8. Produce only the two feed variants in the approved matrix unless this document is amended.
9. Record card media, copy, destination, source-product identity, placement adaptation, and status in the acquisition creative manifest.
10. Review actual Ads Manager previews before issuing the pre-launch Creative Director decision.

## 9. Campaign / MVV Operator live verification gate

Before full asset export or meaningful spend, the Campaign / MVV Operator must verify in the actual campaign builder:

- Traffic objective, Website destination, and “maximize number of link clicks” are available together;
- manual Facebook Feed and Instagram Feed placements can be selected without unintended placements;
- the manual, image-only carousel accepts all 10 cards;
- the exact accepted ratios, dimensions, media types, and file limits;
- the intended 1:1 Facebook Feed and 4:5 Instagram Feed media can be assigned without uncontrolled cropping or broken card-to-URL mapping;
- the visible and truncated behavior of primary text, headline, description, and CTA;
- automatic best-performing-card ordering is available and enabled as intended;
- every card retains its correct destination URL and source-card / source-product parameters after any reordering;
- the rendered Facebook and Instagram previews preserve essential meaning.

Use one representative card in both ratios for this check before requesting the complete export package. If the live interface conflicts with this document, stop and update the campaign-specific requirement before creative rework or meaningful spend.

## 10. Canonical card attribution and QA gate

Technical Review approved this convention on 2026-09-08. It is compatible with the deployed implementation and requires no code change, database migration, or event-schema change.

### Canonical semantics

| Field | Canonical value / rule |
|---|---|
| Carousel execution | `creative_id=WTD-MVV001-CAR-01` |
| Source card and product | `utm_content=<stable_card_id>~<source_product_design_id>` |
| Production source | `utm_source=meta` |
| Controlled-QA source | `utm_source=meta_qa` |
| Medium | `utm_medium=paid-social` |
| Campaign | `utm_campaign=mvv-r012-001` |
| Meta click ID | Do not construct `fbclid`; preserve it when Meta supplies it. |
| Downstream product | Landing-page `design_id` remains independent and must come only from the product viewed or selected. |

The tilde (`~`) is the sole separator inside `utm_content`. Preserve the canonical case and spelling of both identifiers. Example: `C01~Type-Led-4`.

Each card's Website URL must use:

```text
https://worth-the-detour.com/?creative_id=WTD-MVV001-CAR-01&utm_source=<meta-or-meta_qa>&utm_medium=paid-social&utm_campaign=mvv-r012-001&utm_content=<stable_card_id>~<source_product_design_id>
```

If the live builder confirms that a shared URL-parameters field appends to every card without replacing its existing query string, enter only:

```text
meta_campaign_id={{campaign.id}}&meta_adset_id={{adset.id}}&meta_ad_id={{ad.id}}
```

Do not add a leading `?` or duplicate the static card parameters in the shared field. Omit `utm_term`, `variant_id`, and `creative_territory_id` unless separate canonical values are later approved.

### Required live two-card QA

Before meaningful spend:

1. Keep the campaign unpublished.
2. Configure `C01 / Type-Led-4` and `C02 / B2` with `utm_source=meta_qa` and their canonical `utm_content` values.
3. Test each card from the actual carousel preview in a genuinely fresh private/incognito browser session. Close the entire private session before testing the second card because attribution is first-touch, field-by-field within a browser-tab session.
4. Confirm each landing URL retains its own `creative_id`, `utm_source`, and `utm_content`.
5. For the `C01` session, interact with `B2` and trigger at least one `intent_click`; confirm acquisition `utm_content=C01~Type-Led-4` remains paired with downstream `design_id=B2`.
6. Confirm two distinct session IDs, one `landing_view` for each source card, and `utm_source=meta_qa` on every associated downstream event in Production D1.
7. If test leads are submitted, verify them separately and keep the `meta_qa` marker.
8. Exclude only records explicitly bearing `utm_source=meta_qa` from live analysis.
9. Stop before spend if literal dynamic-token braces appear, Meta IDs are unexpectedly absent, shared URL parameters replace card parameters, reordering detaches a card from its URL, or either card produces the wrong `utm_content`.

The repository proves redirect preservation, field persistence, `design_id` independence, `~` preservation, schema compatibility, and privacy limits. The live builder must still verify dynamic-token acceptance and expansion, shared-parameter behavior across individual cards, card-to-URL integrity after automatic reordering, and whether `fbclid` appears in the chosen preview or delivery path.

## 11. Pre-launch role checks

### Creative Director

Verify mobile comprehension, product fidelity, crop, legibility, coherent carousel presentation, and rendered-placement quality.

### Brand Manager

Verify that the complete execution attracts R012 treasure hunters, decodes antiques / vintage discovery, communicates apparel, and avoids generic vintage, thrift-fashion, farmhouse, reseller, appraisal, or travel drift.

### Technical Reviewer

Verify URL construction, source-card attribution, `creative_id` / source-product / downstream `design_id` separation, redirect persistence, D1 evidence, privacy, and unnecessary complexity.

### Founder

Approve the final creative package, campaign structure, and spending before launch.

## 12. Change control

Update this document when:

- live Ads Manager behavior differs from the verified documentation;
- the performance goal changes because a validated Meta Pixel/CAPI signal is introduced;
- placements change;
- the source-card attribution method is verified;
- Meta materially changes carousel requirements before launch.

Record the verification date and cite the current official Meta source. Do not generalize MVV #1 platform behavior into permanent company methodology without repeated evidence.
