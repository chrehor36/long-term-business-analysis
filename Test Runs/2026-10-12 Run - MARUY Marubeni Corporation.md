# Company Run: Marubeni Corporation (TSE: 8002; US ADS: MARUY), 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`. Every judgment cites a v5 ledger id in bold; Marubeni files no periodic report with
the SEC, so each filing fact carries the company document and its date in place of an accession number (operator rule 5,
the brief). A STOP that returns OUT or TOO HARD closes the run; later questions are marked NOT REACHED.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session (overnight cycle, 2026-10-12), after the run was committed: `PORTFOLIO.md` names no Marubeni Corporation (8002, MARUY); not held.*

**Contamination, declared:** the directory listing made when the run file was created showed other run files dated
2026-10-12 by name only, including "ITOCY ITOCHU Corporation", "MITSY Mitsui and Co", "MTSUY Mitsubishi Corporation" and an
addendum titled "the MTSUY brief that ran Mitsui, the dispatcher's ticker error"; the recent-commit subjects in the session
header named an ITOCY run closed "OUT at Q7 on the floor". None of these files was opened, listed further or searched. The
framework's own text (Q1, A holding company; Q4, Equity-method income) names a "MITSY regression run"; that is the governing
document, read as required. Nothing from any of these was used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING

- **Price, Tokyo:** JPY 4,702 (TSE close 2026-10-09, the last session before the price date; 2026-10-12 is a Japanese
  holiday). Source: Yahoo Finance chart API, 8002.T (an aggregator, flagged, live quote only, operator rule 5).
- **Price, ADS:** $29.74 (MARUY close 2026-10-12, same aggregator, flagged). **ADS ratio used: one ADS = one share.** The
  three F-6 POS amendments on EDGAR (CIK 801645) each state it: Citibank, N.A., filed 2026-06-02 (accession
  0001193805-26-000735: "each ADS representing the right to receive one (1) share of common stock"); JPMorgan Chase Bank,
  N.A., filed 2026-07-07 (0001193805-26-000925: "each American Depositary Share representing one share of common stock");
  Deutsche Bank Trust Company Americas, filed 2026-07-09 (0001104659-26-082191: "filed to reflect a change in the ratio").
  *(The brief named JPMorgan for the 2026-06-02 filing; that filing's depositary is Citibank.)* **No share split was found in
  the company's documents:** issued shares are 1,660,758,361 at both 2026-03-31 and 2026-06-30 (Q1 FY2026 earnings release,
  2026-08-03), and a text search of every company document downloaded for this run for "share split" and "stock split" found
  none; the ratio change is a depositary change only, so per-share figures are on the ordinary-share basis throughout.
  Cross-check: JPY 4,702 / USDJPY 158.06 (2026-10-08, same aggregator, flagged) = $29.75 against $29.74.
- **Shares:** `python Screens/cover_shares.py MARUY` returned "NOT AN SEC REGISTRANT"; `python tools/run.py MARUY` returned
  "not an SEC filer... UNRESEARCHED, not UNKNOWABLE". Neither tool was used further; every figure below is from the
  company's own documents. Issued 1,660,758,361 less treasury 33,979,475 at 2026-06-30 (Q1 FY2026 earnings release) =
  1,626,778,886; less 5,554,700 shares bought 2026-08-04 to 2026-09-30 under the resolution of 2026-08-03 ("Notice
  Regarding the Progress of Share Repurchases", 2026-10-01) = **1,621,224,186 shares outstanding** (treasury disposals for
  stock pay after 2026-06-30, if any, not found and not added).
- **Market cap:** JPY 4,702 x 1,621.2 million = **JPY 7,623 billion** (about $48.2 billion at 158.06).
- **Sovereign for the earnings currency (JPY):** **4.136%**, the 30-year JGB on 2026-10-08 (the last row), Japan Ministry of
  Finance `jgbcme.csv`, fetched 2026-10-12 (saved as `_research 2026-10-12 MARUY/jgbcme.csv`). The 30-year tenor is used to
  match the protocol's 30-year USD series; the 20-year was 3.916% and the 10-year 3.089% the same day.
- **Filings read** (operator rule 4; no accession numbers exist, document and date given instead):
  - Consolidated Financial Statements with Independent Auditor's Report (English, audited, IFRS) for FY2025 (year to
    2026-03-31), posted 2026-06-12; and the same document for each of FY2016 to FY2024 (posted 2017-08-29, 2018-08-29,
    2019-07-08, 2020-07-20, 2021-07-28, 2022-06-24, 2023-06-23, 2024-06-21, 2025-06-17), from the company's IR library
    (ssl4.eir-parts.net/doc/8002/ir_material_for_fiscal_ym19/...). FY2015 is read from the FY2016 document's comparative.
  - Integrated Report 2026 (marubeni.com/en/ir/reports/integrated_report/pdf/2026_en_all.pdf): Financial Data (p. 70),
    the Metals & Mineral Resources division pages, the CFO message.
  - Summary of Consolidated Financial Results for FY2025 (2026-05-01) and for Q1 FY2026 (2026-08-03); Full-year IR
    Presentation FY2025 (updated 2026-06-18); Q&A condensed transcript (2026-05-01).
  - Notices: share repurchases (2026-08-03; progress 2026-10-01); judicial review in the Sugar Group litigation
    (2026-01-21); articles amendment (2026-04-17); remuneration plan revision (2026-06-19).
  - The Annual Securities Report (yuho) in Japanese and the proxy-equivalent convocation notice were not read; the English
    audited statements carry the figures used.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 = JPY 535,398
  million in the audited Consolidated Statement of Cash Flows (p. 18), against JPY 535.4 billion in the Integrated Report's
  Financial Data table and the FY2025 earnings release. They agree. Net interest-bearing debt at 2026-03-31: bonds and
  borrowings 471,738 + 1,938,239 less cash 551,064 and time deposits 208 = JPY 1,858,705 million, against the company's
  JPY 1,858.7 billion. They agree.

**Owner cash, recast from the audited cash flow statements** (JPY billion; `_research 2026-10-12 MARUY/scripts/ownercash.py`).
Owner cash (equity) = cash from operations (which already contains interest and tax paid, the working-capital change, and
the dividends actually received from equity-method investees) plus cash from investing (every purchase of plant, of
subsidiaries and of investments, net of sales of each, and loans and time deposits) less the principal of lease liabilities
repaid (carried inside "Repayments of long-term bonds and borrowings"; read from each year's note on changes in liabilities
arising from financing activities) less distributions on the hybrid "other equity instruments" (redeemed in full by
FY2023). Never a net-income proxy (operator rule 5). All-equity adds back net interest after tax.

| FY (to Mar) | OCF | ICF | net plant | net purchases of businesses | lease principal | owner cash (equity) | before purchases | all-equity | net profit to owners |
|---|---|---|---|---|---|---|---|---|---|
| 2015 | 359.1 | (174.6) | 232.8 | (43.6) | n/a (pre IFRS 16) | 184.5 | 140.9 | 198.0 | 62.3 |
| 2016 | 324.3 | 46.5 | 41.3 | (61.9) | n/a | 368.8 | 306.9 | 382.7 | 155.4 |
| 2017 | 253.4 | (49.7) | 87.6 | (17.6) | n/a | 199.7 | 182.1 | 217.4 | 211.3 |
| 2018 | 284.9 | 22.5 | 87.2 | (90.3) | n/a | 303.4 | 213.1 | 326.2 | 230.9 |
| 2019 | 327.0 | (209.8) | 101.2 | 132.4 | 55.8 | 57.5 | 189.9 | 83.3 | (197.5) |
| 2020 | 397.1 | (116.3) | 117.0 | 0.7 | 55.5 | 221.4 | 222.1 | 232.0 | 223.3 |
| 2021 | 311.9 | (79.7) | 87.7 | (13.5) | 56.2 | 172.9 | 159.4 | 181.7 | 424.3 |
| 2022 | 606.3 | 156.8 | 86.3 | (265.4) | 59.6 | 700.9 | 435.5 | 723.1 | 543.0 |
| 2023 | 442.5 | (334.4) | 131.7 | 198.4 | 74.7 | 32.1 | 230.5 | 64.8 | 471.4 |
| 2024 | 597.9 | (395.3) | 164.8 | 233.0 | 79.3 | 123.3 | 356.3 | 163.8 | 503.0 |
| 2025 | 535.4 | (118.0) | 129.2 | 18.4 | 75.6 | 341.8 | 360.2 | 380.4 | 543.9 |

Five-year averages FY2021 to FY2025: owner cash (equity) 274.2; before purchases 308.4; all-equity 302.8; reported net
profit 497.1. **Owner cash ran at about 55% of reported net profit over the five years.** The gap is chiefly the share of
profit of equity-method investees (FY2025: 338.3 booked, 220.9 received as dividends), the investing outflows, and lease
principal. Net purchases of businesses over the five years were 170.9 against half of owner cash before purchases of 770.9,
so the serial-acquirer specific does not apply. FY2022 carries the sale of a subsidiary for JPY 330.1 billion (proceeds from
sale of subsidiaries, FY2022 cash flow statement). Depreciation and amortisation FY2025: 209.1; stock pay is small
(stock-compensation-type options at JPY 1 a share and restricted stock, Note 20; not quantified here).

**The balance sheets, ten years and more, read first** **[M2025-032]** (Integrated Report 2026, Financial Data, JPY billion;
FY2024 and FY2025 checked against the audited statements):

| FY | Total assets | Shareholders' equity | Net interest-bearing debt | Net DE (x) | ROE (%) |
|---|---|---|---|---|---|
| 2014 | 7,673.1 | 1,518.5 | 2,887.6 | 1.90 | 7.3 |
| 2015 | 7,117.7 | 1,317.1 | 2,762.5 | 2.10 | 4.4 |
| 2016 | 6,896.7 | 1,683.7 | 2,099.9 | 1.25 | 11.1 |
| 2017 | 6,877.1 | 1,771.5 | 1,915.8 | 1.08 | 14.0 |
| 2018 | 6,809.1 | 1,977.7 | 1,858.8 | 0.94 | 13.9 |
| 2019 | 6,320.0 | 1,515.5 | 1,859.1 | 1.23 | (13.4) |
| 2020 | 6,935.7 | 1,814.8 | 1,687.9 | 0.93 | 15.5 |
| 2021 | 8,255.6 | 2,242.2 | 1,860.0 | 0.83 | 23.0 |
| 2022 | 7,953.6 | 2,877.7 | 1,483.1 | 0.52 | 22.4 |
| 2023 | 8,923.6 | 3,459.7 | 1,902.4 | 0.55 | 15.2 |
| 2024 | 9,202.0 | 3,629.2 | 1,965.5 | 0.54 | 14.2 |
| 2025 | 10,531.8 | 4,363.7 | 1,858.7 | 0.43 | 13.6 |

What the balance sheets say: equity nearly tripled from FY2015 to FY2025 while net debt fell by a third; leverage came down
from 2.10 to 0.43 times. Equity fell twice, by JPY 201 billion in FY2015 and JPY 462 billion in FY2019, the two years of
large impairments. What they do not say on their face: much of the equity growth is currency. In FY2025 total comprehensive
income to owners was JPY 967.7 billion against net profit of 543.9, the difference chiefly foreign-currency translation
(333.4 on the group and 426.4 through associates; audited statement of comprehensive income, p. 13-14). Investments in
associates and joint ventures were JPY 3,504.2 billion, 33% of total assets, at 2026-03-31; the auditor names their
impairment indicators a key audit matter. Intangible assets were JPY 341.2 billion. At 2026-06-30 net interest-bearing debt
was JPY 2,050.5 billion and non-controlling interests JPY 150.3 billion (Q1 FY2026 release).

---
## THE FOUNDATIONS (not a gate)

A share is a business: the test is whether this would be owned content if the market closed for years **[M1997-109]**. The
market serves and does not instruct; the price is read against where the facts lead, not as a signal **[M2006-077]**. The
margin of safety foundation bears on the end: if the decision needs pencil and paper it is too close **[M1996-084]**. No
macro forecast enters: "macro conclusions are — just never enter into the discussion" **[M2000-094]**; the commodity version
of that rule is the speakers' own, "we have no opinion on commodities" **[M2007-129]**, and it matters here because a third
of this company's profit is copper, iron ore and steelmaking coal. Who is paid to tell you: Marubeni's report prints a Wood
Mackenzie copper supply-demand gap; it is a forecast of a commodity, read as a seller's projection and not used.

**Contrary evidence, written down as found** **[M1997-127]**:
- Antofagasta's Annual Report 2025 (the operator of Marubeni's Chilean copper mines; LSE, no SEC filing) gives Centinela a
  2025 net cash cost of $0.75/lb and Los Pelambres $0.82/lb, low on any cost curve. This pulls toward a standing castle in
  the deciding part, against the reading in Q2. (It is weighed there; see Q2.)
- The company's resources business earned a 13% to 14% return on invested capital in FY2024 and FY2025 by its own
  measure (Full-year IR Presentation FY2025, p. 14), above the group's 8%.
- Owner cash grew between the two halves of the decade (all-equity average 248.3 for FY2016-20, 302.8 for FY2021-25), the
  balance sheet de-levered, and the share count fell.
- The speakers bought this company's shares as one of five trading houses, "understandable companies" **[M2023-031]**, and
  named it in praise of their share policies **[L2023-008]**. Under the framework's convention on a row about one company these
  are weighed, never a STOP alone (Q2, A row about one company).

## THE STANDING RULE

The rule binds the buyer: "We are never going to risk what we have and need for what we don't have and don't need"
**[M2012-081]**; "Never risk permanent loss of capital" **[L2023-005]**. A purchase of this listed share for cash, unlevered
and sized by the buyer, puts the buyer at no risk of ruin; borrowing to buy it, or a size that a 50% fall would make
unbearable, would break the rule **[M2004-065]**. Nothing in the run depends on how it would be financed.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**Which part must be understood.** Q1's holding-company paragraph (CONVENTION, the framework's) asks that each part that
matters be understood, a part mattering when it decides under Q2: more than half of five-year operating profit, or else the
largest part. Marubeni reports segment profit only as net profit attributable to owners (Note 4 of each year's audited
statements); no segment operating profit is filed, so the segment net profit is used *(CONVENTION of this run: the
framework's threshold names operating profit; the filer reports none by segment; rationale: the filed measure is the only
one available for every year, and it is the measure management allocates by)*. Segments were reorganised in FY2022,
FY2023, FY2024, FY2025 and FY2026; each year's own figure is taken as first published or restated in the next year's
statements.

| Part (segment) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Five-year | Share |
|---|---|---|---|---|---|---|---|
| Metals & Mineral Resources | 190.7 | 199.4 | 163.5 | 123.5 | 134.3 | 811.4 | 32.6% |
| Finance, Leasing & Real Estate (next largest) | 7.0 | 43.7 | 43.9 | 59.1 | 162.0 | 315.8 | 12.7% |
| Consolidated net profit to owners | 424.3 | 543.0 | 471.4 | 503.0 | 543.9 | 2,485.6 | 100% |

No part carries more than half; **Metals & Mineral Resources is the largest and decides.** It is, in the filer's words,
"Mine development, production and sale of copper, iron ore, and steelmaking coal; Smelting and refining of copper and
aluminum" (Integrated Report 2026, Metals & Mineral Resources division), held mainly as minority interests accounted for by
the equity method (share of profit of associates in the segment FY2025: JPY 128.7 billion of 134.3; investments in
associates JPY 1,159.7 billion; Note 4). Its operators are partners: Antofagasta at the Centinela, Antucoya and Los
Pelambres copper mines in Chile; Roy Hill (iron ore) and the Jellinbah Group (steelmaking coal) in Australia. Equity copper
sales were 132 thousand tons and equity steelmaking coal 6.7 million tons in FY2025 (IR Presentation FY2025, p. 16).

**The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**. The key variables **[M1998-044]** of the deciding part are the prices of copper,
iron ore and steelmaking coal, the by-product gold price (see Q2), the mines' unit costs, and their volumes and reserve life.
The prices are not predictable, and the speakers say so of themselves: "We don’t think we can predict commodity prices"
**[M2016-025]**; of copper over ten years, "I don’t know of people who I feel would have an edge" **[M2011-047]**. But the
rows do not treat a commodity producer as outside understanding for that reason. They say how such a business is understood:
"If we owned a copper mining company in its entirety, we would measure it, probably, more by cost of production than we
would by whether copper was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**; and "It’s like comparing a copper
producer whose costs are $2.50 a pound with a copper producer whose costs are $1 a pound. Those are two different kinds of
businesses" **[M2009-059]**. On that reading the knowable and important variable **[M2006-076]** is the cost position
against the industry, the forecastable range of earning power follows from it across the price cycle, and the price itself
is the thing not paid for **[M2006-004]** and not forecast **[M2007-129]**. The industry does not change fast; the routing
that closes a business at Q1 TOO HARD is for fast change **[L1993-023]**, which mining is not. The past statements do tell
the shape of the future ones (test 3): eleven years of segment results show the swing, from a combined Energy & Metals loss
of JPY 142.4 billion in FY2015 to Metals profits of JPY 199.4 billion in FY2022.

Abroad (test 11): Japanese governance and tax are read from the filer's own English statements and governance report; the
company moved to a three-committee board in 2026 (articles amendment notice, 2026-04-17). The rows allow an understood
business abroad at a better price rather than a pass **[M2006-021]**, **[M2000-141]**.

The holding company as a whole: the speakers bought this company as one of five houses "that we could understand as a
group, although it didn’t mean we had deep understanding on any" **[M2023-031]**. That row is OPEN against the by-parts
convention and is weighed, not decisive. Doubt about the whole (hundreds of businesses across ten segments) is real; the
convention puts the test on the deciding part, and the doubt that remains is carried into Q2 rather than resolved here
**[M2002-092]**.

Contrary note on this verdict, written down: an oil producer's outcome "is going to depend on the price of oil to a great
extent" **[M2020-035]**; the same is true of a copper, iron-ore and coal portfolio, and a stricter reader would close Q1
TOO HARD (NATURE) on that row. It is not followed here because the speakers' own copper and cost rows **[M2006-004]**,
**[M2009-059]** give the way such a business is understood, and the question they leave is the castle (Q2), not the
foresight.

**VERDICT: IN.** The deciding part is a commodity producer understood by its cost position **[M2006-004]**, **[M2009-059]**,
in an industry that does not change fast **[L1993-023]**; the commodity prices are not forecast **[M2016-025]** and pass to
Q2 and Q7 as the castle and the cycle.

---
## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.

The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. It is asked of the deciding
part (Q1's parts table), as the business-of-parts paragraph directs **[L2008-005]**.

**What kind of business the deciding part is.** Copper cathode and concentrate, iron ore and steelmaking coal are sold at
world prices; the buyer does not ask for Marubeni's copper by name, and the producer takes the price the market sets, the
position of the gas station whose neighbour "determined our profit" **[M2023-079]**, **[M2012-109]**. The segment's results
move with the London Metal Exchange price: management's own sensitivity is "approx. JPY1.3 bn/[USD100/ton]" of copper, and
it explains FY2025's rise with a commodity effect of "Copper +24.0 bn" (IR Presentation FY2025, p. 4 and p. 16). In such a
field the rows allow one castle: "when a company is selling a product with commodity-like economic characteristics, being
the low-cost producer is all-important" **[L2000-017]**; "commodity businesses have risk unless you’re the low-cost producer"
**[M1997-010]**; "Another way to prosper in a commodity-type business is to be the low-cost operator" **[L2004-007]**; a
formidable barrier "such as a company's being the low-cost producer" **[L2007-004]**. So the castle question for this part
is one question: is it the low-cost producer, durably?

**The tests, each with its filing fact.**
1. *The cost position, now* (test 6; the speakers' own measure for a copper miner **[M2006-004]**). From the operator's
   filing (Antofagasta plc, Annual Report and Financial Statements 2025, Production statistics, p. 248; LSE-listed, no SEC
   filing, so its own report is the primary document): 2025 net cash cost Centinela $0.75/lb (2024: $1.60), Los Pelambres
   $0.82/lb (2024: $1.26), Antucoya $2.82/lb (2024: $2.53), against an LME average of $4.51/lb. Centinela's low figure is a
   gold figure: "Cash costs before by-product credits" $2.27 and "By-product credits (principally gold)" $(1.52), with gold
   realised at $3,754/oz against $2,530 the year before. Before by-products Centinela cost $2.27/lb in 2025 and $2.60 in
   2024. The filer's own words on its largest copper asset: "After completion of the expansion project, Centinela’s cost
   competitiveness is expected to rank in the top 25% of the world’s copper mines" (Integrated Report 2026, Metals & Mineral
   Resources division); it does not claim that rank now. Jellinbah is called "highly cost-competitive" with no figure; for
   Roy Hill no cost figure was found in the filer's documents read (text search of the Integrated Report, the IR
   Presentation and the audited notes for "Roy Hill" and for "cost").
2. *The trough* (test 6's failing answer): of two copper producers, "One is going to go broke at a buck-fifty a pound. And
   the other one’s going to still be doing fine" **[M2009-059]**; "a tough market helps the low-cost operator"
   **[L1997-021]**. Segment net profit to owners, audited Note 4 of each year (JPY billion): Energy & Metals FY2015 (142.4),
   FY2016 (6.2), FY2017 21.9, FY2018 67.9; Metals & Mineral Resources FY2019 (5.7) (Energy that year (149.3)), FY2020 61.4,
   FY2021 190.7, FY2022 199.4, FY2023 163.5, FY2024 123.5, FY2025 134.3. In each of the last two commodity troughs the
   deciding part, or the segment that then contained it, lost money. That is the failing answer the rows describe, not the
   low-cost producer's.
3. *Is the position durable?* The 2025 cost leadership at Centinela rests on a by-product price that rose 48% in a year;
   Antucoya is high on the curve in both years; the top-quartile claim is a forecast for after 2027, and business history
   "is filled with "Roman Candles"" **[L2007-004]**. The filer itself names the decay of the asset: "the inherent
   limitations of mining projects—namely, that resource reserves decrease as a result of mining" (Integrated Report 2026,
   same page). A moat that depends on the price of another commodity and on an expansion not yet finished is a moat
   "tenuous in any way" **[M2000-019]**.
4. *The attacker with money; pricing power; share of mind; the brand; the low bid* (tests 3, 4, 5, 7, 8): no price to raise
   and no brand to ask for in a price-taker. The money test runs the other way: Marubeni itself buys into mines with money
   (the additional investment in the Jellinbah Group, IR Presentation FY2025), as any well-funded rival can.
5. *Widening or narrowing* (test 10): the Centinela expansion (completion "toward completion in 2027, as planned") would
   widen it if the cost claim holds. A change for the better is credited only on the evidence of a full cycle; until then
   the question is TOO HARD (NATURE) with a dated re-look condition (the framework's Q2 convention of 2026-10-06, amended
   2026-10-10).

**The competitor row.** The filer names no rival by name; it names its class: "Our ambition is not to be merely compared
within the existing "general trading company (sogo shosha)" sector" (Integrated Report 2026, Our Vision). None of the class
files a 10-K or 20-F with the SEC (EDGAR company search, 2026-10-12: Mitsui & Co.'s last 20-F was filed 2010-08-13, with
amendments to 2010-12-03; none found for ITOCHU, Mitsubishi Corporation or Sumitomo Corporation), all flagged as non-SEC.
Their own reports are the primary documents; two were read (Mitsubishi Corporation's IR library refused the fetch, HTTP 403;
Sumitomo's was not fetched). Metric: return on equity, as each company states it or as computed from its own figures.

| FY (to Mar) | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Marubeni ROE % (Integrated Report 2026, p. 70) | 4.4 | 11.1 | 14.0 | 13.9 | (13.4) | 15.5 | 23.0 | 22.4 | 15.2 | 14.2 | 13.6 |
| ITOCHU ROE % (Integrated Report 2026, Selected Financial Data, p. 71) | 10.4 | 15.3 | 15.8 | 17.9 | 17.0 | 12.7 | 21.8 | 17.7 | 15.6 | 15.7 | 14.6 |
| ITOCHU resource net profit, JPY bn (same page) | 1.8 | 30.6 | 82.3 | 115.5 | 126.8 | 107.9 | 221.6 | 215.6 | 204.6 | 172.6 | 133.3 |
| Mitsui & Co. ROE %, computed as profit to owners over average owners' equity (Integrated Report 2025, financial data) | n.r. | n.r. | n.r. | n.r. | n.r. | n.r. | 18.0 | 18.9 | 15.3 | 11.9 | n.r. |

(n.r.: not read; Mitsui's 2025 report carries five years, FY2020 to FY2024, without FY2020's opening equity.) Over the whole
span Marubeni's return averaged below ITOCHU's, the house whose profit is mostly non-resource, and fell below zero once; the
field's resource earnings swing from near nothing (ITOCHU JPY 1.8 billion in FY2015) to a peak in FY2021-22 and back down.
**The field's returns over the last full cycle**, judged in words as the convention asks **[M1999-108]**: excellent at the top
of the commodity cycle, losses at the bottom; the field is not shown to earn only ordinary returns over the cycle, so the
"ordinary returns" OUT is not applied, nor is it shown to earn excellent ones once the troughs are counted.

**The parts table.**

| Part | Share of five-year segment profit | Castle | Decides |
|---|---|---|---|
| Metals & Mineral Resources | 32.6% (largest) | commodity producer; low-cost position partial, contingent on gold credits and a 2027 expansion; losses in the FY2015-16 and FY2019 troughs | yes |
| The other nine segments | 67.4% together, none more than 12.7% | not read for this STOP (they do not decide) | no |

**The verdict.** A castle shown open on the evidence closes OUT; a castle whose future cannot be judged closes TOO HARD
(Q2, Why it is a STOP). The evidence does not show this castle open: Los Pelambres and, in 2025, Centinela sit low on the
curve, and the field is not shown to earn only ordinary returns. Nor does it show the castle standing: the deciding part
lost money in both of the last two troughs, which is the speakers' test of the low-cost producer **[M2009-059]**,
**[L1997-021]**; its main asset's cost leadership in 2025 is a by-product gold price, and the filer claims top-quartile cost
only after an expansion due in 2027. That is the moat "tenuous in any way", of which the rows say "it’s just too risky. We
don’t know how to valuate that, and therefore we leave it alone" **[M2000-019]**; the framework sends it to TOO HARD, not OUT,
among the rows' three boxes **[M2006-013]**. A lower price does not reopen it.

**Which cause: NATURE.** Whether this collection of mine stakes keeps a low-cost position through the next ten to twenty
years turns on the future prices of copper, gold, iron ore and coal and on grades not yet mined. The speakers know of no one
with an edge in that forecast over ten years **[M2011-047]** and say they cannot make it **[M2016-025]**; it is a case where
"the nature of the industry would be the roadblock" **[L1993-023]**, not study. The knowable half, today's cost position, was
read above from the operator's filing and did not settle the question; the half that decides is a price forecast. The change
for the better (Centinela after 2027) is credited only on a full cycle (Q2 convention). **Re-look condition:** the first fiscal
year after the Centinela expansion is complete (stated for 2027) in which Marubeni's equity copper sales volume or the copper
price falls, read from the filings; Q2 is then put again on whether the Metals & Mineral Resources segment stayed profitable
through it.

**VERDICT: TOO HARD (NATURE).** The deciding part's only possible castle in a commodity field, the low-cost position
**[L2000-017]**, **[M1997-010]**, is shown tenuous **[M2000-019]**: losses in both recent troughs **[M2009-059]**, and cost
leadership that depends on gold credits and on an expansion not yet finished; its durability is a commodity-price forecast
no one can make **[M2011-047]**, **[L1993-023]**.

---
## Q3 to Q12: NOT REACHED

Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are not answered (operator rule 2). Facts already found are written under AFTER THE
STOP, not weighed. Figures for Q7 below are headed COMPUTATION, NOT A CLEARANCE (operator rule 3).

---
## THE BOX

**TOO HARD (NATURE), decided at Q2** on the deciding part (Metals & Mineral Resources): the low-cost castle is tenuous and
its durability is a commodity-price forecast. Re-look: the first fiscal year after the Centinela expansion (2027) in which
Marubeni's equity copper volume or the copper price falls. Reporting figures, computed and not cleared: value range on the
all-equity basis JPY 2,734 to 4,391 a share against JPY 4,702. **Integrity facts recorded, not judged** (a 2014 US guilty
plea under the Foreign Corrupt Practices Act; see AFTER THE STOP, Q5).

---
## AFTER THE STOP: FACTS FOUND, NOT WEIGHED

Written down, not weighed; no verdict; the box is unchanged (operator rule 2; Part VII) **[M1997-127]**.

**Q3 (capital).** The company's own return on invested capital (Full-year IR Presentation FY2025, p. 14; adjusted net profit
over invested capital, the company's measure): consolidated 8% on JPY 5.6 trillion (FY2024) and 8% on 6.2 trillion
(FY2025); Resources 13% and 14% on 1.0 and 1.1 trillion; Non-resources 7% and 7% on 4.6 and 5.1 trillion; "Non-resources
(Others)" 6% and 6% on 3.4 and 3.7 trillion, labelled by the company "Divestment of low-growth, low ROIC businesses". The
company targets "Non-resources ROIC over 10%" toward FY2030. Net plant spending FY2021-25 averaged JPY 119.9 billion against
depreciation and amortisation of 143 to 209 billion (the latter includes right-of-use assets).

**Q4 (the accounts).** Owner cash averaged about 55% of reported net profit over FY2021-25 (Step 0 table). The company
features "Adjusted net profit" ("Net profit excluding one-time items, shown in an approximate figure", Integrated Report
2026, p. 70) and "Core operating cash flow" ("Operating cash flow excluding changes in working capital and other items",
same page); adjusted net profit was below the audited figure in FY2024 (451.0 against 503.0) and FY2025 (480.0 against
543.9). Large impairment years: FY2015 and FY2019 (net loss JPY 197.5 billion in FY2019; Energy segment (149.3), Agri
Business (77.1), audited Note 4 of the FY2019 statements). Equity growth is partly currency translation (Step 0). The auditor
names two key audit matters for FY2025: impairment indicators for equity-method investments, and the provision for the
Sugar Group litigation.

**Q5 (the people), integrity facts.** The U.S. Department of Justice announced on 2014-03-19 that Marubeni pleaded guilty to
one count of conspiracy and seven counts of violating the anti-bribery provisions of the Foreign Corrupt Practices Act and
agreed to pay a criminal fine of $88 million, for bribes to Indonesian officials to secure a power project; the plea
agreement cited the company's refusal to cooperate when given the opportunity, the lack of an effective compliance and
ethics program at the time, and its failure to timely remediate. *Source and its limit:* justice.gov press releases
"14-crm-290" and "Marubeni Corporation Sentenced for Foreign Bribery Violations", located by web search on 2026-10-12; both
pages refused an automated fetch (an Akamai challenge), so the facts above are as the search result summarised those pages,
and the release text was not read in full. An earlier U.S. resolution of 2012 concerning the Nigeria (Bonny Island) matter
is recalled but was not verified and is not relied on. No mention of either was found in the company documents read (text
search for "corrupt", "FCPA", "bribe", "Department of Justice"). Any later run that reaches Q5 must answer these
**[M2013-088]**. The remuneration plan was revised on 2026-06-19 (notice not read in full); the company moved to a
three-committee board in June 2026.

**Q6 (money and owners).** Net cash outflows on purchase of treasury stock (audited cash flow statements, JPY billion):
FY2021 19.2, FY2022 41.0, FY2023 50.1, FY2024 50.0, FY2025 70.0. The current
programme, up to JPY 100 billion and 40 million shares to 2027-03-31, names a cap on amount and shares, not a price; shares
bought in September 2026 cost JPY 13,702,630,400 for 2,705,000 shares, an average of JPY 5,066 (notice of 2026-10-01). Against
the COMPUTATION below, that is above the top of the computed range, not at or below its bottom (the Q6 test's comparison,
recorded and not weighed). Dividend policy: progressive, total payout about 40% for FY2026; DPS FY2025 JPY 107.5. Issued
shares were 1,660.8 million at 2026-06-30; the issued count was not traced year by year.

**Q9 (debt and exposures).** Net interest-bearing debt JPY 2,050.5 billion and net DE 0.46 at 2026-06-30; lease
liabilities JPY 246.4 billion at 2026-03-31 (73.9 current, 172.5 non-current; audited Note 10). Sugar Group (Indonesia):
the Supreme Court of Indonesia ruled in 2017 that the company and other defendants are jointly liable for US$250 million;
no provision is recognised; on 2026-01-19 the company received a judicial-review decision revoking a 2022 Supreme Court
ruling in its favour in the related Central Jakarta case (notice of 2026-01-21; auditor's key audit matter, FY2025
statements). Commodity sensitivities: copper JPY 1.3 billion per $100/t; USDJPY JPY 1.9 billion per yen.

**Q12.** None of the businesses the rows name (casinos, tobacco, distributor-loading schemes) was found in the segment
descriptions (audited Note 4, FY2025); the group holds coal mines and coal-fired power interests, which the rows do not name.

---
## COMPUTATION, NOT A CLEARANCE: Q7 AND THE OPERATOR'S TWO FIGURES

*Arithmetic only, after a closing STOP; no entry language; nothing here is a verdict (operator rule 3).* Script:
`_research 2026-10-12 MARUY/scripts/q7.py`. Rate 4.136% (30-year JGB, 2026-10-08). Price JPY 4,702; 1,621.2 million shares;
market value JPY 7,623 billion. Claims ahead of the common: net interest-bearing debt JPY 2,050.5 billion at 2026-06-30
plus the JPY 27.7 billion paid for shares bought after that date = 2,078.2; non-controlling interests JPY 150.3 billion
*(CONVENTION of this run: owner cash is consolidated, so the minority partners' claim is deducted at its carrying amount like
debt; rationale: the framework's all-equity basis names debt and leases but not minorities, and leaving them in would credit
the common with cash it does not own)*. Lease liabilities left out of net debt because lease principal is charged inside
owner cash (said so, as Q7 directs for operating leases). All-equity value of the claims: JPY 9,851 billion.

**How the range was built, by Q7's range convention.**
- *Base and (a) cycles:* the literal window FY2021-25 averages JPY 302.8 billion (all-equity), but both of its first two
  years are aberrational on the filer's own description: FY2021's operating cash carried a JPY 341.5 billion inventory build
  in the commodity spike, and FY2022 carried the JPY 330.1 billion sale of a subsidiary. The base is therefore the ten-year
  average FY2016-25, JPY 275.5 billion, spanning trough (FY2016, FY2019) to the latest year, and growth is measured between
  the averages of its two halves (FY2016-20: 248.3; FY2021-25: 302.8), **4.05% a year**, on aggregate owner cash. The
  literal window is shown beside.
- *(b) decline:* the halves of the literal window would show a decline (FY2021-22 average 452.4 against FY2024-25 average
  272.1), driven by the subsidiary sale; not used for the central case because (a) governs aberrational end years.
- *(c) acquisitions:* deducted, net of businesses sold, with total growth credited (the default pair); net purchases of
  170.9 over FY2021-25 are below half of owner cash before purchases (770.9), so not a serial acquirer. The organic pair is
  beside. No signed unclosed deal found.
- *(d) working capital:* counted (it is inside operating cash).
- *(e) maintenance:* the filing does not separate maintenance from growth spending across hundreds of investments; the
  all-spending case is central, said so.
- *(f) the cap:* 4.05% is below the discount rate and is carried ten years, then zero nominal growth.

| Case | Base (JPY bn) | Growth | Value range (JPY bn, claims included) | Per share | Width |
|---|---|---|---|---|---|
| **Central: all-equity, acquisitions deducted, cycle base** | 275.5 | 4.05% | 6,661 to 9,348 | **JPY 2,734 to 4,391** | 1.40x |
| Organic pair, beside | 289.0 | 6.93% | 6,987 to 12,458 | JPY 2,935 to 6,309 | 1.78x |
| Literal window average, beside | 302.8 | 4.05% | 7,321 to 10,274 | JPY 3,141 to 4,963 | 1.40x |
| Equity-only, beside (owner cash after interest; minorities still deducted) | 252.2 | 3.56% | 6,098 to 8,215 | JPY 3,668 to 4,975 | 1.35x |

**The floor, tested first:** the expected return at JPY 4,702 is 3.93% on the central growth case, 5.13% on the organic
growth case and 2.80% on no growth; no case reaches about ten percent. Had Q7 been reached it would have closed OUT on the
floor whatever the width, and the price also sits above the top of the central range.

**(a) VALUE RANGE (reporting convention):** JPY 2,734 to 4,391 a share, central, all-equity basis, company tax, against the
Tokyo price of JPY 4,702 (2026-10-09). In ADS terms at one share per ADS and USDJPY 158.06: $17.30 to $27.78 against
$29.74 (2026-10-12).

**(b) FAIR PRICE (Part VII; each end case valued at ten percent, the two averaged; company tax; no conversion):** **JPY 596
a share** on the all-equity basis, the central figure (ends at ten percent: JPY 325 and 867); **JPY 1,677** on the
equity-only basis beside it. In ADS terms: $3.77 all-equity, $10.61 equity-only. Against the price of JPY 4,702 ($29.74).
The literal-window central would give JPY 791 and the organic pair JPY 954.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (first commit, template only); written question by question; committed
      after Step 0, Q1, Q2 and this close, each with a pathspec of the two paths only.
- [x] Dispatched run: the brief allowed per-question commits; the lock and the fold are the dispatching session's (operator
      rule ten). No git lock was met.
- [x] Blind rule: no other run file, holding review, `PORTFOLIO.md`, resume file, queue file or reading list was opened,
      listed further or searched. One directory listing of `Test Runs` (to check that my two paths did not exist) showed
      other file names; declared under Contamination at the top and not used. The major-shareholder notice of 2026-05-07 was
      downloaded with the others but not read, to avoid learning who holds the name.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by `_research 2026-10-12 MARUY/scripts/check_ids.py`); every
      filing fact names its document and date; no accession numbers exist for the company's own filings (no SEC periodic
      filings), the F-6 accessions are given.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost from the audited cash flow statements, never a net-income proxy; the sovereign from
      the Ministry of Finance; aggregator quotes (prices, FX) flagged.
- [x] Contrary evidence written down as found (under THE FOUNDATIONS, and inside Q1 and Q2); facts for later questions are
      under AFTER THE STOP, with the integrity flag in the box line.
- [x] No point-in-time anchor; not applicable.
- [x] `tools/run.py` and `Screens/cover_shares.py` returned nothing usable (not an SEC registrant); no line of theirs used.
- [x] `python tools/check_framework.py`: PASS (2026-10-12, before the final commit). Citation check
      (`scripts/check_ids.py`): no E-ids; 37 distinct ids, all in the v5 ledger; the fragments it flagged were filing quotes
      or search terms attributed to their documents, each read by hand, none placed as a row's words.
- Honest limits: the DOJ facts rest on search-result text of justice.gov pages that refused a fetch; Mitsubishi and
  Sumitomo's reports were not read; the Japanese yuho and the convocation notice (pay, board detail) were not read; Roy Hill
  and Jellinbah costs are not public in the documents read; the parts table rests on segment net profit, not operating
  profit, across five reorganisations.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) The business-of-parts threshold names "operating profit"; a Japanese trading house reports segment profit
only as net profit attributable to owners, and its segments were reorganised in each of the last five years, so "five-year
operating profit by part" does not exist in its filings. I used segment net profit as filed each year and confessed it as a
CONVENTION of this run. (2) The convention then hands the whole Q1 and Q2 judgement of a ten-segment conglomerate to a part
carrying 32.6% of profit; the framework already marks **[M2023-031]** OPEN against it, and this run is a case where the
by-parts reading and the speakers' own reading of the same company point in different directions; the text gives no rule for
when "the largest part" is too small a share to stand for the whole. (3) Q2's commodity rule has the low-cost operator as
the one castle, but gives no test for a producer that is low-cost only through by-product credits of a second commodity,
or whose cost leadership is a forecast tied to an expansion; I read that as "tenuous" under **[M2000-019]** and sent it to
TOO HARD (NATURE). A rule naming where cost position is read (net of by-products or before them, and over which span) would
make the verdict reproducible. Smaller: Q7's all-equity basis says nothing of non-controlling interests; I deducted them
like debt and confessed it. And the brief's ADS note named JPMorgan for the filing of 2026-06-02, whose depositary is
Citibank.
