
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0 and are written under AFTER THE STOP, Q4.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are recorded, not judged, under AFTER THE STOP, Q5; any later run that reaches Q5 must answer them.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts under AFTER THE STOP, Q6 (the buyback prices against the computed range are written there as facts, not weighed).

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures are computed below under **COMPUTATION, NOT A CLEARANCE**, as Part VII
(The owner's price) asks of a file closed before Q7.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP, Q9.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (No business on the rows' named list is carried on: the businesses are engineering, construction, government site
management and staffing.)

---
## COMPUTATION, NOT A CLEARANCE
*Operator rule 3: valuation arithmetic after a closing STOP. It carries no entry language, decides nothing, and does not reopen Q2. The
reporting figures are the owner's (a reporting convention, not a rule). Scripts and outputs: `owner_cash.py`, `owner_cash_output.txt`,
`value.py`, `value_output.txt` in the research folder. Note for the self-audit: these scripts were run while the filings were being
gathered, before the Q2 section was written; their outputs were headed as computation and did not enter the Q2 reasoning.*

**Owner cash after every real cost** (operator rule 5; never a net-income proxy), USD millions, from the filed cash-flow statements:
operating cash flow, less capital spending, less stock pay (a real cost added back inside OCF), less distributions paid to minority
partners (cash that leaves Fluor's owners). Two recastings, both stated:
- **NuScale removed (core).** NuScale was consolidated until October 2024 and its own operating cash outflow sat inside Fluor's OCF:
  $(99)M 2021, $(149)M 2022, $(183)M 2023, $(82)M nine months of 2024 (NuScale's filings, accessions in Step 0). NuScale was an
  investment, sold for about $2.43 billion (8-K `0001124198-26-000051`) whose proceeds are in today's net cash; its burn is added back
  so that it is not charged twice. NuScale's stock pay inside Fluor's consolidated figure was not separated (small; see What I could
  not get).
- **All-equity basis (central, Q7 On what the floor is earned).** Net interest income is removed after tax so that the cash earning it
  is counted once, in net debt. **CONVENTION of this run:** the US statutory rate of 21% is applied to net interest; rationale: the
  company's effective rate swung from 39% to 103% on items unrelated to interest, and no filing states the tax on the interest line.

| year | OCF | owner cash, literal | core | core, all-equity | core, all-equity, Santos added back | OC / revenue (core, all-equity) |
|---|---|---|---|---|---|---|
| 2016 | 706 | 372 | 372 | 414 | 414 | 2.17% |
| 2017 | 602 | 231 | 231 | 263 | 263 | 1.77% |
| 2018 | 162 | (155) | (155) | (123) | (123) | -0.65% |
| 2019 | 219 | (32) | (32) | (23) | (23) | -0.15% |
| 2020 | 186 | 28 | 28 | 64 | 64 | 0.41% |
| 2021 | 25 | (191) | (92) | (34) | (34) | -0.24% |
| 2022 | 31 | (123) | 26 | (2) | (2) | -0.01% |
| 2023 | 212 | 5 | 188 | 56 | 56 | 0.36% |
| 2024 | 828 | 619 | 701 | 583 | 583 | 3.57% |
| 2025 | (387) | (531) | (531) | (584) | 58 | -3.77% |

Means, core, all-equity: **literal window 2021 to 2025: $3.6M**; ten years 2016 to 2025: **$61.3M**; the cycle 2017 to 2024 (the year
after the 2016 high to the 2024 high): $97.9M; the window with the Santos payment added back: $132.0M. With net joint-venture funding
deducted as well (investments less returns of capital; $256M in 2025, of which $158M funded "a proportionately consolidated loss
project", FY2025 10-K), the window mean is $(87.2)M.

**Q7's range convention applied in full.**
- *The PG four.* Growth measured on aggregate owner cash, not per share; all capital spending deducted (the depreciation variant: capex
  ran below D&A in 2023 to 2025, $106M/$74M, $164M/$73M, $50M/$68M per `tools/run.py`, so the variant changes little); zero nominal
  growth after year ten; a price above the top of the range closes OUT through the floor.
- *(a) Cycles.* The last year of the window, 2025, is aberrational on the filer's own description: results "significantly impacted by a
  judgment on the long completed Santos project" (FY2025 10-K, Item 7). The base is therefore taken over the full cycle. **CONVENTION of
  this run:** the ten years 2016 to 2025 are the cycle base (central); rationale: the owner-cash series runs from a high (2016) through a
  trough (2018 to 2022) to a high (2024) and a new low (2025), and the ten years hold the whole swing without choosing which loss year
  to leave out; the 2017 to 2024 high-to-high span and the literal window are shown beside it.
- *(b) Decline.* The owner-cash series changes sign repeatedly, so its compound rate between end years is meaningless; between the first
  and second halves of the ten years it falls from $119M to $3.6M a year, a rate (about -50% a year) that is also meaningless on a
  series that crosses zero. By (b) the range would then be the no-growth case alone. **CONVENTION of this run:** the decline is carried
  as the bottom at the business's own sales growth, -2.26% a year (revenue $19,037M in 2016 to $15,503M in 2025, company facts);
  rationale: the business is shrinking on the filed record, (b) says a decline makes the bottom, and sales is the nearest filed series
  that does not cross zero.
- *(c) Acquisitions.* None in the window. Businesses sold (AMECO, Stork, the China fabrication yard, the Mexico joint venture) are not
  credited as owner cash: **CONVENTION of this run**, rationale: (c) nets sales against purchases, and with no purchases a sale is a
  shrinking of the business, not a cash yield; their cash is inside net cash. No signed, unclosed deal at the price date (the China yard
  sale closed in 2026 with a $124M gain, 10-Q). Not a serial acquirer.
- *(d) Working capital* is inside OCF and so counted; the 2025 working-capital release on "several large projects" is part of that
  year's figure.
- *(e) Growth spending.* The filings do not separate maintenance from growth capital spending (2025 capex "primarily related to
  investments in IT", 2024 "improvements to our new office lease in Houston"); the all-spending case is therefore central, said so.
- *(f) The cap.* Not engaged: the growth carried is negative. The highest share of revenue earned as owner cash in the years read was
  3.57% (2024).
- *Tax.* Owner cash is after the company's own tax as paid (inside OCF). No carryforward or credit that runs out inside ten years was
  priced (the effective rate was above statutory in each of 2023 to 2025, 75%, 103% and 39%, FY2025 10-K); not applicable.
- *Net debt* (all-equity basis, latest filed balance sheet 2026-06-30, 10-Q `0001124198-26-000071`): cash $2,923M plus marketable
  securities $120M less long-term debt $1,072M, plus the subsequent event the 10-Q itself states, the July 2026 sale of the Mexico
  joint venture for $175M less the $33M tax funded in August 2026: **net cash $2,113M** ($15.59 a share). Operating leases left out, and
  said so. Of the cash, $320M and $26M of securities relate to consolidated VIEs and are "not available for our general operations";
  excluding them, net cash would be $1,767M (shown, not used).

**The floor, tested first** (Q7 CONVENTION of 2026-10-10). Enterprise value at the price: $46.95 x 135.564M shares = $6,365M, less net
cash $2,113M = **$4,252M**. To earn about ten percent at no growth, owner cash before interest would need to be about $425M a year; to be
worth the price even at the 5.43% sovereign, about $231M. The cases: ten-year base $61.3M (1.44% on EV), cycle 2017 to 2024 $97.9M
(2.30%), window with Santos added back $132.0M (3.10%), literal window $3.6M (0.08%); with any growth case lower still. **No case in the
range earns the floor at the price.** Had Q7 been reached it would have closed OUT on the floor; the width test does not arise.

**(a) THE VALUE RANGE** (Q7's construction; central figure on the all-equity basis, net cash added back per share, 135.564M shares at
2026-06-30): **$22.55 to $23.91 a share, against a price of $46.95.** Bottom: the ten-year base declining at the sales rate for ten years,
then flat, at 5.43%. Top: the ten-year base at no growth. Beside it: the literal window, $16.00 to $16.08; the 2017 to 2024 cycle base,
$26.70 to $28.89; the window with the Santos payment added back, $30.57 to $33.52. At the cover count (133.741M) the central range would
be $22.86 to $24.24. The price sits above the top of every case.

**(b) THE FAIR PRICE** (Part VII: each end case valued at ten percent instead of the sovereign, the two averaged), after the company's own
tax, no conversion: **$19.79 a share on the all-equity basis (central)** (no-growth end $20.11, decline end $19.47). **Equity-only figure,
beside: $5.05 a share** (owner cash after interest, ten-year core mean $73.6M, valued at ten percent: no-growth $5.43, decline $4.67;
no net cash added, because the cash's interest is inside that owner-cash figure). The equity-only figure values $3.0 billion of cash and
securities only through its after-tax interest income capitalised at ten percent, which is why it is far below the central figure; it
never decides alone (Q7, On what the floor is earned). Beside the central figure: on the 2017 to 2024 cycle base, $22.30; on the window
with Santos added back, $24.64; on the literal window, $15.83. No other price figure is reported.

---
## THE BOX
**OUT, at Q2 (the castle is open on the filed evidence), integrity facts recorded, not judged.** Computed beneath the stop, not a
clearance: value range $22.55 to $23.91 a share (all-equity, ten-year cycle base) against $46.95; no case earns the floor; fair price
$19.79 (all-equity), $5.05 equity-only beside. Q11 belongs to the holding review, not to a purchase run.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no verdict; the box
unchanged (operator rule 2).*

**Q3 (capital).** Capital spending $50M to $283M a year over 2016 to 2025 on revenue of $13.7 billion to $19.0 billion; PP&E $446M at
2026-06-30. Working capital: accounts receivable $1,027M and contract assets $1,440M against accounts payable $1,762M and contract
liabilities $541M at 2026-06-30 (10-Q); client advances only $14M at 2025-12-31 (FY2025 10-K). Joint-venture funding: $278M invested
in 2025, including $158M "on a proportionately consolidated loss project for an infrastructure joint venture" and $33M for "a legal
settlement payment"; $101M in the first half of 2026. Claims: $214M of revenue recognised for claims at 2025-12-31 ($244M a year
earlier); "up to $105 million" of back charges that may be disputed.

**Q4 (the accounts). The balance sheets, read in Step 0 before the income account** **[M2025-032]** (USD millions; company facts and
`tools/run.py` ten-year table; 2026-06-30 from the 10-Q):

| year-end | assets | equity | cash + securities | goodwill | long-term debt | retained earnings |
|---|---|---|---|---|---|---|
| 2016 | 9,216 | 3,125 | 1,961 | 532 | 1,518 | 3,582 |
| 2017 | 9,328 | 3,342 | 1,965 | 565 | 1,592 | 3,655 |
| 2018 | 8,883 | 2,834 | 1,980 | 467 | 1,662 | 3,294 |
| 2019 | 7,967 | 1,488 | 2,005 | 508 | 1,652 | 1,701 |
| 2020 | 7,310 | 1,030 | 2,222 | 207 | 1,701 | 1,250 |
| 2021 | 7,089 | 1,393 | 2,336 | 249 | 1,174 | 791 |
| 2022 | 6,827 | 1,786 | 2,624 | 206 | 978 | 896 |
| 2023 | 6,973 | 1,940 | 2,588 | 206 | 1,158 | 979 |
| 2024 | 9,143 | 3,949 | 2,959 | 199 | 1,104 | 3,124 |
| 2025 | 8,236 | 3,244 | 2,194 | - | 1,070 | 3,064 |
| 2026-06-30 | 7,536 | 2,686 | 3,043 | - | 1,072 | 2,978 |

What moved and why: retained earnings fell by $2.9 billion from 2017 to 2021 (the 2019 charges and restatement, losses in 2020 and
2021); equity fell to $1,030M; the goodwill bought with Stork in 2016 ($532M) was impaired and then sold away; the recovery of equity in
2024 came from the fair-value mark on NuScale ($2,221M gain booked in 2024; the stake has since been sold for cash, so the cash now on the
balance sheet is the realised form of that mark); equity then fell again in 2025 to 2026 as $1.57 billion of shares were bought back
(2025 and first half of 2026). Cash has stayed near $2 billion to $3 billion throughout, part of it inside joint ventures and VIEs
($328M at 2025-12-31, "not necessarily readily available"). What the figures cannot say: the size of claims and estimates inside
contract assets, the subject of the 2019 restatement.
The restatement: the FY2019 10-K (filed 2020-09-25 after an NT 10-K, `0001628280-20-013900`) restated 2016, 2017 and 2018 and the
interim periods of 2018 and 2019, and reported material weaknesses, one in the Energy & Chemicals segment where "Former leaders of our
Energy & Chemicals segment caused pressure to be applied on the individuals charged with accounting and finance responsibilities in a
manner intended to present overly optimistic forecasts", which "in certain instances [...] gave rise to an override of our project
controls on a project and resulted in errors in our financial statements due to unsupported forecasted estimates". Construction in
progress is the accounting the rows name as one where "there’s so many ways you can cheat" **[M2013-086]**.
Featured figures: the release headline gives "Adjusted EBITDA" and "adjusted EPS" and the company gives and revises adjusted-EBITDA
guidance ("narrowing its 2026 adjusted EBITDA guidance from $525 – $560 million to $500 – $525 million", Exhibit 99.1,
`0001124198-26-000074`); the 10-K features non-GAAP "Total segment profit" and "adjusted net revenue". Under the framework these are
recorded at Q4 as a weighing against and carried to Q5 **[L2016-006]**, **[L2019-006]**; here they are recorded only. Stock pay $19M to
$48M a year (2016 to 2025). Effective tax rate 75% (2023), 103% (2024), 39% (2025).

**Q5 (the people). Integrity facts, recorded, not judged.**
- SEC investigation announced February 2020 into the second-quarter 2019 charges; DOJ subpoenas April 2020 and January 2022. "In May
  2023, the DOJ advised that it had closed its investigation and does not intend to bring charges. In September 2023, we entered into a
  settlement agreement with the SEC resolving the investigation and agreed to pay a civil penalty of $15 million." (FY2023 10-K,
  `0001628280-24-005451`).
- The restatement and the Energy & Chemicals "pressure" material weakness (Q4 above). The current chief executive, James R. Breuer
  (chief executive since May 2025, with the company since 1993), was "President, Downstream — Energy & Chemicals from 2019 to 2021"
  (FY2025 10-K, executive officers). The filings read make no finding about him; the fact of tenure is recorded only because a later run
  reaching Q5 must read it with the rest.
- Securities class action filed 2018 (class period August 2013 to February 2020), dismissed except for one 2015 statement about a
  gas-fired power contract, settled and approved November 2022 (FY2022 10-K, `0001628280-23-004139`); eleven derivative actions settled
  2023 (FY2023 10-K).
- New securities class action filed September 2025 over statements made from February to July 2025 "concerning market conditions,
  rising costs on three infrastructure projects and the effectiveness of our risk mitigation strategies"; four derivative actions and a
  books-and-records demand followed (FY2025 10-K). In February 2026 NuScale shareholders sued NuScale, two NuScale executives and Fluor;
  the July 2026 amended complaint added "two current Fluor employees who are former NuScale directors" (10-Q `0001124198-26-000071`).
- Guidance and an adjusted figure featured (Q4 above); under the framework these are judged at Q5 with the rest, and "If you’ve got
  doubts, forget it." **[M2013-088]** governs that later reading.

**Q6 (the money and the owners).**
- Buybacks: "Since we restarted the program in the fourth quarter of 2024, a total of 38 million shares have been purchased for $1.7
  billion through June 2026" (10-Q), an average of about $44.7; 2025, 18 million shares for $754M (about $41.9); first half of 2026, 17
  million for $816M (about $48.0); second quarter of 2026 at an average of $48.74 (10-Q, Part II). The programme names no price: "at such
  time and in amounts that we deem appropriate" (FY2025 10-K, Item 5). Against the computed range above (bottom $22.55), every reported
  average price paid sits above the bottom; under the framework's buyback convention that would weigh against at Q6 **[L2016-002]**;
  recorded, not weighed.
- NuScale: total investment $570M, sales of about $2.43 billion since September 2025 (8-K `0001124198-26-000051`); federal and state
  tax of $357M paid in 2026 "primarily related to the 2025 conversion of our shares in NuScale" (10-Q).
- Dividends: none since April 2020 (FY2025 10-K, Item 5).
- Pay (DEF 14A `0001104659-26-027053`): the 2025 incentive definitions of EBITDA exclude "significant litigation and regulatory costs and
  settlements or associated damages in excess of $10 million", marked as applicable in 2025 (the year of the Santos judgment); the chief
  executive's 2025 total compensation was $6,873,013, including $1,330,300 of non-equity incentive pay, in a year in which net earnings
  attributable to Fluor were a loss of $51M; long-term awards weighted 70% on annual EBT goals averaged over three years and 30% on
  relative TSR; a supplemental clawback was adopted in February 2026; the pay ratio was 97 to 1. Under the framework Part B would read
  these against "heads I win, tails you lose" **[L1994-020]**; recorded, not weighed.
- 2029 convertible notes (1.125%, conversion price $45.37, capped calls to $68.48); the stock traded above the conversion price in the
  second quarter of 2026, adding 872,024 shares to diluted shares (10-Q).

**Q9 (debt and exposures).** Long-term debt $1,072M (2028 notes and the 2029 converts) against cash and securities of $3,043M at
2026-06-30. The $2.2 billion credit facility (undrawn) "will require us to provide collateral to secure the facility should we be
downgraded to BB by S&P and Ba2 by Moody's, which is a one notch downgrade from both agencies' current ratings"; covenants include
debt-to-capitalisation at most 0.60 and minimum liquidity of $1.1 billion (FY2025 10-K, Item 7). Letters of credit $424M committed and
$918M uncommitted, including $347M for two lump-sum projects in Kuwait "substantially complete except for the resolution of unapproved
change orders and extension of time claims"; performance guarantees "estimated to be $14 billion". Santos: appeal hearing scheduled for
July 2026, insurer coverage dispute under a standstill (FY2025 10-K; the 10-Q reports the appeal hearing commenced). Joint and several
liability on venture contracts (Item 1A).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `3b4ce064`); written question by question; committed after each (Step 0 to Q1
      `2dac5292`; Q2 `e1741f77`; the rest in the final commit). The first write replaced the template's later headings with Step 0 to
      Q1; the remaining headings were restored from the template in this final section.
- [x] Dispatched: the brief allowed per-question pathspec commits of the run file and research folder only; the lock is the
      dispatching session's; the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination declared:** (1) a directory
      listing of `Test Runs/` filtered for today's date (made to check that this run's folder did not yet exist) showed the names
      `2026-10-17 Run - AMTM Amentum.md`, `2026-10-17 Run - ARCAY Arcadis.md` and their research folders; (2) the session's opening git
      context showed recent commit subjects about the AMTM run (its box, a figure share for its Global Engineering Solutions part, its
      competitor names). Neither file was opened. Amentum is a rival the 10-K names; it was not chosen for the competitor row, and nothing
      from those subjects was used. (3) The memory index loaded with the session names queue counts and "57 gate-clearers"; not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; every quoted fragment beside an id is in that row (check script
      `check_ids.py`, output `check_ids_output.txt`); no E-id. Every filing fact carries its accession; the competitor figures are flagged
      as XBRL transcription.
- [x] The order was kept; Q2 closed the run OUT; nothing after it is a clearance. **Declared:** the owner-cash and value scripts were run
      while the filings were being gathered, before the Q2 section was written (their outputs are headed as computation); they did not
      enter the Q2 reasoning, which rests on Items 1, 1A and 7 and the competitor row.
- [x] Owner cash after every real cost (stock pay, all capital spending, distributions to minority partners), never a net-income proxy;
      the sovereign from the US Treasury par curve; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (Foundations; Q1); facts for later questions under AFTER THE STOP, with the integrity flag
      in the box line.
- [x] No point-in-time anchor; no row dated after an anchor issue arises.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 text was ignored.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the reply to the dispatcher).

## WHAT I COULD NOT GET
NuScale's stock pay inside Fluor's consolidated stock pay (not separated; small against the gap to the floor). NuScale's operating cash
before 2021 (Fluor funded it then; left inside owner cash). Operating leases (not read; left out of net debt as the convention allows).
The rivals' figures were not checked against their filed statements line by line (XBRL transcription). No scuttlebutt (test 9 of Q2).
Cash and payments of proportionately consolidated joint ventures beyond what the 10-K states.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a contractor.** Q1 asks for "a reasonable fix on about what the earning power and competitive position will look
like" **[M2012-065]**, and the doubt row closes on any doubt **[M2002-092]**; a contractor's yearly earnings level is not predictable
(the filer says awards are "unpredictable"), yet its economic dynamics, and the absence of a moat, are plain. The text does not say
whether an unpredictable level with a foreseeable shape is a Q1 TOO HARD or a Q1 IN that Q2 then closes; this run read it as IN and let
Q2 decide, on M2011-014's "Is there ease of entry?". Two analysts could split here (Q1 TOO HARD (NATURE) against Q2 OUT), with the same
practical result but different boxes and re-look rules. (2) **Q7 (b) on a series that crosses zero.** (b) says that where halves are
meaningless "the range is the no-growth case alone"; it does not say whether a decline visible in another filed series (sales) may set
the bottom. This run carried sales decline as the bottom as a CONVENTION of the run; the text should say. (3) **Q7 (c) with sales and no
purchases.** "Cash paid for businesses, net of businesses sold" read literally would credit divestiture proceeds (AMECO, Stork, China
yard, Mexico joint venture) as owner cash in a shrinking business; this run excluded them and counted their cash in net cash. (4)
**Consolidated investee burn.** Neither Q4 nor Q7 says how to treat the operating losses of a consolidated investee later sold (NuScale);
the equity-method paragraph covers the reverse case only. (5) **The equity-only figure with large net cash.** Valuing owner cash after
interest at ten percent capitalises the cash at its interest yield ($5.05 against $19.79 here); the convention says the figure never
decides alone, but a reader of the two figures side by side may misread the gap. (6) **The template** asks for the balance sheets "in Step
0 if the file closes before Q4" but gives Step 0 no slot for them; they are written under AFTER THE STOP, Q4, with a note that they
were read in Step 0.
