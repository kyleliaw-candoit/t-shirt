---
title: Finance Ledger
owner: Finance Analyst
status: Active
version: 0.2
last_updated: 2026-09-03
---

# Finance Ledger

## Purpose

This is the lightweight canonical transaction ledger for the company's earliest operating stage.

Use it to preserve material cash inflows and outflows until transaction volume justifies moving the working ledger to a structured spreadsheet or accounting system.

Amounts should be recorded in the transaction currency. Do not infer taxes, fees, payment method, or accounting treatment when they are not known.

---

# Transactions

| Transaction ID | Date | Type | Amount | Currency | Vendor / Source | Category | Brand | Experiment ID | Description | Recurring? | Evidence / Note |
|---|---|---:|---:|---|---|---|---|---|---|---|---|
| FIN-0001 | 2026-08-14 | Expense | 10.46 | USD | Cloudflare Registrar | Domain | Worth the Detour | — | One-year registration of `worth-the-detour.com` | Yes — annual auto-renew currently enabled | Founder-provided Cloudflare purchase and domain-status screenshots; current renewal shown as $10.46/year |
| FIN-0002 | 2026-08-31 | Expense | 300.00 | USD | Texas Secretary of State | Legal / Formation | Company-wide | — | Certificate of Formation for Taukay LLC | No | Founder-provided Texas Secretary of State receipt; $300.00 card payment accepted. Receipt notes that a separate 2.7% convenience fee may appear on the card statement; no such fee is recorded without confirmation. |

---

# Running Summary

As of 2026-08-31:

- **Recorded expenses:** $310.46
- **Recorded revenue:** $0.00
- **Net recorded cash flow:** -$310.46
- **Known recurring annual commitment:** $10.46/year for `worth-the-detour.com`, subject to future registrar pricing / renewal decisions

---

# Recording Rule

For each new material transaction:

1. assign the next `FIN-####` ID;
2. record the actual transaction date and amount;
3. attach the relevant brand and experiment ID when applicable;
4. note whether the cost is recurring;
5. preserve enough evidence/context to understand the transaction later;
6. avoid speculative accounting classifications.

During MVV, Meta Ads and other test-specific expenses should be tied to the appropriate `MVV-...` experiment ID whenever possible.
