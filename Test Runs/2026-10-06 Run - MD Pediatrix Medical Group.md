# Company Run: Pediatrix Medical Group, Inc. (NYSE: MD), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated name before any fetch. Working folder:
`Test Runs/_research 2026-10-06 MD/` (raw filings, the converter `totext2.py`, the fetcher `fetch.py`, the series
script `series.py`, the value arithmetic `value.py` and its output `value_output.txt`, the cited ledger rows
`ledger_cited.txt`, the citation check `check_cites.py`).

**POSITION NOTE, declared before any verdict:** not known to this session. `PORTFOLIO.md` was not opened (blind rule
of the brief). The run is written as if the name is not held.

**Contamination declared.** The session start showed the repository status and five recent commit subjects (TPC, REYN,
PATK, BCC and an OSIS/BCC addendum); none concerns this company. The status listed three untracked run files of
2026-10-06 (COLL, MHO, WKC) by name only; none was opened. No other `Test Runs/` file about MD (Mednax) was found by a
file-name search (`ls "Test Runs" | grep -i "MD |pediatrix|mednax"` returned only AMD and TCMD, unrelated) and none was
opened. Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`, the run queue, the prepped reading list,
the unadopted gaps case. The run was interrupted once by a session limit and resumed from the files on disk; nothing
outside the working folder was read on resumption.

**Write-early and commits.** The brief forbids commits; the file was written section by section and not committed. That
departs from the template's first self-audit line and is recorded there.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $26.10 (close 2026-10-05; `python tools/run.py MD`, aggregator quote flagged as live quote only, operator
  rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock $.01 par, **81,253,271** shares
  (10-Q for the quarter ended 2026-06-30, filed 2026-08-04, accession `0001193125-26-331513`;
  `python Screens/cover_shares.py MD`). No other class; preferred authorized, none issued (10-K FY2025 balance sheet).
- **Market cap:** $26.10 x 81.253M = **$2,121M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 2026-10-05, as fetched
  by `tools/sources.py` through `tools/run.py` (issuing authority; FRED not used).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-19, `0001193125-26-058074` (Items 1, 1A, 7, 8 read in the parts cited below).
  - 10-Q Q2 2026, filed 2026-08-04, `0001193125-26-331513`.
  - Proxy (DEF 14A) filed 2026-03-27, `0001193125-26-127299` (pay, ownership).
  - 8-Ks: 2026-07-15 `0001193125-26-304033` (ex. 99.1, second-quarter update, Adjusted EBITDA outlook $280M to $300M);
    2026-08-04 `0001193125-26-331488` (ex. 99.1, results); 2026-07-24 `0001193125-26-316225` (general counsel
    separation); 2025-08-18 `0000950170-25-109777` ($250M buyback authorization, no price named).
  - Earlier 10-Ks for the span: FY2005 `0000950144-06-001900`, FY2006 `0000950144-07-007315`, FY2010
    `0001193125-11-045579`, FY2012 `0001193125-13-062738`, FY2015 `0001193125-16-459842`, FY2018
    `0001193125-19-040891`, FY2019 `0001193125-20-042622`, FY2020 `0001193125-21-047064`, FY2021
    `0000950170-22-001387`, FY2022 `0000950170-23-003127`, FY2023 `0000950170-24-016794`, FY2024
    `0000950170-25-023730`.
- **One figure cross-checked against the filed statement:** net revenue FY2025 $1,913,849K on the filed Consolidated
  Statement of Income (10-K FY2025) equals the XBRL figure $1,913.8M used by `run.py`; operating cash flow FY2025
  $271,091K total and $274,739K continuing on the filed cash-flow statement; `run.py` printed the total ($271.1M),
  which includes discontinued-operations outflows. This run uses the continuing figure and says so.
- **`tools/run.py MD` arithmetic lines** (read for arithmetic only; its v4 material ignored, Part VII): OCF 2023-2025
  $137.3M / $206.6M / $271.1M (totals); SBC $12.3M / $11.9M / $18.0M; capex $33.3M / $22.0M / $18.5M; D&A $36.2M /
  $32.2M / $21.8M. **It does not subtract acquisitions.** The brief says acquisitions of physician practices are
  capital; this run subtracts them (see the owner-cash table).

### Owner cash after every real cost (USD M; continuing operations; filed cash-flow statements)
Owner cash = continuing OCF minus stock pay minus capex minus acquisition payments. Interest is already inside OCF, so
this is cash to the equity.

| FY | OCF cont. | SBC | capex | acquisitions | **owner cash** | D&A variant |
|---|---|---|---|---|---|---|
| 2021 | 113.8 | 19.0 | 32.2 | 29.9 | **32.6** | 32.7 |
| 2022 | 182.3 | 16.1 | 29.7 | 28.2 | **108.3** | 102.4 |
| 2023 | 146.1 | 12.3 | 33.3 | 6.7 | **93.8** | 90.9 |
| 2024 | 217.3 | 11.9 | 22.0 | 8.2 | **175.2** | 165.0 |
| 2025 | 274.7 | 18.0 | 18.5 | 23.2 | **215.0** | 211.7 |
| five-year mean | | | | | **125.0** | 120.5 |

Sources: 10-K FY2022 cash-flow statement (2021, 2022), 10-K FY2025 (2023 to 2025). Abnormal years in the window: 2021
carries a $72.7M receivables build from the revenue-cycle transition (10-K FY2022) and a $20.0M strategic investment
(not subtracted above; written off as "Impairment of strategic investment" in 2023); 2025 carries a $30.6M receivables
release and a $30.0M divested-investment receipt (investing, not in owner cash). Contingent consideration paid in
financing ($1.8M, $1.2M, $3.2M in 2023 to 2025) is not subtracted; immaterial. Mean excluding 2021: **$148.1M**.

### The ten balance sheets, read before the income account **[M2025-032]**
From `run.py`'s table (first-filed XBRL) checked against the filed statements of FY2018, FY2019, FY2020 and FY2025.

| year-end | assets | equity | goodwill | receivables | cash | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 5,339 | 2,761 | 3,845 | 495 | 56 | 1,682 | 1,786 |
| 2017 | 5,867 | 3,066 | 4,284 | 504 | 60 | 1,846 | 2,048 |
| 2018 | 5,935 | 3,088 | 4,383 | 542 | 37 | 1,970 | 2,094 |
| 2019 | 4,146 | 1,499 | 2,710 | 499 | 113 | 1,728 | 510 |
| 2020 | 3,348 | 747 | 1,478 | 242 | 1,124 | 1,700 | -286 |
| 2021 | 2,723 | 896 | 1,505 | 302 | 387 | 990 | -155 |
| 2022 | 2,348 | 892 | 1,532 | 297 | 10 | 637 | -89 |
| 2023 | 2,220 | 849 | 1,384 | 272 | 73 | 622 | 149 |
| 2024 | 2,153 | 765 | 1,243 | 260 | 230 | 597 (with leases) | -249 |
| 2025 | 2,247 | 866 | 1,261 | 230 | 375 | 571 + 27 current | -83 |

What the figures say. (1) Goodwill rose to $4.38bn by 2018 on acquisitions of about **$4.0bn from 2010 to 2019**
(XBRL acquisition payments summed, `series.py`), then fell by $3.1bn: a $1.45bn goodwill impairment in 2019 (anesthesia),
the anesthesia group sold in May 2020 for **$50.0M cash** plus a contingent interest of $0 to $250M, radiology sold in
December 2020 for **$885M**, MedData sold in 2019 (10-K FY2020, Divestitures). (2) Retained earnings went from **+$2,094M
(2018) to -$83M (2025)**: the decade's acquisitions consumed what the business had retained since its listing.
Cumulative net income 2016 to 2025 is **-$1,177M** (sum of filed annual net income). (3) Equity of $866M is less than
goodwill of $1,261M: **tangible equity is about -$412M**. (4) Debt has come down from $1.97bn to $584M at 2026-06-30
($186M term loan due February 2027 now current, $400M 5.375% notes due 2030), against cash and short-term investments
of $404M (10-Q Q2 2026). (5) Receivables fell with the divestitures and with days outstanding from 47.6 to 42.8
(10-K FY2025). (6) A professional-liability reserve of **$273.5M**, self-insured through a captive, sits beside the
debt (10-K FY2025, Liquidity). What they cannot say: whether the $1.26bn of goodwill left is worth anything apart from
the people who generate it; the 2024 impairment was triggered by the market value falling below book (10-K FY2025,
Goodwill).

---
## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the NICU contracts and their payers will yield, not where the quote goes
**[M1997-109]**; the quote "just tells us prices" **[M2006-077]**. The habits govern this run: looking "for what's wrong in
things" **[M2025-013]**, with the reading done "to possibly reject your original hypothesis" **[M1998-144]**.
**Contrary evidence, written down as found** **[M1997-127]**:
1. Operating margin roughly halved over twenty years on the same lines of business (Q2).
2. Physician pay rose from 56.7% of revenue (2005) to 70.1% (2025) (Q2).
3. About $4.0bn spent on acquisitions 2010 to 2019; anesthesia sold for $50M cash after a $1.45bn impairment; retained
   earnings wiped out (Step 0).
4. Hospital contracts run one to three years and either side can end them without cause (10-K FY2025, Item 1).
5. A 2006 federal and state settlement of $25.1M over neonatal Medicaid billing 1996 to 1999 with a five-year Corporate
   Integrity Agreement, and options backdating 1997 to 2000 found by the audit committee, with the then chief executive
   "party to e-mail correspondence concerning the selection of favorable dates" (10-K FY2006, `0000950144-07-007315`).
   The people named are no longer the management; recorded, not weighed (Q5 not reached).
6. Management leads with Adjusted EBITDA (guidance $280M to $300M; executive performance shares paid on it; proxy 2026).
7. Four chief-executive regimes in six years (Medel to 2020; Ordan; Swift 2022 to January 2025; Ordan again, paid
   $14.1M for 2025 including a $2.0M retention award; proxy 2026, Summary Compensation Table).
For the business: a national leader in neonatology (about 1,350 of about 7,200 board-certified neonatologists; over
360 NICUs; 10-K FY2025), payor mix steady for seventeen years, debt cut by two thirds, adjusted operating margin back
to 12.1% in 2025.

## THE STANDING RULE
Owning a share bought with cash, unlevered and sized within the buyer's means, puts the buyer at no risk of ruin from
this name; the rule is the buyer's conduct **[M2012-081]**, **[M2004-065]**. Nothing in the purchase would be financed by
borrowing.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- The test **[M1995-051]**: "a reasonable fix on about what the earning power and competitive position will look like in
  five or 10 years" **[M2012-065]**. The product (critical care of newborns) does not need to be understood medically; the
  economic dynamics do **[M2011-014]**.
- **The key variables and their record** **[M1998-044]**: (a) births x NICU admission (about 3.6M births, 14% to 15%
  admitted; births about 4M in the FY2015 10-K, so down about a tenth in a decade); same-unit volume moved -0.1% to
  +2.1% a year 2010 to 2025 outside 2020 to 2021 (MD&A of each 10-K). (b) payor mix: government 23% to 27% of net
  patient revenue every year 2008 to 2025, while 53% to 57% of gross billings are government (payor-mix tables, every
  10-K); commercial payers carry the economics. (c) price: Medicaid fee schedules set by the states "are not
  negotiated"; commercial contracts negotiated with consolidating payers; the No Surprises Act bars balance billing for
  neonatology outright (10-K FY2025, Item 1A). (d) the cost of the physician, 70% of revenue. (e) the hospital
  contract, one to three years, terminable without cause, sometimes with administrative fees (14% of 2025 revenue).
- These are knowable and important **[M2006-076]**, and the filings have recorded them consistently for twenty years;
  nothing turns on fast technology (no TOO HARD routing under **[M1998-008]**). Against: the proxy says payor-mix shifts
  are "extremely difficult to forecast over both short- and long-term periods" (DEF 14A 2026, Measuring
  Pay-for-Performance), which reads as the insiders declining to write the forecast down **[M2000-105]**; but seventeen
  years of a 23% to 27% government share contradict that claim at the horizon that matters. Federal Medicaid policy
  (the July 2025 law's cuts) is the open variable; it moves the size of the cash, not the nature of the business.
- The doubt rule **[M2002-092]** was applied: the doubt is about policy levels, not about how the business makes or loses
  money. A fix on earning power and position is possible, and the fix is what Q2 tests.
- **VERDICT: IN** (narrowly), **[M1995-051]**, **[M2012-065]**, **[M1998-044]**; filing fact: the payor-mix and same-unit tables
  of the 10-Ks FY2010 to FY2025.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
The question: "why is that castle still standing? And what's going to keep it standing or cause it not to be
standing five, 10, 20 years from now" **[M1995-038]**; "The dynamics of capitalism guarantee that competitors will
repeatedly assault any business "castle" that is earning high returns" **[L2007-004]**.

**Widening or narrowing: the whole span** **[M1999-108]**, **[M2000-075]**. Operating margin, same lines of business
(neonatal, maternal-fetal, pediatric subspecialty; anesthesia and radiology removed from 2018 on as restated):

| | 2002 | 2004 | 2005 | 2007 | 2010 | 2012 | 2015 | 2018c | 2019c | 2020c | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| op. margin | 24.1% | 25.2% | 21.3% | 24.1% | 22.3% | 21.4% | 20.1% | 14.4% | 9.7% | 5.7% | 10.6% | 8.8% | 0.4% | -3.4% | 10.9% |
| adjusted* | | | | | | | | 14.4% | 13.1% | 9.9% | 10.6% | 8.8% | 7.9% | 9.1% | 12.1% |
| practice pay / revenue | 56.5% | 56.5% | 56.7% | 58.1% | 61.0% | 62.3% | 63.1% | 65.3% | 66.3% | 68.9% | 67.9% | 70.1% | 72.6% | 71.6% | 70.1% |

Sources: selected-data tables of the 10-Ks FY2005 and FY2010; income statements of FY2012, FY2015, FY2020 (2018c to
2020c, continuing operations as restated) and FY2021 to FY2025. *Adjusted removes goodwill impairments, restructuring
and disposal losses as the filer itemizes them; shown only to give the castle every benefit. The 2010 to 2015 figures
include the anesthesia business acquired from 2007; the 2002 to 2005 figures are nearly pure neonatology and
maternal-fetal. Over twenty years the margin went from about 24% to about 11% and the physicians' share of revenue
rose about 13 points. That is the notch, lost more than once **[L1995-023]**, **[M2002-005]**.

**The castle tests, each with its filing fact.**
1. *What keeps it standing, and does it depend on the lord* **[M1995-038]**, **[L2007-006]**. The asset is the physician.
   "The partnership's moat will go when the surgeon goes" **[L2007-006]**; the expert's earning power stays with the
   expert, who "bought your expertise when you went to medical school" **[M2005-050]**. The filer: employment agreements
   "can be terminated without cause", non-competes may not be enforced, and recruiting "has become increasingly more
   competitive"; FY2023 10-K: "We anticipate that we will continue to experience a higher rate of growth in clinician
   compensation expense at our existing units over historic averages". The table above shows the physicians taking
   the margin.
2. *The money test* **[M2011-015]**, **[M2012-106]**. Could a funded attacker take a NICU? The filer says yes in its own
   words: "Demand for hospital-based physician services, including neonatology, is determined by a national market in
   which qualified physicians with advanced training compete for hospital contracts"; "We also face competition from
   hospitals themselves"; "we face competition from healthcare-focused and other private equity firms" (10-K FY2025).
   The supply of board-certified neonatologists rose from about 4,600 (10-K FY2010) to about 7,200 (10-K FY2025);
   Pediatrix's share of them fell from about 21% (968) to about 19% (1,350). The NICU count is flat (over 370 in
   FY2015, over 380 in FY2020, over 360 in FY2025).
3. *Pricing power and the agony before a rise* **[M2005-020]**. None: "we generally cannot increase our revenue through
   increases in the amount we charge for our services" for government programs; Medicaid rates "are established by
   state governments and are not negotiated"; payers consolidating "with increased negotiating power"; balance billing
   for neonatology "always prohibited" under the NSA (10-K FY2025, Items 1 and 1A). Same-unit reimbursement gains ran
   0.5% to 2.8% a year in the normal years (MD&A, FY2010 to FY2024), below the rise in physician pay. The price is set
   by someone else, as at the gas station where "whatever he charged for gas was my price" **[M2012-109]**, **[M2023-079]**.
4. *Would the customer still choose it over the low bid* **[M2017-009]**. The paying customer is the insurer or the state,
   who pays a fee schedule and does not choose the group; the contracting customer is the hospital, whose contract can
   be ended on notice. Hospitals pay administrative fees (14% of revenue) to keep the units staffed, which shows need,
   not loyalty: the fees "may" be reduced or eliminated (10-K FY2025).
5. *The low-cost position* **[M2001-013]**. The cost is labor, set in a national market for the same physicians; no
   evidence of a cost advantage over the hospital that employs its own neonatologists. "you just can't take labor
   costs that are materially higher than your competitor in a business that has commodity-like characteristics"
   **[M2001-013]**.
6. *What could destroy, modify or reduce it* **[M2000-014]**: Medicaid cuts (the July 2025 law, a CBO estimate of
   about $1 trillion less federal Medicaid and CHIP spending; 10-K FY2025), lapsed exchange subsidies, the NSA's
   arbitration, physician wage inflation, a Texas concentration of 32% of revenue.
7. *The competitor row* (same metric, competitors' own filings):

| company | metric | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | source |
|---|---|---|---|---|---|---|---|---|
| TeamHealth (hospital physician staffing; private since 2017) | operating income before interest, debt and deal costs / net revenue | 8.5% | 7.5% | 6.1% | 6.8% | 6.7% | 6.6% | 10-K FY2012 `0001082754-13-000007`, 10-K FY2015 `0001082754-16-000054` |
| Envision, EmCare segment (facility-based physician services; private since 2018) | segment income from operations / net revenue | | | | 9.3% | 9.9% | 6.6% | 10-K FY2015 `0001558370-16-003692` |
| Pediatrix / Mednax | income from operations / net revenue | 22.3% | 22.4% | 21.4% | 21.0% | 21.0% | 20.1% | 10-Ks FY2012, FY2015 |
| Pediatrix 2025 | same | | | | | | | 10.9% reported, 12.1% adjusted |

   Pediatrix earned two to three times the staffing peers' margin in 2010 to 2015 and has since moved most of the way
   toward them. The later fates of the two private peers (an Envision bankruptcy in 2023 and a TeamHealth debt
   restructuring are widely reported) were **not** taken from any primary filing and are not relied on. Hospital
   employment is named by the filer as a competitor; no filing gives its margin, so no row was filled for it.
8. *Ask the competitors* **[M2025-043]**: no competitor testimony on the public record was found in the filings read.
   Not answerable from primary documents; recorded and set aside.

**The case for the castle, stated as strongly as the filings allow.** The largest national neonatology group, 45-plus
years old, with a clinical data warehouse of 2.1M patients, hearing screening at 340 hospitals, contracts that "in
most cases" renew, and a 2025 same-unit revenue rise of 6.2% with adjusted margin up to 12.1%. That is a recovery from
a trough of the company's own making (revenue-cycle failure 2022 to 2023, the office-practice exits of 2024), not a
widening: the 2025 margin is half the 2004 margin, and the filer itself expects clinician pay to keep outrunning its
history.

**Reading.** The moat is not tenuous in the sense of unknowable **[M2000-019]**; it is shown on twenty years of filed
figures to have narrowed, with the reasons named by the filer: the price is set by states and consolidating insurers,
the scarce input is free to leave and takes a rising share, and hospitals and private equity can staff the same
units. "you do not want to have something whose competitive position is going to erode over time" **[M2007-117]**.
"Leadership alone provides no certainties" **[L1996-031]**. A low price does not reopen it: "What you can't do is turn
any investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** A castle shown on the evidence to be filling in closes OUT **[M2011-015]**, **[M2006-013]**; filing facts:
  operating margin 25.2% (2004) to 10.9% (2025), practice pay 56.5% to 70.1% of revenue, hospital contracts terminable
  without cause, rates not negotiated with government payers, peers' margins converged on.

## Q3 to Q12: NOT REACHED
Q2 closed the file OUT. Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are **NOT REACHED** and nothing below is a clearance.
The facts gathered for them stay in Step 0 and the foundations line as record.

---
## COMPUTATION, NOT A CLEARANCE (reported at the owner's request; not a rule change)
Everything in this section is arithmetic after a closing STOP. It carries no entry language (operator rule 3).

**Construction (Part VI convention for Q7, applied as arithmetic only).** Value is the discounted cash "that can be
taken out of a business during its remaining life" **[R1996-018]**, at "the yield on long-term U.S. bonds" **[L2000-021]**; owner cash after "all forms of compensation" **[L2021-003]**; five-year mean, with the base-year
caution **[L2005-003]**; growth capped so that it does not trace to an absurdity **[M1997-095]**, **[M1999-067]**; ten years at
the shown growth, then zero nominal growth; discounted at the 30-year Treasury 5.66%. Equity basis: owner cash is
after interest, so no debt is deducted again; the $186M term loan due February 2027 is covered by $404M of cash and
short-term investments.

**The growth input. CONVENTION of this run:** aggregate owner cash "grew" from $32.6M (2021) to $215.0M (2025), a
rate built on an aberrant base year **[L2005-003]**; carried forward it traces to an absurdity **[M1999-067]**. Revenue was
flat over the window ($1,911M in 2021, $1,914M in 2025, after exits and acquisitions); same-unit revenue averaged about
3% a year 2022 to 2025. The shown-growth end uses **3%**, the most the record supports; rationale: the convention asks
for the growth the business has shown and the only clean measure of it is same-unit revenue.

**(a) VALUE RANGE (USD per share; 81.253M shares).**

| case | owner cash | no-growth end | 3% shown-growth end | top / bottom |
|---|---|---|---|---|
| convention: five-year mean 2021 to 2025 | $125.0M | **$27.18** | **$34.47** | 1.27 |
| variant excluding abnormal 2021 | $148.1M | $32.20 | $40.83 | 1.27 |
| **whole-cycle variant**: mean adjusted continuing margin 2018 to 2025 (10.3%) on 2025 revenue, less interest, tax at 26.6%, plus D&A less capex and average acquisitions | $102.7M | **$22.33** | **$28.32** | 1.27 |

Against **$26.10**: the price sits just below the bottom of the convention range and inside the whole-cycle range.
Had the file reached Q7, the convention would close it OUT: narrower than three to one, price inside or just below the
range, not a screamer **[M2009-005]**, **[M1996-084]**. The low sovereign-relative values flatter the range; the floor below
binds harder.

**(b) FAIR PRICE: the price at or below which the central case clears the ~10% pre-tax floor** **[M2003-149]** (Part VI
CONVENTION). Central case: owner cash $136.5M (midpoint of the five-year mean and the ex-2021 mean), growth 1.5% (half
the shown 3%). Tax treatment: owner cash grossed up at the filer's 2025 adjusted rate of 26.6% (10-K FY2025, MD&A) to
pre-tax $186.0M; expected pre-tax return = pre-tax yield + growth.
- **On equity: fair about $26.93** (equity $2,188M). With no growth: $22.89. With the full 3%: $32.70.
- On equity plus net debt (pre-tax owner cash plus $36.0M interest, floor on enterprise value, net debt $180M at
  2026-06-30 deducted): $29.93 at 1.5% growth, $25.11 at none.
- At $26.10 the trailing five-year owner cash is 5.9% after tax, **8.0% pre-tax**, on the market value: below the floor
  without growth, at it only with growth the castle evidence does not support.

**(c) CHEAP PRICE. Rule (CONVENTION of this run):** the lower of (i) the price at which the whole-cycle owner cash with
no growth yields 10% pre-tax, and (ii) two thirds of the bottom of the convention range; below it no pencil would be
needed. (i) $17.22; (ii) $18.12. **Cheap about $17.20.** This does not reopen the file: Q2 is OUT, and a lower price
does not cure a narrowing castle **[M2019-015]**.

---
## THE BOX
**OUT at Q2.** The castle is shown on twenty years of filings to have narrowed: operating margin from about 24% to about
11%, physicians' share of revenue up 13 points, prices set by states and consolidating insurers, hospital contracts
terminable without cause, and margins converging on the staffing peers'. Computation only: value range $27.18 to
$34.47 (whole-cycle $22.33 to $28.32), fair about $26.93 (equity, 1.5% growth) or $22.89 (no growth), cheap about
$17.20, against $26.10.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed** (the brief forbids
      commits); the write-early commit after each question did not happen.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (`check_cites.py` in the working folder); every filing fact has
      its accession or its 10-K year; numbers carry a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance (computation headed as such).
- [x] Owner cash from operating cash flow less stock pay, capex and acquisitions, never a net-income proxy; sovereign
      from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found **[M1997-127]** (foundations list).
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used; its omission of acquisitions was corrected.
- [x] `python tools/check_framework.py` run before reporting (result in the reply).
- Honest limits: the 2002 to 2005 margins include a small non-neonatal share, and the 2010 to 2015 margins include
  anesthesia, so the "same lines of business" comparison is approximate at the middle of the span; the 2018 to 2025
  continuing figures and the 2002 to 2007 figures are the cleanest ends, and they show the same narrowing. Hospital
  contract retention rates are not disclosed; no instance found in the 10-Ks read of a count of contracts lost or won.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) Q1 and policy: the framework routes fast technological change to Q1 TOO HARD but says nothing about
a business whose price is set by government; the filer's proxy says its key variable cannot be forecast, while
seventeen years of its own tables say it barely moved. I read the record over the claim and passed Q1, but the rule
does not say which governs. (2) The Q7 convention measures shown growth "on the aggregate owner cash", which here
starts from an aberrant base year (2021) and would yield an absurd 60%-plus rate; the convention has no fallback, so
this run used same-unit revenue growth and confessed it. (3) The "fair price" and "cheap price" the owner asked for
have no rule in the framework: the floor convention gives a minimum return, not whether growth belongs in the central
case or whether the floor sits on equity or enterprise value. Both bases are shown; the choice of 1.5% central growth
is this run's.
