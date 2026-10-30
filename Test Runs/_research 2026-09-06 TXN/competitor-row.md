# TXN: COMPETITOR ROW (filing-sourced)
Built 2026-09-06. Q2 requires the competitor row: **a moat is a relative claim.**

**STATUS: COMPUTATION, NOT A CLEARANCE.** Nothing here is a Q1-Q4 verdict. This is the
comparative evidence a Q2 judgment would be made against.

---
## 0. EVIDENCE LADDER: which rung each name sits on

| Company | Rung | Source | Note |
|---|---|---|---|
| TXN | **SEC primary (top rung)** | 10-K, CIK 0000097476 | US domestic filer |
| ADI | **SEC primary** | 10-K, CIK 0000006281 | US domestic filer |
| MCHP | **SEC primary** | 10-K, CIK 0000827054 | US domestic filer |
| NXPI | **SEC primary** | 10-K, CIK 0001413447 | Dutch, but files 10-K on US GAAP |
| ON | **SEC primary** | 10-K, CIK 0001097864 | US domestic filer |
| STM | **SEC primary** | 20-F, CIK 0000932787 | **Checked: STM IS an SEC registrant.** Files 20-F, reports in **US GAAP, USD**. The brief flagged STM as possibly IR-rung; it is not. It is on the SEC rung, same as the rest. |
| Infineon | IR rung (see §7) | company-published annual report | not an SEC registrant; German, IFRS, EUR, FYE 30 Sept |
| Renesas | IR rung (see §7) | company-published annual report | not an SEC registrant; TSE, IFRS, JPY, FYE 31 Dec |

All SEC data pulled from `data.sec.gov` XBRL companyfacts and `www.sec.gov/Archives`
with User-Agent `Chris Hrehor chrehor36@gmail.com`. Accession numbers in §6.

**Operator rule 4 satisfied:** the filing was read, not just the tagged data. Cross-check
in §1.1 below against the filed statement image.

---
## 1. THE NUMBER THE PRIOR RUN GOT: resolved

### 1.1 TXN: is 34.1% the OPERATING margin or the PRE-TAX margin?

**It is the OPERATING margin.** Not the pre-tax margin. Shown from the filed statement.

Source: Texas Instruments 10-K for FY ended 2025-12-31, filed 2026-02-06, accession
**0000097476-26-000059**, *Consolidated Statements of Income* (R3), $ in millions:

```
Revenue                                    17,682
Cost of revenue (COR)                       7,599
Gross profit                               10,083
Research and development (R&D)              2,083
Selling, general and administrative        1,860
Restructuring charges/other                   117
Operating profit                            6,023      <-- the filed operating income line
Other income (expense), net (OI&E)            230
Interest and debt expense                     543
Income before income taxes                  5,710      <-- EBT
```

Arithmetic:

| | | |
|---|---|---|
| **Operating margin** | 6,023 / 17,682 | **34.06%** → rounds to **34.1%** ✅ |
| **Pre-tax (EBT) margin** | 5,710 / 17,682 | **32.29%** → **32.3%** |

The two differ by 177 bp. TXN's EBT sits **below** operating profit because interest and
debt expense (543) now exceeds other income (230), a consequence of the debt raised to
fund the 300mm build. That crossover happened in FY2025: in FY2024, OI&E (496) roughly
offset interest (508) and the two margins were both 34.9%.

**So the prior run's label "operating/EBT margin" is wrong as a compound. 34.1% is
operating only.** The correct pre-tax figure for a Q4/Q5 owner-earnings build is 32.3%.

### 1.2 NXPI: reproduce 24.8% on $12,269M

Source: NXP Semiconductors 10-K for FY ended 2025-12-31, filed 2026-02-19, accession
**0001413447-26-000008**.

| | | |
|---|---|---|
| Revenue | | 12,269 |
| Operating income | | 3,047 |
| **Operating margin** | 3,047 / 12,269 | **24.83%** → **24.8%** ✅ |
| Income before income taxes | | 2,663 |
| **Pre-tax margin** | 2,663 / 12,269 | **21.71%** → **21.7%** |

**Same answer: 24.8% is the OPERATING margin, not pre-tax.** Both prior-run figures are
operating margins and are reproduced exactly. The two numbers are consistent with each
other; the prior run was comparing like with like, it just mislabelled the line.

### 1.3 The clincher: TXN says it itself, verbatim

TXN 10-K FY2025, MD&A, on the same page as the arithmetic:

> "Operating profit was $6.02 billion, or **34.1% of revenue**, compared with $5.47
> billion, or 34.9% of revenue."

TXN's own filing labels 34.1% as **operating profit** margin. No inference required.

---
## 2. THE CENTRAL COMPARISON: gross margin through the 2023-2025 analog downcycle

The question: **did gross margin hold?** All figures from each company's own 10-K, US GAAP,
gross profit / revenue as filed.

### 2.1 Revenue, $M (as filed)

| FY | TXN | ADI | MCHP | NXPI | ON |
|---|---|---|---|---|---|
| 2021 | 18,344 | 7,318 | 5,438 | 11,063 | 6,740 |
| 2022 | **20,028** | 12,014 | 6,821 | 13,205 | 8,326 |
| 2023 | 17,519 | **12,306** | **8,439** | **13,276** | 8,253 |
| 2024 | 15,641 | 9,427 | 7,634 | 12,614 | 7,082 |
| 2025 | 17,682 | 11,020 | 4,402 | 12,269 | 5,995 |
| **Peak year** | FY2022 | FY2023 | FY2023 | FY2023 | FY2023 |
| **FY25 vs peak** | **−11.7%** | −10.4% | **−47.8%** | −7.6% | **−28.0%** |
| **FY25 vs FY21** | **+3.6%** | +50.6% | −19.1% | +10.9% | −11.0% |

*Fiscal-year alignment caveat, stated once and carried:* TXN, NXPI, ON and STM close on
31 Dec. **ADI closes in late Oct/early Nov**: ADI "FY2025" = 3 Nov 2024 to 1 Nov 2025,
about two months ahead of the calendar names. **MCHP closes 31 Mar**: MCHP "FY2025" =
1 Apr 2024 to 31 Mar 2025, i.e. it maps to roughly **calendar 2024**, and MCHP FY2026
(ended 31 Mar 2026) maps to roughly calendar 2025. MCHP is therefore shown on its own
fiscal labels; **read MCHP one year to the right** when comparing to the Dec-31 names.
MCHP's trough is its FY2025 (calendar 2024), which is why its −47.8% looks worse than the
others at the same calendar date. It is not; it is offset.

### 2.2 Gross margin %, as filed (gross profit / revenue): **THE ROW THAT MATTERS**

| FY | **TXN** | ADI | MCHP | NXPI | ON |
|---|---|---|---|---|---|
| 2021 | **67.5** | 61.8 | 62.1 | 54.8 | 40.3 |
| 2022 | **68.8** | 62.7 | 65.2 | 56.9 | 49.0 |
| 2023 | **62.9** | 64.0 | 67.5 | 56.9 | 47.1 |
| 2024 | **58.1** | 57.1 | 65.4 | 56.4 | 45.4 |
| 2025 | **57.0** | 61.5 | 56.1 | 54.7 | 33.1 |
| 2026 (MCHP only) | n/a | n/a | 57.7 | n/a | n/a |
| **Peak GM** | **68.8** (FY22) | 64.0 (FY23) | 67.5 (FY23) | 56.9 (FY22/23) | 49.0 (FY22) |
| **Trough GM** | **57.0** (FY25) | 57.1 (FY24) | 56.1 (FY25) | 54.7 (FY25) | 33.1 (FY25) |
| **Peak-to-trough drop** | **−11.8 pt** | −6.9 pt | −11.4 pt | **−2.2 pt** | **−15.9 pt** |

*Rounding convention: all gaps and point-changes quoted in the prose are computed from the
rounded percentages shown in these tables, so a reader can reproduce every one of them from
the table alone. Computed from unrounded XBRL they differ by at most 0.1 pt.*

**→ The eight-company version of this table, with Infineon and Renesas added on the IR
rung, is at §7.6. It does not soften the finding; it sharpens it. Renesas held gross margin
flat at 57% while capping capex at a stated ~5% of revenue.**

**Read this carefully, because it does not say what a TXN bull wants it to say.**

1. **TXN's gross margin did NOT hold through the downcycle.** It fell from 68.8% to 57.0%,
   an **11.8-point** decline, the second-largest fall in the peer set, behind only ON.
   TXN gave up more gross margin than ADI (−6.9) and far more than NXPI (−2.2).
2. **TXN still has the highest gross margin in the group at the peak (68.8%)** but at the
   trough it is **57.0%, which is BELOW ADI (61.5%) and only 2.3 points above NXPI (54.7%).**
   The gross-margin gap that defines the franchise **swung from +6.1 points over ADI in
   FY2022 (68.8 vs 62.7) to −4.5 points in FY2025 (57.0 vs 61.5), i.e. TXN is now BEHIND
   ADI on gross margin.** A 10.6-point swing in the relative position. Against NXPI the
   lead narrowed from +11.9 points (68.8 vs 56.9) to +2.3 points (57.0 vs 54.7).
3. **NXPI is the one that held.** −2.2 points peak to trough, on a −7.6% revenue decline.
   NXPI is the fab-lite name. That is the uncomfortable finding: the **fab-lite** competitor
   defended gross margin through the downcycle better than the vertically integrated one.
4. **The mechanism is not price, it is fixed cost.** TXN's cost of revenue *rose* from
   6,257 (FY22) to 7,599 (FY25), **+21%**, while revenue *fell* 11.7%. TXN added
   depreciation faster than it added revenue (see §3). This is the 300mm capex cycle
   landing in COGS. It is a deliberate, disclosed choice, not a demand failure.
5. **ADI's recovery is real:** GM back to 61.5% in FY2025 from 57.1%, on +16.9% revenue.
   TXN's FY2025 GM went the *other way* (58.1 → 57.0) despite +13.0% revenue. TXN's
   incremental gross margin in FY2025 was 989/2,041 = **48.5%**, well below its 57% average.
   Depreciation is still climbing into the P&L.
6. **ON is the broken one.** GM 49.0 → 33.1, operating margin 30.8% → 1.4%. ON FY2025 is
   a different animal from the rest of the row.

### 2.3 Same window, operating margin % (filed operating income / revenue)

| FY | **TXN** | ADI | MCHP | NXPI | ON | STM |
|---|---|---|---|---|---|---|
| 2021 | **48.8** | 23.1 | 18.4 | 23.3 | 19.1 | 19.0 |
| 2022 | **50.6** | 27.3 | 27.1 | 28.8 | 28.3 | 27.5 |
| 2023 | **41.8** | 31.1 | 36.9 | 27.6 | 30.8 | 26.7 |
| 2024 | **34.9** | 21.6 | 33.7 | 27.1 | 25.0 | 12.6 |
| 2025 | **34.1** | 26.6 | 6.7 | 24.8 | 1.4 | 1.5 |
| 2026 (MCHP) | n/a | n/a | 10.4 | n/a | n/a | n/a |

TXN still leads the row on operating margin in every year, but the lead over NXPI shrank
from **21.8 points (FY22) to 9.3 points (FY25)**.

### 2.4 Same window, pre-tax (EBT) margin %

| FY | **TXN** | ADI | MCHP | NXPI | ON | STM |
|---|---|---|---|---|---|---|
| 2021 | 48.6 | 18.2 | 6.2 | 19.7 | 17.2 | 18.3 |
| 2022 | 50.1 | 25.8 | 21.7 | 25.5 | 28.4 | 27.8 |
| 2023 | 42.3 | 29.3 | 34.5 | 25.2 | 30.7 | 27.6 |
| 2024 | 34.9 | 18.9 | 31.0 | 24.6 | 25.9 | 14.2 |
| 2025 | **32.3** | 24.6 | 0.9 | 21.7 | 2.2 | 3.4 |

---
## 3. THE FULL COMPETITOR ROW: most recent full fiscal year

**Windows are NOT identical** and this is stated rather than smoothed: TXN/NXPI/ON/STM =
FY ended 31 Dec 2025; ADI = FY ended 1 Nov 2025; MCHP = FY ended 31 Mar 2026 (its most
recent full year, mapping to ~calendar 2025).

| Metric | **TXN** | ADI | MCHP | NXPI | ON | STM |
|---|---|---|---|---|---|---|
| FY end | 2025-12-31 | 2025-11-01 | 2026-03-31 | 2025-12-31 | 2025-12-31 | 2025-12-31 |
| **1. Revenue $M** | **17,682** | 11,020 | 4,713 | 12,269 | 5,995 | 11,800 |
| **2. Gross margin %** | **57.0** | 61.5 | 57.7 | 54.7 | 33.1 | 33.9 |
| **3. Operating margin %** | **34.1** | 26.6 | 10.4 | 24.8 | 1.4 | 1.5 |
| **4. Pre-tax (EBT) margin %** | **32.3** | 24.6 | 5.8 | 21.7 | 2.2 | 3.4 |
| **5. R&D % of revenue** | **11.8** | 16.0 | 23.0 | 19.2 | 9.7 | 17.3 |
| **6. Capex % of revenue** | **25.7** | 4.8 | 1.9 | 3.2 | 5.7 | 17.9 |
| **7. Capex / depreciation** | **2.37×** | 1.31× | 0.59× | 0.71× | 0.62× | 1.20× |
| **7b. Capex / D&A** | 2.37× | 0.89× | 0.13× | 0.48× | 0.50× | 1.14× |
| **8. ROE (ending equity)** | **30.7** | 6.7 | 3.6 | 20.1 | 1.6 | 0.9 |
| **8b. ROE (average equity)** | **30.1** | 6.6 | 3.4 | 21.0 | 1.5 | 0.9 |
| **9. Fabs?** | **owns fabs** | fab-lite/hybrid | owns fabs (hybrid) | **fab-lite** | owns fabs (hybrid) | owns fabs | 

Both ROE bases are given. **Average equity is the one to prefer** (it matches the flow to
the capital that produced it). TXN's ending and average are near-identical because equity
barely moved.

### 3.0.1 One-off charges inside FY2025: do not over-read the two collapses

ON and STM both show ~1.5% operating margins in FY2025. **Neither is a clean run-rate.**
Cross-checked to the filed statements:

- **STM** *(Consolidated Statements of Income, R3)*: an explicit line
  **"Impairment, restructuring charges and other related phase-out costs (376)"**, zero in
  both FY2024 and FY2023. Ex-that charge, STM operating income would be 551 on 11,800, i.e.
  **4.7%**, not 1.5%. Filed operating income is 175.
- **ON**: restructuring/impairment inside operating expense. Reconciled exactly from the
  filed statement (R5): gross profit 1,983.9 − R&D 583.6 − selling & marketing 255.9 −
  G&A 348.9 − intangible amortisation 44.4 = **751.1**, against filed operating income of
  **84.2**. The difference, **666.9**, is the restructuring line, and it ties to the
  disclosed components: **$496.0M non-cash impairment + $67.1M severance (≈2,400 employees)
  + $103.9M other exit costs = $667.0M.** Ex-those charges ON's operating margin would be
  **12.5%**, not 1.4%.
- **TXN** also carries **$117M restructuring** in FY2025 (150mm fab closures plus a goodwill
  impairment on custom ASIC). Ex-that, (6,023 + 117) / 17,682 = **34.7%**, against 34.1%
  as filed. Small.
- **MCHP** carries $39.7M special charges in FY2026.

The tables above use **as-filed** figures throughout, without adjustment, because that is
the standard. But the ranking of "who is structurally broken" should not be read off the
FY2025 operating-margin line alone. **TXN's lead over ON and STM is real but smaller than
the headline suggests; its lead over ADI and NXPI is unaffected by this.**

Capex/depreciation uses **depreciation of PP&E only** where a company tags it separately
(row 7), because that is the ratio that answers "are they building capacity faster than
they are consuming it". Row 7b uses total D&A as filed in the cash flow statement, which
for ADI and MCHP is dominated by acquisition intangible amortisation (ADI FY2025:
depreciation 407 vs intangible amortisation 1,592) and is **not** a capacity signal.
**Use row 7.**

### 3.1 Same nine metrics, FY2022 peak year: for direction

| Metric | **TXN** | ADI | MCHP | NXPI | ON | STM |
|---|---|---|---|---|---|---|
| FY end | 2022-12-31 | 2022-10-29 | 2022-03-31 | 2022-12-31 | 2022-12-31 | 2022-12-31 |
| **1. Revenue $M** | **20,028** | 12,014 | 6,821 | 13,205 | 8,326 | 16,128 |
| **2. Gross margin %** | **68.8** | 62.7 | 65.2 | 56.9 | 49.0 | 47.3 |
| **3. Operating margin %** | **50.6** | 27.3 | 27.1 | 28.8 | 28.3 | 27.5 |
| **4. Pre-tax (EBT) margin %** | **50.1** | 25.8 | 21.7 | 25.5 | 28.4 | 27.8 |
| **5. R&D % of revenue** | **8.3** | 14.2 | 14.5 | 16.3 | 7.2 | 11.8 |
| **6. Capex % of revenue** | **14.0** | 5.8 | 5.4 | 8.0 | 12.1 | 22.0 |
| **7. Capex / depreciation** | **3.02×** | 2.47× | 1.77× | 1.76× | 2.52× | 3.19× |
| **8. ROE (ending equity)** | **60.0** | 7.5 | 21.8 | 37.4 | 30.7 | 31.2 |
| **8b. ROE (average equity)** | **62.7** | 7.4 | 22.9 | 39.9 | 35.3 | 36.2 |

### 3.2 The direction, FY2022 → latest

**Label precision:** this table compares the FY2022 column to the latest column. It is
**not** peak-to-trough. FY2022 was the peak only for TXN, ON and STM. ADI, MCHP and NXPI
peaked in FY2023, so their FY2022→latest change understates their true decline. The
peak-to-trough gross-margin numbers are in §2.2 and they are the ones to quote.

| | TXN | ADI | MCHP | NXPI | ON | STM |
|---|---|---|---|---|---|---|
| Gross margin | **−11.8 pt** | −1.2 pt | −7.5 pt | **−2.2 pt** | −15.9 pt | −13.4 pt |
| Operating margin | **−16.5 pt** | −0.7 pt | −16.7 pt | **−4.0 pt** | −26.9 pt | −26.0 pt |
| Pre-tax margin | **−17.8 pt** | −1.2 pt | −15.9 pt | −3.8 pt | −26.2 pt | −24.4 pt |
| R&D % rev | **+3.5 pt** | +1.8 pt | +8.5 pt | +2.9 pt | +2.5 pt | +5.5 pt |
| Capex % rev | **+11.7 pt** | −1.0 pt | −3.5 pt | −4.8 pt | −6.4 pt | −4.1 pt |
| Capex/dep | 3.02 → **2.37×** | 2.47 → 1.31× | 1.77 → 0.59× | 1.76 → **0.71×** | 2.52 → 0.62× | 3.19 → 1.20× |
| ROE (avg) | **62.7 → 30.1** | 7.4 → 6.6 | 22.9 → 3.4 | 39.9 → 21.0 | 35.3 → 1.5 | 36.2 → 0.9 |

**TXN is the only company in the row still spending above 2× depreciation.** Every peer
cut capex below or near replacement level (ADI 1.31×, STM 1.20×, NXPI 0.71×, ON 0.62×,
MCHP 0.59×). TXN went the other way and *raised* capex intensity from 14.0% to 25.7% of
revenue while revenue fell.

This is the single most important structural fact in the row, and it cuts both ways:
- **The bull reading:** TXN is buying 300mm capacity at the bottom of the cycle while
  every competitor starves theirs. Capacity bought now earns for 20+ years.
- **The bear reading:** the depreciation from that capex is already in COGS and is why
  TXN's gross margin fell 11.8 points while the fab-lite competitor's fell 2.2. TXN
  depreciation went 925 (FY22) → **1,918 (FY25), +107%**, on revenue down 11.7%. There is
  more of it coming: capex of 4,550 is still 2.37× depreciation, so the depreciation base
  keeps compounding.
- **Q4/Q6 hook:** the disclosed judgment on *maintenance* capex is unavoidable here. Total
  capex 4,550 is emphatically **not** maintenance capex. Depreciation 1,918 is a floor, not
  the answer. Buffett's (c) "must be a guess" applies with full force.


## 4. FABS: from the filings' own words (verbatim)

**TXN: owns fabs. The most vertically integrated name in the row.**
> "We expect to maintain sufficient internal manufacturing capacity to meet the majority
> of our production needs... **In 2025, we sourced the majority of our wafer fabrication,
> as well as assembly and test, internally.** To supplement our internal manufacturing
> capacity, we selectively use the capacity of outside suppliers, commonly known as
> foundries and subcontractors."

> "Except as otherwise indicated, **we own these facilities**." *(Item 2, Properties)*

**ADI: fab-lite. MORE THAN HALF OUTSOURCED, in its own words.**
> "We currently source **more than half of our wafer requirements annually from
> third-party wafer fabrication foundries**, such as Taiwan Semiconductor Manufacturing
> Company (TSMC) and others, and the remainder is sourced internally."

ADI's own fabs: Wilmington MA, Camas WA, Beaverton OR, Limerick Ireland.

**MCHP: hybrid, and now majority-outsourced. It states both sides.**
> "By **owning wafer fabrication facilities** and our assembly and test operations... we
> have been able to achieve and maintain high production yields... This control also
> allows us to capture a portion of the wafer manufacturing, assembly and testing profit
> margin."

> "In fiscal 2026, approximately **35% of our sales came from products produced at our own
> wafer fabrication facilities**... We augment our internal manufacturing capabilities by
> outsourcing a significant portion of our wafer production requirements to third-party
> wafer foundries... In fiscal 2026, approximately **65% of our sales came from products
> that were produced at outside wafer foundries.**"

MCHP closed Fab 2 (Tempe, Arizona) in May 2025, and it was held for sale at 31 Mar 2026.

**NXPI: fab-lite, and it has a name for it: the "hybrid manufacturing model".**
> "We employ a **hybrid manufacturing model** where we manufacture semiconductors through a
> combination of wholly owned manufacturing facilities, a manufacturing facility operated
> jointly with another semiconductor company and third-party foundries and assembly and
> test subcontractors."

> "In less favorable industry environments... we are generally faced with a decline in the
> utilization rates of our manufacturing facilities... **the fixed costs associated with
> the full capacity continue to be incurred, resulting in lower gross profit.**"

That second quote is NXPI naming the exact mechanism that hit TXN's gross margin, and
NXPI structured itself to avoid it.

**ON: owns fabs (hybrid, with a consolidated JV).**
> "**All of our manufacturing facilities are fully owned and operated by us**, except our
> assembly and test operations facility located in Leshan, China, which is owned by
> Leshan-Phoenix Semiconductor Company Limited, a joint venture company in which we own
> 80% of the outstanding equity interests."

ON took a **$496.0 million non-cash impairment** in FY2025 "related to previous investments
in manufacturing equipment at certain manufacturing facilities pursuant to held-for-sale
accounting guidance", plus $67.1M severance for ~2,400 employees. This is what a failed
capacity bet looks like on the income statement, and it is the reason ON's FY2025 gross margin is
33.1% and operating margin 1.4%.

**STM: owns fabs, all of them.**
> "**We own all of our manufacturing facilities**, but certain facilities (Muar, Malaysia;
> Shenzhen, China; Kirkop, Malta; and Toa Payoh and Ang Mo Kio, Singapore) are built on
> land subject to long-term leases."

### 4.1 The fab spectrum, ranked

| | Company | Internal share | Direction |
|---|---|---|---|
| Most integrated | **TXN** | majority internal, rising | building 300mm hard |
| | **STM** | 100% owned fabs | reshaping/resizing footprint |
| | **ON** | ~all owned | shrinking, impairing |
| | **MCHP** | **35%** internal | shrinking, closed Fab 2 |
| | **ADI** | **<50%** internal | stable fab-lite |
| Most fab-lite | **NXPI** | hybrid, consolidating to 300mm **via JVs** | outsourcing the capex |

**The row's finding: the three most integrated names (TXN, STM, ON) took the three largest
gross-margin hits (−11.8, −13.4, −15.9 points). The two most fab-lite (ADI, NXPI) took the
two smallest (−1.2, −2.2 points).** Vertical integration was a liability in this downcycle,
not an asset. Whether it becomes an asset in the next upcycle is the actual Q2/Q4 question,
and it is not answerable from these filings.

---
## 5. 300mm vs 200mm: and Chinese analog competition

### 5.1 Wafer-size disclosure, counted and quoted

Mentions in each company's most recent annual filing:

| | TXN | ADI | MCHP | NXPI | ON | STM |
|---|---|---|---|---|---|---|
| "300mm/300 millimeter" | 6 | **0** | 1 | 3 | **0** | 10 |
| "200mm/200 millimeter" | 1 | **0** | 1 | 0 | **0** | 24 |

**ADI and ON do not disclose wafer size at all in their FY2025 10-Ks.** That is a real
disclosure gap, and it is recorded as such rather than filled from memory or an
aggregator. **UNRESEARCHED** against these documents; the resolving document would be an
investor-day deck or fab-level press release, which is not on the filing shelf.

**TXN: the 300mm cost claim, verbatim. This is the moat statement.**
> "We have focused on creating a competitive manufacturing structural cost advantage by
> investing in our 300mm capacity, as **an unpackaged chip built on a 300mm wafer costs
> about 40% less than an unpackaged chip built on a 200mm wafer.**"

> "In 2025, we continued qualifying and ramping production at our **newest 300mm wafer fabs
> in Richardson and Sherman, Texas, and Lehi, Utah.** These fabs are well positioned to
> support customer demand, external foundry transfers and internal transfers from our
> **legacy 150mm facilities**."

TXN is also closing 150mm: restructuring charges of $117M in FY2025 included "the planned
closures of our **two remaining factories with 150mm production**". And it holds a CHIPS Act
award of **up to $1.6 billion** for the three 300mm fabs, with **$3.35 billion of CHIPS Act
receivables recognised** at 31 Dec 2025, plus a **35% investment tax credit** on qualifying
assets placed in service after 31 Dec 2025.

*The 40% figure is TXN's own claim in its own filing. It is a management assertion, not an
audited number. Record it as such.*

**NXPI: consolidating to 300mm, but paying for it with equity stakes, not capex.**
> "As part of executing our hybrid manufacturing model, **we have initiated the
> consolidation of our internal wafer fabs to 300 millimeter factories.** We believe this
> will enable economic and manufacturing efficiencies in the future."

> "European Semiconductor Manufacturing Company (ESMC) GmbH will build and operate a new
> 300mm semiconductor wafer manufacturing facility in Dresden, Germany. **ESMC is 70% owned
> by TSMC, with Bosch, Infineon, and NXP each owning 10%. NXP is entitled to 10% of the fab
> facility capacity.** Initial production... targeted to begin in 2028."

> "VisionPower Semiconductor Manufacturing Company Pte. Ltd. (VSMC) will build and operate
> a new 300mm semiconductor wafer manufacturing facility in Singapore. **VSMC is 60% owned
> by Vanguard International Semiconductor Corporation and 40% owned by NXP. NXP is entitled
> to 40% of the fab facility capacity.** Initial production... targeted to begin in 2027."

**This is why NXPI's capex is only 3.2% of revenue while it still gets 300mm capacity.**
The spending is off the capex line and in equity commitments: €500M into ESMC (of which
$183M invested), **$969M more committed to VSMC through 2027**, plus $345M for capacity
infrastructure. A Q4 owner-earnings build for NXPI must add these back; the capex line
understates NXPI's true capital intensity. Flagged as a comparability defect in the row.

**MCHP: outsources 100% of its 300mm.**
> "We augment our internal manufacturing capabilities by outsourcing a significant portion
> of our wafer production requirements to third-party wafer foundries, **including all of
> our 300mm wafer requirements and some of our 200mm and 150mm specialty process
> technologies.**"

MCHP's own fabs: Fab 4 (Gresham, Oregon) "currently produces **8-inch wafers**" (= 200mm),
Fab 5 (Colorado Springs) partly **6-inch** (150mm), expansion at both **paused through
fiscal 2027**.

**STM: the most detailed wafer-size disclosure of the six.** Fab-by-fab, from Item 4:
- Agrate, Italy: Fab 1 **200mm**; Fab 2 **200mm**; **Fab 3 300mm** (analog CMOS, BCD)
  *(Fab 3 shared with Tower Semiconductor)*
- Crolles, France: Fab 1 **200mm**; **Fab 2 300mm** (FD-SOI advanced CMOS)
- Ang Mo Kio, Singapore: Fab 1 **150mm**; Fab 2 **200mm**
- Catania, Italy: Fab 1 **150mm** SiC; Fab 2 **200mm**; Site 2 **200mm SiC substrate**
- Rousset / Tours, France: **200mm** and **150mm**

> "As of December 31, 2025, our front-end facilities had a total maximum capacity of
> approximately **140,000 wafer starts per week (200mm equivalent)**."

> "The joint **300mm** semiconductor manufacturing facility with GlobalFoundries Inc in
> Crolles, France... has a projected cost of **€7.5 billion** of capital expenditure,
> maintenance and ancillary costs and will benefit from financial support of up to roughly
> **€2.9 billion from the State of France** in line with the European Chips Act."

### 5.2 Chinese competition: who says it, who does not

Occurrences of "China/Chinese" within 300 characters of "compet" in each filing:

| | TXN | ADI | MCHP | NXPI | ON | STM |
|---|---|---|---|---|---|---|
| China-near-competition mentions | 1 | 1 | **19** | **0** | 2* | 5 |

\* ON's two are incidental (design-office locations, collective bargaining). **ON does not
name Chinese competition as a competitive risk anywhere in its FY2025 10-K.**

**TXN: the one mention. It is in the competition risk factor.**
> "We face competition from large competitors and from small competitors serving niche
> markets, and also from emerging companies, **particularly in Asia**, that sell products
> into the same markets in which we operate. **For example, we may face increased
> competition as a result of China actively promoting and reshaping its domestic
> semiconductor industry through policy changes and investment, which could prevent us from
> competing effectively.** Certain competitors possess sufficient financial, technical and
> management resources and **utilize available incentives offered by various countries and
> government entities** to develop and market products that may compete favorably against
> our products."

TXN's exposure, from the same filing:
> "Revenue from **end customers headquartered in China represented about 20% of our revenue
> in 2025**, while revenue from **products shipped into China represented about 50% of our
> revenue in 2025**."

The segment note gives China revenue as **$3,781M, 21% of total** (FY2025), up from $3,012M
/19% (FY2024). TXN also holds **$674M of PP&E in China** (Chengdu, Shanghai).

*The 50%-shipped-into-China figure is the one that matters and it is easy to miss. Twenty
percent is where the customer is headquartered; fifty percent is where the product
physically goes. The tariff and localisation exposure runs on the larger number.*

**MCHP: by far the most explicit, and the most alarmed. 19 mentions.**
> "Having a strong position in the Chinese market is a key component of our global growth
> strategy. Although our sales in the Chinese market have been strong in the past,
> **competition in China is intense. Throughout fiscal 2024, fiscal 2025 and fiscal 2026,
> changes in the Chinese market adversely impacted our sales volumes in China.**"

> "We also compete with a number of companies that we believe have **copied, cloned, pirated
> or reverse engineered our proprietary product lines in such countries as China and
> Taiwan.**"

> "If China further restricts exports or pressures other countries to do so, our suppliers
> may face shortages, longer lead times, or increased costs. Limited access to these
> materials could impair our ability to manufacture certain products, increase our
> production costs, or **reduce our competitiveness relative to manufacturers with
> alternative supply sources.**"

**STM: names the policy mechanism.**
> "**We could face increased competition as a result of China's programs to promote a
> domestic semiconductor industry and supply chains** (such as its 5-year plans, the China
> Standards 2035 campaign and related large scale national and local public funding
> schemes)."

STM's answer is to build inside China. From its executive-compensation criteria:
> "Execution of the **China-for-China operating model** to support domestic China growth
> notably with **localized scalable manufacturing networks**."

And the JV, verbatim:
> "On June 7, 2023, the Company and Sanan Optoelectronics jointly created SANAN,
> STMicroelectronics Co. Ltd. ('Sanan ST JV'), for **high-volume 200mm SiC device
> manufacturing in China.** This joint venture will make SiC devices exclusively for us,
> using our proprietary SiC manufacturing process technology, and will **serve as a
> dedicated foundry to support the demand of our Chinese customers.** The total amount for
> the full buildout... is expected to be about **$3.2 billion**."

**ADI: names it as indigenisation, not head-on competition.**
> "These restrictions... may cause them to amass large inventories of our products, replace
> our products with products from another supplier that is not subject to the export
> restrictions or **focus on building indigenous semiconductor capacity to reduce reliance
> on U.S. suppliers.**"

> "Our success may be adversely affected by China's continuously evolving policies, laws and
> regulations, including those relating to... **indigenous innovation, the promotion of a
> domestic semiconductor industry**, intellectual property rights and enforcement."

**NXPI: SILENT. Zero mentions of Chinese competition.** NXPI's competition risk factor is
generic ("The semiconductor industry is highly competitive and characterized by constant and
rapid technological change, short product lifecycles, significant price erosion") and never
names China as a competitive source.

**ON: SILENT on Chinese competition too.** Its competition disclosure is entirely generic:
> "We face significant competition within each of our product lines from major global
> semiconductor companies as well as smaller companies focused on specific market niches."

### 5.3 What the China row actually tells you

The disclosure gradient is **not** a ranking of real exposure; it is a ranking of
management candour and of legal exposure to US export rules. MCHP (US filer, 18% China
sales) and TXN (US filer, 50% shipped into China) disclose most. NXPI (Dutch) and ON say
nothing. **A silent risk factor is not an absent risk.** Do not read NXPI's silence as
safety; read it as an unresearched question with a nameable resolving document (NXPI's
own investor day, or its Chinese revenue disclosure by end-market).

**For the TXN thesis, the honest statement is:** TXN names Chinese state-backed analog
competition as a risk in one sentence, at the level of "may face increased competition."
The filing does **not** quantify it, does **not** name a competitor, and does **not**
disclose share loss. Anyone who wants to claim Chinese analog competition is or is not
eroding TXN's franchise cannot get that from the 10-K. It is **UNRESEARCHED**, and the
resolving documents exist (customs data, SIA/WSTS share data, Chinese listed-company
filings for e.g. SG Micro, 3Peak, Silergy). That is a real research task, not a closed
question.

---
## 5.4 WHAT THE ROW SAYS ABOUT Q2: read before using any of it

A moat is a relative claim. Here is what the relative evidence supports and what it does not.

**Supports a franchise claim:**
1. TXN leads the row on **operating margin in every single year** of the window, FY2021
   through FY2025: 34.1% at the trough against ADI 26.6, NXPI 24.8, MCHP 10.4, ON 1.4,
   STM 1.5. Nobody else is close at the bottom of the cycle.
2. TXN leads on **ROE by a wide margin**: 30.1% (avg) vs NXPI 21.0, ADI 6.6, MCHP 3.4,
   ON 1.5, STM 0.9. And it does so on a balance sheet carrying real debt, not leverage
   games; equity is $16.3bn on $17.7bn of revenue.
3. TXN's **R&D intensity is 11.8%, second-lowest in the row** (only ON is lower at 9.7%,
   and ON is the one that broke), while its margins are the highest. Against the names
   that are actually healthy it spends far less: ADI 16.0%, NXPI 19.2%, MCHP 23.0%,
   STM 17.3%. It is not buying its position with R&D spend. That is the analog catalogue
   effect, and it is real.
4. TXN was **profitable through the worst of the cycle** while STM and ON went to roughly
   zero operating profit and MCHP went negative on net income (FY2025: −$0.5M).

**Cuts against a franchise claim, and must not be suppressed:**
1. **Gross margin did not hold.** −11.8 points, second-worst in the row. The premise of
   the question ("did gross margin hold through the downcycle") is answered **no** for TXN
   and **yes** for NXPI and ADI. This is the opposite of the comfortable answer.
2. **The gross-margin lead over ADI is gone.** FY2022: TXN 68.8 vs ADI 62.7 (+6.1). FY2025:
   TXN 57.0 vs ADI 61.5 (**−4.5**). On gross margin alone, ADI now out-earns TXN per dollar
   of revenue. TXN's operating-margin lead survives only because ADI carries $1.59bn of
   acquisition intangible amortisation that TXN does not.
3. **The capex is not yet vindicated.** Capex/depreciation 2.37× against a peer group at
   0.59-1.31×. Depreciation has already **doubled** (925 → 1,918) and will keep rising.
   The 40%-cost-advantage claim is management's, unaudited, and the P&L has not yet shown
   it: FY2025 incremental gross margin was 48.5%, *below* the average.
4. **ROE has halved**, 62.7% → 30.1%.

**The one question this row cannot answer:** whether TXN's 300mm build is a Buffett-style
"we are buying a toll bridge while everyone else is scared" or a Munger-style "the fixed
cost is the trap." Both readings fit every number above. It resolves on 2027-2030
utilisation, which no filing discloses. That is an **UNKNOWABLE at this date**, not an
UNRESEARCHED one; no existing document settles it.

**A note on the analyst, per operator rule 9.** The gross-margin finding here is the
disconfirming one. It was hunted for deliberately because the vertically-integrated-moat
story is the attractive hypothesis. *"You must not fool yourself, and you're the easiest
person to fool"* **[E3-41]**. The finding stands as found.

---
## 6. SOURCES: accession numbers

| Company | Form | Period | Filed | Accession | Primary doc |
|---|---|---|---|---|---|
| TXN | 10-K | 2025-12-31 | 2026-02-06 | 0000097476-26-000059 | txn-20251231.htm |
| TXN | 10-K | 2022-12-31 | 2023-02-03 | 0000097476-23-000007 | txn-20221231.htm |
| ADI | 10-K | 2025-11-01 | 2025-11-25 | 0000006281-25-000153 | adi-20251101.htm |
| ADI | 10-K | 2022-10-29 | 2022-11-22 | 0000006281-22-000250 | adi-20221029.htm |
| MCHP | 10-K | 2026-03-31 | 2026-05-21 | 0000827054-26-000016 | mchp-20260331.htm |
| MCHP | 10-K | 2025-03-31 | 2025-05-23 | 0000827054-25-000077 | mchp-20250331.htm |
| MCHP | 10-K | 2022-03-31 | 2022-05-20 | 0000827054-22-000094 | mchp-20220331.htm |
| NXPI | 10-K | 2025-12-31 | 2026-02-19 | 0001413447-26-000008 | nxpi-20251231.htm |
| NXPI | 10-K | 2022-12-31 | 2023-03-01 | 0001413447-23-000006 | nxpi-20221231.htm |
| ON | 10-K | 2025-12-31 | 2026-02-09 | 0001097864-26-000006 | on-20251231.htm |
| ON | 10-K | 2022-12-31 | 2023-02-06 | 0001628280-23-002350 | on-20221231.htm |
| STM | 20-F | 2025-12-31 | 2026-02-26 | 0000932787-26-000009 | stm-20251231.htm |
| STM | 20-F | 2024-12-31 | 2025-02-27 | 0000932787-25-000006 | stm-20241231.htm |

### 6.1 Operator rule 4: the filing got read, cross-check record

XBRL was used for transcription and screening only. For every company in the row, at least
one figure was cross-checked against the rendered filed statement (the `R*.htm` Financial
Report exhibits inside each accession), not just the tagged fact:

| Company | Statement read | Figures verified against it |
|---|---|---|
| TXN | R3 *Consolidated Statements of Income* | Revenue 17,682; Operating profit 6,023; Income before income taxes 5,710; **full income statement transcribed in §1.1** |
| NXPI | R3 *Consolidated Statements of Operations* | Revenue 12,269; Cost of revenue (5,553); Gross profit 6,716 |
| ADI | R3 *Consolidated Statements of Income* | Revenue 11,019,707 (thousands); Cost of sales 4,246,229; Gross margin 6,773,478 |
| ON | R5 *Consolidated Statements of Operations* | Revenue 5,995.4; Gross profit 1,983.9; R&D 583.6; **and the full opex bridge to operating income 84.2 reconciled in §3.0.1** |
| STM | R3 *Consolidated Statements of Income* | Net revenues 11,800; Gross profit 3,999; the **(376)** impairment line; Operating income 175 |
| STM | R9 *Consolidated Statements of Cash Flows* | "Payment for purchase of tangible assets" 2,111 / 3,088 / 4,439 |
| MCHP | R5 *Consolidated Statements of Operations* | Net sales 4,713.1; Cost of sales 1,992.0; Gross profit 2,721.1; R&D 1,085.9 |

**All six SEC names cross-checked against the rendered filed statement. No gap remains on
this row.**

The **FY2022 peak-year column** was separately cross-checked against the FY2022 filings
themselves (not restated later figures), which also validates the FY2021 and FY2020 entries
in the §2 series since each statement carries three years:

| Company | Statement read | Figures verified |
|---|---|---|
| TXN | accession 0000097476-23-000007, R3 | FY2022 revenue 20,028 / COR 6,257 / gross profit 13,771; FY2021 revenue 18,344 / COR 5,968; FY2020 revenue 14,461 |
| NXPI | accession 0001413447-23-000006, R3 | FY2022 revenue 13,205 / cost of revenue (5,688) / gross profit 7,517; FY2021 revenue 11,063; FY2020 revenue 8,612 |
| MCHP | accession 0000827054-22-000094, R5 | FY2022 net sales 6,820.9 / cost of sales 2,371.3; FY2021 5,438.4; FY2020 5,274.2 |
| ADI | accession 0000006281-22-000250, R3 | FY2022 revenue 12,013,953 (thousands); FY2021 7,318,286; FY2020 5,603,056 |
| ON | accession 0001628280-23-002350, R5 | FY2022 revenue 8,326.2 / cost of revenue 4,249.0; FY2021 6,739.8; FY2020 5,255.0 |
| STM | accession 0001564590-23-002312, R2 | FY2022 net revenues 16,128 / cost of sales (8,493) / gross profit 7,635; FY2021 12,761; FY2020 10,219 |

**Both columns of the row, for all six SEC names, now rest on a read filed statement rather
than on tagged data alone.** Note the archive path for ON's and STM's FY2022 filings uses
the subject-company CIK (1097864, 932787), not the filing-agent CIK in the accession
number; the filing-agent path returns 404.

STM capex is taken from the filed *Consolidated Statements of Cash Flows* line
"Payment for purchase of tangible assets" (FY2025 2,111; FY2024 3,088; FY2023 4,439;
FY2022 3,549). STM does not tag it to `PaymentsToAcquirePropertyPlantAndEquipment` in
recent years, so the statement was read rather than the tag taken.

---
## 7. NON-SEC NAMES: IR rung

### 7.0 Rung declaration, stated plainly

**These two names sit one rung BELOW everything above.** Infineon and Renesas are not SEC
registrants. Every figure below comes from the **company's own IR-published annual report**
in English, read directly. **No aggregator was used for any number.** No press release or
quarterly PDF was used. Where a figure does not exist in a company-published document it is
recorded as **NOT FOUND IN IR DOCUMENT** and left empty rather than estimated.

Documents read:

| Company | Document | Publisher | Period |
|---|---|---|---|
| Infineon | **Annual Report 2025**, published 30 Nov 2025 | Infineon IR | FY ended 30 Sep 2025 |
| Infineon | **Annual Report 2022**, published 28 Nov 2022 | Infineon IR | FY ended 30 Sep 2022 |
| Renesas | **Financial Report 2025** | Renesas IR | FY ended 31 Dec 2025 |
| Renesas | **Financial Report 2022** | Renesas IR | FY ended 31 Dec 2022 |
| Renesas | **Annual Securities Report 2025 / 2022 (Excerpt)** | Renesas IR | same |

### 7.1 Comparability caveats, stated before the numbers

1. **Different accounting standard.** Both report **IFRS**, not US GAAP. Gross profit,
   operating profit and equity are not constructed identically to the six above.
2. **Different currency.** Infineon reports in **EUR**, Renesas in **JPY**. Figures below
   are in the **reporting currency, unconverted**, deliberately: converting at a spot or
   average rate would import an FX judgment into a margin comparison that does not need one.
   **Margins and ratios are currency-invariant and those are what the row uses.**
3. **Different fiscal calendar.** Infineon closes **30 September**. Renesas closes 31 Dec.
4. **Infineon restated its cost split.** From 1 Oct 2024 it moved certain expenses from COGS
   into R&D, restating FY2024 but **not** FY2022. Verbatim:
   > "In order to provide more meaningful information, the accounting policy was changed as
   > of 1 October 2024 with regard to the allocation of certain expenses. This led to a
   > **reclassification of expenses from cost of goods sold to research and development
   > expenses.** The previous year's figures have been adjusted accordingly."

   **So Infineon's FY2022→FY2025 gross-margin and R&D movements are NOT like-for-like.**
   Part of the 3.9-point gross-margin decline is reclassification, not deterioration. The
   filing does not quantify how much. **UNRESEARCHED**, and the resolving document (a
   restated FY2022) does not exist, which makes it **UNKNOWABLE** on this evidence.
5. **Renesas puts R&D inside SG&A**, not on the income-statement face. Verbatim:
   > "Research and development expenses are included in selling, general and administrative
   > expenses."

   R&D below is taken from the Note 27 SG&A components table. **Renesas' R&D still sits
   BELOW gross profit**, as it does for TXN, so its gross margin remains comparable in
   construction to TXN's.

### 7.2 The nine metrics, IR-sourced

**INFINEON TECHNOLOGIES AG** (IFRS, EUR millions)

| Metric | FY2025 (to 30 Sep 25) | FY2022 (to 30 Sep 22) |
|---|---|---|
| **1. Revenue** | **€14,662** | **€14,218** |
| **2. Gross margin %** | **39.2** | **43.1** |
| **3. Operating margin %** (filed line: "Operating profit" 1,515 / 2,845) | **10.3** | **20.0** |
| **4. Pre-tax margin %** (1,375 / 2,723) | **9.4** | **19.2** |
| **5. R&D % of revenue** (2,227 / 1,798) | **15.2** | **12.6** |
| **6. Capex % of revenue** (PP&E only: 1,800 / 2,053) | **12.3** | **14.4** |
| 6b. Capex incl. intangibles % | 14.3 | 16.2 |
| **7. Capex / D&A** (D&A combined 1,917 / 1,664) | **0.94×** | **1.23×** |
| 7b. Capex / depreciation only | **NOT SEPARATELY DISCLOSED** | **NOT SEPARATELY DISCLOSED** |
| **8. ROE, ending total equity** (1,015 / 17,051; 2,179 / 14,944) | **6.0** | **14.6** |
| **8b. ROE, average total equity** | **5.9** | **16.5** |
| **9. Fabs** | **owns fabs, selectively (hybrid IDM)** | same |

*Capex cross-check:* Infineon's own "Investments" key figure equals PP&E + intangibles
exactly in both years (2,094 FY2025; 2,310 FY2022), confirming the cash-flow lines were read
correctly. **Infineon does not split depreciation from amortisation**, so row 7 of the main
table (capex / depreciation-only) **cannot be computed for Infineon**. Recorded as a gap.

**RENESAS ELECTRONICS CORPORATION** (IFRS, JPY millions)

| Metric | FY2025 (CY2025) | FY2022 (CY2022) |
|---|---|---|
| **1. Revenue** | **¥1,321,212** | **¥1,500,853** |
| **2. Gross margin %** | **57.1** | **56.9** |
| **3. Operating margin %** (201,166 / 424,170) | **15.2** | **28.3** |
| **4. Pre-tax margin %** ((30,275) / 362,299) | **(2.3)** | **24.1** |
| **5. R&D % of revenue** (238,056 / 205,963, inside SG&A) | **18.0** | **13.7** |
| **6. Capex % of revenue** (PP&E only: 89,151 / 66,135) | **6.7** | **4.4** |
| 6b. Capex incl. intangibles % | 10.1 | 5.9 |
| **7. Capex / depreciation only** (dep 47,156 / 58,208) | **1.89×** | **1.14×** |
| 7b. Capex / total D&A (188,597 / 186,032) | 0.47× | 0.36× |
| **8. ROE, ending equity attributable to owners** | **(2.1)** | **16.7** |
| **8b. ROE, average equity attributable** | **(2.1)** | **19.1** |
| **9. Fabs** | **owns fabs, plus foundry use** | same |

*Renesas FY2025 net loss is BELOW the operating line.* Operating profit was ¥201.2bn
(15.2%); the pre-tax loss comes from **¥245,641M of finance costs**. Operating cash flow
**rose** to ¥452,857M from ¥340,484M. This is a financing/non-cash event, not an operating
collapse, and it must not be read as one.

*A D&A reconciliation gap is disclosed rather than smoothed:* depreciation 47,156 +
amortisation 138,961 = 186,117 against ¥188,597M on the cash flow statement, a ¥2,480M
difference the company does not reconcile (FY2022: ¥2,943M). Reported as found.

### 7.3 Fab ownership, verbatim

**Infineon: hybrid IDM, and it states the rule it uses to decide.** This is the clearest
articulation of the make-or-buy decision in the entire eight-company set:
> "In areas in which we create added value for our customers and differentiation for
> Infineon in manufacturing, **we rely on in-house manufacturing.** We make products in our
> own fabs when doing so means that our customers benefit from lower cost, higher
> performance or improved availability. **This is the case, for example, with power
> semiconductors and sensors as well as with analog/mixed-signal technologies.** However,
> where manufacturing in our own fabs offers no additional customer benefit or opportunity
> to differentiate ourselves from the competition, **we work together with contract
> manufacturers.** This is predominantly the case for highly integrated digital products
> such as microcontrollers, connectivity components and security ICs, where the
> differentiation arises mainly from the design and the software."

**Renesas: owns fabs and also uses foundries.** The term "fab-lite" does **not appear** in
any Renesas IR document read.
> "The manufacturing functions are handled mainly by domestic and overseas production
> subsidiaries, but **we also utilize foundries and other external production
> subcontractors as needed.**"

> "the Group **owns key facilities and equipment** in areas where earthquakes occur at a
> frequency higher than the global average"

Owned fabs itemised: **Naka Factory** (Ibaraki, ¥61,825M book value), **Kawashiri Factory**
(Kumamoto, ¥31,408M), Musashi (Tokyo, R&D, ¥30,976M).

**Renesas states a capex policy TXN does not:**
> "The Group aims to **control capital expenditures at approximately 5% of revenue** in the
> medium- to long-term while maintaining an appropriate level relative to revenue."

Set that against TXN at **25.7%**. The two companies have made opposite capital decisions
and both have said so in writing.

### 7.4 300mm vs 200mm, verbatim

**Infineon has the strongest 300mm claim of any company in the set, TXN included.** It is
the direct competitor claim to TXN's "40% less" statement:
> "Our **300-millimeter thin wafer manufacturing technology for power semiconductors** is a
> clear indication of the value of differentiating manufacturing in our own fabs. **As
> pioneers of this technology**, the level of production we have now reached has allowed us
> to achieve significant economies of scale. **Compared with manufacturing on
> 200-millimeter wafers, we benefit from significantly lower costs and lower capital
> investment. This has enabled us to maintain our lead.** With the factory at the Villach
> site (Austria), together with our 300-millimeter manufacturing facility in Dresden
> (Germany), we have established a closely coordinated manufacturing network across the two
> sites. In line with our **'One Virtual Fab'** concept, we are using the same processes,
> equipment, and automation and digitalization concepts in Villach and in Dresden."

> "We are also expanding our site in Dresden as planned, to include **an additional
> 300-millimeter module for analog/mixed-signal products** as well as power semiconductors."

> "In autumn 2024, we were **the first company worldwide to announce the rollout of
> 300-millimeter in-house manufacturing of GaN-based semiconductors.**"

Infineon **sold its 200mm Austin fab to SkyWater on 30 June 2025**, taking €149M of
impairment losses on the sale.

**Renesas: the 300mm disclosure has been WITHDRAWN.** Present in FY2022, absent in FY2025.
FY2022, verbatim:
> "the utilization rate of the Group's front-end production factories during this Business
> Period was **63% for the 150mm wafer production line, 93% for the 200mm wafer production
> line, and 80% for the 300mm wafer production line**, an average of 86% for all factories."

> "we aim to **restart the Kofu Factory as a 300mm wafer production line with a target start
> in 2024**"

**Neither the Financial Report 2025 nor the Annual Securities Report 2025 contains any
300mm/200mm wafer-size disclosure, and the wafer-line utilisation table has been dropped.**
Recorded as **NOT FOUND IN IR DOCUMENT** for FY2025. A company that discloses fab
utilisation in a good year and stops in a bad one has told you something, but not something
you can cite as a number.

### 7.5 Chinese competition, verbatim

**Infineon names it, and names the specific mechanism.** Risk section, "Risks arising from
increased market competition and commoditization of products":
> "The spread of new technological developments in a global market also results in greater
> replaceability of products. Due to the resulting price competition, we may be unable to
> achieve our long-term strategic goals of gaining and/or maintaining market share and of
> product pricing. Moreover, accelerating M&A activities within the semiconductor industry
> or **government subsidies restricted to specific regions** could result in even tougher
> competition. Potential benefits for competitors include improved cost structures and
> preferential customer access. **There is also the risk that an increased volume of
> previously imported semiconductors will be manufactured in China and that a greater volume
> of those made in that country will be exported.** Overall, this situation could have an
> adverse impact on Infineon's financial condition, liquidity and results of operations."

That last sentence is the sharpest statement of the Chinese-analog-substitution risk in the
entire eight-company set. It is more specific than TXN's.

**Renesas: NOT FOUND IN IR DOCUMENT.** Its competition risk factor is entirely
country-agnostic. Every occurrence of "China" across the FY2025 documents is a subsidiary
name, a revenue-geography heading, or a corporate-history entry. **"Chinese" appears zero
times.** The filed competition risk, in full:
> "The semiconductor industry is extremely competitive, and the Group is exposed to fierce
> competition from competitors around the world in areas such as product performance,
> structure, pricing and quality... **fierce market competition has subjected the products
> of the Group to sharp downward pressure on prices**, for which measures to improve
> profitability, such as price negotiations and efforts at cost price reduction, have been
> unable to fully compensate. This raises the possibility of a **worsening of the Group's
> gross margin.**"

*(Transcription note per PRIME RULE 1: the Renesas English translation contains the
artefact "and others. In recent years and there is a possibility that such actions will be
taken in the future as well." It is reproduced as filed elsewhere in the source and is
flagged here rather than smoothed.)*

### 7.6 The eight-company gross-margin table, complete

This is the central comparison with the IR-rung names added. **Rung is marked on every row.**

| Company | Rung | Standard | GM at FY2022 | GM latest | **Change** |
|---|---|---|---|---|---|
| **Renesas** | IR | IFRS | 56.9 | **57.1** | **+0.2 pt** |
| **ADI** | SEC | US GAAP | 62.7 | 61.5 | **−1.2 pt** |
| **NXPI** | SEC | US GAAP | 56.9 | 54.7 | **−2.2 pt** |
| **Infineon** | IR | IFRS | 43.1 | 39.2 | **−3.9 pt** \* |
| **MCHP** | SEC | US GAAP | 65.2 | 57.7 | −7.5 pt |
| **TXN** | SEC | US GAAP | **68.8** | **57.0** | **−11.8 pt** |
| **STM** | SEC | US GAAP | 47.3 | 33.9 | −13.4 pt |
| **ON** | SEC | US GAAP | 49.0 | 33.1 | −15.9 pt |

\* Infineon's change is contaminated by the COGS→R&D reclassification described in §7.1(4)
and is **not** a clean like-for-like. Its true operating decline is smaller than −3.9 pt.

**The finding survives the extension and gets stronger.** Sorted by gross-margin defence,
TXN is **sixth of eight**. The two names that defended gross margin best are Renesas (+0.2)
and ADI (−1.2). **Renesas defended a 57% gross margin, the same level TXN now sits at,
while cutting capex to a stated ~5%-of-revenue policy** and taking a −12.0% revenue decline.
TXN spent 25.7% of revenue on capex and lost 11.8 points of gross margin over the same span.

**The honest reading:** on the evidence of this row, high capital intensity did not protect
gross margin through the 2023-2025 analog downcycle; it consumed it. Whether that reverses
when the 300mm base is fully loaded is the open question, and no document in this file
answers it.

---
## 8. WHAT REMAINS OPEN

| Question | Verdict | Resolving document, if any |
|---|---|---|
| ADI and ON wafer-size mix | **UNRESEARCHED** | investor-day decks, fab press releases (off the filing shelf) |
| Infineon depreciation vs amortisation split | **UNRESEARCHED** | none published; combined schedule only |
| Infineon FY2022 restated on the FY2025 cost basis | **UNKNOWABLE** | company did not restate FY2022 |
| Renesas FY2025 wafer-line utilisation / 300mm | **UNRESEARCHED** | disclosure withdrawn after FY2022 |
| Is Chinese analog competition actually taking TXN share? | **UNRESEARCHED** | WSTS/SIA share data; Chinese listed filings (SG Micro, 3Peak, Silergy); customs data |
| Does TXN's 300mm build earn its cost of capital? | **UNKNOWABLE at this date** | resolves on 2027-2030 utilisation; no document exists yet |
| TXN maintenance capex vs total capex | **must be a DISCLOSED JUDGMENT** | no filing gives it; depreciation 1,918 is a floor, not the answer |

**Gate status: this file is Q2 evidence only. No Q1-Q4 verdict is recorded here, and no Q5
computation may proceed from it.**
