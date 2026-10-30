# Company Run — The Travelers Companies, Inc. (NYSE: TRV) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`), with `Framework/SECTOR METHOD v5 - insurers and float companies.md`
governing (TRV is a property-casualty insurer). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, holding
reviews, the session-state files, the register, the prepped reading list and `tools/alerts.json` were not opened, and
no earlier TRV run or research folder was opened.

**CONTAMINATION, declared.** (1) A directory listing of `Test Runs/` showed the file names of the 2026-10-05 v5 runs
(none is an insurer and none was opened for this name; the HUBB run was opened for form only, its header and Step 0).
(2) The analyst knows Travelers in general terms from training (a large US commercial and personal lines insurer that
sells through independent agents, and an agreed sale of its Canadian business). That memory is a prior; every fact
below is from the filings cited. (3) No other contamination noticed.

Working folder: `Test Runs/_research 2026-10-06 TRV/` (`fetch.py`, `h2t.py`, `listfilings.py` and the arithmetic
scripts; raw filings in its gitignored `cache/` subfolder).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$360.70** (close 2026-10-05; Yahoo chart via `tools/sources.py` `price()`, an aggregator, live quote only,
  flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock without par value, **208,575,022**
  outstanding at July 10, 2026 (Form 10-Q for the quarter to 2026-06-30, filed 2026-07-17, accession
  `0000086312-26-000145`). `python Screens/cover_shares.py TRV` found the filing but printed "NO COVER SHARE COUNT PARSED -
  read the filing by hand" (tool defect noted below); the count was read by hand from the cover. The balance sheet of the
  same 10-Q shows 208.6 million shares issued and outstanding at June 30, 2026, which agrees.
- **Market cap:** 208,575,022 x $360.70 = **$75,233M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, dated
  10/05/2026 (`python tools/sources.py`, issuing authority). TRV earned almost wholly in dollars after the sale of its
  Canadian business on January 2, 2026 (10-Q `0000086312-26-000145`, note on the divestiture); the remaining UK, Ireland,
  Lloyd's and Brazil operations change reported lines "by insignificant amounts" (same 10-Q, foreign currency paragraph).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-12, `0000086312-26-000065`): Item 1, Item 1A, Item 5,
  Item 7, the statements and the notes named at each question; 10-Q Q2 2026 (filed 2026-07-17, `0000086312-26-000145`):
  balance sheet, equity statement, cash flow, divestiture note, share repurchases, liquidity; DEF 14A filed 2026-04-07
  (`0000086312-26-000103`); 8-K of 2026-07-17 (`0000086312-26-000143`) with Exhibit 99.1 (the Q2 2026 earnings release)
  and Exhibit 99.2 (the financial supplement). Further filings are named where they are used.
- **One figure cross-checked against the filed statement:** net income FY2025 **$6,288M** in the filed Consolidated
  Statement of Income (10-K FY2025, `0000086312-26-000065`) against the XBRL company-facts series (NetIncomeLoss,
  2025-12-31, 6,288,000,000): they agree. Also net cash from operating activities FY2025 $10,606M in the filed cash-flow
  statement against XBRL 10,606,000,000: they agree.
- **`python tools/run.py TRV`, arithmetic lines only:** it printed one line, "TRV: no overlapping OCF/D&A/capex annual
  facts. UNRESEARCHED." (saved as `run_py_output.txt`). An insurer files no capital-expenditure tag, so the tool computes
  nothing for TRV. Under the sector method the operating cash flow is not the insurer's cash figure in any case (its
  float growth is funding, not earnings, **[L1996-008]**, **[M2023-004]**); the cash figure is built at Q4 from the filed
  statements by the sector method's steps, not by the tool.
- **Balance sheet at June 30, 2026** (10-Q `0000086312-26-000145`, USD millions): total investments 103,179; claims and
  claim adjustment expense reserves 67,226; unearned premium reserves 23,327; reinsurance recoverables 8,009; ceded
  unearned premiums 1,674; debt 9,068; shareholders' equity 33,121 (book value **$158.80** a share on 208.575M shares;
  the price is 2.27 times book).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety: an insurer's earnings are "a self-graded exam"
**[L2001-022]**, so the price must sit so far below value that "it ought to just kind of scream at you" **[M1996-084]**,
and "the more volatile the business is [...] the larger the margin of safety" **[M1997-080]**. Second, who is paid to tell
you: the company's headline figures are "core income" and an "underlying combined ratio" that leaves out catastrophes
and prior-year reserve development (Exhibit 99.1, `0000086312-26-000143`), and the rows warn that excluding catastrophe
losses from "true" earnings "is deceptive nonsense" **[L2002-002]**; that is weighed at Q4, not here. Third, a share is a
business: the question is whether I would be content to own TRV "if the market closed for five years" **[M1997-109]**,
judged on what the business earns and not on the 2026 rise in the quotation (the company itself bought stock at an
average $301.86 in the first half of 2026, 10-Q `0000086312-26-000145`, note 10, against $360.70 today), since
appreciation "is never a reason to buy it" **[L2013-007]**. No macro forecast enters **[M2000-094]**: the 2026 fall in
catastrophe losses is weather, and is read at Q4 as one year, not as a trend. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the price has run well above where the company itself was buying five months ago; (2) the filer's
headline figures leave out catastrophes and reserve releases; (3) the 2025 and first-half-2026 results are the best in
the ten years of the XBRL series (net income 6,288 in 2025 against 2,056 to 3,692 in 2014 to 2023), so any average that
leans on the latest years leans on a peak (**[L1994-009]**, "a cyclical peak in earnings").

## THE STANDING RULE
Buying TRV for cash, unlevered and sized so that a fall of half or more can be sat through, puts the buyer at no risk
of ruin: "you don’t want to put yourself in a position where you have to sell" **[M2020-007]**, and borrowed money "has
no place in the investor's tool kit" **[L2014-005]**. Nothing about the target changes this; the target's own exposures
(catastrophes, reserves, reinsurers) are Q9's subject, not the buyer's conduct. **The rule is met.**

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**Stage zero of the sector method (split, float, two ratios).**
1. **Split.** TRV reports three segments, Business Insurance, Bond & Specialty Insurance and Personal Insurance, plus
   Corporate (10-K FY2025 `0000086312-26-000065`, Item 1). All three are property-casualty insurance; there is no
   non-insurance segment with its own balance sheet, no finance operation, and accident-and-health reserves of $3M
   (note 8). So the method applies to the whole company (CONVENTION C9, **[L2008-005]**), and no part is a life or
   annuity book with cash-out features (C10, **[L2013-003]**, **[L2014-024]**).
2. **Float** (A2, "the funds prepaid by policyholders and the funds earmarked for incurred-but-not-yet-paid claims"
   **[L1993-009]**, net of the part ceded): claims reserves + unearned premiums − reinsurance recoverables − ceded unearned
   premiums. At December 31, 2025: 65,737 + 22,431 − 7,886 − 1,283 = **$78,999M**; at June 30, 2026 (10-Q
   `0000086312-26-000145`): 67,226 + 23,327 − 8,009 − 1,674 = **$80,870M**. The balance-sheet recoverable used includes
   $89M recoverable on paid losses (note 8 gives $7,797M on unpaid losses at year-end 2025), a difference of 0.1% of
   float, kept as filed. The first construction's further deductions (premiums receivable 10,992 and deferred acquisition
   costs 3,518) would give $64,489M; whether they survive A2 is an open item of the method, and both are shown. TRV
   publishes no float figure of its own (no instance of the word "float" in the FY2025 10-K text), so there is nothing to
   reconcile to. Arithmetic: `uw_float.py`, output `uw_float_out.txt` (XBRL series, cross-checked to the filed balance
   sheet for 2024 and 2025).
3. **The two ratios** (CONVENTION C2, no threshold): float to investments **0.78** and investments to equity **3.08**
   at year-end 2025 (investments 101,182, equity 32,894). Across 2015 to 2025 the first ran 0.72 to 0.84 and the second
   2.89 to 3.73. About three-quarters of the portfolio is funded by money that is not the owners' **[L1995-015]**, and
   the owners' equity is about a third of the assets it stands behind; the rows let float be treated as near-equity only
   where there is "so much equity" **[M2001-053]**, and Berkshire says "no other insurance company could do it"
   **[M2023-012]**. So the answer will lie mostly in the underwriting and in the equity-funded part of the portfolio.

**The test, applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years" **[M2012-065]**; for an insurer, both sides of the balance sheet must be readable
(CONVENTION C8), and the reserve is "the biggest single element that is very difficult to evaluate, even if you own the
company" **[M2005-067]**.
- **The asset side reads.** Fixed maturities $89,833M of $101,182M investments, of which municipal obligations $31,378M
  rated Aaa/Aa1 on average, corporates and other $41,054M, mortgage-backed $13,232M, US government $3,857M; below
  investment grade 1.2% of fixed maturities (10-K FY2025, Item 7, Investment Portfolio). Equity securities are $618M.
  No derivatives book, no finance arm. Nothing here is a black box.
- **The liability side reads, with one opaque corner.** The 10-K publishes ten-year accident-year development tables
  (undiscounted, net of reinsurance) for the products holding $51,130M of the $59,846M net reserves (note 8), and the
  roll-forward gives the prior-year change every year. Read in full (`devtables.py`, `devtables_out.txt`; FY2025 10-K
  and, for the short-tail lines' 2016 to 2020 accident years, FY2020 10-K `0000086312-21-000011`): the prior-year change
  was favorable in nine of the ten years 2016 to 2025 (roll-forward; 2019 the exception, +$164M including accretion,
  10-K FY2021 `0000086312-22-000013`), and summed over the tables each accident year 2016 to 2024 except 2019 has
  developed favorably since first booked. **Contrary evidence, written down as found** **[M1997-127]**: the Business
  Insurance general-liability table has developed **adversely in every accident year 2016 to 2023** (+$103M to +$351M
  each; AY2018 from $1,253M first booked to $1,604M today, +28%), commercial automobile adverse in seven of the nine
  accident years 2016 to 2024 and commercial multi-peril mixed; the favorable total is carried by workers' compensation
  (−$2M to −$676M in every accident year 2016 to 2024) and personal lines. And asbestos was added to every year: $284M (2023), $242M (2024), $277M (2025), net asbestos reserves $1.36B
  (note 8; Item 7, Asbestos Claims and Litigation). This is the long tail of **[M1999-098]**, "big and they can come
  late", and of **[M2005-069]**: "your statistics are much more valid in something like that than they will be if you’re
  taking something that — like asbestos". It is a minority of the book (Business Insurance general liability $11,942M
  net, 20% of net reserves), and its direction can be read from the tables, which is the point of C8.
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) price against loss-cost trend, readable
  each year in the filer's renewal premium change and loss ratios; (2) catastrophe losses ($2.99B, $3.34B, $3.69B in
  2023 to 2025, 10-K FY2025 Item 7), unpredictable by year but bounded by the reinsurance program and visible in a
  ten-year average; (3) reserve adequacy, readable in direction from the tables; (4) the yield on about $100B of
  bonds, which follows rates and is not forecast here **[M2000-094]**. Do the past statements tell me the future ones
  **[M2008-033]**? For a commercial and personal lines writer in a slow-changing industry, yes in kind: "your statistics
  are much more valid" for the repetitive lines **[M2005-069]**. The insiders do write their forecast down: the reserve
  tables are that forecast, published every year **[M2000-105]**. The industry is not a fast-changing technology field;
  the CEO's claim to "differentiating technology, including AI" (Exhibit 99.1, `0000086312-26-000143`) is a label on an
  insurance company, not a change in what it is **[M2022-077]**.

**VERDICT: IN.** Both sides of the balance sheet can be read from the filings (C8): the portfolio is plain bonds, and
the reserves come with ten years of accident-year history that has been read and shows a favorable aggregate with an
adverse general-liability and asbestos corner. The doubt that would put it outside **[M2002-092]** is that corner; it is
important and knowable in direction **[M2006-076]**, it is about a fifth of the reserves, and it is carried forward to Q4
and Q9 rather than treated as the whole.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question for an insurer is harder, not easier: "Insurers sell a non-proprietary piece of paper containing a
non-proprietary promise. [...] The critical variables, therefore, are managerial brains, discipline and integrity."
**[L2003-014]**; "most insureds don't care from whom they buy" **[L2004-003]**; "Average is going be terrible in insurance
over time" **[M2000-072]**. The evidence the sector method accepts is a cost of float kept low over years **[L2001-006]**,
**[M1996-023]**, prices below competitors' with an underwriting profit **[M2013-006]**, or a franchise of the kinds the rows
name **[M1999-112]**, **[M1996-088]**, read against the commodity character of the product.

**The main exhibit: the cost of float, by year, calendar and accident-year developed** (`uw_float.py`,
`uw_float_out.txt`; pre-tax, USD millions; calendar underwriting = earned premiums x (1 − the filer's combined ratio);
accident-year developed = the calendar figure with the prior-year change taken out and the later development of that
accident year from the tables put in, CONVENTION A3; float = the A2 average of opening and closing; a negative cost is a
profit):

| year | earned premiums | combined ratio | calendar UW | AY developed UW | avg float | cost, calendar | cost, AY | 30-yr Treasury |
|---|---|---|---|---|---|---|---|---|
| 2016 | 24,534 | 92.0% | 1,963 | 1,889 | 51,051 | −3.84% | −3.70% | 2.59% |
| 2017 | 25,683 | 97.9% | 539 | 570 | 52,554 | −1.03% | −1.09% | 2.89% |
| 2018 | 27,059 | 96.9% | 839 | 551 | 54,490 | −1.54% | −1.01% | 3.11% |
| 2019 | 28,272 | 96.5% | 990 | 896 | 56,402 | −1.75% | −1.59% | 2.58% |
| 2020 | 29,044 | 95.0% | 1,452 | 1,852 | 59,075 | −2.46% | −3.14% | 1.56% |
| 2021 | 30,855 | 94.5% | 1,697 | 1,818 | 62,322 | −2.72% | −2.92% | 2.06% |
| 2022 | 33,763 | 95.6% | 1,486 | 1,027 | 65,912 | −2.25% | −1.56% | 3.11% |
| 2023 | 37,761 | 97.0% | 1,133 | 1,312 | 70,504 | −1.61% | −1.86% | 4.09% |
| 2024 (immature) | 41,941 | 92.5% | 3,146 | 3,120 | 75,193 | −4.18% | −4.15% | 4.41% |
| 2025 (immature) | 43,914 | 89.9% | 4,435 | 3,496 | 78,090 | −5.68% | −4.48% | 4.78% |

Sources: premiums and combined ratios from the 10-Ks FY2018 (`0000086312-19-000009`), FY2021 (`0000086312-22-000013`),
FY2024 (`0000086312-25-000012`) and FY2025 (`0000086312-26-000065`); 30-year rates are annual averages of the US Treasury
daily par curve (`treasury30.py`). Averages: 2016 to 2020, AY cost **−2.10%** against a 30-year rate of 2.55%; 2021 to
2025, **−3.06%** against 3.69%; mature accident years 2016 to 2023, **−2.10%** against 2.75%. Underwriting profit in
every one of ten years, on both bases, in both halves of the window, through catastrophe years of $2.99B to $3.69B
(2023 to 2025). Read as the rows read it: float that costs less than nothing is the opposite of "a lemon" **[L1997-011]**,
and "very few" property-casualty companies "stack up" on this test **[L2001-006]**. Caveats, written down as found
**[M1997-127]**: the accident-year table coverage is 85% of net reserves; the short-tail lines' 2016 to 2020 accident
years carry development only to 2020 (FY2020 10-K), and AY2020's short-tail development is not shown at all; asbestos
and other pre-2016 accident years fall outside the accident-year window by construction although they cost $242M to $284M
a year in 2023 to 2025 (the calendar column carries them, and is the lower figure in four of the eight mature years).

**The competitor row** (combined ratio as filed, the competitors' own 10-Ks; lower is better):

| company, figure | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|---|
| **TRV**, consolidated | 95.0 | 94.5 | 95.6 | 97.0 | 92.5 | 89.9 | **94.1** |
| Chubb (CB), P&C combined ratio, 10-K FY2022 `0000896159-23-000007`, FY2025 `0000896159-26-000005` | 96.1 | 89.1 | 87.6 | 86.5 | 86.6 | 85.7 | **88.6** |
| W. R. Berkley (WRB), total, 10-K FY2022 `0000011544-23-000004`, FY2025 `0000011544-26-000005` | 94.9 | 89.6 | 89.3 | 89.7 | 90.3 | 90.7 | **90.8** |
| The Hartford (HIG), Commercial Lines / Business Insurance, 10-K FY2022 `0000874766-23-000023`, FY2025 `0000874766-26-000012` | 100.4 | 95.8 | 90.2 | 89.6 | 89.9 | 88.3 | **92.4** |
| CNA, Commercial segment, 10-K FY2022 `0000021175-23-000006`, FY2025 `0000021175-26-000011` | n/s | 103.1 | 97.3 | n/s | 96.7 | 95.2 | **98.1** (4 yrs) |

(n/s: not shown in the two filings read; Progressive's 10-K carries its ratios in an incorporated annual-report exhibit
that was not fetched, so the personal-auto low-cost comparison is not made from a filing.)

**The castle tests, each with its filing fact.**
- **Low-cost position** **[L2004-007]**, **[L2000-017]**: **not shown.** TRV's underwriting expense ratio was 28.5% in
  2024 and 2025 (10-K FY2025); it sells through independent agents and brokers (Item 1), the channel the rows describe as
  "so ingrained in the business of these insurers that it was impossible for them to give it up" **[L1995-011]**. Its
  combined ratio over 2020 to 2025 averaged 94.1, above Chubb (88.6), Berkley (90.8) and Hartford's commercial book (92.4),
  below CNA Commercial (98.1). It is not the low-cost operator in its row, and "You have to be in the top 10 percent,
  really, to do at all well in it" **[M2012-059]**: on this row it is not top of its class. **Contrary evidence** **[M1997-127]**.
- **Would the customer still choose it over the low bid; pricing power** **[M2000-031]**, **[M2005-020]**: Business
  Insurance retention "remained very strong at 86%" with renewal premium change of 4.8% in Q2 2026 (Exhibit 99.1,
  `0000086312-26-000143`), and in every Business Insurance unit in 2025 "Retention rates remained strong" while "Renewal
  premium changes [...] remained positive" (10-K FY2025, Item 7). Customers stay while price rises. The same is reported by
  Hartford (policy-count retention 84%, renewal written price increases 5.5% to 6.5%, 10-K FY2022): it is a market fact
  as much as a TRV fact. Weak evidence of a castle; good evidence of discipline.
- **The attacker with money** **[M2011-015]**: "Anybody can generate float" **[M2001-030]**; the rows name no barrier in an
  insurer but "managerial brains, discipline and integrity" **[L2003-014]**. A well-funded entrant could write the same
  policies through the same agents; what it could not copy quickly is a ten-year record of underwriting profit on a
  $44B premium base. The castle is a discipline, not a structure.
- **Would it stand without the lord** **[L2007-006]**, **[M1995-038]**: the whole 2016 to 2025 record falls under one
  chief executive, Alan Schnitzer (Chairman and CEO, Exhibit 99.1); the record is institutional in its breadth (three
  segments, combined ratios 91.7, 81.9 and 89.5 in 2025, 10-K FY2025 Item 7) but the evidence of succession is not
  inside the window. **Contrary evidence** **[M1997-127]**: Personal Insurance ran a combined ratio of 104.8 and a
  segment loss of $128M in 2023 (same table), so the record is a consolidated one, not one in every line every year.
- **Widening or narrowing** **[M1999-108]**, **[L2005-010]**: the cost of float was lower in the second half (−3.06%) than
  the first (−2.10%), but the second half includes the hard-market years 2024 to 2025 that every peer shared (the
  competitor row improves in the same years). Not shown to be widening relative to the row.
- **What could destroy or reduce it** **[M2000-014]**: social inflation in general liability (adverse in every accident
  year 2016 to 2023, Q1), catastrophe severity, and a soft market; none is a shown collapse.

**VERDICT: IN, marginally.** The castle is the one the rows allow an insurer, "underwriting discipline" **[L2001-006]**:
float at a negative cost in every year of a ten-year window, in both halves, on developed figures, while "very few stack
up". It is not a structural moat: TRV is neither the low-cost operator nor the best underwriter in its competitor row
**[M2012-059]**, and the moat is "managerial brains, discipline and integrity" **[L2003-014]**. The castle is not shown
open (no filling-in on the evidence), and its future can be judged from ten years of filed results, so neither OUT nor
TOO HARD is the honest box. The narrowness is carried forward: "the more volatile the business is [...] the larger the
margin of safety" **[M1997-080]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
For an insurer there is no maintenance capital expenditure to estimate; the capital that must go in is the capital
that stands behind the promises **[M2025-049]**, **[M2020-041]**, and its return is read by the three items of
**[L1995-015]**: what the assets earn, what the liabilities cost, and the leverage.
1. **The capital behind the promises** (CONVENTION C2, stated, no threshold): shareholders' equity to net written
   premiums **0.74** in 2025 (32,894 / 44,387) against **0.93** in 2016 (23,221 / 24,958) (XBRL, cross-checked to the
   FY2025 10-K premium table and balance sheet). Premiums grew 78% over the nine years and equity 42%; the capital per
   dollar of premium fell while the company bought back stock, so capital did **not** grow faster than the business could
   use it, the case **[M1995-069]** warns of. The company states the rule it runs by: "the combination of dividends to
   common shareholders and common share repurchases will likely not exceed net income", and "in periods of growing premium
   volumes, the level of capital to support the Company’s financial strength ratings will also increase" (10-Q
   `0000086312-26-000145`, Capital Position).
2. **The three items.** Assets: net investment income $3,959M on average investments of $97.7B in 2025, **4.05%**
   pre-tax (3.53% in 2021). Liabilities: the float cost less than nothing in every year 2016 to 2025 (Q2); the debt,
   $9,267M at year-end 2025, cost $425M of interest, about **4.9%**. Leverage: investments **3.08** times equity. Return on
   average equity: 12.6%, 11.3%, 12.9%, 18.9%, 20.7% in 2021 to 2025, **15.5%** over the five years (net income over
   average equity, XBRL). Read with care **[L1994-009]**: 2024 and 2025 are the best years of the decade (combined
   ratios 92.5 and 89.9, Q2), and 2022 and 2023 were flattered by equity shrunk by unrealized bond losses ($21.6B at
   year-end 2022 against $28.9B a year earlier), a return on equity made by a smaller denominator **[M1998-017]**. The
   return rests on leverage of about three to one, which is the insurer's model and is read as such **[M2001-054]**,
   **[M1994-019]**.
3. **Growth and its cost.** More premium needs more capital behind it (point 1, the filer's own words), so growth is not
   free: it is the second kind of business, "It takes more money, but the rate at which you invest — reinvest — the money
   to get that growth is a very satisfactory rate" **[M1998-081]**, provided the underwriting stays profitable; growth at
   a loss is the "curse" **[L1998-016]**. GEICO's rule applies: "not a business where, if you double the capital, you can
   double the earnings easily" **[M1995-069]**.
- **WEIGHS FOR, modestly.** A mid-teens return on equity over five years, earned with an underwriting profit on top of
  the investment income rather than in spite of an underwriting loss, and capital returned rather than piled up
  **[L2009-012]**, **[M1998-081]**; tempered by the peak years in the average and a return that leans on three-to-one
  leverage of other people's money.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, eleven of them, before the income account** **[M2025-032]** (`comp.py`, `comp_out.txt`;
XBRL series, the 2024 and 2025 columns checked against the filed balance sheet in the FY2025 10-K; USD millions):

| year-end | investments | claims reserves | unearned premiums | premiums receivable | debt | goodwill | AOCI | equity | equity ex-AOCI | receivables / NWP |
|---|---|---|---|---|---|---|---|---|---|---|
| 2015 | 70,470 | 48,295 | 11,971 | 6,437 | 6,344 | 3,573 | −157 | 23,598 | 23,755 | 0.267 |
| 2017 | 72,502 | 49,650 | 12,915 | 7,144 | 6,571 | 3,951 | −343 | 23,731 | 24,074 | 0.272 |
| 2019 | 77,884 | 51,849 | 14,604 | 7,909 | 6,558 | 3,961 | 640 | 25,943 | 25,303 | 0.271 |
| 2021 | 87,375 | 56,907 | 16,469 | 8,085 | 7,290 | 4,008 | 1,193 | 28,887 | 27,694 | 0.253 |
| 2022 | 80,454 | 58,649 | 18,240 | 8,922 | 7,292 | 3,952 | −6,445 | 21,560 | 28,005 | 0.252 |
| 2023 | 88,810 | 61,627 | 20,872 | 10,282 | 8,031 | 3,976 | −4,471 | 24,921 | 29,392 | 0.256 |
| 2024 | 94,223 | 64,093 | 22,289 | 11,110 | 8,033 | 4,233 | −4,967 | 27,864 | 32,831 | 0.256 |
| 2025 | 101,182 | 65,737 | 22,431 | 10,992 | 9,267 | 4,066 | −2,500 | 32,894 | 35,394 | 0.248 |

(The even years 2016, 2018 and 2020 are in `comp_out.txt` and say the same.) **What moved and why.** Investments grew 44%
and reserves 36% over ten years while unearned premiums grew 87%, the trace of rising rates on renewal (Q2); premiums
receivable held at a quarter of net written premiums throughout (0.248 to 0.272), so no receivable is building against
sales, the tell **[M1995-064]** names; goodwill is flat at about $4B, an eighth of equity, so the equity is mostly
tangible; equity excluding the bond marks' swing (AOCI) rose every year from $23.8B to $35.4B while $16.3B of stock was
bought back over 2016 to 2025 (XBRL repurchase payments, 2,400 in 2016 to 3,004 in 2025), and the GAAP equity line
fell 25% in 2022 on unrealized bond losses that the ex-AOCI column shows were not operating losses; debt rose from $6.3B
to $9.3B, with $1,233M issued in 2025, the same year $3,004M of stock was bought (cash-flow statement, 10-K FY2025).
What the figures cannot say **[M2025-032]**: whether the reserves are right; that is read below and at Q1.

**The cash figure, by the sector method (Q4 steps 1 to 5).**
1. **Operating cash flow is not the insurer's cash figure.** It ran $10,606M in 2025 against net income of $6,288M
   (filed cash-flow statement), the difference carried largely by reserve growth of $3,300M and unearned premium growth
   of $584M: funding, not earnings **[L1996-008]**, **[M2023-004]**.
2. **Investment income comes out** **[L1998-002]**, **[M1997-141]**: component 2 = income before tax − net investment
   income − realized gains and losses (2025: 7,796 − 3,959 + 48 = **3,885** pre-tax). Net income swung by securities
   gains is ignored **[L2010-017]**.
3. **Underwriting on developed accident-year figures, with the operating-income trap removed** (A3, A5): the calendar
   underwriting result inside component 2 is taken out and the accident-year developed result put in, line by line in
   `comp_out.txt` (2025: 3,885 − 4,435 calendar + 3,496 accident-year = **2,946**). The items left after underwriting
   (fee and other income less interest, corporate costs and the expenses outside the combined ratio) ran −$280M to
   −$579M a year.
4. **Catastrophes stay in** **[L2002-002]**, **[M2018-024]**: every figure above carries them ($2.99B to $3.69B a year in
   2023 to 2025).
5. **Component 2 by year, pre-tax, accident-year basis:** 1,609; 148; 85; 463; 1,408; 1,375; 537; 733; 2,594 (immature);
   2,946 (immature), for 2016 to 2025. **Five-year mean 2021 to 2025: $1,637M pre-tax** (calendar basis $1,862M); after
   tax at the filer's effective rate over those years, 17.4% (sum of tax over sum of pre-tax income, CONVENTION A4),
   **$1,352M**. The accident-year basis is the lower: the development recognized in 2017 to 2025 on accident years before
   2016 and on lines outside the tables, asbestos included, netted to about $469M favorable over the nine years (calendar
   prior-year changes, −3,513, less the tables' development of AY2016 to AY2024, −3,044), so excluding it costs the
   calendar figure, not the accident-year one. Ten-year mean on the same basis $1,190M; mature years 2016 to 2023 $795M.
   **Contrary evidence** **[M1997-127]**: the five-year mean leans on 2024 and 2025, two immature accident years at the top
   of the cycle **[L1994-009]**, **[L2005-003]**; 2017 and 2018 show what a heavy catastrophe year does (component 2 of
   $148M and $85M).

**The real costs.** Stock pay is expensed: compensation amortization under share-based plans $256M, $260M, $216M in
2025 to 2023 (equity statement, 10-K FY2025), inside general and administrative expenses and so inside the combined
ratio **[L2021-003]**, **[L2015-003]**. Depreciation and amortization $680M in 2025 is likewise inside the expenses; there
is no plant whose upkeep it understates. No restructuring charge recurs (no instance of "restructuring" as a charge in
the FY2025 10-K text). No EBITDA anywhere (no instance in the 10-K, the release or the proxy) **[M2002-026]**.

**The candor reading of the reserves** (sector method, Q4 step 6). Direction across the window: favorable in nine of ten
calendar years, $406M to $939M a year in seven of them, against underwriting results of $539M to $4,435M (Q2), so releases
were a large part of the reported underwriting profit in several years (2017: $458M of $539M). The filer calls it "net
favorable prior year reserve development", not an error, though by **[L2001-021]** it is "an error in the earnings
previously reported" — here an error on the side of caution, the opposite of "The natural tendency of most
casualty-insurance managers is to underreserve" **[L2002-006]**. Tells looked for: (1) **reserves that move with a sale or
purchase of stock** **[M2013-085]**: the company buys stock every year; the row's pattern for a buyer is reserves being
built, and the releases here grew in the very years of the largest buybacks (2025: $939M; first half of 2026: $991M,
10-Q `0000086312-26-000145`, with $3.10B of stock bought) — **contrary evidence** **[M1997-127]**, though the tables show
the earlier reserves really did run off favorably; (2) **reserves reset at an acquisition** **[L1998-034]**: none material
(the one 2024 acquisition was $382M cash); (3) **discounting** **[M2003-103]**, **[L2001-024]**: present, on long-term
disability and annuity claims in workers' compensation, $1.03B of discount, the reserves standing at $2.61B net of it, at rates of 3.5%
to 5.0% in both 2024 and 2025 (note 8), the discount about 1.7% of net reserves; disclosed and stable, not the quick fix of the row,
but a tell of the kind named; (4) **published targets** **[M2005-036]**: the proxy (`0000086312-26-000103`) sets a
2025 core return on equity target of 15.0% and pays on it, though the plan "did not budget for any prior year reserve
development, positive or negative"; (5) **adjusted figures featured** **[L2016-006]**: the release's headline bullets carry
"Underlying underwriting income" and an "underlying combined ratio" that leave out catastrophes and reserve development,
beside the all-in combined ratio and the catastrophe losses in dollars (Exhibit 99.1, `0000086312-26-000143`); and pay is
measured on an "Adjusted Core Income" that removes actual catastrophes but charges a fixed "normal" amount ($2.45 billion
for 2025) and removes asbestos and environmental charges (proxy, performance shares).

**VERDICT on confusion: IN** (the accounts are clear, the development tables are full, and the condition can be read).
**On suspicion, WEIGHS AGAINST, mildly; not a STOP.** Under the two-tell CONVENTION a make-the-numbers habit or adverse
development needs a second tell to become suspicion **[M2003-029]**, **[L2002-039]**. The aggregate development is
favorable, not adverse, and a habit of beating targets is not shown (one year's plan beaten). Present and weighed: an ROE
target paid on, adjusted figures in the headline and in pay, discounting, and releases running high while the company
buys its own stock. Weighed for: catastrophes are charged at a normal amount in pay and stated in dollars in every
release, the plan budgets no reserve releases, and the earlier reserves proved conservative. **The recast earnings for
Q7: component 2 five-year mean $1,637M pre-tax, $1,352M after tax** (accident-year basis; calendar $1,862M pre-tax).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
For an insurer the rows make this the castle itself: "The critical variables, therefore, are managerial brains,
discipline and integrity." **[L2003-014]**. Alan D. Schnitzer has been Chief Executive since 2015 and is also Chairman
(proxy `0000086312-26-000103`, board leadership section); an independent Lead Director is elected by the independent
directors. For a marketable stock the speakers "read rather than meet" **[M2007-081]**, so the tests are the yardsticks
and the documents.
- **The record against the hand dealt** **[M1994-008]**: ten years of underwriting profit (Q2) in an industry the rows
  call "not a terribly good business" **[M2012-059]**, including the catastrophe years 2017 ($539M calendar underwriting
  profit) and 2023 to 2025 ($2.99B to $3.69B of catastrophe losses a year). Against it: the competitor row in Q2, where
  Chubb, Berkley and Hartford's commercial book ran lower combined ratios in the same years with the same hand, and a
  Personal Insurance loss in 2023 (combined ratio 104.8).
- **The proxy: how they treat themselves against the owners** **[M1994-009]**: CEO total compensation **$26,983,859** in
  2025, 204 times the median employee (pay-ratio section); annual bonus up from $7M to $9M and the equity grant from
  $15.25M to $18.05M. Mr. Schnitzer owns 314,215 shares directly and indirectly (about $113M at $360.70) besides 759,510
  options exercisable within 60 days (ownership table, March 23, 2026); hedging is prohibited and pledging needs consent,
  "no pledges have been made". Perquisites are small ($25,257 car, $48,078 security, $19,247 tax planning). The pay is
  large and is set with "an independent compensation consultant" against a "Compensation Comparison Group", the
  ratchet the rows distrust **[M2012-095]**; it is not concealed.
- **The letters and reports** **[M1998-036]**, **[M2007-083]**: the 10-K is full and plain: ten-year development tables,
  the asbestos review described at length, the discount on reserves stated with its rates, catastrophe reinsurance set
  out layer by layer. The earnings release is promotional in its adjectives ("Excellent", "terrific", "our winning
  strategy", Exhibit 99.1 `0000086312-26-000143`), the voice of an investor-relations department **[M2007-083]**.
- **Taking credit** **[M1998-167]**: the proxy justifies the CEO's pay partly by "increased its underlying underwriting
  income by more than 300%, from $1.3 billion to $5.5 billion" over ten years, a figure that leaves out catastrophes and
  reserve development, in years when the whole competitor row also improved with the market (Q2). Mild; noted.
- **How they talk about mistakes** **[L2024-003]**: no instance found, in the FY2025 10-K, the Q2 2026 release or the
  proxy, of a stated management mistake; the recurring asbestos additions are attributed to "court decisions and other
  trends that have attempted to expand insurance coverage far beyond what we believe to be the intent of the original
  parties" (proxy, adjusted core ROE). That may be true; it is also the external explanation.
- **Discipline over volume** **[L2010-008]**, **[M2013-031]**: the pay design charges catastrophes at a fixed "normal"
  amount and does not reward premium growth as such (core return on equity is the main measure), and the plan budgets no
  reserve releases (proxy). Premium fell in Personal Insurance in the first half of 2026 (auto −6%) while retention rose
  (10-Q `0000086312-26-000145`), which is consistent with not chasing volume.

**VERDICT on integrity: IN.** No tell of dishonesty was found: the accounts are clear and complete, the reserves have
run off favorably for a decade (the reverse of the under-reserving the rows expect of a pressed management
**[L2002-006]**), and catastrophes are neither hidden in the releases nor waved out of pay. The adjusted figures in the
headline and the credit taken in the proxy are noted at Q4 and here as weights, not as doubts about honesty; integrity is
applied on doubt **[M2013-088]**, and the documents did not raise one. **Ability WEIGHS FOR**: a decade of underwriting
profit in a commodity line under one management **[M1994-008]**, tempered by trailing the best of its row and by a
chairman who is also the chief executive **[L2014-026]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**: over the ten fiscal years 2016 to 2025 TRV earned $33,694M of
  net income, paid $8,643M of dividends and spent $16,294M on repurchases under its authorizations (XBRL, cross-checked
  to the FY2025 cash-flow statement for 2023 to 2025), so it kept about **$8,757M**. Market value went from **$32,150M**
  (284,058,764 shares on the cover of the Q3 2016 10-Q, `0001104659-16-151040`, at $113.18 on 2016-10-06, aggregator
  close, flagged) to **$75,233M**, a rise of about $43,083M against $8,757M kept, after $24,937M was handed back. On the
  market leg the test is passed many times over. On the intrinsic leg, which the 2009 rewrite asks for because the market
  leg misleads **[R2009-002]**: book value per share excluding the bond marks went from $85.72 (equity ex-AOCI $23,976M
  over 279,685,489 shares on the FY2016 10-K cover) to the company's adjusted book value per share of $168.20 at June 30,
  2026 (Exhibit 99.1), about 7.4% a year before dividends. The rows' question for the future, "Can you keep using all of
  the capital you generate, effectively, for a very long time?" **[M2010-097]**, is answered by the company itself: it
  returns about what it earns ("the combination of dividends [...] and common share repurchases will likely not exceed
  net income", 10-Q `0000086312-26-000145`), keeping only what growing premium needs (Q3).
- **Buybacks** **[L1999-023]**, **[L2016-002]**: the authorization names no price ("The timing and actual number of shares
  to be repurchased [...] will depend on a variety of factors, including [...] share price", 10-Q); it adds $5.0 billion
  approved January 21, 2026. Prices actually paid: about $179 a share in 2023 ($965M for 5.4M shares), $227 in 2024
  ($1,000M for 4.4M), $278 in 2025 ($3,025M for 10.9M) (equity statement, 10-K FY2025), $301.86 in the first half of 2026
  (10-Q note 10). Under the CONVENTION of Q6 these are read against the bottom of the Q7 range, **$151** a share (recorded back from Q7
  below): every year's average price sits above it, and the 2026 price sits at the middle case ($302). So the programme
  **weighs against**: value bought is "entirely purchase-price dependent" **[L2016-002]**, and buying at about the middle
  of the range is not the "demonstrable margin" of **[M2016-048]**. In its favor, for an insurer whose float has cost less
  than nothing, "repurchases automatically increase the amount of "float" per share" **[L2021-008]**, and the shares have
  fallen from 321.4M (cover of the FY2014 10-K, XBRL dei) to 208.6M, the opposite of the serial issuer **[L2014-015]**.
  Debt was raised $1,233M in 2025, the year of the largest buyback (cash-flow statement); the holding company kept
  $2.51B of liquidity against a target of $1.45B (10-Q, Holding Company Liquidity).
- **Deals**: the sale of the Canadian personal and most commercial business to Definity for about US$2.4 billion
  ($2,384M of proceeds, 10-Q cash-flow statement) against net assets held for sale of $2,008M ($4,550M less $2,542M, 10-K
  FY2025 balance sheet): value got above book given. The one acquisition in the window, Corvus (a cyber managing general
  underwriter) for about $427M in January 2024 (10-K FY2025 note on acquisitions), was paid in cash. **No all-stock deal**,
  so the one STOP of Part A **[L2009-019]** does not arise.
- **Part A WEIGHS FOR, narrowly**: the retention test is passed on both legs and capital not needed is returned, but the
  buybacks name no price and have been made at prices above the bottom of the range **[L2016-002]**, **[L2011-003]**.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**: the performance shares vest on a three-year "Adjusted Return on
  Equity" that removes actual catastrophes but charges a fixed "normal" catastrophe amount ($2.45 billion for 2025), and
  removes asbestos and environmental charges "largely beyond the control of current management" (proxy
  `0000086312-26-000103`); 50% vests at 8.75%, 100% at 11.75%, 200% at 16.75%, adjusted up or down by up to 20 points on
  total return relative to the S&P 500 Financials. The hurdle question **[M2004-097]**: a threshold of 8.75% return on
  equity against a ten-year Treasury that the company itself says it beat "on average, more than 1,000 basis points"
  (proxy) is not high for this business. Reserve releases outside asbestos count toward the measure, and the plan budgets
  none, so releases raise pay **[M2005-036]**.
- **Options** **[L1998-028]**, **[M1997-043]**: granted "with an exercise price equal to" the closing price on the grant
  date, with no step-up for retained earnings; "No right to dividends or dividend equivalents is granted on outstanding
  stock options" (proxy), and no instance was found of the proxy naming the dividend conflict **[L2005-014]**. They are
  expensed (Q4).
- **Who designs it** **[M1997-041]**, **[M2004-016]**: a compensation committee with "an independent compensation
  consultant" and a "Compensation Comparison Group" (proxy), the peer ratchet the rows warn of **[L2005-015]**; the
  compensation discussion runs from page 31 to page 75 of the proxy (its table of contents) **[M2009-087]**.
- **The board** **[L2014-026]**, **[M2007-120]**: the CEO is also Chairman, with an independent Lead Director; two
  directors left at the 2026 meeting and one was added on August 5, 2026, leaving nine (8-Ks `0001104659-26-011530`,
  `0001104659-26-016444`, `0001104659-26-092716`). Directors and officers as a group own about 1.38% including options
  exercisable within 60 days (proxy ownership table); the directors' stock is held largely as deferred stock units
  granted to them, not bought "with their savings" **[L2019-008]**.
- **Owners as partners** **[L1994-023]**: the 10-K tells an owner what he would want to know about reserves and
  catastrophes; no earnings guidance is given, but a return-on-equity target is set and published in the proxy.
- **Part B WEIGHS AGAINST, mildly**: a sensible catastrophe charge in pay, set beside a peer-group ratchet, options
  without a step-up, a low vesting threshold, releases that raise pay, and a combined Chairman and CEO.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[R1996-018]**, as a range
**[L2000-024]**; for an insurer, two components and a stated judgment **[M1997-141]**, **[L1998-002]**, **[L2006-002]**,
**[L2010-002]**, inside the Q7 CONVENTION (five-year average, growth shown capped by Q3, ten years then zero nominal
growth, at the sovereign, the two ends) and the sector method's amended steps. Arithmetic: `value.py` (`value_out.txt`)
and `value_mature.py` (`value_mature_out.txt`). Balance-sheet figures are at June 30, 2026 (10-Q `0000086312-26-000145`).

**Choices on the method's open items, stated and labelled** (each a CONVENTION of this run, as the method's header asks):
- **Float construction.** A2's float, $80,870M, also less premiums receivable ($12,382M) and deferred acquisition costs
  ($3,713M), **$64,775M**: premiums not yet collected and commissions already paid are assets standing against the
  unearned-premium liability, not money held **[L1996-008]**. The A2 figure without those deductions is shown beside it.
- **Gross or net of float (A1).** Tests: *costless in each half*: passed (developed cost −2.10% in 2016 to 2020 against a
  2.55% long rate, −3.06% in 2021 to 2025 against 3.69%, Q2); *long-enduring*: passed for what remains (float grew in
  every year 2015 to 2025, and the sale of the Canadian book, $1,627M of net reserves disposed, closed on January 2, 2026
  and is not under way); *equity enough behind it*: **failed**: investments are 3.08 times equity, and nothing in the
  filing makes TRV the exception to "no other insurance company could do it" **[M2023-012]**, **[M1995-035]**. So
  **net of float**, the float treated as a debt to be paid **[L2011-005]**.
- **Tax on unrealized gains** **[M2016-058]**: the fixed-maturity portfolio carries a net unrealized **loss** ($92,922M
  fair value against $95,401M amortized cost) and equities a $242M gain; no deferred tax is deducted, and the tax asset on
  the loss is not counted either (the bonds are expected to be held to maturity, when the mark reverses).
- **Immature accident years (A3).** 2024 and 2025 are shown and flagged; the main case's five-year mean includes them as
  booked, and a second case uses the five mature accident years 2019 to 2023 only. Both are carried; the box does not
  turn on the choice.
- **Debt** is carried by its interest inside component 2 (−$425M a year in 2025), not at face; at face it would take
  about $1.6B more off value ($9,068M face against $425M capitalized at 5.66%, about $7.5B), about $7.5 a share.

**Component 1, the investments, net of float:** investments $103,179M + cash $621M − float $64,775M = **$39,025M**
(with the A2 float: $22,930M). Cash and bonds inside the insurer are "slightly less valuable" than at a parent
**[L2016-009]**; no number is put on that.

**Component 2, the operating earnings other than investments, after tax** (Q4): five-year mean on the accident-year basis
**$1,352M** (pre-tax $1,637M, at the filer's 17.4% effective rate, A4); mature-years case **$762M** (2019 to 2023, pre-tax
$903M, at 15.6%). The items other than underwriting run about −$427M a year after tax.

**Growth shown, and its cap.** Aggregate component 2 grew **21.0% a year** from 2021 to 2025 (1,375 to 2,946, accident-year
basis): a base year depressed and an end year at the top of a hard market **[L2005-003]**, **[L1994-009]**, carried ten
years an absurdity **[M1999-067]**. Over 2016 to 2025 it grew 7.0% a year, which still runs past the discount rate;
the strict cap is the rate itself, **5.66%** **[M1997-095]**.

**The two ends (C6) and the range** (per share on 208.575M shares):

| case | C2 value | total value | per share |
|---|---|---|---|
| low: underwriting at zero (break-even, C6), no growth | −7,544 | 31,481 | **$151** |
| middle: developed average underwriting, no growth | 23,887 | 62,912 | $302 |
| top: developed average, 5.66% for ten years, then flat | 37,407 | 76,432 | **$366** |
| rejected: 21.0% shown, uncapped | 123,369 | 162,394 | $779 |
| mature years 2019 to 2023: low / middle / top | | | $153 / $252 / $288 |
| A2 float instead (no receivables or DAC deduction): low / top | | | $74 / $289 |

- **Value range: $151 to $366 a share** (width 2.43 to 1; mature-years case $153 to $288, 1.88 to 1) **against $360.70.**
  Both widths are inside the three-to-one CONVENTION, so a conclusion can be drawn **[L2000-025]**.
- **The bracket check (C7):** net worth $33,121M; net worth plus float (A2) $113,991M. The range runs from about net worth
  (break-even underwriting) to well above it, which the rows allow only on float that costs less than market money
  **[L1994-025]**, **[L2011-006]**: TRV's does. Above net worth plus float would need "a significant underwriting profit"
  and "significant growth" **[M2012-033]**; no case comes near it.
- **The third element** **[L2010-002]**: the money is returned, not retained (Q6), and recent buybacks were made at about
  the middle case, so it adds nothing up or down.
- **The price against the range.** At $360.70 the price sits at the very top of the main range and above the top of the
  mature-years range. Owner earnings with no growth (component 2, $1,352M, plus after-tax income on component 1 at the
  2025 portfolio yield of 4.05% pre-tax and an 85% after-tax share, a CONVENTION for the municipal bonds, $1,344M) come to
  **$2,696M**, a yield of **3.58% after tax, about 4.3% pre-tax**, on the $75,233M market value. The price implies
  component 2 growing about **5.2% a year for ten years** at the bond rate, i.e. the top case almost exactly.

**Reported at the owner's request (COMPUTATION, not a clearance):**
- **Fair price** (the top case, 5.66% growth for ten years, earns the floor of about 10% pre-tax, 8.26% after tax at
  17.4%): **about $196** (mature-years case $142).
- **Cheap price** (owner earnings with no growth earn the floor; below it no pencil is needed **[M1996-084]**): **about
  $156** (mature-years case $120). The price is 2.3 times the cheap price and 1.8 times the fair price.

**VERDICT: OUT.** Valued, with a range narrower than three to one, and the price at the top of it (or above it, on the
mature years): the expected return at the price, about 4% pre-tax before growth, is below the floor of about ten percent
**[M2003-149]**, **[L2002-020]**, and nowhere near a price that would "scream" **[M2009-005]**. "You can turn any
investment into a bad deal by paying too much" **[M2019-015]**. The file closes here; Q8, Q9, Q10 and Q12 are NOT
REACHED.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (the file closed at Q7).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (the file closed at Q7).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (the file closed at Q7). Inaction is the default **[M1996-006]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (the file closed at Q7; not asked by the operator).

---
## THE BOX
**OUT — decided at Q7.** Value range **$151 to $366 a share** (mature-years case $153 to $288) against **$360.70**:
the price sits at the top of the range, the expected return at it is about 4% pre-tax before growth against a floor of
about ten percent **[M2003-149]**, and the case would need a pencil, not a scream **[M2009-005]**. Q1 to Q6 passed or
weighed: Q1 IN (both sides readable), Q2 IN marginally (float at a negative cost in every year 2016 to 2025, but not the
low-cost operator and trailing Chubb, Berkley and Hartford's commercial book), Q3 for modestly, Q4 IN on confusion and
against mildly on the tells, Q5 IN on integrity, Q6 for narrowly (A) and against mildly (B). **What would reverse it:** a
price at or below about **$196** (the top case earns the floor; the "fair" price) and, to need no pencil, about **$156**
(no-growth owner earnings earn the floor; the "cheap" price), with the underwriting record intact (a developed accident-
year underwriting profit continuing and the general-liability development not spreading); or, at today's price, the
2024 and 2025 accident years maturing as booked and component 2 holding near its 2025 level for several more years,
which would lift the five-year mean enough to move the range. Q11 belongs to the holding review.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy was the first action after reading; the first EDGAR fetch came
      after it); written question by question; committed after Step 0 and after each of Q1 to Q7 (write-early).
- [x] Every v5 id resolves: the 136 distinct ids cited were each grepped in `principle_ledger_v5.csv` (none missing);
      every filing fact has its accession; no number without a filing, a script output in the research folder, or a
      CONVENTION label.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are NOT REACHED and nothing after Q7
      is a clearance. Q6's buyback reading used the Q7 bottom, computed after Q1 to Q4 closed, as the CONVENTION allows.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): for an insurer, component 2 by the
      sector method (investment income and realized gains out, accident-year underwriting in, catastrophes and stock pay
      in, after tax); the sovereign from the US Treasury; the price quotes (2026-10-05 and 2016-10-06) flagged as
      aggregator closes.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations, Q1, Q2, Q4, Q5).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): this is a run of today, not a
      point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII): it printed one line, "UNRESEARCHED", and nothing
      from it was used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7's five-year average against the sector method's A3.** The Q7 CONVENTION averages the last five years; A3 says
the immature accident years are "never averaged in as if developed". For an insurer the last five years always contain
two immature years, and here they are the two best. I carried both cases (2021 to 2025 as booked, $151 to $366; mature
2019 to 2023, $153 to $288); the box did not turn on it, but on a name nearer the line it would. (2) **The float
construction's open item moves the value by about $77 a share**: deducting premiums receivable and deferred acquisition
costs (the first construction) or not (A2 as written) changes component 1 by $16.1B; I chose the deductions and labelled
it. Until it is settled, two analysts can disagree by a fifth of the price on the same filing. (3) **Width against
price.** On the A2 float the range is $74 to $289, 3.92 to 1, wider than the three-to-one CONVENTION, with the price above
its top: the width rule says TOO HARD and the price-above-top specific says OUT. The framework does not say which is read
first; I read OUT because every case built was below the price, and record the gap. (4) **The floor for a value built of
two components** (the method's open item) forced a choice the method does not make: the expected return at the price
needed the after-tax income of component 1, for which I assumed an 85% after-tax share of portfolio income (a
CONVENTION, for the municipal bonds). (5) **Q2 for an insurer is an "or" list.** The sector method accepts a cost of
float kept low over years as sufficient evidence of a castle, while **[M2012-059]** says one must be "in the top 10
percent, really" to do well; TRV passes the first and fails the second against its own competitor row, and the
framework gives no rule for which governs. I closed Q2 IN marginally and carried the narrowness to the margin of safety.
(6) **A3 drops pre-window accident years.** The accident-year basis excludes development on accident years before the
window, asbestos included ($242M to $284M a year in 2023 to 2025); here those years netted favorable, so the calendar
basis was the higher, but for a company whose old years run adverse the A3 basis would flatter the result, and the
method does not say how the run-off cost re-enters. (7) **Reserve releases during buybacks.** **[M2013-085]** names the
tell for a company buying its own stock as reserves being *built*; TRV's releases were highest in its years of largest
buybacks, and no row covers that direction. **Tool defects** (reported, not fixed): `tools/run.py` prints
"UNRESEARCHED" for any insurer because it requires capital-expenditure facts, where it should say that the sector method
applies; `Screens/cover_shares.py` printed "NO COVER SHARE COUNT PARSED" because TRV's cover renderer (R1.htm of
`0000086312-26-000145`) labels the value "Common stock shares outstanding", a filer-specific label, not "Entity Common
Stock, Shares Outstanding", which is the only label its regex accepts; the dei element name in the same page would have
matched.
