# Company Run — Magnera Corporation (NYSE: MAGN) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session on 2026-10-17, after the run was committed (7a300146): not held; `PORTFOLIO.md` has no line for MAGN, Magnera, GLT or Glatfelter.*

**Dispatch and contamination, declared before any verdict.** Dispatched blind run under `Screens/_daily/_dispatch_brief.md`
as the brief restates it, with the brief's one stated departure (the lines of evidence derived by the analyst from the 10-K,
below). Seen by accident, not used: the session's opening git status lists untracked research folders of other runs by
folder name (`_research 2026-09-26 AYI`, `_research 2026-09-27 ARCB`) and the five most recent commit subjects (a KGHI run
and fold, an HLEO overnight log line); a directory listing of `Screens/_daily/` showed file names only (daily digests, the
overnight log, the lock); a listing of `Test Runs/` filtered for MAGN, GLT and Glatfelter returned no file. The memory index
loaded with the session names the queue state in general terms and names no company relevant here. Nothing of any other
run file, holding review, `PORTFOLIO.md`, the register or the reading list was opened. Whether anyone holds or wants this
name was not sought.

**The lines of evidence this name needs, chosen from the latest 10-K (the brief's departure).** From Item 1: the business
is nonwoven and fibre-based roll goods sold to consumer-product makers (wipes, diapers, incontinence, feminine care, medical
garments, filtration, tea bags and coffee filters), in two segments, Americas (57% of FY2025 sales) and Rest of World (43%);
the 10-K names six competitors and says competition is on "service, innovation, quality, and price"; raw materials (resin,
wood fibre, pulp) are "generally passed on to customers through contractual price mechanisms over time". From Item 1A:
customers "may shift suppliers quickly" because there are no long-term arrangements with many of them; competitors may have
"substantially greater" resources; goodwill is a large part of net worth; material weaknesses in internal control. From
Item 7: organic volume declines, "competitive pressures from imports in South America", the price-cost spread as the
swing in profit, the $171M goodwill impairment of FY2024, Project CORE plant closures, and the debt taken on at the merger.
So the lines chosen are: (1) the field's returns over a full cycle, from the filer's two predecessors (Berry's nonwovens
segment and the Treasure carve-out; Glatfelter) and the one named rival that files with the SEC (Mativ); (2) volume and
the price-cost spread year by year, the test of pricing power in a pass-through business; (3) whether the customer buys on
the low bid; (4) whether the castle is widening or narrowing (volume, closures, impairments); (5) the debt the merger put on
the business, for Q9 and the all-equity basis. Why these: Item 1 and Item 1A describe a converter selling a specified input
to a few large buyers, which is the commodity case of Q2, and Q2's commodity paragraph says such a business is judged on
whether it is the low-cost producer and on the field's returns, read from the filings.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $11.05 (close 2026-10-16; aggregator quote via `tools/run.py`, flagged per operator rule 5; live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **35,800,000** (10-Q for the
  quarter ended 2026-06-27, filed 2026-08-06, accession `0000041719-26-000049`; `python Screens/cover_shares.py MAGN`).
  Checked against the same 10-Q's balance sheet: "35.8 and 35.6 million shares issued", no treasury-stock line, so issued
  less treasury is 35.8M. No 8-K or prospectus filed after that 10-Q (the EDGAR filing list ends with the 10-Q and the
  same-day earnings 8-K, `0001140361-26-031690`). The share count reflects the 1-for-13 reverse split of 2024-11-04.
  Potential shares: 2.1M excluded from diluted EPS as antidilutive (10-Q note 10), RSUs and PSUs.
- **Market cap:** 35.8M x $11.05 = **$395.6M**.
- **Sovereign for the earnings currency:** USD (the reporting currency; about 43% of sales are Rest of World, mostly euro,
  and the 10-K reports in dollars). **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16 (`python tools/sources.py`).
- **Filings read** (operator rule 4):
  - 10-K for FY2025 (year ended 2025-09-27), filed 2025-11-25, accession `0000041719-25-000110`: Items 1, 1A, 7, 7A, 8
    (statements and notes 1 to 12), the auditor's two reports (an unqualified opinion on the statements and an **adverse**
    opinion on internal control).
  - 10-Q for the quarter ended 2026-06-27, filed 2026-08-06, accession `0000041719-26-000049` (statements, notes, MD&A).
  - Earnings release, 8-K Exhibit 99.1, 2026-08-06, accession `0001140361-26-031690`.
  - Proxy (DEF 14A) filed 2026-01-14, accession `0001140361-26-001150` (pay tables and incentive design; read for Q5 and Q6
    facts only, see AFTER THE STOP).
  - The deal prospectus (424B3) filed 2024-09-19, accession `0001104659-24-101145`: the audited combined (carve-out)
    statements of Treasure, the "HHNF Business", for FY2021 to FY2023, its MD&A, the summary financials of Glatfelter, the
    background of the merger.
  - Glatfelter's own filings under the same CIK: 10-K for 2023 (`0000041719-24-000007`), and the XBRL of its 10-Ks for
    2013 to 2023 and its 10-Qs for the quarters ended September 2018 to September 2024 (`0001564590-19-038558`,
    `0001564590-20-052408`, `0000041719-21-000006`, `0000041719-22-000048`, `0000041719-23-000048`, `0000041719-24-000036`),
    used to build Glatfelter's twelve months to each September.
  - Berry Global's 10-Ks for FY2016 (`0001378992-16-000097`), FY2018 (`0001378992-18-000039`), FY2020
    (`0001140361-20-026326`), FY2021 (`0001140361-21-038583`) and FY2024 (`0001140361-24-047881`): the Health, Hygiene &
    Specialties segment, the predecessor of the Treasure business.
  - Mativ Holdings 10-K XBRL (`0001000623-23-000021`, `0001000623-24-000009`, `0001000623-25-000009`,
    `0001000623-26-000016`): the named rival that files with the SEC.
- **One figure cross-checked against the filed statement:** long-term debt $1,952M at 2025-09-27 on the filed balance sheet
  of the 10-K equals the tagged figure `tools/run.py` printed. A second: Treasure FY2024 sales $2,187M (10-K) plus
  Glatfelter's twelve months to September 2024 built from XBRL ($1,309.2M) give $3,496.2M; the 10-K's own unaudited pro
  forma net sales for FY2024 are "$3,496 million" (note 2). The splice of the two predecessors reproduces the filer's figure.
- **The entity in each column.** The CIK is Glatfelter's. Before 2024-11-04 its filings are Glatfelter's (calendar years);
  from the FY2025 10-K the statements are Treasure's (fiscal years to late September), with Glatfelter included from
  2024-11-04. `tools/run.py` mixed the two: its rows dated 2018-12-31 to 2023-12-31 are Glatfelter, its 2024-09-28 and
  2025-09-27 rows are Treasure and Magnera. Its three-year owner-earnings mean (2023 Glatfelter, 2024 Treasure, 2025
  Magnera) adds three different entities and is **not used**.
- `python tools/run.py MAGN` arithmetic lines (saved, `Test Runs/_research 2026-10-17 MAGN/run_py_output.txt`): price,
  shares, the sovereign, the ten balance-sheet columns and the debt lines were used after the check above; nothing it prints
  as a rule or a verdict was read.

**Owner cash after every real cost, before interest, by year (USD millions).** Built in
`Test Runs/_research 2026-10-17 MAGN/calc.py` (output `calc_output.txt`). The deal of 2024 was paid in shares (Treasure's
holders received 90% of the combined company), so by Q7's specific (c) it is a **merger** and is valued "on the combined
companies' averages". Each fiscal year t below is Treasure's fiscal year to late September t plus Glatfelter's twelve months
to 30 September t (its 10-K year t-1, less its first nine months of t-1, plus its first nine months of t). FY2025 is
Magnera as filed; it omits Glatfelter's October 2024 (not filed separately).

| FY | Treasure OCF - SBC - capex - tax gap | Glatfelter OCF + interest paid - SBC - capex | **Owner cash** | Depreciation variant | Cash paid for businesses | Combined sales |
|---|---|---|---|---|---|---|
| 2021 | 380 - 6 - 141 - 10 = 223 | 123.0 + 6.2 - 5.7 - 26.5 = 97.0 | **320.0** | 319.0 | 172.3 | 3,812.5 |
| 2022 | 324 - 7 - 104 - 0 = 213 | -31.9 + 20.1 - 1.1 - 41.6 = -54.5 | **158.5** | 121.4 | 291.1 | 4,254.9 |
| 2023 | 257 - 7 - 88 - 14 = 148 | -18.4 + 52.3 - 3.0 - 32.9 = -2.0 | **146.0** | 85.3 | 0 | 3,714.0 |
| 2024 | 192 - 7 - 72 - 19 = 94 | 7.9 + 66.6 - 3.1 - 30.2 = 41.2 | **135.2** | 47.4 | 0 | 3,496.2 |
| 2025 | Magnera: 103 + 124 cash interest - 19 - 67 | (included from 2024-11-04) | **141.0** | 52.0 | 0 | 3,316 (pro forma) |

Five-year average **180.1**; without the aberrational FY2021 **145.2**. TTM to 2026-06-27 beside it: operating cash 172,
interest added back about 128 (interest expense less non-cash interest), stock pay 17, capital spending 59: about **224**.

Notes on the inputs. Treasure's carve-out had no debt, so its operating cash is already before interest. Glatfelter's
interest paid is added back gross, not net of tax: it recorded tax valuation allowances and operating losses in the years of
its heaviest interest, so the deduction sheltered little (**CONVENTION of this run**: gross add-back where the filer was in
losses; rationale: the all-equity basis wants owner cash before interest, and a tax shield the filer could not use is not
cash). Magnera's FY2025 interest is added back gross for the same reason (10-K note 6: valuation allowance up $163M to $199M).
"Tax gap" is Treasure's current tax expense less the cash taxes it paid, deducted where positive, because the carve-out says
Berry paid taxes "on Spinco's behalf" through the parent account, outside operating cash (424B3, notes; 10-K note 6) (**CONVENTION
of this run**; rationale: tax paid by the parent is still the business's tax). Treasure's FY2021 "other investing" of $10M
is counted as capital spending. Stock pay is deducted every year (operator rule 5; never a net-income proxy). Restructuring
cash is left in: FY2023 to FY2025 each carry it, $28M, $19M and $77M (10-K note 9), and the framework counts the recurring
"one-time" cost as a cost. Magnera's own "free cash flow" of $126M for FY2025 adds a "Pre-Transaction free cash flow from
operating activities" of $90M to GAAP operating cash (10-K, Item 7); that add-back is management's and is not used here.

### The balance sheets, eight to ten years, read before the income account (the file closes before Q4)
Two predecessors, so two runs of balance sheets. The Treasure carve-out exists only from FY2022; Berry's segment reporting
gives no balance sheet. Glatfelter (XBRL, first filed, each year's 10-K; USD millions):

| Dec 31 | Assets | Equity | Cash | Receivables | Inventory | Goodwill + intangibles | Debt (LT + current) | Retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2014 | 1,562 | 649 | 100 | 164 | 249 | 161 | 405 | 919 |
| 2015 | 1,504 | 663 | 105 | 167 | 247 | 139 | 364 | 963 |
| 2016 | 1,521 | 654 | 55 | 153 | 250 | 129 | 373 | 963 |
| 2017 | 1,731 | 709 | 116 | 174 | 252 | 142 | 481 | 948 |
| 2018 | 1,340 | 539 | 143 | 120 | 173 | 247 | 412 | 770 |
| 2019 | 1,284 | 556 | 126 | 124 | 190 | 235 | 360 | 726 |
| 2020 | 1,287 | 578 | 100 | 123 | 196 | 246 | 313 | 723 |
| 2021 | 1,881 | 543 | 138 | 170 | 280 | 392 | 764 | 706 |
| 2022 | 1,647 | 318 | 111 | 196 | 309 | 214 | 833 | 499 |
| 2023 | 1,564 | 257 | 50 | 171 | 298 | 214 | 854 | 420 |

Treasure (carve-out) and Magnera (USD millions; 424B3 for FY2022 and FY2023, 10-K for FY2024 and FY2025, 10-Q for June 2026):

| Date | Assets | Equity | Cash | Receivables | Inventory | Goodwill + intangibles | PP&E | Debt |
|---|---|---|---|---|---|---|---|---|
| 2022-10-01 | 3,145 | 2,487 | 213 | 368 | 281 | 1,106 | 1,006 | 6 |
| 2023-09-30 | 3,027 | 2,390 | 185 | 330 | 243 | 1,069 | 998 | 2 |
| 2024-09-28 | 2,807 | 2,139 | 230 | 359 | 259 | 850 | 949 | 0 |
| 2025-09-27 | 3,989 | 1,064 | 305 | 522 | 474 | 890 | 1,476 | 1,952 |
| 2026-06-27 | 3,834 | 1,017 | 280 | 531 | 498 | 858 | 1,393 | 1,901 |

What the figures say. **Glatfelter** shrank and borrowed: it sold its Specialty Papers business in 2018 (equity fell from
709 to 539), then in 2021 bought two nonwovens businesses for $465M of cash (XBRL `0000041719-22-000012`), almost all of it
borrowed (debt from 313 to 764); in 2022 it recorded $191M of impairments, $119M of them goodwill and $34M intangibles
(XBRL, `0000041719-23-000005`), goodwill and intangibles fell from 392 to 214, and equity fell from 543 to 257 by 2023
while debt rose to 854. Retained earnings fell every year from 2016 (963 to 420). Inventory held at about a fifth of sales
(196 on 2020 sales of 928; 298 on 2023 sales of 1,386), so the working capital moved with the deals rather than ahead of
them. **Treasure** carried
no debt and $2.1B to $2.5B of parent equity, of which about 1.1B was goodwill and intangibles from Berry's purchases (Avintiv
2015, $2.26B net of cash, Berry FY2016 10-K; Clopay 2018, $475M, Berry FY2018 10-K); the FY2024 goodwill impairment of
$171M took the Rest of World goodwill from 205 to 39 (10-K note 1). At the merger Berry took a **$1,111M cash distribution**
funded by new debt, so equity fell from 2,139 to 1,064 and debt went from nil to 1,952: the debt is the price Berry's owners
took out, not money put into the business. Receivables and inventory rose by the Glatfelter amounts (working capital acquired
$247M, note 2). What they do not say: no segment assets or capital spending are reported (note 11: "Total assets and capital
expenditures by segment are not disclosed"); the carve-out's US cash was held by Berry and is not in the FY2022 to FY2024
columns; receivables are reduced by supply-chain financing sold without recourse, of undisclosed size. What they cannot
say: whether the plant is worth its book; the 10-K's own goodwill test shows a cushion of $134M on Americas and $65M on Rest
of World at discount rates of 11% to 13% (Item 7).

## THE FOUNDATIONS (not a gate)
Three bear on this name. A share is a business: the question is "the prospects of the businesses" **[M1998-099]**, and the
market's verdict on the stock ($11.05 against the $20.16 average grant price of the FY2025 awards, 10-K note 10) instructs nothing **[M2006-077]**. Who is paid to tell you: the figures
management features are Adjusted EBITDA, its own "free cash flow" with a $90M add-back, and a "Twelve-month adjusted free
cash flow yield of greater than 25%" (8-K Ex. 99.1, 2026-08-06); the rows say "don’t ask the barber whether you need a
haircut" **[M2011-083]**, so the analysis is built from GAAP cash. Margin of safety: a price that needs "pencil and paper"
to clear is "too close to think about" **[M1996-084]**; with net debt four times the market value, a small change in
owner cash moves the equity a great deal, which is the situation the foundation warns of. No macro view enters
**[M2000-094]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the carve-out prospectus says Spinco's
management "believes" its scale "positions Spinco as a low-cost manufacturer relative to its competitors" (424B3,
`0001104659-24-101145`), the one claim of a castle in the filings; (2) the latest quarter shows "a 1% organic volume
improvement" and a "favorable price cost spread of $11 million" (10-Q, MD&A); (3) twelve months of owner cash to June 2026
(about 224) are the best since FY2021 and, at the price, earn about 11% on the market value plus net debt. Each is weighed
where it belongs below.

## THE STANDING RULE
A part-interest bought for cash, with no borrowing and no position size fixed here, puts no demand for sudden sums on the
buyer; the rule binds the buyer's conduct, "never going to risk what we have and need for what we don’t have and don’t
need" **[M2012-081]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt is
heavy (net debt about $1.6B against a market value of $0.4B); that is the target's exposure, weighed at Q9 if reached, and
it becomes the buyer's ruin only through the buyer's own sizing.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, which needs "the key variables in that particular business, and evaluating
  how predictable they were" **[M1998-044]**. The business makes rolls of nonwoven and fibre-based fabric (spunbond,
  meltblown, spunlace, airlaid, abaca-based papers) to a buyer's specification and sells them to the makers of diapers,
  wipes, incontinence and feminine products, medical garments, filters, tea bags and coffee filters (10-K Item 1). The key
  variables are four, and each is stated in the filings year after year: **volume** with a few large customers (top customer
  14%, top ten 42% of FY2025 sales, 10-K note 1; 11% and 45% for Treasure in FY2023, 424B3); the **price-cost spread** in a
  business whose resin and pulp costs are "passed on to customers through contractual price mechanisms over time" (10-K Item
  1), named as the swing in operating income in every MD&A read (Berry FY2016 to FY2024, Treasure FY2021 to FY2024, Magnera
  FY2025 and FY2026); **industry capacity and imports** ("competitive pressures from imports in South America", 10-K Item 7);
  and **the capital cost** of the plant. None is technology that moves fast; the end products (diapers, wipes, tea bags) are
  old and their demand moves with births, ageing and household spending.
- **Can I foresee the economics ten years out?** In kind, yes: a converter of a specified input sold to concentrated buyers on
  a cost-plus pass-through, whose earning power is set by the spread and by capacity in its field. That is not a forecast of
  the spread in 2036; it is a fix on what sort of earning power the business will have. The rows say a dependence on a
  commodity price is never by itself a STOP at Q1: "We don’t think we can predict commodity prices." **[M2016-025]**, and the
  business is still read "off the figures" **[M2008-069]**. The figures exist for ten years: Berry's segment from FY2016, the
  Treasure carve-out from FY2021, Glatfelter from 2014, Magnera from FY2025. Do the past statements tell me the future ones
  **[M2008-033]**? They tell me the economics of the field, which is what Q2 then judges.
- **Doubt about the perimeter** **[M2002-092]**. The doubt here is not about how the business works but about how good it is,
  and that is Q2's question. The part of Magnera that is hardest to read is the Argentine and Brazilian business (hyperinflation
  accounting, a Brazilian tax claim of up to $66M, 10-Q note 9); it sits inside Americas, which is read as a whole below.
- **Routing.** Not fast-changing technology **[M1998-008]**; not a financial institution; not a holding company. A business of
  two geographic segments with the same products, read by parts at Q2.
- **VERDICT: IN.** The economics can be understood from the filings: "What is important is that I understand the economic
  dynamics of the industry." **[M2011-014]**. Filing facts: 10-K Item 1 and Item 7 (`0000041719-25-000110`); 424B3 MD&A
  (`0001104659-24-101145`).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question starts from the attacker: "why is that castle still standing?" **[M1995-038]**. A moat is what "protects
excellent returns on invested capital" **[L2007-004]**. Q2's commodity paragraph governs the form of the answer: a commodity
dependence is not by itself a stop, the business is judged on whether it is the low-cost producer, read from its own and its
rivals' filings, "The figures are available." **[M2009-059]**, and the field's returns over a full cycle decide whether a
standing castle protects anything more than ordinary returns.

**The parts table** (section B of the gaps case: a part decides at more than half of five-year operating profit). The filer
reports two segments with the same products in different places. Segment operating income for FY2021 to FY2023 is in the
424B3 MD&A; for FY2024 and FY2025 the 10-K gives segment Adjusted EBITDA and segment depreciation and amortization only, so
the figure is Adjusted EBITDA less D&A (**CONVENTION of this run**: the nearest filed figure to segment operating profit;
rationale: the decision is not close, so the choice of measure cannot change it).

| Part | FY2021 | FY2022 | FY2023 | FY2024* | FY2025* | Five-year sum | Share | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Americas | 265 | 152 | 81 | 100 | 109 | 707 | 83% | judged below | **yes** |
| Rest of World | 88 | 20 | -12 | 7 | 39 | 142 | 17% | carried, same evidence | no |

*Adjusted EBITDA less D&A (10-K note 11: Americas 223 - 123 and 241 - 132; Rest of World 59 - 52 and 113 - 74). FY2025
includes Glatfelter from 2024-11-04. Americas decides; its evidence is set out with the whole company's below, and where the
two differ the Americas figure is given.

**The castle tests, each with its filing fact.**
1. **The key factors and how permanent** **[M1995-038]**. The filings name one claimed advantage, and only once: in 2024
   Berry wrote that "Spinco management believes Spinco's manufacturing processes, manufacturing footprint and its ability to
   leverage its scale to reduce costs, positions Spinco as a low-cost manufacturer relative to its competitors" (424B3,
   `0001104659-24-101145`). The FY2025 10-K and the June 2026 10-Q of the company itself do not repeat it (a search of both
   for "low-cost" and "low cost" finds nothing). Item 1 names no patent, brand or contract of consequence: "sales of any one
   individually patented product is not considered material".
2. **The money test** **[M2011-015]**. Could a well-funded rival take the business? The 10-K: "Our competitors may have
   financial and other resources that are substantially greater than ours" and "This competition is significant as to both
   the size and the number of competing firms" (Item 1A, Item 1). The attack is already under way in the deciding part:
   Americas lost 2% of organic volume in FY2025 to "competitive pressures from imports in South America" (Item 7). The rows'
   failing answer fits: "there are some industries that are just never going to have barriers to entry. And in those
   industries, you better be running very fast" **[M2012-106]**.
3. **Pricing power and the agony before a rise** **[M2005-020]**. Prices move with resin and pulp under "contractual price
   mechanisms over time"; profit moves with the "price cost spread", which the filer names in every year's MD&A. When costs
   rose in FY2022 the spread cost Treasure **$157M** of operating income ($100M of it in Americas), and operating income fell
   from $353M to $172M; in FY2023 the spread cost another $45M (Americas $22M) and operating income fell to $69M (424B3
   MD&A). A business with power over price would show the reverse: "over time the businesses with strong competitive
   positions manage to pass through increases in raw material costs" **[M2005-017]**. The pass-through here is contractual,
   lagged and incomplete, and it runs both ways: FY2025 "decreased selling prices of $45 million primarily due to the
   pass-through of lower raw material costs" (10-K Item 7).
4. **Unit volume** **[M1999-054]**. Treasure's organic volume: FY2022 -3%, FY2023 -8% (Americas -9%), first nine months of
   FY2024 -1% (424B3 MD&A); Magnera FY2025 -2% (10-K); first nine months of FY2026 -1%, with +1% in the June quarter
   (10-Q). Five years of falling volume in products (diapers, wipes, incontinence) whose end demand did not fall by as much
   (an inference from the filer's own words, "general market softness and customer destocking", not a filed figure).
5. **The low-cost position** **[L2000-017]**, **[M1997-010]**. The rows measure it "more by cost of production than we would
   by whether copper was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**. The five other named rivals do not
   file with the SEC (the competitor row), so no rival's unit cost can be read. What can be read is the result the low-cost
   producer shows in a commodity field: it holds its returns when the field's fall. Treasure's operating margin went from
   12.5% (FY2021) to 6.1%, 3.0% and 1.4% before impairment (FY2024), and Magnera's to 0.2% (FY2025) and 2.2% (nine months
   of FY2026); the volume lost to imports in South America is volume lost to cheaper supply. The 2024 claim is a belief, and
   the figures since do not show it.
6. **The brand in the customer's mind** **[M2015-038]**. None: the product is an unbranded input inside another company's
   brand; the consumer never sees Magnera's name.
7. **Would the customer still choose it over the low bid** **[M2017-009]**. The 10-K: competition is on "service,
   innovation, quality, and price"; "since we do not have long-term arrangements with many of our customers, these
   competitive factors could cause our customers to shift suppliers quickly" (Item 1A). The top ten customers take 42% of
   sales (note 1). The rows' failing answer: "most insureds don't care from whom they buy." **[L2004-003]**.
8. **Ask the competitors** **[M1999-130]**. On the public record, one competitor answered at the merger table: Glatfelter's
   chief executive told his board in September 2023 that "while Glatfelter's turnaround strategy had recently led to
   relatively better performance than its competitors, Glatfelter's scale and debt levels continued to be challenging"
   (424B3, background of the merger). The other named rivals' views are not on the public record read.
9. **Widening or narrowing** **[M1999-108]**. Narrowing, on every filed sign: the $171M goodwill impairment of FY2024 on the
   Rest of World unit (10-K note 1); Glatfelter's $191M of impairments in 2022 on the businesses it bought in 2021 (XBRL
   `0000041719-23-000005`); Mativ's goodwill impairments of $401M (2023) and $412M (2025) (XBRL `0001000623-24-000009`,
   `0001000623-26-000016`); Project CORE, "capacity rationalizations" with savings "intended to counter general economic
   softness" (10-K Item 7); the sale of a facility at a $7M loss in the June 2026 quarter (10-Q note 3); and the goodwill
   test's own thin cushion, $65M on Rest of World at an 11% to 13% discount rate (Item 7).
10. **What could destroy, modify or reduce it** **[M2000-014]**. Imported supply in the Americas; customers that can switch
    "quickly"; capacity added by rivals with "substantially greater" resources; and the debt the merger placed on it (Q9).

**The competitor row and the field's returns over the last full cycle** (same metric: operating income over net sales, from
each filer's own filings; pre-tax, after amortization of acquired intangibles; USD millions).

| Filer | Years | Operating income / sales, by year | What it shows |
|---|---|---|---|
| Berry Global, Health, Hygiene & Specialties segment (Treasure's predecessor; it also held Tapes and some films, so it is wider than Treasure) | FY2016 to FY2024 | 196/2,400 (8.2%); 216/2,369 (9.1%); 202/2,734 (7.4%); 255/2,748 (9.3%, the reported 469 less the $214M gain on the Seal For Life sale); 295/2,594 (11.4%); 398/3,158 (12.6%); 230/3,166 (7.3%); 127/2,627 (4.8%); 75/2,537 (3.0%) | A full cycle: resin deflation and inflation, the COVID peak (FY2020 to FY2021, "higher demand in our advantaged health and hygiene products as the result of COVID-19", Berry FY2021 10-K) and the destocking trough (FY2023 to FY2024). Average about 8% of sales, on a segment Berry bought for about $2.7B (Avintiv $2.26B, Clopay $475M) |
| Treasure carve-out (424B3; 10-K) | FY2021 to FY2024 | 353/2,827 (12.5%); 172/2,803 (6.1%); 69/2,275 (3.0%); 31/2,187 (1.4%, before the $172M impairment; -141 after) | Operating income before amortization on tangible capital (PP&E plus working capital): about 18% in FY2022, 10% in FY2023, 7% in FY2024, pre-tax |
| Glatfelter (10-K XBRL) | 2019 to 2023 | 54.6/928 (5.9%); 49.2/917 (5.4%); 28.6/1,085 (2.6%); -164.0/1,491; 2.7/1,386 (0.2%) | On equity plus net debt: about 7%, 6%, 2%, a loss, 0.3%, pre-tax |
| Magnera (10-K; 10-Q) | FY2025; nine months of FY2026 | 5/3,204 (0.2%); 53/2,445 (2.2%) | About 3% pre-tax on tangible capital in FY2025 (7% if the $89M of restructuring is added back) |
| **Mativ Holdings** (named rival; SEC filer; 10-K XBRL) | 2022 to 2025 | 51.4/2,167 (2.4%); -413.9/2,026 (-12.9 before the $401M impairment); 6.3/1,981 (0.3%); -384.4/1,987 (+27.5, 1.4%, before the $412M impairment) | Before 2022 Mativ was Schweitzer-Mauduit, mostly cigarette papers, a different business, so its earlier years are not compared |

Named rivals that do not file periodic reports with the SEC (EDGAR company search, 2026-10-17; the only hits were
individuals, a 2017 tender-offer filing by Ahlstrom-Munksjo and an unrelated "Avgold"): **Ahlstrom, Avgol, PFNonwovens,
Freudenberg, Fitesa**. Their returns are not compared.

**Judged in words** (the convention: "ordinary" carries no figure; the moat is judged, not measured **[M1999-108]**).
Over a full cycle the best-placed part of this field, Berry's segment with a claimed low-cost position and Berry's
purchasing power behind it, earned about 8% of sales before tax on average and 3% at its trough, on a price of about $2.7B
paid for it; the filer then took a $171M impairment on part of that price. The other two filers in the field, Glatfelter
and Mativ, earned less, wrote off what they bought, and in Glatfelter's case ended the cycle with equity cut by more than
half. The combined company now earns 0% to 2% of sales. The rows' description fits: "you can have only two competitors and
they’re still terrible businesses, they beat each other’s brains out." **[M2013-052]**; "the improvement you get one day,
your competitor gets the next day." **[M2004-053]**. And the rows' commodity exception, where "being the low-cost producer
is all-important" **[L2000-017]**, is failed on the filer's own figures: a low-cost producer holds its returns when the
field's fall, and these fell with the field and further. The one change for the better on the record, a 1% volume gain and
an $11M favourable spread in one quarter, is not a full cycle and is not credited (section C).

**Price does not reopen it.** "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**;
"If you really think a business is declining, most of the time you should avoid it." **[M2012-062]**.

- **VERDICT: OUT.** The deciding part (Americas, 83% of five-year segment profit) and the whole are a commodity converter
  whose field, on the evidence of the filer's predecessors' and the one SEC-filing rival's own filings, earns ordinary
  returns or less over a full cycle (Q2's list of what it rules OUT, the standing castle that protects only ordinary
  returns, **[L2007-004]**, **[M2013-052]**); the customer buys on price and, by the 10-K's own risk factor, can shift
  suppliers at short notice, the rows' failing answer to the low-bid test **[L2004-003]**, **[M2017-009]**; volume has fallen five years running and imports are taking it **[M2012-106]**; the claimed low-cost
  position is not shown in the returns **[L2000-017]**, **[M1997-010]**. The castle is shown open on the evidence, so the
  box is OUT, not TOO HARD **[M2011-015]**, **[M2006-013]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 because the file closed before Q4. Facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP. The company bought no shares, so Q6's buyback test has no prices paid to
read against the bottom of the Q7 range, and there is no line to write back.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The figures the owner asked for are under COMPUTATION, NOT A CLEARANCE, below.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Nothing in the filings read falls among the businesses Q12 names.

---
## THE BOX
**OUT**, decided at **Q2**: a commodity converter whose field earns ordinary returns or less over a full cycle, whose
customers buy on price and can change supplier at short notice, and whose claimed low-cost position does not show in its
returns. Integrity facts recorded, not judged. COMPUTATION beneath the stop: value range $11.11 to $29.40 a share against
$11.05; fair price negative on the all-equity basis (-$8.99), $4.29 on the equity-only basis.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Facts already found that bear on later questions, each with its source **[M1997-127]**; no verdict; the box unchanged
(operator rule 2).

**Q3 (capital).** Pre-tax operating income before amortization on tangible capital (PP&E plus working capital): Treasure
about 18% (FY2022), 10% (FY2023), 7% (FY2024); Magnera about 3% (FY2025). Capital spending against depreciation: Treasure
131 against 111 (FY2021), then 104/115, 88/118, 72/127; Magnera 67/156 (FY2025, depreciation raised by the merger's
fair-value step-up) and 44/116 in nine months of FY2026; FY2026 capital spending guided at $80M in the 10-K and at $60M in
the June 10-Q. The plant base is being run down and closed as volume falls (Project CORE). Glatfelter's 2021 purchases
($465M, borrowed) were followed by $191M of impairments in 2022: what those purchases returned on their price was a loss.

**Q4 (the accounts).** The auditor's opinion on internal control is **adverse**: material weaknesses in "controls associated
with the purchase price allocation of the merger with Glatfelter and information technology general controls related to
legacy Berry U.S. IT systems" and in "controls related to the realizability of deferred tax assets" (10-K, EY report of
2025-11-25). The FY2023 to FY2025 statements are partly carve-out statements built from Berry's records with allocated
costs ($26M, $21M, $3M). Restructuring has been charged every year: $24M, $30M, $89M, and $61M in nine months of FY2026.
Recorded as weighings carried to Q5: the featured adjusted figures (Adjusted EBITDA as "the primary measure of profit"; a
"free cash flow" of $126M for FY2025 that adds $90M of "Pre-Transaction free cash flow from operating activities" to GAAP
operating cash of $103M; a "Twelve-month adjusted free cash flow yield of greater than 25%" in the August 2026 release); and
**guidance**: the 10-K guided FY2026 operating cash of $170M to $190M and free cash flow of $90M to $110M on $80M of capital
spending; the June 10-Q guides operating cash of $150M to $170M and the same free cash flow on $60M of capital spending, so
the free-cash-flow figure was held by cutting planned capital spending by the $20M that operating cash guidance fell.

**Q5 (the people; integrity facts recorded, not judged).** The chief executive in the August 2026 release: "We delivered a
record third quarter led by organic volume growth", for a quarter of $22M operating income and a $20M net loss, the first
quarter of organic volume growth in the run's record, in a company that has existed since November 2024. The material
weakness on deferred-tax realizability and the guidance change above. Pay (DEF 14A, `0001140361-26-001150`): chief
executive total $9.79M for FY2025 (salary $0.91M, a $0.75M merger retention bonus, stock awards $7.27M, cash incentive
$0.85M) in a year of a $159M net loss; the cash incentive is paid on Adjusted EBITDA (75%) and "Post-Merger Adjusted Free
Cash Flow" (25%); 75% of long-term awards are PSUs on "absolute stock price growth"; pay is set "around the 50th percentile
of the peer group". Insider ownership and directors' own purchases were not read.

**Q6 (the money and the owners).** No dividend and no share repurchase since the merger (cash-flow statements). Debt repaid:
$484M in FY2025 (Glatfelter's debt at the merger) and $65M in nine months of FY2026 (term loan down $25M, 7.25% notes down
$40M). The 10-Q states an acquisition strategy: "We seek to obtain businesses for attractive post-synergy multiples". The
merger: Glatfelter's holders kept 10%, valued in the purchase accounting at $74M of equity alongside $869M of Glatfelter
debt assumed (10-K note 2); Berry's holders received 90% plus the $1,111M cash distribution, funded by the debt Magnera now
carries.

**Q9 (debt and exposures).** Debt at 2026-06-27 (10-Q note 5): term loan $706M (SOFR plus 4.25%, due November 2031), 4.75%
first-priority secured notes $500M (October 2029), 7.25% first-priority secured notes $760M (November 2031); face $1,966M,
carrying $1,901M; cash $280M (86% of the FY2025 cash was outside the US, 10-K Item 7). Revolver $350M, undrawn. No
financial maintenance covenants. Twelve months to June 2026: operating income about $63M against interest expense about
$151M, a pre-tax loss of about $97M; coverage as the rows measure it, "pre-tax earnings/interest, not EBITDA/interest"
**[L2012-002]**, is below one. Other claims: cross-currency swap liability $78M; a Brazilian tax claim with outcomes "not
expected to exceed $66 million"; the Fox River environmental liability $17M against a $9M escrow; operating leases about
$60M; receivables sold under supply-chain financing without recourse, of undisclosed size.

### COMPUTATION, NOT A CLEARANCE: Q7's range and the owner's two reporting figures
Built by Q7's range convention in full, in `Test Runs/_research 2026-10-17 MAGN/calc.py` (output `calc_output.txt`). No
entry language attaches to any figure here (operator rule 3).

- **Inputs.** Owner cash before interest, after the company's own tax, every capital dollar and stock pay deducted, the
  combined companies spliced as in Step 0. Sovereign 5.43%. Market value $395.6M. Net debt at 2026-06-27 on the all-equity
  basis: borrowings as the balance sheet states them, $1,901M, less cash $280M, **$1,621M** (operating leases left out; no
  finance leases of note; no subsequent event stated in that filing). Market value plus net debt $2,016.6M.
- **The four PG specifics.** Growth measured on aggregate owner cash; all capital spending deducted, the depreciation variant
  beside; zero nominal growth after year ten; a price above the top closes OUT.
- **(a) Cycles.** FY2021, the first year of the window, is aberrational on the filer's own description: Berry's FY2021 10-K
  credits "higher demand in our advantaged health and hygiene products as the result of COVID-19", and the 424B3 explains
  the FY2022 decline by "the moderation of advantaged products related to the COVID-19 pandemic". No full cycle of owner
  cash is in the filed combined series (Berry's segment reporting gives no cash flow before FY2021), so the base is the
  window without its aberrational year, FY2022 to FY2025, **145.2** (**CONVENTION of this run**: the rule's peak-to-peak or
  trough-to-trough average cannot be built from what is filed; rationale: dropping the year the filer itself calls
  aberrational is the nearest the filings allow). The literal window, **180.1**, is shown beside.
- **(c) Acquisitions and the merger.** The 2024 merger is valued on the combined averages (Step 0); its financing, the
  $1,111M distribution, is inside today's net debt. Cash paid for businesses over the window was $463.4M (Glatfelter, 2021
  and 2022), against half of owner cash before purchases of $450.4M: the **serial-acquirer** rule applies, so the central
  figure is the **organic pair** (purchases left out, organic growth as the filer reports it), with the default pair
  (purchases deducted, total growth credited) beside.
- **(b) Decline.** Organic volume as the filer reports it, FY2022 to FY2025 (-3%, -8%, -1% for the nine months reported,
  -2%), compounds to **-3.54% a year**; carried as negative, it makes the bottom; the no-growth case is the top. Owner cash
  itself fell 3.8% a year from FY2022 to FY2025 (18.5% a year on the literal end years).
- **(d) Working capital.** Inside operating cash every year; no single-year draw tied by the filer to one event.
- **(e) Growth spending.** The filing does not allow a maintenance guess (no split of capital spending is given), and
  capital spending has run below depreciation since FY2022, so the all-spending case is central and is the more generous of
  the two; the depreciation variant is shown beside.
- **(f) The cap.** Not triggered on the organic pair (the growth is negative). On the default pair, purchases deducted give
  a series that changes sign (147.7, -132.6, 146.0, 135.2, 141.0), the half-window comparison gives an absurd rate (from 7.6
  to 138.1), and the rate is cut to the business's own sales growth, FY2021 to FY2025, **-3.43% a year**.

| Case | Base | Growth to year 10 | Range at 5.43%, per share | Fair price per share (ends at 10%, averaged) |
|---|---|---|---|---|
| **Central: organic pair, base FY2022-FY2025, all-equity** | **145.2** | **-3.54% / 0%** | **$11.11 to $29.40** | **-$8.99** |
| Organic pair, literal window, all-equity | 180.1 | -3.54% / 0% | $24.69 to $47.39 | -$0.25 |
| Default pair (purchases deducted), base FY2022-FY2025 | 72.4 | -3.43% / 0% | -$16.91 to -$8.04 | -$27.12 |
| Default pair, literal window | 87.5 | -3.43% / 0% | -$11.01 to -$0.29 | -$23.35 |
| Depreciation variant, base FY2022-FY2025 | 76.5 | -3.54% / 0% | -$15.56 to -$5.91 | -$26.15 |
| Depreciation variant, literal window | 125.0 | -3.54% / 0% | $3.28 to $19.03 | -$14.03 |
| **Equity-only beside the central case** (owner cash after today's cash interest of about $128M, against market value) | 17.2 | -3.54% / 0% | $6.67 to $8.84 | **$4.29** |
| Equity-only, literal window | 52.1 | -3.54% / 0% | $20.25 to $26.82 | $13.03 |
| Beside only, not the convention's input: twelve months to June 2026, all-equity | 224 | -3.54% / 0% | $41.72 to $69.95 | $10.72 |

- **The floor, tested first.** On the all-equity basis no case earns about ten percent at the price: the best case, the
  literal window at no growth, yields 180.1 on $2,016.6M, **8.9%**; the central top yields **7.2%**; every declining case
  less. Owner cash of about $202M a year, held flat, would be needed to earn ten percent at the price. Had Q7 been reached,
  it would have closed OUT on the floor **[M2003-149]**. The equity-only literal window (13.2% on market value) and the
  twelve-month figure (11.1% on market value plus net debt) clear it; neither decides, the first by the basis convention and
  the second because it is one year, with capital spending at $59M against depreciation of about $144M.
- **Width.** Central range 2.6 to 1 per share (1.3 to 1 for the whole business); not the deciding test, since the floor
  fails first.
- **Face value of debt beside.** With debt at face ($1,966M) net debt is $1,686M: central range $9.29 to $27.59, fair price
  -$10.80.

**The owner's two figures (reporting convention, not a verdict):** **VALUE RANGE $11.11 to $29.40 a share** (central,
all-equity, organic pair, base without the aberrational year) against **$11.05**; **FAIR PRICE: none on the all-equity
basis (computed at -$8.99 a share**: the midpoint of the range valued at ten percent does not cover net debt); **equity-only
$4.29** beside it. Tax: the company's own (it paid $22M of cash tax in FY2025 on a pre-tax loss); no carryforward was priced
separately, since the $199M valuation allowance against the loss carryforwards makes their use uncertain and they could
only raise the figures if used.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `8e23c8bb`, before the first EDGAR request); written question by
      question and committed after each closing: Step 0 to Q1 (`dc4464b3`), Q2 (`ea37a2ef`), the box, the facts after the
      stop and the computation (`a9993106`), this audit. One departure: Step 0 and Q1 were written in one pass and
      committed together, so Q1 has no commit of its own.
- [x] Dispatched: the brief allowed the per-question pathspec commits; a lock file was present in `Screens/_daily/` (seen
      in a directory listing, not opened), taken to be the dispatching session's; the fold into the register is the
      dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared at the top under contamination and was not used.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`Test Runs/_research 2026-10-17 MAGN/check_ids.py`:
      no E-ids, 40 ids, no problems; it caught one filing word quoted beside an id, since corrected); every filing fact
      carries its document and accession.
- [x] The order was kept; Q2 closed the file; everything after it is NOT REACHED, facts are under AFTER THE STOP, and the
      value figures are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, stock pay deducted, never a net-income proxy; the sovereign from the US Treasury
      curve; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations list: the 2024 low-cost claim, the June 2026 quarter's volume
      gain and spread, the twelve-month owner cash); each weighed at Q2 or shown beside the computation.
- [x] Not a point-in-time run; no anchor-date issue.
- [x] Only the arithmetic lines of `tools/run.py` were used; its three-year owner-earnings mean, which adds Glatfelter 2023,
      Treasure FY2024 and Magnera FY2025, was discarded.
- [x] `python tools/check_framework.py` PASS before the commit.
- Honest limits: the Glatfelter twelve-month figures are built from tagged XBRL, cross-checked once against the filer's own
  pro forma sales; Mativ's figures are tagged XBRL from its 10-Ks, not read in its statements; Berry's segment figures were
  read in its 10-K text; Treasure's FY2024 full-year organic volume change was not found in text (the 8-K/A exhibits are
  images), so the nine-month figure stands in; Glatfelter's October 2024 is missing from FY2025; insider ownership was not
  read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
**(1) Two Q2 rules point different ways for a commodity business whose rivals do not file.** Q2's commodity paragraph says
the business is judged on its cost position, read from its own and its operators' filings, and "where no filing states it,
TOO HARD (NATURE)". Five of the six rivals the 10-K names do not file with the SEC, so no rival's unit cost can be read, and
read literally the paragraph closes the file TOO HARD (NATURE). The ordinary-returns item in Q2's list closes OUT "a field
whose durable players earn ordinary returns over a full cycle, on the evidence of the filer's and the rivals' own filings".
Here the returns of the filer's predecessors and the one filing rival can be read. I applied the returns item, reading the
low-cost producer's mark in the rows as its returns when the field's fall; the text does not say which governs. **(2) The
merger splice across fiscal years.** Q7(c) values a merger "on the combined companies' own averages" without saying how to
add a September fiscal year to a December one; I built Glatfelter's twelve months to each September from 10-K and 10-Q
figures and checked the splice against the filer's pro forma sales. The filer's own FY2025 omits one month of the smaller
partner. **(3) The serial-acquirer test across a merger.** The purchases were the smaller predecessor's, before the merger,
and the combined window trips the test by $13M ($463.4M against $450.4M), moving the central figure to the organic pair,
the more generous one. The text does not say whether a merged predecessor's purchases count or what to do at the line.
**(4) Q7(a) with no filed full cycle.** The rule asks for the average over the last full cycle; the filed combined series
starts at the aberrational year, so I used the window without it (a convention of this run). **(5) A negative fair price.**
Part VII defines the fair price as a price; on the all-equity basis it is negative here, and the text does not say whether
to report it as negative, as zero or as none. I reported "none", with the computed figure. **(6) Carve-out statements.**
Neither Q4 nor Q7 says how to treat taxes the parent paid on the carve-out's behalf, outside its operating cash; I deducted
the gap (a convention of this run). **(7) A reused CIK.** `tools/run.py` prints Glatfelter's and Treasure's years as one
series under the same CIK; a run that trusted its owner-earnings mean would have averaged three different companies.
