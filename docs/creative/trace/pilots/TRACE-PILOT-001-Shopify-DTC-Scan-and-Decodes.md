---
title: TRACE-PILOT-001 — Shopify/DTC Scan and Source Decodes
owner: Creative Director
status: Complete — incomplete stratum under frozen v0.2 rules
pilot_id: TRACE-PILOT-001
methodology_version: TRACE v0.2
methodology_frozen_commit: c383e2d90619e594b38b65dbd3508638d6e845d0
observation_date: 2026-09-25
---

# TRACE-PILOT-001 — Shopify/DTC Scan and Source Decodes

- Frozen method commit: `c383e2d90619e594b38b65dbd3508638d6e845d0`
- Observation date: `2026-09-25`
- Status: complete pilot record; 10 families were selected at execution, 4 remain final qualifying sources after the stricter frozen-v0.2 Gate 0 provenance audit, and no failed, quarantined, or excluded slot was backfilled.
- Rank semantics: Shopify native `best-selling` = all-time count of orders containing a product; ranks are within collection, lifetime-weighted, single snapshot, and not cross-store comparable.
- Common evidence vector on successful pool rows: `WITHIN-STORE-SALES-ORDER | EXACT listing (family collapse noted separately) | LIFETIME | SINGLE-SNAPSHOT`.

## Audit outcome

| Measure | Count | Treatment |
|---|---:|---|
| Selected at execution | 10 | Stable source IDs `TRACE-P001-DTC-01` through `TRACE-P001-DTC-10` remain in the audit trail |
| Final qualifying sources | 4 | `TRACE-P001-DTC-01`, `-03`, `-06`, and `-07`; eligible for source decoding under frozen v0.2 |
| Selected, then provenance-quarantined on final audit | 4 | `TRACE-P001-DTC-02`, `-04`, `-05`, and `-10`; retained only as audit records pending provenance resolution |
| Selected, then brand-excluded on final audit | 2 | `TRACE-P001-DTC-08` and `TRACE-P001-DTC-09`; retained only as exclusion records |
| Original preselected-store failures | 2 | OpenTrail and Two-Cross; neither was replaced |

The final audit is controlling. The four quarantines and two brand exclusions are contamination-control records, not infringement findings or legal conclusions. They are not source decodes and cannot contribute SDC, mechanisms, apparel grammar, clusters, corroboration, recipe maturity, or transfer work. No backfill was performed.

## Store panel

| Store | Preselected eligibility basis | Broad collection / native-sort verification | Outcome |
|---|---|---|---|
| Boredwalk | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://www.boredwalk.com/collections/mens-tshirts?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| Wicked Clothes | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://www.wickedclothes.com/collections/t-shirts?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| INTO THE AM | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://intotheam.com/collections/mens-graphic-t-shirts?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| Solid Threads | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://solidthreads.com/collections/mens-t-shirts?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| Crazy Dog T-Shirts | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://www.crazydogtshirts.com/collections/crazy-shirts?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| AukCliff | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://aukcliff.com/collections/explore-the-great-outdoors-with-t-shirts?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| SeaMonkey Apparel | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://www.seamonkeyapparel.com/collections/staple-tees?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| South Coast Outdoors | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://southcoastoutdoorscompany.com/collections/all-t-shirts?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| Raiz'd Up Outfitters | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://raizdupoutfitters.com/collections/all?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| Sloth Hiking Club | Independent graphic-tee-led assortment; not principally franchise/sports/celebrity merchandise at panel review | [`sort_by=best-selling`](https://slothhikingclub.com/collections/sale?sort_by=best-selling); live HTML rendered Best selling as active/selected/checked | PASS |
| OpenTrail | Independent outdoor graphic-tee assortment; current store also carries hoodies | Current indexed Shopify Best Sellers page exists, but broad `/collections/all?sort_by=best-selling` was inaccessible (DNS/prohibited-IP/403) | **FAIL — broad native-ranked pool not captured** |
| Two-Cross | Preselected from cached independent sarcastic-tee assortment | Current page changed to sweatshirts/hoodies; broad URL returned 502; no current qualifying tee pool | **FAIL — no qualifying tee family** |

## Captured ranked pools (CSV)

`execution_disposition` preserves the labels written during the run. `final_disposition` is the controlling frozen-v0.2 audit result where a product received a final screen; a blank value means no final product-level determination was made.

### Execution-label crosswalk

| Execution label | Frozen-v0.2 audit interpretation | Proposed v0.3 mapping |
|---|---|---|
| `SELECTED` | Execution event only; consult `final_disposition`, which is `ELIGIBLE`, `IP-QUARANTINE`, or an exclusion | Preserve selection history separately from final Gate 0 status |
| `CAPTURED-NOT-SCREENED-AFTER-SELECTION` | Operational capture state, not a Gate 0 disposition; no eligibility claim | Same operational state |
| `DUPLICATE-FAMILY:*` | Operational family-collapse state; not a Gate 0 disposition; the controlling parent-family row governs | Same operational state with explicit family fields |
| `INELIGIBLE-BASIC/NON-GRAPHIC` | `PRODUCT-EXCLUDED` | `PRODUCT-EXCLUDED` |
| `INELIGIBLE-BRAND-DEPENDENT` | `IP-EXCLUDED:BRAND-DEPENDENT` because frozen v0.2 had no separate house-brand label | `BRAND-EXCLUDED` |
| `IP-QUARANTINE:*` | Already a frozen-v0.2 Gate 0 disposition; preserved unchanged | `IP-QUARANTINE` |
| `STORE-FAILED:*` | Store/pool execution failure, not a product-level Gate 0 disposition | Preserve as a store-failure code |

```csv
source_id,store,rank,title,url,execution_disposition,demand_signal,attribution,currency,persistence,final_disposition
"TRACE-P001-DTC-01","Boredwalk","1","Men's Ban The Fascists Save The Books T-Shirt","https://www.boredwalk.com/products/mens-ban-the-fascists-save-the-books-t-shirt","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","ELIGIBLE"
"","Boredwalk","2","Men's Someday We'll All Be Dead T-Shirt","https://www.boredwalk.com/products/mens-someday-well-all-be-dead-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","3","Men's Have The Day You Deserve T-Shirt","https://www.boredwalk.com/products/mens-have-the-day-you-deserve-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","4","Men's Support Your Local Library T-Shirt","https://www.boredwalk.com/products/mens-support-your-local-library-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","5","Men's Oxford Comma Appreciation Society T-Shirt","https://www.boredwalk.com/products/mens-oxford-comma-appreciation-society-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","6","Men's Hell Is Other People T-Shirt","https://www.boredwalk.com/products/mens-hell-is-other-people-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","7","Men's Everything is Terrible T-Shirt","https://www.boredwalk.com/products/mens-everything-is-terrible-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","8","Men's The Female Gaze Medusa T-Shirt","https://www.boredwalk.com/products/mens-the-female-gaze-medusa-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","9","Men's Everything is Trash Raccoon T-Shirt","https://www.boredwalk.com/products/mens-everything-is-trash-raccoon-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","10","Men's Fine Thanks T-Shirt","https://www.boredwalk.com/products/mens-fine-thanks-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","11","Men's Girls Will Be Girls Witch T-Shirt","https://www.boredwalk.com/products/mens-girls-will-be-girls-witch-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","12","Men's Living My Okayest Life T-Shirt","https://www.boredwalk.com/products/mens-living-my-okayest-life-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","13","Men's Dystopia Got You Down? Try Dissociating! T-Shirt","https://www.boredwalk.com/products/mens-dystopia-got-you-down-try-dissociating-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","14","Men's Feminist is My Second Favorite F Word T-Shirt","https://www.boredwalk.com/products/mens-feminist-is-my-second-favorite-f-word-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","15","Men's We're All In This Together Like Hostages T-Shirt","https://www.boredwalk.com/products/mens-were-all-in-this-together-like-hostages-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","16","Men's Nolite Te Bastardes Carborundorum T-Shirt","https://www.boredwalk.com/products/mens-nolite-te-bastardes-carborundorum-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","17","Men's Maybe Worrying About It Will Help Anxiety T-Shirt","https://www.boredwalk.com/products/mens-maybe-worrying-about-it-will-help-anxiety-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","18","Men's Maybe Tomorrow Satan T-Shirt","https://www.boredwalk.com/products/mens-maybe-tomorrow-satan-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","19","Men's Hard Pass T-Shirt","https://www.boredwalk.com/products/mens-hard-pass-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","20","Men's A Woman's Place is in The White House T-Shirt","https://www.boredwalk.com/products/mens-a-womans-place-is-in-the-white-house-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","21","Men's What a Time to be Alive and Anxious T-Shirt","https://www.boredwalk.com/products/mens-what-a-time-to-be-alive-and-anxious-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","22","Men's Catnip Freakout T-Shirt - By Ex-Boyfriend","https://www.boredwalk.com/products/mens-catnip-freakout-t-shirt-by-ex-boyfriend","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","23","Men's No One Asked You T-Shirt","https://www.boredwalk.com/products/mens-no-one-asked-you-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Boredwalk","24","Men's Antisocial Butterfly T-Shirt","https://www.boredwalk.com/products/mens-antisocial-butterfly-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"TRACE-P001-DTC-02","Wicked Clothes","1","Feel Alive' Shirt","https://www.wickedclothes.com/products/feel-alive-shirt","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-QUARANTINE"
"","Wicked Clothes","2","Live Fast, Eat Trash' Shirt","https://www.wickedclothes.com/products/live-fast-eat-trash-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","3","Purely Spite' Shirt","https://www.wickedclothes.com/products/purely-spite-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","4","Mothman' Shirt","https://www.wickedclothes.com/products/mothman-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","5","Conspiracy Theories' Shirt","https://www.wickedclothes.com/products/conspiracy-theories-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","6","Stay Weird' Glow in the Dark Shirt","https://www.wickedclothes.com/products/stay-weird-glow-in-the-dark-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","7","Empathy is More Rebellious' Shirt","https://www.wickedclothes.com/products/empathy-is-more-rebellious-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","8","Jurassic Bloom' Shirt","https://www.wickedclothes.com/products/jurassic-bloom-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","9","The Lovers' Shirt","https://www.wickedclothes.com/products/the-lovers-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","10","Let's Get Stoned' Shirt","https://www.wickedclothes.com/products/lets-get-stoned-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","11","Paranormal' Shirt","https://www.wickedclothes.com/products/paranormal-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","12","True Crime Club' Shirt","https://www.wickedclothes.com/products/true-crime-club-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","13","Memento Mori' Shirt","https://www.wickedclothes.com/products/memento-mori-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","14","See You Later' Shirt","https://www.wickedclothes.com/products/see-you-later-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","15","Spooky Boop' Shirt","https://www.wickedclothes.com/products/spooky-boop-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","16","Death By Pizza' Shirt","https://www.wickedclothes.com/products/death-by-pizza-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","17","Gonna Be Okay' Shirt","https://www.wickedclothes.com/products/everything-is-gonna-be-okay-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","18","Destroyer of Worlds' Shirt","https://www.wickedclothes.com/products/preorder-destroyer-of-worlds-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","19","You've Got Mail' Shirt","https://www.wickedclothes.com/products/youve-got-mail-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","20","Forbidden Cats' Shirt","https://www.wickedclothes.com/products/forbidden-cats-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","21","Don't Be A Prick' Shirt","https://www.wickedclothes.com/products/dont-be-a-prick-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","22","Live Laugh Love' Shirt","https://www.wickedclothes.com/products/live-laugh-love-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","23","Catana' Shirt","https://www.wickedclothes.com/products/catana-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Wicked Clothes","24","The Horrors Are Never Ending' Shirt","https://www.wickedclothes.com/products/the-horrors-are-never-ending-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"TRACE-P001-DTC-03","INTO THE AM","1","+ Quick Add","https://intotheam.com/products/lunar-canyon-tee","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","ELIGIBLE"
"","INTO THE AM","2","+ Quick Add","https://intotheam.com/products/eternal-blossom-vintage-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","3","+ Quick Add","https://intotheam.com/products/evergreen-vintage-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","4","+ Quick Add","https://intotheam.com/products/tropic-night-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","5","+ Quick Add","https://intotheam.com/products/wild-retreat-vintage-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","6","+ Quick Add","https://intotheam.com/products/tranquil-ascent-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","7","+ Quick Add","https://intotheam.com/products/gleaming-octo-glow-in-the-dark-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","8","+ Quick Add","https://intotheam.com/products/dark-samurai-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","9","+ Quick Add","https://intotheam.com/products/tidal-surge-glow-in-the-dark-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","10","+ Quick Add","https://intotheam.com/products/astral-departure-glow-in-the-dark-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","11","+ Quick Add","https://intotheam.com/products/split-nature-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","12","+ Quick Add","https://intotheam.com/products/life-after-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","13","+ Quick Add","https://intotheam.com/products/toxic-dread-glow-in-the-dark-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","14","+ Quick Add","https://intotheam.com/products/event-horizon-glow-in-the-dark-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","15","+ Quick Add","https://intotheam.com/products/ancient-fury-glow-in-the-dark-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","16","+ Quick Add","https://intotheam.com/products/midnight-bloom-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","17","+ Quick Add","https://intotheam.com/products/no-return-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","18","+ Quick Add","https://intotheam.com/products/eternal-blossom-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","19","+ Quick Add","https://intotheam.com/products/golden-reflections-vintage-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","20","+ Quick Add","https://intotheam.com/products/bone-blossom-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","21","+ Quick Add","https://intotheam.com/products/tidal-rise-vintage-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","22","+ Quick Add","https://intotheam.com/products/infinite-horizon-glow-in-the-dark-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","23","+ Quick Add","https://intotheam.com/products/neon-horizon-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","INTO THE AM","24","+ Quick Add","https://intotheam.com/products/cosmic-descent-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"TRACE-P001-DTC-04","Solid Threads","1","F Bombs Signature T-Shirt","https://solidthreads.com/products/f-bombs-t-shirt","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-QUARANTINE"
"","Solid Threads","2","Bad Ass Signature T-Shirt","https://solidthreads.com/products/bad-ass-cool-tee-funny-donkey-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","3","Teen Wolf Signature T-Shirt","https://solidthreads.com/products/teen-wolf-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","4","Take It Slow Signature T-Shirt","https://solidthreads.com/products/take-it-slow-vintage-graphic-tee-animal-turtle-mindfulness-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","5","Easy E Signature T-Shirt","https://solidthreads.com/products/easy-e-vintage-graphic-tee-sports-new-york-giants-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","6","What's Crackin Signature T-Shirt","https://solidthreads.com/products/whats-crackin-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","7","Whiskey Helps Signature T-Shirt","https://solidthreads.com/products/whiskey-helps-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","8","Jesus Is My Lift Ticket Signature T-Shirt","https://solidthreads.com/products/jesus-is-my-lift-ticket-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","9","Boozehound Brewing Co. Signature T-Shirt","https://solidthreads.com/products/boozehound-brewing-co-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","10","Photosynthesis is Fun Signature T-Shirt","https://solidthreads.com/products/photosynthesis-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","11","Slow Down Signature T-Shirt","https://solidthreads.com/products/slow-down-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","12","That's Bananas Signature T-Shirt","https://solidthreads.com/products/thats-bananas-vintage-funny-tee-fruit-food-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","13","Swirly Mountains Signature T-Shirt","https://solidthreads.com/products/swirly-mountains-vintage-inspired-tee-shirt-with-cool-nature-graphic","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","14","Tequila Skull Signature T-Shirt","https://solidthreads.com/products/tequila-skull-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","15","Dude Abides Signature T-Shirt","https://solidthreads.com/products/the-dude-abides-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","16","How You Lichen Me Now T-Shirt","https://solidthreads.com/products/how-you-lichen-me-now-graphic-t-shirt-funny-nature-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","17","Sunset Mountains Signature T-Shirt","https://solidthreads.com/products/sunset-vintage-inspired-tee-shirt-with-cool-mountain-forest-graphic","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","18","Sunday Funday Signature T-Shirt","https://solidthreads.com/products/sunday-funday-graphic-t-shirt-vintage-drinking-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","19","Squirrelzilla Signature T-Shirt","https://solidthreads.com/products/squirrelzilla-graphic-t-shirt-funny-godzilla-pun-kaiju-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","20","Nice & Hammered Signature T-Shirt","https://solidthreads.com/products/nice-hammered-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","21","Holy Guacamole Signature T-Shirt","https://solidthreads.com/products/holy-guacamole-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","22","Stay Cool Signature T-Shirt","https://solidthreads.com/products/stay-cool-graphic-t-shirt-vintage-summer-drinking-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","23","I'm a Drinker Not a Fighter Signature T-Shirt","https://solidthreads.com/products/im-a-drinker-not-a-fighter-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Solid Threads","24","Later Gator Signature T-Shirt","https://solidthreads.com/products/later-gator-vintage-graphic-tee-funny-alligator-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"TRACE-P001-DTC-05","Crazy Dog T-Shirts","1","Ask Me About My Ninja Disguise Flip Men's T Shirt","https://www.crazydogtshirts.com/products/ask-me-about-my-ninja-disguise-shirt","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-QUARANTINE"
"","Crazy Dog T-Shirts","2","Synonym Rolls Just Like Grammar Used To Make Women's T Shirt","https://www.crazydogtshirts.com/products/synonym-rolls-just-like-grammar-used-to-make-womens-tshirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","3","Ask Me About My Ninja Disguise Flip Youth T Shirt","https://www.crazydogtshirts.com/products/ask-me-about-my-ninja-disguise-shirt-youth","DUPLICATE-FAMILY:CRAZYDOG-R1","WITHIN-STORE-SALES-ORDER","SAME-PRINT-VARIANTS","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","4","Kickin’ Me Smalls Maternity T Shirt","https://www.crazydogtshirts.com/products/you-re-kickin-me-smalls-maternity-shirt-maternity","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","5","Women's Take No Shit Give No Fucks Socks","https://www.crazydogtshirts.com/products/womens-take-no-shit-give-no-fucks-socks","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","6","I'm Going To Feed All You Fuckers Funny Cooking Food Graphic Kitchen Accessories Bakeware","https://www.crazydogtshirts.com/products/im-going-to-feed-all-you-fuckers-funny-cooking-food-graphic-kitchen-accessories","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","7","Hold On Let Me Overthink This Mug","https://www.crazydogtshirts.com/products/hold-on-let-me-overthink-this-mug","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","8","Can't Work Today My Arm Is In A Cast Men's T Shirt","https://www.crazydogtshirts.com/products/mens-cant-work-today-arm-is-in-a-cast-tshirt-funny-fathers-day-fishing-tee-for-guys","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","9","That Sounds Like A Horrible Idea. What Time? Men's T Shirt","https://www.crazydogtshirts.com/products/that-soulds-like-a-horrible-idea-what-time-mens-tshirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","10","Fitness Taco In My Mouth Men's T Shirt","https://www.crazydogtshirts.com/products/fitness-taco-in-my-mouth-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","11","With A Body Like This Who Needs Hair Men's T Shirt","https://www.crazydogtshirts.com/products/with-a-body-like-this-who-needs-hair-mens-tshirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","12","Of Course I Talk To Myself, I Need Expert Advice Men's T Shirt","https://www.crazydogtshirts.com/products/talk-to-myself-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","13","Awesome Like My Daughter Men's T Shirt","https://www.crazydogtshirts.com/products/awesome-like-my-daughter-mens-tshirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","14","Hide And Seek Champion Men's T Shirt","https://www.crazydogtshirts.com/products/hide-and-seek-champion-mens-tshirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","15","I Like Coffee And Maybe 3 People Men's T Shirt","https://www.crazydogtshirts.com/products/i-like-coffee-and-maybe-3-people-mens-tshirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","16","World's Greatest Farter Father Men's T Shirt","https://www.crazydogtshirts.com/products/world-s-greatest-farter-father-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","17","My Favorite People Call Me Papa Men's T Shirt","https://www.crazydogtshirts.com/products/mens-my-favorite-people-call-me-papa-tshirt-funny-fathers-day-tee-for-guys","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","18","Wonder if Beer Thinks About Me Men's T Shirt","https://www.crazydogtshirts.com/products/wonder-if-beer-thinks-about-me-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","19","Science: Like Magic But Real Men's T Shirt","https://www.crazydogtshirts.com/products/science-like-magic-but-real-mens-tshirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","20","I'm Silently Correcting Your Grammar Men's T Shirt","https://www.crazydogtshirts.com/products/silently-correcting-your-grammar-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","21","World's Okayest Brother Men's T Shirt","https://www.crazydogtshirts.com/products/okayest-brother-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","22","Bushwood Country Club Men's T Shirt","https://www.crazydogtshirts.com/products/bushwood-country-club-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","23","I'm Hiding Men's T Shirt","https://www.crazydogtshirts.com/products/mens-im-hiding-camo-tee-shirt-funny-sarcastic-military-tee-for-guys","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Crazy Dog T-Shirts","24","Surely Not Everybody Was Kung Fu Fighting Men's T Shirt","https://www.crazydogtshirts.com/products/surely-not-everybody-was-kung-fu-fighting-mens-tshirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","1","Simple","https://aukcliff.com/products/simple-t-shirt","INELIGIBLE-BASIC/NON-GRAPHIC","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","PRODUCT-EXCLUDED"
"TRACE-P001-DTC-06","AukCliff","2","Coastal Waves","https://aukcliff.com/products/coastal-waves-t-shirt","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","ELIGIBLE"
"","AukCliff","3","Captain Puffin Wildlife Photographer","https://aukcliff.com/products/captain-puffin-wildlife-photographer-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","4","Captain Puffin Hiker","https://aukcliff.com/products/captain-puffin-hiker-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","5","Embrace The Mountain Call","https://aukcliff.com/products/embrace-the-mountain-call-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","6","Outlet Psithurism, the Sound of Wind in the Trees","https://aukcliff.com/products/psithurism-the-sound-of-wind-in-the-trees-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","7","Mountain Call","https://aukcliff.com/products/mountain-call-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","8","Outlet Owl in Flight Above a Red Horizon","https://aukcliff.com/products/owl-in-flight-above-a-red-horizon-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","9","Captain Puffin Van Life","https://aukcliff.com/products/captain-puffin-van-life-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","10","Outlet Petrichor, the Smell of Rain on Dry Earth","https://aukcliff.com/products/petrichor-the-smell-of-rain-on-dry-earth-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","11","Outlet One Red Line, a Whole Pine Tree","https://aukcliff.com/products/one-red-line-a-whole-pine-tree-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","12","Abstract Peaks","https://aukcliff.com/products/abstract-peaks-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","13","Geometric Puffin Trekker","https://aukcliff.com/products/geometric-puffin-trekker-t-shirt-1","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","14","Captain Puffin Bush Pilot","https://aukcliff.com/products/captain-puffin-bush-pilot-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","15","Captain Puffin Bird Photographer","https://aukcliff.com/products/captain-puffin-bird-photographer-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","16","Abstract Ridge Line Mountain","https://aukcliff.com/products/abstract-ridge-line-mountain-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","17","Sunrise Vista Landscape Back Print","https://aukcliff.com/products/sunrise-vista-landscape-back-print-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","18","AukCliff® Puffin Logo","https://aukcliff.com/products/aukcliff-puffin-logo-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","19","Outlet Solvitur Ambulando, It Is Solved by Walking","https://aukcliff.com/products/solvitur-ambulando-it-is-solved-by-walking-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","20","Conquer New Heights Mountain","https://aukcliff.com/products/conquer-new-heights-mountain-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","21","The Cliffborn","https://aukcliff.com/products/the-cliffborn-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","22","Captain Puffin Canada Trailkeeper","https://aukcliff.com/products/captain-puffin-canada-trailkeeper-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","23","Captain Puffin Mountaineer","https://aukcliff.com/products/captain-puffin-mountaineer-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","AukCliff","24","Alpine Ridge","https://aukcliff.com/products/alpine-ridge-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"TRACE-P001-DTC-07","SeaMonkey Apparel","1","Puff Puff Pass Tee","https://www.seamonkeyapparel.com/products/puff-puff-pass-tee","SELECTED","WITHIN-STORE-SALES-ORDER","SAME-PRINT-VARIANTS","LIFETIME","SINGLE-SNAPSHOT","ELIGIBLE"
"","SeaMonkey Apparel","2","Hard Decisions Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/hard-decisions-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","3","Hula Gang Tee Sale price $15.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/copy-of-mens-hula-gang-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","4","Driftwood Tee Sale price $15.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/driftwood-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","5","Puff Puff Pass Tee","https://www.seamonkeyapparel.com/products/puff-puff-pass-tee-1","DUPLICATE-FAMILY:PENDING-ARTWORK-VERIFY-AGAINST-R1","WITHIN-STORE-SALES-ORDER","SAME-PRINT-VARIANTS","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","6","Cortez Pride Tee Regular price $30.00 Sold out","https://www.seamonkeyapparel.com/products/mens-cortez-pride-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","7","Peace, Love and Paws Tee Sale price $15.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/peace-love-paws-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","8","Tropical State Of Mind Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/tropical-state-of-mind-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","9","Sunset Surfer Tee Sale price $15.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/sunset-surfer-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","10","Dwellers of The Deep Sea Tee Sale price $12.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/dwellers-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","11","Wet Your Whiskers Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/wet-your-whiskers-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","12","Pass The Reefer Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/pass-the-reefer-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","13","Tails Of The Tiki Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/tails-of-the-tiki-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","14","All Paws On Deck Tee Sale price $15.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/all-paws-on-deck-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","15","Go With The Flow Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/go-with-the-flow-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","16","Latitudes Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/go-with-the-flow-tee-copy","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","17","Patriotic Logo II Tee Sale price $15.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/patriotic-logo-ii-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","18","Beach Day Tee Sale price $15.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/beach-day-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","19","Ladies Wet Your Whiskers V Neck Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/ladies-wet-your-whiskers-v-neck-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","20","Cruisin' Tee Sale price $15.00 Regular price $30.00 Sale","https://www.seamonkeyapparel.com/products/cruisin-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","21","Clancy's Collaboration Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/clancys-collaboration-tee-1","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","22","Save Our Seabirds Tee Regular price $30.00 Sold out","https://www.seamonkeyapparel.com/products/save-our-seabirds-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","23","Conch'd Out Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/conchd-out-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","SeaMonkey Apparel","24","Patriotic Logo Tee Regular price $30.00","https://www.seamonkeyapparel.com/products/patriotic-logo-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"TRACE-P001-DTC-08","South Coast Outdoors","1","Blue Marlin Sc1600","https://southcoastoutdoorscompany.com/products/blue-marlin-sc1600","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-EXCLUDED:BRAND-DEPENDENT"
"","South Coast Outdoors","2","Stay Wild Sc3100","https://southcoastoutdoorscompany.com/products/stay-wild-sc3100","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","3","Tropical Stilt House Sc4100","https://southcoastoutdoorscompany.com/products/tropical-stilt-house-sc4100","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","4","Live Salty Sc3000","https://southcoastoutdoorscompany.com/products/live-salty-sc3000","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","5","Magic Of Coastal Living Sc800","https://southcoastoutdoorscompany.com/products/magic-of-coastal-living-sc800","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","6","Tarpon Sc 2000","https://southcoastoutdoorscompany.com/products/tarpon-sc-2000","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","7","South Coast Outdoors Co Oval Logo Sc51000","https://southcoastoutdoorscompany.com/products/south-coast-outdoors-co-oval-logo-sc51000","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","8","South Coast Outdoors Co Circle Logo Sc5200","https://southcoastoutdoorscompany.com/products/south-coast-outdoors-co-circle-logo-sc5200","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","9","South Coast Outdoors Co Classic Logo Sc4800","https://southcoastoutdoorscompany.com/products/south-coast-outdoors-co-classic-logo-sc4800","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","10","South Coast Sc4700","https://southcoastoutdoorscompany.com/products/south-coast-sc4700","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","11","South Coast Silhouette Sc4600","https://southcoastoutdoorscompany.com/products/south-coast-silhouette-sc4600","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","12","Sco Logo Sc4500","https://southcoastoutdoorscompany.com/products/sco-logo-sc4500","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","13","Beach Bar T Shirt Sc4300","https://southcoastoutdoorscompany.com/products/beach-bar-t-shirt-sc4300","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","14","Beaches Bayous Backroads Sc4200","https://southcoastoutdoorscompany.com/products/beaches-bayous-backroads-sc4200","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","15","Coastal Living The Southern Way Sc4000","https://southcoastoutdoorscompany.com/products/coastal-living-the-southern-way-sc4000","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","16","Gulf Breeze Sc3900","https://southcoastoutdoorscompany.com/products/gulf-breeze-sc3900","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","17","Strong Traditions Sc3800","https://southcoastoutdoorscompany.com/products/strong-traditions-sc3800","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","18","Southern Shoreline Sc3700","https://southcoastoutdoorscompany.com/products/southern-shoreline-sc3700","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","19","Slow Down Sc3600","https://southcoastoutdoorscompany.com/products/slow-down-sc3600","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","20","Southern Shoreline Sc3500","https://southcoastoutdoorscompany.com/products/southern-shoreline-sc3500","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","21","Mangrove Kayak Sc3400","https://southcoastoutdoorscompany.com/products/mangrove-kayak-sc3400","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","22","Offshore Marlin Sc3300","https://southcoastoutdoorscompany.com/products/offshore-marlin-sc3300","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","23","Above Below Sc3200","https://southcoastoutdoorscompany.com/products/above-below-sc3200","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","South Coast Outdoors","24","Stay Wild Sc3000","https://southcoastoutdoorscompany.com/products/stay-wild-sc3000","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","1","Wrangler Edition – Women's","https://raizdupoutfitters.com/products/wrangler-edition-womens","IP-QUARANTINE:JEEP-WRANGLER","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-QUARANTINE:JEEP-WRANGLER"
"","Raiz'd Up Outfitters","2","Gladiator Edition – Women's","https://raizdupoutfitters.com/products/gladiator-tee","IP-QUARANTINE:JEEP-GLADIATOR","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-QUARANTINE:JEEP-GLADIATOR"
"","Raiz'd Up Outfitters","3","RUH - Gladiator Buck - Men's","https://raizdupoutfitters.com/products/ruh-mens-gladiator-hunting-rig","IP-QUARANTINE:JEEP-GLADIATOR","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-QUARANTINE:JEEP-GLADIATOR"
"","Raiz'd Up Outfitters","4","RUO - Florida Roots - Women's","https://raizdupoutfitters.com/products/ruo-rooted-here-raizd-everywhere-tee","INELIGIBLE-BRAND-DEPENDENT","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-EXCLUDED:BRAND-DEPENDENT"
"TRACE-P001-DTC-09","Raiz'd Up Outfitters","5","RUF - Built for the Salt - Women's","https://raizdupoutfitters.com/products/ruf-built-for-the-salt-tee","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-EXCLUDED:BRAND-DEPENDENT"
"","Raiz'd Up Outfitters","6","Built for the Wild UTV Tee – Men's","https://raizdupoutfitters.com/products/ruo-built-for-the-wild-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","7","Apex Predator Fishing Tee – Men's","https://raizdupoutfitters.com/products/raizd-up-fishing-apex-predator-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","8","Blue Gladiator Edition – Men's","https://raizdupoutfitters.com/products/blue-gladiator-edition-mens","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","9","RUF - Captain's Wheel Performance Long Sleeve - Men's","https://raizdupoutfitters.com/products/ruf-captains-wheel-performance-long-sleeve-mens","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","10","RUO - Custom Shirt Order","https://raizdupoutfitters.com/products/custom-shirt-order","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","11","RUO - Built for the Trails - Wrangler Lovers Collection","https://raizdupoutfitters.com/products/ruo-built-for-the-trails-wrangler","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","12","RUO - Tail Of The Dragon - Men’s","https://raizdupoutfitters.com/products/ruo-tail-of-the-dragon-men-s","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","13","RUF - Chase The Bite - Men's","https://raizdupoutfitters.com/products/ruf-chase-the-bite-mens","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","14","RUH - Whitetail Heritage","https://raizdupoutfitters.com/products/ruo-mud-truck-mens-copy","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","15","RUO Built for the Wild UTV - Women's","https://raizdupoutfitters.com/products/ruo-mud-truck-tee-womens","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","16","RUO – Bear, Elk, Eagle, and Adventure - Men's","https://raizdupoutfitters.com/products/bear","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","17","RUF - Built for Offshore - Men's","https://raizdupoutfitters.com/products/ruf-built-for-offshore-tee","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","18","RUO - Florida Roots - Men's","https://raizdupoutfitters.com/products/ruo-florida-roots-tee-copy","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","19","Apex Predator Fishing Tee – Women's","https://raizdupoutfitters.com/products/ruf-apex-predator-tee-copy","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","20","RUO - Blue Water Florida Roots - Men's","https://raizdupoutfitters.com/products/ruo-florida-roots-mens-copy-1","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","21","Blue Gladiator Edition – Women's","https://raizdupoutfitters.com/products/blue-gladiator-edition-womens","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","22","RUF - Flounder Shirt & Hoodie - Men's","https://raizdupoutfitters.com/products/ruf-cobia-mens-copy-1","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","23","RUO - Tail Of The Dragon - Women’s","https://raizdupoutfitters.com/products/ruo-tail-of-the-dragon","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Raiz'd Up Outfitters","24","RUO - Halloween Limited Edition - Women's","https://raizdupoutfitters.com/products/ruo-florida-roots-woods-womens-copy","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"TRACE-P001-DTC-10","Sloth Hiking Club","1","Out Of Breath T-shirt","https://slothhikingclub.com/products/out-of-breath-t-shirt","SELECTED","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT","IP-QUARANTINE"
"","Sloth Hiking Club","2","Go Outside T-shirt","https://slothhikingclub.com/products/go-outside-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","3","Meese T-shirt","https://slothhikingclub.com/products/meese-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","4","Blowing Wishes T-Shirt","https://slothhikingclub.com/products/blowing-wishes-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","5","Sunrise Pines T-shirt","https://slothhikingclub.com/products/sunrise-pines-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","6","Haven't Been Everywhere T-shirt","https://slothhikingclub.com/products/havent-been-everywhere-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","7","Bad Knees T-shirt","https://slothhikingclub.com/products/bad-knees-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","8","Stump Of Life T-shirt","https://slothhikingclub.com/products/stump-of-life-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","9","Funky Peace T-shirt","https://slothhikingclub.com/products/funky-peace-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","10","I Love Peeing Outside T-shirt","https://slothhikingclub.com/products/i-love-peeing-outside-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","11","Slow Hiking Society Snail T-Shirt","https://slothhikingclub.com/products/slow-hiking-society-snail-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","12","Take A Hike T-shirt","https://slothhikingclub.com/products/take-a-hike-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","13","Water Color Forest T-shirt","https://slothhikingclub.com/products/water-color-forest-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","14","Paths In Life T-shirt","https://slothhikingclub.com/products/paths-in-life-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","15","I'm Lichen It T-shirt","https://slothhikingclub.com/products/im-lichen-it-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","16","Campfire Friends T-Shirt","https://slothhikingclub.com/products/campfire-friends-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","17","Earth Laughs In Flowers T-shirt","https://slothhikingclub.com/products/earth-laughs-in-flowers-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","18","Bear Reflection T-Shirt","https://slothhikingclub.com/products/bear-reflection-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","19","Fox Spirit T-Shirt","https://slothhikingclub.com/products/fox-spirit-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","20","Still Plays Outside T-shirt","https://slothhikingclub.com/products/still-plays-outside-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","21","If It Involves Hiking And Dogs T-Shirt","https://slothhikingclub.com/products/if-it-involves-hiking-and-dogs-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","22","Meowntains T-shirt","https://slothhikingclub.com/products/meowntains-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","23","Birds & Flowers T-Shirt","https://slothhikingclub.com/products/birds-flowers-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","Sloth Hiking Club","24","Bear Hug T-Shirt","https://slothhikingclub.com/products/bear-hug-t-shirt","CAPTURED-NOT-SCREENED-AFTER-SELECTION","WITHIN-STORE-SALES-ORDER","EXACT","LIFETIME","SINGLE-SNAPSHOT",""
"","OpenTrail","","","https://shopopentrail.com/collections/all?sort_by=best-selling","STORE-FAILED:ACCESS/NO-BROAD-POOL","DISCOVERY-ONLY","UNCLEAR","CURRENT-SNAPSHOT-UNKNOWN-WINDOW","UNKNOWN",""
"","Two-Cross","","","https://two-cross.com/collections/all?sort_by=best-selling","STORE-FAILED:NO-CURRENT-TEE-POOL","DISCOVERY-ONLY","UNCLEAR","CURRENT-SNAPSHOT-UNKNOWN-WINDOW","UNKNOWN",""
```

SeaMonkey ranks 1 and 5 retain the raw-capture attribution value `SAME-PRINT-VARIANTS`. This field is mixed evidence: the repeated title and adjacent product-family context support a likely family relationship, but the two listings' artwork equivalence was not verified. Rank 5 therefore remains `DUPLICATE-FAMILY:PENDING-ARTWORK-VERIFY-AGAINST-R1`; the attribution value must not be read as confirmation that the prints are identical.

## Selected-family audit records

The four records with final disposition `ELIGIBLE` are **source decode inputs**, not promoted recipes. Confidence applies to the interpretation of the concept, not to the existence of the within-store rank. The four post-selection quarantines and two post-selection exclusions are audit records only and are prohibited from downstream analytical use.

### TRACE-P001-DTC-01 — Boredwalk, rank 1

- Product: [Men's Ban The Fascists Save The Books T-Shirt](https://www.boredwalk.com/products/mens-ban-the-fascists-save-the-books-t-shirt)
- Collection/rank/date: [Mens TShirts, native Best selling](https://www.boredwalk.com/collections/mens-tshirts?sort_by=best-selling), 1, 2026-09-25.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | EXACT | LIFETIME | SINGLE-SNAPSHOT`.
- Reviews: `400` shown on this item page; treated as item-specific. Store also has separate general review content.
- Eligibility/IP: `ELIGIBLE`; political/anti-censorship expression, no franchise/celebrity/team/logo dependency observed.
- Observed expression: `BAN THE FASCISTS / SAVE THE BOOKS`; cheerful anthropomorphic book mascot, small stars/books, warm orange/cream on navy, arched headline and underlined footer.
- Source niche / insider truth: readers, librarians, teachers, and free-speech advocates; book bans are understood as tools of authoritarian control.
- Payoff / candidate mechanism: solidarity and defiance; a symmetrical two-imperative contrast identifies the threat and the cherished object in one instantly parsed moral choice.
- Apparel grammar: retro civic/varsity badge; large centered mascot; two-tier type hierarchy; limited high-contrast palette.
- Confounders: current political salience, Boredwalk's aligned audience, giftability, and 400 accumulated item reviews.
- Prohibited transfer: exact phrase/syntax pair, anthropomorphic book mascot, same arch-and-footer layout, same palette.
- Decode confidence: `HIGH`.

### TRACE-P001-DTC-02 — post-selection quarantine record (Wicked Clothes, rank 1)

- Product: [You Make Me Feel Alive Shirt](https://www.wickedclothes.com/products/feel-alive-shirt)
- Collection/rank/date: [T-Shirts, native Best selling](https://www.wickedclothes.com/collections/t-shirts?sort_by=best-selling), 1, 2026-09-25.
- Execution status: selected during the run; stable source ID retained for audit continuity.
- Controlling final disposition: `IP-QUARANTINE` under frozen v0.2.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | EXACT | LIFETIME | SINGLE-SNAPSHOT`.
- Reviews: `29` in product-scoped structured review data; `7,386` elsewhere is store-wide and not attributed to this design.
- Expression under audit: `YOU MAKE ME / FEEL ALIVE` with a skeleton watering plants.
- Representative recurrence evidence: a [Vexels stock-design listing](https://www.vexels.com/vectors/preview/279540/skeleton-watering-plants-t-shirt-design) and a [Threadless marketplace listing](https://www.threadless.com/shop/%40TheIdleSheep/design/skeleton-watering-plants-you-make-me-feel-alive) show the same skeleton-watering-plants / `You Make Me Feel Alive` combination across sources.
- Gate 0 correction: the stock/multi-seller recurrence makes source independence and provenance unresolved. The evidence does not establish whether any seller created, licensed, or copied the expression, so frozen v0.2 requires quarantine rather than creative attribution.
- Use restriction: audit evidence only; no source decode, SDC, insider-truth inference, candidate mechanism, apparel grammar, clustering, corroboration, recipe-maturity credit, or transfer use.
- Scope: contamination control only, not an infringement finding or legal conclusion.
- Backfill: none.

### TRACE-P001-DTC-03 — INTO THE AM, rank 1

- Product: [Lunar Canyon Tee](https://intotheam.com/products/lunar-canyon-tee)
- Collection/rank/date: [Men's Graphic T-Shirts, native Best selling](https://intotheam.com/collections/mens-graphic-t-shirts?sort_by=best-selling), 1, 2026-09-25.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | SAME-PRINT-VARIANTS | LIFETIME | SINGLE-SNAPSHOT`.
- Reviews: `13,700` in Product/ProductGroup structured data for this product family; no visible review panel was captured, so use with medium attribution confidence.
- Eligibility/IP: `ELIGIBLE`; original non-text cosmic landscape.
- Observed expression: no wording; a winding luminous canyon/river leads toward a dark eclipse/void, surrounded by a radial starburst in monochrome white/gray on black.
- Source niche / insider truth: cosmic/surreal adventure-art wearers; wilderness is used as a route into awe, introspection, and the unknown.
- Payoff / candidate mechanism: sublime awe; fuse a familiar terrestrial path with an impossible cosmic destination so scale escalates from human landscape to universe.
- Apparel grammar: tall centered poster; one dominant circular focal point; detailed line/halftone texture; monochrome high contrast; no explanatory copy.
- Confounders: premium-fit positioning, sale price/final-sale status, store audience already shopping visual art, unusually large structured review count.
- Prohibited transfer: exact canyon-to-eclipse composition, radial burst, monochrome artwork.
- Decode confidence: `MEDIUM-HIGH`.

### TRACE-P001-DTC-04 — post-selection quarantine record (Solid Threads, rank 1)

- Product: [F Bombs Signature T-Shirt](https://solidthreads.com/products/f-bombs-t-shirt)
- Collection/rank/date: [Men's T-Shirts, native Best selling](https://solidthreads.com/collections/mens-t-shirts?sort_by=best-selling), 1, 2026-09-25.
- Execution status: selected during the run; stable source ID retained for audit continuity.
- Controlling final disposition: `IP-QUARANTINE` under frozen v0.2.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | EXACT | LIFETIME | SINGLE-SNAPSHOT`.
- Reviews: `83` shown on this exact item page.
- Expression under audit: a vintage bomber aircraft drops a diagonal chain of bombs, each marked with a large `F`; no explanatory sentence.
- Representative recurrence evidence: a [TeePublic listing titled “Dropping F-Bombs | Funny Bomber Graphic Design”](https://www.teepublic.com/t-shirt/77093217-dropping-f-bombs-funny-bomber-graphic-design) by Brevan Tee Co. describes an air-force bomber literally dropping “F-Bombs,” materially recurring across sellers as the same phrase-to-bomber visual rebus.
- Gate 0 correction: the cross-seller material recurrence makes source independence and expression origin unresolved. Although [Solid Threads says its designs are created or art-directed by its team](https://solidthreads.com/pages/graphic-tee-brand-intro), that broad seller claim does not resolve the recurrence or establish publication direction, licensing, or authorship for this expression. Frozen v0.2 therefore requires quarantine rather than creative attribution.
- Use restriction: audit evidence only; no source decode, SDC, insider-truth inference, candidate mechanism, apparel grammar, clustering, corroboration, recipe-maturity credit, or transfer use.
- Scope: contamination control only, not an infringement finding or legal conclusion.
- Backfill: none.

### TRACE-P001-DTC-05 — post-selection quarantine record (Crazy Dog T-Shirts, rank 1)

- Product: [Ask Me About My Ninja Disguise Flip Men's T Shirt](https://www.crazydogtshirts.com/products/ask-me-about-my-ninja-disguise-shirt)
- Collection/rank/date: [Crazy Shirts, native Best selling](https://www.crazydogtshirts.com/collections/crazy-shirts?sort_by=best-selling), 1, 2026-09-25.
- Execution status: selected during the run; stable source ID retained for audit continuity.
- Controlling final disposition: `IP-QUARANTINE` under frozen v0.2.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | SAME-PRINT-VARIANTS | LIFETIME | SINGLE-SNAPSHOT`; youth version reappears at raw rank 3 and collapses into this family.
- Reviews: no separately attributable item-review count; displayed testimonials are generic/store-level.
- Expression under audit: front text `ASK ME / ABOUT MY / NINJA / DISGUISE`; lifting the hem reveals an inside-printed ninja mask aligned to the wearer's face.
- Representative recurrence evidence: a [long-running video record](https://www.youtube.com/watch?v=FLkqawY8fqE) and a [Vat19 retail listing](https://www.vat19.com/item/ask-me-about-my-ninja-disguise-t-shirt) document the same phrase-plus-inside-mask interaction. The concept has been publicly documented for at least 13 years and appears through multiple sellers.
- Gate 0 correction: the exact long-running, multi-seller construction makes source independence and provenance unresolved. The evidence does not establish which sellers created, licensed, or copied it, so frozen v0.2 requires quarantine.
- Use restriction: audit evidence only; no source decode, SDC, insider-truth inference, candidate mechanism, apparel grammar, clustering, corroboration, recipe-maturity credit, or transfer use.
- Scope: contamination control only, not an infringement finding or legal conclusion.
- Backfill: none.

### TRACE-P001-DTC-06 — AukCliff, raw rank 2 (rank 1 excluded)

- Product: [Coastal Waves T-shirt](https://aukcliff.com/products/coastal-waves-t-shirt)
- Collection/rank/date: [T-shirts, native Best selling](https://aukcliff.com/collections/explore-the-great-outdoors-with-t-shirts?sort_by=best-selling), 2, 2026-09-25.
- Rank-1 disposition: `Simple T-shirt` excluded as `BASIC/NON-GRAPHIC`; its demand cannot safely be attributed to a concept.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | SAME-PRINT-VARIANTS | LIFETIME | SINGLE-SNAPSHOT`.
- Reviews: product structured data reports `4`; visible `4.8 from 830 reviews across the shop` is shop-wide and not credited to the design.
- Eligibility/IP: `ELIGIBLE`; store expressly describes the art as its own, not licensed.
- Observed expression: small puffin front mark; large framed back print of a stylized breaking wave under a red sun, with restrained small aspirational copy.
- Source niche / insider truth: coast/surf/outdoor people identify with the power, rhythm, and resilience of the sea.
- Payoff / candidate mechanism: calm aspiration; attach a short capability/renewal claim to a natural-force metaphor that already embodies the desired trait.
- Apparel grammar: micro front mark + large back poster; Japanese-print/woodcut influence; navy/white/red; rectangular frame and ample negative space.
- Confounders: very high price, brand/fabric quality, store-wide review proof, and all-time rank in a large collection.
- Prohibited transfer: same wave/red-sun composition, puffin mark, exact copy, same framed poster treatment.
- Decode confidence: `MEDIUM`.

### TRACE-P001-DTC-07 — SeaMonkey Apparel, rank 1

- Product: [Puff Puff Pass Tee](https://www.seamonkeyapparel.com/products/puff-puff-pass-tee)
- Collection/rank/date: [Tee's, native Best selling](https://www.seamonkeyapparel.com/collections/staple-tees?sort_by=best-selling), 1, 2026-09-25.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | SAME-PRINT-VARIANTS | LIFETIME | SINGLE-SNAPSHOT`; a same-titled second product appears at raw rank 5 and should be family-collapsed after artwork verification.
- Reviews: `10` displayed in the product-specific review widget.
- Eligibility/IP: `ELIGIBLE`; no franchise/team/celebrity dependency observed.
- Observed expression: `PUFF PUFF PASS` above a large pufferfish in a tropical/coastal illustrated scene; apparel-brand footer; distressed saturated aqua/orange palette.
- Source niche / insider truth: the cannabis ritual phrase is widely known, while a pufferfish literally “puffs”; coastal leisure culture makes the hybrid feel natural.
- Payoff / candidate mechanism: cheeky insider recognition; replace or embody one element of a familiar ritual phrase with a subject whose defining trait literally performs that word.
- Apparel grammar: large back rectangular scene; headline at top; mascot centered; small brand footer; tiny front hit.
- Confounders: cannabis novelty, coastal-brand audience, same-family duplicate listing, sale/merchandising labels.
- Prohibited transfer: exact phrase + pufferfish pairing, tropical scene, same headline/mascot/footer composition.
- Decode confidence: `HIGH`.

### TRACE-P001-DTC-08 — post-selection exclusion record (South Coast Outdoors, rank 1)

- Product: [Blue Marlin – Offshore Saltwater Fishing Tee SC1600](https://southcoastoutdoorscompany.com/products/blue-marlin-sc1600)
- Collection/rank/date: [All T-Shirts, native Best selling](https://southcoastoutdoorscompany.com/collections/all-t-shirts?sort_by=best-selling), 1, 2026-09-25.
- Execution status: selected during the run; stable source ID retained for audit continuity.
- Controlling final disposition: `IP-EXCLUDED:BRAND-DEPENDENT` under frozen v0.2; maps to proposed-v0.3 `BRAND-EXCLUDED`.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | EXACT | LIFETIME | SINGLE-SNAPSHOT`.
- Reviews: `No reviews` shown for this exact product.
- Exclusion evidence: the marlin is subordinate to prominent `SOUTH COAST OUTDOORS CO. / IT'S A WAY OF LIFE / FROM TEXAS TO KEY WEST` house-brand, motto, and regional copy, plus a matching front brand mark. The original notes already identified that brand and region may drive demand more than the art.
- Gate 0 correction: the observed rank cannot be attributed safely to a transferable design concept independent of the seller's own brand equity. Retaining this source while recognizing that dependency was inconsistent with frozen v0.2 Gate 0.
- Use restriction: audit evidence only; no source decode, insider-truth inference, candidate mechanism, apparel grammar, clustering, corroboration, or recipe-maturity credit.
- Backfill: none.

### TRACE-P001-DTC-09 — post-selection exclusion record (Raiz'd Up Outfitters, raw rank 5)

- Product: [RUF - Built for the Salt - Women's](https://raizdupoutfitters.com/products/ruf-built-for-the-salt-tee)
- Collection/rank/date: [All, native Best selling](https://raizdupoutfitters.com/collections/all?sort_by=best-selling), 5, 2026-09-25.
- Higher-rank dispositions: ranks 1–3 quarantine Jeep Wrangler/Gladiator references and recognizable vehicle dependency; rank 4 is principally house-logo/brand merch (`Florida Roots`) and was excluded under the brand-dependent rule.
- Execution status: selected during the run; stable source ID retained for audit continuity.
- Controlling final disposition: `IP-EXCLUDED:BRAND-DEPENDENT` under frozen v0.2; maps to proposed-v0.3 `BRAND-EXCLUDED`.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | EXACT | LIFETIME | SINGLE-SNAPSHOT`.
- Reviews: no separately attributable product count; shop-level review markup is not used.
- Exclusion evidence: `RAIZ'D UP FISHING` is visually dominant over `BUILT FOR THE SALT / Made for the Adventure`, with an additional front fishing logo. The original notes already identified the brand name as visually dominant.
- Gate 0 correction: excluding rank 4 for house-brand dependence but retaining this still more brand-dominant rank-5 family was internally inconsistent. Its rank cannot be attributed safely to a transferable design concept independent of Raiz'd Up brand equity.
- Use restriction: audit evidence only; no source decode, insider-truth inference, candidate mechanism, apparel grammar, clustering, corroboration, or recipe-maturity credit.
- Backfill: none.

### TRACE-P001-DTC-10 — post-selection quarantine record (Sloth Hiking Club, rank 1)

- Product: [Out Of Breath T-shirt](https://slothhikingclub.com/products/out-of-breath-t-shirt)
- Collection/rank/date: [Hiking T-Shirt Sale (the store's broad tee pool), native Best selling](https://slothhikingclub.com/collections/sale?sort_by=best-selling), 1, 2026-09-25.
- Execution status: selected during the run; stable source ID retained for audit continuity.
- Controlling final disposition: `IP-QUARANTINE` under frozen v0.2.
- Evidence vector: `WITHIN-STORE-SALES-ORDER | EXACT | LIFETIME | SINGLE-SNAPSHOT`.
- Reviews: product structured data reports `396`; visible `4.8 / 5 from 4,613` is a mixed store-wide feed and is not attributed wholesale to this design.
- Expression under audit: `OUT OF BREATH / HIKING SOCIETY / DON'T WORRY, I'LL BE THERE IN A MINUTE` in an outdoor-club badge treatment.
- Representative recurrence evidence: an [Etsy listing](https://www.etsy.com/listing/1742021183/out-of-breath-hiking-society-dont-worry) and a [TeePublic listing](https://www.teepublic.com/t-shirt/49883254-out-of-breath-hiking-society-dont-worry-ill-be-the) show the exact phrase and closely corresponding hiking-society design across sellers.
- Gate 0 correction: the exact cross-market recurrence makes source independence and provenance unresolved. The evidence does not establish which sellers created, licensed, or copied it, so frozen v0.2 requires quarantine.
- Use restriction: audit evidence only; no source decode, SDC, insider-truth inference, candidate mechanism, apparel grammar, clustering, corroboration, recipe-maturity credit, or transfer use.
- Scope: contamination control only, not an infringement finding or legal conclusion.
- Backfill: none.

## Failed preselected stores

- **OpenTrail:** current indexed Shopify Best Sellers page exposed 16 ranked products, but the frozen method requires a broad tee/all collection. Direct access to `/collections/all?sort_by=best-selling` and product pages failed with DNS/prohibited-IP/403 errors. The indexed curated collection was not substituted for the required broad pool; no source was selected.
- **Two-Cross:** cached search evidence showed a sarcastic-tee assortment three months earlier, but the current accessible Best Sellers page contained only sweatshirts/hoodies and the broad collection returned 502. No current qualifying tee family was selected.

## Method frictions and v0.3 recommendations

1. Define preselection as occurring before **ranked-result inspection**, while permitting assortment/category-level inspection needed to judge tee-led status and IP/brand predominance.
2. Require three-part native-sort verification: broad collection scope, explicit `sort_by=best-selling` URL, and active/selected/checked `Best selling` state in returned HTML. A page merely named “Best Sellers” is insufficient.
3. Freeze whether `24` means raw ranked product cards or 24 deduplicated design families. Recommended: capture the first 24 raw cards, preserve raw ranks, collapse families, and continue only if a quota explicitly requires 24 distinct families.
4. Add `RAW_PRODUCT_RANK`, `FAMILY_FIRST_RANK`, and `DUPLICATE_RANKS`; Crazy Dog rank 1/rank 3 and SeaMonkey rank 1/rank 5 exposed this need.
5. Add a store-failure code set: `ACCESS`, `SORT-UNVERIFIED`, `NO-BROAD-COLLECTION`, `ASSORTMENT-CHANGED`, `NO-ELIGIBLE-FAMILY`; never replace a preselected store after ranked results are seen.
6. Treat all Shopify native best-selling observations as `LIFETIME`; Shopify says zero-sale collections fall back to newest-first, so add a `NONZERO-SALES-CORROBORATION` flag (item review, seller statement, repeat snapshot, or other evidence).
7. Never infer item-review scope from placement or JSON-LD alone. Record `ITEM-VISIBLE`, `ITEM-STRUCTURED`, `SAME-FAMILY`, `SHOP-WIDE`, or `UNCLEAR`, and preserve conflicting counts separately.
8. Capture page-render/access mode (`LIVE-HTML`, `SEARCH-INDEX`, `BLOCKED`) and source freshness. Storefronts changed between crawl and scan in this pilot.
9. Run a cross-market provenance/stock-template screen before source decoding. Exact or closely corresponding recurrence with unresolved origin maps to frozen-v0.2 `IP-QUARANTINE` and cannot support SDC, clustering, corroboration, recipe maturity, or transfer until resolved.
10. Add `BRAND-EXCLUDED` as an explicit eligibility disposition distinct from `IP-EXCLUDED`; the final audit removed two execution-selected families whose own-store branding plausibly drove demand, and the separation makes that decision legible without treating house branding as third-party IP.
11. Do not promote any recipe to `CORROBORATED` from this stratum alone. The 4 final qualifying source families yielded candidate mechanisms, but the frozen maturity rule still requires non-derivative support across unrelated niches/sellers and ideally other platforms.
