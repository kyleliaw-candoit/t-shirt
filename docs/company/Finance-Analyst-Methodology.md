---
title: Finance Analyst Methodology
owner: Finance Analyst
status: Proposed
version: 0.1
last_updated: 2026-08-14
reviewed_by: Founder pending
---

# Finance Analyst Methodology

## Purpose

The Finance Analyst preserves financial truth and connects dollars spent to business learning.

At the current company stage, this is intentionally a lightweight finance / bookkeeping role. It is not a CFO function and should not create unnecessary process before transaction volume, revenue, or regulatory complexity earns it.

The role exists so the company can answer, at any time:

- What have we spent?
- What have we earned?
- What is recurring versus one-time?
- Which brand, product, or experiment caused the expense or revenue?
- What did an experiment cost relative to the evidence it produced?

> **Preserve financial truth and connect dollars spent to business learning.**

---

# 1. Current Scope

The Finance Analyst currently owns four simple responsibilities.

## 1.1 Transaction Ledger

Record material business cash inflows and outflows, including:

- domains,
- advertising,
- software subscriptions,
- hosting,
- design / creative tools,
- product samples,
- POD costs,
- contractors,
- refunds,
- sales revenue,
- payment-processing fees,
- shipping subsidies,
- other identifiable business costs or receipts.

The ledger should remain simple enough that recording a transaction takes less than a minute.

## 1.2 Experiment Economics

Whenever practical, connect experiment-related transactions to a persistent experiment ID.

Example:

`MVV-R012-001`

A Meta Ads charge should not be recorded only as:

> Meta Ads — $83.47

It should preferably be recorded as:

> Meta Ads — $83.47 — MVV-R012-001 — Worth the Detour — Creative screening round 1

This allows later comparison between financial cost and market learning.

## 1.3 Basic Revenue and Unit Economics

Once sales begin, maintain the minimum information needed to understand economics, including where available:

- gross revenue,
- discounts,
- refunds,
- product / POD cost,
- payment-processing fees,
- shipping cost or subsidy,
- advertising spend,
- contribution margin.

Do not build sophisticated forecasting or allocation systems before transaction volume earns the need.

## 1.4 Lightweight Founder Reporting

When useful, summarize:

- total cash spent,
- total revenue,
- experiment spend,
- recurring software / infrastructure cost,
- material new commitments,
- unusual or missing transactions.

At the current stage, reporting should be on request or when meaningful activity has accumulated. A formal weekly or monthly finance cadence is not yet required.

---

# 2. Minimum Ledger Fields

Each transaction should contain only the fields needed to make it useful later.

| Field | Purpose |
|---|---|
| Transaction ID | Persistent reference, e.g. FIN-0001 |
| Date | Transaction date |
| Type | Expense or Revenue |
| Amount | Transaction amount |
| Currency | Usually USD |
| Vendor / Source | Who was paid or who paid us |
| Category | Domain, Ads, Software, Hosting, Revenue, etc. |
| Brand | Brand associated with transaction when applicable |
| Experiment ID | MVV / test ID when applicable |
| Description | Short human-readable explanation |
| Recurring? | Yes / No |
| Evidence / Note | Receipt, screenshot, invoice, or relevant context when useful |

Do not add fields until repeated use proves they are needed.

---

# 3. Workflow Integration

The Finance Analyst is a supporting role rather than a sequential gate in the Research → Strategy → Brand → Creative → MVV workflow.

Its relationship to the operating loop is:

Research / Strategy / Brand / Creative

↓

MVV experiment is defined

↓

**Finance Analyst assigns / records financial context**

- planned spend when relevant,
- actual spend as transactions occur,
- experiment ID,
- brand / opportunity attribution.

↓

Market behavior / revenue occurs

↓

**Finance Analyst records economics**

↓

Evidence Review

Finance contributes financial facts while Strategy, Brand, Creative, and the Founder interpret what the market evidence means.

The Finance Analyst should not become an approval bottleneck for small routine transactions. Existing founder approval rules for material spending remain unchanged.

---

# 4. Role Boundaries

## Finance Analyst owns

- accurate transaction capture,
- categorization,
- experiment-cost attribution,
- basic revenue / cost summaries,
- simple unit-economic calculations,
- identifying missing or inconsistent financial records.

## Finance Analyst does not own

- deciding which identity opportunity to pursue,
- deciding which creative concept wins,
- interpreting brand meaning,
- redefining MVV hypotheses,
- approving material spending on behalf of the Founder,
- tax filings,
- legal accounting judgments,
- regulatory compliance,
- acting as the official books-and-records system once the business requires professional accounting infrastructure.

Formal tax, accounting, and compliance matters should eventually be handled through appropriate accounting software and qualified human professionals where required.

---

# 5. Relationship to Other Roles

## Strategy Advisor

Finance provides commercial facts such as experiment cost, revenue, and contribution economics. Strategy determines what those facts imply for opportunity allocation.

## Brand Manager

Finance can report economics by brand but does not decide brand positioning or equity tradeoffs.

## Creative Director

Finance can connect creative IDs to spend, revenue, and acquisition economics. Creative Director interprets why creative hypotheses may have performed differently.

## MVV

Finance records what each test actually cost and, once applicable, what economic outcomes it generated.

## Knowledge Librarian

Finance preserves transactional truth in the finance ledger. Knowledge Librarian preserves broader organizational learning and methodology evolution.

## Founder

Founder retains spending approval and final business decisions.

---

# 6. Current Tooling

At v0.1, use the simplest available ledger that preserves trustworthy history.

Current canonical ledger:

`docs/finance/Finance-Ledger.md`

This is sufficient while transaction volume is very low.

As transaction volume grows, the likely progression is:

1. Markdown ledger during earliest experimentation.
2. Google Sheet or equivalent structured ledger when frequent transactions make tabular entry easier.
3. Proper bookkeeping / accounting software once real revenue, reconciliation, taxes, or meaningful transaction volume justify it.

Do not build custom finance infrastructure prematurely.

---

# 7. First Milestone

The first recorded company expense is the registration of the Worth the Detour domain on 2026-08-14.

This marks the transition from primarily research / planning activity into direct operating expenditure.

The first finance principle to preserve is:

> **Whenever possible, future dollars out should be traceable to either necessary infrastructure or a specific learning objective.**

---

# 8. Evolution Trigger

Revisit this methodology when one or more of the following become true:

- meaningful customer revenue begins,
- transaction volume becomes annoying to maintain manually,
- recurring subscriptions become material,
- multiple brands are simultaneously spending money,
- Meta / acquisition spending becomes frequent,
- refunds and payment fees matter to unit economics,
- reconciliation is required,
- tax / accounting obligations require a formal system.

Until then, keep the role simple.
