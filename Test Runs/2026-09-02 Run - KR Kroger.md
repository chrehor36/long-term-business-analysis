# Company Run — The Kroger Co. (NYSE: KR) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file and
that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`. Format precedents:
`Test Runs/2026-08-30 Run - COST (Costco) v4.1.md` (the food retailer already run by this
project, whose competitor work is built on rather than repeated),
`Test Runs/2026-09-01 Run - SHOE Shoe Station Group.md` (the ASC 842 operating-lease test),
`Test Runs/2026-09-01 Run - GIS General Mills.md` (the packaged-food counterparty whose
private-label finding is the mirror image of this one).

**Position context: NONE HELD. Fresh entry run.** Surfaced by
`Screens/2026-09-01 MASTER RUN QUEUE.csv` at a **5.82% bottom-boundary owner-earnings yield
against a 5.18% sovereign, needing 4.18% perpetual growth to reach the [E4-28] 10% floor**,
on a **57% spread** across the constructions. Under **[E4-25] the range width is itself the
finding**, and the operator's first instruction was to explain the width from the filings
before pricing anything. That is done in Stage 0(c) below, and it is the analytical core of
this run.

**Bias declared before the evidence, per operator rule 9.** Four biases were live.
**First**, this analyst arrives from the GIS run, which closed a packaged-food company at Q2
on private-label substitution. Kroger is the *other side* of that trade — the retailer whose
$39bn of Our Brands is the substitute doing the damage — and there is a real temptation to
reward it for winning a fight whose loser I have already scored. **Second**, the opposite
pull: eleven grocery-adjacent names in this project have failed, and finding a twelfth is
cheap. **Third**, the screen put this name on the desk at a yield **above** the sovereign
with a growth requirement of 4.18%, which is the shape that earned OTIS, FCN and GIS their
full runs — an incentive to clear it **[E4-27]**. **Fourth, and the sharpest**: this run
consumed more research hours than any name in the queue. Sunk cost is an incentive to
justify the time with a verdict. **The base rate is that thirteen businesses have cleared
Q1–Q4 in this project and all thirteen failed on price, and five more failed at Q2 despite
clearing the floor on yield. A "no" here is a fully successful run.**

**Evidence files committed with this run** (all in `Test Runs/_research 2026-08-26/`, `.txt`
extractions tracked, raw `.htm` gitignored): `KR_10K_FY2026`, `KR_10K_FY2025`,
`KR_10K_FY2024`, `KR_10K_FY2022`, `KR_10K_FY2019`, `KR_10Q_Q1_FY2027`, `KR_DEF14A_2026`,
`KR_companyfacts.json`, `KR_submissions.json`, plus the 8-K exhibits named at Step 0 and the
peer filings named in the competitor row (`ACI_10K_FY2026`, `PUSH_10K_FY2025`,
`SFM_10K_FY2025`, `TGT_10K_FY2026`, `DG_10K_FY2026`, `CASY_10K_FY2026`, `WMT_10K_FY2026`,
`COST_10K_FY2025`).

**A note on fiscal-year labels, because they are a trap here.** Kroger labels a fiscal year
by the calendar year in which it *begins*. **"Fiscal 2025" is the 52 weeks ended
2026-01-31**, and its 10-K was filed 2026-03-31. This run uses Kroger's own labels
throughout and gives the period-end date wherever a number could be mistaken.

---

# STAGE 0 — THE FIVE-MINUTE ARTIFACT CHECK, REPORTED FIRST

## (a) THE CAP IS REAL — total economic shares from the newest filed cover

> "The number of shares outstanding of the registrant's common stock, as of the latest
> practicable date. **612,575,611**, shares of Common Stock of $1 par value, as of
> March 25, 2026."
> — Form 10-K for the fiscal year ended 2026-01-31, cover page, filed **2026-03-31**,
> accession **0001104659-26-037723**

- **One class of common stock, $1 par, one vote per share. No preferred is outstanding:**
  "Preferred shares, $100 par per share, 5 shares authorized and unissued — $—" (filed
  balance sheet). Two million of the five million authorised preferred shares remain
  available for issuance; **none has been issued.** Noncontrolling interests are **$9M**.
- Confirmed independently from the Q1 FY2026 balance sheet (10-Q for the quarter ended
  2026-05-23, filed 2026-06-26, accession **0001104659-26-078236**): **1,918M shares issued
  less 1,305M in treasury = 613M outstanding**; diluted weighted average 615M.
- Diluted weighted-average shares for fiscal 2025: **655M** (XBRL, tied to the filed
  $1.54 EPS line). The gap between 655M and 613M is the year's own buyback, not an artifact.
- Price **$57.94**, close **2026-09-01** (Yahoo chart API — *aggregator, live quote only,
  flagged*). 52-week range on closes **$55.53 – $75.60**; intraday **$54.15 – $76.58**.
- **Market cap: 612.576M × $57.94 = $35,493M.** The screen's $35,322M is within **0.5%**.
  **No share-class artifact. LEG PASSES.**
- Net debt: total debt including finance leases **$17,566M** ($1,802M current + $15,764M
  long-term, filed balance sheet) less cash and temporary cash investments **$3,334M** =
  **$14,232M**. Kroger's own Table 5 reconciliation gives **$14,448M** (it nets only
  $3,106M of *temporary* cash investments). Add operating lease liabilities of **$7,126M**
  and the full claim ahead of the equity is **≈$21.4bn** against a $35.5bn quote.
- **A fact the screen did not carry.** The stock closed at **$62.85 on 2026-01-30**, the
  last trading day of the fiscal year, ran to **$71.57 on 2026-03-05** (the day the FY2025
  results and FY2026 guidance were published), and is **$57.94 today — 19% below the March
  print and 24% below the 52-week high.** The screen is pricing a business the market has
  already re-rated *down* by a fifth in six months.

## (b) THE DIVIDEND, DECOMPOSED — and the buyback with it

**Regular versus special: every distribution in the filed record is a regular quarterly
dividend. No special dividend appears anywhere in the per-share series.** Kroger reinstated
a dividend in 2006 and has raised it annually since. Filed per-share and dollar series:

| fiscal | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| dividends paid, $M | 443 | 437 | 486 | 534 | 589 | 682 | 796 | 883 | **885** |
| DPS paid, $ | — | — | — | 0.68 | 0.78 | 0.94 | 1.10 | 1.22 | **1.34** |

- DPS paid **+14.5%/yr** compound over fiscal 2020→2025. **The current rate is $0.35 a
  quarter** ("On March 12, 2026, we announced that our Board of Directors declared a
  quarterly cash dividend of $0.35 per share"), an annualised $1.40 = a **2.42% yield** at
  $57.94.
- **[E2-52] NOT fired.** No shares were issued to fund any of it; the only equity issuance
  is option exercises ($182M in fiscal 2025), and the 1999 Repurchase Program is expressly
  limited to the proceeds of those exercises.
- **[E2-60] NOT fired.** Dividends of $885M against fiscal 2025 owner earnings of $3,102M is
  a **29% payout**; against the conservative five-year mean of $2,057M it is **43%**. There
  is no restricted-earnings distribution here. **This is the cleanest leg in the file.**
- **The buyback is the capital-allocation story, not the dividend.** Filed, verbatim:

  > "During 2024, we funded $5.0 billion and received a $4.0 billion initial delivery of
  > approximately 65.6 million Kroger common shares at an average price of $61.54 per share
  > … In total, we invested $5.0 billion to repurchase **75.6 million shares of Kroger
  > common stock at an average price of $66.68 per share**"
  > "During 2025, we invested $2.7 billion to repurchase **41.8 million shares … at an
  > average price of $65.21 per share**"
  > "During 2023, we invested $62 million to repurchase 1.3 million shares … at an average
  > price of $46.98 per share" — FY2025 10-K, MD&A, acc. 0001104659-26-037723

  **$7.5bn deployed across fiscal 2024–25 at a blended ~$66 against a $57.94 quote today:
  a 12% mark in under two years.** Scored properly at Q3.

**LEG PASSES**, with the buyback price carried forward as a live flag.

## (c) THE BOOM WINDOW — AND THE INSTABILITY, WHICH IS THE OPERATOR'S FIRST QUESTION

**The operator's nine-year series is verified against the filed statements, not inherited.
Every year ties.** "Capital acquired" is cash capex **plus** finance-lease right-of-use
additions, the convention set by `ADDENDUM 2026-09-01 - finance-lease additions omitted from
(c) in the COST and HD runs`. Sources: filed *Consolidated Statements of Cash Flows* in the
FY2026, FY2025, FY2024, FY2022 and FY2019 10-Ks, cross-read against `companyfacts` pulled
2026-09-01 from `https://data.sec.gov/api/xbrl/companyfacts/CIK0000056873.json`.

| fiscal (period end) | wks | OCF | SBC | D&A | cash capex | +FL adds | **capital acquired** | **OE** | operator |
|---|---|---|---|---|---|---|---|---|---|
| 2017 (2018-02-03) | **53** | 3,413 | 151 | 2,436 | 2,809 | — | 2,809 | **453** | 453 ✓ |
| 2018 (2019-02-02) | 52 | 4,164 | 154 | 2,465 | 2,967 | — | 2,967 | **1,043** | 1,043 ✓ |
| 2019 (2020-02-01) | 52 | 4,664 | 155 | 2,649 | 3,128 | 233 | 3,361 | **1,148** | 1,148 ✓ |
| 2020 (2021-01-30) | 52 | 6,815 | 185 | 2,747 | 2,865 | 190 | 3,055 | **3,575** | 3,575 ✓ |
| 2021 (2022-01-29) | 52 | 6,190 | 203 | 2,824 | 2,614 | 753 | 3,367 | **2,620** | 2,620 ✓ |
| 2022 (2023-01-28) | 52 | 4,498 | 190 | 2,965 | 3,078 | 656 | 3,734 | **574** | 574 ✓ |
| 2023 (2024-02-03) | **53** | 6,788 | 172 | 3,125 | 3,904 | 168 | 4,072 | **2,544** | 2,544 ✓ |
| 2024 (2025-02-01) | 52 | 5,794 | 175 | 3,246 | 4,017 | 157 | 4,174 | **1,445** | 1,445 ✓ |
| 2025 (2026-01-31) | 52 | 7,311 | 157 | 3,332 | 3,855 | 197 | 4,052 | **3,102** | 3,102 ✓ |

**Nine-year capital acquired ÷ D&A = 1.225×** (operator's 1.22×, verified). Every one of the
nine years is above 1.0×; the range is 1.11× to 1.30×.

### WHERE THE INSTABILITY ACTUALLY SITS — and the GM lesson applied

*The GM run of 2026-09-01 found a screen distortion sitting on the income statement rather
than the cash-flow statement. The transferable lesson is to locate the distortion before
assuming which line is wrong. **On Kroger it is not the income statement and it is not the
capex line. It is one block inside operating cash flow: "Changes in operating assets and
liabilities."*** Every figure below is transcribed from the filed cash-flow statements.

| fiscal | working-capital block, **ex** the ASC 842 lease line | ASC 842 net effect on OCF | the one-line explanation, from the filing |
|---|---|---|---|
| 2017 | **−1,141** | n/a (pre-842) | includes a **−$1,000M discretionary contribution to company-sponsored pension plans**, plus a −$265M store-deposits-in-transit swing on the 53rd week |
| 2018 | +301 | n/a | includes a further −$185M pension contribution |
| 2019 | +327 | +1 | includes +$295M "proceeds from contract associated with sale of business" |
| 2020 | **+2,093** | +74 | **accrued expenses +$1,382M and "Other" +$699M — the pandemic.** ID sales ex-fuel **+14.1%** that year |
| 2021 | +389 | −13 | the pandemic float beginning to unwind; ID sales ex-fuel **+0.2%** |
| 2022 | **−2,571** | −8 | **inventories −$1,370M** on the inflation spike (LIFO charge $626M, the highest in the series), "Other" −$585M, taxes −$190M |
| 2023 | **+1,503** | −70 | **"Other" +$772M**, substantially the opioid settlement accrued but not paid; 53 weeks, worth **$179M pre-tax** on the company's own figure |
| 2024 | −403 | −6 | receivables −$288M, prepaid −$166M; and **$684M pre-tax of cash merger-related costs** sit inside OG&A |
| 2025 | +199 | +59 | a benign year; **$246M of the $350M Ocado termination payment was routed through *financing*, not operating** |

**Answering the operator's four questions in order.**

1. **How much is working capital? Almost all of it.** The block swings from **+$2,093M
   (fiscal 2020) to −$2,571M (fiscal 2022) — a $4,664M swing against a nine-year mean owner
   earnings of $1,834M.** Nothing else in the series is remotely that large. **But over the
   full nine years the same block nets to +$697M cumulative, or +$77M a year — essentially
   zero.** That is the payables-financed grocery model working: accounts payable of
   $10,488M exceed FIFO inventory of $9,445M, so suppliers fund the entire stock and $1bn
   besides, and unit growth *releases* working capital rather than consuming it.
   **[E2-23]'s LIFO carve-out applies literally here** — "businesses following the LIFO
   inventory method usually do not require additional working capital if unit volume does
   not change", and Kroger's US inventory is on LIFO with unit volume falling. **The
   violent year-to-year swings are timing. The nine-year mean is the least distorted
   window, and the corpus's "average annual amount" is precisely the remedy [E2-23].**
2. **How much is the 2020–21 stimulus period?** Fiscal 2020 alone. ID sales ex-fuel
   **+14.1%**, then **+0.2%** the following year — the filing's own numbers, and the
   two-year stack tells you the first year was borrowed from the second. **Fiscal 2020's
   $3,575M of owner earnings is roughly $2.1bn of working-capital inflow on top of a
   normal year; strip it and fiscal 2020 is a ~$1.5bn year. [E4-41] requires favourable
   exogenous breaks named and removed before the mean is trusted — and it is named here.**
   **It is also already out of both the three- and five-year windows.** The fiscal-2022
   trough is the *reversal* of the same event and is equally artificial in the other
   direction. **They cancel, which is exactly why the multi-year mean is the answer and the
   single year is not.**
3. **How much is fuel? Large in revenue, and UNKNOWABLE in profit.** Supermarket fuel sales
   ran **$16,621M → $14,973M → $13,584M** across fiscal 2023–25 (a **−18% three-year
   slide**, entirely price: fiscal 2025 saw "a decrease in the average retail fuel price of
   6.1% and a decrease in fuel gallons sold of 3.4%"), then **+21.3% in Q1 fiscal 2026** on
   "an increase in the average retail fuel price of 22.7%". **Fuel is 9.2% of sales and its
   dollar swing is ±$1.5–3.0bn a year.** But **Kroger has never disclosed fuel gross profit
   or fuel operating profit in any filing read for this run.** It discloses only that fuel
   "lower[s] our FIFO gross margin rate" and "lower[s] our OG&A rate", and reports every
   rate metric ex-fuel. Under the four-verdict test the separating question is asked aloud:
   *can I name the document that would resolve this?* **No — no filing Kroger makes contains
   the number, and no peer filing measures Kroger. The fuel profit contribution is
   UNKNOWABLE from primary filings**, recorded per the absence-claim rule as *no instance
   found in the documents read*. **What can be said is that fuel is not the source of the
   owner-earnings instability**: the fuel *revenue* slide of fiscal 2023–25 ran in one
   direction across three years while owner earnings went 2,544 → 1,445 → 3,102. The shapes
   do not match. **The volatility the operator asked about is working capital, not fuel.**
4. **How much is real?** Set beside all of the above, the genuinely recurring series is
   remarkably narrow. **Kroger's own adjusted FIFO operating profit — the operating result
   before every one of these cash-timing effects — reads $4,056M, $4,310M, $5,079M,
   $4,986M, $4,674M, $4,905M across fiscal 2020–25.** A six-year range of 4.1 to 5.1, peak
   in fiscal 2022, and **fiscal 2025 still below the fiscal 2022 peak three years later**.
   *That* is the real business, and it is flat. **The 57% spread in owner earnings is an
   artefact of cash timing sitting on top of an operating result that has not moved.**

**VERDICT ON THE INSTABILITY: DETERMINABLE, and therefore NOT a Q4 UNKNOWABLE.** The width
is explained, its two largest components (fiscal 2020's pandemic inflow and fiscal 2022's
reversal) are named and cancel, and the underlying operating series is stable enough to
price. **The range is carried in full at Q4 per [E4-25] and it does not close the file.**
**[E3-55] is the governing scope: volatility with a certain mechanism is not a defect** —
here the mechanism is payables timing, it is understood, and the endgame is arithmetic.

**LEG PASSES. No leg of Stage 0 fails; the run continues.**

---

## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32] — issuing authority
first, per the CLAUDE.md correction of 2026-09-02:**
- **USD 30-year: 5.27% · 2026-09-01 · U.S. Treasury daily par yield curve, "30 Yr" column,
  home.treasury.gov** — the issuing authority itself. The 2026-09-02 print was not yet
  posted at fetch time. FRED DGS30 (the fallback) read 5.25% at 2026-08-31, consistent.
- **The screen used 5.18%. This run uses 5.27%, +9bp, and the difference is carried.**
- Kroger earns and reports **entirely in USD**: "All of the Company's operations are
  domestic" (Note 16, Segment Reporting). No FX, no ADR ratio.
- Price $57.94, 2026-09-01 (aggregator, live quote only, flagged).

**The filing was read, not tagged data [E3-27, E4-14]:**
- **Form 10-K for the fiscal year ended January 31, 2026, filed 2026-03-31, accession
  0001104659-26-037723**, primary document `kr-20260131x10k.htm`. Audited by
  **PricewaterhouseCoopers LLP**, unqualified.
  [x] **MD&A** (value creation model, 2025 executive summary, non-GAAP definitions and the
  full adjusted-items list, total sales and the fuel split, identical sales, gross margin
  and LIFO, OG&A, operating profit, net interest, income taxes, ROIC, critical accounting
  estimates including multi-employer pensions, liquidity, capital investments, storing
  activity, debt management, repurchase programs, dividends, material cash requirements,
  factors affecting liquidity, Item 7A market risk)
  [x] **cash-flow statement including its detail lines** (every adjustment and every
  working-capital line for three years, the capital-investment reconciliation, and the
  supplemental cash interest and cash tax lines)
  [x] **footnotes** (Note 1 policies · Note 2 goodwill · Note 4 income taxes · Note 5 debt
  and the credit facility covenant · Note 6 derivatives · Note 7 fair value · **Note 11
  leases and lease-financed transactions** · **Note 12 commitments and contingencies incl.
  opioids** · Note 13 stock · Note 14 company-sponsored benefit plans · **Note 15
  multi-employer pension plans** · **Note 16 segment reporting** · Note 17 Kroger Specialty
  Pharmacy · **Note 18 termination of merger with Albertsons** · **Note 19 fulfillment
  network asset impairment**)
- Also read in full, with accessions: **10-Q Q1 FY2026** (quarter ended 2026-05-23, filed
  2026-06-26, acc. **0001104659-26-078236**); **10-K FY2024** (acc. **0001558370-25-004267**),
  **FY2023** (acc. **0001558370-24-004603**), **FY2021** (acc. **0001558370-22-004595**),
  **FY2018** (acc. **0001558370-19-002756**) for the nine-year cash-flow detail;
  **DEF 14A filed 2026-05-13, acc. 0001104659-26-060250**; and five 8-Ks —
  **2024-12-11 Item 1.02 merger termination** (acc. **0001104659-24-127669**),
  **2025-03-03 Item 5.02 CEO resignation** (acc. **0001104659-25-019465**),
  **2025-11-18 Item 2.06 material impairment** (acc. **0001104659-25-113746**),
  **2026-03-05 Q4/FY2025 results and FY2026 guidance** (acc. **0001104659-26-023800**),
  **2026-06-18 Q1 FY2026 results** (acc. **0001104659-26-075395**).
- **Figure cross-checked against the filed statement, four ways:** fiscal 2025 net cash
  provided by operating activities. The filed *Consolidated Statements of Cash Flows* reads
  **7,311**; the MD&A liquidity table reads **7,311**; the MD&A narrative reads "We
  generated **$7.3 billion** of cash from operations in 2025"; XBRL `companyfacts` reads
  **7,311,000,000**. **A discrepancy is recorded rather than smoothed: the 2026-03-05
  Ex-99.1 Table 8 reads $7,273M for the same line** — a $38M revision between the earnings
  release and the 10-K, immaterial (0.5%), and the audited 10-K figure governs. Second
  cross-check: fiscal 2025 sales **$147,642M**, identical in the filed income statement, the
  MD&A total-sales table and Note 16.
- **52/53-week artifact: PRESENT, twice, and handled.** Fiscal 2017 and fiscal 2023 were
  53-week years. The company quantifies the fiscal 2023 extra week at **$179M pre-tax /
  $144M net / $0.20 of EPS** and publishes an ex-extra-week column; fiscal 2017's extra week
  is not separately quantified and is flagged where it bears.

---

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, without management's language.** Kroger buys groceries
  from about the same manufacturers as everyone else, marks them up **22.9%**, and sells
  **$147.6bn** a year through **2,697 supermarkets** in 35 states, of which 2,250 have a
  pharmacy and 1,731 have a fuel forecourt. It then spends **19.2% of sales** on wages,
  occupancy and utilities and **0.6%** on rent and **2.3%** on depreciation, which is why
  the whole enterprise keeps **1.28% of revenue as GAAP operating profit** and, on the
  company's own preferred measure, **3.32% as adjusted FIFO operating profit**. Four things
  ride on top of that thin retail base: a **pharmacy** whose price is set by third-party
  payors and now by federal statute; a **fuel** business that is a pure commodity
  pass-through at 9.2% of sales; **33 owned food plants** supplying about 20% of Our Brands
  units; and — the genuinely different one — **an advertising business**, Kroger Precision
  Marketing, which sells access to the purchase histories of 63 million households and
  contributes to **$1.5bn of "alternative profit"**, roughly **31% of adjusted FIFO
  operating profit**, at a margin the filing calls "attractive … relative to our traditional
  operations" but never quantifies.
- **The scarce input this business controls:** the physical store network's local density —
  2,697 boxes with the distribution centres and route economics behind them — and the
  purchase data it generates, **">95% of customer transactions are tethered to a Kroger
  loyalty card"** across 63 million households. Neither is easy to build. Neither, as Q2
  will show, is scarce enough.
- **Will the fundamentals look broadly the same in ten years?** Yes as to mechanism.
  Americans will buy groceries; someone will stock shelves and run forecourts; the
  arrangement will look much as it does now. The doubts are about **who captures the margin
  between the farm and the shopper** and about **how many units go through Kroger's doors**
  — Q2 and Q4 questions, not intelligibility failures.
- **Recorded as a limit, not a failure.** Kroger reports **one segment**: "The Company's
  retail operations, which represent substantially all of the Company's consolidated sales,
  are its only reportable segment." So the unit economics of pharmacy, fuel, media,
  eCommerce and manufacturing **cannot be separated from the filing**, and three of them are
  named as UNKNOWABLE later in this run. That is a disclosure limit on the *parts*; the
  *whole* is intelligible and the arithmetic is not complicated **[E3-27]**.
- **VERDICT: [x] IN.** "Relatively simple and stable in character" **[E3-31]**. Nothing here
  needs five months of study **[E4-46]**.

---

## Q2 — IS IT A FRANCHISE? **[E3-03]**

*This is the question the operator flagged as central, and grocery is the hardest case in
retail. It is answered at length, with the counter-case stated before the verdict, per
**[E4-51]**.*

- Needed or desired **[x]**. Food. The most needed product there is.
- Not price-regulated **[~] — partially, and the exception is growing.** The grocery aisle
  is unregulated. **The pharmacy counter is not.** Kroger's Q1 FY2026 identical sales carry
  "an unfavorable **130 basis point impact from the Inflation Reduction Act**", and FY2026
  guidance carries the same 130bp for the full year. Pharmacy is one of the two departments
  the company names as driving its sales growth, and its price is set by statute and by
  pharmacy benefit managers. **[E3-03] criterion 3 is met for the business as a whole and
  breached for a growing slice of it.** Recorded; not decisive.
- **No close substitute [ ] — FAILS, and it fails in the issuer's own words.**

### The subject's own denial of criterion 2

> "The operating environment for the food retailing industry continues to be characterized
> by the proliferation of local, regional, and national retailers, including both retail and
> digital formats, and **intense and ever-increasing competition** ranging from online
> retailers, mass merchants, club stores, regional chains, deep discounters, dollar stores,
> and ethnic, specialty and natural food stores. With the proliferation of grocery delivery
> — both by retailers and third-party delivery service providers — **customers have a wide
> range of retailers from which to choose.**"
> — FY2025 10-K, Item 1A, "Competitive Environment", acc. 0001104659-26-037723

That is **[E3-03]** criterion 2 answered in the negative by the company itself. It is not a
boilerplate risk factor buried in a list; **it is the entire "Competitive Environment"
disclosure**, and Item 1 incorporates it by cross-reference in place of any competition
discussion of its own.

### The physical series is the honest one — **[E4-55]**, and it reads five for five

Precision Steel's lesson is pounds falling while price rises hold dollar revenue level, and
Buffett calls that "a serious reverse, not likely to disappear in some 'bounce back'
effect." **Kroger discloses the same thing about itself, in the same clause, in five
consecutive reported periods.** Verbatim, from the identical-sales explanation in each
filing:

| period | filed explanation of identical sales |
|---|---|
| fiscal 2022 | "increased primarily due to an increase in the number of households shopping with us and an increase in basket value due to retail inflation, **partially offset by a reduction in the number of items in basket**" |
| fiscal 2023 | "increased primarily due to an increase in the number of loyal households shopping with us and an increase in basket value due to retail inflation, **partially offset by a reduction in the number of items in basket**" |
| fiscal 2024 | "increased primarily due to increases in total and loyal households shopping with us, increased Health and Wellness sales and digital sales, **partially offset by a reduction in the number of items in basket**" |
| **fiscal 2025** | "increased primarily due to increased pharmacy, eCommerce and Fresh sales and **increased spend per item, partially offset by a reduction in the number of units sold**" |
| **Q1 fiscal 2026** | "increased primarily due to increased eCommerce, pharmacy, Fresh and Our Brands sales and **increased spend per item, partially offset by a reduction in the number of units sold**" |

**Note the change in the last two rows: the disclosure moves from "items in basket" (a
per-trip measure that a rising household count could offset) to "the number of units sold"
(the total).** The physical series is negative and the dollar series is positive, and the
bridge between them is price. **The square footage agrees**: 180M → 182M → 180M sq ft across
fiscal 2023–25 with **50 stores closed operationally in fiscal 2025 alone**, store count
2,731 → **2,697**, and Q1 fiscal 2026: "Total supermarket square footage at the end of the
first quarter of 2026 **decreased 1.0%** from the end of the first quarter of 2025."

### The two-characteristic test **[E2-44]** — both halves fail

**1. "Can it raise prices even when product demand is flat and capacity is not fully
utilized?" No — and it is not trying to. Price is a permanent, declared outflow.**

The filed record: "our continued investments in lower prices for our customers" (fiscal
2017 and 2018 MD&As), "increased price investments" (fiscal 2025 gross-margin bridge), "**$5
billion in lower prices since 2003**" (2024-12-11 Ex-99.1, acc. 0001104659-24-127669), and
FY2026 guidance which "reflects our ability to **invest more aggressively in value for
customers**" (2026-03-05 Ex-99.1, acc. 0001104659-26-023800).

**This must be scored fairly, because it is exactly what Costco does and Costco cleared this
gate WIDE in this project on 2026-08-30.** For a low-cost retailer, giving price back is the
moat's funding, not a defeat — the COST run recorded the 11.1% gross margin as "enormous
unexercised price room, held back on purpose to widen the moat." **The distinguishing test
is whether the spending buys volume.** At Costco it does: paid members +6.3%, shopping
frequency +5%, renewal 92.3%. **At Kroger it does not: units fell in each of the last five
reported periods while the price investment ran.** The same act is moat-funding at one
company and margin-donation at the other, and the units series is what separates them.

**[E4-37]'s inverse metric confirms it.** The corpus measures a franchise by "the agony they
go through in determining whether a price increase can be sustained." Kroger does not hold
a prayer session before raising prices — it publishes a running total of the price it has
given away since 2003. That is a level below the agony case.

**2. "Can it grow dollar volume with only minor additional investment of capital?" No, and
the arithmetic is stark.** Sales without fuel: **$123,012M (fiscal 2020) → $134,058M (fiscal
2025)**, **+9.0% over five years = +1.73%/yr**, below food inflation over the same span. To
get it, Kroger consumed **$19,399M of capital acquired** (fiscal 2021–25, from the table at
Stage 0(c)) and **shrank the store estate** from 2,742 to 2,697 boxes and 182M to 180M sq ft.
**$19.4bn of capital bought $11.0bn of incremental non-fuel revenue at a ~1.3% net margin,
no unit growth, no square-footage growth, and no operating-profit growth.**

### Direction outranks existence — **[E4-32]**

| filed metric | fiscal 2020 | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|
| Adjusted FIFO operating profit, $M | 4,056 | 4,310 | **5,079** | 4,986 | 4,674 | 4,905 |
| Adjusted net earnings attributable, $M | 2,740 | 2,802 | 3,104 | **3,479** | 3,246 | 3,199 |
| Adjusted diluted EPS, $ | 3.47 | 3.68 | 4.23 | 4.76 | 4.47 | **4.85** |
| Diluted shares, M | 781 | 754 | 727 | 725 | 720 | **655** |
| ID sales ex-fuel | +14.1% | +0.2% | +5.6% | +0.9% | +1.5% | +2.9% |
| supermarkets | 2,742 | 2,726 | 2,719 | 2,722 | 2,731 | **2,697** |

**Adjusted operating profit peaked in fiscal 2022 and adjusted net earnings in fiscal 2023.
Only EPS still rises, and only because the share count fell 16% in three years.** The
direction test is answered: **the moat is not widening.** The one line that genuinely is
widening is alternative profit ($1.3bn → $1.35bn → $1.5bn) and eCommerce sales
(+12%, +11%, **+16%** to >$16bn) — and eCommerce is loss-making, on which see below.

### The commodity doctrine — **[E2-58]**, and it is the right lens for this industry

> "persistent over-capacity without administered prices (or costs) equals poor
> profitability" … long-run profitability set by "the ratio of supply-tight to supply-ample
> years" … the one exception is "a cost advantage that is both **wide and sustainable** …
> By definition such exceptions are few." — **[E2-58]**

US food retail is the textbook case: tens of thousands of supermarkets plus mass merchants,
clubs, dollar stores, hard discounters and delivery platforms, no administered price, and
net margins of 0.3% to 3.5% across the row below. **The only escape [E2-58] permits is a
wide and sustainable cost advantage. Kroger does not have one — the competitor row shows it
is on the wrong end of the comparison against the two largest attackers.**

**[E3-62]'s second step applies to the capex, and it is the run's sharpest single finding.**
The corpus asks of any efficiency investment: *"how much is going to stay home and how much
is just going to flow through to the customer"* — in a commodity business the gains flow to
buyers. **Kroger answered that question against itself in writing.** Its FY2026 guidance is
built on eCommerce reaching profitability, "meaningful procurement efficiencies, and
productivity gains", and the stated use of them is "our ability to **invest more
aggressively in value for customers**." **The savings are pre-committed to the shopper.
Nothing is going to stick to the owners' ribs. That is the textile-loom lesson, filed.**

### THE COMPETITOR ROW — required **[E3-28]**. A moat is a claim about *relative* position.

All figures filing-sourced with accession numbers. Peer extractions saved to
`Test Runs/_research 2026-08-26/`. Where a fiscal year differs from Kroger's, the period end
is given.

| company (period end) | revenue $M | GAAP op margin | net margin | comp / ID sales | units / volume direction | stores | private label quantified? | multiemployer pension |
|---|---|---|---|---|---|---|---|---|
| **KROGER** (2026-01-31, acc. 0001104659-26-037723) | **147,642** | **1.28%** *(3.32% adj FIFO)* | **0.69%** *(2.17% adj)* | **+2.9%** ex-fuel | **NEGATIVE — "a reduction in the number of units sold"** | **2,697** | **yes, ">$39 billion"** ≈29% of non-fuel sales | **yes: $496M/yr; share of underfunding $1.2bn** |
| **Walmart U.S.** (2026-01-31, acc. WMT 10-K FY2026) | **482,975** | **5.21%** | n/d by segment | **+4.3%** | **POSITIVE — "reflected growth in unit volumes"** | 4,611 | **no** (Great Value not quantified) | **no** |
| Walmart Inc. total (2026-01-31) | 713,163 | 4.18% | 3.12% | — | — | — | no | no |
| **Albertsons** (2026-02-28, acc. ACI 10-K FY2026) | **83,173** | **0.87%** | **0.26%** | **+2.0%** ex-fuel | not disclosed | 2,244 (+405 fuel) | **no** ("more than 14,000 unique items") | **yes: $583.3M/yr, ~$610M guided; 16 of 28 plans "Critical"** |
| **Publix** (2025-12-27, acc. PUSH 10-K FY2025) | **63,209** | **7.32%** | **7.49%** | **+3.5%** | not disclosed | **1,390** | no | **no** |
| **Costco** (2025-08-31, acc. 0000909832-25-000101) | 269,912 | 3.85% | 3.00% | **+6%** (+8% ex gas/FX) | **POSITIVE — frequency +5%** | 914 | no (Kirkland share not quantified) | no |
| **Target** (2026-01-31, acc. TGT 10-K FY2026) | 104,780 | 4.88% | 3.54% | n/d here | — | ~1,980 | no | no |
| **Dollar General** (2026-01-30, acc. DG 10-K FY2026) | 42,724 | 5.16% | 3.54% | n/d here | — | ~20,600 | no | no |
| **Sprouts** (2025-12-28, acc. SFM 10-K FY2025) | 8,806 | 7.79% | 5.95% | n/d here | — | ~475 | no | no |
| **Casey's** (2026-04-30, acc. CASY 10-K FY2026) | 17,561 | n/d | 4.07% | — | — | ~2,900 | no | no |

- **Peers named: 8, from a US food-retail set this run counts at 12 at scale.** The four not
  taken are **H-E-B, Aldi, Trader Joe's and Wegmans** — all private or subsidiaries of
  foreign parents, **none of which files anything with the SEC**. Under the four-verdict test
  that is **UNKNOWABLE, not UNRESEARCHED**: no document exists on this project's shelf that
  would resolve them. Stated per the absence-claim rule as *no instance found in a search of
  EDGAR full-text and company indices*. **Ahold Delhaize** files with Euronext, not the SEC,
  and is likewise out. **Their absence does not make the moat PROVISIONAL**, because the two
  attackers that matter most — Walmart and Costco — are both fully filed and both in the row.
- **The row's limit, stated [E3-61]:** it shows position, not conduct. Identical structures
  produce opposite outcomes and the row cannot predict how these managements will behave.

### What the row establishes — four findings, and the first is decisive

1. **Same fiscal year, same end date, same country, opposite answer on the only question
   that matters.** Walmart U.S. and Kroger both closed their fiscal years on **2026-01-31**.
   Walmart U.S. grew comparable sales **+4.3%** and states, verbatim, that they "reflected
   **growth in unit volumes** and strength in all merchandise categories." Kroger grew
   identical sales **+2.9%** and states, verbatim, that it was "**partially offset by a
   reduction in the number of units sold**." **Walmart U.S. earns a 5.21% operating margin.
   Kroger earns 1.28% GAAP and 3.32% on its own adjusted measure.** The largest competitor
   is growing faster, on more units, at 1.6× the margin, in the same twelve months.
   **That is what stops a customer shopping at Kroger: nothing, and they are going.**
2. **The regional operator earns more than twice Kroger's margin.** Publix — 1,390 stores in
   eight states, no fuel forecourts of consequence, no automated warehouses, no national
   scale — earns a **7.32% operating margin and 7.49% net margin on comparable store sales
   of +3.5%.** Kroger, with 2× the stores and 2.3× the revenue, earns 1.28%. **National
   scale in grocery is not producing a cost advantage over a well-run regional. That is
   [E2-58]'s exception failing its own test.** The fair caveat is recorded: Publix owns most
   of its real estate, operates in one high-growth region, and is essentially non-union —
   which is the *point*, not an excuse, and leads directly to finding 4.
3. **Every listed peer earns more than Kroger, and the closest one earns less.** On GAAP
   operating margin: Sprouts 7.79%, Publix 7.32%, Dollar General 5.16%, Walmart U.S. 5.21%,
   Target 4.88%, Costco 3.85%, **Kroger 1.28%**, Albertsons 0.87%. Only Albertsons — the
   company Kroger tried to buy, and the one most like it — sits below. **Kroger's cost
   position is at the bottom of its own peer group on filed numbers, and its nearest twin is
   worse.** That is the structure of the industry, not a Kroger-specific failure, which is
   precisely why it is a **[E2-58]** finding rather than a management finding.
4. **The cost disadvantage has a name, and only Kroger and Albertsons carry it.** Kroger
   employs **"more than 403,000 full- and part-time employees"**, of whom **"more than
   two-thirds … are covered by collective bargaining agreements"** across **"approximately
   350 such agreements"**. It contributes **$496M a year to multi-employer pension plans**
   plus **$1,241M a year to multi-employer health and welfare plans** — **$1,737M a year, or
   35% of adjusted FIFO operating profit** — and carries an estimated **$1.2bn share of
   multi-employer underfunding** with a contingent withdrawal liability on top. **Albertsons
   carries the same: $583.3M of contributions, ~$610M guided, and 16 of its 28 plans
   classified "Critical" or "Critical and Declining."** **Walmart, Costco, Publix, Target,
   Dollar General, Sprouts and Casey's carry none of it.** In an industry where the whole
   operating margin is 1–5% of sales, a 1.2-point structural cost the two largest attackers
   do not bear is not a detail. **It is the reason the row reads the way it does.**

### The one genuine moat candidate, tested — Our Brands

**This is the strongest asset in the file and it is tested rather than assumed.** Verbatim:

> "**Our Brands products play an important role in our merchandising strategy and
> represented over $39 billion of our sales in 2025.** We own 33 food production plants,
> primarily bakeries and dairies, which supply approximately **20%** of Our Brands units
> sold in our supermarkets; the remaining Our Brands items are produced to our strict
> specifications by outside manufacturers." — FY2025 10-K, Item 7

**Against Kroger's own disclosed total sales to retail customers without fuel of $132,712M,
"over $39 billion" is over 29.4% of non-fuel retail sales** (arithmetic ours; floored,
because the disclosure says "over"). **That is a real and industry-leading number** — the
GIS run of 2026-09-01 could not obtain a comparable figure from Costco or Walmart, both of
which decline to quantify Kirkland Signature and Great Value, and it is the mechanism that
closed the General Mills file. **Kroger is on the winning side of that trade.**

**Three things must be said against it, and they are why it does not carry Q2.**

- **The series is not clean.** "Nearly $28 billion" (fiscal 2021) → "over $31 billion"
  (2023) → "over $32 billion" (2024) → "**over $39 billion**" (2025). A **$7bn, 5-point
  jump in a single year** while total non-fuel sales grew 1.3% is not organic mix shift.
  **The filing states no basis for the measure and never defines it.** Under **[E2-26]** the
  half-owner test asks whether the reporting tells me what I would want to know: on the
  single metric this run identifies as the moat candidate, **it does not.** Recorded as a
  candour gap at Q3 and as a reason not to underwrite the level.
- **Vertical integration is going the wrong way.** The share of Our Brands units made in
  Kroger's own plants fell **30% (fiscal 2023) → 31% (2024) → 20% (2025)** while the plant
  count stayed at 33. **Four-fifths of the "own brand" is now made by contract
  manufacturers to specification — which is a sourcing arrangement any competitor of scale
  can replicate, and Walmart, Costco, Aldi and Target all have.** The proprietary part of
  the asset is shrinking.
- **It has not shown up in the margin.** Private label carries a higher gross margin than
  national brands. Our Brands penetration rose ~5 points in one year and **the FIFO gross
  margin rate ex-fuel rose 44bp, of which the filing attributes the majority to the
  *disposal* of Kroger Specialty Pharmacy** — "Excluding the effect of fuel, the Labor
  Dispute **and Kroger Specialty Pharmacy**, our FIFO gross margin rate increased **14 basis
  points**." **And in the newest quarter it went into reverse: Q1 fiscal 2026 FIFO gross
  margin ex-fuel decreased 9 basis points** while OG&A rose 16bp. **A moat that is widening
  in share and not in margin is [E3-62]'s pass-through: the gain went to the customer.**

### The remaining Q2 tests

- **The dominance class [E2-53]: NO.** "Once dominant, the newspaper itself, not the
  marketplace, determines just how good or how bad the paper will be. Good or bad, it will
  prosper." Nothing about Kroger prospers good or bad. Its economics are set by Walmart's
  price file, by the union contracts under negotiation in any given year, by fuel spreads,
  and by pharmacy reimbursement statute. **The filing says so itself: "intense and
  ever-increasing competition."**
- **The second question about the business is a number [E3-46], and this is the strongest
  fact for the defence.** Kroger's own ROIC — a rent-and-D&A-added-back measure, computed on
  a $73.8bn invested-capital base — reads **12.36% (fiscal 2025) and 12.23% (fiscal 2024)**,
  stable. On **[E2-43]**'s denominator, unleveraged net tangible assets: total assets
  $49,953M less goodwill $2,595M, intangibles $808M and cash $3,334M = $43,216M of tangible
  operating assets; less non-debt operating liabilities of $19,325M (payables $10,488M +
  accrued wages $1,267M + other current $3,886M + deferred taxes $1,094M + pension $421M +
  other long-term $2,169M) = **$23,891M of net tangible assets**. Adjusted FIFO operating
  profit of $4,905M taxed at the company's guided 23% = **$3,777M → 15.8% after tax**.
  **That is a genuinely good return and it is stated as such.** It is not, however, "very
  high returns on capital employed over time" — it is the **[E5-40]** "quite satisfactory"
  band, on a base that is not growing.
- **Untapped pricing power [E3-33] / near-monopoly [E5-28]: NO, and the opposite.**
  Claiming this class would be claiming near-monopoly. Kroger did not leave price on the
  table; it publishes the cumulative total it has handed over and promises more.
- **Continuously rebuilt? [E4-04], scoped as v4.1 scopes it.** The test is whether a lapse
  in spending *destroys* the structure or merely *narrows* it, and whether the spending
  defends the same advantage or **buys its replacement**. **Both are happening, and the
  second is the one that matters.** The 278–285 remodels a year at ≥$8/sq ft defend the same
  stores — legitimate maintenance, the Coca-Cola case **[E3-49]**. But the **automated
  fulfillment network was an attempt to buy a *replacement* advantage — a new basis for the
  moat in delivery — and it was written off for $2,497M in a single year.** Under
  **[E4-04]** as scoped, a moat whose basis must be periodically replaced by purchase is the
  excluded class, and Kroger just demonstrated the exclusion at a cost of $2.5bn.
- **Key-person dependence [E4-23]: LOW, and recorded IN THE BUSINESS'S FAVOUR.** You do not
  need to know who runs Kroger for the Cincinnati store to sell milk. That is the Mayo
  Clinic side of **[E4-23]** and it is a real property of the asset. **It does not repair
  the franchise test.**
- **The attacker's test [E2-45] — the one forward-looking moat test the shelf carries.**
  With ample capital and skilled people, how would I compete with Kroger? **I would not need
  to try, because the attack has already been made, continuously, for twenty years, by five
  different attackers at once, and the filings show it working.** Walmart from above on
  price and now on units; Costco from above on stock-up trips at 3.85% margin and +6% comps;
  Aldi and Lidl from below on a 1,500-SKU box; Dollar General from below on the fill-in trip
  with 20,600 doors at 5.16% margin; Amazon and the third-party platforms on the delivery
  layer, which is the one Kroger spent $2.5bn trying to own and abandoned. **The correct
  answer to [E2-45] is not a strategy. It is the observation that no attack needs to be
  designed.**

### THE FAIR COUNTER-CASE, stated as its best advocate would state it **[E4-51]**

*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."*

**The bull case is not weak and it is not dismissed.** Kroger is 143 years old, has earned
positive net income in every filed year including 2008–09 and the pandemic, and generated
**$7.3bn of operating cash flow** last year — the highest in its history. It earns
**15.8% after tax on unleveraged net tangible capital** and **12.36% on its own fully-loaded
ROIC**, both stable, in a business where suppliers finance the entire inventory ($10,488M of
payables against $9,445M of FIFO stock). It holds a **loyalty franchise no competitor in the
row can match on disclosure — 63 million households, >95% of transactions tethered** — and
it has already monetised it: **$1.5bn of alternative profit, 31% of adjusted operating
profit, growing, with Kroger Precision Marketing profit up over 20%.** It has **$39bn of Our
Brands**, the largest quantified private-label franchise in the row, on the winning side of
the exact substitution that closed the General Mills file six days ago. **eCommerce grew 16%
to over $16bn** and management has now committed to **$400M of operating profit improvement
in fiscal 2026** by killing the sheds and running delivery off the store base — which is
what the asset-light bull case always said Kroger should do. **Identical sales accelerated
from +1.5% to +2.9%**, the executive summary claims "**Food volumes improved** … leading to
the final period of the quarter resulting in positive share gains", and management guides
adjusted EPS of **$5.10–$5.30** for fiscal 2026, which at $57.94 is **10.9–11.4× earnings**
with a 2.4% dividend and a fresh $2bn buyback. Net leverage is **1.76×**, comfortably below
the company's own 2.30–2.50× target and far below the 3.50× covenant. **A brand-new external
CEO with the strongest possible pedigree for this exact job — Greg Foran, formerly CEO of
Walmart U.S. — took the seat in fiscal 2025 and is redirecting capital from warehouses to
stores.** On that reading Kroger is a cheap, cash-generative, improving compounder in a
non-cyclical staple, with an underappreciated advertising business inside it.

**What defeats that reading is one thing the bull case cannot absorb, and it is not an
opinion — it is two filed sentences about the same twelve months.** Walmart U.S., fiscal
year ended 2026-01-31: comparable sales +4.3%, "**reflected growth in unit volumes**",
operating margin 5.21%. Kroger, fiscal year ended 2026-01-31: identical sales +2.9%,
"**partially offset by a reduction in the number of units sold**", operating margin 1.28%.
**A business whose customers believe there is no close substitute does not lose units to a
competitor that is simultaneously growing units, growing faster, and earning four times the
margin — while spending five years and $19.4bn of capital to prevent exactly that.** The
price investment is real, the private label is real, the media business is real, and after
all of them the shopper still put fewer things in the trolley for the fifth reporting period
running.

- Class: **[x] NONE at the enterprise level.** A narrow, local, real position exists in
  individual markets, and Kroger Precision Marketing is a genuinely narrow moat *inside* the
  business — but it is 31% of the profit riding on store traffic, and store traffic is the
  thing in question **[E4-23]**'s logic applied to an asset rather than a person.
  Direction: **NARROWING** on every observable — units, square footage, store count,
  adjusted operating profit (peak fiscal 2022), adjusted net earnings (peak fiscal 2023),
  operating margin against every listed peer, and gross margin in the newest quarter.
- **VERDICT: [x] OUT.** The franchise claim cannot be sustained. It fails **[E3-03]
  criterion 2** in the issuer's own words, fails **both halves of [E2-44]**, fails
  **[E4-32]**'s direction test, reads at the wrong end of **[E4-37]**'s inverse metric, shows
  **[E4-55]**'s falling-units signature in five consecutive periods, and sits at the bottom
  of its own competitor row on the metric **[E2-58]** says decides a commodity industry.
  **The entry run stops here. [E5-13]: most names should end here, and that is the system
  working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry. Q1 IN · Q2 OUT.** The hard sequence closes the file
for any BUY decision. No position exists, so no **[E2-28]** hold read is required. Everything
below is **FOR THE RECORD**, because the operator tasked the Albertsons rationality question,
the multiemployer quantification, the Ocado (c) judgment, the named way it dies, the floor
arithmetic and Q6 regardless. **Everything below carries operator rule 3's header:
COMPUTATION — NOT A CLEARANCE. Nothing below is entry language.**

---

## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?

*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless.
**Q3 can stop a run. It can never start one.***

### STEP 1 — THE WEIGHT CASE, declared first. Nothing below counts until this is filled in.

- [x] **Daily execution [E3-38] — TICKED.** Kroger is a retailer, the corpus's own named
  example of the class: *"For a retailer, hiring that nephew would be an express ticket to
  bankruptcy."* And here the margin for error is thinner than at Costco, where this project
  ticked the same box: **a 1.28% GAAP operating margin means a 130-basis-point cost error
  erases the entire profit.** 403,000 people, 2,697 stores, 350 collective bargaining
  agreements. Have-to-be-smart-every-day in its purest form.
- [x] **Leverage [E3-29] — TICKED.** $17,566M of total debt including finance leases plus
  $7,126M of operating lease liabilities against **$5,936M of total equity**. Debt to book
  equity **2.96×**; debt plus leases to equity **4.16×**. The equity is thin because $28.1bn
  of treasury stock has been bought back out of it, but thin is thin: **a single year's
  impairment moved book equity from $8,285M to $5,927M, a 28% reduction, with no cash
  leaving the building.** That is the proof that asset-side errors transmit straight to the
  equity.
- [ ] Control **[E1-16]** — no. Marketable minority; an exit exists.

**Two determinants high, so Q3 is a BINARY GATE and no price compensates [E3-38, E3-29,
E5-35]:** *"You can turn any investment into a bad deal by paying too much. What you can't
do is turn any investment into a good deal by paying little."*

### Honesty — the binary **[E5-16]**, and there is a real event to score

**A CEO resigned for personal misconduct, and it must be scored rather than mentioned.**
Verbatim, from the 8-K dated 2025-03-03, accession **0001104659-25-019465**:

> "On March 3, 2025, the Company announced that Rodney McMullen, the Company's Chairman and
> Chief Executive Officer, **has resigned from those positions, effective immediately.**
> On February 21, 2025, the Board of Directors was made aware of certain personal conduct by
> Mr. McMullen and **immediately retained outside independent counsel to conduct an
> investigation**, which was overseen by a special Board committee. **Mr. McMullen's conduct
> is not related to the Company's financial performance, operations or reporting, and it did
> not involve any Kroger associates.** In connection with his resignation, Mr. McMullen will
> **forfeit all unvested equity awards** … and will not be eligible to receive payment of a
> 2024 bonus."

And in the press release (Ex-99.1, same accession): conduct "**inconsistent with Kroger's
Policy on Business Ethics.**"

**[E5-16] says the tolerance for personal misconduct is zero. It was applied here, by the
board, to the CEO, in ten days.** **[E5-22]** supplies the test — *"the failure that counts
is they didn't act when they learned"* — and Kroger acted: outside counsel engaged
immediately, a special committee, resignation effective immediately, all unvested equity
forfeited and the bonus cancelled. **The forfeiture is visible in the filed numbers: a $21M
credit to OG&A in fiscal 2025 for "executive stock compensation for a former executive", and
"Compensation Actually Paid" to Mr. McMullen for fiscal 2025 of negative $27,697,216** (DEF
14A, acc. 0001104659-26-060250, pay-versus-performance table). **The board then went outside
the company for the first CEO in Kroger's 143-year history** — Greg Foran, formerly CEO of
Walmart U.S. — with the lead director serving as interim CEO in between.
**Recorded as the [E5-22] case passing, not as an integrity finding against current
management. [E5-26]'s Sokol calibration is noted: a decade of strong record preceded the
failure, and "it's generally a mistake to assume that rationality is going to be perfect,
even in very able people."**

**No other integrity disqualifier found.** *(Worded per the absence-claim rule: no instance
found in the documents read, not "none exists.")* **The sweep, named:** Item 3 Legal
Proceedings and Note 12 Commitments and Contingencies read in full — opioid litigation
(settled for up to $1,413M, disclosed and accrued in full in the year the agreement became
probable, with the payment schedule, the escrow mechanics and the balance-sheet split
published); the Albertsons Delaware Chancery litigation (below); wage-and-hour and personnel
class actions in the ordinary course; a Colorado labor dispute. **PwC unqualified on the
financial statements and on internal control over financial reporting.** No restatement, no
disclosed material weakness, no SEC enforcement matter found. One class of common stock, one
vote per share. **A pass here is the absence of found disqualifiers, never a clearance
[E5-17], and the filed statement is not bedrock [E5-32].**

### THE ALBERTSONS MERGER — the operator's rationality question, answered from the filings

**The facts, verbatim from Note 18 of the FY2025 10-K (acc. 0001104659-26-037723):**

> "on October 13, 2022, the Company entered into the Merger Agreement with Albertsons
> pursuant to which all of the outstanding shares of Albertsons common and preferred stock …
> automatically would have been converted into the right to receive **$34.10 per share** …
> The adjusted per share cash purchase price was expected to be **$27.25**."
> "On December 10, 2024 … the court issued a **preliminary injunction enjoining the
> consummation of the merger.**"
> "On December 11, 2024, the Company delivered a notice to Albertsons **terminating the
> merger agreement** … Kroger notified Albertsons that **Kroger has no obligation to pay the
> Parent Termination Fee** … because Albertsons failed to perform and comply in all material
> respects with its covenants."
> "On December 10, 2024, **Albertsons sued the Company in the Delaware Court of Chancery** …
> Albertsons seeks payment of a **$600** termination fee … **as well as additional damages,
> including expenses paid by Albertsons in connection with the Merger and the lost premium
> Albertsons alleges is owed to its shareholders** … On March 17, 2025, the Company filed an
> answer denying the allegations … and also filed **counterclaims**."

**The amounts, assembled from the filed statements. Every figure carries its source.**

| item | $M | where it is filed |
|---|---|---|
| merger-related costs expensed, fiscal 2023 | **316** | FY2025 10-K adjusted-items footnote (6) |
| merger-related costs expensed, fiscal 2024 | **684** | same; "primarily … third-party professional fees and credit facility fees" |
| merger-related net interest expense, fiscal 2024 | **34** | adjusted-items footnote (9) |
| merger-related litigation and settlement charges, fiscal 2025 | **161** | adjusted-items footnote (7) |
| financing fees paid, fiscal 2024 | **116** | filed cash-flow statement, financing section |
| redemption premium on the $4.7bn special-mandatory-redemption notes at 101% | **≈47** | Note 18: "redeemed the SMR Notes on December 18, 2024 at a redemption price equal to **101%** of the principal amount" (arithmetic ours on the filed $4,700M) |
| **identified pre-tax cost of a deal that never happened** | **≈1,358** | |

**And the cost that does not stop.** Kroger issued **$10,500M of senior notes on 2024-08-20**
to fund the merger. It redeemed **$4,700M** of them at 101% within four months. **$5,800M of
5.00% / 5.50% / 5.65% notes maturing in 2034, 2054 and 2064 remain outstanding, raised for
an acquisition that was blocked and spent instead on buybacks.** The consequence is on the
income statement: **net interest expense $441M (fiscal 2023) → $450M (fiscal 2024) → $639M
(fiscal 2025)**, a **$198M-a-year permanent step**, against adjusted net earnings of $3,199M.
**Kroger will be paying interest on the Albertsons merger until 2064.**

**The [E2-30] institutional-imperative reading, and it is the central Q3 finding.**

- [x] **(2) "corporate projects or acquisitions will materialize to soak up available
  funds" — FIRED, and then fired again in reverse within twenty-four hours.** The merger
  itself is behaviour (2) in its ordinary form: a $24.6bn acquisition of the only company in
  America structurally similar to the acquirer, pursued for 26 months against an FTC
  challenge, two state AG suits and a private class action. **What is remarkable is the
  second half.** The press release announcing the termination — same day, same accession
  0001104659-24-127669 — is headlined "**Kroger Reiterates Its Commitment to Lower Prices
  and Initiates New $7.5B Share Buyback Program**", and announces a **$7.5bn authorisation
  including a $5.0bn accelerated share repurchase**, with the stated rationale: "**Now that
  Kroger has terminated the merger agreement, the company is ready to deploy its capacity.**"
  **The size was set by the balance-sheet capacity built for the deal, not by the price of
  the stock.** **[E5-24]**'s first law — *"what is smart at one price is dumb at another"* —
  was not applied on the day; the capacity was.
- [x] **(3) "staff studies produced to justify the leader's craving" — cannot be observed
  from filings, but the artefact class is visible**: a **$17,400M bridge facility
  commitment**, a **$4,750M term loan credit agreement**, a **$7,442M exchange offer** for
  Albertsons' notes, and a **$10,500M bond issue** were all arranged, and all of them
  unwound. No finding is recorded against a box that filings cannot reach.
- [ ] **(1) resists any change in current direction — NO FINDING, and the honest read is the
  opposite.** Management killed the fulfillment network, sold Kroger Specialty Pharmacy and
  Vitacost.com, closed ~60 stores, cut ~1,000 corporate roles, and hired an external CEO.
  **That is a company changing direction, and it is recorded in its favour.**
- [x] **(4) peer behaviour mindlessly imitated — FIRED, narrowly.** The Ocado partnership
  (2018) was the sector's shared answer to Amazon/Whole Foods; Ahold, Sobeys and Ocado's
  other partners bought the same answer. **Kroger has now written off $2,497M of it, of
  which $948M was finance-lease assets** (Note 11) — i.e. the sheds were leased, capitalised,
  and impaired. **The $753M and $656M of finance-lease additions in fiscal 2021 and 2022 are
  those buildings**, which is how a fashionable capital commitment enters (c) and never
  comes out.

*The last clause of [E2-30] governs: **institutional dynamics, not venality or stupidity.**
This is not a fraud finding.*

**The counter-case on the merger, stated fairly [E4-51].** Kroger negotiated a **capped**
downside — a $600M parent termination fee, which it is contesting rather than paying. It
arranged a divestiture package designed to answer the FTC. Antitrust outcomes in that period
were genuinely uncertain and the FTC lost merger cases in the same window. And the
balance-sheet capacity built for the deal was redeployed rather than stranded. **A board that
declines a large acquisition it believes accretive because it *might* be enjoined is not
obviously behaving better.** The finding here is not that the attempt was irrational; it is
that **$1.36bn of identified cost, a $198M-a-year permanent interest step running to 2064,
and an open Chancery claim for $600M plus "the lost premium … owed to its shareholders" were
incurred by a business earning $4.9bn of adjusted operating profit, and that the capital
freed by the failure was committed to a buyback the same day at a price 12% above today's.**

**One more filed fact, from the counterparty, and it is the fairest available read of the
litigation's status.** Albertsons' own FY2026 10-K (acc. per `ACI_10K_FY2026`) states in its
risk factors that "legal proceedings are expensive and could result in significant costs to
us, including any costs we may be required to pay in connection with the legal proceedings
with Kroger. These significant costs, along with **our inability to collect the termination
fee of $600 million from Kroger**, could have a material adverse effect." **The plaintiff is
telling its own shareholders it has not collected. Kroger accrues nothing for the $600M and
states that "the aggregate range of loss for the Company's exposure is not material."** Both
statements are in filed documents and they cannot both be comfortable. **Carried to Q4 as a
named contingency and to Q6 as a watch item.**

### STEP 2 — THE FLAGS **[E4-22, E4-29, E5-15, E4-30, E2-49, E2-52, E3-50, E2-57, E3-53]**

- [ ] **Weak accounting — NOT fired, and the impairment behaviour is a point in favour.**
  SBC expensed in full ($157M). The $2,497M fulfillment charge was taken in one quarter,
  announced by an Item 2.06 8-K **before** the results (2025-11-18, acc.
  0001104659-25-113746, "approximately $2.6 billion"), and landed at $2,497M — **guided
  high, delivered lower.** The multi-employer underfunding estimate is published with its
  direction and its methodology and its limitations. LIFO disclosed and quantified every
  year.
- [ ] **Unintelligible footnotes — NOT fired.** Note 19 names the four sites by city, the
  trigger, the method, the fair-value approach, the $350M Ocado termination payment and
  **the exact split of that payment between financing ($246M) and operating ($104M) cash
  flow.** That is a level of specificity most filers do not offer.
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — FIRED, and structurally.** *"Trumpeting
  EBITDA … is a particularly pernicious practice … That's nonsense."* Kroger's **segment
  profit measure is literally EBITDA**: "The Company's CODM assesses performance and
  allocates resources for the retail operations segment using segment FIFO **earnings before
  net interest expense, income tax expense and depreciation and amortization ('EBITDA')**"
  (Note 16). Its **capital-structure target is an EBITDA multiple** — "our net total debt to
  adjusted EBITDA ratio target range is **2.30 to 2.50**" — and every guided metric (identical
  sales, FIFO operating profit, EPS, free cash flow) is non-GAAP. **The disclosure of the
  CODM measure is required by ASU 2023-07; the choice of the measure, and of an EBITDA
  leverage target, is management's.** In a business with **$3,332M of annual depreciation
  against $4,905M of adjusted operating profit**, deleting depreciation deletes 40% of the
  cost base. **[E5-41]**'s reverse float is exactly this asset class: the money was spent on
  the stores first and the expense is recorded later, and it is the expense EBITDA removes.
- [x] **The "except for" flag [E2-57] — FIRED, and it is quantified.** *"you must count the
  runs scored against you in all nine innings."* Kroger's **Adjusted Free Cash Flow** adds
  back **cash that actually left the building**: fiscal 2025 free cash flow of $3,418M
  becomes $3,868M by adding back $121M of merger litigation, **$105M of Ocado exit
  payments**, $57M of pension-restructuring payments and **$167M of opioid settlement
  payments** — **$450M of real cash, 13% of the figure.** Every one of those is a cost of
  decisions this management made. The pattern repeats: $722M added back in fiscal 2024,
  $331M in fiscal 2023. **This run's owner-earnings mean uses the unadjusted cash flows and
  the add-backs are refused [E5-33].**
- [x] **Restructuring / impairment cadence [E3-53] — FIRED.** Asset impairment and store
  closure charges appear on **every one of the last three filed income statements** — $69M,
  $98M, **$187M** — plus $2,497M of fulfillment impairment, $50M of intangible impairment,
  $47M of severance and $100M of store closures in fiscal 2025 alone. **[E5-33]: these are
  real costs of this business and they stay inside the owner-earnings mean**, which is why
  the mean is computed from operating cash flow and never from adjusted income.
- [x] **Trumpeted projections and growth targets [E4-22, E5-30] — FIRED as a practice, and
  the record is scored honestly, which means it is scored in management's favour.** Kroger
  publishes a full annual guidance suite **and** a standing long-term target: *"We expect our
  value creation model will result in **total shareholder return within our target range of
  8% to 11% over time**."* **[E4-35]** is explicit that lofty targets "corrode CEO behavior"
  and **[E5-30]** that a guidance culture is a ratchet — *"once you start it, it's all over."*
  **[E3-48] pulled and scored:**

  | FY | initial guidance (prior-year Q4 8-K) | outturn | score |
  |---|---|---|---|
  | 2024 | ID ex-fuel **0.25–1.75%**; Adj FIFO OP **$4.6–4.8bn**; Adj EPS **$4.30–4.50**; capex $3.4–3.6bn | ID **+1.5%**; Adj FIFO OP **$4,674M**; Adj EPS **$4.47**; capital investments **$3,623M** | **MET — inside every range** |
  | 2025 | ID **2.0–3.0%**; Adj FIFO OP **$4.7–4.9bn**; Adj EPS **$4.60–4.80**; capex $3.6–3.8bn | ID **+2.9%**; Adj FIFO OP **$4,905M**; Adj EPS **$4.85**; capital investments **$3,862M** | **BEAT — profit and EPS above the top** |
  | 2026 | ID **1.0–2.0%**; Adj FIFO OP **$5.0–5.2bn**; Adj EPS **$5.10–5.30**; FCF $2.7–2.9bn; capex $3.8–4.0bn | in progress; Q1 ID **+1.0%** (the bottom of the range); **reaffirmed** 2026-06-18 | — |

  **The flag is a prompt to read, and what the reading shows is a management that hits its
  numbers.** That is recorded plainly. **What it does not do is repair Q2** — **[E2-49]**'s
  yardstick was not discarded when the reading went bad, which is the candour case, and
  **[E2-37]**'s guardrail governs: a grocer that guides brilliantly is a remarkable grocer,
  not a remarkable business.
- [ ] **Serial share issuance [E5-15] — NOT fired; the reverse.** Diluted shares 958M (fiscal
  2016) → **655M (fiscal 2025)**, a 32% reduction, entirely by purchase.
- [ ] **Filed-figure tells [E4-30] — NOT fired.** Reported growth is visibly lumpy, not
  unnaturally smooth. Cash taxes paid: **$751M (fiscal 2023), $681M (2024), $635M (2025)**
  against pre-tax income of $2,836M / $3,342M / $1,200M. Fiscal 2025's cash tax of $635M
  **exceeds** the year's $176M of book tax expense, because the $2,497M impairment is not yet
  deductible. **The tell points the honest way: cash tax is running ahead of book tax, not
  behind it.**
- [ ] **Metric-switching [E2-49] — NOT fired.** Identical-sales, adjusted-FIFO and ROIC
  definitions are stable across the filed decade, each published with its own limitations
  paragraph, and the 53-week adjustments were disclosed and applied rather than used.
- [ ] **Stock-price targeting [E3-50] — NOT fired.** No statement of the [E3-50] premise
  found. The **8–11% TSR target** is adjacent to it and is recorded under the projections
  flag instead, where it belongs.
- [ ] **Dividends funded by issuance [E2-52] / restricted earnings [E2-60] — NOT fired.**
  Scored at Stage 0(b).
- [ ] **Consultant-driven or delegated allocation [E3-58] — not evidenced** in the documents
  read, though the bridge/term-loan/exchange-offer apparatus of 2022–24 is noted above.

**Flags that converge [E4-52].** Three fired and they point one way, which makes them one
reinforcing system rather than three prompts: **a segment and leverage framework built on
EBITDA in a business whose largest single expense is depreciation; a free-cash-flow measure
that adds back the cash consequences of management's own decisions; and impairment as a
recurring income-statement line.** Together they describe a reporting frame in which the cost
of capital already spent is systematically removed from the headline. **The offsetting facts
are equally real and are stated with them: guidance met and beaten, cash tax ahead of book
tax, an impairment guided high and delivered low, footnotes of unusual specificity, and a
32% share-count reduction with no issuance.**

### STEP 3 — THE PRIMARY TEST **[E2-01]**. Balance sheet before income statement.

**Nine years of balance sheet:** equity **$6,931M (fiscal 2017) → $11,615M (fiscal 2023) →
$8,285M (2024) → $5,927M (2025)**, the last two steps being **$6.9bn of buybacks** and a
**$2.5bn impairment**, not losses. Total debt including finance leases roughly $12–18bn
throughout, stepping up $5.7bn in fiscal 2024 for the merger and back down $339M in fiscal
2025. **Treasury stock at cost: $28,113M — nearly five times the remaining book equity.**

**ROE (net earnings attributable ÷ average equity):**

| fiscal | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| ROE | 41.6% | 20.1% | 28.4% | 17.4% | 23.0% | 20.0% | 26.8% | **14.3%** |
| **on adjusted net earnings** | — | — | 30.1% | 29.4% | 31.8% | 32.2% | 32.6% | **45.0%** |

**Scoped exactly as the corpus scopes it, and the scoping is the finding. [E2-47]** carves
out unusual debt-equity ratios and **[E2-43]** requires the denominator for leveraged filers
to be **unleveraged net tangible assets**, with the goodwill wedge separate.

| denominator | return | what it answers |
|---|---|---|
| book equity $5,927M | 14.3% GAAP / 45.0% adjusted | **inflated and rising for the wrong reason** — the denominator is being retired at $66 a share |
| **unleveraged net tangible assets $23,891M** | **15.8% after tax** on adjusted FIFO operating profit | **[E2-73]: judge the operators here.** They run a very large, very thin business on a reasonable return, and this is the honest number |
| **Kroger's own ROIC, $73,792M invested capital** | **12.36%** | management's own fully-loaded measure, stable at 12.2–12.4% |
| goodwill wedge | **$2,595M** — only 5.2% of assets | **recorded in Kroger's favour.** Unlike every packaged-food name in this project's files, Kroger's balance sheet is not a pile of unamortised intangibles. It is 49% net property and equipment. **There is no [E5-20] intangible artifact here.** |

### The half-owner test **[E2-26]** — genuinely mixed, and better than the flags suggest

**Passes, and these are real.** The units disclosure that convicts the franchise
("a reduction in the number of units sold") is in Kroger's own MD&A, unprompted. The
multi-employer underfunding estimate is published in dollars, net of tax, with the direction
of change, the ARP Act effect and an explicit statement of its unreliability. The opioid
settlement is disclosed with the payment schedule, the escrow mechanics and the
balance-sheet split. Note 19 gives the four closed sites by city. The credit-facility
covenant is **quantified**: "Our Leverage Ratio … was **1.54 to 1** as of January 31, 2026.
**If this ratio were to exceed 3.50 to 1**, we would be in default" — which the GIS run
found General Mills refusing to disclose at all. **That is [E2-67]-class candour on the
items that hurt.**

**Fails, on three specific things.** **(1) Fuel profit is never disclosed** for a business
that is 9.2% of sales and the acknowledged source of "volatility of fuel margins" in the
company's own forward-looking-statements list. **(2) The eCommerce loss is never
quantified** — the company says the review "is expected to deliver **$400 million in
eCommerce operating profit improvement in 2026, and establish a path to eCommerce
profitability**", which tells an owner that a business doing **over $16bn of sales, ~12% of
non-fuel revenue, is losing money**, and refuses to say how much. **(3) The Our Brands series
jumps $32bn to $39bn in one year with no stated basis**, on the single metric this run
identifies as the moat candidate.

### Buybacks and capital allocation **[E5-08, E4-31, E5-24, E5-31, E2-51]**

**Condition (1), ample funds for operations and liquidity: YES.** $3,334M of cash, $7,311M of
operating cash flow, net leverage 1.76× against a 3.50× covenant, $2.75bn undrawn revolver
and no commercial paper outstanding.

**Condition (2), a material discount to conservatively calculated intrinsic value: FAILS, but
narrowly and honestly.** $7.5bn was deployed in fiscal 2024–25 at a blended **~$66 a share**.
This run's conservative zero-growth value at the bare sovereign is **$63.72/sh** (five-year
mean, (c) at capital acquired) and **$73.22/sh** on the three-year window. **Kroger therefore
bought at roughly its own conservative zero-growth value — which is not a material discount,
but is a long way from the COST case where the mark was against a value three times below.**
→ **CAPITAL-ALLOCATION FLAG**, stated with the humility clause **[E4-13]**: management knows
this business far better than I do, and "many CEOs never stop believing their stock is cheap"
**[E5-08]**. **The flag binds position size, never the discount rate** — moot here, no
position. **[E2-51]'s refusal tell is not prosecuted: they did not refuse; they bought.**

**The sharper allocation finding is [E5-31]'s ordering, not the price.** The stated order is
business needs first, then acquisitions versus repurchases by per-share value added. Kroger
committed **$7.5bn to buybacks within twenty-four hours of the merger's collapse**, sized to
the capacity; then, eleven months later, wrote off **$2,497M** of the fulfillment network it
had been building for six years; and **now intends to lever up further** — its own target is
**2.30–2.50× against an actual 1.76×**, a gap worth roughly **$4.5bn of additional debt** at
the current $8,224M of adjusted EBITDA, with a further **$2.0bn authorisation approved
2025-12-23.** **Capital was allocated to the share count before the operating problem was
diagnosed, and the diagnosis when it came cost $2.5bn.**

**The retention test [E3-54], run on the company's own published series, and it is the
cleanest scorecard in the file.** Kroger publishes it: cumulative TSR, $100 invested
2021-01-30, through fiscal 2025 (10-K performance graph, and the same series in the DEF 14A
pay-versus-performance table):

| | fiscal 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|
| **The Kroger Co.** | 128.57 | 135.86 | 142.48 | 194.80 | **202.66** |
| S&P 500 | 121.00 | 112.98 | 139.92 | 172.78 | **201.03** |
| Peer Group | 118.08 | 114.43 | 133.33 | 193.49 | **217.65** |

**Kroger returned +102.7% over five years against the S&P 500's +101.0% and its own peer
group's +117.7%. It matched the index and lagged the peers.** By the letter of **[E3-54]**
(at least $1 of market value per $1 retained) it passes; by **[E2-37]**'s standard it is a
remarkable grocer, not a remarkable business.

**And the decomposition the operator asked for, which is where the retention test actually
bites.** Fiscal 2020 → fiscal 2025, five years, all figures filed:

| source of the ~15.2%/yr total shareholder return | contribution | evidence |
|---|---|---|
| **real earnings growth** | **+3.1%/yr** | adjusted net earnings $2,740M → $3,199M |
| **share retirement** | **+3.6%/yr** | diluted shares 781M → 655M |
| **multiple expansion** | **+5.5%/yr** | price/adjusted EPS 9.94× (2021-01-29, $34.50) → 12.96× (2026-01-30, $62.85) |
| **dividend** | **+2.4%/yr** | DPS $0.68 → $1.34 |

**Adjusted EPS grew 6.9%/yr, of which more than half — 3.6 points — is the share count.
Less than a quarter of the five-year return came from the business earning more money, and
more than a third came from the multiple.** **[E4-44]** is explicit: *"the value of an
asset, whatever its character, cannot over the long term grow faster than its earnings do."*
**The multiple term has already begun to give back — 12.96× at the fiscal year end, 11.95×
today — and there is no further multiple to spend.**

### THE GUARDRAIL

- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** Q2 is OUT and
  stays OUT **[E2-37, E2-38, E3-39]**. *"A textile company that allocates capital brilliantly
  within its industry is a remarkable textile company — but not a remarkable business."*
- [x] Key-person dependence is **low**, and that was recorded at **Q2** as a property of the
  business per **[E4-23]**, not here as a compliment to the managers.
- [x] **The excisable-cancer question [E2-35, E2-36], asked properly and answered.** The
  automated fulfillment network *looked* like a localised excisable cancer, and it has been
  excised — three sites closed, one cancelled, $2,497M written off, and a new external
  surgeon hired with the best possible CV for the operation. **But the corpus's test is
  whether the franchise is already intact and the damage local, or whether the manager is
  the plan.** Units are falling, square footage is falling, adjusted operating profit peaked
  three years ago, and the largest competitor is growing units at four times the margin.
  **The base business is not intact. The exception does not apply, and Greg Foran is
  therefore the plan rather than the surgeon — which [E2-36] says is the case not to buy.**
- **The ABCs [E5-45].** Recorded in Kroger's favour: this is a company visibly *fighting*
  arrogance, bureaucracy and complacency — 1,000 corporate roles cut, the sheds killed, the
  first outside CEO in 143 years. **The finding is not that the ABCs have metastasised; it is
  that the remedy is being applied to a business the row says is losing anyway.**

**Q3 FOR-THE-RECORD READ: no honesty disqualifier found, and the honesty side is genuinely
better than most names in this project's files** — the misconduct was acted on in ten days,
the covenant is quantified, the underfunding is published, guidance is met and beaten, and
cash tax runs ahead of book tax. **The gate would be a close call on rationality under a
weight case that is binary.** Fired: an EBITDA-based segment and leverage framework in a
depreciation-heavy business; an adjusted-FCF measure that adds back $450M a year of real
cash; impairment as a recurring line; **$1.36bn of identified cost and a $198M-a-year
interest step running to 2064 from a blocked merger**; and $7.5bn of buyback sized by
capacity within a day of that merger's collapse, at a blended price 12% above today's.
*A pass here would be the absence of found disqualifiers, never a clearance **[E5-17]**.
IN never promotes, and Q2 OUT stands regardless.*

**FOR-THE-RECORD VERDICT: would not clear on rationality. NOT OUT on integrity.**

---

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### The ASC 842 operating-lease test, run first, because the operator asked and because it is the one place a retailer's OCF can lie

**The SHOE run of 2026-09-01 established the test: transcribe both ASC 842 lines out of
operating cash flow and net them. Kroger's lease base is 25× Shoe Carnival's. It does not
lie here either, and the filing lets you prove it three ways.**

| $M | fiscal 2023 | fiscal 2024 | **fiscal 2025** |
|---|---|---|---|
| **add-back:** operating lease asset amortisation | +625 | +603 | **+588** |
| **deduct:** operating lease liabilities (cash paid) | −695 | −609 | **−529** |
| **net effect on operating cash flow** | **−70** | **−6** | **+59** |

**Cross-check from Note 11**, which discloses the cash line separately: "Cash paid for
amounts included in the measurement of lease liabilities — **Operating cash flows from
operating leases $855** (fiscal 2025), **$916** (fiscal 2024)." Against **operating lease
cost of $980M** (gross) / **$872M** (net of $108M of sublease and other rental income, which
is the "Rent" line on the income statement). **The three views agree: real cash of $855M went
out on operating leases and it is genuinely inside the $7,311M of operating cash flow. The
net ASC 842 inflation of fiscal 2025 OCF is +$59M — 0.8% of OCF and 1.9% of owner earnings.
Immaterial. The leg passes.**

**But the lease note carries a finding the cash-flow statement does not, and it is the Ocado
story in one line.** Note 11: **"Impairment of finance lease assets $954"** in fiscal 2025,
of which **"$948 related to the Company's automated fulfillment network."** The sheds were
leased, capitalised as finance leases, and impaired. **This is the direct evidence that the
$753M and $656M of finance-lease additions in fiscal 2021 and 2022 — 20% and 18% of those
years' capital acquired — were the automated warehouses.** It settles the (c) question below.
Note also **$415M of financing cash flows on finance leases in fiscal 2025** (including the
$246M Ocado termination) against only $197M of new finance-lease additions: on a pure cash
basis the finance-lease line consumed more than it added, and the "capital acquired"
convention counts the additions, not the payments. **Disclosed, and it errs against Kroger by
$218M in fiscal 2025 — i.e. the convention is the conservative one here.**

### Owner earnings — **COMPUTATION — NOT A CLEARANCE** **[E2-23]**

Convention applied: multi-year mean of **(operating cash flow − share-based compensation)
− (c)**, because operating cash flow nets the working-capital increment from one audited
line. **[E2-23]**'s LIFO carve-out is applied and discussed at Stage 0(c). Never a net-income
proxy. The nine-year series is verified at Stage 0(c) and every year ties.

**MORE THAN ONE WINDOW, AND THE SPREAD IS PART OF THE RANGE [E4-25], with every window
published per [E4-38]:**

| (c) basis | 3-yr mean (fiscal 2023–25) | 5-yr mean (fiscal 2021–25) | 9-yr mean (fiscal 2017–25) |
|---|---|---|---|
| **(c) = capital acquired** | **$2,364M** | **$2,057M** | **$1,834M** |
| **(c) = full D&A** | $3,229M | $2,838M | $2,478M |

**Bottom boundary $1,834M (9-yr, capital acquired); top $3,229M (3-yr, D&A). Full spread
+76%. The operator's stated 57% is the 5-yr-to-3-yr version and it is confirmed:
$2,057M → $3,229M.** The window spread alone, at the conservative end, is **+29%**
($1,834M → $2,364M).

### **MAINTENANCE CAPEX — THE DISCLOSED JUDGMENT, made explicitly [E2-23, E3-44, E2-41, E5-20]**

*(c) must be a guess. Here is the guess and its full reasoning, and the operator was right
that the direction must be argued rather than assumed.*

**The corpus default is D&A [E3-44, E2-41].** The exception class is a business "whose own
filing says depreciation understates renewal", where the D&A end is **INVALID** and (c) is
judged up from total capex **[E5-20]**. **Kroger belongs in the exception class, and the
argument is entirely from filed numbers.**

1. **Capital acquired has exceeded D&A in every one of the nine years, 1.11× to 1.30×,
   averaging 1.225×.** Nine years is not a cycle artefact.
2. **And it did so while the estate SHRANK.** Store count 2,742 (fiscal 2020) → **2,697**;
   square footage 180M → 182M → **180M**, and −1.0% year-on-year in Q1 fiscal 2026;
   **50 stores closed operationally in fiscal 2025.** **Capex above depreciation with no unit
   growth is renewal, not growth.** That is the single strongest argument for the capex end
   and it is decisive.
3. **The forward number confirms it and kills the obvious objection.** The obvious objection
   is that trailing capex is inflated by the now-dead fulfillment programme — and it is:
   $948M of finance-lease assets plus the real estate and equipment inside the $2,497M
   charge, concentrated in fiscal 2021–24. **But Kroger's own FY2026 guidance is capital
   expenditure of $3.8–4.0bn against D&A of $3,332M — 1.14× to 1.20× — with the shed
   programme dead and square footage still falling.** The Q1 fiscal 2026 print is already
   $1,293M of cash capex against $989M of D&A, **1.31×**. **The capital is being redirected
   from warehouses to stores, not released.** Management is not claiming the maintenance
   requirement falls; it is telling owners it rises.
4. **The filing names a mandated renewal cost.** "As a result of current state and federal
   requirements regarding the phasedown of hydrofluorocarbon ('HFC') refrigerants, **we are
   steadily replacing our refrigerant infrastructure to reach required levels, which incurs
   capital costs to the business.**" That is a filed statement of renewal spending on
   already-depreciated assets.
5. **[E4-47]'s inflation condition applies.** Depreciation on stores built ten and twenty
   years ago is charged in old dollars; replacing a refrigeration deck or a store today costs
   current dollars. In an asset-heavy filer this widens the exception class.

**THE JUDGMENT, DISCLOSED: (c) is held at the CAPITAL-ACQUIRED end. The D&A end is NOT
credited and is treated as invalid rather than merely optimistic, per [E5-20].** The
operator's instruction to state the direction rather than assume it is discharged: **the
capex end is the conservative one, and here it is also the correct one.**

**Two offsets are named and NOT quantified into the number, per [E4-11] — conservatism is
spent once. Windage count: 1.**
- The trailing series carries roughly $2–3bn of fulfillment-network capital that will not
  recur in that form. **Refused as an adjustment because the FY2026 guidance says total
  capital consumption does not fall.**
- **[E5-33]** governs the impairment: *"to tell owners year after year, 'Don't count this' …
  is misleading."* The $2,497M is a real cost of this business and the capital that produced
  it stays inside the owner-earnings mean.

### The forward cross-check, and it is the number that matters most in this section

From the FY2026 guidance (8-K 2026-03-05, acc. 0001104659-26-023800, **reaffirmed**
2026-06-18): **Adjusted Free Cash Flow $2.7–2.9bn**; **Cap Ex $3.8–4.0bn**.

- Kroger's adjusted FCF **adds back** the cash it pays on opioid settlements, pension
  restructuring and merger litigation. Those add-backs ran **$450M in fiscal 2025**; the
  contractual-obligations table shows **$140M of opioid payments due in 2026** plus the
  ~$57M pension item and continuing litigation cost — call it **$200–350M**.
- **Unadjusted free cash flow ≈ $2.35–2.70bn.**
- Less share-based compensation (~$160M) and finance-lease additions (~$200M):
  **owner earnings on the company's own guidance ≈ $1.99bn–$2.34bn.**

> ### **COMBINED RANGE, all constructions: $1,834M (9-yr, capex end) to $3,229M (3-yr, D&A end). BOTTOM BOUNDARY per [E5-34]: ~$2,000M, and it is corroborated two independent ways — the 5-year trailing mean at the capex end ($2,057M) and the company's own FY2026 guidance ($1.99–2.34bn).**

**Is the range too wide to reach a conclusion [E4-25]? No — and the reason is the whole
point of Stage 0(c).** The width is 76% end to end, which would normally force a close. But
the width has been **decomposed and its causes named**: the top of the range is the D&A end,
which this run has ruled INVALID on filed evidence; and within the valid (capex) end the
spread is 29%, driven by two identified and offsetting cash-timing events that cancel over the
cycle. **After the invalid end is removed, the valid range is $1,834M to $2,364M — 29% wide —
and the company's own forward guidance lands inside it.** A conclusion can be reached.
**[E3-55]** governs the scope: volatility with an understood mechanism is not a defect.

Stock compensation subtracted in full **[E5-06]**; no repricing found, so the reported charge
stands as the measure rather than the floor **[E3-70]**. **[E3-04]** look-through: no material
equity-method stakes; the Ocado shareholding was disposed of years ago. Not applicable.

### Great, good, or gruesome? **[E4-20]**

- [ ] **great.** Ruled out by **[E4-32]**: the return is not "extraordinarily high … [and
  rising] as the years pass." Adjusted FIFO operating margin 3.06% → 3.43% → 3.32%; adjusted
  operating profit below its fiscal 2022 peak three years later.
- [x] **GOOD, and at the lower boundary of it.** *"an attractive rate of interest that will
  be earned also on deposits that are added."* **15.8% after tax on unleveraged net tangible
  assets and 12.36% on the company's own fully-loaded ROIC** clear **[E5-40]**'s ~12%
  "quite satisfactory" calibration, and **[E4-43]** is explicit that the good class
  **passes** Q4 — "nothing shabby about earning $82 million pre-tax on $400 million of net
  tangible assets." **It is at the lower boundary because the return on *added* deposits is
  the part that fails: $19.4bn of capital acquired over five years produced no growth in
  adjusted operating profit and $2.5bn of write-off.**
- [ ] **gruesome** is the wrong label and is refused. Kroger does not grow rapidly, does not
  consume cash, and earns a real return. **The corpus's gruesome test is cash consumption
  "unless the cash they consume gets to earn a reasonable return", and Kroger's base capital
  does earn one.**

### Staying power — score all three **[E5-11]**

- **(1) a large and reliable stream of earnings — PASS, and it is the strongest leg.**
  Positive net earnings in every filed year for decades, through 2008–09 and the pandemic.
  $147.6bn of sales from 63 million households buying food weekly; **operating cash flow has
  never been negative and has run $3.4bn to $7.3bn across the nine-year window.** This is as
  non-cyclical as a revenue line gets.
- **(2) massive liquid assets — PASS, adequately rather than massively.** $3,334M of cash and
  temporary cash investments against $1,802M of debt due within twelve months. A **$2.75bn
  undrawn revolver to September 2029** and a $2.75bn commercial paper programme exist and are
  **explicitly not counted** under **[E5-39]** — "no bank lines counted, no commercial paper,
  nothing depended on." **On cash alone the leg passes; it is not the Costco net-cash case.**
  Recorded honestly: the filing itself says "we generally operate with a working capital
  deficit", and total current liabilities of $18,108M exceed current assets of $14,505M by
  **$3.6bn** — normal and structural for a payables-financed grocer, but it is a genuine
  dependence on continuing to sell food every day.
- **(3) no significant near-term cash requirements — PASS, and this is the leg that usually
  kills.** The filed material-cash-requirements table for calendar 2026: long-term debt
  $1,366M, interest $735M, finance leases $482M, operating leases $962M, self-insurance
  $387M, construction commitments $1,071M, opioid $140M, purchase obligations $992M =
  **$6,135M**, against $7,311M of operating cash flow before capex. **Tight on that
  arithmetic** — but $1,071M of the construction commitments and most of the lease payments
  are already inside the capex and rent lines rather than additive, and the maturity ladder
  beyond 2026 falls to **$606M, $665M, $557M and $1,035M** in 2027–30 with $11,646M
  "Thereafter." **No tower. No commercial paper outstanding at year end or at 2026-03-26.
  No maturity wall.**
- **[E2-54]'s coverage test, run as the corpus states it** — all interest, payable and
  accrued, comfortably met out of current cash flow **net of ample capital expenditures**:
  net interest expense **$639M** against operating cash flow less capital acquired of
  **$3,259M** = **5.1×**. On the FY2026 guide (FCF $2.35–2.70bn before the add-backs,
  interest ~$650M) it is roughly **4.6×.** **Passes without strain, and note it passes on the
  test EBITDA-based covenants are built to avoid.**
- **[E3-52] terms, read rather than counted.** 99.4% fixed-rate ($15,919M fixed against $88M
  variable), no maintenance covenant except the **1.54× leverage ratio against a 3.50×
  limit**, no rating trigger on the revolver's availability. **The benign end of the debt
  spectrum.** Against that: **$7,126M of operating lease liabilities with a 13.7-year
  weighted-average remaining term** are covenant-free but are absolutely not optional — they
  are the stores.
- **Leverage, named and quantified, with no ratio ceiling applied** because the framework has
  none and the corpus supplies none: **total debt including finance leases $17,566M; net debt
  $14,232M; plus operating leases $21,358M; net total debt to adjusted EBITDA 1.76× against
  the company's own 2.30–2.50× target and a 3.50× covenant; debt to book equity 2.96×.**
  **The distinguishing fact is that management says this is too little debt and intends to
  add roughly $4.5bn of it.**

### THE MULTIEMPLOYER PENSION — quantified, as the operator required

**This is the claim a screen cannot see and it is the largest single structural cost
difference between Kroger and the two attackers that matter.** Filed, Note 15 and the MD&A:

| | fiscal 2023 | fiscal 2024 | **fiscal 2025** |
|---|---|---|---|
| cash contributions, multi-employer **pension** | $635M | $398M | **$496M** |
| cash contributions, multi-employer **health and welfare** | $1,182M | $1,228M | **$1,241M** |
| **total** | **$1,817M** | **$1,626M** | **$1,737M** |

> "As of December 31, 2025, **we estimate our share of the underfunding of multi-employer
> pension plans to which we contribute was approximately $1.2 billion, $942 million net of
> tax.** As of December 31, 2024, we estimate our share of the underfunding … was
> approximately **$1.9 billion**, $1.4 billion net of tax."
> "In the event we were to exit certain markets or otherwise cease making contributions to
> these plans, **we could trigger a substantial withdrawal liability.**"
> "we believe the present value of actuarially accrued liabilities in most of these
> multi-employer plans exceeds the value of the assets held in trust to pay benefits, and
> **we expect that our contributions to most of these funds will increase over the next few
> years.**" — FY2025 10-K, MD&A and Note 15

**Quantified against the business:** $1,737M a year of multi-employer cost is **35% of
adjusted FIFO operating profit** and **1.18% of sales** in a business whose whole GAAP
operating margin is 1.28%. The **$1.2bn off-balance-sheet underfunding share** is 20% of book
equity. **Two of the twelve named plans are in the "Red" zone with rehabilitation plans
implemented; the contribution to the UFCW Consolidated Pension Plan tripled in one year,
$70M → $207M, "due to the exhaustion of prefunding credits."** **Six of the eleven listed
funds have collective bargaining agreements expiring in 2026.**

**The fair reading, both ways [E4-51].** *Against:* the underfunding **fell $630M in one
year** on higher asset returns and ARP Act money; it is not a direct liability; Kroger is
named fiduciary of the two largest plans with sole investment authority; and the company has
been actively restructuring them for a decade. *For the finding:* **it is a cost Walmart,
Costco, Publix, Target, Dollar General and Sprouts do not bear at all**, it is contractual
and rising by the company's own statement, and the withdrawal liability is the reason Kroger
cannot cheaply exit a bad market — **which is the mechanism by which a structural cost
becomes a strategic trap.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**Model exposure, not experience [E4-40].** 143 years of survival is exactly the benign
history the corpus calls "not only useless, but actually dangerous" as a guide. What follows
comes from what the filing shows the business is exposed to.

**The mechanism, in one sentence: this business does not die, it dissolves — the unit count
falls a little every year while price and mix hold the dollar line, the union cost base and
the lease ladder do not fall with it, and the 1.28% operating margin is consumed from both
ends until the equity is worth its real estate and nothing more.**

**Quantified from filed figures, four legs.**

1. **The operating leg, and it is the one that decides it.** Adjusted FIFO operating profit
   is **$4,905M on $147,642M of sales — 3.32%.** The three costs that must be held to keep it
   are labour ($1,737M of multi-employer cost alone, rising by the company's own statement),
   occupancy ($872M of net rent plus $3,332M of depreciation on a 13.7-year lease ladder),
   and price ("invest more aggressively in value"). **A sustained 100bp deterioration in the
   FIFO gross margin rate — precisely what Q1 fiscal 2026 delivered nine basis points of — is
   $1,476M, or 30% of adjusted operating profit and more than the entire $1,016M of GAAP net
   earnings.** Walmart U.S. can absorb that: it earns 5.21%. **Kroger cannot: at 3.32% it has
   three points of buffer against a competitor with five.**
2. **The units leg, which sets the pace.** Units fell in five consecutive reported periods.
   **At −1% of units a year with price and mix holding, dollar sales look fine for a decade
   and the store network does not.** Square footage is already −1.0% and 50 stores closed in
   one year. **Each closure crystallises lease exit costs and, in a unionised market,
   potentially a withdrawal liability on the pension fund** — so the shrinkage is not free,
   which is why it happens slowly and why the margin bleeds while it does.
3. **The contingent leg, unaccrued.** Albertsons' Chancery claim seeks **$600M plus expenses
   plus "the lost premium … owed to its shareholders."** Albertsons' shareholders would have
   received $27.25 a share on roughly 580M shares. **Kroger accrues nothing and states the
   range of loss "is not material"; the plaintiff tells its own shareholders it cannot
   collect $600M.** Quantified at the accrued level: zero. Quantified at the claim level:
   **a $600M certain component plus an uncapped premium claim against $5,936M of book
   equity.** A $600M adverse award is 19% of one year's adjusted net earnings — survivable.
   A multi-billion premium award would not be, and it is not accrued.
4. **The refinancing leg, which is real but not near.** $11,646M of the $15,875M of long-term
   debt matures "Thereafter" — beyond 2030 — at fixed rates. **This is the leg that does not
   fire.**

**LIKELIHOOD: [x] a real possibility** — for the dissolution, over a decade, not for
insolvency. **Not "likely":** Kroger throws off $2.0–2.4bn of owner earnings a year on the
honest construction, covers interest 5.1× net of full capex, has no maturity wall, holds
99.4% fixed-rate debt with a covenant at 1.54× against 3.50×, and owns 49% of its balance
sheet as net property and equipment. **Not "a low-level possibility" either:** units have
fallen five periods running, the largest competitor is growing units at 1.6× the margin in
the same twelve months, adjusted operating profit peaked three years ago, and the company
has just written off its one attempt to buy a new advantage.

**FOR-THE-RECORD VERDICT: would clear, on the corpus's own terms.** The three staying-power
legs pass, **[E2-54]**'s coverage test passes at 5.1×, the business is **GOOD** rather than
gruesome under **[E4-20]** and **[E4-43]** says the good class passes, and no named mechanism
touches solvency at any plausible severity. **The owner-earnings range is wide but its width
is explained, its invalid end is removed on filed evidence, and the verdict does not change
anywhere inside the valid range — so no [E4-25] close is forced.** **This is stated for the
record only. Q2 OUT governs and no Q5 clearance exists.**

---
⛔ **Q5 DOES NOT OPEN. Q1 IN · Q2 OUT.** OUT closes the file permanently. What follows is the
floor arithmetic the operator tasked, and it is **COMPUTATION — NOT A CLEARANCE**.

---

## Q5 — COMPUTATION ONLY, NOT A CLEARANCE

**THE FLOOR, before any ranking [E4-28, E3-13].** *"that's the figure we quit on … that's
true whether short rates are 6 percent or whether short rates are 1 percent."*

Market cap **$35,493M** (612,575,611 shares × $57.94, 2026-09-01). Sovereign **5.27%**
(US 30-year, Treasury daily par yield curve, 2026-09-01, issuing authority).

| owner-earnings construction | $M | yield | vs sovereign | perpetual growth needed for the [E4-28] 10% floor |
|---|---|---|---|---|
| 3-yr, (c) = D&A *(**INVALID end**, [E5-20])* | 3,229 | 9.10% | +3.83 pts | +0.90% |
| 5-yr, (c) = D&A *(**INVALID end**)* | 2,838 | 8.00% | +2.73 pts | +2.00% |
| 9-yr, (c) = D&A *(**INVALID end**)* | 2,478 | 6.98% | +1.71 pts | +3.02% |
| **3-yr, (c) = capital acquired** | **2,364** | **6.66%** | **+1.39 pts** | **+3.34%** |
| **5-yr, (c) = capital acquired — the screen's number** | **2,057** | **5.80%** | **+0.53 pts** | **+4.20%** |
| **FY2026, on the company's own guidance — the honest bottom boundary [E5-34]** | **~1,990–2,340** | **5.61–6.59%** | **+0.34 to +1.32** | **+3.41 to +4.39%** |
| **9-yr, (c) = capital acquired — the widest valid window** | **1,834** | **5.17%** | **−0.10 pts** | **+4.83%** |

**The screen's 5.82% yield and 4.18% growth requirement are confirmed to within 2bp on the
corrected 5.27% sovereign: 5.80% and 4.20%.**

**WHAT THE PRICE ALREADY ASSUMES, against what the business has actually done.** The DCF ran
as an engine only; it casts no vote **[E3-34]**. Ten-year fade to a 2.5% terminal, discounted
at the **bare sovereign** — no risk premium in the rate **[E3-42]**.

- **Year-1 growth the quote assumes:** **negative in every construction** — −11.2% at the
  9-yr capex end, −13.6% at the 5-yr capex end, −16.3% at the 3-yr capex end. **The market is
  pricing Kroger for decline.** That is a genuinely important finding and it is the strongest
  fact for the defence anywhere in this file: **the price does not require the business to
  grow. It requires it not to shrink faster than the quote already says.**
- **Honest pre-tax expectancy, points over the sovereign, at the current price:**

  | construction | 0% start growth | 2% | 4% |
  |---|---|---|---|
  | 3-yr, (c) = capital acquired | +3.37 | +3.92 | +4.49 |
  | **5-yr, (c) = capital acquired** | **+2.56** | **+3.05** | **+3.56** |
  | 9-yr, (c) = capital acquired | +1.98 | +2.41 | +2.87 |

  **Total pre-tax expectancy = sovereign + points.** At the 5-year capex construction with
  2% growth: **5.27% + 3.05% = 8.32%.** At the 3-year construction with 4%: **9.76%.** At the
  9-year construction with 0%: **7.25%.**
- **What the business has actually done:** adjusted net earnings **+3.1%/yr** over five
  years; adjusted operating profit **below its fiscal 2022 peak**; non-fuel sales
  **+1.73%/yr**; **units negative in five consecutive periods.**

**THE FLOOR ARITHMETIC, STATED PLAINLY: on the valid (c) end, the honest pre-tax expectancy
at $57.94 is roughly 7.3% to 9.8% across the three windows and a 0–4% growth range. It
reaches the [E4-28] 10% floor only at the three-year window with more than 5% sustained
growth — which is above anything the business has delivered on any operating measure in the
last five years. Below roughly 10%, the name is not ranked; it is quit on.**

**THE CEILING, named [E2-63, E4-44].** The upside is bounded three ways. **[E4-44]:** value
cannot over the long term grow faster than earnings, and adjusted earnings have grown 3.1%/yr
while the *multiple* supplied 5.5 points of the last five years' return — a term that has
already begun to reverse (12.96× at the fiscal year end, 11.95× today). **[E2-63]:** the
upside is capped unless more capital is continuously invested, and Kroger's continuously
invested capital produced no operating-profit growth over five years and one $2.5bn
write-off. **And the share count has done more than half the work** and cannot be repeated
indefinitely: at 655M diluted shares and $2.0bn authorised, the next full authorisation
retires 5.6% of the company.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — for the record, and carrying **no entry
language**:

- **conservative: roughly $55–75 a share** — the 9-year to 3-year mean owner earnings at the
  valid (capex) end, capitalised at the bare 5.27% sovereign with zero growth
  ($1,834M → $56.80/sh; $2,057M → $63.72/sh; $2,364M → $73.22/sh)
- **generous: roughly $90–100 a share** — the D&A end this run has ruled INVALID, shown only
  so the reader can see what the wide end of the screen's spread was made of
  ($2,838M → $87.92/sh; $3,229M → $100.01/sh)
- **current price: $57.94 — inside the conservative band, near its bottom.**

**No margin of safety is applied and no bar is selected**, because **[E4-11]** and
**[E4-01]** both operate on a number the hard sequence never authorised. **Certainty is not
priced in the rate [E3-42]:** every discount rate above is the observed sovereign with no
per-name premium. **Windage count: 1** — the (c) judgment held at the capital-acquired end,
disclosed and argued at Q4; the two offsets that would raise owner earnings are named there
and deliberately not taken.

**VERDICT: does not open. Q2 OUT governs.** For the record, the arithmetic says the name
clears the **[E4-28]** floor only on the D&A constructions this run has ruled invalid, or on
a three-year window plus sustained growth the business has not produced. **On the bottom
boundary [E5-34] actually asks for — corroborated by the company's own FY2026 guidance — it
yields 5.6–6.6% and pays between a third of a point and one and a third points over the
bond.** **A grocer, for a third of a point over a government bond.**

---

## Q6 — FOR THE RECORD: WHAT WOULD PROVE ME WRONG, AND WHEN WOULD I REOPEN?

**No position exists.** **[E2-28]**'s hold conditions do not apply. What follows is
pre-committed per **[E1-02]**, written before any future look, so that "retrospectively,
almost anything can be made to look good in relation to something or other" cannot operate.

**The verdict is OUT on the business, and OUT is permanent.** The corpus permits a reopen only
on a change in the facts that produced it, **never on a change in the price** — and this is
the case where that rule bites hardest, because the price is already at the bottom of the
conservative band. **[E4-17]: "beliefs change quite gradually."**

**THESIS-BREAKING METRIC AND ITS THRESHOLD** *(what would prove this OUT wrong)*:
**the number of units sold flat or positive for four consecutive quarters, disclosed in the
identical-sales explanation, with identical sales ex-fuel positive over the same span.** That
is the **[E2-44]** first characteristic and the **[E4-55]** physical series recovered
together, and it is the only thing that would reopen Q2. It is reported, in words, in every
quarterly MD&A.

**Secondary confirmations required alongside it, none sufficient alone:**
- adjusted FIFO operating **margin** rising above the 3.43% fiscal 2022 peak
- the gap to Walmart U.S. on operating margin narrowing rather than widening (currently
  1.28% GAAP vs 5.21%; 3.32% adjusted vs 5.21%)
- Our Brands penetration published **on a stated and consistent basis**
- eCommerce operating profit **quantified** rather than described as "a path to profitability"
- total supermarket square footage flat or growing

**THESIS-CONFIRMING METRICS** *(what would confirm the OUT)*: a sixth and seventh consecutive
period of "a reduction in the number of units sold"; adjusted FIFO operating profit below the
$5.0–5.2bn guide; FIFO gross margin ex-fuel negative for a second consecutive quarter (Q1
fiscal 2026 was −9bp); multi-employer contributions rising as the filing predicts; leverage
moving toward the stated 2.30–2.50× target on buybacks rather than on investment.

**Next catalyst dates:**
- **Q2 fiscal 2026 results, expected ~2026-09-10** — the first read on whether the units line
  turns, and on whether the reaffirmed FY2026 guidance survives a +1.0% Q1
- **the fiscal 2026 third-quarter dividend declaration** and the pace of the $2.0bn December
  2025 authorisation
- **the Delaware Court of Chancery docket** in *Albertsons v. Kroger* — the $600M plus
  lost-premium claim is unaccrued
- **collective bargaining agreements expiring in 2026** across six of the eleven named pension
  funds, including the SO CA UFCW fund (Red zone, $82M/yr) and the Bakery & Confectionary fund
- **the FY2026 10-K, ~late March 2027** — refresh the owner-earnings table and the units series

**The monitoring question [E3-30, E4-17]:** is this erosion "just part of an aberrational
cycle" or has the business "slipped in a way that permanently reduces intrinsic business
values"? **This run answers: slipped.** Five consecutive periods of falling units, a shrinking
estate, an operating profit that peaked three years ago, and a competitor of three times the
size growing units in the same twelve months at 1.6× the margin. **[E2-40]'s counter-trigger
applies to the analyst as much as the holder: once the view has crystallized, delay is the
graver error.**

**Position size: ZERO.** No entry. **[E3-45]:** capital goes to rank #1 and nothing here
ranks. **[E2-74]:** between opportunities the money is parked, and no cash pressure should
bend this standard.

**VERDICT: [x] OUT** *(mirrors Q2; no position, no sell rule engaged)*.

---

## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT**, and Q3–Q6 recorded
      explicitly as **FOR THE RECORD** under operator rule 3's header, not as gates passed.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the
      only IN and it rests on the filed segment, MD&A and cash-flow disclosures.
- [x] Every UNRESEARCHED verdict names the artifact. **None issued** — every gate closed on
      documents in hand.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known. **Four issued, all
      sub-questions, none load-bearing on the verdict:** (i) **fuel gross and operating
      profit** — Kroger discloses fuel sales, price change and gallon change but no profit
      figure in any filing read, and no peer filing measures Kroger; (ii) **the eCommerce
      operating loss** — bounded below by the company's own $400M improvement target for
      fiscal 2026 and by "establish a path to eCommerce profitability", but never quantified;
      (iii) **the Our Brands measurement basis** — "over $39 billion" is stated with no
      definition and the series jumps $7bn in one year; (iv) **H-E-B, Aldi, Trader Joe's,
      Wegmans and Ahold Delhaize** — no SEC filings exist, so the four-verdict test makes them
      UNKNOWABLE rather than UNRESEARCHED, and the moat class is **not** made provisional
      because Walmart and Costco are both fully filed and both in the row.
- [x] **Step 0: the filing was read, not tagged data**, with accession **0001104659-26-037723**
      (10-K, fiscal year ended 2026-01-31, filed 2026-03-31), plus a 10-Q, four prior 10-Ks, a
      DEF 14A and five 8-Ks, all with accessions. **Fiscal 2025 operating cash flow of $7,311M
      cross-checked four ways** against the filed cash-flow statement, the MD&A table, the MD&A
      narrative and XBRL, **and the $38M discrepancy against the earnings release recorded
      rather than smoothed** (PRIME RULE 1).
- [x] **Owner earnings on multi-year means; three windows published [E4-38]; the spread
      carried as part of the range [E4-25]; the capex band disclosed as a judgment with its
      reasoning in full and the D&A end ruled INVALID on filed evidence [E5-20]; windage count
      stated: 1.** The 53-week years (fiscal 2017 and fiscal 2023) are flagged and fiscal
      2023's extra week quantified at $179M pre-tax on the company's own figure.
- [x] **The ASC 842 operating-lease test run before the owner-earnings table**, per the SHOE
      precedent, with both cash-flow lines transcribed for three years, the Note 11 cash line
      cross-checked, and the net effect quantified at **+$59M, 0.8% of OCF**.
- [x] **Competitor row filled: 8 named peers**, every figure filing-sourced with an accession;
      the four private/foreign competitors named with the obstacle and recorded as UNKNOWABLE;
      **[E3-61]**'s limit on the row stated.
- [x] Sovereign is for the earnings currency (USD), **from the issuing authority (US Treasury
      daily par yield curve, not the FRED mirror)**, dated 2026-09-01, and the +9bp difference
      from the screen's 5.18% is carried explicitly.
- [x] Value stated as a round-number range ($55–75 conservative), **headed COMPUTATION — NOT
      A CLEARANCE and carrying no entry language.**
- [x] **No bar selected**, because no margin may be applied to a number the sequence did not
      authorise.
- [x] Prices dated; the aggregator was used for the live quote only and is flagged.
- [x] **The absence-claim rule observed:** every negative claim names the sweep that looked for
      it and is worded "no instance found."
- [x] **[E4-51] discharged:** the fair counter-case is stated at Q2 at length **before** the
      verdict, and the strongest pro-Kroger facts — 15.8% after tax on unleveraged net tangible
      assets, 12.36% ROIC, 63 million loyalty households, $39bn of Our Brands, $1.5bn of
      alternative profit, guidance met and beaten two years running, a board that removed its
      CEO in ten days, and a quote that already assumes decline — are given their full weight
      in the text rather than in a footnote.
- [x] **Operator rule 9 discharged:** four biases declared before the evidence, including the
      sunk-cost incentive created by the length of this run.
- [x] Run committed to git with its extracted evidence files.

## REGISTER

- Verdict: **[x] OUT (about the business)**
- One line: **Kroger and Walmart U.S. closed the same fiscal year on the same day; Walmart
  grew comparable sales 4.3% "with growth in unit volumes" at a 5.21% operating margin while
  Kroger grew identical sales 2.9% "partially offset by a reduction in the number of units
  sold" at 1.28%, and that is [E3-03] criterion 2 answered by the customers.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** four narrow sub-questions listed in the self-audit; none changes the
  verdict.

---

# THE OUTPUT CONTRACT

## (a) THE PRICE — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)

**Owner earnings, valid range: $1,834M to $2,364M** (nine-year to three-year means, (c) held
at capital acquired; the D&A end of $2,478M–$3,229M is ruled INVALID under **[E5-20]** because
capital acquired has exceeded depreciation for nine consecutive years while the store estate
shrank, and FY2026 guidance keeps it there). **Bottom boundary [E5-34]: ~$2,000M, corroborated
by the company's own FY2026 guidance of $1.99–2.34bn.**

**Value, as a round-number range at the 5.27% sovereign with zero growth: roughly $55 to $75
a share. Current price $57.94 (2026-09-01), inside that band and near its bottom.**

**Honest pre-tax expectancy at $57.94: roughly 7.3% to 9.8%, against the [E4-28] floor of
10%.** *No entry language attaches to any number above.*

## (b) PASS / FAIL

# **FAIL — the file closed at Q2.**
**Q1 IN · Q2 OUT · Q3, Q4, Q5, Q6 recorded FOR THE RECORD only.** Kroger is not a franchise:
it fails **[E3-03]** criterion 2 in its own filed words, fails both halves of **[E2-44]**,
fails **[E4-32]**'s direction test, and shows **[E4-55]**'s falling-units signature in five
consecutive reported periods while its largest competitor grows units at 1.6× the margin in
the same twelve months. **No yield repairs a franchise finding.**

---

### THE SINGLE STRONGEST DISCONFIRMING FACT

**Against the case for buying** (and it is the fact the verdict turns on): **two filed
sentences about the same twelve months, both fiscal years ended 2026-01-31.** Walmart's 10-K:
Walmart U.S. comparable sales "increased 4.3% … driven by growth in average ticket and
transactions, and also **reflected growth in unit volumes** and strength in all merchandise
categories", on a **5.21% operating margin**. Kroger's 10-K: identical sales ex-fuel
"increased primarily due to increased pharmacy, eCommerce and Fresh sales and increased spend
per item, **partially offset by a reduction in the number of units sold**", on a **1.28%
operating margin**. **A business whose customers believe there is no close substitute does not
lose units to a competitor that is simultaneously growing units, growing faster, and earning
four times the margin — after five years and $19.4bn of capital spent to prevent exactly
that.**

**Against the OUT verdict** (hunted hardest, per **[E4-26]**, and it is genuinely strong):
**the market is already pricing Kroger for decline.** The DCF engine, run at the bare
sovereign, says the **$35.5bn quote implies year-1 owner-earnings growth of −11% to −16%** on
every valid construction. Against that the business earns **15.8% after tax on unleveraged net
tangible assets and 12.36% on its own fully-loaded ROIC**, both stable; carries a goodwill
wedge of only **5.2% of assets** in a project whose last four closed files were destroyed by
intangibles; met its guidance in fiscal 2024 and beat it in fiscal 2025; holds **63 million
loyalty households and $39bn of Our Brands**, the two assets whose growth is dismantling the
packaged-food companies this project closed last week; and has just installed the former CEO
of Walmart U.S. to fix precisely the gap this run identifies. **A buyer at $57.94 is not
paying for growth. That fact does not survive contact with the units line — a franchise
question is not answered by a discount — but it is why this run took the counter-case
seriously rather than pattern-matching to the packaged-food files, and it is why the Q6
reopen condition is written on units rather than on price.**
