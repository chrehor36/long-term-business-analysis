# Company Run — The Greenbrier Companies, Inc. (NYSE: GBX) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to its dated name before any fetch** (commit
5542c4a8, before the first EDGAR call).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.  *Filled at the fold by the dispatching session, 2026-10-16, after the run was committed: `PORTFOLIO.md` read for this ticker only; not held.*

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure (the
analyst chose which 10-K lines to read; the choice is stated under Step 0). The dispatching session holds the lock.

**Contamination, declared.** (1) A directory listing of `Test Runs/` made at the start, to confirm that no run file of this
name existed before the copy, showed the file names of other runs dated 2026-10-16, among them `GATX GATX Corporation`,
`WAB Wabtec`, `R Ryder System`, `WLFC Willis Lease Finance` and `AER AerCap Holdings`, with their research folders. None was
opened. GATX is one of the three rivals chosen below; its figures are taken from GATX's own SEC filings, not from that run.
(2) The session's opening context showed recent commit subjects about the WLFC run (OUT at Q2), which I did not use. (3)
The memory index shown at the start carries one-line notes on the queue and the framework; nothing in it names GBX. No other
blind-listed file was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $39.11 (2026-10-16, as printed by `tools/run.py`; an aggregator quote, live quote only, flagged under operator
  rule 5).
- **Shares by class** from the latest filing's cover: common stock without par value, **30,939,686** shares as of
  2026-06-25 (10-Q for the quarter ended 2026-05-31, filed 2026-07-01, accession `0001193125-26-292719`;
  `python Screens/cover_shares.py GBX`). One class only. Check: the 10-Q balance sheet gives 30,939 thousand outstanding at
  2026-05-31; Oregon law and the filings carry no treasury shares (repurchased shares are retired; the issued-share tag
  that `tools/run.py` found is a stale 2010 value and is not used). The 8-Ks filed after the 10-Q (2026-08-31, item 5.02,
  accession `0001193125-26-376734`; 2026-09-22, item 7.01, accession `0001193125-26-397231`) change no share count. The
  2028 convertible notes ($373.8M issued 2021; conversion price about $55.10, FY2025 10-K Note on debt) sit above the price,
  and their par settles in cash; about 8.1 million shares are reserved for them. Not added.
- **Market cap:** $39.11 × 30.940M = **$1,210.1M**.
- **Sovereign for the earnings currency:** USD, the US Treasury daily par yield curve, 30-year, **5.43%** on 2026-10-15
  (`python tools/sources.py`, issuing authority). Most earnings are in USD; Mexico and Europe report through the USD
  consolidation, so the USD rate is used.
- **Filings read** (operator rule 4): the 10-K for FY2025 (year to 2025-08-31), filed 2025-10-28, accession
  `0001193125-25-253612` (Item 1, Item 1A, Item 7, the statements, Note 17 segments, the debt and lease notes); the 10-Q for
  the quarter to 2026-05-31, filed 2026-07-01, accession `0001193125-26-292719`; the proxy (DEF 14A) filed 2025-11-17,
  accession `0001193125-25-284604`; the 8-Ks of 2026-07-01 (`0001193125-26-292598`), 2026-08-31 and 2026-09-22. For the
  cycle: the 10-Ks for FY2024 (`0000950170-24-117047`), FY2022 (`0000950170-22-020502`), FY2021 (`0001564590-21-052050`),
  FY2019 (`0001193125-19-277713`) and FY2016 (`0001193125-16-746547`), each for its cash-flow statement, balance sheet and
  segment note. **No FY2026 10-K was on EDGAR** at the fetch (the submissions index, read 2026-10-16, lists the 10-Q of
  2026-07-01 as the latest periodic report). **Which lines I read, and why** (the brief's one departure): from Item 1, the
  segment description, backlog, customers, raw materials and Competition, because Q1 and Q2 turn on them; from Item 1A,
  the risk headings in full and the text of the competition, customer-concentration, cyclicality, debt, dilution and
  buyback risks, because they are where the filer states the case against itself; from Item 7, the overview, the segment
  discussion, the capital-spending table and liquidity, because they say where the cash went.
- **One figure cross-checked against the filed statement:** FY2025 revenue $3,240.2M and operating cash flow $265.7M in
  the filed statements of the FY2025 10-K equal the XBRL values `tools/run.py` printed (Revenues 3,240.2; OCF 265.7).
  FY2025 debt, net $1,750.9M (recourse 771.2, non-recourse 979.7) on the filed balance sheet equals the LongTermDebt tag.
- `python tools/run.py GBX` arithmetic lines only (output kept in `Test Runs/_research 2026-10-16 GBX/run_py_output.txt`):
  OCF 71.2 / 329.6 / 265.7, SBC 12.1 / 17.1 / 17.5, D&A 106.3 / 115.6 / 121.5, capex 362.1 / 398.3 / 280.4 for FY2023 to
  FY2025; owner cash on the capex basis -303.0 / -85.8 / -32.2. The tool deducts gross capex and does not add back the
  proceeds from sales of lease-fleet railcars, which the filer reports as a normal part of the leasing business (FY2022
  10-K MD&A: "Proceeds from the sale of assets primarily relate to sales of railcars from our lease fleet"). My own owner-cash
  series, from the filed cash-flow statements, is below and in `Test Runs/_research 2026-10-16 GBX/scripts/owner_cash.py`;
  nothing the tool prints as a rule, a floor or a verdict was read.

**Owner cash, from the filed cash-flow statements (USD millions; equity basis, after interest).** Owner cash = operating
cash flow − stock pay − capital spending + proceeds from sales of assets − acquisitions − cash distributed to the joint-venture
partner (net of the partner's investment) + net cash from unconsolidated affiliates (distributions received less
investments and advances, the equity-method convention of Q4). Working capital, including "Leased railcars for syndication",
is inside operating cash and is counted (Q7 specific (d)). The all-equity figure adds back cash interest paid at a 25% tax
shield (CONVENTION of this run: the rows give no rate; 25% sits between the US statutory 21% and the filer's FY2025
effective rate of 32%, 91.4 / 284.4, with Mexico at 30%).

| FY (Aug) | OCF | SBC | capex | asset sales | acquisitions | JV partner | affiliates | owner cash, equity | owner cash, all-equity | D&A | revenue | earnings from operations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2014 | 135.9 | 11.3 | 70.2 | 54.2 | 0 | 4.7 | -13.8 | 90.1 | 100.8 | 40.4 | 2,204.0 | 239.5 |
| 2015 | 192.3 | 19.5 | 106.0 | 5.3 | 0 | 20.4 | -31.1 | 20.6 | 32.2 | 45.2 | 2,605.3 | 386.9 |
| 2016 | 331.7 | 24.0 | 139.0 | 103.7 | 0 | 89.7 | -5.0 | 177.7 | 186.9 | 63.3 | 2,679.5 | 408.6 |
| 2017 | 285.6 | 26.4 | 86.1 | 24.1 | 27.1 | 28.5 | -40.1 | 101.5 | 112.0 | 65.1 | 2,169.2 | 260.4 |
| 2018 | 103.3 | 29.3 | 176.8 | 153.2 | 34.9 | 66.5 | -21.8 | -72.8 | -58.6 | 74.4 | 2,519.5 | 253.0 |
| 2019 | -21.2 | 11.2 | 198.2 | 125.4 | 361.9 | 16.9 | -9.3 | -493.3 | -479.6 | 83.7 | 3,033.6 | 184.1 |
| 2020 | 272.2 | 9.0 | 66.9 | 83.5 | 0 | 38.9 | 10.9 | 251.8 | 275.6 | 109.9 | 2,792.2 | 168.4 |
| 2021 | -40.5 | 14.7 | 139.0 | 15.9 | 0 | 18.3 | 5.3 | -191.3 | -170.2 | 100.7 | 1,747.9 | 41.0 |
| 2022 | -150.4 | 15.5 | 380.7 | 155.5 | 0 | 16.9 | 1.2 | -406.8 | -373.0 | 102.0 | 2,977.7 | 118.0 |
| 2023 | 71.2 | 12.1 | 362.1 | 78.8 | 0 | 13.0 | 3.3 | -233.9 | -181.4 | 106.3 | 3,944.0 | 176.4 |
| 2024 | 329.6 | 17.1 | 398.3 | 75.0 | 0 | 9.3 | 2.9 | -17.2 | 47.1 | 115.6 | 3,544.7 | 324.5 |
| 2025 | 265.7 | 17.5 | 280.4 | 77.3 | 0 | 17.9 | 0.0 | 27.2 | 88.9 | 121.5 | 3,240.2 | 360.1 |

Sources by year: FY2014 to FY2016 from the FY2016 10-K (`0001193125-16-746547`, in thousands, rounded); FY2017 to FY2019
from the FY2019 10-K (`0001193125-19-277713`); FY2020 to FY2022 from the FY2022 10-K (`0000950170-22-020502`); FY2023 to
FY2025 from the FY2025 10-K (`0001193125-25-253612`). The FY2016 OCF is the 331.7 first filed; a later filing restated it
to 337.2 for the restricted-cash rule (XBRL), immaterial here. FY2019 acquisitions are the cash paid for the
manufacturing business of American Railcar Industries (ARI), $361.9M; the same deal also issued convertible notes
(non-cash, FY2019 10-K non-cash activity). **Averages:** FY2021 to FY2025 (the literal window) -164.4 equity / -117.7
all-equity; FY2016 to FY2025 -85.7 / -55.2; FY2014 to FY2025 -62.2 / -34.9. With depreciation in place of all capital
spending, acquisitions and asset sales (the maintenance guess, Q7 specific (e)): FY2021 to FY2025 -42.0 equity / +4.6
all-equity; FY2016 to FY2025 -4.1 / +26.4.

**The balance sheets, read before the income account** (the template asks for them in Step 0 when the file may close
before Q4; FY2016, FY2019, FY2022 and FY2025 from the filed statements of the 10-Ks above, the other years from
`tools/run.py`'s XBRL table; USD millions):

| Aug 31 | assets | cash | receivables | inventories | railcars for syndication | lease fleet (equipment on operating leases) | PP&E | goodwill | debt | equity, Greenbrier | noncontrolling | retained earnings |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,838 | 223 | 233 | 366 | 145 | 306 | 330 | 43 | 304 | 874 | 143 | 618 |
| 2019 | 2,991 | 330 | 373 | 665 | 182 | 367 | 718 | 130 | 850 | 1,277 | 165 (+32 redeemable) | 868 |
| 2022 | 3,852 | 543 | 501 | 815 | 111 | 771 | 645 | 127 | 1,566 | 1,277 | 152 (+28) | 898 |
| 2025 | 4,361 | 306 | 526 | 688 | 226 | 1,329 | 727 | 130 | 1,751 | 1,532 | 165 (+36) | 1,199 |
| 2026-05-31 (10-Q) | 4,348 | 274 (+49 restricted) | 463 | 619 | 427 | 1,298 | 709 | 130 | 1,806 | 1,573 | 123 (+32) | 1,238 |

What moved, and why. Debt rose from $304M to $1,751M (nearly sixfold) while equity rose from $874M to $1,532M; the
increase in debt ($1,447M) is more than twice the increase in Greenbrier equity ($658M). Most of the new debt is
non-recourse and sits against the lease fleet, which grew from $306M to $1,329M (FY2022 10-K MD&A: "The increase in capital
expenditures in 2022 primarily relates to additions to our lease fleet as part of our leasing strategy"). Goodwill tripled
in FY2019 with the ARI manufacturing purchase. Inventories rose from $366M to $688M against revenue up from $2,680M to
$3,240M, so inventory grew faster than sales; at the 2022 build it was $815M. Retained earnings rose $581M in nine years
while owner cash, all spending deducted, was negative in total: the earnings were kept as lease fleet, inventory and plants,
not as cash, and the gap was borrowed. What the figures do not say: the market value of the lease fleet against its book
value (the filer gives none), and how much of the debt would be called in a downturn (Q9). The ten-year span runs from the
FY2016 peak (earnings from operations $408.6M on 20,300 deliveries) through the FY2021 trough ($41.0M on 11,300) to FY2025
($360.1M on 20,400); deliveries in FY2025 were the same as in FY2016.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would own this cyclical builder and lessor "if the market closed for five
years" **[M1997-109]**, which turns on the business's cash over a cycle, not on the quotation. The market serves and does
not instruct **[M2006-077]**: the price has fallen with deliveries in FY2026 (the 10-Q's third quarter shows deliveries down
38.5% and revenue down 31.6%), and that fall is information about price only. No macro forecast enters: the next order
cycle is not forecast here; the business is judged over the cycle the filings already show. Margin of safety: "if you have
to actually do it on — with pencil and paper, it’s too close to think about" **[M1996-084]**. **Contrary evidence, written
down as found** **[M1997-127]**: (1) owner cash after all spending was negative in total over FY2014 to FY2025 and in seven
of twelve years (Step 0); (2) deliveries in FY2025 (20,400) equal FY2016's (20,300) while capital employed roughly tripled;
(3) the filer names no rival, says it competes on price among other things, and states that some rivals are state-backed
and "may sell products below cost" (FY2025 10-K Item 1A); (4) two customers were 26% of FY2025 revenue (Item 1); (5) in
favour of the business, GBX's manufacturing margin exceeded Trinity's rail-products margin in most years of the span
(Q2), which I write down because it runs against my working hypothesis.

## THE STANDING RULE
The buyer's own conduct: a part-interest bought for cash, without borrowed money, puts the buyer at no risk of ruin from
this purchase **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own
debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The filings describe two
  businesses with plain economics (FY2025 10-K Item 1): Manufacturing, which builds freight cars (hoppers, tank cars,
  boxcars, intermodal and automotive cars) in Mexico, the US, Europe and, through a 60% equity-method interest, Brazil, and
  provides wheel, parts, maintenance and conversion services; and Leasing & Fleet Management, an owned fleet of about
  17,000 railcars, 98.2% on lease at 2025-08-31 with an average remaining term of 4.0 years, plus fleet management services.
  The product changes slowly: the car types named are the ones the FY2016 10-K names, and R&D was $5.5M in FY2025 on
  $3.2B of revenue (Item 1).
- **The key variables, and how predictable they are** **[M1998-044]**: (1) North American freight-car deliveries, which are
  cyclical (GBX's own deliveries 16,200 in FY2014, 21,100 in FY2015, 11,300 in FY2021, 24,900 in FY2023, 20,400 in FY2025)
  and whose level in any year cannot be foreseen, though their range over a cycle can be read from the filings; (2) the
  margin per car, which moves with volume, mix, steel and labour costs and the rivals' pricing; (3) the lease fleet's
  utilization and rates; (4) the capital the business puts in to get (1) to (3). These are knowable and important
  **[M2006-076]** in the sense that matters: the past statements tell me what the future ones will look like, a cyclical
  manufacturer whose cash comes and goes with the cycle **[M2008-033]**. A dependence on steel prices and on the order
  cycle is not by itself a stop at Q1 **[M2016-025]**; the business can be judged "off the figures" **[M2008-069]**.
- **Would the insiders write it down?** **[M2000-105]**: yes. The filer publishes a multi-year strategy (FY2025 10-K Item 7:
  "increasing recurring revenue, expanding aggregate gross margin and raising return on invested capital") and the proxy
  sets a ten-percent ROIC target for pay (DEF 14A, `0001193125-25-284604`). This is a forecast the industry's insiders are
  willing to write down, unlike the tech forecasts the row describes.
- **Can I name the winner, not just the industry?** **[M2012-067]**, **[L2009-005]**: the industry is old and concentrated;
  the filer says it is one of the two largest North American builders. Which builder does better over ten years is a Q2
  question and the filings answer it with numbers (the competitor row below).
- **The parts** (Q1's holding-company paragraph, extended to segments): Manufacturing decides (Q2's parts table); it is
  understood by the tests above. The leasing part is understood the same way. The Brazilian and other equity-method
  interests are small (investment in unconsolidated affiliates $99.3M at 2025-08-31) and are counted at the cash they pay.
- **VERDICT: IN.** The ten-year economics of a cyclical freight-car builder and lessor can be pictured from its filings:
  what it earns over a cycle and what capital it consumes are on the record for twelve years, and nothing in the product
  changes fast **[M2012-065]**, **[M2008-033]**. Doubt about the perimeter was weighed **[M2002-092]**: the doubt here is
  about whether the business is good, which is Q2's question, not about whether it can be understood.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing" **[M1995-038]**; a moat is what
"protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (Q2's business-of-parts convention; segment earnings from operations before unallocated corporate cost,
external basis, USD millions; FY2021 and FY2022 from the FY2022 10-K, the former Manufacturing and Maintenance Services
segments added together because the FY2025 10-K combined them from 2024-09-01 and recast FY2023 to the combined figure,
which matches the old two segments' sum, 140.9 + 36.9 = 177.8; FY2023 to FY2025 from Note 17 of the FY2025 10-K):

| part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Manufacturing (incl. maintenance, wheels, parts) | 54.8 | 118.9 | 177.8 | 308.7 | 327.5 | 987.7 | 63% | open on the evidence below | **yes, more than half** |
| Leasing & Fleet Management | 68.9 | 108.3 | 103.3 | 139.0 | 160.6 | 580.1 | 37% | standing, ordinary returns (below) | no |

Corporate cost not allocated to either part was $82.7M to $128.0M a year in the window. Manufacturing carries more than
half of five-year operating profit and decides the file.

**The castle tests, applied to Manufacturing, each with its filing fact.**
1. *What keeps it standing* **[M1995-038]**. The filer's own case (FY2025 10-K Item 1): "one of the two largest railcar
   manufacturers in North America", an "integrated business model" it believes "is difficult to duplicate", customer
   relationships, and competition "on the basis of quality, price, timeliness of delivery, innovative product design,
   reputation and customer service". Price is in the list; no brand the customer asks for by name and no patent position is
   claimed as the castle (the patents paragraph says manufacturing expertise and product development matter "in addition to
   patent protection").
2. *The attacker with money* **[M2011-015]**, **[M2012-106]**. Entry has happened in the span. FreightCar America, a US
   builder that lost money in operations every year from 2017 to 2022 (an operating loss of $75.6M on $230.0M of revenue in
   2019, XBRL of its 10-Ks), moved its production to Mexico (its 2025 10-K, `0001193125-26-098668`, shows 1,916 of its
   1,986 employees there) and earned operating income of $37.3M and $33.9M on $559.4M and $501.0M of revenue in 2024 and
   2025. The filer itself warns of "the introduction of competitive products and new entrants into our markets" and of rivals
   "owned or financially supported by foreign governments or sovereign wealth funds" that "may potentially sell products and
   services below cost" (Item 1A). The cost of a car plant in Mexico is the barrier, and a small rival has crossed it.
3. *Pricing power and the agony before a rise* **[M2005-020]**. The margin follows volume, not the builder's choice of
   price: Manufacturing earned 20.1% of segment revenue at FY2016's 20,300 deliveries, 3.9% at FY2021's 11,300, 4.6% at
   FY2023's record 24,900 (a year of input-cost inflation), and 10.6% in FY2025. In the 10-Q for the quarter to 2026-05-31
   the Manufacturing margin fell to $52.5M on $529.1M of revenue from $120.8M on $793.4M a year earlier, "primarily due to an
   unfavorable change in railcar manufacturing product mix and operating at lower volumes". Cost increases are not fully
   passed on: "Not all of these costs are subject to escalation and related clauses which allow us to pass through costs to
   our customers" (Item 1A, of Europe). The rows say strong positions "pass through increases in raw material costs"
   **[M2005-017]**; the record here is that they pass through only in part.
4. *Volume*. GBX's deliveries were 20,300 in FY2016 and 20,400 in FY2025: no growth in units over the cycle. The backlog fell
   from 30,900 units at 2023-08-31 to 16,600 at 2025-08-31 (FY2025 10-K Item 1) and 13,800 at 2026-05-31 (10-Q).
5. *The low-cost position* **[M2018-043]**, **[L2004-007]**, **[M1997-010]**, measured against the rival, not in absolute
   terms **[M2001-013]**, from the filings: "The figures are available." **[M2009-059]**. See the competitor row: on reported
   segment margins GBX's manufacturing earned more per dollar of revenue than Trinity's rail products in seven of the nine
   years compared from 2016 (Trinity higher in 2019, 9.6% against 8.9%, and in 2023, 4.8% against 4.6%; Trinity was also
   higher in 2014 and 2015, before its 2018 spin-off changed the perimeter), and far more than FreightCar America in every
   year until 2023. This is evidence in GBX's favour and I credit it: of the two large builders it
   appears to be the lower-cost or better-priced one. It is "Another way to prosper in a commodity-type business"
   **[L2004-007]**; whether it has prospered is item 9.
6. *The brand and the low bid* **[M2017-009]**, **[L2004-003]**. The buyers are railroads, lessors and shippers buying fleets
   of standard cars built to AAR and FRA rules (Item 1, Regulation); two customers were 26% of FY2025 revenue, and three
   customers were 16%, 12% and 11% of FY2022 revenue (FY2024 10-K, customer-concentration note). Large, repeat, technical
   buyers of a certified standard product buy on price among the other factors the filer lists; no filing fact shows a
   customer paying GBX more than a rival for the same car.
7. *High labour content* **[M2007-116]**. About half of GBX's 11,000 employees are in Mexico (Item 1, Human Capital); the
   same move was open to the rivals and both made it (Trinity: "Our foreign operations are primarily located in Mexico",
   2025 10-K segment note).
8. *Widening or narrowing* **[M1999-108]**, **[M2000-075]**. Manufacturing margins in FY2024 and FY2025 (9.5% and 10.6%) are
   about half of FY2015 to FY2017's (17.0% to 20.1%); FY2026 so far is lower again. The filer closed plants in Romania,
   Poland and Turkey in 2025 to cut European headcount by 30% "while maintaining the same production capacity" (Item 7), and
   ceased rail production at its Portland plant in 2023 with impairment, disposal and exit costs of $46.7M that year (FY2025
   10-K income statement and impairment note). These are costs taken to stay competitive, a lead being rebuilt
   **[L2007-005]**, not a moat widening.
9. *The field's returns over the last full cycle* (judged in words, no figure, as the moat is judged **[M1999-108]**). The
   span FY2016 to FY2025 runs peak to trough to recovery (earnings from operations $408.6M, $41.0M in FY2021, $360.1M).
   GBX's earnings from operations after a 25% tax, against total equity (including noncontrolling interests) plus debt less
   cash: FY2016 27.9% on $1,098M; FY2017 16.7%; FY2018 14.1%; FY2019 6.9%; FY2020 6.9%; FY2021 1.5%; FY2022 3.6%; FY2023
   4.7%; FY2024 8.2%; FY2025 8.5% on $3,178M (balance sheets above; intermediate years from `tools/run.py`'s XBRL table). The
   mean is 9.9% with the FY2016 peak and 7.9% without it. Return on Greenbrier equity averaged 9.0% (21.0% in FY2016, 2.5% in
   FY2021, 13.3% in FY2025), with debt rising from $304M to $1,751M. Capital employed rose by about $2,080M while after-tax
   earnings from operations fell from $306M to $270M: the added capital earned nothing over the cycle, and owner cash after
   all spending was negative in total over twelve years (Step 0). The rivals: Trinity's rail products earned 0.4% to 9.6% of
   revenue in every year from 2018 to 2025, and Trinity's net income on ending equity ran from minus 8.5% (2020) to 17.7%
   (2021, carrying discontinued operations) and 23.5% in 2025 (carrying a $194.2M gain on the Triumph divestiture) (TRN
   XBRL and 2025 10-K); FreightCar America lost money from 2017 to 2022 and was in a stockholders' deficit of $107.4M at
   2025-12-31 (its 2025 10-K balance sheet). In leasing, GATX, the largest filing pure railcar lessor, earned 7.1% to 12.1%
   of ending equity from 2018 to 2025 (XBRL of its 10-Ks; 2017's 28.0% carries the tax-reform benefit). The durable players
   in this field have earned ordinary returns over the cycle, and GBX, the best-margined builder of the three, earned an
   ordinary return on a capital base that tripled. "in some businesses, you can have only two competitors and they’re still
   terrible businesses" **[M2013-052]**; "the improvement you get one day, your competitor gets the next day" **[M2004-053]**.
10. *A change for the better?* The filer claims one: FY2025 "Margin as a percentage of Revenue improved by 2.9% to 18.7%"
    and "The increase from the prior year was driven by operating efficiencies in our Manufacturing segment" (Item 7). A
    change for the better is credited only on a full cycle (Q2, Change, and what it does to a castle). Even at the improved
    level, in FY2024 and FY2025, the after-tax return on capital was 8.2% and 8.5% and owner cash after all spending was
    -$17.2M and $27.2M on the equity basis: the better years are themselves ordinary. And the downturn that would test the
    change is under way: the 10-Q shows third-quarter deliveries down 38.5% and Manufacturing margin down to 9.9% of
    Manufacturing revenue from 15.2%. There is no better level to credit, so the TOO HARD (NATURE) re-look of that paragraph
    does not arise.

**The competitor row.** The 10-K names no rival: it says only that GBX is "one of the two largest railcar manufacturers in
North America" with "a handful of specialty builders" beside it, and Item 1A names none either. **CONVENTION of this run:**
the three filing rivals chosen are Trinity Industries (the other of the two largest builders, and a lessor), FreightCar
America (a filing builder) and GATX (the largest filing railcar lessor, for the part that does not decide); rationale: they
are the US-listed companies in the two businesses the filer describes, and the only railcar builders of size that file.
Rivals that do not file with the SEC, such as the state-backed foreign builders Item 1A alludes to, are flagged and not
read.

| year | GBX manufacturing margin (segment earnings / segment revenue) | Trinity rail products margin | FreightCar America operating margin |
|---|---|---|---|
| 2014 | 12.5% | 19.0% (Rail Group) | 1.6% |
| 2015 | 18.6% | 20.9% (Rail Group) | 6.1% |
| 2016 | 20.1% | 14.9% (Rail Group) | 3.0% |
| 2017 | 17.0% | not read | -7.8% |
| 2018 | 12.0% | 7.3% | -10.1% |
| 2019 | 8.9% | 9.6% (9.3% as recast in the 2020 10-K) | -32.9% |
| 2020 | 6.8% | 2.3% | -74.4% |
| 2021 | 3.9% | 0.4% | -11.2% |
| 2022 | 4.1% | 2.8% | -4.1% |
| 2023 | 4.6% | 4.8% | 2.9% |
| 2024 | 9.5% (8.7% combined with maintenance) | 7.8% | 6.7% |
| 2025 | 10.6% (combined) | 5.2% | 6.8% |

Sources: GBX segment notes of the FY2016, FY2019, FY2022, FY2024 and FY2025 10-Ks (accessions in Step 0; GBX years end in
August, segment revenue includes intersegment sales); Trinity's 10-Ks for 2016 (`0000099780-17-000014`), 2019
(`0000099780-20-000025`), 2020 (`0000099780-21-000012`), 2022 (`0000099780-23-000013`), 2023 (`0000099780-24-000017`) and
2025 (`0000099780-26-000014`), Rail Group and Rail Products Group tables (calendar years; Trinity's segment revenue includes
its sales to its own leasing arm, and before the 2018 Arcosa spin-off its Rail Group is a different perimeter); FreightCar
America's revenue and operating income from XBRL of its 10-Ks, 2025 checked against its filed statement of operations
(revenue $500,991K, operating income $33,920K, `0001193125-26-098668`). Trinity's 2017 figure was not read (the 2017 and 2018
10-Ks were not fetched). The 2019 comparison goes to Trinity on both its first-filed 9.6% and its recast 9.3%.

**The leasing part** (does not decide; read so that the parts are not lumped **[L2008-005]**): an owned fleet of about 17,000
cars, mostly built by GBX and financed largely with non-recourse debt ($979.7M at 2025-08-31). Its segment earnings of
$139.0M in FY2024 on segment assets of $1,633.6M (FY2024 10-K, the latest year that states segment assets) are before the
interest on that debt. Beside GATX's ordinary returns it is a standing business protecting ordinary returns; under the parts
rule it would be carried to Q7 as an ordinary business at no growth.

- **VERDICT: OUT.** The deciding part, Manufacturing, has commodity-type economics **[L2004-003]**: a certified standard
  product sold to a few large buyers, margins set by volume, costs passed through in part, an entrant that crossed the
  barrier inside the span. GBX holds a better margin position than its one large rival on the reported figures, which is
  credited; but the field's durable players, GBX included, earned ordinary returns over the full cycle FY2016 to FY2025,
  while GBX's capital tripled and its owner cash after all spending was negative in total. The standing castle that protects
  only ordinary returns closes OUT (Q2, What it rules OUT): the moat is what "protects excellent returns" **[L2007-004]**,
  and these returns are known, so the tenuous-moat route to TOO HARD, "We don’t know how to valuate that" **[M2000-019]**,
  does not apply. The relative low-cost position does not change the box, since it has not made the business prosper over
  the cycle **[L2004-007]**. A low price does not reopen it **[M2019-015]**, **[L2014-009]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance sheets were read in Step 0; facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Facts found are under AFTER THE STOP, with the integrity flag in the box line.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Q6's buyback line needs the bottom of the Q7 range; the computation below puts the bottom below zero, and
the facts on buybacks are under AFTER THE STOP. No weighing is given.

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** The two reporting figures the owner asked for are computed below, headed as the protocol requires.

### COMPUTATION, NOT A CLEARANCE
*Computed after a closing STOP at Q2 (operator rule 3). It carries no entry language and decides nothing; the box is OUT at
Q2 whatever it shows. Script and output: `Test Runs/_research 2026-10-16 GBX/scripts/q7.py`, `q7_output.txt`.*

**Inputs.** Price $39.11 (aggregator, flagged); 30.940M shares (cover); market value $1,210.1M. Net debt at the latest filed
balance sheet, 2026-05-31 (10-Q `0001193125-26-292719`): debt, net $1,805.6M (recourse $733.3M, of which the 2.875%
convertible notes due April 2028 are $373.8M; non-recourse, lease fleet, $1,072.3M) less cash and cash equivalents $273.7M
= **$1,531.9M**; restricted cash ($49.1M) is collateral for the non-recourse debt and is not subtracted; operating leases
left out (lessee leases, said so); finance leases "not a material component" (10-Q lease note). No subsequent event in the
10-Q or the later 8-Ks changes the debt (the Series 2026-1 notes of February 2026 are already in the May balance). The
contingently redeemable noncontrolling interest ($31.9M) and the noncontrolling interest ($123.1M) are not subtracted,
because owner cash already deducts the cash paid to the joint-venture partner; subtracting them as well would charge the
partner twice. Enterprise value at the price: $2,742.0M. Sovereign 5.43% (US Treasury 30-year, 2026-10-15). The company's
own tax is inside operating cash; the interest added back for the all-equity basis is taken at a 25% shield (CONVENTION of
this run, Step 0).

**The range, by Q7's range convention.**
- *Cash input and cycle base, specifics (a) and (e).* The literal five-year window FY2021 to FY2025 opens at the filer's
  trough year (FY2021: deliveries 11,300, earnings from operations $41.0M) and so is aberrational at its first year; the base
  is the last full cycle, FY2016 (the prior peak, $408.6M) to FY2025, ten years. The filing allows a maintenance guess: it
  splits capital spending by segment and says that leasing capex is "additions to our lease fleet as part of our leasing
  strategy" (FY2022 10-K MD&A), so the central case charges depreciation as the maintenance spending (the depreciation charge
  "is not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**) in place of all
  capital spending, acquisitions and asset sales, with working capital counted, specific (d). All-equity owner cash on that
  basis averages **$26.4M a year** over FY2016 to FY2025 (Step 0's table, the D&A columns).
- *Growth, specific (b).* The series changes sign within the window (it is negative in FY2018, FY2019, FY2021, FY2022 and
  FY2023), so growth is measured between the halves: $48.2M (FY2016 to FY2020) to $4.6M (FY2021 to FY2025), a compound
  decline of 37.4% a year. A decline is carried as the bottom; the no-growth case is the top. The growth spending bought no
  growth (deliveries flat, owner cash falling), so by specific (e) the maintenance-only no-growth case is the top and the
  inversion is the finding, not an error.
- *Acquisitions, specific (c).* Purchases over the cycle were ARI ($361.9M in FY2019) and two small deals ($27.1M and
  $34.9M in FY2017 and FY2018). The serial-acquirer rule compares net purchases with owner cash before purchases; here owner
  cash before purchases is itself near zero or negative, so the comparison means nothing, and with one deal of size in ten
  years I do not treat GBX as a serial acquirer. The maintenance case leaves purchases out; the default pair, acquisitions
  deducted, is the all-spending row beside, and the organic pair is shown too.
- *The cap, specific (f).* Not needed; no case grows.

| case (all-equity basis unless marked) | base, $M a year | growth | value per share at 5.43% | at 10% |
|---|---|---|---|---|
| **TOP:** maintenance-only, cycle base FY2016 to FY2025, no growth | 26.4 | 0 | **-$33.79** | -$40.98 |
| **BOTTOM:** maintenance-only, cycle base, the halves decline carried ten years, then flat | 26.4 | -37.4% a year | **-$48.18** | -$48.36 |
| beside: all spending, acquisitions deducted, cycle base, no growth | -55.2 | 0 | -$82.39 | -$67.37 |
| beside: organic pair (acquisitions left out), cycle base, no growth | -12.8 | 0 | -$57.16 | -$53.66 |
| beside: literal window FY2021 to FY2025, maintenance-only, no growth | 4.6 | 0 | -$46.75 | -$48.01 |
| beside: literal window FY2021 to FY2025, all spending, no growth | -117.7 | 0 | -$119.59 | -$87.57 |
| beside: twelve years FY2014 to FY2025, maintenance-only, no growth | 35.7 | 0 | -$28.27 | -$37.98 |
| equity-only (after interest, against market value): maintenance-only, cycle base, no growth (the halves change sign, so the no-growth case alone) | -4.1 | 0 | -$2.42 | -$1.31 |
| equity-only: all spending, cycle base, no growth | -85.7 | 0 | -$51.02 | -$27.70 |

**Value range (all-equity, central): -$48.18 to -$33.79 a share against $39.11.** Every case is below zero per share.
**The floor, tested first:** no case in the range earns about ten percent at the price **[M2003-149]**. To earn ten percent
on the enterprise value at the price with no growth, owner cash before interest would need to be about $274M a year; the
best single year in twelve was $275.6M (FY2020, a year of large working-capital release), and the ten-year average was
$26.4M on the generous maintenance basis. Had Q7 been reached, it would have closed OUT on the floor, before the width
test.

**A generous case beside, not the convention's range, written down so the result is not an artefact of working capital.**
If every working-capital movement and every dollar of capital spending above depreciation were ignored, owner cash would
be roughly earnings from operations after a 25% tax, less the joint-venture partner's cash, plus net affiliate cash:
FY2016 to FY2025 averages $229.5M × 0.75 − $31.6M − $5.3M ≈ **$135M a year**. At 5.43% and no growth that is about
$2,490M of enterprise value, **$30.96 a share** after net debt, still below the price; at the price it yields about 4.9% on
the enterprise value. Even on figures that leave out the cash the business has actually consumed, no case reaches the floor.

**FAIR PRICE (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, the two averaged.
**All-equity (central): -$44.67 a share** (top -$40.98, bottom -$48.36). **Equity-only beside: -$1.31 a share** (the
no-growth case alone, since the equity-only halves change sign). Both are below zero: at no positive price does the
midpoint of the range earn the floor. Tax treatment: owner cash after the company's own income tax, as paid inside operating
cash; no carryforward shelter priced separately (the deferred-tax note shows operating-loss carryforward assets of $21M and a total
valuation allowance of $14M at 2025-08-31, XBRL of the FY2025 10-K; immaterial).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** No business the rows name is involved.

---
## THE BOX
**OUT at Q2** (the deciding part, Manufacturing, is a commodity-type builder whose field, GBX included, earned ordinary
returns over the full cycle FY2016 to FY2025 while GBX's capital tripled; Q1 IN). COMPUTATION, NOT A CLEARANCE: value range
-$48.18 to -$33.79 a share against $39.11 (all-equity; no case earns the floor); fair price -$44.67 all-equity, -$1.31
equity-only. Integrity facts recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).*

**Bearing on Q3 (capital).**
- Capital employed (total equity plus debt less cash) rose from $1,098M (FY2016) to $3,178M (FY2025); after-tax earnings
  from operations went from $306M to $270M (Q2, item 9). Deliveries were 20,300 and 20,400 in the two years.
- Capital spending by segment, FY2016 to FY2025, from the segment notes: Leasing $77.5M, $28.0M, $111.9M, $99.8M, $7.0M,
  $103.8M, $323.2M, $272.9M, $277.0M, and FY2025's total $280.4M (the FY2025 segment split was not read); Manufacturing and
  maintenance together from $35.2M (FY2021) to $121.3M (FY2024) a year. The lease fleet grew from $306M to $1,329M of book value.
- Owner cash after all spending was negative in seven of twelve years and in total (Step 0): "there’s your profit sitting in
  the yard" **[M2008-036]** describes the pattern the table shows; the second kind of business "reports the 12 percent on
  capital but there’s never any cash" **[M2003-122]**. Recorded, not weighed.

**Bearing on Q4 (the accounts).**
- The 10-K and the 10-Q do not feature an adjusted figure or EBITDA in the MD&A; the only EBITDA in the FY2025 10-K is in the
  put option of a noncontrolling partner (priced at the higher of fair value or an EBITDA multiple) and in the pay plan.
- Charges recurring under the "impairment, disposal and exit" heading: $10.0M goodwill impairment in FY2019; $46.7M in
  FY2023 (Portland plant, Gunderson Marine sale, Southwest Steel sale, Rayvag); European plant closures announced in FY2025
  (Romania, Poland, Turkey). The pay metrics exclude "facility-related rationalization/closure costs in Arad (Romania), Olawa
  (Poland), and Adana (Turkey)" (DEF 14A). See **[L2016-007]** on restructuring charges excluded year after year; not weighed.
- The segment basis changed three times in five years: the syndication allocation between Manufacturing and Leasing was
  re-measured from 2021-09-01 (FY2022 10-K) and again from 2025-09-01 (10-Q), and Maintenance Services was folded into
  Manufacturing from 2024-09-01 (FY2025 10-K). Each recast prior periods; the consolidated figures are unaffected.
- Equity-method income ($20.1M in FY2025) is not cash until paid; owner cash counts the affiliates' net cash only.

**Bearing on Q5 (the people): integrity facts.**
- Pay (DEF 14A `0001193125-25-284604`): the CEO and President, Lorie L. Tekorius, was paid $7,706,230 for FY2025
  ($6,500,650 in FY2024; $5,639,481 in FY2023). Fiscal 2025 performance share units vest 60% on "Company EBITDA", 20% on
  Company ROIC and 20% on relative TSR, with a threshold of 6% ROIC, a target of 10% and a maximum of 15%, and EBITDA
  thresholds of $840M, $1,250M and $1,560M for the performance period, as the proxy's table states them. EBITDA is defined as net earnings before interest
  and foreign exchange, tax, depreciation and amortization, excluding the European closure costs above. The rows on EBITDA
  **[M1998-086]** and on the hurdle **[M2004-097]** bear on this; not judged.
- The 2022 to 2024 PSU period: the FY2025 10-K records 55 thousand additional shares earned "based on the EBITDA
  criteria for which actual performance resulted in a payout above target" for the 2022 to 2024 period.
- The proxy asked owners to raise the authorized common shares above 50,000,000, stating that only a fraction remained after
  31,190,881 outstanding, 854,677 reserved for existing awards, 476,748 for future awards and 8,123,421 reserved for the
  convertible notes; and asked to add 1,000,000 shares to the stock plan. Diluted weighted shares were 31.78M against 30.94M
  basic in the nine months to 2026-05-31 (10-Q EPS note).
- Leadership: an 8-K of 2026-08-31 (item 5.02, `0001193125-26-376734`) announced the CEO and President's retirement,
  effective 2027-01-06 (the brief's description; the exhibit press release was not read). Forms 144 were filed on
  2026-01-30 and 2026-07-13 and Forms 4 through 2026-07-20 (titles only seen in the EDGAR index, not read).
- The proxy is where the rows read the record, "considering what the hand was that they were dealt" **[M1994-009]**; the hand here is a cyclical industry, and the record
  over the cycle is the return in Q2, item 9. Not judged.

**Bearing on Q6 (the money and the owners).**
- Dividends paid $23.3M (FY2016) rising to $39.6M (FY2025); $32.0M in the nine months to 2026-05-31.
- Buybacks: $33.5M FY2016, $20.0M FY2021, $56.9M FY2023, $22.7M FY2025, $13.3M for 313 thousand shares (about $42.50 each) in
  the nine months to 2026-05-31; the programme names a dollar amount ($100M, to 2027-01-31) and no price (10-Q). The prices
  paid sit above the bottom of the computed range, which is below zero; Q6's buyback test is not run because Q6 was not
  reached.
- Shares outstanding rose from 28.2M (2016-08-31) to 32.6M (2022-08-31), then fell to 30.9M; the FY2019 ARI purchase was paid
  in cash ($361.9M) and convertible notes.
- Cash distributed to the Mexican joint-venture partner: $95.1M in FY2016, $73.0M in FY2018, $38.8M in the nine months to
  2026-05-31.

**Bearing on Q9 (debt and exposures).**
- Debt $1,805.6M at 2026-05-31, of which recourse $733.3M (revolving lines $121.4M, senior term debt $240.6M, 2.875%
  convertible notes $373.8M due 2028-04-15) and non-recourse $1,072.3M against the lease fleet (Series 2026-1 notes $300.0M
  at 5.13% and 5.30%, anticipated repayment 2033). The 2028 notes are a maturity that "must actually be met by payment" if
  not refinanced **[L2010-020]**.
- Coverage on the rows' definition, pre-tax earnings over interest **[L2012-002]**: FY2025 earnings before tax and affiliates
  $284.4M against interest and foreign exchange $75.7M; in the FY2021 trough earnings before tax were -$8.6M against $43.3M.
- The acquisition criteria's "little or no debt" **[R1997-001]** is stated for whole businesses; recorded only.
- Contingent: Portland Harbor Superfund site, where the EPA's estimated cleanup cost is $1.7B for all parties, GBX is one of
  about 100 parties in the allocation, and the filer says "sufficient information is currently not available to determine
  our liability, if any, for the cost of any required remediation or restoration of the Portland Harbor Superfund Site or to
  estimate a range of potential loss" (FY2025 10-K Item 1, Environmental Matters).
- Two customers were 26% of FY2025 revenue (customer concentration).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 5542c4a8); written question by question; committed after each
      (5542c4a8 template; 711692db Step 0 to Q1; c1194579 Q2; this commit the close).
- [x] Dispatched: the brief allowed the per-question pathspec commits and the dispatching session holds the lock; the fold is
      the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. One listing of `Test Runs/` was
      made before the copy (to confirm that no file of this name existed); the names it showed are declared under
      contamination and were not used. GATX, whose run file name appeared in it, is used as a rival from its own filings.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-16 GBX/scripts/check_ids.py`); every filing fact has its
      accession; numbers are from the filings, the tools' arithmetic lines, or labelled CONVENTION.
- [x] The order was kept; Q2 closed the file; everything after it is NOT REACHED, the facts are under AFTER THE STOP, and the
      Q7 figures are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the generous beside case
      in the computation is labelled as such and decides nothing. Sovereign from the US Treasury; the price is an aggregator
      quote, flagged.
- [x] Contrary evidence written down as found (Foundations, item 5; Q2 item 5).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit.
- Weak points, declared: (1) the return-on-capital series uses a 25% tax on earnings from operations, a CONVENTION of the
  run, and the intermediate years' debt comes from `tools/run.py`'s XBRL table, not from each filed balance sheet; the
  FY2016, FY2019, FY2022 and FY2025 years were read from the filed statements. (2) Trinity's 2017 margin was not read, and
  Trinity's segment perimeter changed with the 2018 Arcosa spin-off. (3) FreightCar America's figures are XBRL
  transcriptions except the 2025 year, checked against its statement. (4) The competitor margins compare an August fiscal
  year with calendar years. None of these would move the box: GBX's own returns and cash over the cycle decide it.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q2's rule that "a durable castle that protects only ordinary returns closes OUT" says the field's returns are judged
"from the filer's and the rivals' filings" but not on what measure; I used after-tax earnings from operations on total
capital less cash for the filer, segment margins for the rivals (whose capital by segment is not comparable), and return on
equity as a cross-check, and said so. A named measure, or a rule that the run states its measure and shows a second, would
make two runs comparable. (2) The low-cost exception and the ordinary-returns rule pull against each other when, as here,
the filer is the better-margined of two large builders and still earns an ordinary return; the text says the low-cost
operator is "Another way to prosper" but not what to do when the operator has not prospered. I read the exception as
credited only where it shows in the returns, and closed OUT on the returns; the text does not say so in terms. (3) Q7
specific (e) lets depreciation stand in for maintenance spending, but for a lessor that grows its fleet with non-recourse
debt and sells cars out of it, the asset-sale proceeds and the fleet capex are both "growth" and both left out of the
maintenance case; the text does not say whether recurring sales of fleet cars, which the filer calls a normal part of the
business, belong to the maintenance case. I left them out of the central case and kept them in the all-spending case
beside it. (4) Specific (b)'s "where the series changes sign ... measured between the halves" gave a rate here (-37.4%)
because both half-averages were positive though the yearly series changed sign five times; the text does not say whether a
series that changes sign within each half still yields a meaningful halves rate. Nothing turned on it, since every case is
below zero. (5) The brief's departure (the analyst chooses the 10-K lines) worked; I stated the lines chosen under Step 0.
