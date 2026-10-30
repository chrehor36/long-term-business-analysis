# Company Run — Malibu Boats, Inc. (NASDAQ: MBUU) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Working folder:
`Test Runs/_research 2026-10-05 MBUU/` (every filing read is saved there as text with its URL and accession on line 1;
the arithmetic is in `q7_computation.py` and its output file beside it).

**POSITION NOTE, declared before any verdict:** NOT CHECKED. The blind rule of this run forbids opening `PORTFOLIO.md`,
any holding review, the session-state file, the queue and the prepped reading list; the analyst does not know whether the
operator holds or wants this name. **Contamination declared:** the session context carried commit subjects naming other
runs' boxes (ETN, HUBB, ATKR, all electrical or conduit names, none a boat builder) and a memory index line with generic
queue counts; none mentions Malibu or a boat builder. `tools/run.py` prints v4 material; only its arithmetic lines were
read (Part VII). No other `Test Runs/` file about this company was opened, and none was searched for.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $22.54 (2026-10-05, Yahoo chart through `tools/sources.py`; aggregator, live quote only, flagged per operator
  rule 5). The 10-K states $29.47 on 2026-08-24. The fall of about 23% since then has no filed event behind it: the EDGAR
  submissions list from 2026-08-31 to 2026-10-05 holds only the proxy (no instance found of an 8-K in that span).
- **Shares by class** (10-K for FY ended 2026-06-30, filed 2026-08-27, accession `0001590976-26-000037`;
  `python Screens/cover_shares.py MBUU`): Class A 19,677,264; Class B 12. The charter note was read: the Class B shares
  carry votes only, "holders of our Class B Common Stock do not have any right to receive dividends or other
  distributions" (10-K Item 1), one share per pre-IPO owner, voting the LLC Units that owner holds. The economic claim of
  the Class B holders is their LLC Units, exchangeable one for one into Class A: 270,419 units at 2026-06-30 (10-K, the
  non-controlling interest note; 1.4% of the LLC). **Economic share count: 19,947,683** (Class A plus outside LLC Units;
  the 12 Class B shares are not added).
- **Market cap:** $449.6M at $22.54 on 19,947,683.
- **Sovereign for the earnings currency (USD):** 5.63%, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4), all saved as text in the working folder:
  - 10-K FY2026 `0001590976-26-000037` (Items 1, 1A summary, 2, 3, 5, 7 in full; balance sheet, cash-flow statement,
    notes 4, 18, 20 and the non-controlling interest note); 10-K FY2025 `0001590976-25-000080`; FY2024
    `0001590976-24-000073` (Batchelder verdict, Tommy's Boats, dealer concentration); FY2023 `0001590976-23-000069`;
    FY2022 `0001590976-22-000050`; FY2021 `0001590976-21-000065`; FY2020 `0001590976-20-000069`; FY2019
    `0001590976-19-000073`; FY2017 `0001590976-17-000118`; FY2015 `0001590976-15-000075` (market-share statements,
    acquisition prices, cash-flow lines).
  - IPO prospectus, 424B4 of 2014-01-31, `0001193125-14-031218` (selected data FY2011 to FY2013; market share 2008 to
    2013; the recession years). Malibu was private through 2009: the prospectus's selected data begin at FY2011, and no
    filed figure for FY2009 or FY2010 was found.
  - Proxy, DEF 14A of 2026-09-21, `0001590976-26-000067` (pay, bonus outcome, ownership).
  - 8-Ks: Saxdor purchase 2026-03-02 `0001590976-26-000010`; credit agreement 2026-07-13 `0001590976-26-000029`;
    director departure 2026-08-24 `0001590976-26-000031`; FY2026 results with EX-99.1 `0001590976-26-000035`; Saxdor pro
    forma EX-99.1 `0001590976-26-000040`; FY2025 results EX-99.1 `0001590976-25-000076`; officer changes
    `0001590976-23-000025` (CFO resigns, 2023-04), `0001590976-23-000120` (new CFO, 2023-11),
    `0001590976-24-000016` (CEO leaves, 2024-02), `0001590976-24-000055` (new CEO, 2024-07),
    `0001590976-24-000136` (President retires, 2024-11), `0001590976-25-000117` (CFO resigns, 2025-11).
  - The latest periodic report is the FY2026 10-K; the September-quarter 10-Q is not yet due. The March-quarter 10-Q
    (`0001590976-26-000017`) was not read separately; the 10-K covers its period.
  - Competitors, from their own filings: MasterCraft 10-K FY2026 `0001193125-26-387432`, FY2025
    `0000950170-25-111682`, FY2023 `0000950170-23-045222`, FY2021 `0001564590-21-046866`, FY2019
    `0001564590-19-034678`, FY2017 `0001558370-17-006982`; Marine Products 10-K CY2025 `0001104659-26-021478`;
    Brunswick 10-K CY2025 `0000014930-26-000027`; Polaris 10-K CY2025 `0001628280-26-008033`; XBRL company facts for all
    five (transcription, cross-checked below).
- **One figure cross-checked against the filed statement:** FY2026 net cash from operations $67,509 thousand in the filed
  cash-flow statement (`0001590976-26-000037`) = "$67.5 million" in the 10-K MD&A = 68 in `tools/run.py`. Also FY2024
  capital spending $75,962 thousand filed = 76 in `tools/run.py`.
- **`python tools/run.py MBUU`, arithmetic lines only.** Defects found and corrected against the filing: (1) the share
  basis is a weighted average, 19.3M, not the cover count plus the outside LLC Units (19.95M); (2) its stock pay omits
  "Non-cash compensation to directors" ($1.0M to $1.5M a year, a separate cash-flow line); (3) its "OE lo" column deducts
  depreciation and amortization of acquired intangibles, and its "OE hi" column deducts capital spending, so the labels
  describe neither method; (4) its balance-sheet table is first-filed XBRL and was read against the filed statements.

**Owner cash after every real cost, recast from the filed cash-flow statements** (operator rule 5; never a net-income
proxy). Cash from operations, less all stock pay (employees and directors), less all capital spending; the depreciation
variant beside it (Part VI, the PG specifics). $ thousands.

| FY (June) | Cash from operations | Stock pay (employees + directors) | Capital spending | Depreciation | **Owner cash (all capex)** | Depreciation variant |
|---|---|---|---|---|---|---|
| 2022 | 164,846 | 6,342 + 1,054 | 55,064 | 19,365 | **102,386** | 138,085 |
| 2023 | 184,733 | 5,894 + 1,136 | 54,840 | 21,912 | **122,863** | 155,791 |
| 2024 | 55,558 | 4,935 + 1,512 | 75,962 | 26,178 | **−26,851** | 22,933 |
| 2025 | 56,506 | 5,916 + 1,091 | 27,917 | 31,794 | **21,582** | 17,705 |
| 2026 | 67,509 | 5,603 + 1,041 | 24,663 | 33,147 | **36,202** | 27,718 |
| five-year mean | | | | | **51,236** | 72,446 |

What sits inside these years: FY2022 and FY2023 are the pandemic boom (net sales $1,214.9M and $1,388.4M against
$807.6M in FY2025). FY2024 carries the one-time $100.0M payment of the Batchelder product-liability settlement (accrued in
FY2023, paid in FY2024: 10-K FY2024 MD&A) and a $33.3M plant purchase inside capital spending. FY2026 carries $14.8M of
Saxdor acquisition and integration expense and four months of Saxdor. Taxes: cash from operations is after cash income
tax and after the tax receivable agreement payments ($758K in FY2026, $4,208K in FY2024, $3,974K in FY2023, inside
operations in the filed statement). Interest is inside it as well.

## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. For a
boat builder the honest answer turns on the cycle, and the rows say how to hold a cyclical: "what do we care if it’s
lumpy, as long as it’s a good business?" **[M2011-102]**, and over twenty years "there will be, you know, three or four
terrible years for residential housing" **[M2011-101]**. So the whole run turns on whether it is a good business, which is
Q2's question. The market serves and does not instruct: the fall from $29.47 to $22.54 in six weeks with no filed event
"just tells us prices" **[M2006-077]**. No macro forecast enters: the 10-K's outlook (soft retail, rates, tariffs) is
recorded and not used; "macro conclusions are — just never enter into the discussion" **[M2000-094]**; what counts is
"the average profitability of the business over time" **[M2015-016]**. Who is paid to tell you: the company's own
headline is adjusted earnings, and its officers are paid on adjusted EBITDA (both recorded below). The analyst's habits:
contrary evidence was written down as found **[M1997-127]**, looking for "what you’re missing" **[M2025-013]**, and the
other side's case is stated at its strongest before disagreeing **[M2016-055]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Gross margin 16.0% in FY2026 against 25.3% in FY2023 and 24.3% in FY2019, while net sales per unit rose to a record
   $184,990; the 10-K expects "promotional activity and dealer incentive costs, including floor plan interest support, to
   remain elevated relative to historical levels" (FY2026 MD&A, Outlook).
2. The 10-Ks from FY2017 to FY2024 claim the number one US share in performance sport boats; the FY2025 and FY2026 10-Ks
   drop the claim ("among the market leaders"). The last share disclosed is 30.5% for calendar 2023, after 33.0% (2016),
   32.7% (2019), 31.7% (2020), 30.5% (2021), 28.8% (2022) (10-Ks FY2017, FY2020 to FY2024).
3. FY2026, same June year-end: Malibu segment units 2,150 against 2,223 (−3.3%), with "increased dealer incentive costs
   per unit"; MasterCraft's ski/wake segment units 1,639 against 1,548 (+5.9%), with "decreased dealer incentives"
   (MasterCraft 10-K FY2026). MasterCraft's consolidated gross margin 22.9% against Malibu's 16.0%; in FY2019 the two
   were 24.2% and 24.3%.
4. Batchelder: a 2021 jury verdict of $80M compensatory and $120M punitive damages ($80M against Boats LLC, $40M against
   the predecessor West, whose assets Boats LLC bought in 2006), entered in full against Boats LLC, over a 2014 accident in
   a 2000 boat built by the predecessor; settled for $100.0M in June 2023 against insurance of $26M, of which $21M
   received; the suit against the insurer is on petition to the Georgia Supreme Court (10-K FY2024 note 17; FY2026 note 18).
5. Tommy's Boats, 10.7% of FY2023 sales: agreements not renewed and two terminated in FY2024; the dealer group went
   bankrupt; Malibu paid its estate $3.5M; its owner's suit is pending; a securities class action over statements from
   November 2022 to May 2024 about "inventory, demand and relationship with one of its former dealers" settled for $7.8M,
   funded by the directors-and-officers insurers, without admission (10-K FY2026 note 18).
6. Turnover at the top: CFO resigned April 2023; CEO left by "mutual" agreement in February 2024 with a two-year paid
   consulting term, continued vesting and a year's salary; President retired February 2025; the next CFO resigned November
   2025 after two years, again with continued vesting and a year's salary (8-Ks listed in Step 0).
7. Maverick Boat Group bought for $150.4M cash in FY2021; $88.4M of its goodwill and trade names written off in FY2024.
8. Owner cash did not grow from one cycle to the next: about $54.9M a year in FY2017 to FY2021 and $51.2M in FY2022 to
   FY2026 (computation below), while Cobalt ($130.0M, 2017), Pursuit ($100.1M, 2018) and Maverick ($150.4M, 2020) were
   bought and net sales averaged $608M in the first half against $1,031M in the second.
9. Unallocated corporate costs $28.4M (FY2024), $46.3M (FY2025), $51.0M (FY2026) (10-K FY2026 note 20).
10. Inventory against net sales: 12.3% (FY2023), 17.6% (FY2024), 17.6% (FY2025), 19.7% (FY2026, with Saxdor).
11. The FY2026 results release leads with "Adjusted net income per share" of $1.52 against GAAP $0.09; "professional
    fees" are added back to adjusted EBITDA in each of FY2024, FY2025 and FY2026.
12. The FY2026 bonus paid 100% of target: net income of $1.7M was adjusted to $15.1M for the bonus by removing Saxdor's
    results and the integration expense (proxy, CD&A).
13. Dealer concentration: top ten dealers 62.4% of FY2026 net sales (40.4% in FY2024); OneWater 22.3%.
14. In FY2026 the company bought back 1,243,996 shares for $33.9M (about $27.26 each) and issued 1,523,794 shares to
    the Saxdor sellers at $27.37 (10-K Item 5 and note 4).
15. The General Motors engine-block supply agreement for Malibu and Axis ends with calendar 2026 and is "currently
    negotiating an extension" (10-K Item 1).

**The other side's case, stated at its strongest** **[M2016-055]**: Malibu and Axis held the first or second US share in
performance sport boats every year from 2008, rising from 23.2% (2008, prospectus) to about 30% now; its Surf Gate
patents are licensed to Nautique, MasterCraft, Tige and Chaparral, who pay it royalties; net sales per Malibu-segment unit
rose from about $62,500 (company-wide, FY2013) to $145,538 (FY2026); Cobalt rose from 14.2% (2010) to 40.8% (2023) of
24- to 29-foot sterndrives; owner cash was positive in nine of the last ten years; the company came through 2009 and
gained share.

## THE STANDING RULE
Owning this unlevered, sized so that a fall of half or more harms nothing the buyer needs, risks nothing the buyer has and
needs **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The quote has fallen from
$91.9 (2021 high) to $22.54; a holder must be able to sit through that. The rule binds the buyer, not the company, and it
is met if no borrowing is used.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test, applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**. The key variables **[M1998-044]**: (1) average US retail demand for
  premium powerboats across a cycle; (2) the company's share and price premium in its categories; (3) its cost base,
  heavy in fixed cost ("We have a large fixed-cost base", the first risk factor); (4) what it buys. The product and the
  channel have not changed in forty years: fiberglass hulls, purchased or marinized engines, independent dealers financed
  by floor plan lenders (about 80% of US shipments in FY2026), retail buyers who mostly borrow. The company was founded in
  1982; NMMA and SSI have tracked its categories for decades.
- **Do the past statements tell the future ones** **[M2008-033]**? They show the same shape twice: operating margin 1.3%
  in FY2011 (net sales $99,984K, operating income $1,261K, prospectus), 17.6% at the FY2022 peak, 0.3% in FY2026
  ($3,099K on $914,590K). A cyclical's statements tell its shape; the level of its through-cycle earning power is the
  castle's question, Q2.
- **Change.** Not fast-moving technology. The named threats are slow: electric and alternative-fuel boats, used-boat
  preference, oversupply (risk factors). "slow change can be much harder to perceive" **[M2014-038]** is carried to Q2.
- **Can I name the winner, not just the industry?** In wake boats, Malibu and MasterCraft have been the two largest US
  shares since 2008 (prospectus table; MasterCraft 10-Ks). **The doubt, written down:** Saxdor (premium adventure
  dayboats, an emerging market in the 10-K's own words, 9.2% of FY2026 sales for four months) is a young brand in a new
  category. Its economics are a boat builder's selling through dealers, the same as the rest; whether its position will
  hold is a castle question. Q1 asks whether the economics and position can be foreseen at all, and Q2 what the foresight
  shows about the castle (framework, Q1, How the order is settled), so the doubt is carried to Q2 and not used to close
  here. If the doubt were about the kind of economics, "if you have doubts about something being into your circle of
  competence, it isn’t" **[M2002-092]** would close the file; it is not.
- **VERDICT: IN.** A boat builder's earning power over a cycle and its standing in its categories can be pictured from
  fifteen years of filed statements and the competitors' filings; the cycle is a property of the business, read as an
  average **[M2011-101]**, **[M2011-102]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and "How much do they depend on the genius of the lord in the
castle?" **[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The tests, each with its filing fact.**
1. **The key factors and their permanence** **[M1995-038]**. The 10-K names four: brands; patented features (Surf Gate,
   introduced 2012, first patented September 2013, offered on every Malibu and Axis model and on some Cobalt
   models); the dealer network; vertical integration (Monsoon engines since model year 2019, towers, trailers,
   wiring harnesses, tooling). Patents expire; the feature that made the wake-surf boom is licensed to the four largest
   rivals, who sell it on their own boats. "the improvement you get one day, your competitor gets the next day"
   **[M2004-053]**; "anything you do, your competitors can copy" **[M1996-017]**.
2. **Would it stand without the lord?** The 10-K (Item 7, New Product Development) calls new models and features
   essential to the value of the brands, aims at several new models every year, and gives a development cycle of up to
   two years. This is a business "where you have to stay smart" **[M1995-040]**;
   "A moat that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**. The leadership that
   rebuilt it has turned over completely since 2023 (contrary evidence, item 6).
3. **The money test** **[M2011-015]**. Could a funded attacker take wake-boat share? The record says share moves: Malibu
   itself went from 23.2% (2008) to 33.0% (2016) on product, past MasterCraft (23.8% in 2008, 21.5% in 2016, 19.2% by
   March 2025, MasterCraft 10-Ks), and has since drifted to about 30%. Brunswick entered wake boats under Heyday (Brunswick
   10-K, Boat segment brands). "usually if something can gain competitive advantage very quickly, you have to worry about
   them losing it quickly, too" **[M2002-050]**. MasterCraft calls ski/wake "relatively concentrated" (10-K FY2026), so
   the attackers are few and known.
4. **Pricing power and the prayer session** **[M2005-020]**. List prices rise every year ("year-over-year price
   increases"), and per-unit revenue is at a record, but in the downturn the price is held by dealer money: free flooring,
   rebates and "promotional activity" kept "elevated", and gross margin fell from 25.3% (FY2023) to 16.0% (FY2026). The
   industry downturn is common to all; what is not common is that in FY2026 MasterCraft cut dealer incentives and widened
   its gross margin 290 basis points while Malibu raised per-unit incentives and lost 180 basis points.
5. **Unit volume and share of mind.** Share 24.5% (2010), 33.0% (2016), 32.7% (2019), 31.7% (2020), 30.5% (2021), 28.8%
   (2022), 30.5% (2023), then not disclosed; the number one claim dropped from the FY2025 10-K on. Category retail units
   7,818 in calendar 2025 (10-K FY2026 table) against 13,100 in 2006 and 5,500 in 2012 (prospectus).
6. **The low-cost position.** No filing shows Malibu as the low-cost builder; vertical integration is aimed at cost and
   supply, and the FY2026 cost of sales per unit rose in every legacy segment. No instance found in the filings read of a
   cost comparison with a rival.
7. **The brand in the customer's mind, and against the intermediary.** The brands are asked for by name in their
   categories. But the dealer stands between: top ten dealers 62.4% of FY2026 sales, OneWater alone 22.3%, MarineMax
   expected above 10% of Saxdor. "the value of having the brand moves over to the retailer from the product itself"
   **[M2001-090]** to the extent the dealer is trusted more; "the brand is our protection against the intermediaries
   making all the money" **[M2019-041]**. The Tommy's Boats fight shows how far a dealer relationship can break.
8. **The low bid.** Wake-boat buyers do not buy on the low bid; the premium features are why they pay more. This test
   passes on the evidence of rising per-unit prices **[M2017-009]**.
9. **Ask the competitors** **[M1999-130]**. Only what they file: MasterCraft claims the #1 share by brand (19.2%,
   March 2025) because Malibu's share is split across two brands; no rival filing names Malibu as the one to beat or to
   short.
10. **Widening or narrowing?** **[M1999-108]**. Share: below its 2016-2019 level. Relative margin: at parity with
    MasterCraft in FY2019, below it in FY2025 and FY2026 on consolidated figures. Against that, consolidated figures mix
    Malibu's saltwater, sterndrive and Saxdor segments with MasterCraft's pontoon and fishing lines, and Malibu's own wake
    segment still earned a segment adjusted EBITDA margin of 16.2% in FY2026 ($50,674K on $312,907K) before depreciation
    and $51.0M of unallocated corporate cost, which is not comparable to MasterCraft's ski/wake segment operating margin
    of 7.9% ($21,538K on $271,177K) after its own allocations. The like-for-like comparison has not been made.
11. **What could destroy, modify or reduce it** **[M2000-014]**. Product liability that outruns insurance (Batchelder,
    contrary evidence item 4); a dealer channel concentrated in two consolidators; the slow threats (electric, used
    boats) **[M2014-038]**; the end of the GM block agreement. "one competitor is frequently enough to ruin a business"
    **[M2012-108]**.

**The competitor row** (same metrics, each company's own filing):

| Company (filing) | Gross margin FY2019 / CY2019 | Peak year | Latest | Operating margin latest | Note |
|---|---|---|---|---|---|
| Malibu (10-Ks FY2019, FY2023, FY2026) | 24.3% | 25.3% (FY2023) | 16.0% (FY2026) | 0.3% (FY2026); 2.7% (FY2025) | FY2011 operating margin 1.3% (prospectus) |
| MasterCraft (10-Ks FY2019, FY2023, FY2026) | 24.2% | 27.7% (FY2023) | 22.9% (FY2026) | −0.3% consolidated (merger costs, impairment); ski/wake segment 7.9% (FY2026), 8.6% (FY2025) | brand share 21.6% (Dec 2018) → 19.2% (Mar 2025) |
| Marine Products (10-K CY2025) | n/a in facts read | 2022-23 operating income $51.8M, $49.2M | 19.1% (CY2025) | 5.7% (CY2025) | CY2009: sales $39.4M, operating loss $19.2M; merged into MasterCraft May 2026 |
| Brunswick Boat segment (10-K CY2025) | n/a | n/a | n/a | 2.1% GAAP (CY2025); 4.1% (CY2024) | the engine and parts segments earn the group's margin |
| Polaris Marine (10-K CY2025) | n/a | 22.1% (CY2023) | 14.2% (CY2025) | n/a | pontoons; gross profit $72.5M on $512.4M |

Read together: every boat builder in the row earned high margins in 2021 to 2023 and thin ones now; the builders are
alike in the trough, which is the commodity sign **[M2004-053]**, and the one difference in the latest year runs against
Malibu (tests 4 and 10).

**Why TOO HARD, and not OUT or IN.**
- *The case for OUT:* share below its peak and undisclosed for two years, the number one claim dropped, a rival gaining
  units and cutting incentives in the same year Malibu lost units and raised them, gross margin below that rival's two
  years running, the key feature in every rival's boat, a castle that must be rebuilt every model year **[L2007-005]**.
  It did not carry because each fact is one or two years long, the margin comparison mixes unlike segments, and the rows
  sort a bad year by whether competitive superiority was "maintained", which turns a trough into "a cyclical problem, not
  a secular one" **[L1995-022]**. That sorting has not been done.
- *The case for IN:* fifteen years at or near the top of a concentrated category, rivals paying it royalties, prices per
  unit at records. It did not carry because the castle has not protected returns in either trough on the record (FY2011
  1.3%, FY2026 0.3% operating margin), and a moat is what "protects excellent returns on invested capital"
  **[L2007-004]**.
- What remains is a moat that is tenuous: "when we see a moat that’s tenuous in any way" ... "We don’t know how to
  valuate that, and therefore we leave it alone." **[M2000-019]**; the framework sends that to TOO HARD (Q2, What it rules
  OUT, Sent to TOO HARD) in the rows' three boxes, "in, out, and too hard" **[M2006-013]**.
- **The cause is WORK, not NATURE.** The deciding question is whether the wake-boat castle held from 2023 to 2026 in share
  and in price premium against MasterCraft. It is "important and knowable" **[M2006-076]**: registration share is
  measured and published by both companies from SSI, and both file segment data. The insiders write these numbers down
  every year, which is the test that separates the two causes **[M2000-105]**. The work is not done: the share for
  calendar 2024 and 2025 and the like-for-like segment comparison were not found in the filings read. "I haven’t done the
  work" **[M1994-026]**; the research pass below is written, not run.

**VERDICT: TOO HARD (WORK)**, with **[M2000-019]**, **[M2006-013]**, **[M2006-076]**, **[L1995-022]**.

---
## COMPUTATION — NOT A CLEARANCE
*The file closed at Q2. Everything in this section is arithmetic made at the owner's request, carries no entry language,
and clears nothing (operator rule 3). Q3 to Q10 are NOT REACHED.*

**1. The value range under the Part VI construction, applied literally.** Five-year mean owner cash $51.2M (table in
Step 0). The growth shown on aggregate owner cash, FY2022 to FY2026, four intervals: −22.9% a year. Ten years at that
rate, then zero nominal growth, at 5.63%: $171.7M; no growth throughout: $910.1M. To reach the common share: plus Saxdor at
its purchase price, $203.9M (10-K note 4; a business four months owned has no record, and carrying it at cost is generous,
since "the acquirer typically gives up more intrinsic value than it receives" **[L1994-015]**; CONVENTION, ours, for this
run); less net debt $90.6M (debt $165.0M, cash $74.4M, 2026-06-30); less the earnout's fair value $29.9M (MD&A). Net
claims adjustment +$83.4M; 19,947,683 shares. **Range $12.79 to $49.80 a share; top 3.9 times bottom.** By the Part VI
width rule this range would close Q7 TOO HARD: "the range must be so wide that no useful conclusion can be reached"
**[L2000-025]**.

**2. The boom inside the window, and how it was treated.** No instance found in v5 of a rule for a boom inside the
five-year window (a text search of `Framework/THE FRAMEWORK v5.md` for the words boom and peak finds only the Q3 caution
against "a cyclical peak in earnings" **[L1994-009]**). The literal growth rate above is measured from FY2022, a boom
year, so it is the kind of rate the rows distrust: "If either year was aberrational, any calculation of growth will be
distorted." **[L2005-003]**. The treatment used here, a CONVENTION of this run, confessed: (a) growth is measured cycle
to cycle, the FY2022-26 mean against the FY2017-21 mean (about $54.9M; FY2017-18 director pay not read, so slightly
high), which gives about −1.4% a year, taken as no growth; (b) the bottom end is the post-boom base: FY2024 to FY2026
with the $100.0M settlement taken out of FY2024 and charged back at $10.0M a year in each year (one such loss in the ten
years read), $33.6M a year, no growth. The top end is the five-year mean, no growth, $51.2M. **Boom-treated range
$34.14 to $49.80 a share (1.46 to one).** The depreciation variant, no growth, is $68.69 and is shown only because the
construction asks for it; capital spending ran above depreciation in FY2022 to FY2024, and the all-capex figure is used.

**3. The floor, and the conversion between pre-tax and after-tax.** The floor is about ten percent pre-tax on the price
paid (Part VI CONVENTION: "a very high probability of at least 10% pre-tax returns" **[L2002-020]**; "a point at which we
drop out of the game" **[M2003-149]**). Owner cash is after Malibu's own cash taxes, so the floor is converted at the
company's own effective rate, 24.8% (FY2025, 10-K; FY2026's 30.2% is distorted by a near-zero pre-tax base): 10% × (1 −
0.248) = **7.52% after tax**. The row itself converts at the corporate rates of its day, "(which translate to 6�-7% after
corporate tax)" **[L2002-020]** (the replacement character is the row's); using the company's rate is the stricter of
the two here. Expected return at a price = owner cash ÷ (market value less the +$83.4M claims adjustment), at no growth.

**4. The three numbers the owner asked for, all COMPUTATION (the file closed before Q7):**
- **Value range:** literal $12.79 to $49.80 (TOO HARD by width); boom-treated $34.14 to $49.80.
- **Fair-price band:** prices inside the boom-treated range at which the expected return on the five-year mean is at or
  above the floor: **$34.14 to $38.34.** On the post-boom base no price inside the range clears the floor.
- **Cheap price:** the price at which the post-boom base alone, with no growth, earns the floor: **about $26.61.** Below
  it even the pessimistic case of this computation is paid the floor without a pencil **[M2009-005]**.
- **Against the price of $22.54:** the price sits below the computed cheap price. At $22.54 the legacy business is priced
  at $366.2M; the five-year mean yields 14.0% after tax (18.6% pre-tax), the post-boom base 9.2% (12.2% pre-tax). This is
  arithmetic on a business whose castle is unproven. It means only that, if the research pass closed Q2 IN and Q3 to Q6
  cleared, price would not be what stopped it. What the arithmetic does not see: a 2009-type trough (no such year is in
  the window; Marine Products' sales fell to $39.4M with a $19.2M operating loss in CY2009), the trend of owner cash
  falling cycle to cycle while capital went in, and the claims of the tax receivable agreement ($38.7M payable, set
  against a $50.4M deferred tax asset; both left out as already inside the cash stream).

**5. The balance sheets, ten years, read before the income account** **[M2025-032]** (Q4 NOT REACHED; recorded as facts
for the research pass). $ millions, filed statements as transcribed by XBRL first vintage, checked against FY2026 and
FY2025 filed balance sheets:

| June | Equity | Goodwill + intangibles | Cash | Inventory | Inventory / sales | Debt | Retained earnings |
|---|---|---|---|---|---|---|---|
| 2018 | 134 | 126 | 62 | 44 | 8.9% | 108 | 28 |
| 2019 | 204 | 197 | 27 | 68 | 9.9% | 114 | 94 |
| 2020 | 255 | 191 | 34 | 73 | 11.2% | 83 | 154 |
| 2021 | 373 | 336 | 41 | 117 | 12.6% | 139 | 264 |
| 2022 | 503 | 329 | 84 | 157 | 12.9% | 118 | 421 |
| 2023 | 608 | 322 | 79 | 171 | 12.3% | 0 | 526 |
| 2024 | 530 | 227 | 27 | 146 | 17.6% | 0 | 470 |
| 2025 | 515 | 220 | 37 | 142 | 17.6% | 18 | 485 |
| 2026 | 524 | 375 | 74 | 180 | 19.7% | 165 | 486 |

What the figures say: (1) equity was built from retained earnings, which rose from $28M to $526M in five years and have
gone nowhere since (no dividend has ever been paid; buybacks of $29M to $36M a year are charged against paid-in
capital); (2) goodwill and intangibles are 71% of equity in FY2026, so tangible equity is about $150M, $7.50 a share; (3)
the $88M write-off of FY2024 took goodwill and intangibles down by nearly a third in one year; (4) inventory has risen against
sales every year since FY2023, which is the tell the rows name, "inventories look out of line, you know, with sales"
**[M1995-064]**, partly Saxdor (finished boats in Europe) and not separable in the filing; (5) receivables are small
because floor plan lenders pay within days, so the dealer's inventory, which the filing describes but does not count,
is off this balance sheet and inside the repurchase agreements (no repurchases in FY2026; 22 units in FY2025); (6) debt
was zero in FY2023 and FY2024 and is $165M now, refinanced on 2026-07-10 into a $100M term loan and a $250M revolver to
2031, with covenants on EBITDA to interest and debt to EBITDA. What they do not say: the dealer-channel inventory in
units, and Saxdor's own balance sheet before purchase (8-K/A of 2026-05-18, not read).

**6. Returns on capital, for the research pass** (Q3 NOT REACHED). Operating income over tangible capital employed
(equity plus debt less cash, goodwill and intangibles): about 116% (FY2018), 99% (FY2019), 72% (FY2020), 105% (FY2021),
98% (FY2022), 67% (FY2023), 12% (FY2024 before the impairment), 8% (FY2025), 1% (FY2026). Over total capital including
what was paid for acquisitions, the FY2018-26 average is about 18% pre-tax. The rows' caution applies to the early years:
rule out "a cyclical peak in earnings" **[L1994-009]**; and to the second half: "We just put way more capital into the
business as we went along" **[M2023-081]**.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (the file closed at Q2). Facts for the research pass are in the computation section, items 6 and 2(a).

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read (computation section, item 5) because owner cash required them; no verdict is
given. Recorded for the research pass: adjusted earnings lead the results release (contrary evidence, item 11), and the
rows name that as a tell, "a management that regularly attempts to wave away very real costs" **[L2016-006]**; whether a
second tell is present (Q4, the two-tell line) is not decided here.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. No Q5 output is reported (operator rule 2). The facts found are in the contrary-evidence list, items 4, 5, 6,
12 and 14.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The arithmetic the owner asked for is in the COMPUTATION section above and clears nothing.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Recorded for the research pass: "we have passed up some businesses, because we were worried about the
product liability potential" **[M2001-008]**; Batchelder is that potential realised once, at four times the insurance.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing until the research pass closes; inaction is the default.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Recreational boats are not among the named businesses.)

---
## THE BOX
**TOO HARD (WORK), decided at Q2.** The castle in wake boats is real on the fifteen-year record and tenuous on the last
three; whether it held from 2023 to 2026 in share and price premium is knowable and not yet known. Q7 not reached; the
COMPUTATION, not a clearance, puts the value at $34.14 to $49.80 a share boom-treated ($12.79 to $49.80 literal),
against $22.54. A research file is owed (Part VII); its steps 1 and 2 are written below and not run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written section by section. **Not committed:** this run's instruction
      forbids commits; the write-early commits of the template were not made.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, see the end of this file); every filing fact
      has its accession in Step 0 or beside it; every number has a row, a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the file; nothing after it is a clearance, and the computation is headed as such.
- [x] Owner cash after every real cost from the filed cash-flow statements, directors' stock pay included, never a
      net-income proxy; the sovereign from the Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (fifteen items, before the Q1 verdict).
- [x] No point-in-time anchor; rows of every year may be cited.
- [x] Only the arithmetic lines of `tools/run.py` were used, and four defects in them were corrected against the filing.
- [x] `python tools/check_framework.py` run after writing; result recorded at the end of this file.
- [ ] The position note could not be filled (blind rule). Declared above.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A boom inside the five-year window has no rule.** The brief for this run pointed to one in Part VI; a text search of
v5 for the words boom and peak finds none. The Part VI construction measures the growth shown over the window from
its first year of the window, which here is the pandemic peak, so the literal rate is −22.9% a year
and the range is 3.9 to 1 (TOO HARD by width), while a cycle-to-cycle reading gives no growth and a range of 1.46 to 1. The
choice of base year decides the box at Q7, which is exactly the distortion **[L2005-003]** warns of; the convention
should say how a cyclical's base years are chosen. What was done: both shown, the cycle-to-cycle variant confessed as a
CONVENTION of this run. (2) **Pre-tax floor, after-tax cash.** The floor is about ten percent pre-tax (Part VI) while owner
cash is after tax, and the two rows behind the floor disagree on which it is: one speaks of "discounting future
after-tax streams of cash at at least a 10 percent rate" **[M1994-004]**, the other of "10% pre-tax returns"
**[L2002-020]**, which it translates to a lower after-tax figure. The convention does not say which; this run converted at the company's own tax rate and states
it. (3) **Claims ahead of the common share** (an Up-C structure with LLC Units, a tax receivable agreement, an earnout)
and **a business bought months ago** have no rule in the Q7 construction; both were handled ad hoc and confessed. (4)
**A multi-brand operating company** is not a holding company, yet its segments differ in castle; the by-parts convention
of Q1 does not say whether it reaches segments. (5) **Q2 has no rule for evidence that leans one way for two years.** OUT
needs a castle shown on the evidence to be filling in, TOO HARD a future that cannot be judged; a short run of adverse
facts with an unsorted cyclical cause falls between them, and only **[L1995-022]**'s sorting test gives a way through,
which makes it WORK. (6) The template's position note requires `PORTFOLIO.md`, which the blind rule forbids, and its
self-audit requires commits, which this run's instruction forbids.

---
## RESEARCH PASS, STEPS 1 AND 2 (written, not run; Part VII; CONVENTION in its form)

**Step 1. "What do I not know that I need to know?"** **[M1999-129]**, each marked knowable or not **[M2006-076]**.
- **R1 (deciding).** Did Malibu and Axis together hold their share of US performance sport boat registrations in calendar
  2024 and 2025? KNOWABLE: SSI registration data, cited by Malibu through FY2024 and by MasterCraft every year.
- **R2 (deciding).** Did the Malibu segment keep its profit premium over MasterCraft's ski/wake segment, measured the same
  way, from FY2019 to FY2026? KNOWABLE: both companies file segment results for years ending June 30.
- **R3.** Did Cobalt hold its share of 24- to 29-foot sterndrive registrations after 2023 (40.8%), in a category of 4,086
  retail units in 2025? KNOWABLE, same sources as R1.
- **R4.** Will wake-surfing restrictions on inland lakes, or electric propulsion, change the category's economics within
  twenty years? NOT KNOWABLE as a forecast; recorded and set aside under refinement (c) of Part VII; it does not decide the
  pass.
- **R5.** Is the product-liability tail now insured at a level that would cover a second Batchelder? KNOWABLE in part
  (10-K insurance disclosure, Chubb litigation record). A Q9 question; it does not decide Q2.

**Step 2. For each knowable question: the evidence, span and source fixed now, and the single fact that closes OUT**
**[M1998-144]**.
- **R1.** Span: calendar 2016 to 2025. Source: Malibu 10-Ks FY2017 to FY2026 and every 8-K EX-99 investor presentation
  of FY2025 and FY2026; MasterCraft 10-Ks FY2025 and FY2026 SSI statements; NMMA retail data. **OUT fact:** Malibu and
  Axis combined US performance sport boat share for calendar 2025 below 28.8%, its 2022 figure and the lowest it has
  disclosed since 2011.
- **R2.** Span: fiscal years 2019 to 2026. Source: the segment notes of the Malibu and MasterCraft 10-Ks for those years
  (Malibu segment adjusted EBITDA and net sales; MasterCraft ski/wake segment operating income plus that segment's
  depreciation where disclosed, and net sales). **OUT fact:** the Malibu segment's EBITDA margin for FY2026, computed on
  the same definition as MasterCraft's segment, at or below MasterCraft's ski/wake segment EBITDA margin for FY2026.
- **R3.** Span: calendar 2016 to 2025. Source: as R1. **OUT fact:** Cobalt's share of 24- to 29-foot sterndrive
  registrations for calendar 2025 below 35.2%, its 2021 figure.
- **R5.** Span: FY2023 to FY2026. Source: 10-K insurance and legal notes; the Georgia appellate record in the Chubb suit.
  **OUT fact** (for Q9, not Q2): product-liability cover limit after FY2024 at or below $26M per occurrence.

The pass closes IN, OUT or TOO HARD (NATURE), never TOO HARD (WORK) a second time on the same question **[M2008-086]**.
The pass never widens the circle to find something to buy **[M1995-018]**.

---
## CHECKS RUN AFTER WRITING
- `python tools/check_framework.py`, run 2026-10-05 after this file was written: **PASS** (exit 0; the run-file scan
  reports phantom ids in 0 files). Output saved as `Test Runs/_research 2026-10-05 MBUU/check_framework_output.txt`.
- `Test Runs/_research 2026-10-05 MBUU/check_ids.py`: 75 citations of 55 distinct v5 ids, every one present in
  `principle_ledger_v5.csv`; no E-ids (v4) cited; every double-quoted fragment standing before an id found in that row
  (apostrophes and quotation marks normalised, `[...]` honoured): 45 checked, 0 unmatched. Quotations from filings are
  kept out of sentences that carry an id, or paraphrased with the filing named.
