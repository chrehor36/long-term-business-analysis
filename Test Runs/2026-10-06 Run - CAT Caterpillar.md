# Company Run — Caterpillar Inc. (NYSE: CAT) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run from the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Every judgment cites a v5
ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Research folder: `Test Runs/_research 2026-10-06 CAT/` (the `tools/run.py`,
`cover_shares.py` and `sources.py` outputs, the fetch and text scripts, the ledger helper `ids.py`, the arithmetic script,
and the filing extracts; raw .htm/.txt filings are not committed).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the queue register, the prepped reading list and `tools/alerts.json` were not opened,
and no attempt was made to learn whether the operator holds or wants this name.

**CONTAMINATION, declared.** (1) When the template was copied, a directory listing of `Test Runs/` filtered for "CAT"
showed that an earlier run file exists for this ticker, `2026-09-28 Run - CAT Caterpillar.md` (a v4.1-era date). It was
not opened; only its file name was seen, and the name carries no verdict. No earlier research folder for CAT was opened.
(2) The repository's last three commit subjects (exports of 2026-10-05: S&P 600 runs, tool fixes) were seen; none names
Caterpillar. (3) My training memory holds a general picture of Caterpillar (a cyclical maker of construction and mining
machines and engines, with a captive finance arm, a large independent dealer network, a 2016 loss year, and a data-centre
power boom). It is treated as a prior to be replaced by the filings; every fact below is from a filing read for this run.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** **$848.14** (2026-10-05 close as fetched by `tools/run.py`; aggregator, flagged per operator rule 5, used for
  the quote only). For scale, the 10-Q's issuer-purchase table shows the company buying its own stock at an average of
  $766.00 in April, $890.17 in May and $947.20 in June 2026 (10-Q Q2 2026, Part II Item 2), and at $385.64 in October 2025
  (10-K FY2025, Item 5).
- **Shares:** one class of common stock. The 10-Q for the quarter ended 2026-06-30 (filed 2026-08-05, accession
  `0000018230-26-000046`) gives on its cover **459,674,889** shares outstanding; `python Screens/cover_shares.py CAT`
  printed the same figure from the same filing ("single class / undimensioned"). The 10-K says basic shares were "approximately
  465 million" at 2025-12-31 (Item 7, Liquidity).
- **Market cap:** $848.14 × 459.675M = **$389.87B** (agrees with `tools/run.py`).
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve, dated
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4), all from SEC EDGAR (CIK 18230):
  - 10-K FY2025, filed 2026-02-13, accession `0000018230-26-000008`: Item 1 (business, competitors by segment, Cat
    Financial, dealers, backlog), Item 1A, Item 5 (issuer purchases), Item 7 (MD&A, outlook, liquidity, resource allocation,
    the non-GAAP reconciliations, the Supplemental Consolidating Data for MP&E and Financial Products), Statements 1, 3
    and 5, Note 3 (stock pay), Note 7 (Cat Financial financing activities, write-offs), Note 16 (repurchases), and the
    segment note's reconciliation of segment profit to consolidated profit.
  - 10-Ks for FY2024 (`0000018230-25-000008`), FY2023 (`0000018230-24-000009`), FY2022 (`0000018230-23-000011`) and FY2021
    (`0000018230-22-000050`): the supplemental cash-flow data and the "ME&T free cash flow" reconciliations, for the
    five-year owner-cash table.
  - 10-Q Q2 2026, filed 2026-08-05, `0000018230-26-000046`: statements, Note on repurchases and ASRs, the IEEPA tariff
    recovery note, MD&A, backlog, Part II Item 2.
  - DEF 14A filed 2026-04-30, `0001308179-26-000358` (read at Q5 and Q6).
  - 8-K of 2026-08-04, `0000018230-26-000040`, EX-99.1 (Q2 2026 earnings release, read at Q4 for non-GAAP habits);
    8-K of 2026-01-06, `0001104659-26-001346` (Executive Chairman Umpleby to leave the board 2026-04-01; CEO Joseph Creed to
    add the chair; board cut from ten to nine); 8-K of 2026-04-10, `0001104659-26-042062` (new CFO Kyle Epley from
    2026-05-01); 8-K of 2026-03-26, `0000018230-26-000013` (Rail moved from Power & Energy to Resource Industries, history
    recast); 8-K of 2026-09-01, `0001104659-26-104197` (bank credit facilities renewed: a $3.5B 364-day facility and the
    three- and five-year facilities extended).
- **One figure cross-checked against the filed statement:** consolidated net cash provided by operating activities for
  2025, **$11,739M** in `tools/run.py` (XBRL) and $11,739M on the filed Consolidated Statement of Cash Flow (10-K FY2025,
  Statement 5) and in the Supplemental Data for Cash Flow. Agrees.
- **`tools/run.py CAT`, arithmetic lines only** (Part VII; its v4 wording, owner-earnings window and verdict language were
  ignored). Its consolidated owner-cash lines treat Caterpillar as one business; they are not used as the input below,
  because the 10-K itself splits the company into two businesses with different balance sheets, and the rows say
  "lumping them together [...] impedes analysis" **[L2008-005]**. The tool did flag the consolidated
  `PaymentsToAcquireEquipmentOnLease` line (Cat Financial's lease fleet) as a capital payment outside capex; that is
  recorded and used in the consolidated variant below.

**The two businesses in the filing.** The 10-K presents "Machinery, Power & Energy" (MP&E: Caterpillar and subsidiaries
excluding Financial Products) and "Financial Products" (Cat Financial and the insurance subsidiaries) side by side, with
separate balance sheets and cash flows (10-K FY2025, Supplemental Consolidating Data). At 2025-12-31 MP&E held $60.1B of
assets, $11.0B of long-term debt and $17.4B of equity; Financial Products held $41.7B of assets (finance receivables
$17.3B current and $15.5B long-term before eliminations), $33.6B of debt ($5.5B short-term, $7.1B due within a year,
$21.0B long-term) and $4.8B of equity. MP&E's operating cash flow includes the dividends Financial Products paid it
($850M 2021, $475M 2022, $425M 2023, $625M 2024, $500M 2025; Supplemental Data for Cash Flow, footnote 5), so Financial
Products enters owner cash at the cash it sends up, which is how Part IV's equity-method convention counts an investee's
profit (Q4, CONVENTION).

**Owner cash after every real cost, MP&E basis** (MP&E operating cash flow as filed, which adds stock pay back, less stock
pay, less all MP&E capital spending including MP&E's own leased equipment; USD millions; from the supplemental cash-flow
data and the ME&T/MP&E free-cash-flow reconciliations of the five 10-Ks; stock pay from Note 3, "Before tax, stock-based
compensation expense"):

| year | MP&E OCF | stock pay | MP&E capex | **owner cash** | MP&E D&A | depreciation variant | company's "free cash flow" |
|---|---|---|---|---|---|---|---|
| 2021 | 7,177 | 200 | 1,129 | **5,848** | 1,550 | 5,427 | 6,048 |
| 2022 | 6,358 | 193 | 1,298 | **4,867** | 1,439 | 4,726 | 5,777 (adds back $717M IRS settlement) |
| 2023 | 11,688 | 208 | 1,663 | **9,817** | 1,361 | 10,119 | 10,025 |
| 2024 | 11,437 | 223 | 1,988 | **9,226** | 1,368 | 9,846 | 9,449 |
| 2025 | 12,278 | 242 | 2,794 | **9,242** | 1,497 | 10,539 | 9,484 |
| five-year mean | | | | **7,800** | | 8,131 | |

The company's "free cash flow" differs from owner cash by the stock pay, and in 2022 by $717M of "Cash payments related
to settlements with the U.S. Internal Revenue Service", which the company added back (10-K FY2022, ME&T free cash flow
reconciliation). A tax paid is a real cost; it stays in owner cash.

**Consolidated variant** (consolidated OCF less stock pay, less capex, less Cat Financial's equipment leased to others;
the conservative reading, which charges the lease fleet's growth to the owner although it is debt-funded and earns lease
income): 2021 4,526; 2022 4,974; 2023 9,585; 2024 8,597; 2025 7,211; **mean 6,979**. (Consolidated OCF 7,198 / 7,766 /
12,885 / 12,035 / 11,739; capex 1,093 / 1,296 / 1,597 / 1,988 / 2,821; leased 1,379 / 1,303 / 1,495 / 1,227 / 1,465; same
filings.)

Per share, on 459.675M shares: owner cash 2025 $20.11; five-year mean $16.97. Against the price, the mean is a **2.0%**
yield and the 2025 figure 2.4%; the sovereign is 5.66%. The arithmetic is in `Test Runs/_research 2026-10-06 CAT/arith.py`.

**The first half of 2026** (10-Q Q2 2026): sales and revenues $37.958B against $30.818B (+23%); profit $7.769B against
$5.388B; MP&E free cash flow, as the company defines it, $5.698B against $2.575B; repurchases $6.522B of cash paid (7.0M
shares received for $4.9B, the rest ASR advances); $392M of "expected IEEPA tariff recoveries" booked in operating profit
after the Supreme Court ruled the IEEPA tariffs unauthorized on 2026-02-20; backlog $72.1B at 2026-06-30 against $51.2B
at 2025-12-31 and $30.0B at 2024-12-31.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what Caterpillar's machines, engines and finance book will earn, not where the
quote goes, and the test is whether I would hold it "if the market closed for five years" **[M1997-109]**. The price has
roughly doubled in a year (the company itself bought at $385.64 in October 2025 and at $947.20 in June 2026), and a
rise "is never a reason to buy it" **[L2013-007]**. No macro enters **[M2000-094]**: the data-centre build-out, tariffs,
copper and gold prices and interest rates are not forecast here; they enter only as properties of the business, its
cyclicality and its freedom to price **[M2011-054]**. The margin of safety is an attitude here and arithmetic at Q7: a
decision that needs pencil and paper is "too close" **[M1996-084]**. Who is paid to tell you: the company's own outlook
("around the top end of our 5 to 7 percent compound annual growth rate (CAGR) target", 10-K FY2025, MD&A) is a seller's
projection and is not used **[M1995-050]**. **Contrary evidence, written down as found** **[M1997-127]**: (a) the
five-year owner-cash window 2021 to 2025 contains no trough year for a business whose own 10-K calls demand "highly
cyclical" (Critical Accounting Estimates, goodwill); the window flatters the base. (b) The 2025 price realization was
negative $817M overall and negative $1.136B in Construction Industries, the largest segment by sales; a business with
pricing power does not usually give back price in a year of record backlog. (c) Against the castle: the dealer agreements
"are terminable at will by either party primarily upon 90 days written notice" (Item 1). (d) For the castle: backlog
more than doubled in eighteen months and the 2026 first half shows price realization of +$1.0B.

## THE STANDING RULE
Owning this would be a cash purchase sized so that no fall in the quotation forces a sale: no borrowed money **[L2014-005]**,
nothing that lets "the other fellow" call the tune **[M2006-079]**, and "always be sure you can play the next day"
**[M2025-015]**. Caterpillar's own debt and Cat Financial's funding are the target's exposures and are weighed at Q9, not
here. **Clear, as to the buyer's conduct.**

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the industry.
Is there [...] are there competitive moats? Is there ease of entry?" **[M2011-014]**. A holding company, or a company that
files as two businesses, is understood by its parts (CONVENTION, Q1).

**The parts, from the filing.** (a) **MP&E**, three primary segments selling heavy machines, engines, turbines and
locomotives, and the parts and service that follow them, through "one of the largest independent global dealer networks"
(Item 1): 41 dealers in the United States and 109 outside, serving 190 countries, for whom "in most cases sales and
servicing of our products are the dealers' principal business" (Item 1). 2025 external sales: Construction Industries
$24.8B, Resource Industries $12.2B, Power & Energy $27.1B, of which Power Generation $10.3B, Oil and Gas $7.5B,
Industrial $4.1B, Transportation $5.3B (10-K FY2025, segment note). (b) **Financial Products**, Cat Financial and the
captive insurers: $25.2B of finance receivables at 2025-12-31 ($23.6B customer, $1.5B dealer), "typically secured by the
equipment purchased", match-funded by policy (Item 1).

**The key variables and how predictable they are** **[M1998-044]**. For MP&E: (1) the installed base and the parts and
service it pulls through the dealers; (2) Caterpillar's position against the named competitors, which the 10-K lists by
segment (Komatsu, Deere, CNH, Volvo, Hitachi, Sany, XCMG and others in machines; Cummins, Rolls-Royce Power Systems,
Siemens Energy and others in engines and turbines; Item 1); (3) the level of demand in construction, mining, oil and gas
and power generation, which the 10-K itself calls "highly cyclical and significantly impacted by commodity prices"
(Critical Accounting Estimates). The first two are slow-moving and readable from the filings. The third is not
foreseeable year by year: sales and revenues were $65.9B in 2012, $38.5B in 2016 and $67.6B in 2025, and profit swung
from $5.7B (2012) to a loss of $59M (2016) to $10.8B (2024) (XBRL `Revenues` and `ProfitLoss` from the 10-Ks of each
year, accessions in `Test Runs/_research 2026-10-06 CAT/hist_xbrl.txt`; transcription, not re-read against each filed
statement). The rows do not ask that the year be foreseen: "what difference does it make to us if the earnings average,
say, 300 million a year, if it comes in in a very lumpy fashion? [...] as long as it's a good business" **[M2011-102]**.
What must be foreseeable is the average over the cycle and "how far off we can be" **[M2011-084]**; the answer here is
"fairly far" on the level and "not far" on the position, and that width is carried to Q7, not settled here.

**Is the industry one that changes fast?** No, on the filing's evidence. The products are diesel and gas engines, steel
machines and turbines; the competitor lists name the same incumbents, and the technology agenda in the 10-K is
emissions compliance, autonomy and electrified powertrains, introduced over decades and sold through the same dealers.
The rows warn that "slow change can be much harder to perceive" **[M2014-038]**; electrification of mining and
construction machines is such a change, and is noted for Q2, test 11. It does not put the ten-year economics out of
reach the way "fast-moving technology" does **[L1993-023]**.

**Would the insiders write the forecast down?** **[M2000-105]**. A mining customer, a dealer or a Komatsu executive could
write down where Caterpillar will stand among the makers of large mining trucks and dozers in ten years; none could
write down 2030's copper price or data-centre build. The first is the understanding asked; the second is the cycle.

**Cat Financial, the bank door** **[M2002-022]**, **[M2011-022]**. Both sides can be read from the 10-K. The asset side:
receivables secured by Caterpillar equipment whose resale values the parent knows; customer receivables 91+ days past due
$182M, 31 to 90 days $272M, together $454M, 1.9% of $23.6B; write-offs $148M and recoveries $47M in 2025, $101M net or
about 0.4%; allowance $277M (10-K FY2025, Note 7, the aging and allowance tables). The funding side: $5.4B of commercial
paper backed by $11.5B of committed global credit facilities, the rest term debt rated mid-A, with a support agreement
from the parent (Item 7, Liquidity). Derivatives are described as hedges for match funding and currency (Item 1, Note 4),
not a trading book. The rows' warning about a finance company, "I don't understand that — whether I can continually fund
it [...] independent from using Berkshire's credit" **[M2002-094]**, applies in part: Cat Financial's funding leans on
Caterpillar's rating and support agreement. That is a Q9 exposure of the whole; it does not make the receivables unreadable.

**Doubt test** **[M2002-092]**. I have no doubt that the business (heavy iron sold and serviced through captive-like
dealers) is inside the perimeter; I do doubt the level of earnings in any given year, and the rows put that doubt in the
value range, not in the circle **[M2011-084]**.

**VERDICT: IN.** The ten-year competitive position and the economics of the industry can be foreseen from the filings;
the cycle cannot, and is carried to Q7 as range **[M2012-065]**, **[M2011-102]**; Cat Financial's two sides can be read
**[M2002-022]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what's going to keep it standing [...] five, 10, 20 years from now" **[M1995-038]**.
The 10-K's own answer is three things: the dealer network, the integration of key components, and the total cost of
ownership to the customer ("We believe our ability to control the integration and design of key machine components and
innovative technologies represents a competitive advantage"; Resource Industries, Item 1). Each is tested below with a
filing fact. The competitor figures are in `Test Runs/_research 2026-10-06 CAT/peers.txt`.

**1. The key factors and their permanence.** The installed base and the dealers who service it: 150 dealers covering 190
countries, dealers whose principal business is Caterpillar in most cases (Item 1). The rows name an installed base among
the things that protect a position ("No installed base, key patents, critical real estate or natural resource position
protects an insurer's competitive position", said of the business that lacks one) **[L2003-014]**. Against permanence:
the dealer agreements are "terminable at will by either party primarily upon 90 days written notice" (Item 1); the
dealers are independent and stay because the product line pays them, which makes the castle's permanence the product's,
not the contract's.

**2. Would it stand without the lord?** **[M1996-037]**. The chief executive changed in 2025 (Umpleby, CEO 2017 to 2025,
then executive chairman; Creed CEO; 8-K `0001104659-26-001346`), the CFO in 2026 (8-K `0001104659-26-042062`); the 2026
first half shows sales up 23% and price realization of +$1.0B (10-Q Q2 2026). Nothing in the filings ties the position
to one person.

**3. The money test** **[M2011-015]**, **[M1997-103]**. Could $100B displace Caterpillar from mining trucks, large dozers
and the parts business behind them? Not quickly: a rival would need a dealer and parts network in 190 countries and a
fleet in the field for its parts to serve. But the test has been run by the market, and the answer is mixed. The 10-K
names Sany, XCMG, LiuGong, SDLG and Shantui in China and says "Outside the United States, certain competitors enjoy
competitive advantages inherent to operating in their home countries or regions" (Item 1); Construction Industries' Asia/
Pacific sales fell 3% in 2025 (segment geography table). Written down as found **[M1997-127]**: the castle is not
impregnable abroad, and "one competitor is frequently enough to ruin a business" **[M2012-108]**.

**4. Pricing power and the agony before a rise** **[M2005-020]**. Price realization added $5.179B to ME&T sales in 2022
and $5.596B in 2023 (10-K FY2022 and FY2023, sales bridges), $1.238B in 2024 (10-K FY2024), took away $817M in 2025
(Construction Industries -$1.136B, Resource Industries -$272M, Power & Energy +$592M; 10-K FY2025), and added $1.0B in
the first half of 2026 (10-Q Q2 2026). Over four years the company raised price by roughly $11B net on an ME&T base of
$48.2B (2021) and kept most of it. "over time the businesses with strong competitive positions manage to pass through
increases in raw material costs [...] But you get these temporary situations" **[M2005-017]**; the 2025 giveback came in
the year tariffs added about $1.8B of cost (10-K FY2025 outlook: 2026 impact "$800 million higher than incurred in
2025", $2.6B), and in that year Deere's construction arm also cut price and lost more margin than Caterpillar did (row
below). The pricing record weighs for the castle; the 2025 Construction Industries giveback is the contrary fact.

**5. The competitor row (same metric, the competitors' own filings).**

| business | metric | 2025 | 2024 | source |
|---|---|---|---|---|
| Caterpillar Construction Industries | segment profit / sales | **18.7%** | 24.2% | 10-K FY2025, `0000018230-26-000008` |
| Deere Construction & Forestry (FY to 2025-11-02) | operating profit / net sales | **9.0%** | 15.5% | 10-K FY2025, `0001104659-25-122321` |
| CNH Construction | adjusted EBIT / net sales (filer's segment measure) | **2.3%** | about 5.5% ($169M) | 10-K FY2025, `0001567094-26-000006` |
| Caterpillar Power & Energy | (segment profit + segment D&A) / sales | **22.0%** | | 10-K FY2025 segment note (arithmetic) |
| Cummins Power Systems | segment EBITDA / sales | **22.7%** | 18.4% | 10-K FY2025, `0000026172-26-000009` |

In construction machines, in the same tariff year and with the same price pressure, Caterpillar earned twice Deere's
margin and eight times CNH's; that is the mark of the low-cost or best-priced producer in a field the rows call close to
a commodity, where "being the low-cost producer is all-important" **[L2000-017]**, **[M2018-043]**. In engines and
generator sets, Caterpillar and Cummins earn about the same, so there the position is shared, not dominant. Komatsu,
Volvo, Hitachi and the Chinese makers do not file with the SEC; their figures were not read, and the row is incomplete
without them.

**6. Would the customer still choose it over the low bid?** **[M2017-009]**. The 10-K splits the customers: in developed
economies they "generally weigh productivity and other performance criteria that contribute to lower owning and
operating costs over the lifetime of the machine", while "Customers in developing economies often prioritize purchase
price" (Item 1); Caterpillar answers the second group with a separate low-priced brand, SEM. In mining, customers "place
an emphasis on equipment that is highly productive, reliable and provides the lowest total cost of ownership" (Item 1).
The rows' test is met where downtime costs more than the machine, as with Precision Castparts, "where people don't simply
just take the low bid" **[M2016-006]**; it is not met in the price-led markets the company itself names.

**7. Is the moat widening or narrowing?** **[M1999-108]**, **[L2005-010]**. At roughly equal sales, the business earns more
than it did a cycle ago: sales and revenues $65.9B and profit $5.7B in 2012; $67.6B and $8.9B in 2025; the trough was a
small loss in 2016 on $38.5B of sales and a $3.0B profit in 2020 on $41.7B (XBRL history, transcription). A deeper
trough profit on similar trough sales, and a higher peak margin on similar peak sales, is evidence of a stronger
position, or of cost cutting, or both; the filings read do not separate the two. Contrary, written down: CI's 2025
margin fell 5.5 points while price went negative, and Chinese makers are named as advantaged at home.

**8. What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]**. (a) A slow shift of
construction and mining machines to electric drive and autonomy, which would reduce the parts and engine-rebuild stream
the installed base pays for; the 10-K lists "electrified powertrain and zero-emission power sources" as a product line
of its own, so the company is selling into the change, not only against it. (b) The Chinese makers moving from their home
market into the developing markets that buy on price. (c) A fall in Power Generation demand from data centres, now
$10.3B of external sales against $6.4B in 2023 (segment note): a demand risk, not a castle risk, and it belongs to the
cycle carried to Q7. None of these is shown on the evidence to be filling the moat in now.

**VERDICT: IN.** The castle is standing on evidence the filings carry: margins double the nearest filing rival's in the
same year **[L2000-017]**, four years of price kept against cost **[M2005-017]**, an installed base and dealer network a
well-funded attacker has not displaced outside China **[M2011-015]**. It is not a castle that "an idiot can run" in every
segment, and the low-bid markets are named by the company itself; those weigh on how sure the cash is, at Q7, not on
whether the castle stands **[M1999-108]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**Return on the capital actually needed** **[M2010-090]**, measured on tangible assets **[M2011-060]**. MP&E's net
tangible operating capital at 2025-12-31, from the MP&E column of the supplemental balance sheet: total assets $60,061M
less cash $9,333M, goodwill $5,321M and intangibles $241M, less the non-interest-bearing liabilities (accounts payable
$8,988M, accrued expenses $4,877M, accrued wages $2,494M, customer advances $3,311M, dividends payable $703M, other
current $2,259M) = **$22,534M** ($20,927M at 2024-12-31). On it, MP&E operating profit of $10,884M is a 48% pre-tax
return, 2025 owner cash of $9,242M is 41% after every real cost, and the five-year mean owner cash is 35% (arithmetic in
`arith.py`). The segment note agrees in shape: the three machine segments' assets total $22.9B against $13.1B of
segment profit in 2025.

**Read with care before it is credited** **[L1994-009]**: "a cyclical peak in earnings, a monopolistic position, or
leverage". Leverage: no; MP&E's own long-term debt is $11.0B against $9.3B of cash. Cyclical peak: in part, yes. The five
years 2021 to 2025 are recovery and boom years; in 2016 the whole company lost money on $38.5B of sales, so the return
across a full cycle is lower than any figure above, and the filings read do not give MP&E's capital in 2016 to measure it.
Unprecedented returns are not assumed to last **[M1998-016]**.

**Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. MP&E capital spending was $8,872M over
2021 to 2025 against $7,215M of MP&E depreciation and amortization; in 2025 it was $2,794M against $1,497M, and the
company plans "about $3.5 billion" for 2026 (Item 7). The segment note says where it went: Power & Energy capex rose
from $944M (2023) to $1,279M (2024) to $1,774M (2025), capacity for engines and turbines, while Construction Industries
($358M) and Resource Industries ($353M) stayed near their depreciation ($266M, $252M). So depreciation is a fair proxy
for the spending that keeps the machine business in place **[L2000-035]**, and the excess is growth spending in one
segment whose return is not yet shown. Working capital grows with volume: inventories rose from $11.5B (2018) to $18.1B
(2025) (`tools/run.py` balance-sheet table, read against Statement 3), faster than sales, though against a backlog that
rose from $30.0B to $51.2B in 2025 alone.

**The growth arithmetic and its caps** **[M1997-095]**, **[M1999-067]**. Owner cash grew 12.1% a year from 2021 to 2025
on the aggregate figure; across a full cycle the business grew far less: sales and revenues $65.9B in 2012 and $67.6B in
2025 (0.2% a year), profit $5.7B and $8.9B (3.4% a year) (XBRL history). The shown rate is a within-cycle recovery, and
carried ten years from a boom base it would put owner cash near $29B by 2035 on a business whose sales did not grow in
nominal terms over thirteen years; that is the kind of result the rows tell the analyst to "change expectations"
about **[M1999-067]**. Q7 carries the shown rate as the convention requires and shows the capped readings beside it.

**WEIGHS FOR**, with the cycle written against it: the machine business earns very high returns on the tangible capital
it needs and reinvests about its depreciation to stand still **[M1995-051]**, **[L2009-012]**; but the five-year figures
are taken near a peak, the long-run growth of the business is low, and the new capital is going into the segment whose
demand is newest **[L1994-009]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
*(to be written)*

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
*(to be written)*

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
*(to be written)*

## Q7 — WHAT IS IT WORTH? STOP.
*(to be written)*

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
*(to be written)*

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
*(to be written)*

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
*(to be written)*

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
*(to be written)*

---
## THE BOX
*(to be written)*

## SELF-AUDIT
*(to be written)*

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
*(to be written)*
