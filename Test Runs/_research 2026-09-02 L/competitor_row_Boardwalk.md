# COMPETITOR ROW — Boardwalk Pipelines (Loews) vs. natural-gas pipeline / midstream peers
**Status: IN PROGRESS — being appended as sources are read.**
Prepared 2026-09-02. Source class: SEC EDGAR primary filings (10-K) + XBRL companyfacts.
User-Agent used: `Chris Hrehor chrehor36@gmail.com`.

Framework note: this row exists because **Q2 is a relative claim** — a moat cannot be
asserted without the competitor row. Physical series required by **[E4-55]**. Capex/D&A
ratio required because **[E5-20]** forbids D&A as the maintenance-capex proxy in
capital-intensive businesses.

---

## 0. FILING REGISTER (document, date, accession)

| Company | CIK | Filing | Period | Filed | Accession | Primary doc |
|---|---|---|---|---|---|---|
| Boardwalk Pipeline Partners, LP | 0001336047 | (pending) | | | | |
| Williams Companies (WMB) | 0000107263 | (pending) | | | | |
| Kinder Morgan (KMI) | 0001506307 | (pending) | | | | |
| ONEOK (OKE) | 0001039684 | (pending) | | | | |
| Energy Transfer LP (ET) | 0001276187 | (pending) | | | | |

---

*(sections appended below as work proceeds)*

---

## 0. FILING REGISTER (document, date, accession) - COMPLETED

| Company | CIK | Filing | Period | Filed | Accession | Primary doc |
|---|---|---|---|---|---|---|
| Boardwalk Pipeline Partners, LP | 0001336047 | 10-K | FY2025 | 2026-02-10 | 0001336047-26-000004 | bwp-20251231.htm |
| Williams Companies (WMB) | 0000107263 | 10-K | FY2025 | 2026-02-24 | 0000107263-26-000006 | wmb-20251231.htm |
| Kinder Morgan (KMI) | 0001506307 | 10-K | FY2025 | 2026-02-13 | 0001506307-26-000011 | kmi-20251231.htm |
| ONEOK (OKE) | 0001039684 | 10-K | FY2025 | 2026-02-24 | 0001039684-26-000006 | oke-20251231.htm |
| Energy Transfer LP (ET) | 0001276187 | 10-K | FY2025 | 2026-02-19 | 0001276187-26-000013 | et-20251231.htm |

Prior-year filings additionally read for the maintenance-capex series in Section 1:

| Company | Period | Filed | Accession |
|---|---|---|---|
| KMI | FY2024 | 2025-02-13 | 0001506307-25-000008 |
| KMI | FY2023 | 2024-02-20 | 0001506307-24-000011 |
| KMI | FY2022 | 2023-02-08 | 0001506307-23-000023 |
| KMI | FY2021 | 2022-02-07 | 0001506307-22-000018 |
| ET | FY2023 | 2024-02-16 | 0001276187-24-000024 |
| ET | FY2022 | 2023-02-17 | 0001276187-23-000014 |
| BWP | FY2021-FY2024 | - | read from local text already in this folder |

**Operator rule 4 cross-checks - one figure per filer, tagged data against the filed statement:**

- **BWP**: XBRL capex FY2025 $353.9M = MD&A maintenance $194.2M + growth $159.7M. Ties exactly.
- **KMI**: XBRL capex FY2025 $3,026M = MD&A sustaining $951M + expansion $2,030M + accrual/other $45M. Ties exactly.
- **WMB**: XBRL revenue FY2025 $11,950M = filed income statement "Total revenues" $11,950M. Ties.
- **OKE**: XBRL revenue FY2023/24/25 $17,677 / $21,698 / $33,629M = filed "Total revenues" row. Ties.
- **ET**: XBRL revenue FY2023/24/25 $78,586 / $82,671 / $85,536M = filed "Total revenues" row. Ties.

---

## 1. MAINTENANCE vs GROWTH CAPEX SPLIT, FY2021-FY2025 - THE HEADLINE FINDING

Required because **[E5-20]** forbids D&A as the maintenance-capex proxy in a capital-intensive
business. The prior question is whether the peer set even permits obedience to that rule.

**Answer: three of five disclose the split. Two do not.**

| Company | Discloses maintenance vs growth capex? | Where | Basis |
|---|---|---|---|
| **Boardwalk** | **YES** - explicit, every year, with a 3-year look-back | MD&A, *Liquidity and Capital Resources -> Capital Expenditures* | Consolidated cash capex. The two lines **sum exactly to cash-flow-statement capex** in FY2023-25 |
| **Kinder Morgan** | **YES** - "sustaining" vs "expansion" | MD&A, *Liquidity -> Capital Expenditures*; also inside the DCF reconciliation | Consolidated from FY2022 on. FY2021 presentation **includes unconsolidated-JV** sustaining capex |
| **Energy Transfer** | **YES** - "Growth / Maintenance / Total", by segment | MD&A, *Liquidity -> Cash Flows -> Investing Activities* | "Capital expenditures **recorded during period**", includes proportionate JV share, so it **does not tie to cash capex** |
| **Williams** | **NO** | - | Discloses only *"growth capital and investment expenditures"* as forward guidance. **No maintenance-capex figure appears anywhere in the FY2025 10-K** |
| **ONEOK** | **NO** | - | The string "maintenance capital" **does not appear in the FY2025 10-K**. Capex is given only as a single total, by segment |

### 1a. The disclosed numbers ($ millions)

| Company | Line | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **Boardwalk** | Maintenance / sustaining | 154.3 | 157.4 | 164.5 | 202.4 | 194.2 |
| | Growth / expansion | 174.9 | 180.2 | 217.9 | 190.0 | 159.7 |
| | *Total capex, cash-flow statement* | *349.2* | *344.3* | *382.4* | *392.4* | *353.9* |
| **Kinder Morgan** | Maintenance / sustaining | 864 | 901 | 868 | 1,009 | 951 |
| | Growth / expansion | 2,278 | n/d | 1,594 | 1,708 | 2,030 |
| | *Total capex, cash-flow statement* | *1,281* | *1,621* | *2,317* | *2,629* | *3,026* |
| **Energy Transfer** | Maintenance / sustaining | 581 | 821 | 857 | 1,162 | 1,316 |
| | Growth / expansion | 1,577 | 2,205 | 2,011 | 3,420 | 5,096 |
| | *Total capex, cash-flow statement* | *2,822* | *3,381* | *3,134* | *4,164* | *6,303* |
| **Williams** | Maintenance | **not disclosed** | **not disclosed** | **not disclosed** | **not disclosed** | **not disclosed** |
| | *Total capex, cash-flow statement* | *1,239* | *2,253* | *2,516* | *2,573* | *4,893* |
| **ONEOK** | Maintenance | **not disclosed** | **not disclosed** | **not disclosed** | **not disclosed** | **not disclosed** |
| | *Total capex, cash-flow statement* | *697* | *1,202* | *1,595* | *2,021* | *3,152* |

**Caveats that must travel with these numbers:**

1. **KMI FY2021 ($864M) is not on the same basis as FY2022-25.** The FY2021 10-K footnote states the
   figure includes *"$107 million ... for sustaining capital expenditures from unconsolidated joint
   ventures, reduced by consolidated joint venture partners' [share]."* On the consolidated-only basis
   used from FY2022 on, FY2021 sustaining capex is approximately **$757M**. The bridge is confirmed:
   the FY2022 10-K reports FY2022 as $901M *including $140M of JV*, and the FY2023 10-K restates the
   same year as **$761M** consolidated-only. 901 - 140 = 761. The correction is arithmetic, not a guess.
2. **ET' table is "recorded during period", not cash paid,** and includes ET' proportionate share of
   JVs. FY2025: growth $5,096M + maintenance $1,316M = $6,412M against cash capex of $6,303M. Use it
   as a *ratio*, never as a cash number.
3. **KMI FY2022 expansion capex is n/d** because that 10-K presents the counterpart line as
   "Discretionary capital investments" on a different, JV- and acquisition-inclusive basis; only the
   sustaining line is comparable. The KMI FY2021 growth figure of $2,278M is that same line and
   **includes $1,538M of acquisitions (Stagecoach, Kinetrex)** - it is not organic growth capex.
4. **BWP' split does not tie to cash capex in FY2021-22** ($329.2M vs $349.2M; $337.6M vs $344.3M).
   It ties exactly in FY2023, FY2024 and FY2025.

### 1b. Maintenance capex as a share of total capex, and against D&A

This is the [E5-20] test. If D&A were an honest maintenance-capex proxy, maintenance/D&A would sit near 1.0.

| Company | Metric | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **Boardwalk** | Maintenance / total capex | 44% | 46% | 43% | 52% | 55% |
| | **Maintenance / D&A** | **0.42** | **0.40** | **0.40** | **0.48** | **0.44** |
| **Kinder Morgan** | Maintenance / total capex | 67% | 56% | 37% | 38% | 31% |
| | **Maintenance / D&A** | **0.40** | **0.41** | **0.39** | **0.43** | **0.39** |
| **Energy Transfer** | Maintenance / total capex | 21% | 24% | 27% | 28% | 21% |
| | **Maintenance / D&A** | **0.15** | **0.20** | **0.20** | **0.22** | **0.23** |

**Reading.** For all three disclosers, maintenance capex runs at **0.15x to 0.48x of D&A**. D&A
overstates true maintenance spend by roughly two to six times. Boardwalk is the *highest* of the
three at 0.40-0.48x - barely ahead of KMI at 0.39-0.43x, and far ahead of ET at 0.15-0.23x - meaning
Boardwalk assets are the most maintenance-hungry relative to book depreciation;
but even at Boardwalk the D&A proxy would overstate maintenance capex by about 2.2x, understating owner
earnings by roughly $245M in FY2025 - a third of reported operating income.

**[E5-20] is vindicated empirically on this peer set: the D&A proxy errs in the same direction, and by
a large factor, for every filer that shows its work.** For Williams and ONEOK, item (b) of owner
earnings cannot be sourced from the 10-K at all. On the framework' own test - *"can I name the document
that would resolve this?"* - the answer for WMB and OKE maintenance capex is **no 10-K document resolves
it**; the split exists only in investor-day decks and non-GAAP supplements outside the citation shelf.
That is an **UNRESEARCHED-to-UNKNOWABLE** boundary case on the peers, not on Boardwalk.

---

## 2. OPERATING REVENUES, OPERATING INCOME, OPERATING MARGIN, FY2021-FY2025

$ millions. Source: XBRL companyfacts, `us-gaap:Revenues` (BWP, WMB, KMI, ET) and
`us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` (OKE FY2023-25, where the `Revenues` tag
was discontinued), with `us-gaap:OperatingIncomeLoss`. 10-K facts only, latest filed value per year.

| Company | Line | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **Boardwalk** | Operating revenues | 1,340.1 | 1,432.0 | 1,617.7 | 2,028.1 | 2,305.8 |
| | Operating income | 467.1 | 499.2 | 526.2 | 657.7 | 739.9 |
| | **Operating margin** | **34.9%** | **34.9%** | **32.5%** | **32.4%** | **32.1%** |
| **Williams** | Operating revenues | 10,627 | 10,965 | 10,907 | 10,503 | 11,950 |
| | Operating income | 2,631 | 3,018 | 4,311 | 3,339 | 4,196 |
| | **Operating margin** | **24.8%** | **27.5%** | **39.5%** | **31.8%** | **35.1%** |
| **Kinder Morgan** | Operating revenues | 16,610 | 19,200 | 15,334 | 15,100 | 16,937 |
| | Operating income | 2,916 | 4,065 | 4,263 | 4,384 | 4,724 |
| | **Operating margin** | **17.6%** | **21.2%** | **27.8%** | **29.0%** | **27.9%** |
| **ONEOK** | Operating revenues | 16,540 | 22,387 | 17,677 | 21,698 | 33,629 |
| | Operating income | 2,596 | 2,807 | 4,072 | 4,989 | 5,741 |
| | **Operating margin** | **15.7%** | **12.5%** | **23.0%** | **23.0%** | **17.1%** |
| **Energy Transfer** | Operating revenues | 67,417 | 89,876 | 78,586 | 82,671 | 85,536 |
| | Operating income | 8,792 | 7,738 | 8,295 | 9,138 | 9,027 |
| | **Operating margin** | **13.0%** | **8.6%** | **10.6%** | **11.1%** | **10.6%** |

### 2a. Operating margin ranking

| Rank by 5-yr mean | Company | FY2021 | FY2025 | 5-yr mean |
|---|---|---|---|---|
| 1 | Boardwalk | 34.9% | 32.1% | **33.4%** |
| 2 | Williams | 24.8% | 35.1% | **31.7%** |
| 3 | Kinder Morgan | 17.6% | 27.9% | **24.7%** |
| 4 | ONEOK | 15.7% | 17.1% | **18.3%** |
| 5 | Energy Transfer | 13.0% | 10.6% | **10.8%** |

**Boardwalk ranks #1 on the 5-year mean operating margin (33.4%) and #1 in three of the five years**
(2021, 2022, 2024). Williams passes it in 2023 and 2025, taking FY2025 by 35.1% to 32.1%. Boardwalk is
#1 or #2 in every year of the window; it is never third.

**The comparison is only half honest, and the reason matters.** ONEOK and Energy Transfer buy and
resell physical commodity; their revenue line is grossed up by product cost that never touches
Boardwalk' income statement. ET' 10.8% mean margin does not mean ET is a worse business than
Boardwalk by a factor of three - it means ET reports $85.5bn of revenue on an asset base only 13x
Boardwalk'. **Operating margin is not comparable across filers with different revenue gross-ups.**
The defensible statement is narrower: *among the three transportation-and-storage-weighted filers
(BWP, WMB, KMI), Boardwalk earns the highest or second-highest operating margin in every year.*
Section 4 is the comparison that survives the gross-up problem, because it puts operating income over
an asset base rather than over revenue.

---

## 3. CAPEX AND D&A, FY2021-FY2025, WITH THE CAPEX/D&A RATIO

$ millions. Capex is `us-gaap:PaymentsToAcquirePropertyPlantAndEquipment`
(`PaymentsToAcquireProductiveAssets` for ET); D&A is `DepreciationDepletionAndAmortization`
(`DepreciationAndAmortization` for BWP and ET). Cash-flow-statement basis, so acquisitions are excluded.

| Company | Line | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **Boardwalk** | Capex | 349.2 | 344.3 | 382.4 | 392.4 | 353.9 |
| | D&A | 366.3 | 392.3 | 408.7 | 424.8 | 438.9 |
| | **Capex / D&A** | **0.95** | **0.88** | **0.94** | **0.92** | **0.81** |
| **Williams** | Capex | 1,239 | 2,253 | 2,516 | 2,573 | 4,893 |
| | D&A | 1,842 | 2,009 | 2,071 | 2,219 | 2,347 |
| | **Capex / D&A** | **0.67** | **1.12** | **1.21** | **1.16** | **2.08** |
| **Kinder Morgan** | Capex | 1,281 | 1,621 | 2,317 | 2,629 | 3,026 |
| | D&A | 2,135 | 2,186 | 2,250 | 2,354 | 2,453 |
| | **Capex / D&A** | **0.60** | **0.74** | **1.03** | **1.12** | **1.23** |
| **ONEOK** | Capex | 697 | 1,202 | 1,595 | 2,021 | 3,152 |
| | D&A | 622 | 626 | 769 | 1,134 | 1,514 |
| | **Capex / D&A** | **1.12** | **1.92** | **2.07** | **1.78** | **2.08** |
| **Energy Transfer** | Capex | 2,822 | 3,381 | 3,134 | 4,164 | 6,303 |
| | D&A | 3,817 | 4,164 | 4,385 | 5,165 | 5,682 |
| | **Capex / D&A** | **0.74** | **0.81** | **0.71** | **0.81** | **1.11** |

### 3a. Capex/D&A, 5-year mean, ranked low to high

| Company | 5-yr mean capex/D&A | Reading |
|---|---|---|
| Energy Transfer | **0.84** | Lowest on the mean, but only because 2021-23 was a pause; rising to 1.11x by 2025 on the Parkland and other build-out. |
| Boardwalk | **0.90** | Second-lowest, and the most stable of the five (0.81x-0.96x, no trend). Boardwalk reinvests barely above the depreciation line - a mature, largely-built system, not an empire under construction. |
| Kinder Morgan | **0.94** | Rising from 0.60x to 1.23x as the backlog rebuilt. |
| Williams | **1.25** | Steeply rising: 0.67x in 2021 to 2.08x in 2025. Transco expansion plus power-demand-driven projects. |
| ONEOK | **1.80** | Highest and rising hard - 1.12x to 2.08x - and that is on top of large acquisitions (Magellan, EnLink, Medallion) which do not appear in this line at all. |

**Note the trap this ratio sets, and why [E5-20] is not optional.** Boardwalk' FY2025 capex/D&A of 0.81x
looks like a business under-investing against depreciation. It is not. Of Boardwalk' $353.9M FY2025
capex, only $194.2M is maintenance - **0.44x of D&A** - and the other $159.7M is discretionary growth
the owner could stop tomorrow. **A reader using D&A as maintenance capex would conclude Boardwalk is
barely self-funding; the disclosed split shows it throws off roughly $245M a year of D&A that is not
a real replacement cost.** The same correction cannot be made for Williams or ONEOK, whose capex/D&A
of 2.08x is uninterpretable without knowing how much of it is discretionary.

---

## 4. RETURN ON UNLEVERAGED NET TANGIBLE OPERATING ASSETS

### Formula

```
RONTOA = Operating income
         / (Total assets - Goodwill - Intangible assets - Non-interest-bearing current liabilities)

where  NIBCL = Total current liabilities - current interest-bearing debt
```

**Line items used, by tag:**

| Component | Tag(s) |
|---|---|
| Operating income | `us-gaap:OperatingIncomeLoss` |
| Total assets | `us-gaap:Assets` |
| Goodwill | `us-gaap:Goodwill` |
| Intangibles | `us-gaap:IntangibleAssetsNetExcludingGoodwill` (KMI, OKE, ET); `us-gaap:FiniteLivedIntangibleAssetsNet` (BWP); **none tagged for WMB** |
| Total current liabilities | `us-gaap:LiabilitiesCurrent` |
| Current interest-bearing debt | BWP `LongTermDebtCurrent`; WMB `LongTermDebtAndCapitalLeaseObligationsCurrent` + `CommercialPaper`; KMI `DebtCurrent`; OKE `LongTermDebtCurrent` + `CommercialPaper`; ET `LongTermDebtCurrent` |

It is **unleveraged** because operating income is struck before interest, and the denominator removes
only non-interest-bearing liabilities - debt-funded assets stay in the base. It is **tangible** because
goodwill and intangibles are removed. This is the comparison that survives the revenue-gross-up problem
in Section 2.

### 4a. The denominator, $ millions

| Company | Component | 2021 | 2025 |
|---|---|---|---|
| **Boardwalk** | Total assets | 9,331.4 | 10,513.4 |
| | less Goodwill | (237.4) | (237.4) |
| | less Intangibles | (42.2) | (65.8) |
| | less NIBCL | (259.7) | (432.2) |
| | **= Net tangible operating assets** | **8,792.1** | **9,778.0** |
| **Williams** | Total assets | 47,612 | 58,573 |
| | less Goodwill | (0) | (466) |
| | less Intangibles | (0) | (0) |
| | less NIBCL | (2,947) | (4,061) |
| | **= Net tangible operating assets** | **44,665** | **54,046** |
| **Kinder Morgan** | Total assets | 70,416 | 72,748 |
| | less Goodwill | (19,914) | (20,084) |
| | less Intangibles | (1,678) | (1,730) |
| | less NIBCL | (3,175) | (3,096) |
| | **= Net tangible operating assets** | **45,649** | **47,838** |
| **ONEOK** | Total assets | 23,622 | 66,641 |
| | less Goodwill | (528) | (8,058) |
| | less Intangibles | (236) | (2,901) |
| | less NIBCL | (2,289) | (4,304) |
| | **= Net tangible operating assets** | **20,570** | **51,378** |
| **Energy Transfer** | Total assets | 105,963 | 141,286 |
| | less Goodwill | (2,533) | (5,452) |
| | less Intangibles | (5,856) | (7,438) |
| | less NIBCL | (10,155) | (14,930) |
| | **= Net tangible operating assets** | **87,419** | **113,466** |

### 4b. RONTOA, all five years

| Company | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr mean |
|---|---|---|---|---|---|---|
| **Boardwalk** | 5.3% | 5.6% | 5.8% | 7.2% | 7.6% | **6.3%** |
| **Williams** | 5.9% | 6.8% | 8.7% | 6.6% | 7.8% | **7.1%** |
| **Kinder Morgan** | 6.4% | 9.1% | 9.3% | 9.4% | 9.9% | **8.8%** |
| **ONEOK** | 12.6% | 13.1% | 11.6% | 10.1% | 11.2% | **11.7%** |
| **Energy Transfer** | 10.1% | 8.9% | 8.9% | 8.9% | 8.0% | **8.9%** |

### 4c. Ranking

| Rank by 5-yr mean | Company | FY2021 | FY2025 | 5-yr mean |
|---|---|---|---|---|
| 1 | ONEOK | 12.6% | 11.2% | **11.7%** |
| 2 | Energy Transfer | 10.1% | 8.0% | **8.9%** |
| 3 | Kinder Morgan | 6.4% | 9.9% | **8.8%** |
| 4 | Williams | 5.9% | 7.8% | **7.1%** |
| 5 | Boardwalk | 5.3% | 7.6% | **6.3%** |

**Boardwalk ranks LAST of the five on the 5-year mean, and last in both FY2021 and FY2025.**
This is the finding that matters, and it points the opposite way from Section 2.

**The two results are not in conflict - they are the same fact stated twice.** Boardwalk earns the
fattest margin *on revenue* and the thinnest return *on assets*, because its asset base per
dollar of revenue is the heaviest in the group:

| Company | Revenue / total assets, FY2025 |
|---|---|
| Williams | 0.20x |
| Boardwalk | 0.22x |
| Kinder Morgan | 0.23x |
| ONEOK | 0.50x |
| Energy Transfer | 0.61x |

A regulated interstate gas pipeline collects a high margin on each dollar of transportation revenue
and needs roughly $4.50 of assets to produce that dollar. **The high margin is not evidence of a moat;
it is the arithmetic consequence of capital intensity, and the FERC rate construct exists precisely to
cap the return that intensity can earn.** Q2 cannot be answered IN on operating margin.

**Three caveats on the RONTOA comparison, stated so the number is not over-read:**

1. **KMI is flattered most by the goodwill deduction.** $20.1bn of goodwill is 27.6% of KMI total
   assets. Removing it lifts KMI FY2025 RONTOA from about 6.5% (on unadjusted assets net of NIBCL) to
   9.9%. Boardwalk carries only $237.4M of goodwill, 2.3% of assets, so the adjustment barely moves it.
   **The metric rewards the filer that has written the most purchase premium off the tangible base.**
2. **Williams has no separately tagged intangibles.** WMB does not present an intangibles line on the
   face of its balance sheet, so intangibles are taken as zero. If WMB carries intangibles inside
   "Regulatory assets, deferred charges and other", WMB' denominator is overstated and its RONTOA is
   **understated**. This is a known, unresolved item - flagged, not smoothed.
3. **OKE 2021 vs 2025 is not like-for-like.** ONEOK acquired Magellan, EnLink and Medallion across
   2023-25; total assets went from $23.6bn to $66.6bn and goodwill from $0.5bn to $8.1bn. Its RONTOA
   fell from 12.6% to 11.2% while it stayed the highest-returning of the five, which is itself the
   interesting fact: gathering-and-processing assets turn over 2.3x faster than pipeline assets.

---

## 5. TOTAL DEBT AND NET DEBT / EBITDA

### 5a. Total debt, $ millions

Total debt = long-term debt and finance-lease obligations (non-current) + current interest-bearing debt.

| Company | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| **Boardwalk** | 3,334.5 | 3,233.4 | 3,261.9 | 3,234.4 | 3,781.4 |
| **Williams** | 23,675 | 22,904 | 26,438 | 26,911 | 29,361 |
| **Kinder Morgan** | 33,320 | 31,788 | 32,116 | 31,890 | 32,003 |
| **ONEOK** | 13,643 | 13,621 | 21,667 | 32,077 | 32,816 |
| **Energy Transfer** | 49,702 | 48,262 | 52,388 | 59,760 | 68,333 |

**Cross-check:** the BWP FY2025 10-K states "Total debt and finance lease obligation $3,781.4" on the
face of the debt footnote. The build above gives $3,231.8 + $549.6 = **$3,781.4**. Ties exactly.

### 5b. Debt against the operating asset base

| Company | Total debt FY2025 | Net tangible operating assets FY2025 | Debt / NTOA |
|---|---|---|---|
| Boardwalk | 3,781.4 | 9,778.0 | **39%** |
| Williams | 29,361 | 54,046 | **54%** |
| Kinder Morgan | 32,003 | 47,838 | **67%** |
| ONEOK | 32,816 | 51,378 | **64%** |
| Energy Transfer | 68,333 | 113,466 | **60%** |

### 5c. Net debt / EBITDA as **stated by the filer**

| Company | Does the 10-K state a net debt / EBITDA ratio? | What the filing gives |
|---|---|---|
| **Boardwalk** | **NO ratio stated.** | The 10-K gives EBITDA (FY2025 $1,182.7M; FY2024 $1,088.6M) with a net-income reconciliation, and total debt of $3,781.4M, but **states no leverage ratio**. Computed: 3,781.4 / 1,182.7 = **3.2x** (gross debt; **this is my arithmetic, not the filer'**) |
| **Kinder Morgan** | **Partially.** KMI defines Net Debt and gives its components | *"based on amounts as of December 31, 2025, by subtracting the following amounts from our debt balance of $32,003 million: (i) cash and cash equivalents of $63 million; (ii) debt fair value adjustments of $180 million; and (iii) the foreign exchange impact on Euro-denominated bonds of $44 million"* -> **Net Debt $31,716M** |
| **Williams** | **NO ratio stated in the 10-K.** | Discusses credit ratings and leverage targets qualitatively only |
| **ONEOK** | **NO ratio stated.** | Notes only that *"The most common criteria for assessment of our credit ratings are the debt-to-EBITDA ratio"* - the criterion is named, the value is not given |
| **Energy Transfer** | **NO ratio stated.** | The Five-Year Credit Facility covenant is described as a rolling-four-quarter leverage limit, but **no computed ratio is disclosed** |

**Finding: four of five filers do not state a net debt / EBITDA figure in the 10-K, and the fifth
states only the numerator.** Any leverage ratio in this row is therefore the analyst' arithmetic and
must be labelled as such. It is not a filed number.

---

## 6. WHAT IS UNOBTAINABLE FROM THE FILINGS

Stated explicitly, per operator rule: these were sought and not found. None are fabricated below.

| Item | Status | Can I name the document that would resolve it? |
|---|---|---|
| WMB maintenance capex, FY2021-25 | **Not in the 10-K** | Not on the citation shelf. WMB splits capex only in investor decks / non-GAAP supplements. **UNRESEARCHED** as to those, **UNKNOWABLE** from filings |
| OKE maintenance capex, FY2021-25 | **Not in the 10-K** | Same. The phrase does not occur in the document |
| KMI expansion capex FY2022 on a comparable basis | Not comparable | The FY2022 10-K uses "Discretionary capital investments", a different basis |
| WMB intangible assets | **Not separately tagged or presented** | Would require reading the "Regulatory assets, deferred charges and other" footnote in detail |
| Net debt / EBITDA, stated | **4 of 5 do not state it** | Investor supplements, off-shelf |
| BWP net debt / EBITDA | **Not stated by BWP** | Computed here at 3.2x gross; labelled as computed |

---

## 7. THE ROW, IN ONE LINE EACH

| Company | Op. margin, 5-yr mean | RONTOA, 5-yr mean | Capex/D&A, 5-yr | Maint. capex disclosed? | Maint./D&A FY2025 |
|---|---|---|---|---|---|
| **Boardwalk** | 33.4% | 6.3% | 0.90 | YES | **0.44** |
| **Williams** | 31.7% | 7.1% | 1.25 | **NO** | n/d |
| **Kinder Morgan** | 24.7% | 8.8% | 0.94 | YES | **0.39** |
| **ONEOK** | 18.3% | 11.7% | 1.80 | **NO** | n/d |
| **Energy Transfer** | 10.8% | 8.9% | 0.84 | YES | **0.23** |

**Verdict on the competitor row as it bears on Q2.** Boardwalk is the highest-margin and the
lowest-returning business in the set. Its margin advantage is a capital-intensity artifact and a
regulated-tariff artifact, not by itself evidence of a franchise. The one place Boardwalk is
genuinely better than the peer group is **disclosure**: it is the only filer of the five that gives a
clean maintenance/growth split that ties to the cash flow statement in the current year, which is
exactly the input [E5-20] requires and exactly the input two of its four peers withhold.

*Sections 0-7 complete. Data: SEC XBRL companyfacts (retrieved 2026-09-02) and the FY2025 10-K text of
each filer, plus KMI FY2021-24 and ET FY2022-23 10-Ks for the maintenance-capex series.*
