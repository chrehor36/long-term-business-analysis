# Company Run — Carlisle Companies Incorporated (NYSE: CSL) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`, as amended to 2026-10-07). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md` (the canonical brief, slots filled by the dispatcher). The template was
copied to this file before any fetch; working folder `Test Runs/_research 2026-10-07 CSL/` (raw filings under its `cache/`,
which `.gitignore` covers; they are not committed).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared as found (not used):** (1) the session context showed `git status` and the last five commit subjects
of the repository: an untracked run file of another company dated today, and commit subjects reporting the boxes, deciding
questions and alert prices of four other companies' runs (AVGO, BMI, CB, CHD) and the CB run's Q5 to Q7 lines. None is about
Carlisle. (2) The session context carried the operator's memory index, whose lines say a count of "gate-clearers" and
"nothing buyable" across the register, and name the wave and its next name; nothing in it names Carlisle. (3) The lock file in
`Screens/_daily/` was read to confirm it was held (operator rule ten, b): its line reads "interactive v5 re-runs batch 3". No
other run file about Carlisle, no holding review, no `PORTFOLIO.md`, no register or reading list, and no unadopted case file was
opened, listed or searched. `Test Runs/` was not listed.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $325.74 (close 2026-10-06; the live quote printed by `python tools/run.py CSL`, an aggregator, flagged under
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $1 par, **39,714,133** shares as of 2026-07-23
  (Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession `0000790051-26-000037`;
  `python Screens/cover_shares.py CSL`). Check: the 10-Q balance sheet shows 78.7M issued and 38.8M in treasury, 39.8M
  outstanding at 2026-06-30, consistent with the cover count after July purchases. No 8-K or prospectus after the 10-Q
  changes the count (the two later 8-Ks are a director's resignation, `0000790051-26-000042`, 2026-09-10, and the Q2 results
  release, `0000790051-26-000033`). The company was buying in its stock through the third quarter at a stated full-year
  target of $1.2 billion (10-Q MD&A), so the count on the price date is somewhat below the cover count; the cover count is used.
- **Market cap:** 39.714M × $325.74 = **$12,936M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, US Treasury daily par yield curve, 30-year, 2026-10-06
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): Form 10-K FY2025 (filed 2026-02-13, `0000790051-26-000012`); 10-K FY2024
  (`0000790051-25-000077`), FY2023 (`0000790051-24-000058`), FY2022 (`0000790051-23-000044`), FY2021 (`0000790051-22-000061`),
  FY2020 (`0000790051-21-000080`), FY2019 (`0000790051-20-000071`), FY2018 (`0000790051-19-000070`), FY2017
  (`0000790051-18-000095`), FY2016 (`0001558370-17-000547`), FY2015 (`0001047469-16-010052`), FY2013 (`0001047469-14-001036`),
  FY2011 (`0001047469-12-000814`), FY2009 (`0001047469-10-000983`), FY2007 (`0001047469-08-002024`), for the segment over the
  last two cycles; the latest 10-Q (Q2 2026, `0000790051-26-000037`); the proxy (DEF 14A filed 2026-03-17,
  `0001193125-26-109193`); the 8-Ks of 2026-04-30 (`0000790051-26-000020`, the meeting vote) and 2026-09-10.
  **One figure cross-checked against the filed statement:** net cash from operating activities FY2025, $1,101.8M on the filed
  Consolidated Statement of Cash Flows (10-K FY2025, page 29), against $1,102M in the XBRL table `tools/run.py` printed: agree.
- `python tools/run.py CSL`, arithmetic lines only (saved as `runpy_CSL.txt` in the working folder): OCF − SBC − capex
  $1,018M (2023), $884M (2024), $936M (2025) as filed **consolidated, including discontinued operations in 2023 and 2024**;
  the tool's three-year and five-year means are therefore not the continuing business and are not used. Owner cash is
  rebuilt for the continuing business at Q4 and Q7 from the filed statements and the discontinued-operations notes.
  D&A $205M / $173M / $196M (2023-2025 as printed, consolidated); capex $142M / $113M / $131M (consolidated). SBC as filed
  $41.5M / $30.1M / $34.8M (cash-flow statement; the stock-pay note gives $31.7M, $32.9M, $34.8M for continuing operations).
  The tool's yield, "growth the price assumes" and "points over the sovereign" lines are v4 material and are not used
  (Part VII, the tooling).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own Carlisle "if the market closed for five years"
**[M1997-109]**, which turns the run toward the roofing business and away from the quotation. The market serves and does not
instruct **[M2006-077]**: the stock has fallen from its 2024 level (the 10-K's five-year return table shows $246.48 at the end of
2024 against $216.26 at the end of 2025 per $100 invested in 2020) and that fall tells nothing by itself. Margin of safety is
an attitude here and arithmetic only at Q7 **[M1996-084]**. Who is paid to tell you: the company features "Adjusted EBITDA" in its
summary results and a strategic plan ("Vision 2030") with financial objectives; both are carried to Q4 and Q5. The analyst's
habits: hunt the evidence against hardest **[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**:
(i) two distributors, QXO/Beacon and ABC Supply, were 16.7% and 16.3% of 2025 revenue (10-K FY2025, Note 6), and the risk
factors say "Some of the Company’s key customers enjoy significant purchasing power that may be used to exert pricing
pressure"; (ii) the 2016 10-K said CCM's prices were "subject to significant competition, in particular from competitors that
have recently added manufacturing capacity"; (iii) CCM's operating margin moved between 10.3% (2008) and 21.0% (2016) over the
old cycle and has run at 26.8% to 30.2% only since 2022; (iv) raw materials are about 66% of cost of goods sold (10-K FY2025,
Item 1A), and the 2026 10-Q reports "elevated input costs outpaced pricing realization".

## THE STANDING RULE
The buyer's conduct: a cash purchase of a listed common share, unlevered, sized by the owner; no borrowed money, no
collateral, no option given **[L2014-024]**, **[M2012-081]**. The standing rule is not engaged by the purchase as such; it
would be engaged only by financing or sizing, which this run does not set.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The business as filed.** Since the sales of Carlisle Interconnect Technologies (CIT, closed 2024-05-21, $2.025 billion) and
Carlisle Fluid Technologies (CFT, closed 2023-10-02, $520 million) (10-K FY2025, Note 4, `0000790051-26-000012`), and of
Carlisle Brake & Friction (2021, $247.7 million plus a $132.0 million earn-out and real estate in 2022; 10-K FY2022,
`0000790051-23-000044`), Carlisle is two reported segments of building products: **Carlisle Construction Materials (CCM)**,
single-ply roofing membranes (EPDM, TPO, PVC), polyiso insulation and architectural metal, sold "in warranted systems or
separately in non-warranted systems", 74% of 2025 revenue; and **Carlisle Weatherproofing Technologies (CWT)**, waterproofing,
air and vapor barriers, underlayments, spray foam and expanded-polystyrene insulation, 26%, about 44% of it residential
(10-K FY2025, Item 1 and Note 6). Demand at CCM is "primarily driven by the need to replace older, existing roofs on
non-residential structures, and to a lesser extent, new construction"; re-roofing "represents approximately 70% of our
commercial roofing business" (10-K FY2025, Item 1 and MD&A). The same share was stated ten years earlier ("approximately 70%
of net sales from r[e-roofing]", 10-K FY2015, `0001047469-16-010052`, MD&A), and the 2013 10-K records the shift to re-roofing
over the preceding years (`0001047469-14-001036`).

**Which part decides (Q1's holding-company paragraph read with Q2's business of parts, CONVENTION of the framework).** Segment
operating income 2021-2025, on the current segment basis: CCM $619.9M, $1,175.0M, $913.9M, $1,084.3M, $997.2M = $4,790.3M; CWT
$64.4M, $128.6M, $187.9M, $173.6M, $101.9M = $656.4M (10-K FY2022, FY2023, FY2025 segment tables). CCM carries **88%** of
five-year segment operating profit and decides; CWT does not decide.

**The tests, applied to CCM.**
1. *Where will it be in ten years* **[M1997-021]**, **[M1999-132]**: selling replacement roofs to the owners of an installed
   base of low-slope non-residential roofs, "over 70% of which is more than 25 years old" (10-K FY2025, MD&A, the filer's
   statement), through distributors to authorised contractors, as one of "four major manufacturers in the single-ply industry"
   (10-K FY2025, Item 1). The product family has changed slowly: CCM supplied "the first single-ply" EPDM membranes "in the early
   1960s" and has been a leader through the long shift from EPDM to TPO (10-K FY2007 names EPDM and TPO; FY2015 adds PVC; FY2025
   adds architectural metal), with no instance in the filings read of the shift costing it its position.
2. *The key variables and how predictable they are* **[M1998-044]**: (a) re-roofing volume, which follows the age of the
   installed base and is the more predictable half of demand; (b) new-construction volume, cyclical and about 30% of the roofing
   business; (c) the spread between selling price and petrochemical inputs (raw materials and inbound freight "approximately
   66%" of cost of goods sold in 2025), which moved CCM's margin from 17.6% to 10.3% between 2007 and 2008 (10-K FY2009,
   `0001047469-10-000983`) and is the least predictable variable; (d) the bargaining power of two distributors with a third of
   revenue. (a) and (b) can be pictured; (c) and (d) are the castle's question and are taken to Q2, not settled here.
3. *Do the past statements tell me the future ones* **[M2008-033]**: yes in kind; the segment has filed separately for two
   decades, and the statements show the pattern of volume, price and raw-material cost that will recur.
4. *Important and knowable* **[M2006-076]**; *would the insiders write it down* **[M2000-105]**: the industry's own filers
   write their long-run demand down (Carlisle's "re-roofing cycle"; the rivals' filings at Q2 say the same), and none treats
   ten-year demand for commercial roofs as unforecastable. The margin level is not written down by anyone, and that is Q2's
   question.
5. *Is the forecast about technology*: no. Product change is slow and incremental (thinner polyiso, wider sheets, adhesives);
   no technological component of significance threatens the business as it exists **[M1998-008]**.
6. *Do I doubt it is inside* **[M2002-092]**: the doubt this run carries is about the level and durability of CCM's margin,
   not about what the business is or how it earns; that doubt is the castle question and is judged at Q2, where the framework
   puts it (Q1, The routing, fixed).
7. *Do I only think I understand it* **[M1997-024]**: guarded against by reading the old cycle (2007-2021), not the last four
   years alone.

**VERDICT: IN.** A roofing manufacturer whose demand is mostly replacement of an aging installed base, in a product family that
has changed slowly for sixty years, can be given "a reasonable fix on about what the earning power and competitive position
will look like in five or 10 years" **[M2012-065]** as to its kind; the economics of the industry are understood **[M2011-014]**.
What is not foreseeable from Q1 is the margin the castle protects, and that belongs to Q2.


## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**; the moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (section B of the gaps case, as written in Q2; five-year segment operating income 2021-2025 from the
10-Ks FY2022 `0000790051-23-000044`, FY2023 `0000790051-24-000058`, FY2025 `0000790051-26-000012`):

| part | share of five-year operating profit | castle | decides |
|---|---|---|---|
| CCM, commercial single-ply roofing, polyiso, architectural metal | $4,790M of $5,447M, **88%** | one of four single-ply makers; warranted systems; replacement demand; excellent returns on capital over the old cycle (below) | **yes** |
| CWT, waterproofing, air barriers, underlayment, spray foam, EPS insulation (44% residential) | $656M, **12%** | "numerous, usually local or regional competitors" (10-K FY2025, Item 1); operating margin 8.7%, 6.5%, 8.2%, 14.1%, 13.4%, 7.8% (2020-2025) on $1,110M of intangibles and $460M of goodwill; the Henry trade name's fair value exceeded its $219.0M carrying value "by less than 10%" at the 2025 test | no; carried to Q7 as an ordinary business at no growth |

The file is decided on CCM, read separately **[L2008-005]**.

**CCM over the cycles, from the filer's own segment tables** (operating income or EBIT, as filed):

| year | net sales $M | EBIT $M | margin | note (filing) |
|---|---|---|---|---|
| 2007 | 1,370 | 240.5 | 17.6% (14.0% without a $48.5M gain on the Icopal stake) | 10-K FY2009 |
| 2008 | 1,470 | 151.1 | 10.3% | "increased raw material costs, unfavorable product mix, and continued competitive pricing" |
| 2009 | 1,130 (−24%) | 155.2 | 13.8% | volume −24%; "favorable raw material costs" |
| 2010 | 1,223.6 | 159.2 | 13.0% | "3.5% lower selling prices" (10-K FY2011) |
| 2011 | 1,484.0 | 177.9 | 12.0% | "significantly higher raw material costs" |
| 2012 | 1,695.8 | 273.4 | 16.1% | price realization (10-K FY2013) |
| 2013 | 1,776.5 | 264.0 | 14.9% | "lower selling price and higher raw material" |
| 2014 | 1,935.4 | 268.8 | 13.9% | "higher sales volume, partially offset by lower selling price" (10-K FY2015) |
| 2015 | 2,002.6 | 351.1 | 17.5% | lower raw materials; price −1.0% |
| 2016 | about 2,050 | 430.5 | 21.0% | volume +5.1%, price −2.2%; "competitors that have recently added manufacturing capacity" (10-K FY2016) |
| 2017 | not extracted | 421.9 | 18.1% | "lower selling price at CCM" (10-K FY2018) |
| 2018 | 2,880.3 | 435.4 | 15.1% | raw material inflation; Accella acquired (10-K FY2019) |
| 2019 | 3,233.3 | 576.0 | 17.8% | Petersen acquired; "continued price leadership" |
| 2020 | 2,335.4 (current basis) | 524.2 | 22.4% | 10-K FY2022, recast |
| 2021 | 2,846.2 | 619.9 | 21.8% | price realization against raw material inflation |
| 2022 | 3,885.2 | 1,175.0 | 30.2% | "favorable price to raw materials inflation" (10-K FY2023) |
| 2023 | 3,253.4 (−16.3%) | 913.9 | 28.1% | destocking, project delays; no price decline stated |
| 2024 | 3,704.3 | 1,084.3 | 29.3% | "inventory normalization and growing re-roof activity" |
| 2025 | 3,721.7 | 997.2 | 26.8% | new construction at "the bottom of the cycle" (filer); higher operating costs |
| H1 2026 | 1,939.4 | 522.1 | 26.9% | raw material and freight spike; three price increases April to August (10-Q) |

The segment's sales before 2020 include the weatherproofing lines later moved to CWT, so the old and new margins are not on an
identical basis; the 2020-2021 recast (22.4%, 21.8%) bridges them.

**Return on the capital the business needs, over the old cycle** (CCM EBIT against CCM identifiable assets including its
goodwill, as filed in Item 1's segment table: 10-K FY2011, FY2013, FY2015): 2009 27.1% ($155.2M on $572.4M), 2010 26.8%,
2011 23.0%, 2012 31.8%, 2013 29.8%, 2014 29.4%, 2015 39.0% ($351.1M on $899.2M), pre-tax. In the trough years, with volume
down a quarter (2009) or margins squeezed by raw materials (2011), the segment still earned more than 23% pre-tax on all the
assets it carried, goodwill included.

**The castle tests.**
1. *Key factors and how permanent* **[M1995-038]**: (a) the installed base: about 70% of the roofing business is replacement,
   stated in 2015 and 2025; (b) the system and its warranty: membranes, insulation and accessories "sold together in warranted
   systems", with extended warranties of five to 40 years on installed systems, priced separately and deferred (contract
   liabilities $372.3M at 2025 year-end, Note 6); a warranty that long can be offered only by a maker the owner expects to be
   there; (c) four makers: CCM is "one of four major manufacturers in the single-ply industry" in each 10-K searched from FY2018
   to FY2025 (FY2018, FY2019, FY2021 to FY2025); the same four names recur (Carlisle; Firestone Building Products, now Amrize's Elevate; GAF; Johns Manville), and
   Amrize lists "Carlisle, CertainTeed, GAF, Johns Manville, Owens Corning and RPM" as its principal envelope competitors
   (Amrize 10-K FY2025, `0002035989-26-000017`, Item 1). None of this depends on the genius of the lord in the castle.
2. *The attacker with money* **[M2011-015]**: the evidence in the filings is that money buys in rather than builds in.
   Holcim entered by buying Firestone Building Products (2021), then Malarkey (2022) and Duro-Last (2023, acquisition spending
   of $1,358M "primarily related to the acquisition of Duro-Last"; Amrize 10-K FY2025); its envelope segment now carries
   $4,026M of goodwill in $6,959M of segment assets. No instance found, in the filings read, of a new single-ply maker
   entering by building. Incumbents do add capacity (CCM's 2016 10-K names competitors' new capacity), and "one competitor is
   frequently enough to ruin a business" **[M2012-108]**: the 2008, 2010 and 2013-2017 price cuts show what four incumbents
   can do to each other's margins. They did not do it to the return on capital, which stayed above 23% pre-tax.
3. *Pricing power and the agony before a price rise* **[M2005-020]**: the old cycle shows price following raw materials both
   ways (cuts of 1% to 3.5% in 2010, 2013, 2014, 2015, 2016, 2017), the mark of a business that passes costs through rather than
   one that sets price; "over time the businesses with strong competitive positions manage to pass through increases in raw
   material costs" **[M2005-017]**, and CCM did, with lags (the 2008, 2011 and 2018 margins fell first). The new behaviour,
   since 2022: no price decline stated by the filer in 2023 when raw materials fell and volume fell 16%, and three increases in
   2026 with the quarter's margin one point lower. **Contrary evidence, written down as found** **[M1997-127]**: Amrize says
   its envelope segment's 2025 decline "was attributable to lower volumes and pricing".
4. *Would the customer still choose it over the low bid* **[M2017-009]**: the building owner buys a warranted roof through a
   contractor the maker has authorised, and the long warranty favours a maker that will be there for its term; but the
   specification is shared by four makers, and the distributor, not the owner, places much of the order. On this test the
   castle is a shared one, the four against everyone else, not Carlisle against the other three.
5. *The intermediary* **[M2019-041]**, **[M2001-090]**: QXO/Beacon and ABC Supply took 16.7% and 16.3% of 2025 revenue; QXO,
   which bought Beacon in April 2025, says it keeps "purchasing leverage" and names Carlisle Construction Materials among its
   largest suppliers (QXO 10-K FY2025, `0001628280-26-012601`, Item 1). The risk is real and recurring; the evidence of damage
   is not yet in the numbers (CCM 2025 margin 26.8%, H1 2026 26.9%).
6. *The low-cost position*: not established. The filings give no unit-cost comparison among the four, and none is claimed.
7. *Ask the competitors* **[M1999-130]**: Amrize names Carlisle first in its list of principal envelope competitors.
8. *Widening or narrowing* **[M1999-108]**: on the margin record, wider since 2022; on the structure, the same four makers and
   a more concentrated distribution channel. The widening is not credited (below).
9. *What could destroy, modify or reduce it* **[M2000-014]**: a price war among the four (the old cycle's record), the
   distributors' leverage, a fifth maker built rather than bought, a product shift (EPDM to TPO happened, with Carlisle a leader
   through it). No change of a kind that would make the business unforecastable was found.

**The competitor row** (same years, each rival's own filing):

| rival | metric | figures | source |
|---|---|---|---|
| Amrize Building Envelope (Elevate, Duro-Last, Malarkey; spun from Holcim 2025) | segment adjusted EBITDA margin | 22.0% (2023), 22.8% (2024), 22.2% (2025), against CCM's adjusted EBITDA margin 30.0%, 31.4%, 29.2% | AMRZ 10-K FY2025, `0002035989-26-000017`, segment note; CSL 10-Ks FY2023, FY2025 |
| Owens Corning Roofing (residential shingles, the CWT and residential side of the field) | EBIT, then EBITDA from 2023 | EBIT $185M (2008), $530M (2009), $405M (2010, "EBIT margins of 22 percent"), $266M (2015), $486M (2016); EBIT margin 21%, 17%, 17% (2017-2019), 21.9%, 23.5%, 22.7% (2020-2022); EBITDA margin 30.7%, 33.1%, 31.8% (2023-2025), on segment assets of $3,223M (2025) | OC 10-Ks FY2010 `0001193125-11-037296`, FY2016 `0001370946-17-000006`, FY2019 `0001370946-20-000015`, FY2022 `0001370946-23-000010`, FY2025 `0001370946-26-000067` |
| Beacon (now QXO Building Products) | not a competitor: Carlisle's largest customer | gross margin 25.7% in 2023 and 2024, on selling prices "approximately 1-2%" higher and product cost "approximately 0-1%" higher in 2024 | BECN 10-K FY2024, `0001124941-25-000021`, MD&A |
| GAF (Standard Industries) | private; not an SEC filer; flagged, no figures | none | none |
| Johns Manville | owned by Berkshire Hathaway, not separately reported; flagged, no figures | none | none |

**The field's returns over the last full cycle, judged in words** (section C): the old cycle, from the 2007 peak through the
2008-2011 trough to the 2016 peak, is the last full cycle on the record. Over it CCM earned 23% to 39% pre-tax on all the
assets it carried; Owens Corning's roofing business, in the neighbouring residential field, earned margins in the high teens to
low twenties outside 2008. These are not ordinary returns: the castle protected excellent returns on the capital the business
needs across a trough, which is what a moat is for **[L2007-004]**. A field of whom it is said "you can have only two
competitors and they’re still terrible businesses" **[M2013-052]** is not this one: four makers cut price to each other in the
old cycle and still earned these returns.

**The change for the better since 2022, not credited.** CCM's margin has run at 26.8% to 30.2% since 2022 against 10.3% to
22.4% before, and Owens Corning's roofing margin rose in the same years, so the change is field-wide, not Carlisle's alone. It
has held through a 16% volume fall (2023), a new-construction trough (2025) and a raw-material spike (2026), but not through a
non-residential construction recession, and a rival reports lower envelope pricing in 2025. "the railroads were a terrible
business for decades and decades and decades and then they got good" **[M2017-026]**; the framework credits such a change
only on a full cycle in which the price behaviour held **[M2005-020]**, **[L1995-022]**, and that cycle has not run. The
castle verdict below does not rest on the change; whether the change lasts is carried to Q7, where it sets the distance
between the bottom and the top of the range.

**VERDICT: IN.** The deciding part's castle stands on the evidence of the last full cycle: four makers for decades, entry by
purchase rather than construction, warranted systems sold into replacement demand, and pre-tax returns above 23% on the
segment's assets through the trough **[L2007-004]**, **[M1995-038]**, **[M2011-015]**. It is a shared castle with commodity
habits in its pricing **[M2005-017]**, and its post-2022 margin is not credited **[M2017-026]**; neither makes it open on the
evidence, and its future can be judged **[M2000-014]**. CWT does not decide and is carried to Q7 at no growth.


## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The test is the return "in terms of the capital actually needed in the business" **[M2010-090]**, on "return on tangible
assets", with goodwill left out for the business and put back for the capital allocation "because we paid for it"
**[M2011-060]**.

**The capital the business needs (10-K FY2025, balance sheet and Notes 9, 10, 12).** At 2025 year-end: receivables $593.8M,
inventories $447.3M, prepaid and other current $124.2M, less payables $233.0M and other current liabilities $503.0M (which
include $147.8M of accrued taxes swollen by the tax-credit item at Q4), net working capital about $429M; property, plant and
equipment $807.1M. Tangible operating capital about **$1.24 billion** (operating-lease assets of $129.6M and the $372.3M of
deferred warranty revenue, a source of capital, both left out). Against it, 2025 operating income $1,002.5M plus $121.9M of
amortization of purchased intangibles, about $1.12 billion pre-tax: roughly 90% pre-tax on tangible operating capital, in a
year the filer calls the bottom of the new-construction cycle. On the old cycle, at the segment level, CCM earned 23% to 39%
pre-tax on all its assets including goodwill (Q2). This is the first kind of business in the 1998 ranking, or near it: "more
and more money every year without putting up anything to get it, or very little" **[M1998-081]**.

**Reinvestment to stand still and to grow.** Capital spending on the continuing business: $105.5M (2021), $158.8M (2022),
$110.8M (2023), $100.9M (2024), $131.2M (2025) (segment notes, 10-K FY2023 and FY2025), 2.0% to 2.9% of revenue, against
depreciation of $74.6M in 2025 (cash-flow statement). The filer describes its capital spending as "new product and capacity
expansion, business sustaining projects and cost reduction efforts" (10-K FY2023, MD&A) and gives no split. The maintenance
guess **[M2000-144]**, **[L1999-024]**: depreciation as the proxy "not inappropriate in most companies" **[M1998-127]**, about
$75M a year, with the balance, about $50M to $60M a year, growth and cost-reduction spending. Working capital moved with price:
a $275.2M use in 2021 as raw materials inflated (10-K FY2021, MD&A), a release in 2023 as they fell.

**What the added capital earned: the acquisitions.** Most incremental capital in the last decade went to purchases, not plant.
CCM: Accella, Drexel and Arbo ($720.6M, 2017), Petersen ($207.2M, 2019), MTL ($424.6M, 2024). CWT: Henry ($1,571.3M, 2021),
Polar ($36.1M, 2023), PFB ($266.5M, 2024), ThermaFoam ($53.7M) and Bonded Logic ($61.4M) (2025) (10-Ks FY2018, FY2019, FY2021,
FY2025, Note 3). CWT, built mostly from these purchases and carrying $1,110M of intangibles and $460M of goodwill, earned
segment operating income of $64.4M, $128.6M, $187.9M, $173.6M, $101.9M (2021-2025); adding back its amortization ($83.3M in
2025), about $185M pre-tax in 2025 on purchase capital of well over $2 billion, under 10% pre-tax. MTL contributed $86.9M of
revenue and $8.5M of operating income in its first eight months (Note 3). Where "you have to include goodwill, because we paid
for it" **[M2011-060]**, the CWT purchases have earned a poor return on what was paid; "whether that’s good or bad depends on
what we earn on that incremental $130 million over time" **[M2001-019]**, and so far it is not good.

**The growth arithmetic and its cap.** Organic revenue growth, weighted from the segments' filed organic rates: +31.2% (2022, mostly price), −15.8%
(2023), +7.2% (2024, computed from the filed change less MTL and PFB's filed contributions), −2.9% (2025); 3.5% a year
compounded 2021-2025, −4.3% a year from the 2022 peak (working in `val.py`). QXO puts the long-term growth of the roofing
market at "3% to 5%" a year (QXO 10-K FY2025, citing a third-party report). Nothing in the record supports a rate that runs
toward the discount rate; Q7 carries no more than the organic figure shown.

**WEIGHS FOR** on the capital the roofing business needs: very high returns on tangible capital, through the old trough as well
as now, with little reinvestment to grow **[M1998-081]**, **[L2009-012]**; **AGAINST** on the capital added by purchase in CWT,
which has earned under 10% pre-tax on what was paid **[M2011-060]**, **[M2001-019]**. On balance FOR, the deciding part
dominating; the acquisition record is carried to Q6.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends** **[M2025-032]** (`tools/run.py` table, first-filed XBRL vintages, read against the
filed statements of 10-Ks FY2016 to FY2025; USD millions):

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | LT debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 3,966 | 2,467 | 385 | 512 | 377 | 1,081 | 872 | 596 | 2,547 |
| 2017 | 5,300 | 2,528 | 380 | 658 | 508 | 1,602 | 1,234 | 1,586 | 2,821 |
| 2018 | 5,249 | 2,597 | 804 | 698 | 458 | 1,442 | 968 | 1,588 | 3,351 |
| 2019 | 5,496 | 2,643 | 351 | 783 | 511 | 1,716 | 1,141 | 1,341 | 3,721 |
| 2020 | 5,866 | 2,538 | 902 | 613 | 504 | 1,738 | 1,035 | 2,080 | 3,929 |
| 2021 | 7,247 | 2,630 | 324 | 815 | 605 | 2,199 | 2,009 | 2,575 | 4,238 |
| 2022 | 7,222 | 3,024 | 400 | 829 | 749 | 2,201 | 1,837 | 2,282 | 5,027 |
| 2023 | 6,620 | 2,829 | 577 | 615 | 362 | 1,202 | 1,253 | 1,887 | 5,634 |
| 2024 | 5,817 | 2,463 | 754 | 580 | 473 | 1,478 | 1,505 | 1,887 | 6,773 |
| 2025 | 6,263 | 1,795 | 1,112 | 594 | 447 | 1,539 | 1,426 | 2,882 | 7,332 |

(2016-2022 include businesses later sold; 2023 moves CIT to held-for-sale.) What the figures say: retained earnings rose every
year, from $2.5 billion to $7.3 billion, while equity fell from $3.0 billion (2022) to $1.8 billion (2025), because treasury stock
rose to $6,149M at cost: buybacks of $900M (2023), $1,586M (2024) and $1,300M (2025) took more than the operating earnings and
the divestiture proceeds together, and $1.0 billion of new notes in August 2025 (2035 and 2040 Notes) funded part of them.
Goodwill and intangibles ($2,965M) exceed equity: tangible equity is about −$1.2 billion. Long-term debt went from $596M to
$2,882M over the decade. Receivables (11.8% of 2025 revenue) and inventories (13.9% of 2025 cost of goods sold) are in line with
sales; no prepaid or deferred account is building (prepaid $28.5M); the deferred warranty revenue grows steadily ($294.8M at
2023's opening to $372.3M at 2025's close, Note 6) with revenue deferred $52.5M to $56.1M a year and recognised $26.9M to
$30.7M. What they do not say: the margin of each part on its own capital (segment assets stopped being reported), and the
cost of warranty service, which is expensed as incurred and reserved only if expected costs exceed the deferred revenue (Note
1); no such reserve is recorded. What they cannot say: whether the post-2022 margin is the castle or the cycle (Q2).

**The recast: owner cash of the continuing business** (USD millions; working in `val.py`; operating cash flow from the filed
statements less the discontinued operations' operating cash flow from the discontinued-operations notes of 10-Ks FY2023 and
FY2025; stock pay from the stock-pay note, continuing; capital spending from the segment notes; after-tax net interest added
back for the all-equity basis at each year's effective tax rate):

| year | OCF, continuing | stock pay | capital spending | after-tax net interest | owner cash, all-equity | owner cash, equity-only |
|---|---|---|---|---|---|---|
| 2021 | 332.1 | 27.0 | 105.5 | 62.3 | 261.9 | 199.6 |
| 2022 | 940.4 | 25.0 | 158.8 | 60.4 | 817.0 | 756.6 |
| 2023 | 1,037.2 | 31.7 | 110.8 | 42.9 | 937.6 | 894.7 |
| 2024 | 1,039.2 | 32.9 | 100.9 | 10.1 | 915.5 | 905.4 |
| 2025 | 1,103.6 | 34.8 | 131.2 | 41.2 | 853.8 (after −125.0) | 812.6 (after −125.0) |

The 2025 adjustment: the 10-Q for Q2 2026 says operating cash fell partly because of "a $125 million post-year-end settlement of
an accrued liability related to a transferable energy tax credit acquired in 2025"; the 10-K had attributed the 2025 swing in
other current liabilities to "the timing of tax expenses and payments" and accrued income taxes rose from $55.3M to $147.8M
(Note 12). The payment belongs to the year whose taxes the credit paid, so $125.0M is taken out of 2025 (CONVENTION of this
run: the filer ties the item to one transaction, the case specific (d) names for working capital). Depreciation is a real cost
and is inside the figure through capital spending **[L2015-004]**; stock pay is deducted **[L2015-003]**; amortization of
purchased customer relationships and trade names is not deducted, since such charges "arise through purchase-accounting
rules" **[L2012-003]**, and the purchases themselves are charged at Q7 as acquisitions (specific (c)).

**The real costs and the habits.**
- *EBITDA and the adjusted figure, in the filer's own mouth.* The 10-K's MD&A table of "Summary Financial Results" carries
  "Adjusted EBITDA" and its margin beside GAAP operating income, and devotes a section to it; the Q2 2026 release (8-K
  `0000790051-26-000033`, Exhibit 99.1) headlines "record adjusted EPS of $7.03", an outlook "with flat adjusted EBITDA margin",
  and "our path to $40 of adjusted EPS and 25%-plus ROIC under Vision 2030". Adjusted EPS removes acquisition amortization
  (which the rows allow **[L2012-003]**), restructuring, acquisition costs, legal settlements and discrete tax items. EBITDA is
  "utter nonsense" as earnings **[M1998-086]**; "a management that regularly attempts to wave away very real costs by
  highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**.
- *The recurring one-time.* "Non-comparable items" appear every year: acquisitions $11.5M and $15.0M, restructuring $9.8M and
  $2.9M, legal settlements $3.6M and $2.6M, pension settlements $3.0M and $21.1M (2025, 2024); restructuring again $8.4M in
  H1 2026. Small against $1 billion of operating income, but recurring; "to tell owners year after year, "Don't count this,"
  when management is simply making business adjustments that are necessary, is misleading" **[L2016-007]**.
- *Guidance and targets.* A yearly outlook is published and revised (raised in July 2026), and a multi-year target of "$40
  of adjusted EPS" is stated; carried to Q5 **[L2002-041]**, **[L2019-006]**.
- *Stock pay* is expensed ($34.8M in 2025) and options are valued by Black-Scholes-Merton (Note 7); no tell.
- *Pensions*: frozen to new entrants except the executive plan; obligation $68.2M against assets $54.7M (Note 14); immaterial.

**VERDICT on the accounts: no STOP. WEIGHS AGAINST** on the habits (an adjusted figure featured, EBITDA featured, guidance and
a per-share target, recurring "non-comparable" items) **[L2016-006]**, **[M1998-086]**, **[M1994-018]**, carried to Q5 under
section A of the gaps case. The accounts themselves do not confuse **[M1995-063]** and raise no suspicion under the tells that
live in them: no prepaid or deferred account building, inventories and receivables in line with sales **[M1995-064]**, no
reserve moving, no restatement found; the one timing item (the tax credit) is disclosed in the next filing and is knowable.
The recast owner cash above feeds Q7.


## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The two yardsticks: how well they run the business, against "the hand they were dealt", and "how well that they treat their
owners" **[M1994-008]**.

**The people.** D. Christian Koch, Chair (since May 2020) and President and CEO (since January 2016), COO 2014-2015, earlier a
group president inside Carlisle (DEF 14A 2026, `0001193125-26-109193`). He owned 247,850 shares and held 58,015 options at
2026-02-28, about $81M of stock at the run's price. CFO Kevin P. Zdimal signs the filings. The board was fixed at six on
2026-09-10 after a director left on a change of employment, "not the result of any disagreement" (8-K `0000790051-26-000042`).
The outside directors' holdings in the proxy table are small and mostly share-equivalent units (for example 1,220 shares and
7,793 units; 3,664 shares and 9,976 units).

**The record against the hand dealt.** Over ten years the team sold the businesses with worse economics (FoodService, $758.0M,
2018, a $296.8M pre-tax gain; Brake & Friction, $247.7M in 2021 and $132.0M of earn-out and real estate in 2022, after a $141.5M
impairment in 2016; Fluid Technologies, $520M in 2023, an $82.5M loss on a business bought from Graco for $598.9M in 2015;
Interconnect Technologies, $2.025 billion in 2024, a $457.3M pre-tax gain) and kept the best one (10-Ks FY2015, FY2016, FY2018,
FY2022, FY2025). CCM's margin record under this management is the table at Q2. Against that, the CWT purchases (Q3) have earned
under 10% pre-tax on what was paid, and the 2025 10-K calls the year one in which "we continued to deliver on our commitment to
being superior capital allocators", a year in which the company borrowed $1 billion and bought in $1.3 billion of stock at an
average of about $355 a share (Q6).

**Integrity: the tells looked for.**
- *Habits carried from Q4* (an adjusted figure featured, EBITDA featured, yearly outlook, the "$40 of adjusted EPS" target):
  read with the rest of the record, as "things that they do in public in relation to their investors and the promises they
  make" **[M2004-067]**. Against the make-the-numbers reading: the 2025 annual incentive paid the CEO nothing because "the
  performance measures on which their respective 2025 annual incentive awards were based were not met" (DEF 14A 2026, CD&A),
  so the targets set for pay were missed and the miss was paid as a miss. No instance found, in the 10-Ks, the 2026 proxy and the Q2 2026 release read, of a target
  consistently met or beaten **[L2002-041]**; the 2026 outlook was raised in July on reported results, not on adjusted ones
  alone.
- *Reports that dance*: the key figures of the industry (volume, price, raw-material cost, re-roofing share) are discussed in
  every 10-K read; the warranty accounting is disclosed and conservative in direction (revenue deferred, costs expensed as
  incurred). The 2025 tax-credit item was described in the 10-K as "timing of tax expenses and payments" and named in the next
  10-Q; disclosed, if late in detail.
- *Credit taken*: the CCM margin step since 2022 is attributed in the filings to the Carlisle Operating System and "the Carlisle
  Experience"; Owens Corning's roofing margins rose in the same years (Q2), so part of the credit is the field's. The people
  wanted "don’t take credit for things that they didn’t do" **[M1998-167]**. A weighing, not a tell of dishonesty.
- *How they talk about mistakes* **[L2024-003]**: no instance found, in the 10-Ks read, of the CFT loss or the CWT returns
  described as a mistake; the CWT 2025 margin fall is put down to "higher absorption of fixed costs on lower volumes".
- *Auditor*: EY replaced by Deloitte in 2017 after a competitive selection, with "no disagreements" and no reportable events
  (8-K `0001628280-17-005697`). No restatement, investigation or material litigation other than legacy asbestos (Note 15) was
  found.

**VERDICT on integrity: IN.** No tell of dishonesty in the filings read; the habits carried from Q4 do not leave doubt when read
with a pay plan that paid nothing on a missed year **[M2004-067]**, **[M2013-088]**. **Ability WEIGHS FOR** on the portfolio
reshaping and the running of CCM, read against the hand dealt **[M1994-008]**, and **AGAINST** on capital allocation since
2021 (the CWT purchases and the buyback prices), which enters value as "what-will-they-do-with-the-money" **[L2010-002]** and
is weighed at Q6.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- *The retention test* **[R1995-009]**, **[M2011-072]**: over 2021-2025 the company did not retain: net income $4,165.6M against
  dividends of $760.7M and buybacks of $4,501.5M ($315.6M, $400.0M, $900.0M, $1,585.9M, $1,300.0M; cash-flow statements, 10-Ks
  FY2021 to FY2025), the excess funded by $2.9 billion of divestiture proceeds and $1.0 billion of new notes. Owner cash per
  diluted share rose from about $15.5 (2022: $817.0M over 52.6M) to about $19.8 (2025: $853.8M over 43.2M) while aggregate owner
  cash rose 4.5%; the stock's five-year total return was 116% against 55% for the S&P MidCap 400 (10-K FY2025, Item 5). The
  market leg passes; the test of what the money became turns on the buyback prices and the acquisitions.
- *Buybacks* **[L1999-023]**, **[L2016-002]**: the programme "has no expiration date", buys "from time to time", and "no
  maximum purchase price has been set" (10-K FY2025, Item 5). Prices paid: about $260 a share in 2023 ($908.3M for 3.5M shares),
  about $410 in 2024 ($1,599.5M for 3.9M), about $355 in 2025 ($1,312.0M for 3.7M; $311.67 to $330.11 in the fourth quarter),
  $345.42 to $350.47 in the second quarter of 2026 (10-Q, Part II, Item 2), with the full-year 2026 target raised to $1.2
  billion. **Read against Q7's range, recorded back from Q7:** the bottom of the range is $254.79 a share (all-equity basis;
  $282.28 equity-only). Every purchase since 2024 was made well above the bottom, and the 2023 purchases at about the bottom.
  Under the framework's test for a programme with no stated price, the purchases are read by what they paid, and what they paid
  weighs against **[M1996-013]**. The 2025 purchases were made partly with borrowed money ($987.8M of notes issued in August
  2025), above the bottom of the range.
  *(Corrected at Q7, same run, before the close; the sentences above are kept as written and committed. The figures $254.79
  and $282.28 came from a first pass of `val.py` that charged all capital spending and left the acquisitions out; Q7's
  construction under specifics (c) and (e) puts the bottom of the range at **$264.23** a share all-equity and $291.72
  equity-only, and the top at $359.99. Read against those: the 2023 purchases, at about $260, sat just below the bottom; the
  2024 purchases, at about $410, sat above the top; the 2025 and 2026 purchases, at $311.67 to about $355, sat between the
  bottom and the top. The reading does not change: weighs against.)*
- *Issuance and deals* **[L2014-012]**: no share issuance for deals; every acquisition named in Q3 was paid in cash. The one
  STOP of Part A, an all-stock deal by an undervalued acquirer **[L2009-019]**, does not arise. The deal record is mixed:
  divestitures at good prices (CFS, CIT), one at a loss (CFT), and CWT purchases earning under 10% pre-tax on their cost. No
  instance found, in the filings read, of a post-mortem of a deal against its projections **[L2014-013]**.
- *Dividends*: raised "annually for the past 49 years" (10-K FY2025, Item 5), a policy of increase rather than of what the
  dollar can earn kept; not a ratio policy **[M2000-051]**, but a commitment that runs whatever the retention test says.

**Part A WEIGHS AGAINST**: a fixed-sum buyback with no stated price, paid well above the bottom of the value range and partly
with borrowed money **[L2016-002]**, **[M1996-013]**, **[L1999-023]**, and acquisitions in the part that does not decide that
have earned little on their cost **[L2010-002]**; offset in part by divestitures that moved the company into its best business.

**Part B, the pay, the board and the owners** (DEF 14A 2026).
- CEO total compensation $11,359,438 for 2025; pay ratio 92:1. Annual incentive on consolidated sales, operating margin,
  average working capital to sales and earnings, adjusted to exclude acquisitions and some restructuring; paid zero to the CEO
  for 2025. Measures under the executives' reasonable control **[M2003-019]**, **[L1996-018]**.
- Long-term pay: performance shares earned on three-year total shareholder return relative to the S&P MidCap 400 (paid at
  153.95% of target for 2023-2025, the company ranking in the 63.49th percentile), and stock options with a ten-year term at a
  fixed price. Relative TSR rides the market and the multiple, the "lottery ticket" whose value is out of the holder's control
  **[L1996-018]**; the options carry no step-up for retained earnings **[M1997-043]**, a weaker objection here since the company
  retains little.
- The CEO also chairs the board **[L2014-026]**. Outside directors hold small positions, mostly units granted, not shares bought
  "with their savings" **[L2019-008]**. Ownership guidelines: the CEO ten times salary, with a retention requirement.
- The say-on-pay vote at the 2026 meeting: 30,209,063 for, 4,331,231 against (8-K `0000790051-26-000020`).

**Part B WEIGHS AGAINST, mildly**: a sound annual plan that paid nothing on a missed year, set beside long-term pay tied to
relative share price and a combined chair and chief executive **[L1996-018]**, **[L2014-026]**.


## Q7 — WHAT IS IT WORTH? STOP.
"how much do you get back, how sure are you of getting it, when do you get it?" **[M2009-004]**; value is "the discounted value
of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, net of what must go back in
**[M2014-068]**, at the long government rate **[L2000-021]**, held as a range **[L2000-024]**. All arithmetic is in
`val.py` (output saved as `val_output.txt` in the working folder).

**The inputs.**
- *Owner cash*, all-equity basis, continuing business, from Q4's recast: 2021 $261.9M, 2022 $817.0M, 2023 $937.6M, 2024
  $915.5M, 2025 $853.8M.
- *Rate*: 5.64%, the 30-year Treasury on 2026-10-06. Ten years at the growth credited, then zero nominal growth.
- *Tax*: owner cash is after the company's own cash taxes (effective rates 21.3% to 23.6%, 2021-2025), no conversion
  (Q7, Whose tax). No carryforward or credit that runs out inside ten years is relied on: the $52.0M valuation allowance covers
  carryforwards the company itself does not expect to use (10-K FY2025, Critical Accounting Estimates); the transferable energy
  credits are bought for cash and their cost is in operating cash, with the 2025 timing removed at Q4.
- *Net debt* at the latest filed date, 2026-06-30: total debt $2,889.9M less cash $665.3M = **$2,224.6M** (10-Q, Note 9 and
  balance sheet); no securities; operating leases ($135.6M at 2025 year-end) left out, said so; no subsequent event stated in
  the 10-Q. Market value $12,936M; enterprise value at the price **$15,161M**.

**The six specifics, applied.**
- *(a) Cycles.* The literal window is 2021-2025. Its first year is aberrational on the filer's own description: a working-capital
  use of $275.2M that the filer ties to "an increase in receivables and inventory from higher sales" and "rising raw material
  costs" (10-K FY2021, MD&A), in the year Henry was bought (four months owned). The base for the range is therefore the
  average of 2022-2025, **$881.0M**, with the literal window's **$757.1M** shown beside **[L2005-003]**. *CONVENTION of this
  run:* the framework asks for the last full cycle of owner cash, peak to peak or trough to trough; the continuing business took
  its present shape between 2021 and 2024 and no earlier owner-cash series for it can be built from the filings, so the four
  years after the aberrational year stand in for the cycle. Rationale: the alternative is a base that includes a year the filer
  calls distorted.
- *(b) Decline.* The total growth shown is positive (below), so no negative rate is carried.
- *(c) Acquisitions, the default pair.* Cash paid for businesses, 2022-2025: $24.7M, $36.1M, $676.9M, $109.6M, a mean of
  **$211.8M** a year, deducted; the total growth of aggregate owner cash over the base, end year to end year (2022 to 2025),
  **1.48%** a year, credited. The organic pair is shown beside: acquisitions left out, organic growth as the filer reports it
  (weighted from the segments' filed rates, **3.53%** a year 2021-2025). *CONVENTION of this run:* the proceeds of businesses
  sold (CFT, CIT) are not netted against the purchases, because the sold businesses' cash is excluded from the base and their
  proceeds already sit in today's net debt and share count; netting them would count them twice. No deal closed after the
  window and before the price date (the 10-Q shows no acquisition in the first half of 2026).
- *(d) Working capital.* Inside operating cash, so counted; the 2021 draw is handled by (a), the 2025 tax-credit timing by Q4.
- *(e) Growth spending.* The maintenance guess is depreciation, $74.6M (2025) **[M1998-127]**, against capital spending of
  $125.4M a year (2022-2025 mean); the balance, **$50.8M**, is growth and cost-reduction spending. The central case is owner
  cash after maintenance only, with the growth spending and the acquisitions charged against the growth they buy for ten
  years and stopped when growth stops. Result: the growth bought is worth slightly less than its cost (below), so the
  no-growth, maintenance-only case is the top of the range and the growth case the bottom; "growth can destroy value"
  **[L2000-023]**, and that inversion is the finding.
- *(f) The cap.* 1.48% (or 3.53% in the organic pair) for ten years, then zero; no rate near the discount rate **[M1997-095]**,
  nothing traces to an absurdity **[M1999-067]**.
- *CWT* (the part that does not decide, Q2) is carried at no growth throughout, at its 12.4% share of 2022-2025 segment
  operating income.
- *The change for the better since 2022, not credited at the bottom* (Q2, section C): the bottom of the range takes CCM's
  margin at its pre-change level on the current segment basis, 22.08% (2020-2021 recast), instead of the 28.63% earned
  2022-2025, which removes **$184.8M** a year of after-tax owner cash (CCM's mean 2022-2025 revenue × 6.55 points × (1 − the
  mean effective tax rate)). *CONVENTION of this run:* the framework says the change is credited only on a full cycle and gives
  no arithmetic for an uncredited change; taking the margin as it stood on the same basis before the change is the least
  invented form. Rationale: without it the range would rest entirely on years the castle verdict declined to credit. On the
  old segment basis (the 2007-2016 mean margin of 14.65%) the same case would be $183.95 a share, shown as a sensitivity, not
  used, since that basis included lines now in CWT.

**The cases** (all-equity, per share, after net debt; expected return at the price is the rate at which the case's cash stream
is worth the enterprise value at the price):

| case | year-1 cash $M | value per share | expected return at $325.74 |
|---|---|---|---|
| credited, no growth, maintenance only (no purchases) | 931.8 | **$359.99** (top) | 6.15% |
| credited, total growth 1.48%, purchases and growth spending deducted | 681.2 | $355.71 | 6.04% |
| uncredited, no growth, maintenance only | 747.0 | $277.48 | 4.93% |
| uncredited, total growth 1.48%, purchases and growth spending deducted | 494.0 | **$264.23** (bottom) | 4.83% |
| literal window 2021-2025, no growth, maintenance only (beside) | 808.0 | $304.71 | 5.33% |
| organic pair, credited, 3.53% growth, growth spending charged (beside) | 908.2 | $461.55 | 7.50% |

**Value range:** **$264.23 to $359.99 a share** (all-equity basis, central), against **$325.74**; width 1.36 to one; midpoint
$312.11. Equity-only, beside: $291.72 to $387.47 (owner cash after the Q2 2026 run-rate of net interest, $63.9M after tax,
against market value alone). The literal window, no growth, is $304.71. Were the change since 2022 credited in full, the
default pair would run $355.71 to $359.99; the organic pair's credited top is $461.55.

**Closes.** The range is narrower than about three to one, so it is not TOO HARD **[L2000-025]**, **[M2007-022]**. The price sits
inside it, above its midpoint, and "it should scream at you" **[M2009-005]**: it does not, and a pencil is needed to tell one
case from another **[M1996-084]**. By the floor convention: the expected return at the price is 5.45% on the midpoint stream
(all-equity), 6.15% on the most generous default case, and 7.50% on the organic pair's credited top, against the floor of about
ten percent **[M2003-149]**, **[L2002-020]**, as the speakers qualified it for their times **[M1994-004]**, **[M2003-151]**,
**[M2016-078]**. Every case is below it, on both bases. The price is not "a reasonable price in relation to the bottom boundary
of our estimate" **[L2013-012]**: it is 23% above that boundary.

**Fair price (a reporting figure, never a verdict; Part VII):** **$143.72** a share, the price at which the midpoint of the range
earns the floor of ten percent: the year-by-year average of the bottom and top cash streams, discounted at 10%, gives an
enterprise value of $7,932M, less net debt of $2,224.6M, over 39.714M shares. All-equity basis, after the company's own tax;
this is the central figure. Equity-only beside it: **$183.65**. Were the change since 2022 credited in full, the all-equity fair
price would be $169.14. No cheap price is reported.

**VERDICT: OUT.** Valued, with a range narrow enough to use, the price sits inside it and does not clear the floor in any case
shown; "there’s just a point at which we drop out of the game" **[M2003-149]**, and the case is a close call that needs a
pencil, which the rows send away **[M2009-005]**, **[M1996-084]**. The file closes here; Q8 to Q12 are not reached.


## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (closed at Q7). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (closed at Q7). Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (closed at Q7).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (closed at Q7). Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT**, decided at **Q7** (valued: range $264.23 to $359.99 a share, all-equity, against a price of $325.74; the price sits
inside the range and no case shown clears the floor of about ten percent). Q1 IN, Q2 IN (on the old cycle; the post-2022
margin not credited), Q3 weighs for, Q4 no STOP and weighs against on the habits, Q5 integrity IN with ability weighing both
ways, Q6 weighs against. Reporting figures: value range $264.23 to $359.99 all-equity ($291.72 to $387.47 equity-only), the
literal window's no-growth case $304.71 beside; fair price **$143.72** all-equity, **$183.65** equity-only. Q11 belongs to the
holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on questions not reached, each with its source, written down as found **[M1997-127]**; no
verdict; the box unchanged.)*
- **Q8, the bond.** The 30-year Treasury yielded 5.64% on 2026-10-06 (Treasury par yield curve). The expected return at the price
  on Q7's cases ran from 4.83% to 6.15% (default pair) and 7.50% (organic pair, credited top); on the midpoint stream, 5.45%
  all-equity and 5.86% equity-only (`val_output.txt`).
- **Q9, debt and exposures.** Senior notes: $600M 3.75% due 2027-12-01, $750M 2.75% due 2030-03-01, $550M 2.20% due
  2032-03-01, $500M 5.25% due 2035-09-15, $500M 5.55% due 2040-09-15; all fixed-rate, unsecured, with a 101% repurchase offer
  on a change-of-control triggering event; a $1.0 billion revolver to 2029-04-03, undrawn at 2026-06-30; covenants on leverage
  and interest coverage, in compliance (10-K FY2025, Note 13; 10-Q Q2 2026, Note 9). Pre-tax earnings over interest expense,
  2025: ($948.8M + $78.5M) / $78.5M = 13.1 times. Cash paid for interest $56.2M (2025). Letters of credit $48.8M. Legacy
  asbestos claims from the discontinued Motion Control friction products (late 1940s to mid 1980s) and from roofing products of
  Henry Company, acquired 2021; the accrual is called "not material", with insurance receivables recorded where recovery is
  probable (10-K FY2025, Note 15). Two distributors were a third of 2025 revenue (Note 6). Extended warranties of five to 40
  years on installed roofing systems, $372.3M of deferred revenue, no loss reserve recorded (Notes 1 and 6). Product-liability
  coverage "may not be adequate to cover all claims" (Item 1A). Operating-lease liabilities $135.6M.
- **Q12, the business named.** Roofing membranes, insulation and building-envelope products; no business of the kinds the rows
  name. The asbestos history above belongs to a discontinued line and to an acquired roofing line.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      **Departure declared:** Q3 and Q4 were appended and committed together in one commit (`dda8c818`), not one commit each;
      Step 0 to Q1 were committed together, as the brief's first commit. Every other question has its own commit.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (the lock file in `Screens/_daily/` was present, its line naming an interactive batch); the run is to be folded
      into the register by the dispatcher (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule); what was seen by
      accident (commit subjects of four other companies' runs, an untracked run-file name, the memory index lines, the lock
      line) is declared under contamination at the top and was not used.
- [x] Every v5 id resolves (`check_ids.py` in the working folder: no E-ids; every M/L/R id in `principle_ledger_v5.csv`; every
      quoted fragment set directly before an id found in that row); every filing fact has its accession; no number without a
      row, a filing or a labelled CONVENTION.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash of the continuing business
      less stock pay and capital spending, from the filed statements; the sovereign from the issuing authority; the price is
      an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q2 test 3, Q5); facts for questions
      not reached are under AFTER THE STOP; no integrity flag is needed, since Q5 was answered.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its three-year owner-earnings means were not used,
      because they include discontinued businesses.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded below the self-audit).
- Conventions of this run, each confessed where used: the 2025 tax-credit timing adjustment (Q4); the four-year base standing in
  for a full cycle (Q7 a); divestiture proceeds not netted (Q7 c); the uncredited bottom at the pre-change margin (Q7). The
  reporting figures follow the brief's stated definitions; the midpoint stream for the fair price is the year-by-year average
  of the bottom and top streams (my reading of "the midpoint of the range", stated in Q7).
- Corrected within the run before the close: Q6's buyback reading used a first-pass range bottom ($254.79); the correction is
  written at Q6 with the first text kept.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2 section C and Q7 do not meet.** The convention credits a change for the better only on a full cycle and sends the file
to TOO HARD (WORK) "on that question"; here the castle stood without the change (the old cycle's returns were excellent), so Q2
closed IN, but the value at Q7 depends on whether the post-2022 margin lasts, and the framework gives no arithmetic for an
uncredited change inside Q7. I took the bottom of the range at the pre-change margin on the same segment basis and confessed it;
another analyst could have closed Q2 TOO HARD (WORK) on the same facts, or valued on the credited base alone. The box is OUT
on every reading I computed, so the choice did not decide this file, but it could decide another. (2) **Q7 (a) asks for the last
full cycle of owner cash**, which does not exist for a company that sold three of its four businesses inside the window; the
four years after the aberrational first year stood in. (3) **Q7 (c) says acquisitions are taken "net of businesses sold"**,
which double-counts when the base is continuing operations and the proceeds already sit in net debt and the share count; I did
not net them. (4) **(c) and (e) together** do not say whether purchases stop when growth stops after year ten; I stopped them,
the same treatment (e) gives growth capital spending. (5) **The fair price's "midpoint of the range"** is a per-share figure, but
the floor is earned by a cash stream; the text does not say which stream is the midpoint. I used the year-by-year average of
the bottom and top streams. (6) **On what the floor is earned**: its rationale is that debt magnifies a discount per share; here
the company's debt costs 2.20% to 5.55% against a 5.64% discount rate, so the equity-only range ($291.72 to $387.47) is higher
than the all-equity range, the reverse of the magnification the rationale describes. (7) **The template's ten-year balance-sheet
table** comes from first-filed XBRL vintages that include businesses later sold, so the decade reads two companies; the run says
so beside the table. (8) **The brief** (this run's slots) lists Beacon (BECN) among the competitors; Beacon is a distributor and,
with QXO, Carlisle's largest customer (16.7% of 2025 revenue), not a rival; it is shown in the competitor row as a customer. The
brief also calls Amrize "Holcim's North American roofing business"; Amrize is all of Holcim's North American business (cement,
aggregates and the Building Envelope segment), and only the Building Envelope segment competes. The canonical brief's reporting
paragraph has a garbled clause ("with a built by Q7's six specifics").

**Acceptance test, before the final commit:** `python tools/check_framework.py` PASS on 2026-10-07 (run files: phantom ids in
0 files; pointers: 0 missing; v5 scope: 0 outside); the run's own check (`check_ids.py`): PASS, no E-ids, every id in the v5
ledger, every quoted fragment beside an id found in its row.
