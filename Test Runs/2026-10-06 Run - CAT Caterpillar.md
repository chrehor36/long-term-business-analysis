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
countries, dealers whose principal business is Caterpillar in most cases (Item 1); "Services revenues [...] totaled $24
billion in 2025" (DEF 14A 2026, CD&A; aftermarket parts and service, a non-GAAP figure the 10-K defines but whose total
the 10-K text read does not print), over a third of MP&E's $64.0B of sales. The rows name an installed base among
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
**The balance sheets first, eight years of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL, read against
Statement 3 for 2024 and 2025; USD millions):

| year-end | equity | retained earnings | cash | receivables (trade) | inventory | goodwill | intangibles | LT debt |
|---|---|---|---|---|---|---|---|---|
| 2018 | 14,080 | 30,427 | 7,890 | 8,802 | 11,529 | 6,217 | 1,897 | 25,000 |
| 2020 | 15,378 | 35,167 | 9,352 | 7,317 | 11,402 | 6,394 | 1,308 | 25,999 |
| 2022 | 15,891 | 43,514 | 7,004 | 8,856 | 16,270 | 5,288 | 758 | 25,714 |
| 2024 | 19,494 | 59,352 | 6,889 | 9,282 | 16,827 | 5,241 | 399 | 27,351 |
| 2025 | 21,318 | 65,448 | 9,980 | 10,920 | 18,135 | 5,321 | 241 | 30,696 |

What the figures say: retained earnings rose $35.0B from 2018 to 2025 while equity rose $7.2B, the difference having
gone out as dividends and repurchases (treasury stock $49.5B at 2025-12-31, Statement 3); goodwill and intangibles fell
from $8.1B to $5.6B, so no acquisition spree is hiding in the assets, and the intangibles are amortizing away; long-term
debt rose $5.7B, mostly at Cat Financial (MP&E long-term debt $11.0B, Financial Products $21.0B, supplemental balance
sheet); trade receivables grew about in line with sales ($54.7B in 2018, $67.6B in 2025). What moved out of line:
**inventory**, from 21% of sales (2018) to 27% (2025). The rows ask the analyst to "look twice" when inventories "look out
of line [...] with sales" **[M1995-064]**; here the 10-K offers the backlog ($51.2B against $30.0B) and customer advances
($3.3B against $2.3B) as the reason, and the 2026 first half (sales +23%) is consistent with it. Recorded, not a tell.
What the figures cannot say: the cycle. Every year-end in the table is after 2017; the balance sheet at the 2016 trough
was not read.

**The real costs.** Depreciation is charged in full in owner cash and capex runs above it. Stock pay ($242M in 2025) is
expensed in GAAP profit and subtracted in owner cash **[L2021-003]**; options are valued and expensed (Note 3). Pensions:
U.S. pension benefits frozen at 2019-12-31, and actuarial gains and losses are marked to market through earnings each
year (Critical Accounting Estimates), so no smoothing is hidden in the pension line. Taxes: the $717M IRS settlement paid
in 2022 ("without any penalties", 10-K FY2022) is counted as the real cost it was.

**EBITDA in the filer's own mouth:** no instance found in the 10-K FY2025 or the Q2 2026 earnings release (text search
for "EBITDA" in both extracts).

**Adjusted earnings, and the recurring "one-time".** The earnings release puts "Adjusted Profit Per Share" in its headline
table beside GAAP ($8.17 against $7.77 for Q2 2026; 8-K `0000018230-26-000040`, EX-99.1), and the adjustment is
restructuring costs. Restructuring costs have been charged in every year read: $207M (2019), $241M (2020), $90M (2021),
$299M (2022), $780M (2023), $359M (2024), $445M (2025) (segment-to-consolidated reconciliations, 10-Ks FY2021, FY2023,
FY2025), and the 10-K guides to "$300 million to $350 million" more in 2026. A cost that recurs for seven years is a cost
of doing business; the rows' words for telling owners "year after year, 'Don't count this'" are "misleading"
**[L2016-007]**, and a management that features adjusted earnings "makes us nervous" **[L2016-006]**. The company's
"MP&E free cash flow" likewise added back the 2022 IRS payment. Against that: GAAP figures are given first, the
reconciliation is complete, the adjustment is symmetric for pension marks (gains are removed as well as losses), the
$392M IEEPA tariff recovery of Q2 2026 was left in adjusted profit just as the tariff costs had been, and the 10-K reports
MP&E and Financial Products separately, which is the reporting the rows ask for **[L2008-005]**.

**The make-the-numbers habit.** No earnings-per-share target was found in the 10-K or the release; the company states a
sales growth target ("5 to 7 percent compound annual growth rate (CAGR) target") and margin ranges. No second tell from
the list was found: no reserve releases flagged, no prepaid or deferred accounts building, no securitization gains
(proceeds from sale of finance receivables $71M in 2025, small). One tell, adjusted earnings featured over a recurring
cost, is a weighing against, not a STOP (Q4, the two-tell line, CONVENTION) **[L2002-039]**, **[M1994-018]**.

**VERDICT on confusion: IN.** The accounts can be read, the two businesses are reported apart, and the cash figures
reconcile to the filed statements **[M2025-032]**. **WEIGHS AGAINST**, lightly: adjusted profit is featured over
restructuring costs that recur every year **[L2016-007]**, **[L2016-006]**. The recast earnings fed to Q7 are owner cash,
which counts every restructuring dollar and every tax payment.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
This is a marketable stock; the speakers "read rather than meet" for one, and the after-the-sale test belongs to whole
purchases **[M2007-081]**. The reading tests are applied to the 10-K, the proxy and the release.

**The two yardsticks** **[M1994-008]**. *How well they run the business, against the hand dealt:* in the same tariff year,
Construction Industries earned 18.7% on sales against Deere's 9.0% and CNH's 2.3% (Q2, competitor row); the company
earned $3.0B in the 2020 trough on $41.7B of sales where it had lost money in 2016 on $38.5B (XBRL history); price was
raised by about $11B net over 2022 to 2025 and largely held (Q2). *How they treat the owners:* the proxy ties the annual
bonus to "Operating Profit After Capital Charge", operating profit less "average quarterly MP&E net assets multiplied by a
pre-tax capital charge rate of 13 percent" (DEF 14A 2026, CD&A), which is the rows' own rule that a manager pays for the
capital he uses **[L1994-019]**, **[M1995-010]**; the new CEO's equity grant and salary were set at "approximately the 25th
percentile of the compensation peer group" (CD&A); his annualized 2025 pay was $17.5M, 196 times the median employee
(CEO pay ratio), against $8.9B of profit. Stock ownership guidelines (six times salary for the CEO) and "Strict
anti-hedging and anti-pledging policies" are stated (CD&A). The two often go together **[M1994-009]**, and here both read
for the managers.

**The tells of dishonesty.** (a) Reports: the 10-K tells an owner what he would want to know **[M1998-036]**: it splits the
machine business from the finance company, gives the finance book's aging by origination year and region, quantifies
tariff costs each quarter and says how much price was given up, segment by segment. (b) The adjusted-profit habit (Q4)
is a weighing against, and it is the only tell found. (c) The CSARL tax dispute: the IRS contested the treatment of parts
profits booked in a Swiss subsidiary and proposed "accuracy related penalties"; the company "vigorously contested" and
settled in 2022 for tax years 2007 to 2016 "without any penalties" (10-K FY2022, `0000018230-23-000011`). Aggressive tax
structuring settled without penalty is not a finding of dishonesty toward owners; it is recorded for Q12. (d) Language:
the 10-K and release are written in a corporate register ("Values in Action", "three profitable growth pillars"), which
the rows read as the mark of an investor-relations product **[M2007-083]**; no instance found of management discussing a
mistake in the documents read (text search of the 10-K and release for "mistake" and "wrong"), which the rows note
without making it a stop **[L2024-003]**. No instance of a chairman's letter was read; the 10-K carries none.

**Love of the business, and after being paid.** Not testable from the filings for a hired chief executive of a 100-year-old
company, beyond tenure: the new CEO, the new CFO and the departing executive chairman are career Caterpillar executives
(the departing chairman with "forty-five years of service", 8-K `0001104659-26-001346`).

**VERDICT on integrity: IN.** No doubt of the kind the rows act on was found **[M2013-088]**; the capital charge in the
bonus and the reporting of the two businesses apart read the other way **[L1994-019]**, **[M1998-036]**. **Ability WEIGHS
FOR**: margins against the hand dealt and against the filing rivals, and a shallower trough in 2020 than in 2016
**[M1994-008]**. Ability enters the value as certainty, not as a gate **[M1999-104]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.** *The stated policy:* "Our goal is to return substantially all MP&E free cash flow to shareholders
over time in the form of dividends and share repurchases, while maintaining our mid-A rating" (10-K FY2025, Item 7).
*The retention test* **[M1998-033]**, **[M2008-104]**: profit 2021 to 2025 was $43.2B; dividends paid were $12.7B ($2,332M,
$2,440M, $2,563M, $2,646M, $2,749M) and repurchases cost $24.8B ($2.7B, $4.2B, $4.7B, $8.0B, $5.2B; Note 16 of the 10-Ks
FY2023 and FY2025 and the 2022 equivalent), so about $5.7B was kept, roughly the growth in working capital and plant the
volume needed (Q3). Little is retained, so the test of a retained dollar is barely engaged; what is engaged is the price
of the repurchases.

*Buybacks* **[L1999-023]**, **[L2011-003]**. The company names no price above which it stops; it names a sum, "substantially
all" of free cash flow, which is the form the rows distrust: repurchase announcements that "almost never refer to a price
above which repurchases will be eschewed" **[L2016-002]**, and buying "to prevent dilution" or on a schedule rather than
"related to valuation" **[M2016-049]**. The prices actually paid, from the filings:

| period | shares | cost | average |
|---|---|---|---|
| 2021 | 13.0M | $2.7B | about $208 |
| 2022 | 21.9M | $4.2B | about $192 |
| 2023 | 19.5M | $4.7B | about $241 |
| 2024 | 23.4M | $8.0B | about $342 |
| 2025 | 14.1M | $5.2B | about $368 |
| first half 2026 | 7.0M received | $4.9B | about $700 (April $766.00, May $890.17, June $947.20) |

(10-K FY2022, FY2023, FY2025 repurchase notes; 10-Q Q2 2026 repurchase note and Part II Item 2; averages are cost over
shares, arithmetic.) The two Q1 2026 ASRs advanced $4.5B for an initial 4.8M shares "approximately 70% of the estimated
final number" (10-Q Q2 2026), so the final average for the first half depends on prices through settlement.
**The test against the Q7 range** (CONVENTION, Q6, recorded back from Q7): the bottom of the Q7 range is **$300** a share
and the top **$781**. Purchases in 2021 to 2023 were made at well under the bottom of the range; those of 2024 and 2025 sat
inside the range, above its bottom; those of 2026 were near or above its top. The programme was bought at good prices when
the stock was cheap and kept buying at the same pace, or faster, after it was not: $4.9B in six months of 2026 against
$5.2B in all of 2025. The rows: "what is smart at one price is dumb at another" **[L2011-003]**. **Weighs against** for the
2026 purchases.

*Issuance and deals:* no stock-paid acquisition was found in the filings read; the one deal of 2026 is RPMGlobal, mining
software, about $790M in cash (10-K FY2025, Item 7). The Part A STOP **[L2009-019]** is not engaged.
*Dividends:* maintained at $1.51 a quarter in December 2025 (Item 7); paid for 32 consecutive years of increases by the
proxy's account (DEF 14A, CD&A); "clear, consistent and rational" **[L2012-015]**.

**Part B, the pay, the board and the owners.** For: the annual bonus is tied to operating profit after a 13% pre-tax charge
on MP&E net assets, to enterprise operating profit and to services revenues (CD&A, 2025 annual incentive measures), all
"under the reasonable control" of the people measured **[M2003-019]**, and the capital charge is the rows' own design
**[L1994-019]**. Against: the long-term grant is 50% performance units on three-year average ROIC and relative total
shareholder return, 25% time-based units and 25% stock options (CD&A); the options carry no step-up for retained earnings
**[L1994-021]**, and the relative-TSR half pays for the quotation rather than the business **[M2000-062]**; pay is benchmarked
against a compensation peer group using the "Aon Total Compensation Measurement Database" with an "independent
compensation consultant" (CD&A), the comparative machinery the rows distrust **[L2005-015]**, **[M2004-016]**; restructuring
costs are excluded from the bonus measure of operating profit (CD&A), the same recurring cost Q4 noted. The board: from
2026-04-01 the chief executive is also chairman, with a lead independent director (8-K `0001104659-26-001346`); the rows
find it "hard to replace a mediocre CEO if that person is also Chairman" **[L2014-026]**, which matters only if he is
mediocre, and nothing here says so. "There are more problems with having the wrong manager than with having the wrong
compensation system" **[M2007-006]**.

**WEIGHS AGAINST (Part A)**: a buyback sized to cash flow, with no stated price, now buying near or above the top of the
Q7 range **[L2016-002]**, **[L2011-003]**. **WEIGHS FOR (Part B)**, narrowly: the capital charge in the bonus outweighs the
option and peer-group design **[L1994-019]**, **[M2007-006]**.

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
