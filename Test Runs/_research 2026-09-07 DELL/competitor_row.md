# COMPETITOR ROW — Dell Technologies (DELL)
### Q2 evidence. A moat is a relative claim, so this row is mandatory, not colour.

> *"I can't understand how my company is doing unless I understand what the other eight are
> doing. I want to have the perspective of, in terms of market share, what's going on in the
> business or their margins or the trend of margins."* — **[E3-28]**, 1996 Annual Meeting

Built 2026-09-07. **Every figure below is filing-sourced**: SEC XBRL companyfacts
(`https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json`, 10-K forms only, ~365-day
durations) with the filed statement read directly wherever a tag was absent, sparse, or a
subtotal was not presented on the face. Accession numbers are recorded per figure.
No aggregator figures. No figure from memory.

**NO VERDICT IS FORMED HERE.** This file reports numbers and the arithmetic that produced
them. The moat judgment belongs in the run file at Q2.

---
## 0. THE PANEL, THE FISCAL-YEAR MISMATCH, AND HOW IT WAS ALIGNED

| Peer | CIK | FY end | Role in the row |
|---|---|---|---|
| **DELL** | 0001571996 | late Jan / early Feb | subject |
| HPE | 0001645590 | 31 Oct | direct ISG analogue (servers / storage) |
| SMCI | 0001375365 | 30 Jun | the pure AI-server assembler |
| HPQ | 0000047217 | 31 Oct | direct CSG analogue (PCs / printers) |
| IBM | 0000051143 | 31 Dec | the enterprise incumbent that left the box |
| **NVDA** | 0001045810 | late Jan | **the supplier whose margin is the question** |
| Lenovo | not an SEC registrant (HKEX 0992) | 31 Mar | see §8 |

**Alignment convention (stated, not hidden).** Each year is labelled by the filer's own
fiscal-year number and carries its period-end date. No year is re-cut to a common calendar:
doing so would require re-aggregating unfiled quarterly stubs, which is not filing-sourced.
The consequences of the mismatch:

- **DELL FY2026 (ended 2026-01-30) vs NVDA FY2026 (ended 2026-01-25) are five days apart.**
  This is effectively the same window, and it is precisely the comparison the thesis needs.
- **HPE and HPQ end 31 Oct**, so their FY2025 leads DELL's FY2026 by three months. Their
  six-year window is therefore FY2020–FY2025, not FY2021–FY2026.
- **SMCI ends 30 Jun.** Its FY2026 (ended 2026-06-30) *trails* DELL FY2026 by five months
  and so contains five months DELL has not yet reported. Filed 2026-08-31.
- **IBM ends 31 Dec**, window FY2020–FY2025.
- **DELL FY2023 was a 53-week year** (2022-01-28 → 2023-02-03, 371 days). One extra week of
  revenue sits in that column.

**RESTATEMENT RULE APPLIED: latest-filed wins.** Where a company restated a prior year, the
figure used is the most recently filed version, so every year in a row sits on one basis.
It matters in four places and each is named:

- **DELL restated FY2020 and FY2021 for the VMware spin-off** (10-K accn 0001571996-22-000009,
  filed 2022-03-24). FY2021 revenue went **94,224 → 86,670**, gross profit **29,417 → 20,140**,
  operating income **5,144 → 3,685**. The as-first-filed numbers are *not* continuing
  operations and are not used.
- **DELL restated FY2024** in the FY2026 10-K (accn 0001571996-26-000008): gross profit
  **20,869 → 21,069**, operating income **5,211 → 5,411**. Both +200, i.e. a reclassification
  out of cost of net revenue. The restated figures are used.
- HPQ FY2021 revenue **63,487 → 63,460** and operating income **5,302 → 5,359**; HPQ FY2022
  revenue **62,983 → 62,910**. Small reclassifications; restated figures used.
- IBM FY2020 SG&A was restated **23,082 → 20,561** for the Kyndryl separation. The FY2022
  10-K (accn 0001558370-23-002376) continuing-operations basis is used throughout.

---
## 1. GROSS MARGIN % BY FISCAL YEAR — THE ROW THAT CARRIES THE THESIS

**The thesis under test:** in server and PC assembly the margin sits with the merchant-silicon
supplier, not the assembler.

Tag: `us-gaap:GrossProfit` ÷ `us-gaap:Revenues` (or `RevenueFromContractWithCustomerExcludingAssessedTax`),
except HPE and HPQ — see the notes below the table.

| Peer | FY-6 | FY-5 | FY-4 | FY-3 | FY-2 | **latest FY** |
|---|---|---|---|---|---|---|
| **DELL** (Jan/Feb) | **23.24%**<br>FY21 | **21.63%**<br>FY22 | **22.18%**<br>FY23 | **23.83%**<br>FY24 | **22.24%**<br>FY25 | **20.00%**<br>**FY26** |
| HPE (Oct) | 31.39%<br>FY20 | 33.75%<br>FY21 | 33.36%<br>FY22 | 35.14%<br>FY23 | 32.79%<br>FY24 | 30.26%<br>FY25 |
| SMCI (Jun) | 15.03%<br>FY21 | 15.40%<br>FY22 | 18.01%<br>FY23 | 13.75%<br>FY24 | 11.06%<br>FY25 | 10.82%<br>FY26 |
| HPQ (Oct) | 18.43%<br>FY20 | 21.13%<br>FY21 | 19.49%<br>FY22 | 21.42%<br>FY23 | 22.07%<br>FY24 | 20.60%<br>FY25 |
| IBM (Dec) | 55.94%<br>FY20 | 54.90%<br>FY21 | 54.00%<br>FY22 | 55.45%<br>FY23 | 56.65%<br>FY24 | 58.19%<br>FY25 |
| **NVDA** (Jan) | **62.34%**<br>FY21 | **64.93%**<br>FY22 | **56.93%**<br>FY23 | **72.72%**<br>FY24 | **74.99%**<br>FY25 | **71.07%**<br>**FY26** |
| Lenovo ⁋ (Mar) | 16.08%<br>FY21 | 16.82%<br>FY22 | 16.95%<br>FY23 | 17.24%<br>FY24 | 16.07%<br>FY25 | 15.42%<br>FY26 |

⁋ Lenovo is **not SEC-sourced**. It is IFRS, from its HKEX annual results announcements — see
§8 for the source rung and the comparability caveat.

### The underlying dollars ($M)

| DELL | FY2021<br>2021-01-29 | FY2022<br>2022-01-28 | FY2023<br>2023-02-03 | FY2024<br>2024-02-02 | FY2025<br>2025-01-31 | FY2026<br>2026-01-30 |
|---|---|---|---|---|---|---|
| Revenue | 86,670 | 101,197 | 102,301 | 88,425 | 95,567 | 113,538 |
| Cost of net revenue | 66,530 | 79,306 | 79,615 | 67,356 | 74,317 | 90,831 |
| Gross margin | 20,140 | 21,891 | 22,686 | 21,069 | 21,250 | 22,707 |

Tags `Revenues`, `CostOfRevenue`, `GrossProfit`. Latest accession 0001571996-26-000008.
**Cross-check against the filed statement (operator rule 4):** the CONSOLIDATED STATEMENTS OF
INCOME in the FY2026 10-K, R5.htm, reads Total net revenue **$113,538**, Total cost of net
revenue **90,831**, Gross margin **22,707**, Operating income **8,149**. XBRL confirmed
against the filed face.

| NVDA | FY2021<br>2021-01-31 | FY2022<br>2022-01-30 | FY2023<br>2023-01-29 | FY2024<br>2024-01-28 | FY2025<br>2025-01-26 | FY2026<br>2026-01-25 |
|---|---|---|---|---|---|---|
| Revenue | 16,675 | 26,914 | 26,974 | 60,922 | 130,497 | 215,938 |
| Cost of revenue | 6,279 | 9,439 | 11,618 | 16,621 | 32,639 | 62,475 |
| Gross profit | 10,396 | 17,475 | 15,356 | 44,301 | 97,858 | 153,463 |

Latest accession 0001045810-26-000021 (FY2026 10-K, filed 2026-02-25).

| SMCI | FY2021<br>2021-06-30 | FY2022<br>2022-06-30 | FY2023<br>2023-06-30 | FY2024<br>2024-06-30 | FY2025<br>2025-06-30 | FY2026<br>2026-06-30 |
|---|---|---|---|---|---|---|
| Revenue | 3,557.4 | 5,196.1 | 7,123.5 | 14,989.3 | 21,972.0 | 39,063.1 |
| Cost of revenue | 3,022.9 | 4,396.1 | 5,840.5 | 12,927.8 | 19,542.1 | 34,835.8 |
| Gross profit | 534.5 | 800.0 | 1,283.0 | 2,061.4 | 2,429.9 | 4,227.3 |

Latest accession 0001375365-26-000022 (FY2026 10-K, filed 2026-08-31). Balance sheet in that
filing is stated in **thousands**; converted to $M here.

| IBM | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Revenue | 55,179 | 57,350 | 60,530 | 61,860 | 62,753 | 67,535 |
| Cost | 24,314 | 25,865 | 27,842 | 27,560 | 27,201 | 28,239 |
| Gross profit | 30,865 | 31,486 | 32,687 | 34,300 | 35,551 | 39,297 |

Accessions 0001558370-23-002376 (FY22/21/20) and 0000051143-26-000010 (FY25/24/23). IBM
presents `Gross profit` on the face of the CONSOLIDATED INCOME STATEMENT.

| HPQ | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Net revenue | 56,639 | 63,460 | 62,910 | 53,718 | 53,559 | 55,295 |
| Cost of revenue | 46,202 | 50,053 | 50,647 | 42,210 | 41,741 | 43,903 |
| Gross profit (computed) | 10,437 | 13,407 | **12,263** | **11,508** | **11,818** | **11,392** |

> **HPQ METHOD NOTE.** HPQ does **not** present a gross profit subtotal on the face of its
> Consolidated Statements of Earnings; the face runs Net revenue → Costs and expenses (cost of
> revenue, R&D, SG&A, restructuring, amortization) → Total costs and expenses → Earnings from
> operations. `us-gaap:GrossProfit` is tagged only for FY2022–FY2025 (from elsewhere in the
> filing). Gross profit for FY2020 and FY2021 is therefore **computed as Revenue − CostOfRevenue**.
> **The identity was verified, not assumed:** for all four years where HPQ tags GrossProfit, the
> computed figure reproduces the tagged figure **exactly** (FY2022 62,910 − 50,647 = 12,263 ✓;
> FY2023 53,718 − 42,210 = 11,508 ✓; FY2024 53,559 − 41,741 = 11,818 ✓; FY2025 55,295 − 43,903
> = 11,392 ✓). The bolded years are tagged; the two unbolded years are the computation.
> Accessions 0000047217-25-000071, -24-000080, -23-000100, -22-000068, -21-000060.

| HPE | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| Products revenue | 16,264 | 17,011 | 17,794 | 18,100 | 18,587 | 21,956 |
| Services revenue | 10,249 | 10,279 | 10,219 | 10,488 | 10,872 | 11,573 |
| Financing income | 469 | 494 | 483 | 547 | 668 | 767 |
| **Total net revenue** | **26,982** | **27,784** | **28,496** | **29,135** | **30,127** | **34,296** |
| Cost of products | 11,698 | 11,892 | 12,463 | 11,958 | 12,961 | 16,151 |
| Cost of services | 6,544 | 6,304 | 6,217 | 6,555 | 6,793 | 7,268 |
| Financing cost | 271 | 212 | 310 | 383 | 495 | 500 |
| **Gross profit (computed)** | **8,469** | **9,376** | **9,506** | **10,239** | **9,878** | **10,377** |

> **HPE METHOD NOTE — the one place a number had to be built rather than read.** HPE presents
> **no gross profit subtotal and no consolidated cost-of-revenue line**; its face runs Net
> revenue (Products / Services / Financing income) → Costs and expenses (Cost of products, Cost
> of services, Financing cost, R&D, SG&A, amortization, impairment, transformation, acquisition
> charges) → Total costs and expenses → Earnings from operations. `us-gaap:CostOfRevenue` and
> `CostOfGoodsAndServicesSold` return **nothing** for FY2019 onward, and the cost of products /
> cost of services lines carry a `srt:ProductOrServiceAxis` dimension, so they do **not** appear
> in companyfacts at all. They were read off the filed Consolidated Statements of Earnings:
> **FY2025/24/23 from accn 0001645590-25-000130 (R3.htm), FY2022/21/20 from accn
> 0001645590-22-000071 (R3.htm).**
> **CONVENTION, disclosed:** gross profit = total net revenue − (cost of products + cost of
> services + financing cost). Financing cost is included because financing *income* is inside
> the revenue denominator, matching DELL, which likewise runs DFS through revenue and cost of
> net revenue. Excluding financing cost from both sides instead would raise HPE's FY2025 gross
> margin from 30.26% to 31.72% and its FY2020 from 31.39% to 32.39%; the choice moves HPE's
> margin by roughly one point and changes no ordering in the table.

---
## 2. OPERATING MARGIN % BY FISCAL YEAR

Tag `us-gaap:OperatingIncomeLoss` ÷ revenue, except IBM — see the note.

| Peer | FY-6 | FY-5 | FY-4 | FY-3 | FY-2 | **latest FY** |
|---|---|---|---|---|---|---|
| **DELL** | **4.25%**<br>FY21 | **4.60%**<br>FY22 | **5.64%**<br>FY23 | **6.12%**<br>FY24 | **6.53%**<br>FY25 | **7.18%**<br>**FY26** |
| HPE | −1.22%<br>FY20 | 4.07%<br>FY21 | 2.74%<br>FY22 | 7.17%<br>FY23 | 7.27%<br>FY24 | −1.27%<br>FY25 |
| SMCI | 3.48%<br>FY21 | 6.45%<br>FY22 | 10.68%<br>FY23 | 8.08%<br>FY24 | 5.70%<br>FY25 | 7.09%<br>FY26 |
| HPQ | 6.11%<br>FY20 | 8.44%<br>FY21 | 7.25%<br>FY22 | 6.43%<br>FY23 | 7.13%<br>FY24 | 5.74%<br>FY25 |
| IBM † | 8.45%<br>FY20 | 11.97%<br>FY21 | 13.50%<br>FY22 | 15.17%<br>FY23 | 14.95%<br>FY24 | 17.50%<br>FY25 |
| **NVDA** | **27.18%**<br>FY21 | **37.31%**<br>FY22 | **15.66%**<br>FY23 | **54.12%**<br>FY24 | **62.42%**<br>FY25 | **60.38%**<br>**FY26** |
| Lenovo ⁋ | 3.59%<br>FY21 | 4.30%<br>FY22 | 4.31%<br>FY23 | 3.53%<br>FY24 | 3.13%<br>FY25 | 3.93%<br>FY26 |

### Operating income dollars ($M)

| | FY-6 | FY-5 | FY-4 | FY-3 | FY-2 | latest |
|---|---|---|---|---|---|---|
| DELL | 3,685 | 4,659 | 5,771 | 5,411 | 6,237 | 8,149 |
| HPE | (329) | 1,132 | 782 | 2,089 | 2,190 | **(437)** |
| SMCI | 123.9 | 335.2 | 761.1 | 1,210.8 | 1,253.0 | 2,770.5 |
| HPQ | 3,462 | 5,359 | 4,559 | 3,456 | 3,818 | 3,174 |
| IBM † | 4,662 | 6,865 | 8,174 | 9,382 | 9,380 | 11,822 |
| NVDA | 4,532 | 10,041 | 4,224 | 32,972 | 81,453 | 130,387 |

**Two operating-income anomalies, both named rather than smoothed:**

- **HPE FY2025 is an operating LOSS of $(437)M** on $34,296M of revenue, in the year HPE's
  revenue grew 13.8%. The face of the statement (accn 0001645590-25-000130) shows **Impairment
  charges 1,621** (nil in FY2024 and FY2023), amortization of intangibles rising 267 → 511, and
  acquisition/disposition charges rising 211 → 458 — the Juniper year. Goodwill rose 18,086 →
  23,770 and intangibles 510 → 6,368 across the same balance sheet. The footnote records
  goodwill "net of accumulated impairment losses of $3.3 billion", increased ~$1.5B from
  FY2024. HPE still reported positive net earnings of $57M, because $342M of tax benefit,
  a $248M gain on sale of a business and $79M of equity-interest earnings sit below the
  operating line.
- **NVDA FY2023 operating margin collapses to 15.66%** from 37.31%, and gross margin to 56.93%
  from 64.93%. The segment note for that year (accn 0001045810-23-000017) shows an
  **acquisition termination cost of $(1,353)M** inside the All Other reconciling column — the
  Arm break fee — plus $(2,710)M of stock-based compensation. This is the pre-AI trough year.

> **† IBM METHOD NOTE — COMPUTED, NOT TAGGED.** IBM presents **no operating income subtotal**
> and `us-gaap:OperatingIncomeLoss` returns **nothing** for any year. IBM's face runs Gross
> profit → Expense and other (income): SG&A, R&D, Intellectual property and custom development
> income, Other (income) and expense, Interest expense → Total expense and other (income) →
> Income from continuing operations before income taxes.
> **CONVENTION, disclosed:** operating income = Gross profit − SG&A − R&D + IP and custom
> development income. This excludes "Other (income) and expense" and interest expense, which
> keeps IBM comparable to the peers, whose non-service pension credits, FX and interest
> likewise sit below the operating line. It matters: IBM's FY2022 "Other (income) and expense"
> was **+5,803** (a charge — the pension settlement year) and FY2024 **+1,871**; leaving those
> in would have driven IBM's FY2022 margin to 1.91% and made the series unreadable as
> operations.
> Components used, all read off the filed CONSOLIDATED INCOME STATEMENT:
>
> | IBM ($M) | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
> |---|---|---|---|---|---|---|
> | Gross profit | 30,865 | 31,486 | 32,687 | 34,300 | 35,551 | 39,297 |
> | less SG&A | 20,561 | 18,745 | 18,609 | 19,003 | 19,688 | 20,123 |
> | less R&D | 6,262 | 6,488 | 6,567 | 6,775 | 7,479 | 8,316 |
> | plus IP & custom dev income | 620 | 612 | 663 | 860 | 996 | 964 |
> | **= operating income** | **4,662** | **6,865** | **8,174** | **9,382** | **9,380** | **11,822** |
>
> The IP-and-custom-development-income line is an **IBM extension tag** and is absent from
> companyfacts (which carries only `dei`, `us-gaap`, `ffd` for this filer); it was read off
> R2.htm of accn 0001558370-23-002376 and R3.htm of accn 0000051143-26-000010.

---
## 3. DELL'S OWN SEGMENTS — ISG AND CSG OPERATING MARGIN

The consolidated line hides the two businesses the peers are analogues *for*. Segment
operating income is before amortization of intangibles, stock-based compensation and other
corporate expenses, which is why the segments sum above the consolidated total.
Accessions 0001571996-26-000008 (R121.htm) and 0001571996-23-000007 (R127.htm).

| DELL ISG (servers/storage) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Revenue ($M) | 33,002 | 34,366 | 38,356 | 33,885 | 43,593 | **60,826** |
| Operating income ($M) | 3,753 | 3,736 | 5,045 | 4,286 | 5,579 | **7,111** |
| **Operating margin** | **11.37%** | **10.87%** | **13.15%** | **12.65%** | **12.80%** | **11.69%** |

| DELL CSG (PCs) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Revenue ($M) | 48,387 | 61,464 | 58,213 | 48,916 | 48,393 | 50,984 |
| Operating income ($M) | 3,333 | 4,365 | 3,824 | 3,712 | 2,972 | 2,833 |
| **Operating margin** | **6.89%** | **7.10%** | **6.57%** | **7.59%** | **6.14%** | **5.56%** |

**The arithmetic, without a verdict on it:** ISG revenue grew **+39.5%** in FY2026 (43,593 →
60,826) and ISG operating margin fell from 12.80% to 11.69%. Consolidated gross margin in the
same year fell to **20.00%**, the lowest of the six years, while consolidated operating margin
rose to **7.18%**, the highest of the six — operating expenses fell from 15,013 to 14,558 on
19% higher revenue.

---
## 4. RETURN ON UNLEVERAGED NET TANGIBLE ASSETS — MOST RECENT FISCAL YEAR

> *"What a business can be expected to earn on unleveraged net tangible assets, excluding any
> charges against earnings for amortization of Goodwill, is the best guide to the economic
> attractiveness of the operation."* — **[E2-43]**, 1983 Letter, Goodwill appendix

**Formula as specified:** numerator = operating income × (1 − 0.21) at a 21% notional rate;
denominator = total assets − goodwill − intangibles − non-interest-bearing current liabilities
(NIBCL = total current liabilities − short-term/current debt). All balance-sheet figures read
off the filed balance sheet of the latest 10-K.

| | DELL<br>FY2026 | HPE<br>FY2025 | SMCI<br>FY2026 | HPQ<br>FY2025 | IBM<br>FY2025 | NVDA<br>FY2026 |
|---|---|---|---|---|---|---|
| Operating income | 8,149 | **(437)** | 2,770.5 | 3,174 | 11,822 † | 130,387 |
| × 0.79 = **numerator** | **6,437.7** | **(345.2)** | **2,188.7** | **2,507.5** | **9,339.4** | **103,005.7** |
| Total assets | 101,286 | 75,906 | 29,945.5 | 41,769 | 151,880 | 206,803 |
| − Goodwill | 19,547 | 23,770 | **0** | 8,706 | 67,717 | 20,832 |
| − Intangibles, net | 4,533 | 6,368 | **0** | 1,012 ‡ | 11,391 | 3,306 |
| Total current liabilities | 63,269 | 24,643 | 7,160.1 | 29,258 | 38,658 | 32,163 |
| − short-term / current debt | 7,990 | 4,609 | 2,039.8 | 845 | 6,424 | 999 |
| − **NIBCL** | **55,279** | **20,034** | **5,120.3** | **28,413** | **32,234** | **31,164** |
| **= denominator** | **21,927** | **25,734** | **24,825.2** | **3,638** | **40,538** | **151,501** |
| **ROUNTA** | **29.36%** | **−1.34%** | **8.82%** | **68.92%** | **23.04%** | **67.99%** |

**Balance-sheet lines used, by name and filing:**
DELL — CONSOLIDATED STATEMENTS OF FINANCIAL POSITION, accn 0001571996-26-000008 R3.htm:
Total assets 101,286; Goodwill 19,547; Intangible assets, net 4,533; Total current liabilities
63,269; Short-term debt 7,990.
HPE — Consolidated Balance Sheets, accn 0001645590-25-000130 R5.htm: 75,906; 23,770; 6,368;
24,643; Notes payable and short-term borrowings 4,609.
SMCI — CONSOLIDATED BALANCE SHEETS, accn 0001375365-26-000022 R3.htm (stated in thousands):
29,945,467; **no goodwill line and no intangible-assets line appears on the balance sheet at
all**; 7,160,106; Lines of credit and term loans, current 2,039,774.
HPQ — Consolidated Balance Sheets, accn 0000047217-25-000071 R5.htm: 41,769; Goodwill 8,706;
**no separate intangibles line on the face** — ‡ intangibles taken from
`us-gaap:FiniteLivedIntangibleAssetsNet` = 1,012 (inside "Other non-current assets" 7,561);
29,258; Notes payable and short-term borrowings 845.
IBM — CONSOLIDATED BALANCE SHEET, accn 0000051143-26-000010 R5.htm: 151,880; 67,717;
Intangible assets—net 11,391; 38,658; Short-term debt 6,424. † numerator is the computed
operating income from §2.
NVDA — Consolidated Balance Sheets, accn 0001045810-26-000021 R5.htm: 206,803; 20,832; 3,306;
32,163; Short-term debt 999.

### NEGATIVE BOOK EQUITY — stated explicitly, as required

| | Total stockholders' equity (deficit) | Filing |
|---|---|---|
| **DELL FY2026** | **$(2,470)M** — a deficit, and it *widened* from $(1,482)M at FY2025 | 0001571996-26-000008 |
| **HPQ FY2025** | **$(346)M** — a deficit, narrowed from $(1,323)M at FY2024 | 0000047217-25-000071 |
| HPE FY2025 | +$24,754M (incl. NCI) | 0001645590-25-000130 |
| SMCI FY2026 | +$14,479.6M (incl. NCI) | 0001375365-26-000022 |
| IBM FY2025 | +$32,740M (incl. NCI) | 0000051143-26-000010 |
| NVDA FY2026 | +$157,293M | 0001045810-26-000021 |

DELL's deficit is a buyback artefact, not an insolvency signal on its face: treasury stock at
cost is $(14,533)M against retained earnings of +$3,325M. HPQ's is the same shape: accumulated
deficit $(2,027)M against additional paid-in capital of only $2,129M. **Both are named because
a book-equity denominator is meaningless for either company** — which is exactly why [E2-43]
asks for net tangible assets rather than book ROE.

### Four caveats on the ROUNTA line, disclosed rather than buried

1. **HPQ's 68.92% is a negative-working-capital artefact, not a productivity finding.** The
   denominator is only **$3,638M** on $55,295M of revenue, because accounts payable of
   $18,051M exceed inventory of $8,512M. A denominator that small makes the ratio extremely
   sensitive: a $500M move in payables swings the ratio by ~10 percentage points. The dollars,
   not the percentage, are the honest reading.
2. **NVDA's denominator carries $84.8B of non-operating assets** — marketable securities
   51,951 + cash 10,605 + non-marketable equity securities 22,251. Stripping those gives a
   denominator of $66,694M and a ratio of **154.4%**. That variant is flagged as a variant; the
   67.99% above is the formula as specified.
3. **DELL's denominator carries $14,280M of DFS financing receivables** (8,458 short-term +
   5,822 long-term, accn 0001571996-26-000008 R66.htm) — an interest-earning asset funded
   with debt, sitting inside an "unleveraged" denominator. It pushes DELL's ROUNTA down
   relative to a pure-manufacturing peer.
4. **[E2-43] also asks for amortization to be added back to the numerator**, which the
   specified formula does not do. Where the amount is disclosed: DELL FY2026 amortization of
   intangibles **$500M** (reconciling item, R121.htm) — adding it back at 0.79 raises DELL's
   ROUNTA from 29.36% to **31.16%**. HPE FY2025 amortization **$511M** — adding it back takes
   HPE from −1.34% to **+0.23%**. This is a labelled variant, not a substitution.

---
## 5. REVENUE BY FISCAL YEAR ($M)

| Peer | FY-6 | FY-5 | FY-4 | FY-3 | FY-2 | latest FY |
|---|---|---|---|---|---|---|
| DELL | 86,670<br>FY21 | 101,197<br>FY22 | 102,301<br>FY23 | 88,425<br>FY24 | 95,567<br>FY25 | **113,538**<br>FY26 |
| HPE | 26,982<br>FY20 | 27,784<br>FY21 | 28,496<br>FY22 | 29,135<br>FY23 | 30,127<br>FY24 | 34,296<br>FY25 |
| SMCI | 3,557<br>FY21 | 5,196<br>FY22 | 7,124<br>FY23 | 14,989<br>FY24 | 21,972<br>FY25 | **39,063**<br>FY26 |
| HPQ | 56,639<br>FY20 | 63,460<br>FY21 | 62,910<br>FY22 | 53,718<br>FY23 | 53,559<br>FY24 | 55,295<br>FY25 |
| IBM | 55,179<br>FY20 | 57,350<br>FY21 | 60,530<br>FY22 | 61,860<br>FY23 | 62,753<br>FY24 | 67,535<br>FY25 |
| NVDA | 16,675<br>FY21 | 26,914<br>FY22 | 26,974<br>FY23 | 60,922<br>FY24 | 130,497<br>FY25 | **215,938**<br>FY26 |
| Lenovo ⁋ | 60,742<br>FY21 | 71,618<br>FY22 | 61,947<br>FY23 | 56,864<br>FY24 | 69,077<br>FY25 | **83,075**<br>FY26 |

Six-year compound growth (endpoint to endpoint, five intervals): DELL **+5.5%/yr**;
HPE +4.9%/yr; **SMCI +61.5%/yr**; HPQ −0.5%/yr; IBM +4.1%/yr; **NVDA +66.9%/yr**;
Lenovo +6.5%/yr.

**NVDA crossed DELL in revenue in its FY2026: $215,938M against DELL's $113,538M, in fiscal
years ending five days apart.** In FY2021 (windows also five days apart) DELL's revenue was
5.2× NVDA's.

---
## 6. NVDA IN DETAIL — HOW MUCH OF THE AI SERVER DOLLAR STOPS AT NVIDIA

### 6a. Data Center segment revenue by fiscal year ($M)

Read off the segment note, **Schedule of Revenue by Market**: accn 0001045810-26-000021
R85.htm (FY2026/25/24) and accn 0001045810-23-000017 R26.htm (FY2023/22/21).

| NVDA | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| **Data Center revenue** | **6,696** | **10,613** | **15,005** | **47,525** | **115,186** | **193,737** |
| — of which Compute | n/d | n/d | n/d | 38,950 | 102,196 | 162,361 |
| — of which Networking | n/d | n/d | n/d | 8,575 | 12,990 | 31,376 |
| Total company revenue | 16,675 | 26,914 | 26,974 | 60,922 | 130,497 | 215,938 |
| **Data Center as % of revenue** | **40.2%** | **39.4%** | **55.6%** | **78.0%** | **88.3%** | **89.7%** |
| Company gross margin | 62.34% | 64.93% | 56.93% | 72.72% | 74.99% | **71.07%** |

The Compute/Networking split is disclosed only from FY2024 in the FY2026 10-K's table; "n/d"
means not disclosed in the source read, **not** estimated.

### 6b. Data Center gross margin — NOT SEPARATELY DISCLOSED

**NVDA does not report gross margin by market platform or by reportable segment.** No such
figure exists in the filing and none is fabricated here. What *is* disclosed is segment
**operating** income for the two reportable segments, and Data Center sits inside Compute &
Networking:

| Compute & Networking segment | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Revenue ($M) | 6,841 | 11,046 | 15,068 | 47,405 | 116,193 | 193,479 |
| Operating income ($M) | 2,548 | 4,598 | 5,083 | 32,016 | 82,875 | 130,141 |
| **Segment operating margin** | **37.25%** | **41.63%** | **33.73%** | **67.54%** | **71.33%** | **67.26%** |

Accessions 0001045810-26-000021 R82.htm and 0001045810-23-000017 R26.htm. Segment operating
income excludes stock-based compensation, acquisition-related costs and unallocated cost of
revenue, all held in an "All Other" reconciling column — $(5,411)M in FY2023 and $(8,910)M in
FY2026 (139,297 segment total − 130,387 consolidated).

**The trajectory, stated as arithmetic:** as Data Center went from **55.6%** of revenue
(FY2023) to **89.7%** (FY2026), NVDA's company gross margin went from **56.93%** to **71.07%**
and the Compute & Networking segment operating margin from **33.73%** to **67.26%**. The AI mix
arrived carrying *more* margin, not less.

### 6c. NVDA gross margin beside DELL ISG operating margin — the requested comparison

Fiscal years ending **five days apart**.

| | NVDA FY2026<br>(ended 2026-01-25) | DELL FY2026<br>(ended 2026-01-30) |
|---|---|---|
| **NVDA gross margin** | **71.07%** | — |
| **DELL ISG operating margin** | — | **11.69%** |
| DELL consolidated gross margin | — | 20.00% |
| DELL consolidated operating margin | — | 7.18% |
| Revenue | 215,938 | 113,538 |
| Data Center / ISG revenue | 193,737 | 60,826 |
| Gross profit | 153,463 | 22,707 |
| Operating income | 130,387 | 8,149 |

**The arithmetic that answers "how much of the AI server dollar stops at Nvidia":**

- NVDA's **Data Center revenue alone ($193,737M) is 3.19× DELL's entire ISG revenue
  ($60,826M)** and 1.71× DELL's entire company revenue.
- NVDA's **company gross profit ($153,463M) is 1.35× DELL's total revenue ($113,538M)** and
  **6.76× DELL's total gross profit ($22,707M)**, on revenue only 1.90× DELL's.
- NVDA's **operating income ($130,387M) is 16.0× DELL's ($8,149M)** and **18.3× DELL's ISG
  segment operating income ($7,111M)**.
- Per dollar of revenue: NVDA keeps **71.07¢** of gross profit and **60.38¢** of operating
  profit. DELL keeps **20.00¢** and **7.18¢**; DELL's ISG keeps **11.69¢** of segment
  operating profit before corporate cost, amortization and stock-based compensation.
- The gross-margin gap between supplier and assembler in the same window is **71.07% − 20.00%
  = 51.07 percentage points**. Against DELL's ISG segment operating margin the gap is
  **59.38 points**.

No verdict is drawn from these numbers here.

---
## 7. SMCI IN DETAIL — DID AI-SERVER REVENUE ARRIVE WITH MARGIN?

The requested FY2022 → FY2025 series, extended to FY2026 (10-K filed 2026-08-31, accn
0001375365-26-000022) and back to FY2021 for the pre-AI baseline.

| SMCI | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Revenue ($M) | 3,557.4 | 5,196.1 | 7,123.5 | 14,989.3 | 21,972.0 | 39,063.1 |
| Revenue growth | — | +46.1% | +37.1% | **+110.4%** | **+46.6%** | **+77.8%** |
| Gross profit ($M) | 534.5 | 800.0 | 1,283.0 | 2,061.4 | 2,429.9 | 4,227.3 |
| **Gross margin** | **15.03%** | **15.40%** | **18.01%** | **13.75%** | **11.06%** | **10.82%** |
| Operating income ($M) | 123.9 | 335.2 | 761.1 | 1,210.8 | 1,253.0 | 2,770.5 |
| Operating margin | 3.48% | 6.45% | 10.68% | 8.08% | 5.70% | 7.09% |

**ANSWER TO THE QUESTION ASKED: yes, it fell, and it fell hard.**

- **FY2022 → FY2025 gross margin: 15.40% → 11.06%, a fall of 4.34 percentage points**, i.e. a
  **28.2% relative decline**, while revenue over the same three years rose **4.23×** (5,196.1
  → 21,972.0).
- The peak is **FY2023 at 18.01%**, the last year before the AI ramp dominated the mix.
  From that peak to FY2026 the gross margin fell **18.01% → 10.82%**, a fall of **7.19 points**
  and a **39.9% relative decline**, while revenue rose **5.48×** (7,123.5 → 39,063.1).
- Gross profit dollars still grew (1,283.0 → 4,227.3, +3.29×), but **slower than revenue
  (+5.48×)** — the definition of margin dilution. Every incremental dollar of revenue from
  FY2023 to FY2026 carried **9.20¢** of gross profit (Δ gross profit 2,944.3 ÷ Δ revenue
  31,939.6), against the 18.01% the FY2023 base was earning.
- FY2026 shows a partial operating-margin recovery (5.70% → 7.09%) achieved **below** the gross
  line, not at it: gross margin still fell (11.06% → 10.82%) while operating expenses fell
  from 5.36% of revenue to 3.73%.
- The balance-sheet cost of that revenue: SMCI's inventories rose **$4,680.4M → $12,895.9M**
  (+175%) and current lines of credit and term loans **$75.1M → $2,039.8M** (+27×) across
  FY2025 → FY2026 (accn 0001375365-26-000022, R3.htm, stated in thousands).

**SMCI is the cleanest read in the panel** because it carries **zero goodwill and zero
intangibles** on its balance sheet — there is no acquired-asset layer between revenue and the
assembly economics.

**Filing-history caveat, stated:** SMCI's FY2024 10-K was delayed and its FY2022 figures were
re-presented in a filing accessioned 0001375365-25-000004 (filed 2025-02-25). The figures above
are the latest-filed version of each year.

---
## 8. LENOVO — OFF THE SEC SHELF, BUT OBTAINED FROM ITS OWN FILED ACCOUNTS

**The limit first, stated plainly.** Lenovo Group Ltd is **not an SEC registrant**. It is
listed on the Hong Kong Stock Exchange (HKEX 0992 / RMB counter 80992), incorporated in Hong
Kong, reports under **IFRS**, and files no 10-K, 20-F or 40-F. There is **no CIK and no
companyfacts endpoint**, so nothing in §§1–7's method reaches it. Its fiscal year ends
**31 March**.

**It was nevertheless obtained, from the issuer's own audited results announcements.**

### Source and rung — flagged, as required

The documents used are Lenovo's **ANNUAL RESULTS ANNOUNCEMENTS**, each opening with the
standard HKEX disclaimer ("Hong Kong Exchanges and Clearing Limited and The Stock Exchange of
Hong Kong Limited take no responsibility for the contents of this announcement…") and stating
that the board "announces the **audited** results of the Company and its subsidiaries… for the
year ended March 31". The figures below are read off the **CONSOLIDATED INCOME STATEMENT** and
**CONSOLIDATED BALANCE SHEET** pages of those announcements.

**Rung declaration.** These are the issuer's own audited filed accounts — the same class of
document as a 10-K — but the **copies were retrieved from `doc.irasia.com`, a listed-company
document mirror, not from `hkexnews.hk` directly.** That is one rung below the issuing
authority and is recorded here rather than concealed. The documents carry the HKEX
announcement header and page furniture intact, and the FY2026 figures **independently
reconcile** against Lenovo's own investor-relations quarterly income statements
(`investor.lenovo.com`): the four quarters ended 30 Jun 2025, 30 Sep 2025, 31 Dec 2025 and
31 Mar 2026 sum to revenue **83,074,555**, cost of sales **70,265,133**, gross profit
**12,809,422** and operating profit **3,261,743** — matching the annual statement to the
dollar. Two independent company-published routes agreeing to the unit is the check that was
available; it is not a substitute for hkexnews.hk.

| Fiscal year (ended 31 Mar) | Source document | Page |
|---|---|---|
| FY2026, FY2025 | FY2025/26 Annual Results Announcement, `doc.irasia.com/listco/hk/lenovo/annual/2026/res.pdf` | 18, 20–21 |
| FY2024, FY2023 | FY2023/24 Annual Results Announcement, `.../annual/2024/res.pdf` | 18 |
| FY2022, FY2021 | FY2021/22 Annual Results Announcement, `.../annual/2022/res.pdf` | 16 |

### Lenovo consolidated income statement (US$'000, as filed)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Revenue | 60,742,312 | 71,618,216 | 61,946,854 | 56,863,784 | 69,076,968 | 83,074,555 |
| Cost of sales | (50,974,425) | (59,569,241) | (51,445,762) | (47,060,601) | (57,979,358) | (70,265,133) |
| **Gross profit** | **9,767,887** | **12,048,975** | **10,501,092** | **9,803,183** | **11,097,610** | **12,809,422** |
| **Gross margin** | **16.08%** | **16.82%** | **16.95%** | **17.24%** | **16.07%** | **15.42%** |
| Operating profit | 2,180,407 | 3,080,569 | 2,668,823 | 2,005,784 | 2,164,153 | 3,261,743 |
| **Operating margin** | **3.59%** | **4.30%** | **4.31%** | **3.53%** | **3.13%** | **3.93%** |

Lenovo reports in **US dollars**, so no currency translation was applied and none is needed.

### Lenovo ROUNTA, FY2026 — computed, with two caveats

From the CONSOLIDATED BALANCE SHEET at 31 March 2026 (US$'000): Total assets **57,129,094**;
Intangible assets **7,920,745** (a single line on the face, which under IFRS carries goodwill
inside it); Total current liabilities **41,357,576**; current Borrowings **878,443**.

- Numerator: 3,261,743 × 0.79 = **2,576,777** → $2,576.8M
- NIBCL: 41,357,576 − 878,443 = **40,479,133** → $40,479.1M
- Denominator: 57,129,094 − 7,920,745 − 40,479,133 = **8,729,216** → $8,729.2M
- **ROUNTA = 2,576.8 / 8,729.2 = 29.52%**

Total equity at 31 Mar 2026 was **+$8,443.6M** (positive; equity attributable to owners
$7,635.0M). Lenovo does **not** have the negative book equity DELL and HPQ carry.

**Caveat 1 — the 21% rate is notional and foreign here.** Lenovo is a Hong Kong-incorporated
group taxed across many jurisdictions; its FY2026 tax charge was $509,995k on pre-tax profit of
$2,669,908k, an effective rate of 19.1%. The 21% notional US rate is applied for comparability
with the panel, not because it is Lenovo's rate.

**Caveat 2 — IFRS is not US GAAP.** "Cost of sales" under IFRS need not draw the line where
US GAAP "cost of revenue" draws it, and Lenovo's single "Intangible assets" line combines
goodwill with other intangibles rather than splitting them as the US filers do. **Lenovo's
figures should be read as one rung less comparable than the six SEC filers**, and the run file
should say so at Q2 rather than treating the seven rows as homogeneous.

**Fiscal-year alignment.** Lenovo's FY2026 ended **2026-03-31**, two months after DELL's
FY2026 close (2026-01-30) and two months after NVDA's (2026-01-25). Its year therefore contains
two months neither DELL nor NVDA has yet reported. The offset runs the same way in every year
of the series, so the trend comparison is sound even where the level comparison is offset.

---
## 9. WHAT WAS NOT OBTAINED

| Item | Status | Obstacle |
|---|---|---|
| NVDA **Data Center gross margin** | **NOT OBTAINED** | NVDA discloses no gross margin by market platform or by reportable segment. The figure does not exist in the filing. Company gross margin and Compute & Networking segment operating margin are given instead, both labelled as what they are. |
| NVDA Compute / Networking revenue split, FY2021–FY2023 | **NOT OBTAINED** | Not disclosed in the FY2023 10-K's revenue-by-market table; marked "n/d" in §6a, not estimated. |
| HPE consolidated **gross profit** as a filed subtotal | Does not exist | HPE presents no gross profit line. Computed from the filed cost of products / cost of services / financing cost lines; convention disclosed in §1. |
| IBM **operating income** as a filed subtotal | Does not exist | IBM presents no operating income line and tags none. Computed; convention and components disclosed in §2. |
| HPQ gross profit, FY2020–FY2021 | Computed | Not tagged before FY2022; the Revenue − CostOfRevenue identity was verified against all four tagged years before being applied to the two untagged ones. |
| Lenovo from **hkexnews.hk** directly | Not used | Retrieved from `doc.irasia.com` mirror instead; rung flagged in §8. |
| Lenovo goodwill separated from other intangibles | **NOT OBTAINED** | Single combined "Intangible assets" line on the IFRS balance sheet face. The combined figure is deducted, which is what the formula asks for anyway. |

**No figure in this file was taken from an aggregator, and none was written from memory.**
Live quotes were not needed and none were fetched.

---
## 10. THE ROW ON ONE SCREEN

Latest fiscal year for each filer. **This is data, not a verdict.**

| | Gross margin | Operating margin | ROUNTA | Revenue $M | Book equity |
|---|---|---|---|---|---|
| **NVDA** FY26 | **71.07%** | **60.38%** | 67.99% | 215,938 | +157,293 |
| IBM FY25 | 58.19% | 17.50% † | 23.04% | 67,535 | +32,740 |
| HPE FY25 | 30.26% | −1.27% | −1.34% | 34,296 | +24,754 |
| HPQ FY25 | 20.60% | 5.74% | 68.92% ‡ | 55,295 | **−346** |
| **DELL** FY26 | **20.00%** | **7.18%** | **29.36%** | **113,538** | **−2,470** |
| Lenovo FY26 ⁋ | 15.42% | 3.93% | 29.52% | 83,075 | +8,444 |
| SMCI FY26 | 10.82% | 7.09% | 8.82% | 39,063 | +14,480 |

† computed, see §2.  ‡ artefact of a $3,638M denominator, see §4.  ⁋ IFRS / HKEX, see §8.

**The three arithmetic facts the row was built to establish, stated without interpretation:**

1. **The gross-margin ladder in the latest year runs NVDA 71.07% → IBM 58.19% → HPE 30.26% →
   HPQ 20.60% → DELL 20.00% → Lenovo 15.42% → SMCI 10.82%.** The four box assemblers occupy
   the bottom four places. The gap between the supplier and DELL is **51.07 percentage
   points** in fiscal years ending five days apart.
2. **SMCI's gross margin fell from 18.01% (FY2023) to 10.82% (FY2026) while its revenue rose
   5.48×.** Incremental gross profit on incremental revenue over that span was **9.20¢ per
   dollar**.
3. **NVDA's gross margin rose from 56.93% to 71.07% over the same span while Data Center went
   from 55.6% to 89.7% of its revenue.** DELL's consolidated gross margin fell to its six-year
   low of 20.00% in the year ISG revenue grew 39.5%, and DELL's ISG segment operating margin
   fell from 12.80% to 11.69%.

---
## 11. SELF-AUDIT OF THIS FILE

- [x] Every figure carries a fiscal-year label, a tag name or a filed statement reference, and
      an accession number (or, for Lenovo, a named document and page).
- [x] Fiscal-year mismatches stated and the alignment convention declared (§0).
- [x] Restatements found and the latest-filed basis applied, with the four material ones named
      (§0). The DELL VMware restatement would have overstated FY2021 revenue by $7,554M and
      gross margin by 8.0 percentage points had first-filed values been used.
- [x] Two computed metrics (HPE gross profit, IBM operating income) labelled **CONVENTION**
      with a one-line rationale each, per prime rule 3.
- [x] One HPQ computation validated against four years of tagged data before use.
- [x] Operator rule 4 satisfied: DELL's FY2026 income statement was read on the filed face
      (accn 0001571996-26-000008, R5.htm) and reconciled to the XBRL line by line.
- [x] Negative book equity stated explicitly for DELL and HPQ (§4).
- [x] Every number that could not be obtained is listed with its obstacle (§9). Nothing was
      estimated to fill a hole.
- [x] **No moat verdict is formed in this file.** That belongs at Q2 of the run.

*End of competitor row.*
