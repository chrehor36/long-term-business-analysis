# Company Run: LCI Industries (NYSE: LCII), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Working folder:
`Test Runs/_research 2026-10-05 LCII/` (filings as text, the arithmetic script `compute.py` and its output
`compute_out.txt`, the ledger rows read, `ledger_rows.txt`). Every judgment cites a v5 ledger id in bold beside the row's
own words; every filing fact carries its accession. *(Template headings carry no em dashes in this file, by the owner's
standing rule; the protocol's computation header is written "COMPUTATION - NOT A CLEARANCE".)*

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`;
whether the operator holds LCII is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) The session's opening git snapshot showed three commit subjects of other v5 runs of
this date (KSS, AMR, MBC), each closing OUT at Q2 on a filer statement that its products compete on price with low
barriers. That is a pattern I could anchor on; I tried to let the LCII filings decide and to state the other side's case
at Q2 (**[M2016-055]**: "state their case better than they can"). (2) The same snapshot and a directory listing showed
the file names (not contents) of other 2026-10-05 runs and research passes, including an MBUU Malibu Boats research pass
(a marine OEM, an LCII customer industry). None was opened. (3) `tools/run.py` printed v4 material; only its arithmetic
lines were used (Part VII). (4) Running `tools/run.py PATK` for Patrick's price and owner cash showed nothing about LCII.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $82.60 (2026-10-05, aggregator quote via `tools/run.py`, flagged per operator rule 5: live quote only).
  Patrick (PATK) $66.59, same source. Since 2026-06-30 the LCII price is tied to Patrick's by the merger exchange ratio
  of 1.2440 (8-K 2026-06-30, accession `0000763744-26-000040`): $66.59 x 1.2440 = $82.84, so LCII trades about 0.3%
  below the value of the Patrick shares it is to receive.
- **Shares by class:** one class, Common Stock $.01 par, **24,311,507** as of 2026-07-31 on the cover of the 10-Q for the
  period ended 2026-06-30 (filed 2026-08-05, accession `0000763744-26-000070`; `python Screens/cover_shares.py LCII`).
  No other class; the 10-K states "The registrant has no non-voting common equity."
- **Market cap:** 24.311M x $82.60 = **$2,008M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-02 (`python tools/run.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-26, `0000763744-26-000011`); 10-Q Q2 2026 (filed
  2026-08-05, `0000763744-26-000070`); proxy DEF 14A 2026 (filed 2026-03-27, `0001140361-26-011739`, pay metrics only, as
  the file closed before Q5); 8-Ks: Q2 2026 results (`0000763744-26-000068`), call transcript (`0000763744-26-000079`),
  merger agreement and release (`0000763744-26-000040`), CEO retirement (`0000763744-26-000037`), officer agreements
  (`0000763744-26-000038`), new director (`0000763744-26-000061`), HSR filing and voluntary withdrawal and refiling
  (`0000763744-26-000082`, `0000763744-26-000084`); Patrick's S-4 joint proxy (filed 2026-09-23,
  `0001628280-26-063259`, the LCI board's reasons). The 10-Ks FY2007 to FY2024 were read for content per RV, wholesale
  shipments and segment margins (accessions in the content table at Q2).
- **One figure cross-checked against the filed statement:** net cash from operating activities 2025, **$330,976
  thousand** in the consolidated statement of cash flows of the 10-K FY2025 (`0000763744-26-000011`), against **331.0**
  in `tools/run.py`. Also checked: capital expenditures $(52,644)K; stock-based compensation $22,689K; goodwill
  $622,183K; long-term indebtedness $941,502K; total stockholders' equity $1,360,833K. All match.
- **`tools/run.py` arithmetic lines** (USD millions; owner cash = operating cash flow less stock pay less capital
  spending; the D&A variant subtracts depreciation and amortization instead):

| FY | OCF | SBC | D&A | capex | owner cash (capex) | owner cash (D&A) | acquisitions |
|---|---|---|---|---|---|---|---|
| 2021 | -111.6 | 27.2 | 112.3 | 98.5 | -237.3 | -251.1 | 194.1 |
| 2022 | 602.5 | 23.7 | 129.2 | 130.6 | 448.2 | 449.6 | 108.5 |
| 2023 | 527.2 | 18.2 | 131.8 | 62.2 | 446.8 | 377.2 | 25.9 |
| 2024 | 370.3 | 18.7 | 125.7 | 42.3 | 309.3 | 225.9 | 20.0 |
| 2025 | 331.0 | 22.7 | 121.2 | 52.6 | 255.7 | 187.1 | 112.7 |
| **5-yr mean** | | | | | **244.5** | **197.7** | **92.2** |

  SBC resolved by tag each year (`ShareBasedCompensation`); the tool found no securities flows or other capital lines
  inside operating cash flow in the window. The 2021 and 2022-2023 swings are inventory: built $516.7M in 2021, released
  $117.4M and $235.3M in 2022 and 2023 (XBRL `IncreaseDecreaseInInventories`); the window as a whole carries a net build
  of about $153M, so it is not flattered by the release. **Capex sits below depreciation:** 2025 capex $52.6M against
  depreciation of about $67M (D&A $121.2M less amortization of intangibles $54.2M); the filer says "the replacement portion
  has averaged approximately one to two percent of net sales, while the growth portion has averaged approximately two to
  three percent" (10-K FY2025, MD&A), i.e. $41M to $82M of replacement on 2025 sales, while 2025 total capex was 1.3% of
  sales. Depreciation is "almost always true costs" (**[L2015-004]**: "Depreciation charges are a more complicated subject
  but are almost always true costs."), so the D&A column is shown beside the capex column throughout.
- Longer series (same sources; 2007-2008 from the 10-K FY2008, `0001144204-09-013467`): owner cash 2007 $72.5M, 2008
  -$3.1M, 2009 $56.7M; over **2009-2025 owner cash was 5.29% of sales, and 1.14% of sales after acquisitions**;
  acquisitions 2007-2025 totalled **$1,662M**, of which $1,385M in 2016-2025, against owner cash of $1,787M in 2016-2025.
  Dividends and buybacks 2016-2025 were $980M; debt rose from $50M to $945M over the same years (`compute_out.txt`).
- **H1 2026** (10-Q `0000763744-26-000070`): operating cash flow $170.2M (H1 2025 $154.9M); capex $28.4M; LTM operating
  cash flow $346M (release `0000763744-26-000068`). Q2 2026 net sales were reduced $88.8M for IEEPA tariff refunds "expected
  to be passed through to customers" (release).

### The balance sheets, ten years, read before the income account (the template asks this in Step 0 when the file closes before Q4)
Read under **[M2025-032]**: "balance sheets over an 8 or 10 year period before I even look at the income account". Figures
from `tools/run.py` (first-filed XBRL) checked against the FY2025 statement above (USD millions):

| year-end | equity | goodwill | intangibles | tangible equity | debt | cash | inventory | inv./sales | receivables | retained |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 550 | 89 | 113 | 348 | 50 | 86 | 189 | 11.2% | 57 | 395 |
| 2018 | 706 | 180 | 176 | 350 | 294 | 15 | 341 | 13.8% | 122 | 563 |
| 2019 | 801 | 351 | 341 | 109 | 631 | 35 | 394 | 16.6% | 200 | 645 |
| 2021 | 1,093 | 543 | 520 | 30 | 1,303 | 63 | 1,096 | 24.5% | 320 | 931 |
| 2022 | 1,381 | 567 | 503 | 311 | 1,119 | 47 | 1,030 | 19.8% | 214 | 1,221 |
| 2023 | 1,355 | 590 | 449 | 316 | 847 | 66 | 768 | 20.3% | 215 | 1,177 |
| 2024 | 1,387 | 586 | 392 | 409 | 757 | 166 | 737 | 19.7% | 200 | 1,208 |
| 2025 | 1,361 | 622 | 403 | 336 | 945 | 223 | 809 | 19.6% | 243 | 1,280 |

What the figures say: (1) **Equity became mostly purchased goodwill and intangibles**: 37% of equity in 2016, 75% in
2025; tangible equity is about where it was in 2016 ($348M then, $336M now) while sales went from $1.68B to $4.12B. The
growth of the decade was bought: $1.39B of acquisitions 2016-2025. (2) **Debt replaced the equity paid out**: debt went
from $50M (2016) to $1,303M (2021) and $945M (2025; $852.6M at 2026-06-30); the 2016-2025 outflows to acquisitions,
dividends and buybacks ($2.37B) exceeded owner cash ($1.79B) and the gap was borrowed. Debt today is $460M of 3% 2030
convertible notes and a $397M SOFR+2.25% term loan (10-K FY2025, Note 9), with $595M undrawn on the revolver. (3)
**Inventory doubled against sales**: 11.2% of sales in 2016, 19.6% in 2025, peaking at 24.5% in 2021. The filings tie the
rise to the imported-goods businesses bought (Furrion 2021, Way 2022; 10-K FY2025 risk factors) and to the aftermarket;
I read it as a change in the business mix toward distribution of imported goods, not as a tell, but it is the item
**[M1995-064]** names ("inventories look out of line"), and it is written down. Receivables rose from 3.4% to 5.9% of
sales. (4) Retained earnings rose every year but 2023; diluted shares were 24.9M in both 2016 and 2025, the 2025
buyback ($128.6M) offsetting nine years of stock pay. What the figures cannot say: how much of the content gain per RV
was organic and how much bought (the filer gives no annual split).

---
## THE FOUNDATIONS (not a gate)
A share of LCII is, for the next six to nine months, a claim on 1.2440 Patrick shares and, after closing, a 48% interest
in the combined Patrick-Lippert business; the test is whether I would own that business "if the market closed for five
years" (**[M1997-109]**). The quotation "just tells us prices" (**[M2006-077]**: "It just tells us prices."); the fall
in the LCII price says nothing by itself. No macro view enters: the RV cycle is read as a property of the business, its
"average profitability of the business over time" (**[M2015-016]**), not as a forecast of 2027 shipments. Who is paid to
tell me: the merger's fairness opinions and the "$150+ million" synergy figure are the bankers' and managements' numbers
and are not used.

**Contrary evidence, written down as found** (**[M1997-127]**: "write it down in the first 30 minutes"):
1. *Against the castle:* the 10-K FY2025 says "barriers to entry are generally low in the industries we serve"
   (Item 1) and "The industries in which we are engaged are highly competitive and generally characterized by low barriers
   to entry" (Item 1A).
2. *For the castle:* content per towable rose from $1,700 (2007) to $5,670 (2025), 6.9% a year, while towable shipments
   moved from 261,700 to 298,200.
3. *For the castle:* pre-tax operating return on tangible capital (equity less goodwill and intangibles, plus net debt)
   of 64% (2016), 28% (2019), 40% (2022), 26% (2025).
4. *Against:* the same returns fell to 11% in 2023, and the OEM segment earned a 0.6% margin that year (10-K FY2023,
   `0000763744-24-000023`).
5. *Against:* prices are "contractually tied to indices of select commodities", which cut 2023 OEM operating profit by
   $213.7M (10-K FY2023).
6. *Against:* the largest towable OEM makes RV components itself: Thor's Airxcel and Postle sold $297.4M to Thor's own RV
   segments in fiscal 2026 (Thor 10-K FY2026, `0000730263-26-000027`).
7. *Against:* owner cash after acquisitions was 1.14% of sales over 2009-2025; growth was bought.
8. *Against the low-cost claim:* in the 2023 trough Patrick earned a 7.5% operating margin and LCI 3.3%.
9. *For the price, not the business:* at $82.60 the 5-year owner cash is a 16.5% pre-tax yield on the market value.
10. *Context:* the CEO of 13 years retired on 2026-06-03 and the company agreed four weeks later to merge into its chief
    competitor at a 16% premium; the LCI board names "challenges of addressing customer affordability needs" among the
    risks of standing alone (S-4, `0001628280-26-063259`).

## THE STANDING RULE
Owning LCII puts the buyer at risk of ruin only through the buyer's own conduct: bought with cash, no margin, sized so
that a fall of half is borne without forced sale (**[M2020-022]**: "have it go down 50 percent"; **[M1999-005]**:
"almost impossible to go broke without borrowed money being in the equation"). The target's own debt is Q9's question.
**Passes for an unlevered buyer** (**[M2012-081]**: "We are never going to risk what we have and need").

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" (**[M2012-065]**), a "reasonable probability of being able to asses where the business will
  be in 10 years" (**[M2000-037]**), starting by "trying to identify the key variables in that particular business"
  (**[M1998-044]**).
- **The key variables, from the filings.** (1) North American towable wholesale shipments, which swing hard and do not
  trend: 261,700 (2007), 138,800 (2009), 531,200 (2021), 259,100 (2023), 298,200 (2025); the filer's 2026 guide is
  280,000 to 300,000 (release `0000763744-26-000068`). (2) Content per unit, which rises with price, share and
  acquisitions (table at Q2). (3) The OEMs' bargaining position: two customer groups are 33% of sales, "we generally do not
  have long-term agreements with our customers" (10-K FY2025). (4) Steel and aluminum, 30% and 10% of raw material cost,
  passed through by index. (5) The aftermarket (23% of sales, 34% of operating profit in 2025; CURT about half of it).
- **Foreseeable?** The product is not a fast-changing technology; chassis, axles, slide-outs, windows, doors, furniture
  and awnings are the same categories in the FY2007 and FY2025 10-Ks. The cycle makes any year unforeseeable but not the
  pattern, and the speakers accept lumpy earnings in a good business (**[M2011-102]**: "what difference does it make to us
  if the earnings average, say, 300 million a year, if it comes in in a very lumpy fashion"). The economics can be read
  "off the figures" (**[M2008-069]**: "make a decision on something like PetroChina off the figures"): twenty years of
  10-Ks show what the business earns at the top and bottom of the cycle.
- **The merger.** What a buyer owns in ten years is a share of the combined Patrick-Lippert company, not LCI alone. Its
  other part, Patrick, files the same economics in the same words (Q2 competitor row), so the combination does not put a
  part outside the circle (the by-parts reading of Q1's holding-company paragraph, a CONVENTION of the framework, applied
  here by analogy and confessed as such in the last section).
- **Doubt test** (**[M2002-092]**: "if you have doubts about something being into your circle of competence"): the doubt
  I have is about the castle, which is Q2's question, not about what the business is or how it earns.
- **VERDICT: IN.** The ten-year economics of an RV component supplier can be foreseen in kind from its own record; whether
  they are protected is asked next.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" and "how permanent are they?" (**[M1995-038]**). Read the other way
round from **[M1997-148]** ("whether a company can have a sustainable edge"), Q1 having passed.

**The case for the castle, stated as strongly as I can** (**[M2016-055]**: "state their case better than they can").
LCI is the largest supplier of the structural and mechanical content of a North American towable RV. Its content per
towable has risen in every year since 2006 except 2020 (on first-filed figures; the filer's restatement without Furrion
shows a 1% rise) and 2023, from $1,555 to $5,670. It is the supplier that sits next to the OEMs
in Elkhart, ships "within one to two weeks of receipt of orders" (10-K FY2025), and for an OEM building a trailer on a
line, a missing chassis stops the line; the speakers name that kind of value (**[M2017-062]**: "the reliability is
incredibly important"), and the advantage of size (**[M1995-039]**: "the microeconomic business advantages are, by and
large, advantages of scale"). It earned pre-tax returns on tangible capital of 28% to 64% outside the troughs. It came
through 2009 with an operating profit before a goodwill write-down, and through 2023 profitable.

**The tests, each with its filing fact.**
1. **The money test** (**[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on"; "could I do
   it?"). The filer answers it: "While barriers to entry are generally low in the industries we serve, compliance with
   industry standards, safety requirements, and initial capital investments are necessary to establish operations" (10-K
   FY2025, Item 1, Competitive Differentiation). And an attacker with money has come: Thor, the second customer group,
   bought Airxcel in 2021 and now sells $297.4M a year of RV components to its own plants (Thor 10-K FY2026,
   `0000730263-26-000027`, "Intercompany eliminations | (297,407)"). The 10-K names the threat: "the manufacture by our
   customers themselves of products supplied by us could reduce demand for our products" (Item 1A). This is the
   answer the speakers turn away from (**[M2012-106]**: "there are some industries that are just never going to have
   barriers to entry").
2. **Pricing power and the agony before a rise** (**[M2005-020]**: "you can almost measure the strength of a business
   over time by the agony they go through in determining whether a price increase can be sustained"). LCI's prices are set
   by formula and contract, not by its choice: "We have agreements with certain customers that index their pricing to
   select commodities", with other prices "fixed for periods generally not in excess of eighteen months" (10-K FY2025,
   Sales and Marketing). When steel fell in 2023, "Selling prices contractually tied to indices of select commodities
   decreased, resulting in a decrease in operating profit of $213.7 million" and the OEM segment margin fell from 11.1% to
   0.6% (10-K FY2023, `0000763744-24-000023`). The 2025 content gain was "driven primarily by sales price increases related
   to tariffs" (10-K FY2025), and the 2026 tariff refunds are being handed back to the OEMs ($88.8M in Q2 2026). This is
   the strongest point for the castle under this test, and I write it down against my verdict: the rows read the passing
   through of raw-material costs as a mark of a strong position (**[M2005-017]**: "over time the businesses with strong
   competitive positions manage to pass through increases in raw material costs"). But LCI's pass-through is a contract
   term that runs both ways: the index that lifted price in 2022 took $213.7M of operating profit back in 2023, and the
   tariff refunds go back to the customer. It shows the customer accepting cost, not LCI setting a price above it. The interim CEO's account of model-year pricing is cost reduction "to help stimulate and drive
   volume" passed "forward to our customers" (call, `0000763744-26-000079`).
3. **Would the customer still choose it over the low bid?** (**[M2017-009]**: "people buying candy for the low bid").
   The filer lists price among the bases of competition: "Competition is based primarily upon product quality and
   reliability, product innovation, price, customer service, and customer satisfaction" (Item 1A); the buyers are
   concentrated, Berkshire Hathaway (Forest River and Clayton) 18% and Thor 15% of 2025 sales, without long-term
   agreements. The customer here is an OEM purchasing department, not a consumer who asks for the part by name; the
   insurance row describes the position (**[L2004-003]**: "most insureds don't care from whom they buy").
4. **The low-cost position** (**[L2004-007]**: "Another way to prosper in a commodity-type business is to be the low-cost
   operator."; **[M2018-043]**: "Being the low-cost producer, for example, is a terribly important moat."). The
   comparison that decides it is against the competitor (**[M2001-013]**: "if your costs are on parity or less"). Over
   2009-2025 LCI's operating margin (before the 2008-2009 goodwill write-downs) was 7.86% of sales and Patrick's 7.67%;
   in the 2023 trough Patrick earned 7.5% and LCI 3.3% (competitor row). On the evidence LCI is not the low-cost operator
   of its field; it is at parity in good years and behind in the bad one.
5. **Ask the competitors.** Patrick's own 10-K says the same of the whole field: "The barriers to entry for each industry
   are generally low" and "competition exists primarily on price, product features and innovation, timely and reliable
   delivery, quality and customer service" (Patrick 10-K FY2025, `0000076605-26-000013`, Competition). Patrick adds the
   one qualification in LCI's favour: "in order for a competitor to compete with Patrick on a national basis, the Company
   believes that a substantial capital commitment and investment in personnel and facilities would be required." Two
   large suppliers facing two large buyers is the structure the rows warn about (**[M2013-052]**: "you can have only two
   competitors"; **[M2012-108]**: "one competitor is frequently enough to ruin a business").
6. **Widening or narrowing** (**[L2005-010]**: "grows either weaker or stronger"). Content per unit, North American
   towables, from the 10-Ks (the filer restated some years; the first-filed figure is shown):

| year | content per towable | towable shipments | source 10-K |
|---|---|---|---|
| 2007 | $1,700 | 261,700 | FY2008 `0001144204-09-013467` |
| 2008 | $1,902 | 185,100 | FY2009 `0001144204-10-012718` |
| 2009 | $2,101 | 138,800 | FY2009 |
| 2011 | $2,398 | 212,900 | FY2011 `0001437749-12-002281` |
| 2013 | $2,716 | 268,000 | FY2013 `0001437749-14-003110` |
| 2015 | $2,987 | 314,400 | FY2015 `0000763744-16-000351` |
| 2017 | $3,263 | 429,500 | FY2017 `0000763744-18-000042` |
| 2019 | $3,618 | 349,500 | FY2019 `0000763744-20-000030` |
| 2021 | $4,198 | 531,200 | FY2021 `0000763744-22-000016` |
| 2022 | $6,090 | 421,700 | FY2022 `0000763744-23-000016` |
| 2023 | $5,058 | 259,100 | FY2023 `0000763744-24-000023` |
| 2025 | $5,670 | 298,200 | FY2025 `0000763744-26-000011` |

   The filer says what moves it: "Content per RV is impacted by changes in selling prices for our products, market share
   gains, and acquisitions" (10-K FY2025). The 2022 jump (+45%) and 2023 fall (-17%) are commodity-indexed prices; the
   years of few acquisitions show little organic gain (2023 to 2024 +1%, acquisitions $25.9M and $20.0M); and the decade's
   rise came with $1.39B of acquisitions. The content line widens when LCI buys and when steel rises. That is not the
   widening the 2005 letter describes (**[L2005-010]**: "If we are delighting customers, eliminating unnecessary costs and
   improving our products and services, we gain strength."); it is a moat bought in pieces and repriced by an index. Whether the merger with
   Patrick widens it is the antitrust reviewers' open question: the HSR notice was withdrawn and refiled on 2026-09-04 and
   2026-09-09 (`0000763744-26-000084`).
7. **What could destroy, modify or reduce it** (**[M2000-014]**: "destroy, or modify, or reduce the economic strengths").
   OEM vertical integration (Thor, above); the OEMs' affordability squeeze, which the LCI board itself lists among the
   risks of remaining alone, "challenges of addressing customer affordability needs and driving long-term stockholder value
   creation without the scale and synergies available through the combination" (S-4, `0001628280-26-063259`, LCI board's
   reasons); imports (36% of raw materials and components imported in 2025; China-sourced Furrion).
8. **The cycle as a test of the moat.** 2007 to 2009: sales -40.5%, towable shipments -47%, operating loss after a $45.0M
   goodwill write-down (FY2009 10-K). 2022 to 2023: towable RV OEM sales -48% against shipments -39%; OEM margin 0.6%.

**The competitor row** (same metric from each filer's own filings; XBRL companyfacts, first-filed 10-K values, and the
10-Ks named):

| metric | LCI Industries | Patrick Industries (`0000076605-26-000013`) | Thor in-house supply (`0000730263-26-000027`) | Dometic |
|---|---|---|---|---|
| operating margin, 2009-2025 aggregate | 7.86% (before write-downs) | 7.67% | n/a | not read |
| operating margin 2022 / 2023 / 2025 | 10.6% / 3.3% / 6.8% | 10.2% / 7.5% / 7.0% | n/a | not read |
| gross margin 2009 / 2025 | 19.8% / 23.8% | 10.8% / 23.1% | n/a | not read |
| owner cash (OCF-SBC-capex), 5-yr mean 2021-25 | $244.5M | $253.3M | n/a | not read |
| acquisitions, 5-yr mean 2021-25 | $92.2M | $263.3M | Airxcel bought 2021 | not read |
| own words on entry | "barriers to entry are generally low" | "barriers to entry for each industry are generally low" | sells $297.4M of components to its own RV segments | non-SEC filer, flagged |

**Why OUT and not TOO HARD.** The framework sends "a castle shown open on the evidence" to OUT and "a castle whose
future cannot be judged" to TOO HARD (Q2, the routing). The future here is not hidden; the evidence is direct and runs
one way: the filer and its chief competitor each state in their own 10-Ks that entry is easy and price is a basis of
competition; the largest buyers are few, unbound by long contracts, and one of them already makes the products; the
price is set by commodity index and handed back when costs fall; in the one hard test of the last decade (2023) the OEM
business earned 0.6% and LCI did worse than its competitor; and the content gains that look like a widening moat were
bought for $1.39B and repriced by steel. The high returns on tangible capital are real, and I write them down against
myself; but they are earned on a tangible base kept small by paying for growth with goodwill, and on total capital
including what was paid (equity plus net debt) the pre-tax return was 5.8% (2023), 11.0% (2024) and 13.4% (2025). The
speakers' answer to a castle that the attacker with money can reach is that they would not buy it (**[M2011-015]**:
"If the answer had been yes, we wouldn’t have done it."), and a low price does not change that answer (**[M2019-015]**: "turn any investment into a good deal by
paying little"; **[L2012-004]**: "far better to buy a wonderful business at a fair price than to buy a fair business at a
wonderful price").

**VERDICT: OUT.** The castle is shown open by the filer's own statement of low barriers to entry, commodity-indexed
pricing, concentrated customers who can and do make the products themselves, and a trough margin worse than its
competitor's.

---
## Q3: HOW MUCH CAPITAL MUST GO IN. **NOT REACHED** (the file closed at Q2). Facts recorded at Step 0 for the record:
owner cash after acquisitions 1.14% of sales over 2009-2025; $1.66B of acquisitions 2007-2025.
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. **NOT REACHED.** The ten balance sheets were read at Step 0 as the template
requires; no tell beyond the inventory ratio was found, and that one is written down there.
## Q5: WHO RUNS IT. **NOT REACHED.** Facts for the record: the CEO since 2013, Jason Lippert, retired 2026-06-03 with a
$100,000-a-month consulting arrangement to 2027-06-03 and continued vesting (`0000763744-26-000037`); a director, John
Sirpilla, became interim CEO at a $1.1M salary, 140% target bonus and a $1.8M RSU grant; the board chair resigned the
same day. The 2025 PSUs pay on ROIC (goal 18.5%) and free cash flow as a percent of operating profit (proxy
`0001140361-26-011739`).
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. **NOT REACHED.** Facts for the record: 2025 buybacks of 1,366,565
shares at weighted average prices of $91.47 and $94.55 under programmes that state no price limit (10-K FY2025); the
company has agreed to be acquired in an all-stock merger in which LCI holders receive 1.2440 Patrick shares, about 48% of
the combined company, at an implied premium of about 16% to the 2026-06-29 close (S-4). The Q6 STOP in **[L2009-019]**
("If shares of a prospective acquirer are selling below their intrinsic value") concerns the acquirer's stock; whether
it applies to a buyer of the target who will receive the acquirer's stock is not answered by the framework (last section).
## Q7, Q8, Q9, Q10, Q12: **NOT REACHED.**

### COMPUTATION - NOT A CLEARANCE (reported at the owner's request; the file is closed OUT at Q2; nothing here is entry language)
All figures USD; sovereign 5.63%; 24.311M shares; price $82.60. Script and output: `compute.py`, `compute_out.txt`.

**(a) Value range per the Q7 CONVENTION** (five-year average owner cash, carried ten years at the growth shown capped by
the Q3 arithmetic, then zero nominal growth, all at the long government rate; "the range must be so wide that no useful
conclusion can be reached" is the width test, **[L2000-025]**):
- No-growth end, capex basis ($244.5M): **$4,344M, $178.66 a share.** D&A basis ($197.7M): $3,512M, $144.47 a share.
- Shown-growth end. The growth shown in aggregate owner cash (5-year mean 2016-2020 $112.9M to 2021-2025 $244.5M, about
  17% a year) was bought: acquisitions averaged $92.2M a year in the window. CONVENTION of this run: the shown-growth
  case uses the base net of the acquisition spending that bought the growth ($244.5M - $92.2M = $152.3M), and the growth
  rate is capped at the discount rate (5.63%), the Q3 cap the framework names (no rate "that runs past the discount
  rate"). Result: **$4,228M, $173.92 a share.**
- **Convention range: $144 to $179 a share** (D&A no-growth to capex no-growth, the shown-growth case inside it), width
  1.24 to 1, against $82.60.

**Whole-cycle variant** (the five-year window holds the 2021-2022 boom and its inventory unwind). CONVENTION of this run:
owner cash as a share of sales over 2009-2025, a span holding two troughs (2009, 2023) and the boom, applied to LTM sales
of $4,028.4M:
- Owner cash 5.29% of sales gives $212.9M: no growth, **$155.56 a share**.
- If acquisitions are a cost of keeping the content share, owner cash after acquisitions was 1.14% of sales, $46.1M: no
  growth **$33.68 a share**; growth at the rate **$52.65 a share**.
- **Whole-cycle range: $33.68 to $155.56 a share**, width 4.6 to 1; with the convention range, $33.68 to $178.66, width
  5.3 to 1. Admitting the acquisitions as a cost of standing still would put the case past the framework's three-to-one
  width (TOO HARD at Q7 had it been reached); leaving them out puts the price at less than half the bottom of the range.
  The whole verdict of the arithmetic turns on whether the decade's $1.39B of purchases were needed to stand still,
  which is Q2's question, answered against the business above.

**(b) FAIR PRICE.** Central case: whole-cycle owner cash $212.9M after tax, no growth, no acquisitions. Tax treatment:
grossed up at the 2025 effective tax rate of 26.2% (10-K FY2025) to $288.5M pre-tax, so that it is comparable with the
floor stated as "a very high probability of at least 10% pre-tax returns" (**[L2002-020]**) and with the speakers'
whole-business yardstick (**[M2011-062]**: "10 percent pretax earnings on what we pay"). Fair price, where the central case
yields 10% pre-tax with no growth: **$118.67 a share** (at $82.60 the central case yields 14.4% pre-tax). On the 5-year
capex base the fair price is $136.30; on the D&A base $110.21; on the base after acquisitions $25.70.

**(c) CHEAP PRICE.** Rule (CONVENTION of this run): the price at which the central case yields twice the floor, 20%
pre-tax, so that an analyst wrong by half on the cash still clears the floor without a pencil (**[M2009-005]**: "It should
scream at you."): **$59.33 a share.** On the base after acquisitions the same rule gives $12.85.

**The merger, for the record.** LCII is priced off Patrick. Per LCII share, the combined company's five-year owner cash
(LCI $244.5M plus Patrick $253.3M, times 48%) is $9.83, against LCI's own $10.06, so the standalone figures above are
close to the combined ones before synergies. But Patrick spent $263.3M a year on acquisitions in 2021-2025, more than its
owner cash; the combined company's owner cash after acquisitions is negative over that window.

---
## THE BOX
**OUT, decided at Q2** (the castle shown open on the evidence: low barriers stated by the filer and its competitor,
commodity-indexed prices, concentrated OEM buyers who make components themselves, a trough margin worse than the
competitor's). Not a TOO HARD, so no research pass is opened. The computation, not a clearance, puts the price ($82.60)
below a convention range of $144 to $179 and a whole-cycle central fair price of $118.67, but above a whole-cycle value
after acquisitions of $33.68 to $52.65; the castle verdict is what decides which of those is the business, and a low price
does not reopen it (**[M2019-015]**: "turn any investment into a good deal by paying little").

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before the first `tools/run.py` call). Written
      in one pass after the research, not question by question, and **not committed**: the brief for this run forbade
      commits. Deviation from write-early, confessed.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`; result below); every filing fact has its
      accession; numbers without a filing are labelled CONVENTION or computed in `compute.py` from filed figures.
- [x] The order was kept; Q1 IN, Q2 OUT closed the run; Q3 to Q12 NOT REACHED; the valuation block is headed as a
      computation and carries no entry language.
- [x] Owner cash after every real cost (OCF less stock pay less capex, D&A variant beside it), never a net-income proxy;
      the sovereign from the US Treasury; aggregator quotes flagged.
- [x] Contrary evidence written down as it was found, in the foundations, both ways (**[M1997-127]**: "write it down in
      the first 30 minutes").
- [x] No point-in-time anchor in this run (dated today), so the anchor rule does not bind.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 ids, floor and verdict lines were ignored.
- [x] `python tools/check_framework.py` run after writing (result reported to the caller; no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A target in a pending all-stock merger.** The framework has no rule for buying a company that has agreed to be
acquired for the acquirer's stock at a fixed ratio. The buyer of LCII is in substance buying 1.2440 Patrick shares and a
48% share of a business that does not yet exist; Q1 and Q2 have to be asked of LCI and of the combination, and the Q6
STOP (**[L2009-019]**: "If shares of a prospective acquirer are selling below their intrinsic value") is written for the
acquirer's undervalued stock, not for the target's holder who receives it. I
asked Q1 and Q2 of LCI, read Patrick's filings for the other part, and applied Q1's by-parts holding-company reading by
analogy; that analogy is mine. (2) **Bought growth in the Q7 convention.** The convention carries owner cash "at the
growth the business has actually shown", measured on aggregate owner cash; for a roll-up the growth shown was paid for
with acquisitions that sit outside owner cash, so the convention counts bought growth as free. I netted the acquisition
spending from the base of the shown-growth case and showed the variant in which acquisitions are a cost of standing
still; the two readings differ by more than five to one, and the framework does not say which is right. (3) **The
floor's tax basis.** The CONVENTION floor is "about ten percent pre-tax" while owner cash is after tax; the framework
does not say how to convert. I grossed up at the filer's effective rate; another analyst could compare after-tax cash
with the 6.5% to 7% after-tax figure the 2002 row gives, and get a different fair price. (4) **OUT against TOO HARD at
Q2.** The routing sends a castle "shown open on the evidence" to OUT, but gives no line for a business whose filer says
the barriers are low while it earns high returns on a small tangible base. I decided on the direct evidence (the filer's
words, index pricing, customer integration, the 2023 trough against the competitor); an analyst who weighted the
returns on tangible capital more heavily could close TOO HARD (WORK) and open a research pass on organic content share.
(5) **The whole-cycle variant** asked for by the owner is not in the framework; its span (2009-2025) and its base (owner
cash as a share of sales times LTM sales) are mine and confessed above.
