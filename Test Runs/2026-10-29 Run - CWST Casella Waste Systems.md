# Company Run — CASELLA WASTE SYSTEMS, INC. (Nasdaq: CWST) — 2026-10-29
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-29, after the run was committed: not held (no CWST line in `PORTFOLIO.md`).*

**CONTAMINATION, declared:** the `git log` I ran before copying the template showed the three latest commit subjects, all about
another company (AQMS, a v5 re-run folded OUT at Q1); a `ls "Test Runs" | grep -i cwst` run before the copy, to make sure the
dated file name was free, returned nothing. A lock file in `Screens/_daily/` was present (the dispatcher's). The project memory
index, loaded with the session, carries one-line summaries of the queue state with no line about this company. Nothing of these
is used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $89.39 (2026-10-29, live quote printed by `tools/run.py`; an aggregator, flagged per operator rule 5; used for the
  live quote only).
- **Shares by class** from the latest filing's cover: Class A 62,651,846 and Class B 988,200, as of 2026-07-15 (10-Q for the
  quarter to 2026-06-30, filed 2026-08-07, accession `0000911177-26-000049`; `python Screens/cover_shares.py CWST`). The charter
  note (10-K FY2025, accession `0000911177-26-000008`, Note on stockholders' equity): Class B carries ten votes a share, is
  "convertible into Class A common stock on a share-for-share basis at the option of the shareholder", and shares the same
  economics, so the classes are added: **63,640,046 shares**. Cross-check: the 10-K's balance sheet shows 988,000 Class B issued
  and outstanding at 2025-12-31; no treasury stock line; no 8-K or prospectus after the 10-Q issues shares (the 8-Ks of
  2026-08-06 and 2026-10-01 are results and the NCES landfill date).
- **Market cap:** 63.640M x $89.39 = **$5,689M**.
- **Sovereign for the earnings currency (USD):** **5.37%**, the 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-28 (printed by `tools/run.py` from the issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-20, accession `0000911177-26-000008` (Items 1, 1A, 3, 5,
  7, 7A, 8 with notes); 10-Q for the quarter to 2026-06-30, filed 2026-08-07, accession `0000911177-26-000049`; proxy (DEF 14A)
  filed 2026-04-17, accession `0001193125-26-161565`; 8-Ks of 2026-10-01 (`0000911177-26-000052`, NCES landfill final day
  moved to 2026-12-31), 2026-08-06 (`0000911177-26-000041`, Q2 results), 2026-04-22 (`0000911177-26-000015`, equipment master
  lease), 2026-05-11, 2026-05-27, 2026-06-01 (`0000911177-26-000024`, `-000028`, `-000030`, a $15.0M tax-exempt bond
  remarketed at 4.300% to 2036). Earlier 10-Ks for the span as listed under Q2 and Q4.
  **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$329.8M** in the
  10-K's cash-flow summary (Item 7, "Summary of Cash Flow Activity") equals the XBRL figure `tools/run.py` prints (329.8).
- `python tools/run.py CWST` arithmetic lines only (full print in the research folder, `run_py_output.txt`):

  | FY | OCF | SBC | D&A | capex (PP&E) | OCF-SBC-capex | finance-lease principal |
  |---|---|---|---|---|---|---|
  | 2023 | 233.1 | 9.1 | 170.7 | 154.9 | 69.1 | 9.0 |
  | 2024 | 281.4 | 12.2 | 234.9 | 203.2 | 65.9 | 12.1 |
  | 2025 | 329.8 | 14.2 | 306.8 | 245.1 | 70.5 | 20.9 |

  Five-year mean of OCF-SBC-capex: 66.3 (the tool's other window). Acquisitions are not in these columns (see Q3, Q7). The tool's
  "growth the price assumes" and "points over the sovereign" lines are not used (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this collection, transfer, landfill and recycling company will
earn for its owners over ten years and more, not what the quote does. The market serves and does not instruct **[M2006-077]**:
the price of $89.39 is read only against the value at Q7, never as evidence of quality. No macro forecast enters
**[M2000-094]**: the waste volumes of the Northeast economy are not forecast here. Who is paid to tell you: the filer's own
releases feature an adjusted EBITDA and an adjusted free cash flow, so the GAAP figures and the cash-flow statement are read
first. The analyst's habit that bears hardest is to look "for what" is wrong and at "what you" are missing **[M2025-013]**, and
to write contrary evidence down at once **[M1997-127]**. **Contrary evidence, written down as found** **[M1997-127]**:
(1) FY2025 operating income was $63.7M on revenues of $1,836.8M (3.5%) and net income $7.9M (10-K, `0000911177-26-000008`,
Item 7); (2) the Ontario County Board of Supervisors voted on 2024-12-05 to close the Ontario County Landfill at the end of
2028, when the 25-year operating agreement ends, and the company says it will then cease operations there (10-K, Item 1 and
Item 1A); (3) the NCES landfill in Bethlehem, New Hampshire, takes its last waste on 2026-12-31 (8-K `0000911177-26-000052`),
and the company calls it "unlikely" that its replacement in Dalton, New Hampshire, will be permitted and running by the end of
2027 (10-K, Item 1A); (4) the 10-K itself says the three national companies it names "may be able to achieve greater
economies of scale than we can" (Item 1, Competition); (5) four public share offerings since 2019 (3.6M shares at $29.50 in
2019, 2.7M at $56.00 in 2020, 6.1M at $85.50 in 2023, 5.2M at $100.00 in 2024; 10-Ks FY2019, FY2021, FY2023, FY2025, Item 7);
(6) the Mid-Atlantic region, bought from 2023 onward, lost money in each year: $(4.6)M, $(18.0)M, $(20.4)M of operating
income in 2023, 2024 and 2025 (10-Ks FY2024 and FY2025, segment tables).

## THE STANDING RULE
A buyer paying cash from his own funds, with no borrowing and no collateral or cash-out feature, is not put at risk of ruin by
owning a part-interest in a listed waste company; the rule binds how the purchase would be financed, sized and held:
"We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**, and "Never risk permanent loss of capital." **[L2023-005]**. Nothing in this name forces a different answer;
the rule is not engaged.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
  five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**, with the key variables found and
  judged for how predictable they are **[M1998-044]**. The product need not be understood technically if "the economic
  dynamics of the industry" are **[M2011-014]**.
- **What the business is** (10-K FY2025, `0000911177-26-000008`, Item 1): "a regional, vertically integrated solid waste
  services company" in eleven states from Maine to West Virginia; revenues FY2025 $1,836.8M, of which collection 65.1%,
  disposal 14.3%, Resource Solutions (recycling processing and National Accounts brokerage) 19.6%; three regional segments
  (Eastern $472.6M, Western $663.2M, Mid-Atlantic $341.1M of revenue) and Resource Solutions ($360.0M); eight Subtitle D
  landfills and one C&D landfill; about 5,600 employees.
- **The key variables, and how foreseeable they are.** (1) Price per collection stop and per ton disposed: the filer reports it
  every year (solid-waste price +3.9% in 2021, +6.4% in 2022, +7.5% in 2023, +5.7% in 2024, +4.9% in 2025; 10-Ks FY2021 to
  FY2025, Item 7). (2) Volume: small changes either side of zero (+2.2%, +0.7%, -1.9%, -1.8%, -0.9% in the same years).
  (3) Disposal capacity: the permitted and permittable tons at each landfill, the permit and lease terms and dates, all filed
  (total estimated capacity 98.2M tons at 2025-12-31 against 3.7M tons consumed in 2025; 10-K Item 1). (4) The cost of
  collection (labour, fuel, trucks) and the capital to replace trucks, containers and landfill cells. (5) Recycled-commodity
  prices, largely passed to customers through processing fees and a floating fee (Item 1). Garbage is collected and buried in
  ten years much as now; the industry does not change fast, and none of these variables turns on a technology forecast
  **[M1999-063]**. What cannot be foreseen with confidence is the permitting outcome at particular sites; that bears on the
  castle and is asked at Q2, not here.
- **Readable from the figures** **[M2008-069]**: the segment tables, the landfill table, the price and volume bridges and the
  cash-flow statement give the economics directly; the accounts are those of an operating company, not a lender.
- **Doubt test** **[M2002-092]**: no doubt that the business is understood as an operating business; the doubt is about its
  castle and its returns, which are Q2's and Q3's.
- **Routing:** not a fast-changing industry; not a financial institution; not a start-up **[L2007-015]**; a company of four
  operating parts, understood part by part (all four are waste services of one kind; none is opaque).
- **VERDICT: IN.** The economics are those of local route density, disposal capacity and price, foreseeable in outline ten
  years out **[M2012-065]**, **[M2000-037]**, with key variables that are filed and slow to move **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**Lines of evidence chosen** (from the 10-K's Item 1, Item 1A and Item 7, as the brief asks): the landfills and their permit
and lease terms (Item 1, Landfills; Item 1A, permits); the price and volume bridge through the inflation of 2021 to 2025
(Item 7 of each 10-K); the cost position against the three rivals the 10-K names (Item 1, Competition); the segments and their
margins over the span (Item 7 and Note 21 of each 10-K); the acquisitions and their goodwill (Item 7, Note 5).

**The competitors.** The 10-K names "Waste Management, Inc., Republic Services, Inc. and Waste Connections, Inc." (Item 1,
Competition); all three file 10-Ks with the SEC. It also mentions "regional and local companies" without naming any, so none is
flagged as a non-filer. Same metrics from each filer's own XBRL (first-filed vintage, transcription; script and output in the
research folder, `facts.py`, `facts_output.txt`): operating income over revenue, and operating income over total assets less
goodwill and intangibles at the year end.

| Filer (10-K FY2025 accession) | Operating margin, span | Op. income / tangible assets, span | FY2025 margin | FY2025 on tangible |
|---|---|---|---|---|
| Casella (`0000911177-26-000008`), 2012 to 2025 | -2.4% to 8.8% | -2.6% to 8.9% | 3.5% | 3.4% |
| Waste Management (`0001104659-26-012049`), 2012 to 2025 | 7.7% to 18.7% | 6.7% to 17.8% | 17.1% | 15.3% |
| Republic Services (`0001060391-26-000094`), 2012 to 2025 | 11.6% to 17.4% | 13.6% to 20.1% | 17.4% | 19.4% |
| Waste Connections (`0001104659-26-013700`), 2016 to 2025 | 7.6% to 18.1% | 5.8% to 15.9% | 18.1% | 15.9% |

Casella's fiscal years 2012 to 2014 ended in April (it moved to a December year in 2014). Earlier accessions of the span:
Casella FY2016 `0000911177-17-000017`, FY2020 `0000911177-21-000009`; Waste Management FY2013 `0001193125-14-056656`, FY2020
`0001558370-21-001348`; Republic FY2013 `0001060391-14-000011`, FY2020 `0001060391-21-000014`; Waste Connections FY2016
`0001144204-17-011069`, FY2020 `0001558370-21-001174`. In every year of the span Casella's margin is below each of the three
with one exception, Waste Connections' 2020 (7.6%, against Casella's 7.7%).

**The parts table** (operating income by segment as each year's latest 10-K reports it, USD M; corporate costs were largely
unallocated from the FY2024 presentation onward, so 2021 and 2022 stand on the older, allocated basis; 10-Ks FY2021
`0000911177-22-000009`, FY2023 `0000911177-24-000005`, FY2024 `0000911177-25-000010`, FY2025 `0000911177-26-000008`):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum | Share of the positive parts | Decides |
|---|---|---|---|---|---|---|---|---|
| Western (VT, western NH, upstate NY; five Subtitle D landfills and Hakes C&D) | 49.0 | 65.5 | 101.6 | 111.7 | 121.2 | 449.0 | 58% | **yes** (more than half) |
| Eastern (ME, NH, MA, CT; NCES and Juniper Ridge) | 12.9 | 16.6 | 52.8 | 62.7 | 72.6 | 217.6 | 28% | no |
| Resource Solutions (recycling, National Accounts) | 17.6 | 15.9 | 16.4 | 28.4 | 29.2 | 107.5 | 14% | no |
| Mid-Atlantic (PA, NJ, DE, MD, WV; McKean landfill; bought from 2023) | - | - | (4.6) | (19.6) | (20.4) | (44.6) | loss | no |
| Corporate Entities | (1.8) | (2.6) | (85.8) | (110.4) | (138.9) | (339.5) | cost | - |
| **Company** | 77.7 | 95.4 | 80.4 | 72.8 | 63.7 | 390.0 | | |

Western is more than half of the positive parts and more than the company's whole five-year operating income, so it decides
(Q2, a business of parts). Western's own figures: revenue $663.2M in FY2025, operating income $121.2M (18.3% before corporate
costs), segment total assets $1,135.4M at 2025-12-31 (10.7% pre-tax on them, goodwill included); 2023 and 2024 were 10.9% and
9.7% on the same measure (Note 21 of the FY2025 10-K). Charged a share of corporate costs pro rata to revenue (corporate
$138.9M on $1,836.8M, 7.6%; a CONVENTION of this run, rationale: the filing allocates none, and the rivals' margins carry their
own corporate costs), Western's margin is about 10.7% and its pre-tax return on its assets about 6.3%.

**The castle tests, each with its filing fact.**
- **What keeps it standing, and how permanent** **[M1995-038]**. The key factor is permitted disposal capacity in a market the
  10-K says has "tightened" over ten years as sites closed (Item 1, Optimizing Long-term Disposal Capacity), with route density
  around Casella's transfer stations. Waste USA is "the only operating permitted Subtitle D landfill in the State of Vermont"
  (Item 1), a natural franchise of the kind the rows name, "a natural franchise because of surface capabilities"
  **[M1995-037]**. Its permanence is the weak point: several of the deciding part's sites are held under county agreements with
  end dates (Ontario County to 2028; Chemung County to 2035 after a five-year option; Clinton County under an operating,
  management and lease agreement since 1996), and the host decides at the end. "On December 5, 2024, the Board of Supervisors
  of Ontario County, New York approved a motion to close the Ontario County Landfill in Seneca, New York at the end of the
  fiscal year ending December 31, 2028 upon the expiration of the 25-year OMLA, at which time we intend to cease operations at
  the Ontario County Landfill." (10-K Item 1A). Ontario is permitted to take up to 0.9M tons a year, the largest of the five
  Western Subtitle D sites (Waste USA 0.6M, Hyland 0.5M, Chemung 0.4M, Clinton County 0.3M; Item 1).
- **The money test** **[M2011-015]**. A new entrant with money meets the permitting wall the 10-K describes (Item 1A: permits
  opposed by "Local communities and citizen groups"), which protects incumbent landfills. But the attackers are already inside
  the denser markets: "we typically compete against one or more of the large national solid waste companies [...] any of which
  may be able to achieve greater economies of scale than we can", and "competitors may reduce the price of their services to
  attract additional customers or to win a competitively bid solid waste or recycling contract" (Item 1, Competition).
- **Pricing power and the agony before a rise** **[M2005-020]**. Solid-waste price rose 3.9%, 6.4%, 7.5%, 5.7% and 4.9% in
  2021 to 2025, with volume +2.2%, +0.7%, -1.9%, -1.8%, -0.9% (Item 7 bridges of each 10-K, FY2022 accession
  `0000911177-23-000012`). The business passed its cost inflation through **[M2005-017]**; this weighs for the castle. It is
  read with the field: the rivals priced through the same years, so the power belongs at least as much to the region's disposal
  scarcity as to Casella.
- **Unit volume.** Not the decisive test for a hauler, but the volume line fell in three of the five years while price rose;
  the filer gives no cause beyond lower collection and transfer-station volumes (FY2025 Item 7).
- **The low-cost position** **[M2018-043]**, **[M2004-091]**. The table above: in every year from 2012 to 2025 Casella earned
  about half or less of the margin of Waste Management and Republic Services, and less than Waste Connections in all years but
  one. Cost is measured "on parity or less" against "your other major competitors" **[M2001-013]**, and the filer concedes the
  rivals' greater economies of scale. Even the deciding part, carrying its share of corporate costs, earns about 10.7% on
  revenue against 17.1% to 18.1% for the three rivals in FY2025 after all of their own costs.
- **The low bid** **[M2017-009]**, **[L2004-003]**. Commercial and industrial collection is sold on "one-to-five year service
  agreements" and municipal work by bid; "We compete primarily on the basis of the quality, breadth and price of our services"
  (Item 1). No filing fact shows a customer who will not take the low bid at renewal.
- **Ask the competitors** **[M1999-130]**: no rival speaks of Casella in the filings read; not answerable from the record.
- **Widening or narrowing** **[M1999-108]**. Narrowing in disposal: estimated total landfill capacity fell from 107.2M tons at
  the start of 2023 to 98.2M tons at the end of 2025 (Item 1 table); Southbridge closed in 2018; NCES takes its last waste on
  2026-12-31 (8-K `0000911177-26-000052`); and "we believe that it is unlikely that the landfill under development by us in
  Dalton, New Hampshire will be fully permitted, constructed and operational by the end of fiscal year 2027" (Item 1A). The New Hampshire Department of Environmental Services denied that site's application (Granite State Landfill, LLC) on 2025-04-03, and the company is contesting the denial in the Merrimack Superior Court (10-K Note 13).
  Widening elsewhere: rail deliveries to the McKean landfill in Pennsylvania from 2024 (Item 1), in the loss-making
  Mid-Atlantic part.
- **What could destroy, modify or reduce it** **[M2000-014]**: host-community and regulatory decisions on permits and renewals
  (Item 1A), and PFAS rules that could add capping, leachate and closure costs (Item 1A; 8-K of 2026-10-01).

**The field's returns over the last full cycle.** The span 2012 to 2025 includes the 2020 downturn. The three rivals' returns
on tangible assets ran mostly in the teens, so the field is not one of ordinary returns and that item of the OUT list does not
decide. Casella's own return on tangible assets ran from -2.6% to 8.9% pre-tax over the whole span, and fell from 8.8% to 3.4%
as it bought its way from $1.1B to $1.8B of revenue between 2022 and 2025.

**Judgment.** The moat the rows prize "protects excellent returns on invested capital" **[L2007-004]**; in this field the castle
that stands is the low-cost, dense operator with its own disposal. On the filings, Casella is the field's high-cost operator:
its margin and its return on tangible capital sit far below each of the three rivals its own 10-K names, in every year of a
fourteen-year span but one, and the filer says those rivals may have "greater economies of scale". Where customers renew on
price and rivals cut price to win bids, that is the position the rows close: "commodity businesses have risk unless" one is
the low-cost producer, "because the low-cost producer can put you out of business" **[M1997-010]**; "a company must lower its
costs to competitive levels or face extinction" **[L1994-035]**; "the guy with the lower cost comes in and kills you"
**[M2001-013]**. The deciding part's own advantage, its landfills, is real, but its host takes the largest Western site back in
2028 and the Eastern replacement is called unlikely in time: "A moat that must be continuously rebuilt will eventually be no
moat at all." **[L2007-005]**, with the evidence showing the rebuilding failing at two of the company's own sites (Q2's OUT
list). The pricing record weighs for the castle and is written down; it does not outweigh a cost position read from four
companies' filings over fourteen years.

The other reading, carried and not adopted: that the Western landfills are a natural franchise whose future turns on permit
politics no one can forecast, a moat "tenuous in any way" **[M2000-019]**, which the framework sends to TOO HARD (NATURE). I did
not adopt it because the deciding facts are not forecasts: the cost gap, the Ontario vote and the Dalton statement are filed.
The box would not change at the price on either reading (see the COMPUTATION under AFTER THE STOP).

- **VERDICT: OUT.** The high-cost operator in a field that sells collection on price **[M1997-010]**, **[L1994-035]**,
  **[M2001-013]**, with the deciding part's disposal castle shown filling in at its largest site on the filed evidence
  **[L2007-005]**, **[M2011-015]**. The file closes here; Q3 to Q12 are NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed at Q2).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED.

## Q5 — WHO RUNS IT. NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.

## Q7 — WHAT IS IT WORTH. NOT REACHED (the figures are below, under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE).

## Q8 — NOT REACHED.

## Q9 — NOT REACHED.

## Q10 — NOT REACHED.

## Q12 (optional) — NOT REACHED.

---
## THE BOX
**OUT at Q2**: the field's high-cost operator against the three rivals its 10-K names, in a business that sells collection on
price, with the deciding part's disposal castle filling in at its largest site (Ontario County Landfill to close at the end of
2028 by its host's vote). Integrity facts recorded, not judged (a New Hampshire consent decree on leachate management and
leachate data and reporting at the NCES landfill; see AFTER THE STOP, Q5). The COMPUTATION beneath the stop: value range
$3.25 to $20.33 a share on the all-equity basis (equity-only $14.82 to $25.33) against $89.39; no case earns the floor at the
price. Not TOO HARD, so no research pass is opened.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no verdict;
the box unchanged, operator rule 2.)*

**Q3 (capital).** Capital spending on property and equipment against depreciation, amortization and landfill amortization:
2025 capex $245.1M plus finance-lease principal $20.9M, against depreciation $168.4M, landfill amortization $61.9M and other
amortization $76.5M (mostly acquired intangibles) (10-K FY2025, Item 7). Cash paid for businesses, net: $170.6M, $78.2M,
$851.8M, $468.6M and $224.2M in 2021 to 2025, total $1,793.4M, against owner cash before purchases of $411.4M over the same
years (COMPUTATION below); a further $400.8M in the first half of 2026 (10-Q `0000911177-26-000049`, cash-flow statement).
Since 2018 the company has bought 76 businesses with "over $925 million of total annualized revenues" (10-K Item 1). Pre-tax
operating income on tangible assets fell from 8.8% (2022) to 3.4% (2025) as the purchases came in (Q2 table).

**Q4 (the accounts; the balance sheets first, ten year-ends, from `tools/run.py`'s table, read against the filed statements of
FY2019, FY2021 to FY2025).**
- Equity was negative at 2016, 2017 and 2018 ($-25M, $-38M, $-16M) and the accumulated deficit was $-373M in 2016; it is
  $-125M at 2025. Equity rose to $1,569M at 2025 almost wholly from four share offerings (net proceeds $100.4M in 2019,
  $144.8M in 2020, $496.2M in 2023, $496.2M in 2024, about $1,238M), against retained earnings up $248M in nine years.
- Goodwill and intangibles rose from $128M (2016) to $1,411M (2025) and $1,714M at 2026-06-30, against equity of $1,580M at
  that date: tangible equity was about $158M at 2025-12-31 and about $-134M at 2026-06-30 (10-Q balance sheet).
- Receivables against revenue held steady, about 10.8% (2016) and 9.7% (2025); no build-up of prepaid or deferred accounts
  was seen in the balance-sheet lines read. Cash is small ($25.5M at 2026-06-30).
- Debt on the face of the balance sheet (finance leases included) went from $509M (2016) to $1,155M (2025) and $1,351M at
  2026-06-30.
- The recurring "one-time": "Expense from acquisition activities" of $24.9M (2024), $24.2M (2025) and $6.1M in the second
  quarter of 2026 alone (10-K Item 7; 10-Q segment table); an organics facility closure charge in 2025 and 2026; a Southbridge
  landfill charge in 2024.
- The filer features "Adjusted EBITDA" and "Adjusted Free Cash Flow"; its 8-K forward-looking language speaks of "estimated
  Adjusted EBITDA and other targets" and "guidance" (8-K `0000911177-26-000052`). Recorded only; Q4 and Q5 were not reached.
- Cash taxes are near nil (provision $5.2M in 2025, of which $2.4M current); federal net operating losses of $124M are
  projected to carry into 2026 (10-K Item 7).

**Q5 (the people): integrity facts recorded, not judged.** On 2026-01-12 the New Hampshire Department of Justice and the
NCES subsidiary entered a consent decree resolving "alleged violations related to leachate management and leachate data and
reporting", with a $1.9M civil penalty, subject to court approval (10-K Note 13). In 2023 the company settled a wage-and-hour
class action under the Fair Labor Standards Act for $6.15M (10-K FY2025, Note 18). The founder John W. Casella is Executive
Chairman and former chief executive; 2025 total pay $4.41M (proxy `0001193125-26-161565`, Summary Compensation Table);
Edmond R. Coletta's 2025 total was $2.83M. The chief operating officer of solid-waste operations resigned in March 2026 (8-K
`0000911177-26-000011`); a new chief operating officer was appointed effective 2026-07-20 (8-K `0000911177-26-000035`).
Any later run that reaches Q5 must answer the consent-decree fact.

**Q6 (money and owners).** No share repurchases in the cash-flow statements of FY2016 to FY2025 (no instance found in the
XBRL repurchase tag or the financing sections read). Shares issued in four public offerings, 17.6M shares in all, at $29.50,
$56.00, $85.50 and $100.00 (10-Ks FY2019, FY2021, FY2023, FY2025, Item 7). Acquisitions were paid in cash, the offerings being
separate; no all-stock deal was found. The annual cash bonus runs on "Adjusted Operating Income and Adjusted Free Cash Flow"
and two safety and turnover goals; performance shares vest on "Adjusted Free Cash Flow (weighted 50%) and Adjusted EBITDA
(weighted 50%)" with a relative total-return multiplier against the Russell 2000 (proxy, Compensation Discussion).

**Q9 (debt and exposures).** At 2025-12-31: an $800.0M term loan A and a $700.0M revolver maturing September 2029, secured
by substantially all assets; consolidated net leverage 2.34x against a 4.00x covenant; interest cover 7.56x against 3.00x, both
on the credit agreement's "Consolidated EBITDA" (10-K Item 7). $515.0M of interest-rate swaps expire between December 2026 and
February 2030 (10-Q). Pre-tax income plus interest over interest was ($13.1M + $62.5M) / $62.5M in 2025, about 1.2 times
(XBRL, transcription). Surety bonds for landfill closure obligations come partly from Evergreen National Indemnity, in which
the company holds 19.9% (10-K Item 1). A $250.0M equipment-lease basket was approved by the board on 2026-04-20 (8-K
`0000911177-26-000015`).

**Q7: COMPUTATION, NOT A CLEARANCE** (`q7.py`, `q7_output.txt` in the research folder; USD millions; Q7's convention in full,
each specific stated).
- **Owner cash, five-year window FY2021 to FY2025**, all-equity basis: operating cash flow plus interest paid and taxes paid,
  less tax at the 21% federal statutory rate on pre-tax income plus interest expense (CONVENTION of this run: state tax left
  out for want of a filed state rate; rationale: Whose tax asks for the statutory rate where carryforwards shelter the company,
  and the federal rate is the one the 10-K states), less stock pay, less all capital spending on property and equipment, less
  finance-lease principal (trucks and equipment bought on lease are capital spending): 45.1, 73.4, 96.0, 104.4, 92.5; mean
  **82.3**. Equity-only basis (after interest): 30.5, 57.4, 62.4, 56.3, 46.6; mean **50.6**. Working capital is counted inside
  operating cash flow (specific (d)). The NOL shelter ($124M of federal losses, 21%, used within a few years) is worth about
  $22M at the long rate, about $0.35 a share, shown here and left out of the range.
- **Specific (a), cycles:** no end year is aberrational on the filer's description; the literal window is the base. Beside
  it, the latest year alone (92.5) gives a growth-case value of $25.46 a share.
- **Specific (b), decline:** none; owner cash grew.
- **Specific (c), acquisitions, and the serial acquirer:** net purchases of $1,793.4M exceed half of owner cash before
  purchases ($411.4M), so the central figure is the **organic pair** (purchases left out, organic growth as the filer reports
  it): solid-waste price plus volume plus surcharges and commodity, acquisitions out, 6.1%, 12.4%, 7.0%, 3.8% and 4.2% for 2021
  to 2025, mean **6.7%** (10-K Item 7 bridges; 2022's figure includes 5.0% of fuel and other surcharges). The default pair,
  purchases deducted with total growth credited, has owner cash after purchases of -125.5, -4.8, -755.8, -364.2, -131.7 (mean
  -276.4): no positive value on any growth, shown beside. Deals closed after the window (Mountain State Waste on 2026-01-01;
  Star Waste Systems and two others in April 2026; $400.8M paid in the half-year) are credited at nothing, no earnings of the
  targets being filed, and their financing is inside the net debt below. No purchases are carried after year ten.
- **Specific (e), growth spending:** the filing gives no split of capital spending into maintenance and growth, so the
  all-spending case is central, said so; no separate growth spending is charged.
- **Specific (f), the cap:** owner cash's highest share of sales in the window is 7.6% (2023); carried at 6.7% for ten years
  beside sales at the same organic rate, the share stays near 6.4%; no cut. The rate is above the discount rate inside the ten
  years only, as the convention allows, and zero nominal after year ten.
- **Discount rate:** 5.37%, the 30-year Treasury par yield, 2026-10-28.
- **Net debt:** $1,350.7M of debt including finance leases (net of $12.9M issuance costs) less $25.5M cash at 2026-06-30
  (10-Q) = **$1,325.2M**; operating leases left out, said so. Shares 63.640M.
- **VALUE RANGE, all-equity basis (central):** whole business $1,532M (no growth) to $2,619M (6.7% for ten years), less net
  debt: **$3.25 to $20.33 a share** against **$89.39**. Width 1.71 to 1. Equity-only beside: **$14.82 to $25.33**.
- **The floor, tested first:** at $89.39 the expected return is about 2.1% on the growth case and 1.2% on the no-growth case
  (all-equity), 1.6% and 0.9% equity-only; no case earns about ten percent **[M2003-149]**. Had the file reached Q7 it would
  close OUT whatever the width; the price is above the top of the range.
- **FAIR PRICE** (reporting figure, Part VII; each end valued at ten percent, averaged, after the company's own tax at the
  statutory rate): **$-4.10 a share on the all-equity basis (central; not positive)**; **$10.29 a share equity-only (beside)**.
  The central figure is already the organic pair, so no further relabelling applies.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): template,
      Step 0, Q1, Q2, close.
- [x] Dispatched: the brief allowed the per-question commits; the lock in `Screens/_daily/` was present throughout (the
      dispatcher's). Folding into the register is the dispatching session's step; a run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared under
      contamination: the three latest commit subjects (AQMS) and the memory index lines; not used. My one `ls "Test Runs" | grep`
      before the copy, to check the file name was free, listed nothing.
- [x] Every v5 id resolves (checked by `check_ids.py` in the research folder against `principle_ledger_v5.csv`); every filing
      fact has its accession; the rivals' figures carry their 10-K accessions; numbers without a filing are labelled
      COMPUTATION or CONVENTION.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance, and the Q7 figures
      are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, all capital spending, finance-lease principal, statutory tax), never a
      net-income proxy; the sovereign from the US Treasury; the live quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (the foundations paragraph, then Q2); facts for later questions under AFTER THE
      STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) Q2's "standing castle that protects only ordinary returns" item is written for a field whose durable players
all earn ordinary returns; it is silent on the case met here, a weak player whose own returns are ordinary in a field whose
leaders earn well. I decided on the low-cost test and the rebuilt-moat item instead, and said so. (2) The parts rule measures a
part against "the company's five-year operating profit"; with $339.5M of unallocated corporate costs the deciding part earned
more than the whole company, so the share is above 100%; I also showed it against the sum of the positive parts (58%), and it
decides on both readings. The rule does not say whether a part's castle is judged before or after the corporate costs it
needs; I showed both, the pro-rata charge a CONVENTION of this run. (3) "The high-cost producer in a commodity field" is on
Q2's OUT list, but the framework's commodity paragraph defines a commodity business by dependence on a commodity price, not by
a service sold on bid at renewal; whether waste collection is a commodity field is my reading from the 10-K's own words on
price competition. (4) Specific (c)'s organic pair takes growth "as the filer reports it"; the filer reports price, volume,
surcharges and commodity lines separately, and 2022's fuel surcharges (5.0%) are not plainly organic growth; I counted them,
which raises the top of the range, and the box does not turn on it. (5) Whose tax asks for the statutory rate where
carryforwards shelter the company but does not say whether state tax is in it; I used the federal 21% and said so.
