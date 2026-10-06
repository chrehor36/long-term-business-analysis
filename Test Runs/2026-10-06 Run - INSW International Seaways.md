# Company Run: International Seaways, Inc. (NYSE: INSW), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated name before any fetch. Every judgment cites a v5 ledger id in
bold; every filing fact carries its accession; the first STOP that failed closed the run and later questions are marked
NOT REACHED. Working folder: `Test Runs/_research 2026-10-06 INSW/` (fetch and parse scripts, the converted filings,
`owner_cash.py`, `per_day.py`, `peer_series.py`, `cited_rows.txt`).

**POSITION NOTE, declared before any verdict:** not known to this analyst. `PORTFOLIO.md` and every holding review are
barred by the blind rule of this run's brief, so the template's check was not made. The run is written as for a name
not held.

**CONTAMINATION DECLARED.** (1) The session context showed recent commit subjects for other names (NWL OUT at Q2, MD OUT at
Q2, COLL OUT at Q1, MHO OUT at Q2, an S&P 600 session-state note) and untracked run files for LRN, MTCH and NX; the
directory listing of `Test Runs/` showed research folders for other names of 2026-10-05 and 2026-10-06 (ADT, ASO, BCC,
BTU, GPOR, PTEN, WKC and others). None was opened. (2) The memory index in the session context says the watchlist has
"57 gate-clearers, nothing buyable"; it names no ticker and bore on nothing here. (3) `tools/run.py` printed its v4-era
"OWNER EARNINGS" block and three numbered lines; only its arithmetic lines were read, and its capex line is wrong for
this filer (Step 0). (4) No file about INSW in `Test Runs/` was looked for or opened; a `grep` of the directory listing for
the ticker returned nothing.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $116.60, close 2026-10-05, from `tools/run.py` (aggregator, live quote only, flagged per operator rule 5).
- **Shares:** 49,531,311, single class, from the cover of the 10-Q for the period ended 2026-06-30, filed 2026-08-10,
  accession `0001104659-26-093061` (`python Screens/cover_shares.py INSW`). Balance sheet at 2026-06-30: 49,520,476
  issued and outstanding (same 10-Q).
- **Market cap:** 49.531M x $116.60 = **$5,775M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 2026-10-05
  (issuing authority, as printed by `tools/run.py`).
- **Filings read (operator rule 4):**
  - 10-K FY2025, filed 2026-02-26, `0001104659-26-020113` (business, risk factors, MD&A segment tables, statements,
    vessel roll-forward, dividends).
  - 10-Q Q2 2026, filed 2026-08-10, `0001104659-26-093061`; 8-K with Q2 2026 results, `0001104659-26-093033` (ex. 99.1).
  - DEF 14A filed 2026-04-29, `0001140361-26-017661` (summary compensation; rights plan).
  - INSW 10-Ks FY2016 `0001144204-17-017875`, FY2017 `0001144204-18-013984`, FY2018 `0001144204-19-013398`,
    FY2019 `0001558370-20-001928`, FY2021 `0001558370-22-002682`, FY2022 `0001558370-23-002247`, FY2023
    `0001558370-24-002108` (cash flows, segment tables, the 2018 VLCC purchase, the 2021 Diamond S merger).
  - Overseas Shipholding Group 10-Ks: FY2009 `0001144204-10-010646`, FY2012 (filed 2013-08-26) `0001144204-13-047751`,
    FY2013 `0001144204-14-015316` (International Flag segments 2007-2013; the Chapter 11 filing; the restatement).
  - Competitors' annual reports: Frontline 20-F FY2025 `0001628280-26-021774` and FY2019 `0001628280-20-003843`; DHT
    20-F FY2025 `0001140361-26-010407` and FY2019 `0001140361-20-006806`; Scorpio Tankers 20-F FY2025
    `0001483934-26-000021` and FY2019 `0001483934-20-000011`; Teekay Tankers 20-F FY2025 `0001419945-26-000007` and
    FY2019 `0001628280-20-004971`; Ardmore 20-F FY2025 `0001104659-26-024690` and FY2019 `0001104659-20-043130`.
    Their net income and equity series 2016-2025 were taken from the SEC company-facts XBRL (transcription, flagged).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $380,052
  thousand on the filed cash flow statement (10-K FY2025, p. 75), equals the tagged 380.1M that `tools/run.py` used.
- **`tools/run.py` arithmetic, checked line by line against the filing:**
  - OCF 2023-2025 (688.4, 547.1, 380.1), SBC (8.5, 9.0, 8.7) and D&A (129.0, 149.4, 163.6): match the statements.
  - **Its capex line is wrong for this filer.** It read `PaymentsToAcquireOtherPropertyPlantAndEquipment` ($1.5M, $1.4M,
    $1.4M), which is the line "Expenditures for other property". The vessel line, "Expenditures for vessels, vessel
    improvements and vessels under construction", was $205.2M, $278.8M and $340.5M, offset by vessel sale proceeds of
    $66.0M, $71.9M and $246.3M. Its "OE capex" mean of $528.4M and its "yield 9.15%" are therefore void; the corrected
    figures are in the owner-cash table below. Its "OE D&A" basis also double counts drydock (drydock payments are
    already inside OCF and drydock amortization is inside D&A); the D&A basis below adds drydock payments back.
  - Its balance-sheet table matches the filed balance sheets for the years spot-checked (2016, 2021, 2025).

### The balance sheets, ten year-ends before the income account **[M2025-032]**
Read because the file closes before Q4 (the template's instruction). USD millions; filed balance sheets in the 10-Ks
listed above; book value per share uses the year-end shares on each balance sheet.

| year-end | equity | shares (M) | book/share | retained earnings | debt on the face | cash (+ST deposits) | voyage receivables |
|---|---|---|---|---|---|---|---|
| 2016 | 1,180 | 29.19 | $40.41 | -74 | 440 | 92 | 67 |
| 2017 | 1,086 | 29.09 | $37.32 | -181 | 553 | 60 | 58 |
| 2018 | 1,010 | 29.18 | $34.61 | -269 | 811 | 58 | 95 |
| 2019 | 1,022 | 29.27 | $34.92 | -270 | 661 | 90 | 84 |
| 2020 | 972 | 28.01 | $34.70 | -276 | 536 | 199 | 43 |
| 2021 | 1,170 | 49.61 | $23.58 | -409 | 1,105 | 98 | 107 |
| 2022 | 1,488 | 49.12 | $30.29 | -21 | 1,023 | 244 (+80) | 290 |
| 2023 | 1,717 | 48.93 | $35.09 | 227 | 723 | 127 (+60) | 247 |
| 2024 | 1,856 | 49.19 | $37.73 | 359 | 688 | 158 | 186 |
| 2025 | 2,020 | 49.40 | $40.90 | 524 | 567 | 117 (+50) | 178 |
| 2026-06-30 | 2,265 | 49.52 | $45.74 | 773 | 646 | 159 (+250) | 307 |

What the figures say, and what they cannot say **[M2025-032]**:
- **Book value per share went nowhere for nine years.** $40.41 at the spin (2016) and $40.90 at 2025, with about $17.70
  a share of dividends paid in 2020-2025 between them (dividends paid $854.7M over 2020-2025 on the cash flow
  statements, divided by each year's weighted shares). The whole per-share gain of the period is the 2022-2025 boom;
  2016-2021 lost two-fifths of book per share ($40.41 to $23.58).
- **The 2021 merger halved the per-share book at the trough.** 22,536,647 shares were issued for Diamond S (44.25% of
  the combined company); the consideration was $360.0M, about $16 a share, against INSW's own book of $34.70 a share at
  the end of 2020 (10-K FY2021, Note 2). Diamond S's net assets at appraised value were $659.0M, and $330.0M of that was
  written off the vessels under asset-acquisition accounting, so the 2021 book understates the fleet.
- **Retained earnings were negative from the spin to 2022**, after $402M of dividends paid to OSG in 2015-2016 before
  the spin (10-K FY2016 cash flows) and vessel write-downs of $303.5M in 2016-2024 (79.2, 88.4, 19.0, 103.0, 3.5, 1.7,
  8.7; cash flow statements).
- **Debt peaked at $1,105M in 2021** and has been paid down to $567M (2025), with a $250M 7.125% unsecured bond due 2030
  issued in 2025; the trough years carried 10.75% subordinated notes (10-K FY2018). Sale-and-leaseback financings of
  $447M (2021), $108M (2022) and $170M (2023) are inside the debt line.
- **Receivables move with the freight rate**, not with sales effort: $43M in 2020, $290M in 2022, $307M at mid-2026.
  Inventories are bunkers, trivial except when vessels trade voyage charters (2026).
- **What the balance sheet cannot say: the ships' market value.** Vessels are carried at depreciated cost less past
  impairments. The filer's own net loan-to-value ratios (12.9% at 2025, net debt $400M; "approximately 6%" at mid-2026,
  net debt $236M) imply a fleet worth about $3.1B at 2025 and roughly $3.6B-$4.3B at mid-2026, against a carrying value
  near $2.2B. That market value is itself a function of the freight rate of the day.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be happy owning it "if the market closed for five years" **[M1997-109]**,
and a tanker owner's price today ($116.60, more than double its book of $45.74) is set by a freight market at a record:
Q2 2026 crude TCE was $108,927 a day and product TCE $56,226 (10-Q Q2 2026). The market "just tells us prices" **[M2006-077]**.
No macro view enters: "just never enter into the discussion" is the rule **[M2000-094]**, and the
speakers know of no one with "an edge in trying to do that over the next 10 years" for oil and its kin **[M2011-047]**.
So the run does not ask where tanker rates go; it asks what the business earns across the rates it has had.
**Contrary evidence, written down as found [M1997-127]:**
1. The boom is real cash, not paper: owner cash in the first half of 2026 alone was about $505M (OCF $408.7M, less SBC
   $3.0M, less vessel spending $123.3M, plus vessel sales $222.4M), roughly $10.20 a share in six months, and dividends
   of $11.75 a share were declared in 2026 through August. If the boom ran two more years, the owner would be paid a
   large part of the price back.
2. Management has bought low and sold high at least twice on the record: six VLCCs bought in 2018 for $434M at the
   trough (10-K FY2018), Diamond S merged at the 2021 trough, and seven old ships sold in Q1 2026 for $216M with $88M of
   gains (8-K, Q2 2026). This is the one possible route through a commodity field that is not the low-cost position
   (Q2, below).
3. The speakers themselves bought cyclical commodity assets at a price: cement is "an understandable business" and "at a
   price, you know, for low-cost capacity and advantageously located raw materials and so on, you know, we would do it"
   **[M2001-059]**; of brick, "if I can buy the assets cheap enough to participate in those 20 years, that we’ll do OK"
   **[M2011-101]**.
4. INSW's return on equity over 2017-2025 (11.2%) is above two of its five peers (Q2 competitor row).

## THE STANDING RULE
No borrowing, no options and no position size were proposed; the run buys nothing. A purchase with borrowed money is
ruled out by "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Nothing here puts the buyer at risk
of ruin.

---
## Q1: CAN I UNDERSTAND IT? STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years", with "some notion of how the industry will develop and where the company will stand within
  the industry" **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**. The product need not be mastered;
  what matters is to "understand the economic dynamics of the industry", "are there competitive moats? Is there ease of
  entry?" **[M2011-014]**.
- **The business, from the filing.** INSW owns and operates 70 crude and product tankers (8.4M dwt) with four LR1s on
  order at end-2025, weighted average age 10.9 years; it earns spot rates through six commercial pools (82% of 2025
  TCE revenue from spot) and a small lightering business (10-K FY2025, Item 1).
- **The key variables and how predictable they are [M1998-044].** The freight rate (set by the fleet in the water and on
  order against ton-mile demand) and vessel prices. Year by year they are not predictable: crude TCE ran $14,699
  (2013), $49,619 (2023), $15,986 (2021) and $108,927 (Q2 2026). What is predictable for ten years is the structure:
  the tanker is the same product it has been for decades, the ownership is fragmented, entry is a shipyard order, and
  the owner takes the market rate. Commodity freight is a supply-and-demand price "on any kind of commodity like that,
  supply and demand is what determines prices over time" **[M2007-056]**.
- **Routing.** This is not a business of rapid change that closes here TOO HARD **[L1993-023]**; its change is slow
  (fuel, emissions rules, an energy transition measured in decades). The speakers call a cyclical commodity with
  overcapacity periods "an understandable business" **[M2001-059]**, and say of a cyclical business that the order of
  good and bad years need not be known **[M2011-101]**. The economics can be foreseen in kind: a price-taker in a
  fragmented market whose earnings swing with the rate. What that foresight shows about the castle is Q2's question.
- **VERDICT: IN**, on the understanding of the economic dynamics **[M2011-014]**, **[M2012-065]**, with the year-by-year
  rate recorded as not predictable **[M1998-044]** and carried to Q2 and Q7.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing" **[M1995-038]**.

- **The castle questions and the low bid (tests 1 and 8).** The filer answers them itself, in its own words (10-K
  FY2025, Item 1, Competition, and Item 1A): *In the spot market, competition is based primarily on price, cargo quantity
  and cargo type*; and *because ownership of the world tanker fleet is highly fragmented, no single vessel owner is able
  to influence charter rates.*
- That is the commodity of the rows: a product "available from many suppliers" where "most
  insureds don't care from whom they buy", "Think airline seats." **[L2004-003]**.
- **The attacker with money (test 3).** Anyone with money can order a tanker; the filer reports the tanker orderbook
  rose 23.6M dwt in 2025, VLCCs alone 19.0M dwt (10-K FY2025, MD&A). The rows' failing answer is the airline: "you can
  create another airline" ... "Very easily, and you have people that like to do it." **[M2013-054]**. The supply side
  behaves as gypsum did, where managements "like to build new plants" and too much capacity followed: "they like to
  build new plants" **[M2017-043]**.
- **Pricing power (test 4).** None: the rate is the pool's or the spot market's. The rows' picture is the gas station,
  "whatever he charged for gas was my price" (with "I didn’t have much choice") **[M2012-109]**; and two competitors can
  still "beat each other’s brains out" **[M2013-052]**.
- **The low-cost position (test 6), the one exception for a commodity.** "Another way to prosper in a commodity-type
  business is to be the low-cost operator" **[L2004-007]**; "being the low-cost producer is all-important" **[L2000-017]**;
  "commodity businesses have risk unless you’re the low-cost producer" is the 1997 form **[M1997-010]**; the cost is
  measured against the competitor, "if your costs are on parity or less" **[M2001-013]**, and read off the filings:
  "The figures are available." **[M2009-059]**. The evidence:

**The competitor row.** Same metric from each company's own filings.

| | metric | INSW | peers | source |
|---|---|---|---|---|
| Product tankers, 2019 | vessel opex per owned/bareboat day | $8,136 | Scorpio $6,563 (consolidated; MR $6,312); Ardmore $6,562 | INSW 10-K FY2019; STNG 20-F FY2019 `0001483934-20-000011`; ASC 20-F FY2019 `0001104659-20-043130` |
| Product tankers, 2025 | same | $8,900 | Scorpio $8,018 (MR $7,619; LR2 $8,743); Ardmore $7,615 | INSW 10-K FY2025; STNG 20-F FY2025; ASC 20-F FY2025 |
| Crude tankers, 2019 | same | $9,505 (VLCC to Panamax mix, lightering costs inside) | DHT $7,948 (VLCCs: $78.3M over 9,855 operating days) | INSW 10-K FY2019; DHT 20-F FY2019 `0001140361-20-006806` |
| Return on average equity 2017-2025 | net income / mean equity (XBRL, flagged) | 11.2%, losses in 5 of 9 years | Frontline 14.2% (3 loss years); Teekay Tankers 11.9% (3); DHT 10.1% (2); Scorpio 8.5% (4); Ardmore 8.1% (5) | company-facts XBRL of each filer |
| The trough, 2019 and 2020 | return on equity | -0.1%, -0.6% | Frontline 10.5%, 26.4%; DHT 8.2%, 26.1%; Teekay Tankers 4.3%, 8.4% | same |
| The boom, 2022-2025 | return on equity, mean | 25.1% | Teekay Tankers 25.9%; Frontline 22.4%; Scorpio 21.0%; Ardmore 20.7%; DHT 14.6% | same |

INSW's own opex per day, vessel expenses over owned plus bareboat-in days, from the segment tables (OSG's International
Flag segments before 2014, INSW after; the fleets changed, so the series is not like for like):

| | 2007 | 2008 | 2010 | 2012 | 2014 | 2016 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| crude $/day | 8,087 | 10,200 | 8,851 | 8,521 | 7,658 | 9,594 | 9,394 | 9,505 | 10,324 | 9,464 | 9,830 | 10,878 | 11,849 | 11,550 |
| product $/day | 7,567 | 8,098 | 7,456 | 6,568 | 6,992 | 7,626 | 7,850 | 8,136 | 8,590 | 7,954 | 8,143 | 8,974 | 8,997 | 8,900 |
| crude TCE $/day | 34,352 | 52,344 | 23,506 | 15,076 | 19,836 | 29,853 | 17,780 | 26,765 | 38,509 | 15,986 | 34,724 | 49,619 | 41,345 | 42,510 |
| product TCE $/day | 20,454 | 22,803 | 14,402 | 11,614 | 12,544 | 14,206 | 10,594 | 15,652 | 20,745 | 10,842 | 30,221 | 33,518 | 31,846 | 24,787 |

Reading the row over the whole span, not one year: INSW's product-tanker cost per day was 24% above Scorpio's and
Ardmore's in 2019 and 11% to 17% above them in 2025; its crude cost per day in 2019 was 20% above DHT's, though DHT's
fleet was all VLCCs, the costliest class to run. Its equity return across 2017-2025 is in the middle of six, and in the
two years when the market was ordinary (2019-2020) it earned nothing while Frontline and DHT earned 8% to 26%. Its
ten-year opex per day rose from about $9,500 to $11,550 (crude) and $7,600 to $8,900 (product). It is not the low-cost
operator on any measure the filings allow. Two cautions, written down: INSW's crude line carries the lightering
business's costs, and the peers' fleets differ in class and age; neither caution reverses the product-tanker comparison,
where the classes are close and INSW is dearest in both years.
- **The predecessor's record.** OSG's International Flag segments lost money from vessel operations in 2011 (crude
  -$71.0M, product -$42.0M) and 2012 (crude -$70.9M, product -$59.1M), carrying $270M to $286M of charter-hire a year; OSG and 180
  subsidiaries filed Chapter 11 on 2012-11-14, after the audit committee found errors in twelve years of statements over
  a Section 956 tax exposure the company put at up to $460 million ("$460,000", in thousands) (OSG 10-K FY2012, `0001144204-13-047751`).
  INSW's 2014 carve-out cash flow carries $285.3M of "Bankruptcy claim payments" (10-K FY2016). The castle did not stand
  through the last full downturn under the same fleet's owner.
- **The other route, "ebb-and-flow" [L2004-007].** The row says "Another way", so the low-cost position is not the only
  route; it names "an ebb-and-flow business model" for an insurer. INSW's buying in troughs and selling at peaks (contrary
  evidence 2) is the nearest analogue. It is not shown on the record: across 2017-2025 the equity return is not above
  the field, and the per-share book did not grow from 2016 to 2025 before the dividends (Step 0). The rows give no test
  for this route beyond the one row, so it is recorded and not credited.
- **Widening or narrowing (test 10), and what could destroy it (test 11).** There is no moat to widen; the position
  is the age and cost of the fleet, rebuilt by buying ships at the market's price, "A moat that must be continuously
  rebuilt" in the words of **[L2007-005]**. What can reduce it is supply: the 2025 orderbook and the record rates of 2026
  that will call more ships out of the yards, the gypsum pattern above **[M2017-043]**, and in the rows' plainest form,
  "supply has gone up and demand has not gone up" **[M2016-010]**.
- **Price does not reopen it.** "What you can’t do is turn any investment into a good deal by paying little" is the
  rule **[M2019-015]**; marginal businesses bought cheap "are the wrong foundation" **[L2014-009]**. The pull of
  **[M2001-059]** and **[M2011-101]** the other way is carried to the last section.
- **VERDICT: OUT.** The castle is shown open on the evidence: a commodity freight service sold on price by a price-taker
  **[L2004-003]**, **[M2013-054]**, whose costs are above its competitors' over the span **[M2001-013]**, **[M1997-010]**, in a
  business where "a company must lower its costs to competitive levels or face extinction" **[L1994-035]**. The money test
  answers yes, and "If the answer had been yes" the rows do not buy **[M2011-015]**. The box is "out", not "too hard"
  **[M2006-013]**: the castle's future is not unjudgeable; it is judged, and found open.

---
## Q3 to Q12: NOT REACHED
The run closed at Q2. Nothing below is a clearance; every number is arithmetic for the owner's request.

## COMPUTATION - NOT A CLEARANCE
*(The protocol's heading is written with a hyphen in place of the dash, under the standing no-dash rule.)*

### Owner cash, every year of the record, after every real cost
CONVENTION of this run: owner cash = operating cash flow (already after drydock payments) less stock pay, less vessel and
other-property spending, plus vessel sale proceeds, less vessel purchases financed by assumed debt (2018: $311.0M, the
six VLCCs, non-cash investing per the 10-K FY2018). Rationale: the ships are the capital and their sale proceeds return
it **[L1999-024]**, **[M2014-068]**; a ship bought with assumed debt is capital spent even though no cash moved that year.
Vessels bought for shares (Diamond S 2021, $329.0M; $36.8M of shares for vessels in 2024) are carried in the share
count, not deducted. 2014 OCF adds back $285.3M of OSG bankruptcy claim payments. The D&A basis = OCF + drydock
payments - SBC - D&A. USD millions; per share on weighted basic shares.

| year | OCF | capex basis | D&A basis | capex basis / share | D&A basis / share | net income |
|---|---|---|---|---|---|---|
| 2014 | 62.0* | 118.3 | -11.4 | 4.05 | -0.39 | -119.1 |
| 2015 | 260.2 | 273.5 | 196.4 | 9.37 | 6.73 | 173.2 |
| 2016 | 129.0 | 123.3 | 55.6 | 4.22 | 1.90 | -18.2 |
| 2017 | 17.4 | -142.0 | -43.9 | -4.86 | -1.50 | -106.1 |
| 2018 | -12.5 | -307.4 | -83.6 | -10.56 | -2.87 | -88.9 |
| 2019 | 87.5 | 61.8 | 27.0 | 2.12 | 0.92 | -0.8 |
| 2020 | 216.1 | 233.0 | 161.8 | 8.18 | 5.68 | -5.5 |
| 2021 | -76.2 | 0.1 | -131.0 | 0.00 | -3.32 | -134.7 |
| 2022 | 287.8 | 263.6 | 214.0 | 5.34 | 4.33 | 387.9 |
| 2023 | 688.4 | 539.2 | 585.4 | 11.00 | 11.95 | 556.4 |
| 2024 | 547.1 | 329.8 | 447.3 | 6.69 | 9.07 | 416.7 |
| 2025 | 380.1 | 275.8 | 292.0 | 5.59 | 5.92 | 309.3 |
| H1 2026 | 408.7 | 504.8 | 358.8 | 10.20 | 7.25 | 581.1 |

\* 2014 OCF as restated in the 10-K FY2018 selected data (-$223.3M) plus the $285.3M bankruptcy payments.

Means per share: five-year window 2021-2025, **$5.73** (capex basis) and **$5.59** (D&A basis); ten years since the
spin 2016-2025, **$2.77** and **$3.21**; twelve years 2014-2025, **$3.43** and **$3.20**. The five-year window holds one
trough year and the 2022-2025 boom; it also excludes H1 2026, the best half-year in the record. Tax: income tax was a
benefit of $0.4M in 2025 and a charge of $3.9M in 2023 (statements of operations), so pre-tax and after-tax owner cash
are the same for this filer. Maintenance: the filing gives no maintenance figure; the fleet's average age held near 10
to 11 years only by buying ships, so the whole vessel spend net of sales is treated as needed to stand still
**[L1999-024]**, and the depreciation basis is shown beside it.

### (a) VALUE RANGE, per the Q7 convention, and the whole-cycle variant
- **Growth shown.** Aggregate owner cash 2021 to 2025 runs from $0.1M to $275.8M, a base year "in which earnings were
  poor" that yields "a breathtaking, but meaningless, growth rate" **[L2005-003]**; and no rate above the discount rate
  may run on **[M1997-095]**, **[M1999-067]**. The fleet grew only by issuing shares. CONVENTION of this run: the
  shown-growth end is set equal to the no-growth end, so the range comes from the windows and the two bases.
- **Discounted at the sovereign, 5.66%, no growth** **[L2000-021]**, **[M1996-025]**:
  - Convention window (2021-2025): **$98.8 to $101.2 a share.**
  - Whole-cycle variant (2016-2025 and 2014-2025): **$48.9 to $60.6 a share.**
  - All cases together: $48.9 to $101.2, a width of 2.1 to 1, under the convention's three-to-one line.
- **Against the price of $116.60:** above the top of every case. The owner-cash yield at the price is 4.8% to 4.9% on
  the five-year window and 2.4% to 2.9% on the whole cycle, below the floor of about ten percent pre-tax (the CONVENTION
  of the framework, from "at least 10% pre-tax returns" **[L2002-020]** and "a point at which we drop out of the game"
  **[M2003-149]**). Had Q2 passed, Q7 would have closed OUT on the floor.

### (b) FAIR PRICE
The price at or below which the central case clears the ~10% pre-tax floor, on equity (owner cash is after interest),
with tax treated as nil (above) and no growth. **Central case: the twelve-year mean 2014-2025, mid of the two bases,
$3.32 a share** (CONVENTION of this run: the twelve years hold two booms, 2015 and 2022-2025, and two troughs, 2017-2018
and 2021, the closest thing in the record to a whole cycle). **Fair price about $33.** For reference: $27.7 on the
lowest case (2016-2025, capex basis) and $57.3 on the highest (2021-2025, capex basis). The price is 3.5 times the central
fair price.

### (c) CHEAP PRICE
Rule (CONVENTION of this run): half the bottom of the whole-cycle range at the sovereign, so that even the worst
whole-cycle case yields more than 11% and the decision would "scream" **[M2009-005]** with no pencil needed **[M1996-084]**;
the margin is wide because "the more volatile the business is", "the larger the margin of safety" **[M1997-080]**.
**Cheap price about $24.5** (half of $48.9). It sits below half of the 2025 book value per share ($40.90).

### Facts recorded for questions not reached
- **Q4.** The Q2 2026 release features adjusted EBITDA and adjusted net income as its headline figures (8-K
  `0001104659-26-093033`). Depreciation and drydock are real costs here, since the fleet must be bought again; the row
  is **[L2015-004]**. Not judged.
- **Q6, Part A.** The 2021 merger was all stock, issued at about $16 a share against a book of $34.70; the row that
  makes such a deal a STOP when the acquirer's stock is below its intrinsic value is **[L2009-019]**. Not judged. Dividend
  policy since 2025: at least 85% of adjusted net income paid out (Q2 2026 release); the $50M buyback authority was not
  used in 2025 or H1 2026 (10-Q). A shareholder rights plan at a 20% threshold was renewed in April 2026 (10-Q, DEF 14A).
- **Q6, Part B.** CEO total compensation $4,505,569 for 2025, of which $2,618,159 in stock awards (DEF 14A); stock pay
  $8.7M in 2025.
- **Q9.** Debt $645.6M against cash and deposits $409.4M at mid-2026; liquidity about $935M; 38 of 69 vessels pledged at
  end-2025; newbuild commitments: two LR1s ($73M remaining, ECA-financed) and four LR1s ordered in 2026 for $244M (2028).

---
## THE BOX
**OUT**, at **Q2**: a commodity freight business that is not the low-cost operator; the castle is shown open on the
evidence, not unjudgeable. Not reached Q7; for the owner's request the computation gives a value range of $48.9 to $101.2
($98.8 to $101.2 on the convention window, $48.9 to $60.6 on the whole cycle) against $116.60, a fair price near $33 and
a cheap price near $24.50.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. **Not** written and committed question by question: the brief forbade
      commits, and the file was filled in one pass after the reading; the working folder holds every intermediate.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (Python check, below); every filing fact has its accession; the
      peer ROE figures are XBRL transcription and are flagged; every number either has a filing or is labelled
      CONVENTION of this run.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and all valuation is under the computation
      heading.
- [x] Owner cash after every real cost, never a net-income proxy; vessel spending and sales read from the statements
      after `tools/run.py`'s capex line was found wrong; sovereign from the Treasury; aggregator price flagged.
- [x] Contrary evidence written down as found (four items, foundations).
- [x] Not a point-in-time run; no anchor rule applies.
- [x] Only the arithmetic lines of `tools/run.py` were used, and one of them was rejected.
- [x] `python tools/check_framework.py` PASS after writing (2026-10-06: run files phantom in 0 files; v5 scope 0 outside).
      A separate check (`check_ids.py` in the working folder): 47 distinct ids, none missing, no E-ids, every quoted
      fragment beside an id found in that row.
- One more admission: the opex-per-day figures for INSW are this run's division of filed segment expenses by filed
  ship-operating days; the peers' are their own published per-day figures except DHT's, divided the same way. The
  divisions are reproducible in `per_day.py`.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 and Q2 for a cyclical commodity.** Test 2 of Q1 says "If something is not very predictable, forget it"
**[M1998-044]**, and the freight rate is not predictable year to year; read alone it would close the file TOO HARD at Q1.
The routing rule sends only fast change to Q1, and the speakers call a cyclical commodity "understandable"
**[M2001-059]**, so this run read Q1 as asking about the economic dynamics and passed it. The framework does not say
which variable must be predictable: the rate, or the structure that sets it. A one-line ruling would stop two analysts
closing the same tanker owner at Q1 TOO HARD and at Q2 OUT. (2) **The second route has no test.** The row that names
the low-cost operator opens "Another way" and names "an ebb-and-flow business model" **[L2004-007]**; the framework
records the route as open, but no row says how to tell an owner that times the cycle from one that rides it; this run
used the span return against peers and said so. (3) **Price against the castle.** Cement is taken "at a price, you know,
for low-cost capacity [...] we would do it" **[M2001-059]**, and brick on the condition "if I can buy the assets cheap
enough" **[M2011-101]**; both accept a cyclical commodity at a price, while Q2 says price does not reopen a castle
**[M2019-015]**. For
asset-heavy commodities with a resale market for the asset (ships, cement plants), the rows may support a narrow
asset-value door the framework does not have; this run kept Q2's rule. (4) **The Q7 convention breaks on a cycle.** The
five-year window happens to hold one trough year and four boom years, and the growth input is meaningless when the
base year is near zero; the convention needs a whole-cycle rule for businesses whose earnings swing through zero. This
run added the whole-cycle variant and set growth to zero, both confessed. (5) **The template's heading for the
computation** uses a dash that the operator's standing style rule forbids; the hyphen was used.
