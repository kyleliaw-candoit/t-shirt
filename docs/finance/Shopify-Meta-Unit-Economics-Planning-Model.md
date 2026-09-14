---
title: Shopify and Meta Unit Economics Planning Model
owner: Finance Analyst
reviewers:
  - Strategy Advisor
status: Provisional planning model
version: 0.1
last_updated: 2026-09-14
---

# Shopify and Meta Unit Economics Planning Model

## Purpose

This document provides a reusable framework for evaluating Shopify, print-on-demand (POD), and Meta advertising economics.

The formulas and decision logic are canonical. All dollar assumptions and performance scenarios are provisional until replaced by vendor quotes and observed sales data.

This model is not the transaction ledger. Actual cash activity belongs in [Finance-Ledger.md](./Finance-Ledger.md).

## Current strategic decision

Do not activate Shopify solely for the current Tier 2 MVV landing-page test.

1. Complete the current $20–$50 Tier 2 validation.
2. Select a POD vendor and order samples.
3. Record actual product, print, and delivered-shipping costs.
4. Choose retail price and shipping policy.
5. Recalculate first-order contribution and allowable CAC.
6. Run the ten-unit Tier 3 presale.
7. Add Shopify when accepting real orders requires checkout.
8. Run a purchase-optimized Meta test only after checkout and fulfillment are operational.

## Definitions and formulas

| Metric | Definition | Formula |
|---|---|---|
| AOV | Average amount collected per order, including charged shipping and discounts as applicable | Revenue / orders |
| CPM | Meta cost per 1,000 impressions | Ad spend / impressions × 1,000 |
| CTR | Percentage of impressions producing a click | Clicks / impressions |
| CPC | Advertising cost per click | Ad spend / clicks |
| Purchase conversion rate | Percentage of clicks producing an order | Orders / clicks |
| CAC / CPA | Advertising cost per acquired order | Ad spend / orders |
| ROAS | Revenue generated per advertising dollar | Revenue / ad spend |
| Pre-ad contribution | Revenue available after variable order costs but before acquisition | AOV − POD cost − fulfillment shipping − payment fee − variable-order reserve |
| Contribution after ads and Shopify | Scenario output; not operating profit | Pre-ad contribution × orders − ad spend − Shopify subscription |

### First-order break-even CAC

```
First-order break-even CAC
= AOV
− POD product/printing cost
− fulfillment shipping paid by seller
− payment-processing fee
− variable-order reserve
```

### Target CAC

```
Target CAC
= pre-ad contribution
− required contribution per order
```

The variable-order reserve should cover returns, replacements, fraud, and customer-service remedies. No permanent reserve percentage is set yet; establish it from observed data.

### Break-even ROAS

```
Break-even ROAS = AOV / first-order break-even CAC
```

Do not justify an unprofitable first order using assumed lifetime value. Repeat-customer economics may be added only after repeat rate, reorder timing, and repeat-acquisition cost are observed.

## Dated provisional assumptions

Planning date: **2026-09-14**

| Input | Provisional value | Replacement needed |
|---|---:|---|
| Single-shirt AOV | $35.00 | Actual product price, discounts, and shipping charged |
| POD shirt and printing | $13.00 | Selected vendor quote |
| Fulfillment shipping absorbed by seller | $5.00 | Selected vendor and shipping-policy data |
| Shopify Basic subscription | $39/month month-to-month | Actual plan and billing choice |
| Shopify Payments standard domestic consumer-card fee | 2.9% + $0.30 | Store-specific rate |
| Variable-order reserve | $0.00 in illustrations only | Observed return/replacement/fraud experience |
| Items per order | 1 | Actual order data |

Current official Shopify pricing lists Basic at $39 month-to-month or $29/month when billed yearly, with standard online-card rates starting at 2.9% + $0.30. Sources: [Shopify pricing](https://www.shopify.com/pricing) and [Shopify Payments U.S. card types](https://help.shopify.com/en/manual/payments/shopify-payments/transactions/credit-card-rates).

## Provisional single-order economics

| One $35 order | Amount |
|---|---:|
| Customer revenue | $35.00 |
| POD shirt and printing | −$13.00 |
| Fulfillment shipping absorbed | −$5.00 |
| Shopify Payments | −$1.32 |
| Variable-order reserve | −$0.00 |
| **Pre-ad contribution** | **$15.68** |

Under these unverified assumptions:

- First-order break-even CAC before fixed overhead: **$15.68**
- Break-even ROAS before other costs: **2.23**
- CAC of $10 implies ROAS of **3.50** and leaves $5.68 per order before fixed and omitted costs.
- CAC of $12 implies ROAS of **2.92** and leaves $3.68 per order before fixed and omitted costs.

A $10–$12 CAC is therefore a **learning-stage guardrail**, not a proven healthy long-term target.

## Meta advertising sensitivity illustrations

Meta has no recurring platform subscription. Ad delivery and price are auction-based. Daily budgets are averages and may fluctuate; a lifetime budget controls the total campaign allocation. Source: [Meta—About budgets](https://www.facebook.com/business/help/214319341922580).

These scenarios are mathematical sensitivities, not Meta forecasts or industry benchmarks.

| Metric | Weak | Middle | Strong |
|---|---:|---:|---:|
| Meta spend | $300 | $300 | $300 |
| Assumed CPM | $15 | $12 | $10 |
| Impressions | 20,000 | 25,000 | 30,000 |
| Link CTR | 1.5% | 2.5% | 3.5% |
| Clicks | 300 | 625 | 1,050 |
| CPC | $1.00 | $0.48 | $0.29 |
| Purchase conversion rate | 1.0% | 2.5% | 4.0% |
| Expected orders | 3.0 | 15.6 | 42.0 |
| CAC | $100.00 | $19.20 | $7.14 |
| Revenue | $105 | $547 | $1,470 |
| Pre-ad contribution | $47 | $245 | $659 |
| Meta ads | −$300 | −$300 | −$300 |
| Shopify Basic | −$39 | −$39 | −$39 |
| **Contribution after ads and Shopify** | **−$292** | **−$94** | **+$320** |

Expected fractional orders are retained to show model mathematics. Actual campaigns produce whole orders and will be noisier at small sample sizes.

## Monthly 100-order CAC sensitivity

| Monthly model | CAC $10 | CAC $15 | CAC $20 |
|---|---:|---:|---:|
| Revenue: 100 × $35 | $3,500 | $3,500 | $3,500 |
| POD production | −$1,300 | −$1,300 | −$1,300 |
| Fulfillment shipping absorbed | −$500 | −$500 | −$500 |
| Shopify Payments | −$132 | −$132 | −$132 |
| Meta advertising | −$1,000 | −$1,500 | −$2,000 |
| Shopify Basic | −$39 | −$39 | −$39 |
| **Contribution after ads and Shopify** | **$529** | **$29** | **−$471** |
| **Contribution percentage** | **15.1%** | **0.8%** | **−13.5%** |

This is not operating profit. It excludes variable-order reserves, samples, paid apps, accounting, legal/LLC costs, insurance, owner compensation, income tax, and other overhead.

## Shipping-policy treatment

Keep shipping revenue and fulfillment shipping visible rather than automatically netting them.

The model must support:

1. customer pays all shipping;
2. seller subsidizes part of shipping;
3. free shipping above a threshold.

Payment processing is generally applied to the amount collected from the customer, including shipping. Recalculate AOV and payment fees for the selected policy.

## Tier 2 versus commercial acquisition

- **Tier 2 Traffic campaign:** validates audience and design interest through impressions, clicks, and landing-page intent.
- **Future Sales campaign:** tests purchase CAC and commercial viability after checkout and fulfillment exist.

Traffic-campaign CPC must not be used to forecast purchase CAC. A CTR above the MVV threshold is evidence of interest, not proof of profitable customer acquisition.

## Working-capital risk

POD providers may charge when an order enters fulfillment, while Shopify payouts arrive later. Meta spend is paid independently of Shopify payout timing. Maintain enough cash for:

```
Working-capital reserve
= unpaid POD obligations
+ accrued advertising spend
+ refund/replacement buffer
```

Payout delays, holds, refunds, and replacements can create a cash shortfall even when the contribution model is positive.

## Update policy

Replace provisional inputs when the following become available:

- POD vendor quote and sample results;
- actual product price and discounts;
- chosen shipping policy;
- actual payment-method mix and processing fees;
- observed returns and replacements;
- purchase-optimized Meta campaign results;
- actual AOV and items per order;
- observed repeat-purchase behavior.

Each revision should retain its date and distinguish actuals from assumptions.
