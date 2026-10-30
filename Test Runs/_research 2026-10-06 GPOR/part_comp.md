## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict; the balance sheets are read below as the template asks when the file closes before Q4.
## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 — WHAT IS IT WORTH. NOT REACHED as a verdict; the owner's figures are below as COMPUTATION.
## Q8, Q9, Q10, Q12. NOT REACHED.

---
## COMPUTATION — NOT A CLEARANCE
*Written after the file closed OUT at Q2, at the owner's request (value range, a whole-cycle variant, a fair price and a
cheap price) and for the record. Nothing here reopens Q2; none of it is entry language. Arithmetic in
`Test Runs/_research 2026-10-06 GPOR/owner_cash.py`, output in `owner_cash_out.txt`.*

### A. The balance sheets, ten year-ends, before the income account
(USD millions; `tools/run.py` transcription of the first-filed XBRL, checked against the filed statements of equity in the
10-Ks FY2022 and FY2025 for 2020 to 2025: equity -$300.5M at 2020, $639.7M at emergence, $549.5M, $828.8M, $2,161.7M,
$1,711.4M, $1,834.7M, all agreeing.)

| year-end | assets | liabilities | equity | cash | receivables | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|
| 2017 | 5,808 | 2,706 | 3,102 | 100 | 182 | 2,038 | -1,276 |
| 2018 | 6,051 | 2,723 | 3,328 | 52 | 210 | 2,087 | -845 |
| 2019 | 3,883 | 2,568 | 1,315 | 6 | 121 | 1,978 | -2,848 |
| 2020 | 2,540 | 2,840 | -300 | 90 | 120 | 0 (in liabilities subject to compromise) | -4,473 |
| 2021-05-17 (fresh start) | 2,253 | 1,558 | 640 | 2 | 181 | 793 | 0 |
| 2021 | 2,168 | 1,561 | 549 | 3 | 233 | 713 | -113 |
| 2022 | 2,534 | 1,653 | 829 | 7 | 278 | 694 | 382 |
| 2023 | 3,268 | 1,062 | 2,162 | 2 | 122 | 667 | 1,848 |
| 2024 | 2,866 | 1,117 | 1,711 | 1 | 156 | 703 | 1,582 |
| 2025 | 3,030 | 1,195 | 1,835 | 2 | 185 | 788 | 1,835 |

What the figures say. (1) The predecessor's equity went from $3,328M (2018) to -$300M (2020) in two years, by the
$2,040M and $1,357M ceiling-test write-downs, while its debt stayed at about $2.0bn: the assets shrank and the claims did
not. (2) There is no goodwill or intangible in any year; the assets are wells and acreage carried under the full-cost
method, written down to a ceiling set by twelve-month average prices (10-K FY2025, critical accounting policies), so the
book value moves with the gas price. (3) Cash is near zero in every successor year; the company runs on its revolving
credit facility, whose borrowing base is redetermined twice a year "based primarily on projected future cash flows"
(10-K FY2025, MD&A): the lender's switch, held by the lender. (4) The successor's equity jump in 2023 (+$1,333M) is mostly
not cash: net income of $1,471M that year included a $525.2M income tax benefit from releasing the valuation allowance
on the deferred tax asset and $740.3M of derivative gains, much of them unrealized (XBRL `IncomeTaxExpenseBenefit`,
`GainLossOnDerivativeInstrumentsNetPretax`, 10-K FY2025). At the end of 2025 the deferred tax asset is $465.7M of the
$3,030M of assets, resting on a $1.5bn federal net operating loss (10-K FY2025, income-tax note): "what the figures
are saying and what they don’t say and what they can’t say" **[M2025-032]**: they cannot say whether that asset is
realized, which depends on future gas prices. (5) Long-term debt has stayed at $0.67bn to $0.79bn since emergence and rose
to $922.3M at 2026-06-30 (10-Q `0001628280-26-052313`) while the company bought back stock: the buybacks are partly
borrowed. (6) Receivables follow the gas price ($278M at the 2022 peak, $122M in 2023), not sales effort.

### B. Owner cash after every real cost (successor; USD millions)
Operating cash flow less stock pay, less all cash capital spending on oil and gas property (drilling, leasehold and
other), less preferred dividends paid, less the cash paid to settle performance stock units in 2025 (stock pay paid in
cash outside operating cash flow, 10-K FY2025, sources and uses of cash). Interest is inside operating cash flow; cash
income taxes were nil to $1.2M a year (XBRL `IncomeTaxPaidFederalAfterRefundReceived`, `IncomeTaxesPaidNet`), so owner
cash here is effectively pre-tax.

| year | OCF | stock pay | capital | preferred dividends | cash-settled PSUs | **owner cash** | per Mcfe | D&A variant |
|---|---|---|---|---|---|---|---|---|
| 2021 (both stubs) | 465.2 | 3.2 | 309.4 | 1.5 | 0 | **151.1** | 0.41 | 236.8 |
| 2022 | 739.1 | 5.7 | 460.8 | 5.4 | 0 | **267.2** | 0.74 | 460.2 |
| 2023 | 723.2 | 9.5 | 537.4 | 4.8 | 0 | **171.5** | 0.45 | 389.2 |
| 2024 | 650.0 | 11.0 | 454.1 | 4.2 | 0 | **180.7** | 0.47 | 309.1 |
| 2025 | 803.2 | 12.2 | 527.6 | 1.7 | 12.3 | **249.4** | 0.66 | 472.8 |
| five-year mean | | | | | | **204.0** | | 373.6 |

Sources: XBRL facts by period (`facts_table_out.txt`) from the 10-Ks FY2021 to FY2025; preferred dividends from the
cash-flow statements (10-K FY2022 and FY2023: $5.4M, $4.8M; 10-K FY2025: $4.2M, $1.7M; 2021 successor $1.5M); the 2021
predecessor stub includes reorganization cash costs and is flagged. **The maintenance judgment:** production was 1,054,
1,054 and 1,039 MMcfe per day in 2023, 2024 and 2025 (10-K FY2025), so all of the capital in those years was spent to stand
still, and the D&A variant (D&A of $304M to $326M on the fresh-start written-down base) understates the true cost; the
2026 guidance of $400M to $430M for flat production says the same. The all-capital figure is the one used.
The predecessor, same arithmetic (OCF less stock pay less capital): 2014 -928.3, 2015 -1,265.5, 2016 -394.5, 2017 -391.2,
2018 -119.6, 2019 -1.0, 2020 -272.0; **-3,372.1 in total**.

The 2022 gas spike is in the window but barely in the owner cash: realized hedge losses of $2.94 per Mcfe that year (10-K
FY2022) took the realized price including derivatives to $3.55, against $3.13 to $3.64 in the other successor years. The
window's mean realized price including derivatives, $3.34 per Mcfe, sits $0.24 above the 2015 to 2025 mean of $3.10
(own 10-Ks; the 2015 to 2017 prices were reported net of some transport and so understate the gross price).

### C. The value range (Q7 CONVENTION construction), with variants
Sovereign 5.66%; 17.684M shares; price $157.84; market cap $2,791M; net debt $795.2M (year-end 2025).
- **Growth shown and its cap.** Owner cash rose from $151.1M (2021) to $249.4M (2025), 13.3% a year, but the rise is the
  gas price and the emergence-year costs, not the business: production went from 983 to 1,039 MMcfe per day from 2022 to
  2025, 1.86% a year, and fell to 963 in the second quarter of 2026. The high end is capped at the production growth shown
  (CONVENTION of this run: the framework caps growth "by the growth arithmetic of Q3", and Q3 was not reached; a
  price-driven rate cannot be the business's growth). The 13.3% case is shown and not used.
- **The range by the convention** (five-year mean, ten years, then no growth, at 5.66%): **$204 a share (no growth) to
  $236 (1.86%)**, against $157.84. Ratio 1.16 to 1. On the four successor full years (mean $217.2M): $217 to $251.
- **Variant 1, a depleting asset** (CONVENTION of this run: the perpetuity assumes the inventory never runs out; proved
  reserves are 11.2 years of production): the same cash for 11 years then nothing, $93 a share; for 15 years, $115; for 20
  years, $136.
- **Variant 2, whole cycle** (the owner's request): the 2025 cost structure (cash costs $1.25, G&A $0.11, interest $0.14 per
  Mcfe, maintenance capital $1.09 per Mcfe from the 2026 guidance midpoint) at 2025 volume, with the realized price
  including hedges set at the 2015 to 2025 mean of $3.10: owner cash about $193M a year, $193 a share as a perpetuity.
- **Variant 3, the price as the input.** Each $0.10 per Mcfe of realized price is about $38M a year of owner cash and about
  $38 a share of perpetuity value. At the realized prices the company has actually had in its own filings since 2015
  ($2.53 in 2020 to $3.64 in 2025, hedges included), the same arithmetic runs from about **$4 a share at $2.60 to $398 at
  $3.64**: far wider than three to one. Had Q7 been reached, this, not the narrow convention range, is the honest width:
  "Usually, the range must be so wide that no useful conclusion can be reached." **[L2000-025]**; and a wide range is not
  cured by a bigger discount: "we don’t really try to compensate for that sort of thing by having some extra large margin
  of safety" **[M2007-022]**.

### D. The fair price and the cheap price (the owner's request)
- **Expected return at $157.84 on the central case:** owner cash $204.0M on $2,791M = 7.3% pre-tax with no growth, 9.2%
  with the 1.86% production growth. Both below the CONVENTION floor of about ten percent pre-tax ("we don’t want to buy
  equities where our real expectancy is below 10 percent" **[M2003-149]**).
- **FAIR PRICE: about $115 a share** (range $101 to $144). Rule: the price at which the central case (five-year mean owner
  cash, $204.0M, no growth) yields 10% pre-tax on the equity, i.e. after interest: $204.0M / 10% = $2,040M = $115.35 a share.
  Tax: owner cash is after cash taxes, which were nil, so it is pre-tax in practice; the $1.5bn net operating loss shields
  income for some years and is given no extra credit. On equity plus net debt the same floor gives $101 ((204.0 + 54.3
  interest) / 10% - 795.2 net debt); on the four successor full years, $123; with the 1.86% growth as a perpetuity at a 10%
  required return, $144.
- **CHEAP PRICE: about $85 a share.** Rule (CONVENTION of this run): the price below which the buyer gets the wells already
  drilled for less than their value net of all debt and the undeveloped inventory free: the PV-10 of proved developed
  reserves at year-end 2025, $2,291M (10-K FY2025, Item 1, at SEC prices of $3.39 per MMBtu Henry Hub and $66.01 WTI,
  discounted at 10%), less net debt $795.2M, = $1,496M = $84.59 a share. Cross-check: the central owner cash for 11 years
  only (the proved reserve life) at 10% is $1,325M = $75 a share. Below about $75 to $85 no pencil would be needed on
  these figures; at $157.84 the price is 87% above the cheap price and 37% above the fair price.
- None of these figures is an entry signal: the file is closed OUT at Q2, and a lower price does not reopen a castle that
  is not there **[M2019-015]**.

### E. Facts gathered for the questions not reached (record only)
- **Buybacks since emergence** (10-Ks FY2022 to FY2025; 10-Q Q2 2026): 2.9M shares for $250.8M in 2022 (average $86.47);
  1.5M for $148.9M in 2023, $40.4M of it bought from a related party; 1.2M for $184.5M in 2024 ($153.35); 1.8M for $336.3M in
  2025 ($188.65); 8.6M shares for about $1.2bn at an average $135.09 from the start of the program to 2026-06-30, including
  84,416 shares bought from Silver Point Capital on 2026-03-02 for about $17.2M (10-Q, related-party note; a Silver Point
  partner sits on the board, DEF 14A 2026). The program names no price. Shares outstanding: about 21.5M issued at
  emergence (19.8M plus 1.7M to the disputed-claims reserve), 17.68M at 2026-07-28; the preferred converted into at least
  3.6M common shares from 2023 to 2025 (statements of equity, 10-Ks FY2023 and FY2025).
- **Stock pay:** expense $12.2M in 2025, plus $12.3M of 2022 performance units settled in cash; the chief executive's 2025
  total in the summary compensation table $7,323,707 (DEF 14A 2026, `0001213900-26-041489`); the annual incentive scorecard
  includes LOE per Mcfe and "Adjusted Free Cash Flow" targets.
- **Hedging:** about 52% of expected 2026 gas hedged at an average floor of $3.74 per Mcf (10-K FY2025, MD&A); settled
  derivatives added $0.73 per Mcfe in 2024 and took away $2.94 in 2022.
- **Debt and commitments:** $650.0M of 6.75% notes due 2029; revolver $147.0M drawn at year-end 2025, $219.0M at 2026-02-19;
  long-term debt $922.3M at 2026-06-30; firm transportation and gathering $1,037.7M; letters of credit $48.7M and surety bonds
  $45.3M posted "primarily for certain firm transportation agreements" (10-K FY2025).

---
## THE BOX
**OUT, at Q2** (the castle shown open: a commodity seller whose price the market sets, which is not the low-cost producer
on the capital measure the speakers name for this industry; cash margin competitive, capital per unit the highest of six,
the predecessor bankrupt with old equity cancelled). Q7 not reached; for the record only (COMPUTATION): value range by the
convention $204 to $236 a share, honest width with the gas price as the input far wider than three to one; fair about $115;
cheap about $85; price $157.84.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Not committed: the dispatch forbids commits,
      so the write-early rule was kept by writing each part to the file as it closed, not by a commit after each.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, see below); every filing fact carries its
      accession or names its filing; no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the file OUT; nothing after it is a clearance, and the computations are headed so.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: in the foundations (impairments, cash burn,
      the company's own words on price, transport commitments), and in Q2 the evidence for the company (its cash margin
      among the best of six) written down before the evidence against it.
- [x] No row dated after the anchor: not a point-in-time run; the run is dated 2026-10-06 and every row is earlier.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings lines were rejected as reading the wrong
      capital-spending tag (Step 0).
- [x] `python tools/check_framework.py` PASS before closing the file (see the note at the end).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Where a commodity price goes: Q1 or Q2.** Q1's test 4 ("If something’s important but unknowable, forget it."
   **[M2006-076]**) and test 2 ("If something is not very predictable, forget it." **[M1998-044]**) would close every
   commodity producer at Q1, TOO HARD (NATURE), because the price is the key variable and the speakers say no one can
   forecast it **[M2011-047]**. But Q2 has a full section on "The commodity business and its one exception", which assumes
   commodity businesses reach Q2, and the speakers bought producers without a price view **[M2007-129]**, **[M2004-082]**.
   The framework does not say which governs. I passed Q1 and decided at Q2; a second analyst could close the same name at
   Q1 TOO HARD (NATURE) with equal textual support, and the box would differ (OUT against TOO HARD). A one-line routing rule
   is wanted: whether an unforecastable output price is a Q1 matter or is carried to Q2 and Q7.
2. **"The low-cost producer" has no stated measure.** Q2 names the low-cost position as the exception but not what cost:
   cash operating cost, cost including capital, or finding cost. Here the answer turns on it: Gulfport is first or second of
   six on cash margin and last on capital per unit. I used the speakers' own industry-specific figure, finding cost
   **[M2007-082]**, through the capital-per-unit proxy, because the full-cost method's DD&A on a fresh-start base does not
   show finding cost. The framework should say which cost the exception means, or that it means all-in cost.
3. **The Q7 convention's perpetuity misfits a depleting asset.** "Ten years then no real growth" assumes the cash never
   ends; for a producer with 11 years of proved reserves the convention gives $204 a share and the reserve-life variant $93.
   The convention also lets the five-year mean of a commodity price stand in for the future; the range it produces (1.16 to
   1) looks narrow only because the price is held fixed. The three-to-one width test cannot fire unless the analyst varies
   the price, which the convention does not ask for.
4. **The growth cap points to a question that was not reached.** The convention caps growth "by the growth arithmetic of
   Q3"; when a file closes before Q3 and the owner still wants a range, nothing says what cap to use. I capped at the
   production growth shown and said so.
5. **The template's write-early rule assumes commits.** This dispatch forbade commits; the self-audit's first box cannot be
   ticked as written. Recorded rather than ticked silently.
