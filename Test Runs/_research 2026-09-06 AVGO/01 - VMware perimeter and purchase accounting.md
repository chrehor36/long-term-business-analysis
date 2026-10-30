# AVGO research 01 — VMware perimeter and purchase accounting
Primary-filing sweep, SEC EDGAR. Compiled 2026-09-06.
All figures $ millions unless stated. Every figure carries its accession number.

## SOURCES OPENED

| Doc | Accession | Primary file | Filed | Period |
|---|---|---|---|---|
| VMware 10-K FY2023 | 0001124610-23-000015 | vmw-20230203.htm | 2023-03-28 | 2023-02-03 |
| VMware 10-K FY2022 | 0001124610-22-000009 | vmw-20220128.htm | 2022-03-24 | 2022-01-28 |
| VMware 10-K FY2021 | 0001124610-21-000015 | vmw-20210129.htm | 2021-03-26 | 2021-01-29 |
| Broadcom 8-K/A | 0001140361-24-006447 | ef20018945_8ka.htm + ex99-2, ex99-3 | 2024-02-08 | 2023-11-22 |
| Broadcom 10-K FY2025 | 0001730168-25-000121 | avgo-20251102.htm | 2025-12-18 | 2025-11-02 |
| Broadcom 10-K FY2024 | 0001730168-24-000139 | avgo-20241103.htm | 2024-12-20 | 2024-11-03 |
| Broadcom 10-K FY2023 | 0001730168-23-000096 | avgo-20231029.htm | 2023-12-14 | 2023-10-29 |
| Broadcom 10-K FY2022 | 0001730168-22-000118 | avgo-20221030.htm | 2022-12-16 | 2022-10-30 |
| Broadcom 10-K FY2021 | 0001730168-21-000153 | avgo-20211031.htm | 2021-12-17 | 2021-10-31 |

CIK VMware = 1124610 (EDGAR name now "VMWARE LLC"). CIK Broadcom Inc. = 1730168.
All requests carried User-Agent `chrehor36@gmail.com framework-run`.

---

# TASK A — VMware standalone owner earnings

Source of record: **VMware FY2023 10-K, accession 0001124610-23-000015**, CONSOLIDATED
STATEMENTS OF INCOME (p.63 of the filed HTML) and CONSOLIDATED STATEMENTS OF CASH FLOWS
(p.66). That one filing carries all three fiscal years.

**Cross-check performed (operator rule 4):** every FY2021 and FY2022 line below was
re-read against the *originally filed* 10-Ks — 0001124610-21-000015 and
0001124610-22-000009 — from their own filed HTML statements. **All figures agree
exactly; no restatement.** (FY2021 OCF 4,409 and capex 329 appear identically in the
FY2021, FY2022 and FY2023 10-Ks; FY2022 OCF 4,357 and capex 386 appear identically in
the FY2022 and FY2023 10-Ks.)

Note on fiscal calendar: **FY2023 was a 53-week year** (ended 2023-02-03); FY2022 and
FY2021 were 52 weeks. VMware's MD&A repeatedly attributes cost growth to "the extra week
in fiscal 2023."

## A1. Revenue by class — filed income statement

| | FY2021 (2021-01-29) | FY2022 (2022-01-28) | FY2023 (2023-02-03) |
|---|---|---|---|
| License | 3,033 | 3,128 | 2,835 |
| Subscription and SaaS | 2,587 | 3,205 | 4,012 |
| Services | 6,147 | 6,518 | 6,503 |
| **Total revenue** | **11,767** | **12,851** | **13,350** |

The classic on-prem licence line was already **shrinking** by FY2023 (2,835 vs 3,128,
-9.4%), with subscription/SaaS carrying all the growth. Services — overwhelmingly
software maintenance and support on the installed licence base — was flat to slightly
down (6,503 vs 6,518).

Related-party (Dell) revenue inside those totals, same statement, footnote (1):

| | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| License — Dell | 1,598 | 1,530 | 1,395 |
| Subscription and SaaS — Dell | 524 | 820 | 1,132 |
| Services — Dell | 1,994 | 2,470 | 2,566 |
| **Total Dell** | **4,116** | **4,820** | **5,093** |

Verbatim, FY2023 10-K: *"During the years ended February 3, 2023, January 28, 2022 and
January 29, 2021, revenue from Dell accounted for 38%, 38% and 35% of VMware's
consolidated revenue, respectively."* Concentration risk on the acquired perimeter.

## A2. Operating income (GAAP) — filed income statement

| | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Operating income | 2,388 | 2,387 | **2,022** |
| Operating margin | 20.3% | 18.6% | 15.1% |
| Net income | 2,058 | 1,820 | 1,314 |

Operating income was **flat then falling** on rising revenue. Margin compressed 520bp
over two years.

## A3. Cash-flow items — filed statement of cash flows

| | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Net cash provided by operating activities | 4,409 | 4,357 | 4,300 |
| Stock-based compensation (add-back) | 1,122 | 1,075 | 1,290 |
| Depreciation and amortization (add-back) | 1,025 | 1,110 | 1,234 |
| Additions to property and equipment (capex) | (329) | (386) | (450) |
| Increase in unearned revenue (in OCF) | +1,013 | +908 | +1,520 |

**Capitalized software: no separate line item exists.** Sweep performed: grep of all
three 10-K texts for "capitalized software", "capitalized internal-use", "software
development costs"; read of the "Capitalized Software Development Costs" accounting
policy note in the FY2023 10-K. The answer is in the policy note, verbatim:

> "Costs associated with internal-use software, including those used to provide hosted
> services, during the application development stage are capitalized. ... **The
> capitalized amounts are included in property and equipment, net on the consolidated
> balance sheets.**"

and, for software to be sold:

> "During the years presented, software development costs incurred for products during
> the time period between reaching technological feasibility and general release were
> **not material and accordingly were expensed as incurred**."

So internal-use capitalised software is **already inside** the 450/386/329 capex line —
no double count, no missing line. MD&A confirms it is material within that line:
FY2023 R&D was held down by *"increased capitalized internal-use software development
costs of $58 million."*

## A4. OWNER EARNINGS — VMware standalone

**OE = OCF − SBC − capex**

| | FY2021 | FY2022 | FY2023 |
|---|---|---|---|
| Net cash provided by operating activities | 4,409 | 4,357 | 4,300 |
| less Stock-based compensation | (1,122) | (1,075) | (1,290) |
| less Additions to property and equipment | (329) | (386) | (450) |
| **= Owner earnings** | **2,958** | **2,896** | **2,560** |
| OE margin on revenue | 25.1% | 22.5% | 19.2% |

**Three-year mean owner earnings = 2,805.**

Three observations that matter for the perimeter:

1. **The series declines every year** — 2,958 → 2,896 → 2,560, a 13% fall, while revenue
   rose 13%. This is the opposite of the direction of travel implied by the headline
   OCF, which looks flat at ~4.3bn. The whole gap is SBC (+168 in FY2023) and capex
   (+121 over two years).
2. **SBC is 30% of OCF** and rising. Treating it as non-cash would overstate owner
   earnings by ~1.3bn in FY2023 alone.
3. **OCF is flattered by unearned revenue.** The increase in unearned revenue
   contributed +1,013 / +908 / +1,520 to OCF in FY2021/22/23 — i.e. in FY2023, **59% of
   owner earnings came from the deferred-revenue build**, customers prepaying. This is
   the exact balance that purchase accounting later writes down (Task B), which is why
   the acquired perimeter's cash generation is not the standalone perimeter's cash
   generation.

Also for reference, VMware PP&E note (FY2023 10-K, Note L): total property and
equipment, net **1,623** (FY2023) vs **1,461** (FY2022); *"Depreciation expense was $319
million, $276 million and $253 million during the years ended February 3, 2023, January
28, 2022 and January 29, 2021, respectively."* Note that D&A in the cash-flow statement
was 1,234 in FY2023 against only 319 of real depreciation — the residual ~915 is
amortisation of intangibles and of capitalised commissions/deferred costs, not physical
asset consumption.

---
