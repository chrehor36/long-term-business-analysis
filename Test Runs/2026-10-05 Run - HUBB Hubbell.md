# Company Run — Hubbell Incorporated (NYSE: HUBB) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The run was dispatched blind: `PORTFOLIO.md`, holding
reviews, the session-state file, the register and the prepped reading list were not opened, and no attempt was made to
learn whether anyone holds or wants this name.

**CONTAMINATION, declared.** (1) Commit subjects visible at the start of the session name five other 2026-10-05 runs
(PRIM, MTZ, DY, LMB, WCC) and their boxes (all OUT at Q2). WCC is an electrical distributor and so a Hubbell customer;
its run file was not opened and nothing about Hubbell was taken from it. (2) A directory listing of `Test Runs/` showed
the names of other 2026-10-05 files (names only; none opened; none is about Hubbell). (3) `git status` showed that an
earlier research folder of another company holds a Hubbell facts file; it was not opened, and Hubbell's and every
competitor's data were fetched fresh from EDGAR into this run's folder. (4) The auto-memory index loaded with the session
carries an unrelated count of gate-clearers and says nothing about this name. The analyst knows Hubbell in general terms
from training (a long-listed electrical manufacturer); every fact below is from the filings cited.

Working folder: `Test Runs/_research 2026-10-05 HUBB/` (filings as `.htm` and `.txt`; `fetch.py`, `h2t.py`, `series.py`,
`peers.py`, `value.py`; the competitors' company facts in its `peers` subfolder).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $482.23 (close 2026-10-05; Yahoo chart via `tools/sources.py`, an aggregator, live quote only, flagged per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, Common Stock par $0.01, **52,832,571** (Form 10-Q for
  the quarter to 2026-06-30, filed 2026-07-29, accession `0001628280-26-050405`; `python Screens/cover_shares.py HUBB`).
  The two classes were collapsed into one on 2015-12-23 (10-K FY2016, `0001628280-17-001423`), so there is no class to add.
- **Market cap:** 52.83M x $482.23 = **$25,477M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, dated
  2026-10-02 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-12, `0001628280-26-007500`): Item 1, Item 1A, Item 5,
  Item 7 in full, the statements, Notes 1 and 2; 10-Q Q2 2026 (`0001628280-26-050405`): balance sheet, cash flow, debt
  note, supplier finance, issuer purchases; 10-Q Q1 2026 (`0001628280-26-029110`), 10-Q Q1 2025 (`0001628280-25-021677`)
  and 10-Q Q2 2025 (`0001628280-25-036564`): issuer purchases; proxy filed 2026-03-23 (`0001308179-26-000121`): pay
  design, ownership, board; 8-K of 2026-05-04 with Exhibit 99.1 (`0001193125-26-204099`, the NSI Industries purchase);
  8-K of 2026-07-28 with Exhibit 99.1 (`0001628280-26-049934`, Q2 2026 results); for the record: 10-K FY2023
  (`0001628280-24-003792`), FY2022 (`0001628280-23-002875`, cash flows 2020 to 2022), FY2021 (`0001628280-22-002255`,
  the price and cost story of 2021), FY2018 (`0001628280-19-001446`), FY2016 (`0001628280-17-001423`) and FY2009
  (`0000950123-10-014554`, the 2008 and 2009 record).
- **One figure cross-checked against the filed statement:** operating cash flow FY2025 **$1,029.8M** and capital
  expenditures **$155.1M** in the filed Consolidated Statement of Cash Flows (10-K FY2025, `0001628280-26-007500`)
  against `tools/run.py`'s 1,030 and 155: they agree. Also FY2009 operating cash flow 397.7 and capex 29.4 in the filed
  FY2009 statement (`0000950123-10-014554`) against the XBRL series: they agree.
- **`python tools/run.py HUBB`, arithmetic lines only.** The defects named in the dispatch were checked: the share count
  (52.8M as of 2026-04-27) agrees with the cover; stock pay is not zero (26.5, 30.6, 33.0 for 2023 to 2025, as filed);
  the OCF figure is the filed operating cash flow (securities purchases sit in investing, not in it); the "OE lo" column
  is the depreciation-and-amortization variant and "OE hi" the capex variant, which order that way in 2023 to 2025 only
  because D&A (carrying $77M to $127M a year of acquired-intangible amortization) exceeds capex. Nothing the tool prints
  as a rule, id, floor or verdict is used (Part VII). Owner cash below is recomputed from the filed statements.

**Owner cash after every real cost** = operating cash flow (continuing operations) less stock pay less all capital
expenditures (USD millions; stock pay is added back inside operating cash flow, so it is deducted again here as the real
cost it is; interest, taxes and pension contributions are already paid inside operating cash flow):

| FY | OCF | stock pay | capex | owner cash | D&A variant (OCF less stock pay less D&A) | source |
|---|---|---|---|---|---|---|
| 2021 | 513.7 | 17.5 | 90.2 | **406.0** | 347.1 | 10-K FY2022 `0001628280-23-002875` |
| 2022 | 636.2 | 24.5 | 129.3 | **482.4** | 463.2 | same |
| 2023 | 880.8 | 26.5 | 165.7 | **688.6** | 704.6 | 10-K FY2025 `0001628280-26-007500` |
| 2024 | 991.2 | 30.6 | 180.4 | **780.2** | 748.5 | same |
| 2025 | 1,029.8 | 33.0 | 155.1 | **841.7** | 790.7 | same |
| **5-yr mean** | | | | **639.8** | 610.8 | |

The long record (XBRL transcription, 2008 and 2009 cross-checked to the FY2009 filing above; 2008 to 2020 include the
lighting businesses since sold): owner cash 257 (2008), 358 (2009, working capital released in the recession), 208,
265, 284, 309, 315 (2014), 245 (2015), 322 (2016), 277 (2017), 397 (2018), 490 (2019), 543 (2020). Owner cash yield at
the price: 639.8 / 25,477 = **2.5%** after corporate tax.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be happy owning Hubbell "if the market closed for five years"
**[M1997-109]**, so the run asks what will happen to the business and not to the quotation. The margin of safety bears
hardest here. The price has tripled in five years (the 10-K's own performance graph: $100 at 2020-12-31 to $307.70 at
2025-12-31, `0001628280-26-007500`), and a decision that needs pencil and paper is "too close to think about"
**[M1996-084]**. No macro forecast enters: "macro conclusions are — just never enter into the discussion" **[M2000-094]**;
the "megatrends" of grid modernization, load growth and data centres that the company's releases lead with are read only
as evidence about Hubbell's own cash. Who is paid to tell you: the NSI price was described to owners as a multiple of
EBITDA, with an investment bank as adviser and a private-equity seller across the table; each is weighed where it bears
(Q4, Q6). The analyst's habit kept: look for "what you’re missing" **[M2025-013]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. The 10-K says Hubbell "experiences substantial competition in all categories of its business", that "some of its
   competitors are larger companies with substantial financial and other resources", and that "product price, service
   levels and other factors can affect Hubbell's ability to compete" (Item 1, `0001628280-26-007500`).
2. Its stated strategy: "Our competitive strategy is to design and manufacture high quality products at the lowest
   possible cost", and "Competitive pricing pressures may not allow us to offset some or all of our increased costs
   through pricing actions" (Item 1A, same).
3. In 2021 "material cost inflation that exceeded favorable price realization" cut the consolidated gross margin from
   29.5% to 27.5%, and the Utility segment's operating margin fell from 14.7% to 12.2% (10-K FY2021, `0001628280-22-002255`).
4. "our top ten customers account for approximately 42% of our Net sales" (Item 1, FY2025).
5. The operating margin of 19.3% to 20.7% in 2023 to 2025 is a step up from 12.4% to 15.9% in every year 2008 to 2022,
   in the same years in which every electrical peer's margins also rose (competitor row, Q2).
6. The LIFO-to-FIFO switch made in Q2 2025 added $62.7M to 2025 operating income and $0.89 to diluted EPS; reported EPS
   growth of 14.9% would have been about 8.9% under LIFO (Note 1, FY2025).
7. Owner cash was about flat from 2008 (257) to 2017 (277) while about $1.5B went into acquisitions over those years.
8. Grid Automation (meters and AMI, mostly the Aclara business bought in 2018) fell from $1,069.4M to $924.1M of sales in
   2025 (Note 2, FY2025).
9. After the NSI purchase, goodwill and intangibles are $7,544M against shareholders' equity of $3,912M and debt of
   $5,373M (10-Q Q2 2026, `0001628280-26-050405`).
10. Shares were bought back in February to May 2026 at $483 to $514 a share with no stated price limit, in the quarters
    in which $2.8B was borrowed for NSI.

## THE STANDING RULE
A marketable stake bought for cash and held unlevered, with no instrument that can demand cash of the buyer, does not
put at risk "what we have and need for what we don’t have and don’t need" **[M2012-081]**; "borrowed money has no place
in the investor's tool kit" **[L2014-005]**, so none is assumed. The rule is satisfied by the buyer's conduct, whatever
the questions below conclude. Nothing in the target can call on the buyer.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (Item 1 and Note 2, FY2025, `0001628280-26-007500`): two segments. Utility Solutions, 63% of
  2025 sales ($3,672.3M): Grid Infrastructure ($2,748.2M: arresters, insulators, connectors, anchors, bushings,
  enclosures, cutouts, switches; brands Chance, Anderson, Ohio Brass, Fargo, Quazite, DMC Power and others) and Grid
  Automation ($924.1M: smart meters, AMI communications, protection and controls; Aclara, Beckwith, Systems Control).
  Electrical Solutions, 37% ($2,172.3M): wiring devices, rough-in boxes and fittings, connectors and grounding (Burndy),
  harsh-and-hazardous products, sold through electrical distributors to contractors and industrial users. The lighting
  businesses were sold (commercial and industrial lighting in 2022, $332.8M of disposal proceeds in the FY2022 cash flow
  statement; residential lighting, $187.1M of 2023 sales, in Q1 2024). Utility products are "sold into these markets primarily through distributors, or directly to utilities."
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**; the chemistry or metallurgy need not be known if "I understand the
  economic dynamics of the industry" **[M2011-014]**. The key variables **[M1998-044]**: (a) utility spending on
  transmission and distribution hardware, which is replacement-driven and slow-changing; (b) electrical construction and
  industrial activity; (c) the price Hubbell can hold against metal costs (materials are about half of cost of goods sold,
  Item 7 FY2025); (d) share against larger rivals. Of these, (a) and (b) are cyclical but their direction over ten years
  is foreseeable: a utility will still buy anchors, arresters and connectors, and an electrician boxes, fittings and
  devices. (c) and (d) are the castle question, owned by Q2.
- **The technology part.** Grid Automation is a technology business ("if something comes in where there’s a
  technological component that’s of significance" it "won’t make it through the filter" **[M1998-008]**). It is 16% of
  sales and, on the FY2018 filing, carried "a relatively lower gross margin" than the rest (10-K FY2018,
  `0001628280-19-001446`). The doubt rule is applied: "if you have doubts about something being into your circle of
  competence, it isn’t" **[M2002-092]**. Read by its parts, the part I cannot foresee is about a sixth of sales and less
  of profit; the five-sixths that make the earnings are hardware whose ten-year use is not in doubt. The doubt is about a
  minority part, not about where the whole will be.
- Would the insiders write the forecast down **[M2000-105]**? For connectors, anchors and wiring devices, yes: the
  products have been sold under the same brands for decades (Hubbell founded 1888; Chance, Burndy, Ohio Brass).
- **VERDICT: IN.** The economics of the hardware that makes the earnings can be foreseen ten years out **[M2012-065]**,
  **[M2011-014]**; the Grid Automation part is noted as the piece outside the perimeter and is not large enough to
  carry the whole outside it **[M2002-092]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**, starting from the attacker, because "most moats aren’t worth a damn"
**[M1995-038]**.

**The record the castle must explain** (first-filed XBRL 10-K facts, `peers.py`; operating income over revenue, and
operating income over total assets less goodwill and intangibles):

| | 2008 | 2009 | 2012 | 2015 | 2016 | 2018 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HUBB gross margin % | 29.7 | 30.8 | 33.2 | 32.2 | 31.4 | 29.0 | 28.9 | 27.5 | 29.7 | 35.1 | 33.8 | 35.3 |
| HUBB operating margin % | 12.8 | 12.5 | 15.5 | 14.0 | 13.6 | 12.4 | 12.7 | 12.7 | 14.3 | 19.3 | 19.4 | 20.7 |
| HUBB op. income / tangible assets % | n/a | 17.6 | 24.8 | 24.9 | 22.7 | 24.6 | 22.7 | 19.5 | 25.7 | 32.6 | 35.2 | 32.0 |

Segment margins from the filings: Power (now Utility) 15.9% in 2008 and **18.6% in 2009**, when "operating margin
improved 270 basis points" on "commodity cost decreases, productivity improvements and price increases" (10-K FY2009,
`0000950123-10-014554`); 20.1% in 2016 (10-K FY2016, `0001628280-17-001423`); 19.8% in 2017 and 13.0% in 2018 after the
Aclara purchase (10-K FY2018, `0001628280-19-001446`); 14.7% in 2020 and 12.2% in 2021 (10-K FY2021); 21.4%, 20.3%,
21.5% in 2023 to 2025 (10-K FY2025). Electrical, with lighting: 9.9% (2009), 10.9% (2016), 12.1% (2018), 13.3% (2021);
without lighting: 15.6% (2023), 17.8% (2024), 19.3% (2025).

**The competitor row** (each competitor's own 10-K facts from EDGAR company facts, first-filed vintage, latest 10-K
accession named; operating margin % unless stated; "tangible" = operating income over total assets less goodwill and
intangibles):

| Company (latest 10-K) | What it competes in | Operating margin through the record | Gross margin | Op. income / tangible assets |
|---|---|---|---|---|
| Hubbell | all below | 12.4 to 15.9 (2008 to 2022); 19.3 to 20.7 (2023 to 2025) | 27.5 to 35.3 | 17.6 to 35.2 |
| Preformed Line Products PLPC (`0000080035-26-000007`) | utility line hardware, connectors | 3.5 to 12.6 (2009 to 2025); 8.2 in 2025 | 29.2 to 35.1 | 4.2 to 14.9 |
| Itron ITRI (`0000780571-26-000033`) | meters, AMI | minus 18.9 to 13.2 (2008 to 2025); negative in 6 of 18 years | 27.7 to 37.7 | minus 38.7 to 14.8 |
| nVent NVT (`0001628280-26-008608`) | enclosures, connections, fastening | 14.0 to 18.0 except 1.9 in 2020 (2016 to 2025) | 37.5 to 41.1 | 3.3 to 28.3 |
| Eaton ETN (`0001551182-26-000007`) | electrical products and systems | 12.4 to 17.2 where tagged (2010 to 2019) | 29.8 (2010) to 38.2 (2024) | 15.1 to 28.1 where tagged |
| Atkore ATKR (`0001628280-25-054049`) | conduit, fittings, cable | minus 1.1 (FY2014), 31.5 (FY2022), 0.8 (FY2025) | 13.3 to 41.9 | minus 1.8 to 64.0 |
| Acuity AYI (`0001144215-25-000082`) | lighting (Hubbell's exited line) | 9.3 to 14.8 (FY2009 to FY2025) | 38.3 to 47.8 | 19.6 to 33.5 |

**The castle tests, each with its filing fact.**
1. **The key factors and how permanent** **[M1995-038]**. What the filings give is a reputation and a specification:
   "Hubbell considers product performance, reliability, quality and technological innovation to be important factors
   relevant to all areas of its business and considers its reputation as a manufacturer of quality products to be an
   important factor in its business" (Item 1, FY2025). The products that carry the margin are small-ticket, failure-costly
   parts (an arrester or an anchor on a utility line, a connector in a substation), bought by brand from a distributor's
   shelf or a utility's own list. That reading of how they are bought is mine; the filings do not describe approved-vendor
   lists, and I found no sentence in them that does.
2. **Would it stand without the lord?** The record runs through a change of chief executive in 2020 (Item 1, FY2025) and
   two recessions with the operating margin never below 12.4% in seventeen years. It does not depend on one person. "If you have a big enough
   moat, you don’t need as much management" **[M1999-106]** is not claimed; the record is only that ordinary management
   kept it.
3. **The money test** **[M2011-015]**. The attacker with money exists and is named by the company: "some of its
   competitors are larger companies with substantial financial and other resources" (Item 1). Eaton's revenue is $27.4B
   against Hubbell's $5.8B. Yet in utility hardware the listed rival with the same customers, Preformed Line Products,
   has earned an operating margin of 3.5% to 12.6% in every year from 2009 to 2025 against Hubbell's 12.4% to 20.7%, and
   between a sixth and two-thirds of Hubbell's operating income on tangible assets in every year. A rival in the same aisle that cannot reach
   Hubbell's returns in seventeen years is evidence that money alone has not crossed this moat. It is not proof that a
   larger rival could not; no filing read records a rival trying.
4. **Pricing power and the agony before a rise** **[M2005-020]**. Against: there was agony. In 2018 "many of our
   businesses took pricing actions to mitigate the impact of material cost increases" only "During the second half of 2018"
   (10-K FY2018); in 2021 cost ran ahead of price for the whole year (10-K FY2021); the company writes that "if raw material
   and component costs decline, the Company may not be able to maintain current pricing levels" (Item 1A, FY2021 and
   FY2025). For: the price was held when costs fell (Power margin up 270 basis points in 2009), and the 2021 lag was
   recovered and more by 2023. That is the pattern the rows describe for the strong position: "over time the businesses
   with strong competitive positions manage to pass through increases in raw material costs" with "temporary situations
   where, sometimes, the costs are increasing faster" **[M2005-017]**. It is pass-through, not pricing power of the
   "incredible" kind **[M2010-092]**.
5. **Unit volume and share of mind.** Not measurable from the filings: Hubbell does not report units. Organic volume was
   down in 2024 (consolidated "low single digit percentage decrease in unit volume") and mixed in 2025 (Item 7, FY2025).
   No finding.
6. **The low-cost position.** Hubbell claims the strategy (Item 1A, FY2025), not the result. The rows ask the cost
   against the competitor, not in absolute terms **[M2001-013]**; the only comparable figure is margin, and on margin
   Hubbell beats PLPC every year. Whether that is lower cost or a higher price, the filings cannot separate.
7. **The brand in the customer's mind** **[M2015-038]**. Hubbell, Chance, Burndy, Raco, Bell: brands asked for by
   electricians and utility engineers is the claim, and it is the claim the 42% customer concentration tests: the top ten
   customers are mostly distributors, and "the value of having the brand moves over to the retailer" where the customer
   trusts the seller as much as the brand **[M2001-090]**. The record of margins held above PLPC's while selling through the
   same distributors is the evidence that the brand has not moved to the distributor. The filings give no direct measure.
8. **Over the low bid?** **[M2017-009]**. The product mix is closer to the parachute than to the airline seat: a
   lineman's anchor or a substation connector that fails costs far more than its price, and "people don’t simply just take
   the low bid" for such parts is the rows' description of the case **[M2016-006]**. That is a reading by analogy; the
   filing says only that price is one factor among performance, reliability and quality (Item 1).
9. **Ask the competitors** **[M1999-130]**. Not on the public record; not answered.
10. **Widening or narrowing?** **[M1999-108]**. Widening in utility hardware on the margins (20% in 2016 to 2017, 24% adjusted
    in 2025); narrowed and then abandoned in lighting, where the 2016 10-K already expected continued pricing challenges and
    Hubbell later sold out; narrowing in Grid Automation in 2025.
11. **What could destroy or reduce it** **[M2000-014]**: (a) an industry-wide reversal of the 2023 to 2025 pricing as
   utility lead times shorten; (b) a large rival bundling; (c) distributors consolidating further. (a) bears on the level of
   earnings, which Q7 carries; (b) and (c) have been present for the whole seventeen-year record without breaking it.

**Weighing the castle.** Shown open on the evidence? No: a business whose price a rival sets **[M2012-109]** does not earn
a higher return than its nearest listed rival in every one of seventeen years and two recessions, often by half again or
more, and a commodity
producer's record looks like Atkore's (31.5% to 0.8% in three years), not Hubbell's. Shown to be a great castle? Also
no: the company's own words are those of a business that "does battle daily" **[L1993-021]**; pricing passes cost through
with a lag rather than leading it **[M2005-017]**; and the jump of 2023 to 2025 is shared by every peer, so it is not
evidence of a widening moat **[M2000-075]**, and it must be read as possibly "a cyclical peak in earnings" **[L1994-009]**.
What I can judge is a durable, moderate castle in utility hardware and electrical connectors and devices, whose width is
shown by the 2008 to 2022 margins (12% to 16%) and whose current height is not yet shown to last. The future of the castle
can be judged; its present level of profit cannot be assumed. That second point goes to Q7, not here.

- **VERDICT: IN**, narrowly: the castle is shown standing on seventeen years of record against the nearest rival
  **[M1995-038]**, **[M2005-017]**, not shown to be filling in **[M2011-015]**; it is a moderate castle, and the
  2023 to 2025 profit level is treated as unproven **[L1994-009]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital the business needs** **[M2010-090]**, **[M2011-060]** ("look at return on tangible assets").
  Net tangible operating capital (receivables + inventory + net PP&E less payables, filed balance sheets) and operating
  income (GAAP): 2016, 530 + 532 + 440 − 292 = 1,210 against 490 (**40%** pre-tax); 2021, 675 + 662 + 460 − 533 = 1,264
  against 532 (**42%**); 2025, 857 + 1,084 + 841 − 571 = 2,211 against 1,209 (**55%**). Even in 2009, operating income was
  17.6% of all tangible assets including cash. The business itself is capital-light: net PP&E is 14% of sales (2025), and
  capex 2.7% of sales.
- **To stand still and to grow** **[L1999-024]**, **[M2000-144]**. Depreciation proper in 2025 was about $96.5M (D&A
  206.1 less acquired-intangible amortization 109.6, Item 7 FY2025); capex was $155.1M, spent, by Item 7, on footprint optimization, automation and
  productivity. The rows treat depreciation as the cost of standing still **[L2000-035]**, so my
  guess at maintenance is about the depreciation charge, $95M to $100M; the rest is optional. Owner cash deducts all of it (CONVENTION, Q7 specifics).
- **What the added capital has earned** **[M2001-019]**. Here the record is against. Owner cash 2008 was 257 and 2017 was
  277 (2016: 322): about flat over nine years in which Hubbell spent about $1.5B on acquisitions (XBRL: 267, 356, 0, 30, 91,
  97, 184, 163, 173, 184) and retained most of its earnings. From 2017 to 2025 owner cash rose by about 565 while about $3.8B
  more went into acquisitions (Aclara $1,118M in 2018, Systems Control and others $1,212M in 2023, DMC Power and others
  $958M in 2025) on top of retained earnings, and in the same years the industry's pricing lifted margins on the old
  business too. On all capital including goodwill, after-tax operating income was about 16% of capital employed in 2016 and
  about 17% in 2025 (operating income x (1 − tax rate) over equity + debt − cash); so the added capital has earned about the
  average, at a margin peak. At the 2008 to 2022 margin of about 14%, the return on all capital would be about 11% and on
  the capital added since 2016 about 8%. Rising earnings from added capital are not a rising return: "we’re not earning a
  higher rate of return on capital than we were when we started" **[M2023-081]**.
- **Growth arithmetic.** The business's own growth needs little capital (the See's half of **[M2001-019]**); the growth the
  company buys needs a great deal. NSI (2026, $3.0B, "~15.5x anticipated 2026 EBITDA") continues the pattern. "Most of the
  great businesses generate lots of money. They do not generate lots of opportunities to earn high returns on incremental
  capital" **[M2003-120]**.
- **WEIGHS FOR** on the capital the business needs (40% to 55% pre-tax on net tangible operating capital through the
  cycle) **[M2011-060]**; **UNDECIDED** on the added capital, which has earned roughly the average at a cyclical high and
  much less across 2008 to 2017 **[M2001-019]**, **[M2003-120]**. Net: **WEIGHS FOR, qualified.**

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (filed statements; `tools/run.py` table, first-filed vintage;
  USD millions):

| year-end | sales | receivables (% sales) | inventory (% sales) | goodwill + intangibles | equity | debt | cash |
|---|---|---|---|---|---|---|---|
| 2016 | 3,505 | 530 (15.1) | 532 (15.2) | 1,423 | 1,593 | 994 | 438 |
| 2018 | 4,482 | 725 (16.2) | 651 (14.5) | 2,604 | 1,781 | 1,793 | 189 |
| 2020 | 4,186 | 635 (15.2) | 607 (14.5) | 2,734 | 2,070 | 1,590 | 260 |
| 2022 | 4,948 | 742 (15.0) | 741 (15.0) | 2,640 | 2,361 | 1,443 | 440 |
| 2025 | 5,845 | 857 (14.7) | 1,084 (18.5; 852.5 or 14.6 under LIFO) | 4,455 | 3,848 | 2,325 | 482 |
| 2026-06-30 | n/a | n/a | n/a | 7,544 | 3,912 | 5,373 | 379 |

  What the figures say: receivables have stayed at 15% of sales for ten years, and inventory at 14.5% to 15.2% on the
  LIFO basis, so there is no sign of sales pulled forward or stock building ahead of sales **[M1995-064]**. Retained
  earnings rose from 1,879 to 4,156 while equity rose less (buybacks, pension losses in other comprehensive income).
  Goodwill and intangibles tripled and since 2018 exceed equity; tangible equity is negative (2025: 3,848 − 4,455 = −607;
  June 2026: −3,632). What they say together: the business needs little tangible capital, and the growth has been bought
  with retained earnings and debt. What they cannot say: whether the $7.5B of purchased intangibles and goodwill will earn
  their cost. The inventory jump of 2025 is the accounting change, not a build: under LIFO it would be 852.5, or 14.6% of
  sales (Note 1, FY2025).
- **The real costs.** Depreciation is real and is below capex (capex 1.6x depreciation proper in 2025); owner cash deducts
  all capex. Stock pay ($33.0M in 2025) is deducted **[L2021-003]**. Acquired-intangible amortization ($109.6M in 2025) is
  partly a non-cost, since "the amortization of customer relationships" arises "through purchase-accounting rules"
  **[L2012-003]**; the owner-cash figure is cash-based and so already excludes it. Restructuring is charged every year and
  is **not** excluded from the adjusted figures since at least 2023 (Item 7, FY2025), which is to the company's credit by
  **[L2016-007]**; in 2014 to 2019 it was excluded (10-K FY2016).
- **The framing.** Every release and the 10-K lead with adjusted figures: the Q2 2026 release's first bullet is "adjusted
  diluted EPS of $5.52 (up 12% y/y)" beside GAAP $4.52, and "The Company believes Adjusted EPS is a useful measure of
  underlying performance in light of our acquisition strategy" (Exhibit 99.1, `0001628280-26-049934`). The adjustments
  exclude amortization and "transaction, integration and separation costs", which recur every year of a serial acquirer
  (13.5, 13.8, 7.0 in 2023 to 2025; about $0.50 a share expected in 2026). That is the management the rows describe as one that "regularly
  attempts to wave away very real costs" **[L2016-006]**, mild in form (every adjustment reconciled; restructuring and stock pay kept in).
  EBITDA is in the filer's own mouth for the price of a business **[M2002-026]**, **[R1996-023]**: the NSI price was given
  to owners as "~15.5x anticipated 2026 EBITDA" (8-K, `0001193125-26-204099`).
- **The accounting choice.** In Q2 2025, a year of new tariffs, the company moved its US inventories from LIFO to FIFO,
  calling FIFO "preferable because it provides better matching of costs and revenues" and better peer comparability. The
  effect in 2025 was +$62.7M of operating income (operating margin 20.7% reported, 19.6% under LIFO) and +$0.89 of diluted
  EPS; reported EPS growth of 14.9% would have been about 8.9% under LIFO. The balance sheet shows other accrued
  liabilities +$28.1M and other non-current liabilities +$27.5M from the change, which I read as tax on the LIFO reserve
  being recaptured (an inference: the filing does not say whether the tax method changed). If so, the company accepted
  cash tax sooner in exchange for higher reported earnings. That is a choice of the more optimistic of two GAAP readings,
  the thing that makes the speakers "very worried" **[M1994-079]**; it is also fully disclosed, with three years of LIFO
  figures beside the FIFO ones.
- **Confusion or suspicion?** No confusion: every figure reconciles, the LIFO effect is tabulated, and the cash statement
  is plain **[M1995-063]**, **[M2003-029]**. On suspicion, the two-tell CONVENTION (Q4) applies to the make-the-numbers
  habit plus a second tell; I found guidance raised but no record read of targets consistently met, so the habit is not
  established, and the tells found (adjusted EPS featured, EBITDA used for a price, a LIFO switch in an inflationary year)
  are written down and weighed against. A second analyst could call the LIFO switch plus the featured adjusted EPS the
  "one cockroach" pair **[L2002-039]**; I do not, because both are fully disclosed and neither hides a cost from the
  cash statement. Recorded as a judgment that could go the other way.
- **VERDICT on confusion: IN. WEIGHS AGAINST** on the framing and the accounting choice **[L2016-006]**, **[M1994-079]**,
  **[M2002-026]**. The recast earnings for Q7 are the owner-cash table in Step 0 (cash, so neither the LIFO switch nor
  the amortization affects it).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. Running the business: Gerben Bakker, chief executive since October 2020 and
  chairman since May 2021, joined Hubbell in 1988 and ran Hubbell Power Systems from 2014 to 2019 (Item 1, FY2025); the
  utility business that carries the castle is the one he built. The hand he was dealt from 2020 included the strongest
  utility and data-centre demand in the record, so the margin rise from 12.7% (2020) to 20.7% (2025) is partly the hand,
  not the play; peers rose too (Q2). What he did with it: sold residential lighting and kept selling out of the business
  whose moat had gone (ability), and bought Systems Control, DMC Power and NSI at full prices with debt (Q6). Treatment of
  owners: Q6.
- **The proxy** **[M1994-009]**: chief executive's 2025 total pay $10,346,752, 161 times the median employee; personal use
  of the company aircraft $24,705 (proxy, `0001308179-26-000121`). He owns 63,167 shares outright (about $30M at the price)
  plus 50,025 obtainable under SARs, a real stake for a hired manager. The outside directors' common holdings are small
  (366 to 19,085 shares each); several hold more in stock units under the directors' deferred plan, which are granted.
- **The tells of dishonesty.** None found in what was read. Reports explain the drivers in plain terms year by year **[M1998-036]**,
  including the bad years (10-K FY2021 on material cost running ahead of price);
  the 10-K names its competitors' size and its own exposure to price competition. The weak spots are framing (Q4), not
  candour. Integrity is applied on doubt alone **[M2013-088]**: I have no doubt of honesty from the record read, only a
  preference for adjusted figures.
- **Love of the business.** A 38-year Hubbell career and a shareholding held rather than sold are evidence of the business
  over the money **[M2000-098]**; there is no seller's sale here to read.
- **VERDICT on integrity: IN** **[M2015-047]**, **[M2013-088]**. **Ability WEIGHS FOR**, modestly: a long record in the
  business, the exit from lighting, and margins held through 2020 and 2021, against a favourable hand **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- **The retention test** **[R1995-009]**, **[M1998-110]**. Market leg, 2016 to 2025: net income attributable 2017 to
  2025 was $4,718M and dividends $1,964M, so about $2,754M was retained; market value went from about $6.47B
  (55,446,167 shares on the FY2016 cover x $116.70 close 2016-12-30, aggregator, flagged) to about $23.65B (53,253,805
  shares at 2025-12-31 x $444.11, aggregator, flagged), a rise of about $17.2B. The market leg passes many times over, but
  most of the rise is a higher multiple (market value over owner cash about 20 times in 2016, 28 times in 2025), and the
  market leg alone can mislead **[R2009-002]**, so the intrinsic leg is read as well. Intrinsic leg: owner cash rose from 322 (2016) to 842 (2025), about 520 a year more
  on about $2.75B retained and about $1.3B of added net debt, roughly 13% after tax, at a margin peak. It passes, on the
  cycle's best years.
- **Buybacks** **[L1999-023]**, **[L2016-002]**. The programme names no price ("Subject to numerous factors, including
  market conditions and alternative uses of cash", Item 5 FY2025). Prices paid: $347.14 to $387.10 in February to June 2025
  ($225.0M in all), and $482.87 to $513.86 in February to May 2026 (10-Qs Q1 and Q2 2025 and 2026). Under the CONVENTION
  (Q6), a buyback with no stated price weighs against unless the prices paid sit at or below the bottom of the Q7 range; the
  Q7 range below is $204 to $405, so every purchase was above its bottom and the 2026 purchases above its top. The 2026
  purchases were also made while $2.8B was being borrowed for NSI, which fails the first condition, "available funds [...] beyond the near-term needs of the
  business" **[L1999-023]**. **Weighs against.**
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**. No stock deals: every acquisition was for cash, so the all-stock
  STOP **[L2009-019]** does not apply. NSI: $3.0B for a business with about $570M of anticipated 2026 revenue and about
  $194M of anticipated EBITDA (both the seller-side projections in the press release), bought from a private-equity owner
  ("a portfolio company of Sentinel Capital Partners") through an advised sale, the case the rows call "dressed up for
  sale" **[L2000-008]**; financed with a $900M term loan, $1.9B of notes and commercial paper. Judged on an all-equity basis
  **[L2017-004]**: my rough estimate of NSI's owner cash, from the release's EBITDA less an assumed $15M capex and 25% tax,
  is about $135M, a 4.5% yield on the price, below the 5.63% long bond; the deal adds value only if NSI grows at about 7%
  a year for ten years (value.py). Value given against value got is unproven and probably unfavourable at the price. The
  "acquisition strategy" is named as the reason for the adjusted figures (Q4), and "all these forces that push toward deals"
  **[M2014-076]** describe the structure. **Weighs against.**
- **Dividends.** Raised every year read (Item 5 FY2025: $1.32 to $1.42 a quarter in October 2025); payout about a third of
  net income. Neutral.
- **Part A: WEIGHS AGAINST** (buybacks above value with no stated price, debt-funded acquisitions at full prices), with the
  retention test passed at a cyclical high **[L2016-002]**, **[L2017-004]**.

**Part B, the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**. Short-term incentive: 80% financial (adjusted EPS and free
  cash flow at the enterprise; operating profit and operating cash flow in the segments), 20% strategic. Long-term: 50%
  performance shares on relative sales growth, adjusted operating margin and relative total shareholder return; 25%
  stock appreciation rights; 25% restricted shares (proxy, `0001308179-26-000121`). No measure charges for the capital
  employed: "a batting average that does not include a cost of capital is a phony batting average" **[M1995-010]**. Relative
  sales growth and adjusted EPS (which excludes deal costs and amortization) both rise when a business is bought with
  debt, whatever it earns on its price **[L2017-004]**. SARs carry no step-up for retained earnings **[L1994-021]**.
- **The board.** The chief executive is also chairman **[L2014-026]**; the rows treat that as a problem when the chief
  executive is mediocre, which I do not find. Compensation is benchmarked by a consultant to "the 50th percentile of the
  Peer Group data for each compensation element" (proxy), the ratchet the rows warn of. The proxy is long.
- **Owners as partners.** Earnings guidance is given and raised each quarter (Exhibit 99.1, `0001628280-26-049934`), the
  practice **[L2019-006]** calls "the scourge of earnings" guidance.
- **Part B: WEIGHS AGAINST**, modestly: capital-free metrics that reward bought growth, SARs, peer-median benchmarking and
  guidance **[M1995-010]**, **[L1994-021]**, **[L2019-006]**; the person outranks the plan **[M2007-006]**, and the person
  passes Q5.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[R1996-018]**, as a range
**[L2000-024]**. Construction by the CONVENTION (Q7, with the four PG specifics).

- **Cash input:** five-year mean of owner cash after every real cost, **$639.8M** (Step 0; capex variant; the D&A variant
  is $610.8M).
- **Growth shown** on aggregate owner cash, 2021 to 2025: 406.0 to 841.7, **20.0% a year**. **Capped by Q3**: the base year
  2021 was the cost-squeeze year, so the rate is the kind "a base year in which earnings were poor can produce"
  **[L2005-003]**; it includes about $2.35B of acquisitions not deducted from owner cash and a margin step shared by the
  whole industry **[L1994-009]**; carried ten years it puts owner cash at about $5.2B in 2035, against $5.8B of total sales
  today, which "if you trace out the mathematics of it" is an absurdity **[M1999-067]**, **[M2003-120]**. The cap used is
  the highest rate the full record supports: aggregate owner cash 2008 (257) to 2025 (842), **7.2% a year** over seventeen
  years, itself flattered by acquisitions and the boom. A strict reading of "no rate that runs past the discount rate"
  would cap at 5.63% instead (shown below).
- **Ten years, then no real growth** (zero nominal), discounted throughout at **5.63%**.
- **NSI** (bought after the five-year window, with $3.0B of new debt not in the owner-cash figures): adjusted at each end
  using my estimate of its owner cash (about $135M a year, from the seller-side EBITDA projection; flagged, since
  projections are not relied on **[M1995-050]**). At no growth it is worth about $2.41B against $3.0B paid (−$11 a share);
  at 7.2% growth about $4.27B (+$24 a share). The adjustment does not move the box.

| case | value, $M | per share (52.83M) | with NSI adjustment |
|---|---|---|---|
| no growth (bottom) | 11,364 | $215 | **$204** |
| 5.63% for ten years (strict cap) | 17,762 | $336 | not computed |
| 7.2% for ten years (top) | 20,148 | $381 | **$405** |
| 10.0% (what the price implies at 5.63%, see below) | 25,094 | $475 | |
| 20.0% shown, uncapped (rejected as absurd) | 54,447 | $1,031 | |

- **Value range: $204 to $405 a share against $482.23.** Width about 2.0 to 1, inside the three-to-one CONVENTION, so
  the range is narrow enough to conclude from **[L2000-025]**.
- **The price against the range.** The price is above the top of the range. At $482.23 the expected return on owner cash
  is **2.5% to 4.6% a year after corporate tax** (no growth to 7.2% growth; 5.6% if owner cash grew 10% a year for ten
  years). The price implies owner cash growing about **10.2% a year for ten years** at the bond rate, and about **15.5% a
  year** to earn the floor. Under the CONVENTION's fourth specific, a price above the top of the range closes OUT through
  the floor: "there’s just a point at which we drop out of the game" **[M2003-149]**.
- **Pre-tax and after-tax, stated.** Owner cash is after corporate income tax. The floor CONVENTION is about ten percent
  **pre-tax** ("at least 10% pre-tax returns" **[L2002-020]**). I convert by Hubbell's own tax rate, about 21% (effective
  20.3% in 2025, 22.1% in 2024, Item 7 FY2025): 10% pre-tax = **7.9% on after-tax owner cash**; so the expected returns at
  the price above are about 3.2% to 5.8% pre-tax. The row itself translates 10% pre-tax as 6½ to 7% "after corporate tax"
  at the corporate rate of its day **[L2002-020]**; at that translation the fair-price band below would top out at about
  $306 to $337, and the cheap price would be about $153 to $169. Neither reaches the price.

**Reported at the owner's request (not a rule change; COMPUTATION — NOT A CLEARANCE, since the file closes at this STOP):**
- **Value range:** $204 to $405 a share.
- **Fair-price band** (prices inside the range at which the expected return is at or above about 10% pre-tax, 7.9% after
  tax): **$204 to about $259**. Its top is the price at which the top-end case (7.2% growth for ten years, NSI worth about
  what was paid) returns 7.9% after tax; at the bottom of the band, $204, the no-growth case returns 5.9% after tax (7.5%
  pre-tax), so inside the band the floor is met only if the growth case comes true.
- **Cheap price** (below which no pencil is needed): **about $129**, the price at which owner cash with **no growth at all**
  yields 7.9% after tax (about 10% pre-tax) after taking NSI at its no-growth value; below it the case "ought to just kind
  of scream" **[M1996-084]**. The price is 3.7 times the cheap price and 1.9 times the top of the fair-price band.

- **VERDICT: OUT.** Valued, with a range narrower than three to one, and the price above its top: the expected return at
  the price (about 3% to 6% pre-tax) is below the floor of about ten percent **[M2003-149]**, **[L2002-020]**, and far
  from a price that would "scream" **[M2009-005]**. A wonderful business can be bought at a fair price, but "You can turn
  any investment into a bad deal by paying too much" **[M2019-015]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
- **NOT REACHED as a clearance** (the file closed at Q7). Recorded for the record only: the 30-year Treasury at 5.63% beats
  the 2.5% to 4.6% after-tax expected return at the price in every case of the range, so the name would also be "taken out
  of the filter" by the bond **[M1997-089]**. The ranking against holdings was not done (blind rule).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
- **NOT REACHED as a clearance**; recorded. Debt after NSI $5,373M (commercial paper $567.0M; notes of $300M due 2027 and
  $450M due 2028; term loans $600M due 2028 and $900M due 2029; notes 2031 to 2036), cash $378.6M (10-Q Q2 2026). Against
  ability to pay **[M1995-104]**: about $1.0B of owner cash a year including NSI and operating income of about $1.2B to
  $1.4B against an estimated $250M of annual interest, coverage of about 4x to 5x on pre-tax earnings over interest **[L2012-002]**. About $2.8B
  matures by 2029, so the company assumes refinancing, the assumption **[L2010-020]** warns is "usually valid" until it is
  not. Covenant: debt to capitalization no more than 65%. No collateral calls, derivatives books or cash-out features
  found. The "little or no debt" criterion **[R1997-001]** is stated for whole businesses and is not applied to a stake;
  as a weight: **AGAINST**, moderately (leverage at a record for the company, taken on to buy growth at a full price).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
- **NOT REACHED.** The draft would have the buyer wait: "You wait for the fat pitch" **[M2003-070]**; "If the money piles
  up, the money piles up" **[M1998-137]**. Nothing to size.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
- Not asked as a gate (the file closed at Q7). Recorded: electrical and utility hardware; none of the named businesses;
  the newspaper test **[M2008-011]** raises nothing in what was read.

---
## THE BOX
**OUT at Q7.** Q1 IN, Q2 IN (narrowly: a moderate castle shown on seventeen years of record), Q4 IN on confusion; the
value range is **$204 to $405 a share against $482.23**, the price above the top, the expected return about 3% to 6%
pre-tax against the floor of about ten. Fair-price band (COMPUTATION) **$204 to about $259**; cheap price (COMPUTATION)
**about $129**. Not TOO HARD: the deciding question was answered.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed after each**: the dispatch
      forbade commits; the file was written in two passes (Step 0 and the foundations first, then the whole).
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession; no
      number without a row, a filing or the label COMPUTATION or CONVENTION. The aggregator closes used in Q6 and Step 0 are
      flagged.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are recorded as NOT REACHED and are
      not clearances.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash flow less stock pay
      less all capex, from the filed statements; the sovereign from the US Treasury; aggregator quotes flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (ten items under the foundations, before Q1).
- [x] No row dated after the anchor is cited (the run is dated today; no point-in-time anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its labels were checked against the filing.
- [x] `python tools/check_framework.py` PASS before the commit (run at the end of this session; see the report). No commit
      made.
- Honest gaps: no approved-vendor-list or market-share evidence exists in the filings (Q2 tests 1, 5, 8, 9 rest on
  margins and analogy); Eaton's operating margin is not tagged after 2019 and its electrical segment margins were not
  read; NSI's figures are seller-side projections; the LIFO tax reading is an inference; the "tangible assets" ratio for
  peers uses first-filed XBRL totals, not each peer's filed statement read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The Q7 growth cap is ambiguous.** The CONVENTION says the shown growth is "capped by the growth arithmetic of Q3: no
   rate that runs past the discount rate or traces to an absurdity". It does not say what the cap is once the shown rate
   is rejected. A literal reading caps at the discount rate (5.63% here); the absurdity reading leaves the analyst to pick
   a lower rate. I used the full-record aggregate rate (7.2%, 2008 to 2025) and showed the 5.63% case beside it. For a
   serial acquirer the five-year shown rate is mostly bought growth, and the convention has no rule for acquisitions made
   inside the window (owner cash deducts capex but not acquisition outlays), so two analysts can differ by a factor of three
   at the top of the range. A rule is needed: either deduct acquisition spending inside the window from owner cash, or
   measure growth only on the part of the business owned throughout.
2. **Acquisitions after the window.** A purchase that closed after the last fiscal year (NSI, $3.0B, debt-funded) is not
   in the five-year owner cash but its debt is on today's balance sheet. The convention is silent; I adjusted each end
   with an estimate that rests on a seller's projection, which the foundations rule out as a basis for decision. A rule is
   needed for post-window acquisitions (for example: value the acquired business at the price paid at the top end and at
   its no-growth owner cash at the bottom, with the debt subtracted).
3. **The pre-tax floor against after-tax owner cash.** The floor is stated pre-tax; owner cash is after tax; the row that
   states the floor converts at the corporate rate of 2002 (6½ to 7% after tax). The framework does not say which tax
   rate converts. I used the company's own rate (about 21%, giving 7.9%) and showed the row's translation beside it.
4. **"Fair-price band" and "cheap price" are not framework terms** (the owner's reporting request); I defined them in the
   Q7 section. The band's top depends on which case carries "the expected return"; I used the top-end case, which makes
   the band generous.
5. **Q2's tests assume evidence the filings do not hold** for an industrial supplier: approved-vendor lists, share of
   mind, and what competitors say. The verdict therefore rests on the margin record against peers, which the framework
   does not name as a castle test. A sentence saying whether a long comparative return record may stand in for the
   customer-choice tests would help; without it, a stricter analyst could close this castle TOO HARD (WORK).
6. **The Q4 two-tell CONVENTION** is written for the make-the-numbers habit plus a second tell. It does not say how to read
   two tells without the habit (here, featured adjusted EPS plus a LIFO-to-FIFO switch in an inflationary year). I weighed
   them against rather than calling suspicion; the framework does not settle it.
</content>
</invoke>
