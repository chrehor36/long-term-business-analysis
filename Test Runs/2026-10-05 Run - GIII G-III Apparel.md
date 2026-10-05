# Company Run: G-III Apparel Group, Ltd. (NASDAQ: GIII), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Every judgment cites a v5 ledger id in
bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are
marked NOT REACHED. Working folder: `Test Runs/_research 2026-10-05 GIII/` (filings as text, `run_py.txt`,
`cover_shares.txt`, `valuation.txt`, `returns.txt`, `rows.txt`, peer facts in `peers/`).

**POSITION NOTE, declared before any verdict:** not checked. The template asks for `PORTFOLIO.md`; this run's instruction
bars it (blind rule). Whether the operator holds GIII is unknown to the analyst.

**Contamination declared.** Seen before the run, not sought: the session's git status and recent commit subjects (runs of
CSW and HOS of record, a small-cap triage screen, a session-state commit naming "unmapped small caps run, tools fixed,
gaps case waiting", a `run.py` commit naming KLXE), and the memory index line "57 gate-clearers, nothing buyable". None
names GIII or an apparel company. No barred file was opened. No other `Test Runs/` file on GIII was searched for or read.

**Not done, by instruction:** the lock in `Screens/_daily/` was not written and nothing was committed (the run's
instruction allows edits only to this file and the working folder). The write-early commits of the template therefore
did not happen; the file was written top to bottom in one session.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $26.99, 2026-10-05, from `tools/run.py` (aggregator, live quote only; flagged per operator rule 5).
- **Shares:** one class, 42,876,508 common shares as of 2026-09-03, from the cover of the 10-Q for the quarter to
  2026-07-31, filed 2026-09-08, accession `0001104659-26-105950` (`python Screens/cover_shares.py GIII`). The same
  10-Q states "As of September 3, 2026, we had 42,876,508 shares of common stock outstanding."
- **Market cap:** $26.99 x 42.877M = $1,157M.
- **Sovereign (earnings currency USD):** 5.63%, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for fiscal 2026 (year to 2026-01-31), filed 2026-03-24, `0001104659-26-033891`: business, licenses, risk
    factors, MD&A, liquidity, Item 9A, balance sheet, customer note.
  - 10-Q for the quarter to 2026-07-31, filed 2026-09-08, `0001104659-26-105950`: MD&A, liquidity, Note 15 (Marc Jacobs),
    the new risk factor.
  - DEF 14A filed 2026-05-05, `0001104659-26-055621`: ownership table, compensation discussion, pay ratio.
  - 8-K filed 2026-09-02, `0000950142-26-002481` (items 1.01, 2.01, 2.02; Exhibit 99.1, the second-quarter release).
  - 10-K fiscal 2025 `0001558370-25-003540`, 10-K fiscal 2024 `0001558370-24-003856`, 10-K fiscal 2021
    `0001558370-21-003547` (retail closures), 10-K fiscal 2017 `0001571049-17-003132` (the DKI purchase), each searched
    for the named items only.
  - Downloaded, not read beyond its description in the 8-K above: 8-K filed 2026-05-14, `0000950142-26-001394`.
- **One figure cross-checked against the filed statement:** operating cash flow fiscal 2026, $299.1M in the XBRL series
  printed by `tools/run.py`; the 10-K's MD&A reads "We generated $299.1 million of cash from operating activities in
  fiscal 2026" (`0001104659-26-033891`). Total assets $2,610,820K on the filed balance sheet against $2,611M in the
  tool's table. Both agree.
- **`tools/run.py GIII`, arithmetic lines only** (Part VII: nothing it prints as a rule, id or verdict is used). Owner
  cash = operating cash flow less stock pay less capital spending (USD M; the D&A basis differs by less than 5 in every
  year of the five-year window):

| FY to Jan | OCF | SBC | capex | D&A | owner cash (capex) |
|---|---|---|---|---|---|
| 2017 | 105.7 | 16.9 | 24.9 | 32.5 | 63.9 |
| 2018 | 79.7 | 19.7 | 34.5 | 37.8 | 25.5 |
| 2019 | 103.8 | 19.7 | 29.2 | 38.8 | 54.9 |
| 2020 | 209.0 | 17.6 | 38.0 | 38.7 | 153.4 |
| 2021 | 74.8 | 6.1 | 16.0 | 38.6 | 52.7 |
| 2022 | 185.8 | 17.4 | 18.3 | 27.6 | 150.1 |
| 2023 | -104.6 | 32.5 | 21.5 | 27.8 | -158.6 |
| 2024 | 587.6 | 17.2 | 24.7 | 27.5 | 545.7 |
| 2025 | 316.4 | 28.9 | 41.5 | 27.4 | 246.0 |
| 2026 | 299.1 | 23.4 | 35.2 | 29.0 | 240.5 |

  Five-year average (FY2022-26) **204.7**; ten-year average (FY2017-26) **137.4**; three-year average (the screen's
  basis) 344.1. The tool's statement-line check found no securities trades in operating cash, no other stock-pay line,
  no intangible or software payment beside capex, no finance leases, no paid-in-kind interest. Years FY2017-21 come from
  companyfacts XBRL (first-filed vintage, transcription), accessions as listed in `run_py.txt`.
- **The screen's ~30% owner-earnings yield is mostly one year.** The three-year mean is lifted by FY2024's $545.7M, when
  inventory fell from $709M to $520M and receivables from $675M to $562M (ten-year balance table below); the FY2025 10-K
  calls that year's further inventory fall "a reduction of the elevated inventory levels in fiscal 2024 related to supply
  chain issues" (quoted in the FY2026 10-K, `0001104659-26-033891`). FY2023's -$158.6M is the build that FY2024
  released. FY2026 again took in working capital: receivables fell $87.7M, inventories $18.1M, payables rose $24.4M
  (10-K FY2026 MD&A), about $130M of the year's $240.5M. On five years the yield is 17.7% after tax; on ten years 11.9%.
- **The balance sheets, ten year-ends, read before the income account** (`tools/run.py` table, USD M; trademarks from the
  `IndefiniteLivedTrademarks` tag, which the tool's table omits; the FY2026 filed balance sheet shows Trademarks
  $638,909K):

| Jan | equity | goodwill | trademarks | cash | receivables | inventory | debt on face | retained |
|---|---|---|---|---|---|---|---|---|
| 2017 | 1,021 | 269 | 435 | 80 | 264 | 483 | 462 | 612 |
| 2018 | 1,121 | 263 | 442 | 46 | 294 | 553 | 391 | 675 |
| 2019 | 1,189 | 261 | 440 | 70 | 502 | 576 | 387 | 759 |
| 2020 | 1,291 | 261 | 439 | 197 | 530 | 552 | 397 | 893 |
| 2021 | 1,336 | 263 | 444 | 352 | 493 | 417 | 512 | 917 |
| 2022 | 1,520 | 263 | 453 | 466 | 606 | 512 | 520 | 1,117 |
| 2023 | 1,385 | 0 | 628 | 192 | 675 | 709 | 619 | 984 |
| 2024 | 1,550 | 0 | 630 | 508 | 562 | 520 | 418 | 1,160 |
| 2025 | 1,679 | 0 | 609 | 181 | 625 | 478 | 6 | 1,354 |
| 2026 | 1,760 | 0 | 639 | 407 | 537 | 460 | 12 | 1,417 |

  What the sheets say, read "before I even look at the income account" **[M2025-032]**: (1) the business itself needs
  little fixed capital (property and equipment $78M at FY2026) and most of its capital sits in receivables and
  inventory, which swing by $100M to $200M a year with orders and supply chains; (2) the brands it owns were bought, not
  built: trademarks went from $67M (FY2016) to $435M with DKI (FY2017) and $628M with Karl Lagerfeld (FY2023), and all
  goodwill, $347.2M, was written off at FY2023 "as a result of our decline in market capitalization" (10-K FY2024,
  `0001558370-24-003856`); (3) debt went from $462M to $12M, the $400M secured notes redeemed in August 2024 (10-K FY2026),
  and cash rose to $407M, so the sheet at FY2026 was net cash; it no longer is, since about $500M went into Marc Jacobs on
  2026-09-01 "using cash on hand and borrowings under its revolving credit facility" (8-K `0000950142-26-002481`);
  (4) receivables against sales rose from 11% (FY2017, $264M on $2,386M) to 18% (FY2026, $537M on $2,957M), the step
  coming in FY2019; I did not read the filing that explains the step, and say so; the allowance for doubtful accounts rose
  to $19.0M from $7.6M in FY2026 on Saks Global and Hudson's Bay (10-K FY2026); (5) retained earnings rose $805M over the
  ten years, against ten-year net income of $924.1M, the difference being buybacks retired and the small dividend begun
  in FY2026 (not traced line by line). What the sheets cannot say: which brand earns the money. The filing gives no
  profit by brand.

## THE FOUNDATIONS (not a gate)
A share is a business, and what decides the outcome here is the business's own cash, not the market's view of a
license dispute. The analyst's habits bear hardest: look for "what’s wrong in things" **[M2025-013]**, and run the
reading "to possibly reject your original hypothesis" **[M1998-144]**. Projections are not used: the company's guidance
and its "$1 Billion in Long-Term Annual Revenue" target for Marc Jacobs (Exhibit 99.1, `0000950142-26-002481`) are
recorded as what the company says and given no weight, since the speakers have "never looked at a projection" in a
purchase **[M1995-050]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Over ten years G-III's aggregate operating margin, 5.8%, equals PVH's 5.9% and is near Oxford's 6.5% (competitor row,
   Q2). The middleman keeps as much of a sales dollar, after all costs, as two brand owners.
2. Pre-tax operating return on net tangible assets employed averaged 21.0% over FY2017-26 (`returns.txt`), because the
   business needs little fixed capital.
3. Owned brands rose to 57% of net sales in FY2026 from 47% in FY2024 (10-K FY2026); Karl Lagerfeld sales went from
   about $475M to about $630M in two years (same).
4. Wholesale gross margin, excluding the tariff refund, was 43.6% for the six months to 2026-07-31 against 39.6% a year
   earlier, "positively impacted by price increases as well as a shift in product mix to owned brands" (10-Q
   `0001104659-26-105950`). Prices were raised and taken.
5. Management has replaced lost business before: DKI bought in 2016, Karl Lagerfeld completed in 2022, sales held near
   $3B from FY2019 to FY2026 except the pandemic year.
6. The balance sheet was net cash at FY2026 with no notes outstanding.

Each of these is weighed at Q2 below.

## THE STANDING RULE
A purchase for cash, unlevered, in a size the buyer can hold through a fall of half or more, puts the buyer at no risk of
ruin; borrowing to own it would, since leverage is what stops an owner who must "be able to play them out"
**[M2004-065]**. Not a question about the target.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the
  industry" **[M2011-014]**.
- **The economic dynamics, from the filings.** G-III designs, sources (71.6% of product from China, Vietnam and
  Bangladesh in FY2026) and sells apparel and accessories at wholesale to about 1,500 customers; its ten largest customers,
  "all of which are department stores or off price accounts", took 67.6% of FY2026 net sales: Macy's 20.6%, TJX 11.4%,
  Ross 11.0% (10-K FY2026). It sells under brands it owns (57% of sales: DKNY, Donna Karan, Karl Lagerfeld, Vilebrequin
  and smaller ones) and brands it rents by license (43%: Calvin Klein, Tommy Hilfiger, Levi's, Nautica, Halston, Champion,
  Converse, BCBG, French Connection, team sports and others). Its earnings are what is left between the brand owner's
  royalty and the retailer's buying power. Those dynamics are old and plain and I understand them.
- **The key variables and how foreseeable they are.** (a) The PVH licenses: foreseeable to the day. Calvin Klein and
  Tommy Hilfiger were 28.0% of FY2026 net sales and expire $435.6M (15%) on 2025-12-31, $372.2M (13%) on 2026-12-31 and
  $19.3M (1%) on 2027-12-31 (10-K FY2026). (b) The department-store channel: its direction is in the filing (Macy's
  closing 150 stores through 2028; Hudson's Bay liquidated in 2025; Saks Global in bankruptcy). (c) Consumer demand for
  the owned and newly licensed brands: not foreseeable in level. (d) Tariffs: not foreseeable, and not a forecast the
  rows let enter.
- **Is it important and knowable?** (c) is important; its level is not knowable, but its structure is: whether the
  brands G-III sells hold their place against the licensor and the retailer is a question about the castle, which the
  filings answer in part. "If something’s important but unknowable, forget it." **[M2006-076]** applies to the level of
  owned-brand demand, not to the structure, which is Q2's subject.
- **The doubt, stated.** "if you have doubts about something being into your circle of competence, it isn’t"
  **[M2002-092]**, and retail is the speakers' own named case: "it’s easy to sort of think you understand retail, and
  then subsequently find out you don’t" **[M2014-052]**. My doubt is not about how this business makes money or what
  governs its margins; it is about whether its position will hold, and that is the question the rows put second, after
  understanding, since without understanding "we can’t make a decision as to whether it has a sustainable edge"
  **[M1997-148]**. I record the doubt and carry it to Q2 rather than spend it here. An analyst who reads the same doubt
  as falling inside Q1 would close the file here TOO HARD; the next question closes it either way.
- **Routing.** Not a fast-technology business; not a financial institution; not a holding company (the Marc Jacobs
  intellectual property sits in a 50% joint venture, read at Q2 as a part of the operating business).
- **VERDICT: IN**, narrowly, on the economic dynamics **[M2011-014]**, with the doubt **[M2002-092]** carried forward.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**. For G-III the record of the last fifteen years was
built substantially inside a castle it did not own.

- **The attacker with money, and the attacker is the landlord.** The money test asks whether someone with capital could
  take the business; "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. Here the answer is not a
  hypothesis. By fiscal 2020 G-III sold over $1 billion of Calvin Klein and $500 million of Tommy Hilfiger product a
  year (10-K FY2026). The licensor, PVH, is taking the business back: "We have been directly operating a significant
  portion of the businesses for the previously licensed product categories, and we intend to continue to directly
  operate a significant portion of these businesses as the license agreements expire, with the remainder being
  re-licensed to other third parties" (PVH 10-K for 2025, `0000078239-26-000021`). PVH reports the transition "resulted in
  a 1% net increase to our revenue and an approximately 50 basis point decline in our gross margin in 2025" (same): the
  brand owner does without G-III what G-III did, at a small cost to itself. G-III sued on 2025-06-13 over the refused
  extension of the women's suits licenses; PVH's subsidiaries counter-sued on 2025-07-30 (10-K FY2026). "We have found in a
  long life that one competitor is frequently enough to ruin a business" **[M2012-108]**; here the one competitor holds
  the trademark.
- **The brand in the customer's mind, and whose brand it is.** The customer who asks for Calvin Klein asks for PVH's
  brand. The same economics show in the gross margin over the whole span: G-III's ten-year aggregate gross margin is
  37.1%, Perry Ellis's (a licensee-heavy wholesaler, FY2010-18) 34.6%, against 56.1% at PVH, 60.1% at Oxford and 64.0% at
  Ralph Lauren (competitor row). "you’re probably going to get better gross of margins if they ask for you by name"
  **[M2023-073]**: the twenty-point gap is the measure of how much of the asking-by-name belongs to someone else. Even
  in the best half-year on record, with owned brands at 57% and price rises taken, wholesale gross margin ex the tariff
  refund was 43.6% (10-Q), still well below the brand owners' decade averages.
- **The brand against the retailer.** "the retailer is going to use all the pressure they’ve got" **[M2015-038]**; "the
  value of having the brand moves over to the retailer from the product itself" **[M2001-090]**; "the brand is our
  protection against the intermediaries making all the money" **[M2019-041]**. G-III's own filing describes the pressure
  in its own words: consolidation makes it "increasingly dependent on retailers whose bargaining strength may increase",
  with "greater pressure from these customers to provide more favorable terms, including increased support of their
  retail margins", and retailers "devoting more resources to the development of exclusive products" and private label
  (10-K FY2026). Three customers took 43.0% of FY2026 sales; TJX and Ross, off-price buyers, took 22.4% between them.
- **The castle that must be rebuilt.** G-III's model is to rent brands on short leases and replace them as they lapse:
  of the licenses tabled in the FY2026 10-K, Levi's (to 2027-11-30), Dockers (2027-11-30), Kenneth Cole (2027-12-31),
  Margaritaville (2027-12-31) and the remaining Calvin Klein and Tommy Hilfiger categories carry "None" as renewal term;
  the FY2024 10-K's roster named Guess?, which the FY2026 10-K does not. The new licenses (Nautica 2023, Halston 2023,
  Champion 2023, Converse 2024, BCBG 2024, French Connection 2026) and the new acquisition replace what lapses. The
  newest replacement is itself rented: the Marc Jacobs intellectual property is held by IPCo, a joint venture of which
  G-III owns 50% and WHP appoints three of five managers, and G-III "will operate the business pursuant to a license from
  IPCo", terminable on uncured breach (8-K `0000950142-26-002481`; 10-Q Note 15 and risk factor). "A moat that must be
  continuously rebuilt will eventually be no moat at all." **[L2007-005]**; in such industries "you better be running
  very fast" **[M2012-106]**. The rebuilding has already failed once at scale: the largest rented castle is being taken
  back, and $808M of FY2026 sales (the 2025 and 2026 tranches) are gone by the end of calendar 2026.
- **The owned brands, the part that stands on its own.** DKNY net sales were about $590M (FY2024), $675M (FY2025),
  $650M (FY2026); the six months to 2026-07-31 show decreases "in DKNY products" (10-Q). Karl Lagerfeld grew from about
  $475M to $630M. Both sell mainly through the same department-store and off-price customers. G-III bought DKI for
  $669.8M in 2016 (10-K FY2017) and later wrote off all its goodwill. The owned brands are real, and contrary item 3 is
  weighed here: they are growing as a share. But they do not answer the castle question for the business as bought,
  whose record rests on the licenses; and the owned brands' own evidence (flat DKNY, a gross margin far below brand
  owners even after the mix shift, a channel in which "the retailer would like his name to be the brand"
  **[M2001-090]**) does not show a castle the retailer and the attacker cannot reach.
- **Pricing power and the agony before a rise.** Prices were raised in FY2027 (10-Q), in a year when tariffs forced
  every importer to raise them; the filing describes the response as "working with our long standing vendors to
  participate in the increased costs, increasing prices where possible and continuing to look for alternative sourcing
  options" (10-K FY2026). Raising prices where possible, in a year when every importer raised them, is the "prayer session before you raise your prices a penny" **[M2005-020]**, not its absence.
- **The low bid and high labor content.** G-III sells a product of "a very high labor content and that has a product that
  can be shipped in from abroad very easily" **[M2007-116]**, which it itself ships in; what protects it is the brand,
  and most of that is rented. Units shipped fell in FY2026 and in the second quarter of FY2027 (10-K, 10-Q).
- **Ask the competitors.** "which one would it be and why?" **[M1999-130]**. The nearest answer on the public record is
  PVH's action: the licensor judged it better to do the work itself than to keep G-III doing it.
- **What could "destroy, or modify, or reduce the economic strengths"** **[M2000-014]**: here the reduction is already
  under way, set by a contract's end date.
- **Contrary evidence weighed.** The equal operating margin with PVH (item 1) and the high return on tangible assets
  (item 2) show a well-run middleman, not a castle: a lean cost base on rented brands earns the brand owner's margin
  only while the brand owner allows it, and the brand owner has now declined. The business's record therefore does not
  answer "why is that castle still standing?" **[M1995-038]**; the honest answer is that its largest part is not
  standing. Price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little"
  **[M2019-015]**.
- **The two readings, stated.** OUT reads the castle as shown open on the evidence (the licensor's take-back, the
  licensor's own filing, the gross-margin gap over ten years, short leases with no renewals, the replacement itself a
  license). TOO HARD would read the owned brands' future as a moat "tenuous in any way" whose value cannot be judged, and send the
  file there **[M2000-019]**. I choose OUT, because the deciding facts are filed facts, not forecasts: the part of the castle that made
  the record is shown open, and the part offered in its place is a rented castle again. Either reading closes the file;
  neither is IN.

**The competitor row** (ten fiscal years each unless noted; companyfacts XBRL, first-filed vintage, transcription only;
the statements behind them were not read except where cited):

| company | span | aggregate gross margin | aggregate operating margin | operating margin low / high | source |
|---|---|---|---|---|---|
| G-III | FY2017-26 | 37.1% | 5.8% | -3.4% / 11.2% | `0001104659-26-033891` and prior 10-Ks |
| PVH | FY2016-25 (to 2026-02-01) | 56.1% | 5.9% | -15.0% / 11.8% | `0000078239-26-000021` |
| Ralph Lauren | FY2017-26 (to 2026-03-28) | 64.0% | 8.7% | -1.4% / 14.5% | `0001628280-26-037074` |
| Oxford | FY2016-25 (to 2026-01-31) | 60.1% | 6.5% | -16.5% / 15.5% | `0000075288-26-000026` |
| Perry Ellis | FY2010-18 (nine years, last before it went private) | 34.6% | 3.2% | -2.1% / 6.3% | `0001193125-18-119535` |

G-III's ten-year return on average equity is 6.9% (net income $924.1M over the decade; `returns.txt`), with the FY2023
goodwill write-off inside it. The row says: G-III's gross margin is a licensee-wholesaler's, like Perry Ellis's, and
twenty points below the brand owners'; its operating margin is level with PVH's and Oxford's because it spends far less
below gross profit. The record is a cost advantage on someone else's brands.

- **VERDICT: OUT.** The castle is shown open on the evidence **[M2011-015]**, **[L2007-005]**, **[M2012-108]**; a castle
  shown open closes OUT in the rows' three boxes "in, out, and too hard" **[M2006-013]**.

---
**The file is closed at Q2. Q3 to Q12 are NOT REACHED. Everything below the Q2 verdict is reported at the owner's
request and is headed accordingly; none of it is a clearance and none of it is entry language.**

## Q3: HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
**COMPUTATION: NOT A CLEARANCE** (the operator protocol's heading, written with a colon under the standing no-em-dash
rule). The capital "actually needed in the business" **[M2010-090]**: pre-tax operating income on net tangible assets
employed (equity less goodwill, trademarks and other intangibles, plus debt, less cash) by year FY2017-26: 14%, 22%,
30%, 30%, 11%, 38%, -10%, 36%, 34%, 15%; aggregate 21.0%. On total capital including the purchased brands, because "you
have to include goodwill, because we paid for it" **[M2011-060]**: aggregate 11.1%. Return on equity aggregate 6.9%,
the range "Time is the enemy of the poor business" **[M1998-006]** speaks to. The stand-still cost: capital spending ran
$16M to $42M against depreciation of $27M to $39M, but the larger stand-still cost here is buying brands to replace
lapsing licenses: investing outflows other than capital spending were $855.4M over FY2017-26 (DKI $465.4M, Karl
Lagerfeld $168.6M, AWWG and other investments), plus about $500M for Marc Jacobs in FY2027. My best guess, stated as a
guess as the rows require of a maintenance figure, "that’s my best guess" **[M2000-144]**: a substantial part of that
spending is maintenance for a licensee whose leases run out, so the owner's cash would "regularly fall considerably
short" of the operating cash, in the words of **[L2023-009]**. Not a weighing; the file is closed.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
**COMPUTATION: NOT A CLEARANCE.** Recorded for the owner, no verdict: (1) the company leads with adjusted figures: its
release guides "Adjusted EBITDA" of $174.0M to $178.0M and "Non-GAAP net income" of $97.0M to $101.0M for FY2027
against GAAP net income of $181.0M to $185.0M, the GAAP figure lifted by a $139.5M tariff-refund receivable booked in
the first quarter (Exhibit 99.1; 10-Q); the rows put the count of purchases where "people are talking about EBITDA" at
"about zero" **[M2002-026]**, and a management that features adjusted earnings "makes us nervous" when it waves away
real costs **[L2016-006]**; here the adjustment removes a one-time gain as well as costs, which I note in its favor;
(2) Ernst & Young gave an adverse opinion on internal control at 2026-01-31, a material weakness in IT general controls
at the Karl Lagerfeld subsidiary, about 9% of net sales (10-K FY2026, Item 9A and the auditor's report); management says
no misstatement resulted; (3) a $40.0M write-off of equity investments in Saks Global and Saks Off 5th, a customer
(10-K FY2026). Whether (1) and (2) together are two tells under Q4's convention, so that "There is seldom just one
cockroach in the kitchen" **[L2002-039]** would apply, is not decided: the file closed before the question.

## Q5: WHO RUNS IT? NOT REACHED.
Recorded, no verdict. Morris Goldfarb, Chairman and CEO, owns 11% (4,786,041 shares) and his son Jeffrey Goldfarb 2%;
directors and officers together 15% (DEF 14A `0001104659-26-055621`). CEO total compensation for FY2026 was $12,508,253,
a pay ratio of 470 to 1 (same), against net income of $67.4M. The retail record: the Wilsons Leather and G.H. Bass
stores were closed in fiscal 2021 at an aggregate charge of about $100M, $65M of it cash, after retail operating losses
of $49.0M (FY2019), $74.6M (FY2020) and $126.8M (FY2021) (10-K FY2021 `0001558370-21-003547`). The proxy is the place to
"see how they treat themselves versus how they treat the shareholders" **[M1994-009]**; the reading is recorded under Q6
Part B and left unweighed.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
**COMPUTATION: NOT A CLEARANCE.** Part A: buybacks of $235.6M over FY2019-26; in FY2026 2,158,276 shares for $49.8M, an
average of $23.07 (10-K FY2026); the programme states a share count, no price, so it weighs against unless the prices
paid sit at or below the bottom of the Q7 range, since value is "entirely purchase-price dependent" **[L2016-002]**: the
FY2026 average of $23.07 sits below the bottom of the central range ($40.98) and just above the stress value ($21.49).
Issuance: 2,608,877 shares to LVMH at $28.748 as part of the DKI price in 2016 (10-K FY2017); not judged against value
then. Deals: DKI $669.8M, Karl Lagerfeld, AWWG (18.7%, equity method), Saks ($40M written off), Marc Jacobs (about
$500M, with no pro forma figures supplied: "it is impracticable for the Company to make certain business combination
disclosures", 10-Q Note 15). Whether each gave less than it got, "Only if we receive less in value than we give"
**[M1995-001]**, cannot be read from the filings. Part B: the long-term awards pay on "Cumulative Adjusted EBIT" and a
ROIC target of 7.1%, paid at the 150% maximum for FY2024-26; a five-year cliff retention grant of $5.0M to Jeffrey
Goldfarb carries no performance condition; the 2026 proxy asks for 2,500,000 more plan shares, about 6% of those
outstanding (DEF 14A). Unweighed; the file is closed.

## Q7: WHAT IS IT WORTH? NOT REACHED.
**COMPUTATION: NOT A CLEARANCE.** Reported at the owner's request; carries no entry language. Construction per the
Part VI CONVENTION (owner cash after every real cost, averaged, carried at the growth shown capped by Q3, ten years, then
zero nominal growth, discounted at the 5.63% Treasury; ends are the no-growth and shown-growth cases). Per share on
42.877M shares; full arithmetic in `valuation.txt`.

| case | base owner cash ($M, after tax) | growth (top end) | value range, $/share | top / bottom |
|---|---|---|---|---|
| (a) the CONVENTION, five-year window FY2022-26 | 204.7 | 12.5% (owner cash FY2022 to FY2026) | 84.82 to 228.05 | 2.69x |
| (a') the same, growth capped at sales growth shown | 204.7 | 1.7% (sales FY2022-26) | 84.82 to 96.88 | 1.14x |
| (b) whole cycle, ten years FY2017-26 | 137.4 | 2.4% (sales FY2017-26) | 56.92 to 68.91 | 1.21x |
| (c) central: (b) less the PVH run-off | 98.9 | 2.4% | 40.98 to 49.61 | 1.21x |
| (d) stress: (b) less all non-capex investing | 51.9 | 0% | 21.49 | 1.00x |

- **Why a whole-cycle variant.** The five-year window holds an aberrational pair: FY2023 (-$158.6M, the inventory build)
  and FY2024 (+$545.7M, its release), and the growth from FY2022 to FY2026 (12.5% a year) is measured from a base and to
  an end both shaped by working capital; "a base year in which earnings were poor can produce a breathtaking, but
  meaningless, growth rate" **[L2005-003]**. The convention's "growth shown" is therefore capped at the sales growth
  shown, CONVENTION of this run: owner cash cannot outgrow sales for long at a margin that has averaged 5.8% and peaked at
  11.2%.
- **The run-off (case c), CONVENTION of this run.** Calvin Klein and Tommy Hilfiger were 28.0% of FY2026 sales and are
  gone by 2027-12-31 (10-K FY2026). The filing gives no profit by brand, so the profit share is taken equal to the sales
  share (factor 0.72), a disclosed guess **[M2000-144]**. It may be too kind or too harsh: the filing says owned brands
  carry "higher gross profit percentages", which argues the licensed share of profit was below 28%; the lost volume
  leaves fixed costs behind, which argues the other way. The company's own FY2027 figure, non-GAAP net income of $97M to
  $101M before the 2026-12-31 tranche lapses (Exhibit 99.1), is recorded beside case (c)'s $98.9M and not used, being a
  projection **[M1995-050]**. Marc Jacobs is not counted: its cost is gone from the cash and its earnings are unknown.
- **The stress (case d).** If buying brands to replace lapsing licenses is the stand-still cost (Q3), the owner's cash
  over ten years was $51.9M a year, after $855.4M of non-capex investing; the rows ask "are you going to have to put more
  cash into after you buy it?" **[M2014-068]**.
- **Width.** No range is wider than three to one; by the convention none closes TOO HARD on width.
- **Had Q7 been reached** it would close OUT, not IN: the central case at the price yields 8.5% after tax, 11.9%
  pre-tax, just over the floor, and the stress case 6.2% pre-tax, under it; a case that turns on which of two
  assumptions holds is one where "it’s too close to think about" **[M1996-084]**, not one that will "scream at you"
  **[M2009-005]**.

**(a) VALUE RANGE:** central (c) **$40.98 to $49.61** a share; the convention's five-year window (a') $84.82 to $96.88;
whole-cycle (b) $56.92 to $68.91; against **$26.99**. The ranges sit far above the price because the Treasury rate
(5.63%) is far below the floor (10% pre-tax); the floor, not the range, sets the fair price.

**(b) FAIR PRICE (CONVENTION floor, about 10% pre-tax):** the price at which the central case (c), with no growth,
returns 10% pre-tax: owner cash is after cash taxes (operating cash flow is after taxes paid), grossed up at 28%, the
nearest normal effective rates in the filings being 28.4% for FY2025 (10-K FY2026) and 27.4% for FY2024 (10-K FY2024);
$98.9M / 0.72 = $137.4M pre-tax; / 0.10 = $1,374M; **$32.05 a share**. The speakers' own figure is "at least 10% pre-tax
returns" **[L2002-020]**, which they called arbitrary: "And it’s arbitrary." **[M2003-149]**.

**(c) CHEAP PRICE:** rule, CONVENTION of this run: the price at which even the stress case (d), with no growth, returns
the 10% pre-tax floor, so that the choice between the cases no longer decides anything and no pencil is needed:
$51.9M / 0.72 / 0.10 = $721M; **$16.80 a share**.

**Against the price of $26.99:** below the fair price of $32.05, above the cheap price of $16.80. Not a screamer.
Nothing here reopens Q2: price does not cure an open castle **[M2019-015]**.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
Not run. The bond is the first filter, "compare it with a bond" **[M1997-089]**; no comparison is made for a closed file.

## Q9: COULD IT RUIN US? NOT REACHED.
Recorded, no weighing. Debt on the face of the balance sheet was $12M at FY2026 and the $700M asset-based revolver was
undrawn (10-K FY2026); at 2026-07-31 cash was $529.2M and the revolver undrawn with $470.0M available (10-Q). The Marc
Jacobs payment of about $500M on 2026-09-01 used cash and revolver borrowings (8-K), so the seasonal second-half
working-capital build is now funded on the revolver, whose maturity is June 2029 "subject to a springing maturity date"
(10-K FY2026). Operating lease liabilities $273M. G-III guaranteed the payment and indemnity obligations of the Marc
Jacobs business under the LVMH transition services agreement (8-K). Supply-chain finance obligations $114.7M (10-K
FY2026).

## Q10: IS IT THE FAT PITCH? NOT REACHED.
Nothing to do. "You wait for the fat pitch." **[M2003-070]**

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.
Not asked. No named business of the rows is involved.

---
## THE BOX
**OUT at Q2.** The castle that produced the record was largely rented, and the landlord is taking it back: Calvin Klein
and Tommy Hilfiger, 28.0% of FY2026 net sales, expire by 2027-12-31, PVH says it will run most of the business itself,
and the replacement (Marc Jacobs) is again a license from a joint venture G-III does not control; over ten years G-III's
gross margin (37.1%) is a licensee's, twenty points below the brand owners'. Computation only, after the close: central
value range $40.98 to $49.61, fair price $32.05, cheap price $16.80, against $26.99.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch: **yes**. Written question by question: yes, in one session. Committed
      after each: **no**, by the run's instruction (no commits); declared above.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that id's row
      (Python check, run before delivery; result in the session report). No v4 id is cited.
- [x] Every filing fact carries its accession or names the filing whose accession is given in STEP 0. Competitor margins
      are XBRL transcription and flagged as such.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and the after-close sections are headed
      COMPUTATION or NOT REACHED.
- [x] Owner cash after every real cost (operating cash less stock pay less capital spending), never a net-income proxy;
      the sovereign from the issuing authority (Treasury, 10/02/2026); the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found, six items, weighed at Q2.
- [x] Not a point-in-time run; no anchor rule applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield and "growth the price assumes" lines are reported
      as arithmetic and explained (the FY2024 working-capital release).
- [ ] The lock was not written (instruction); the operator protocol's map asks an interactive run to write it.
- [x] `python tools/check_framework.py` run after writing; result in the session report.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Q1's doubt rule against Q2's TOO HARD for a castle whose future cannot be judged.** The doubt row,
   **[M2002-092]**, puts any doubt outside the circle; the framework
   also says Q1 asks whether the economics can be foreseen and Q2 asks what the foresight shows. For a fashion
   wholesaler the doubt is about whether the position holds, which reads as Q2, but a strict reader would close it at Q1.
   The framework gives no test for which question a doubt about position belongs to. I passed Q1 narrowly and said why;
   a second analyst could close TOO HARD at Q1 with the same facts.
2. **No rule for a rented castle.** Q2's tests are written for a business that owns its advantage. Nothing says how to
   read a licensee whose largest brands belong to a licensor that can decline to renew. I treated the licensor as the
   attacker with money (the money test) and its own filing as the competitor's answer; the framework should say whether a
   license with a fixed end and no renewal right is, by itself, a castle shown open.
3. **The Q7 convention's growth input with an abnormal window and a scheduled decline.** The convention carries "the
   growth the business has actually shown", measured on aggregate owner cash. Here the five-year window starts and ends
   on working-capital swings (12.5% a year shown) while the filing schedules the loss of 28% of sales. The convention
   says "never above it" but has no floor for a known decline and no rule for a window with an aberrational pair. I
   capped growth at sales growth and added a run-off case, both confessed as conventions of this run.
4. **Acquisitions as stand-still cost.** Q3's rows speak of capital spending and depreciation. For a licensee, buying
   brands to replace lapsing licenses may be maintenance. The framework does not say whether acquisition outlays enter
   owner cash; the answer moves the fair price from $32.05 to $16.80 here.
5. **Small frictions.** The operator protocol's required heading "COMPUTATION" carries an em dash, against the standing
   no-em-dash rule; a colon was used. The template's position note sends the analyst to `PORTFOLIO.md`, which a blind
   run may not open. The template's write-early and lock lines cannot be met under an instruction that forbids commits
   and edits outside the run's own files.
