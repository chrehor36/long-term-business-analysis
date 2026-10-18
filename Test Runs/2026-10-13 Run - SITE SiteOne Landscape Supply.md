# Company Run: SiteOne Landscape Supply, Inc. (NYSE: SITE), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from the template and committed before any fetch: commit 5ef1e24d.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. The dispatching session
fills it at the fold. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (SITE; also searched for SiteOne); not held.*

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure: the lines of
evidence and the competitors were derived by the analyst from the 10-K, not listed by the dispatcher. Working folder
`Test Runs/_research 2026-10-13 SITE/` (scripts, tool outputs, the rows read; the fetched filings sit in its `cache/`,
which is gitignored).

**Contamination declared (seen by accident, not used).** The session's git status listed other runs' research folders by
name (`_research 2026-09-26 AYI`, `_research 2026-09-27 ARCB` and others); the recent commit subjects shown at session start
concern a Siemens (SIEGY) run; the session's memory index carries one-line notes on queue state (a wave paused at a named
ticker, a count of gate-clearers) that do not name SITE. None of these files was opened. Nothing about SITE, its holders or
any earlier run on it was seen.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $87.99 (close 2026-10-12; printed by `tools/run.py` from its quote source, an **aggregator, flagged** under
  operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **43,655,390** shares (10-Q for the
  quarter ended 2026-06-28, filed 2026-07-29, accession `0001650729-26-000016`; `python Screens/cover_shares.py SITE`).
  Checked against the 10-Q balance sheet: 45,994,836 issued less 2,240,574 treasury = 43,754,262 at 2026-06-28; the 10-Q
  states 100,692 shares repurchased in July 2026, giving 43,653,570, within 1,820 shares of the cover count (vesting). No
  8-K or prospectus after the 10-Q changes the count (8-Ks of 2026 read: none issues shares; the June 2026 Devil Mountain
  buyout's 216,994 treasury shares were issued before the 10-Q date and are inside the count).
- **Market cap:** 43.655M x $87.99 = **$3,841.2M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, the US Treasury daily par yield curve, 30-year, dated
  10/09/2026 (`python tools/sources.py`, issuing authority; 10/12 was a bond-market holiday).
- **Filings read** (operator rule 4): 10-K for FY2025 (fiscal year ended 2025-12-28), filed 2026-02-19, accession
  `0001650729-26-000005`, Items 1, 1A, 3, 5, 7, 7A and the statements and Notes 6 (leases) and 12; 10-Q for the quarter
  ended 2026-06-28, filed 2026-07-29, `0001650729-26-000016`; proxy DEF 14A filed 2026-04-02, `0001104659-26-038879`
  (pay sections); 8-Ks of 2026-03-31 (`0001104659-26-037375`, Item 5.02), 2026-04-27 (`0001104659-26-048750`, Item 1.01,
  the ABL amendment), 2026-05-19 (`0001104659-26-063512`, Item 5.07) and 2026-07-29 (`0001104659-26-087746`, Item 2.02 and
  its Exhibit 99.1); the 10-Ks for FY2018 to FY2024 for the cycle (`0001650729-19-000004`, `0001650729-20-000004`,
  `0001650729-21-000006`, `0001650729-22-000005`, `0001650729-23-000003`, `0001650729-24-000004`, `0001650729-25-000004`),
  read for organic growth, pricing, contingent payments, lease and allowance lines; the 424B5 of 2020-08-05
  (`0001104659-20-090934`). Competitors: Pool Corporation 10-K FY2025 (`0001193125-26-074833`) and The Home Depot 10-K
  FY2025 (`0001628280-26-019436`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$300.5M**,
  read on the filed Consolidated Statement of Cash Flows of `0001650729-26-000005`, equal to the XBRL value `tools/run.py`
  printed. Also checked: FY2025 operating income $238.1M and net sales $4,704.8M on the filed statement of operations; the
  June 2026 net debt of $555.6M on the 10-Q balance sheet equals the figure the company states in Exhibit 99.1.
- `python tools/run.py SITE`, **arithmetic lines only** (output in the research folder, `run_py_output.txt`): OCF FY2023 to
  FY2025 $297.5M, $283.4M, $300.5M; SBC $25.7M, $25.0M, $27.0M (the filed cash-flow line, complete; no other stock-pay line
  found); capex $32.1M, $40.5M, $53.7M; the alternates it printed, purchases of intangible assets $3.9M, $4.3M, $1.4M,
  finance-lease principal $18.5M, $26.7M, $32.5M, and dividends to the minority partner $1.0M (FY2025). Its **D&A warning
  is correct**: the column it printed ($62.6M, $61.0M, $55.6M) is intangible amortization only. The filed cash-flow statement
  carries "Amortization of finance lease right-of-use assets and depreciation" $64.1M, $75.3M, $80.7M and "Amortization of
  software and intangible assets" $63.6M, $63.7M, $60.1M. Its D&A-basis figures are therefore not used. Its owner-earnings
  line leaves out the delivery fleet, which the 10-K says is held on finance leases ("Our finance leases consist primarily of
  leases for our vehicle fleet", Item 7); the fleet is a real capital cost and is charged below.

**Owner cash after every real cost** (research folder, `scripts/compute.py`, `compute_output.txt`; USD millions). Two
bases, as Q7 requires. *All-equity*: OCF, plus cash interest paid after the company's own effective tax rate, less SBC,
property and equipment purchases, software and intangible purchases and the fleet acquired on finance leases (right-of-use
assets obtained, Note 6), plus proceeds of equipment sold. *Equity-only*: OCF less SBC, the same purchases and proceeds,
and finance-lease principal paid in place of the fleet acquired. **CONVENTION of this run:** the fleet is charged as the
right-of-use assets obtained on the all-equity basis and as principal repaid on the equity-only basis; rationale: on the
all-equity basis the finance leases sit in net debt, so the vehicles are bought with the lenders' money and their cost is the
assets obtained, while on the equity-only basis the owner pays for them as the principal falls due. Before FY2019 the filer
did not report right-of-use assets and the capital-lease principal stands in for both (labelled; outside the window).

| FY | equity-only | all-equity | cash paid for businesses (incl. contingent consideration) | all-equity / sales |
|---|---|---|---|---|
| 2016 | 55.5 | 65.2 | 66.4 | 4.0% |
| 2017 | -10.4 | 7.6 | 82.9 | 0.4% |
| 2018 | 47.6 | 73.3 | 151.7 | 3.5% |
| 2019 | 92.2 | 109.4 | 74.5 | 4.6% |
| 2020 | 185.5 | 188.9 | 164.2 | 7.0% |
| 2021 | 151.3 | 160.1 | 155.8 | 4.6% |
| 2022 | 146.8 | 145.5 | 254.9 | 3.6% |
| 2023 | 220.0 | 207.9 | 200.7 | 4.8% |
| 2024 | 192.8 | 181.3 | 143.8 | 4.0% |
| 2025 | 195.5 | 216.8 | 41.7 | 4.6% |
| **FY2021-FY2025 average** | **181.3** | **182.3** | total **796.9** | |

The depreciation variant (equity-only, OCF less SBC less depreciation including fleet amortization less software
amortization, acquired-intangible amortization added back): FY2023 $206.7M, FY2024 $180.4M, FY2025 $188.3M, close to the
all-spending figures, so total spending has run near depreciation and the filing gives no split of maintenance from growth
(capital spending guided at "0.8% to 1.3%" of sales, Item 7). The all-spending case stands as central.

### The balance sheets, ten year-ends, read before the income account **[M2025-032]**
Read in Step 0 because the file closes before Q4 (the brief's instruction). XBRL first-filed values transcribed by
`tools/run.py` and `scripts/series.py`, the FY2023 to FY2025 values read on the filed statements; USD millions.

| year-end | equity | goodwill | intangibles | cash | receivables | inventory | payables | debt | finance leases | operating leases |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017-01-01 | 148.8 | 70.8 | 103.3 | 16.3 | 169.0 | 289.6 | 108.3 | 375.5 | 11.0 | n/a |
| 2017-12-31 | 212.8 | 106.5 | 112.8 | 16.7 | 219.9 | 338.3 | 124.1 | 463.6 | 11.7 | n/a |
| 2018-12-30 | 301.8 | 148.4 | 155.6 | 17.3 | 285.3 | 411.7 | 184.6 | 558.2 | 14.7 | n/a |
| 2019-12-29 | 393.2 | 181.3 | 150.6 | 19.0 | 283.4 | 427.1 | 162.2 | 524.9 | 22.9 | 234.9 |
| 2021-01-03 | 795.0 | 250.6 | 196.3 | 55.2 | 292.8 | 458.6 | 172.8 | 263.5 | 41.6 | 262.9 |
| 2022-01-02 | 1,057.7 | 311.1 | 213.9 | 53.7 | 393.8 | 636.6 | 254.5 | 255.2 | 45.4 | 306.3 |
| 2023-01-01 | 1,302.9 | 411.9 | 276.0 | 29.1 | 455.5 | 767.7 | 279.7 | 350.6 | 58.7 | 330.2 |
| 2023-12-31 | 1,486.1 | 485.5 | 280.8 | 82.5 | 490.6 | 771.2 | 270.8 | 372.9 | 91.6 | 396.9 |
| 2024-12-29 | 1,572.5 | 518.1 | 261.0 | 107.1 | 547.1 | 827.2 | 315.5 | 388.2 | 130.6 | 432.5 |
| 2025-12-28 | 1,659.2 | 530.4 | 220.0 | 190.6 | 546.8 | 876.5 | 310.8 | 385.4 | 134.8 | 459.8 |
| 2026-06-28 (10-Q) | 1,687.6 | 558.8 | 222.4 | 87.4 | 672.0 | 1,092.5 | 440.1 | 505.7 | 137.3 | 485.1 |

What the figures say. Equity rose from $149M to $1,659M: about $1,192M of it is retained earnings and $262M the August
2020 offering of 2,150,000 new shares (10-K FY2020, `0001650729-21-000006`: "approximately $261.7 million of net cash
proceeds"), less $186M of treasury stock bought from 2022. Goodwill and acquired intangibles grew from $174M to $750M,
which is 45% of equity at FY2025 (117% at the first year-end shown): the growth was bought. Debt is flat at about $385M for
a decade while sales rose 2.9 times; the 2020 equity raise, not earnings, cut it from $525M to $264M. The delivery fleet
moved onto finance leases ($11M to $135M) and branch leases are $460M of operating leases left out of debt, so the business
uses more borrowed capital than the debt line shows. Receivables (10.3% of sales at the first year-end, 11.6% at FY2025)
and inventory (17.6% to 18.6% of sales) moved with sales; inventory rose to 19.1% of sales at the 2022 price peak and came
back, which is the inflation passing through working capital, as Item 7 says. The one line that moved out of step: the
**allowance for doubtful accounts rose from $4.7M (FY2017) to $33.3M (FY2025) and $36.6M (June 2026)**, while net
receivables grew 2.5 times; Item 7A puts bad-debt reserves at "approximately 6% of gross receivables". What the figures
cannot say: whether that allowance reflects weaker customers or a more cautious reserve. No prepaid or deferred account is
building out of line with sales **[M1995-064]**. The June 2026 sheet is the seasonal peak (inventory $1,093M, receivables
$672M, ABL drawn), and net debt there ($555.6M) is $226M above the December figure.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest on this name is the share as a business: the question is the row's own: "Would I be happy buying this stock if the market closed for five years?", for "then you’re
buying a business, if you say yes to that." **[M1997-109]**. The stock has fallen from purchases at $126 in April
2026 to $87.99 now; the foundation says the fall instructs nothing, and the work looks at the business. No macro view enters:
the 10-K's long passage on housing, rates and tariffs is read only for what it says about the business's own pricing and
volume. The analyst's habit used throughout: look for "what’s wrong in things because that’s part of investing" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the filer's own words, "barriers to entry in the landscape
supply industry are generally low" (10-K Item 1A); (2) operating margin back to its pre-pandemic level by FY2024 after the
2021-22 peak; (3) the proxy's report that the three-year "EBTA cumulative compound annual growth rate of negative 5.7%" ranked
"at the 6th percentile" of the company's own performance peer group (DEF 14A 2026); (4) the allowance for doubtful accounts
growing seven-fold; (5) the cover share count and net debt taken at the seasonal peak (a convention effect, noted at Q7).
Found for the business: gross margin up 3.5 points over ten years and held through the 2023-25 price deflation; return on
tangible capital near 19% pre-tax in FY2025.

## THE STANDING RULE
The buyer's own conduct: a purchase of a marketable minority stake paid in cash, no borrowed money, sized so that a fall of
half or more forces no sale. "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "We are never going to
risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. Nothing in owning SITE on those terms risks the buyer's ruin.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence chosen, and where each came from.** From Item 1 (business): what is sold, to whom (440,000 customers,
top ten under 4% of sales), from whom (6,000 suppliers, top ten about 30% of purchases), the end-market mix (maintenance
36%, new construction 34%, repair and upgrade 30% of FY2025 sales), the competitors named and the market share implied
(regional and local rivals about 81% of the industry). From Item 1A (risks): competition and barriers to entry; pricing and
the pass-through of cost changes; acquisitions and goodwill; the credit extended to customers; indebtedness. From Item 7
(MD&A): margins over the cycle; organic growth and the price component of it, year by year, FY2017 to FY2025; acquisitions;
capital spending, leases and the fleet; buybacks and their prices; the Adjusted EBITDA presentation and the guidance. From
the proxy: pay metrics and results. Litigation: Item 3 states no material litigation; no investigation is disclosed.

**The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**. The business is a branch distributor: it buys bulk from manufacturers and growers
and sells small lots, with delivery, credit and advice, to landscape contractors who buy "on an as-needed basis" (Item 1).
The **key variables** **[M1998-044]** are (1) the volume of landscape work, of which the maintenance third is recurring and the
construction two-thirds cyclical (Item 1A: commercial downturns "have historically lasted about two to three years, and
generally result in market declines of approximately 20% to 40%"); (2) the spread between buying and selling prices, gross
margin 31% to 35% over the decade; (3) the cost to serve, gross profit less operating income at 26% to 30% of sales; (4) the
price paid for the acquisitions that supply most of the growth. Each is visible in ten years of filings, and the industry
changes slowly: the products are pavers, pipe, fertilizer, plants and lights, and Item 7 says "Our inventories are generally
not susceptible to technological obsolescence." The forecast is about contractors and the volume of outdoor work, not about
technology. The row on a business whose product was opaque puts the test this way: "What is important is that I
understand the economic dynamics of the industry." and it then asks "Is there ease of entry?" **[M2011-014]**; the
industry's dynamics are readable here, and the ease-of-entry question is Q2's. Of ten-year economics I hold a model: a cyclical distributor whose sales follow construction and whose
margin is set by the spread and the cost to serve; how far off I could be is the cycle's 20% to 40% swing in construction
volume, which the maintenance third damps.

**The doubt, written down.** The speakers warn that "it’s easy to sort of think you understand retail, and then subsequently
find out you don’t" **[M2014-052]**, and a branch distributor is a near relation of retail. The doubt I hold is not whether
the economics can be followed (they can, from the filings) but whether the castle stands, which is Q2's question. Reading
"if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]** against that: the doubt
is about the moat, not about the circle, and so does not close Q1.

**VERDICT: IN.** The economics of a landscape-supply distributor ten years out can be followed from the filings; the key
variables are named and slow-moving; nothing in the business turns on technology (10-K `0001650729-26-000005`, Items 1 and 7).

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is the row's: "why is that castle still standing? And what’s going to keep it standing or cause it not to be
standing five, 10, 20 years from now." **[M1995-038]**. Every castle is assumed under attack; "all moats are subject to
attack in a capitalistic system" **[M1995-038]**.

**The parts table.** Not applicable: the filer manages "our business as a single reportable segment" (10-K Item 7,
`0001650729-26-000005`), and its product lines share branches, customers and supply chain.

**The castle tests, each with its filing fact.**
1. *Key factors, and how permanent.* What the filer names as its advantage: the only national full-line distributor, scale
   in buying (supplier volume incentives are "an important factor in our financial results", Item 1), yards and equipment
   for hardscapes and nursery goods that "provide us with a competitive advantage over many competitors who offer a more
   limited selection" (Item 1), private brands at about 15% of sales (LESCO the large majority), and a loyalty programme whose
   members bought about 62% of sales. How permanent, in the filer's own words in Item 1A: "We operate in markets with
   relatively few large competitors, but barriers to entry in the landscape supply industry are generally low, and we may
   have several competitors within a local market area." and "Some local competitors may be able to offer higher levels of
   service, lower prices, or a broader selection of inventory than we can in particular local markets." The FY2018 10-K
   (`0001650729-19-000004`) carried the same sentence on barriers and added "Our industry faces low barriers to entry, making
   the possibility of former associates starting similar businesses more likely." Eight years of the filer saying so.
2. *Would it stand without the lord?* The growth strategy depends on continuous acquisition by a development team (a new
   executive for strategy and development appointed by the 8-K of 2026-03-31, `0001104659-26-037375`). Not decisive here.
3. *The money test: could a well-funded attacker take it?* The row: "if I had a hundred million dollars and I wanted to go
   in and take on See’s Candy, could I do it? [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
   The filings answer yes, three ways. The business itself was put together with money: Deere bought four distributors from
   2001 to 2007 (Item 1, Our History), and SiteOne paid $796.9M for businesses (with contingent consideration) in FY2021 to
   FY2025 alone. The field remains for sale: regional and local competitors were about 89% of the industry by the FY2018
   10-K, 85% by FY2021, 81% by FY2025, and "existing and future competitors, and private equity firms, increasingly compete
   with us for acquisitions" (Item 1A). And an attacker with money has come: the first rival the 10-K names is "Heritage
   Landscape Supply Group (a subsidiary of The Home Depot)"; Home Depot's FY2025 10-K (`0001628280-26-019436`) says "In fiscal
   2024, we acquired SRS", a distributor of "landscape supplies" among other lines, and its cash paid for businesses was
   $17,644M that year (XBRL). The second named parent, Pool Corporation, distributes "irrigation, landscape maintenance and
   related products through our Horizon network" (POOL 10-K FY2025, `0001193125-26-074833`). The speakers' description of
   their own way, "We sort of buy barriers; we don’t build them." **[M2012-105]**, is SiteOne's way too, and the barrier it
   buys can be bought by the next buyer.
4. *Pricing power and the agony before a rise.* "You can learn a lot about [...] the durability of the economics of a
   business by observing the behavior of [...] the price behavior." **[M2005-020]**. The record, from the 10-Ks: price added
   about 11% to organic daily sales in FY2021 and about 18% in FY2022, and gross margin rose 160 basis points in FY2021; then
   prices fell "by less than 1%" in FY2023 and "by 3%" in FY2024 on commodity deflation, and were "negligible" in FY2025.
   Item 1A: "In a declining price environment, including the commodity price deflation experienced in our 2024 and 2025 Fiscal
   Years, we may be required to lower prices". Prices track the costs of the goods both ways. Passing cost increases through
   is to the business's credit, "over time the businesses with strong competitive positions manage to pass through increases
   in raw material costs" **[M2005-017]**; but the speakers' measure is a price raised against the market, and the filings show
   none: the price follows the commodity.
5. *Unit volume.* Organic daily sales grew 11% in FY2022 with about 18% from price, so volume fell; FY2023 flat, FY2024
   down 1% (price down 3%), FY2025 up 1% (price nil); the Q2 2026 release guides organic daily sales "flat to up 1% for the
   full year" with pricing "up 3%" (Exhibit 99.1, `0001104659-26-087746`). Volume has not grown since FY2021.
6. *The low-cost position.* "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; and "if
   your costs are on parity or less [...] than your other major competitors, that is much more important to you than the
   absolute level." **[M2001-013]**. SiteOne's cost to serve (gross profit less operating income) rose from 26.8% of sales in
   FY2016 to 29.7% in FY2025 while sales nearly tripled; scale has not lowered it. The filer itself says local rivals may
   offer "lower prices" (Item 1A). The nearest filed comparison, Pool Corporation's distribution business, carried 18.8% of
   sales between gross profit and operating income in 2025; the products differ (nursery and hardscape are bulky and need
   yards), so the comparison is indicative only. No filing shows SiteOne to be the low-cost operator.
7. *The brand.* LESCO is the one brand of weight (about 15% of sales with the other private labels); the rest of the shelf
   is the manufacturers' brands (Hunter, Rain Bird, Toro and others, Item 1), which the customer can buy from any distributor
   that carries them, and Item 1A warns that "Certain product manufacturers that sell and distribute their products directly
   to landscapers may increase the volume of such direct sales."
8. *Would the customer choose it over the low bid?* For: "While pricing is important to our customers, availability,
   convenience, and expertise are also important factors in their purchase decisions" (Item 1). Against: the customer is a
   contractor who bids for work, 440,000 of them, and the filer lists "pricing of products" and "availability of credit"
   among the principal competitive factors. The row's question is whether people "would not be buying, necessarily, a
   lower-price candy" **[M2017-009]**; for contractor commodities like pipe, seed and fertilizer, the price record in test 4
   answers no.
9. *Ask the competitors.* Not possible from the record: neither filing parent reports its landscape line separately.
10. *Widening or narrowing?* "how wide the moat is and whether it’s likely to widen further or shrink on you" **[M1999-108]**.
   For widening: gross margin rose from 31.3% (FY2016) to 34.8% (FY2025) and held at 34.4% to 34.8% through the FY2023 to
   FY2025 deflation; the large players' share of the industry rose by eight points since FY2018. Against: operating margin
   4.5% in FY2016 and 5.1% in FY2025, with the FY2021 peak of 9.0% given back by FY2024 (4.2%); and the proxy (DEF 14A 2026,
   `0001104659-26-038879`) reports the 2023-2025 performance-share cycle paid nothing on "a three-year EBTA cumulative compound
   annual growth rate of negative 5.7%, which ranked at the 6th percentile relative to the PSU performance peer group", the
   company's own chosen peers. On the measure that reaches the owner, no widening.
11. *What could destroy, modify or reduce it.* Item 1A names them: manufacturers selling direct, suppliers' exclusive
   arrangements with other distributors, the consolidation of landscape contractors, and rivals or private equity buying the
   same local distributors.

**The competitor row.** The 10-K names nine rivals (Item 1): Heritage Landscape Supply Group (a Home Depot subsidiary),
Ewing, Target Specialty Products, Harrell's, Horizon Distributors (a Pool Corporation subsidiary), BWI, Outdoor Living
Supply, Central Pro Supply and W.S. Connelly. **Flagged as not SEC filers in their own names** (private, or reported only
inside a parent): Ewing, Target Specialty Products, Harrell's, BWI, Outdoor Living Supply, Central Pro Supply, W.S.
Connelly, and Heritage and Horizon themselves. Two of the named rivals file through their parents, and neither parent reports
the landscape line apart: The Home Depot (CIK 354950) and Pool Corporation (CIK 945841). No third named rival files. The two
parents are compared as the nearest filed evidence, never as like-for-like. Same metric, all ten years (XBRL first-filed
values, `scripts/returns.py`; POOL's 2025 operating income of $580.2M read on its filed 10-K; HD's fiscal years end in late
January or early February of the next year):

| year | SITE gross / operating margin | POOL gross / operating margin | HD gross / operating margin |
|---|---|---|---|
| 2016 | 31.3% / 4.5% | 28.8% / 10.0% | 34.2% / 14.2% |
| 2017 | 32.0% / 5.3% | 28.9% / 10.2% | 34.0% / 14.5% |
| 2018 | 32.1% / 5.1% | 29.0% / 10.5% | 34.3% / 14.4% |
| 2019 | 32.8% / 5.3% | 28.9% / 10.7% | 34.1% / 14.4% |
| 2020 | 33.3% / 6.6% | 28.7% / 11.8% | 34.0% / 13.8% |
| 2021 | 34.9% / 9.0% | 30.5% / 15.7% | 33.6% / 15.2% |
| 2022 | 35.4% / 8.3% | 31.3% / 16.6% | 33.5% / 15.3% |
| 2023 | 34.7% / 5.8% | 30.0% / 13.5% | 33.4% / 14.2% |
| 2024 | 34.4% / 4.2% | 29.7% / 11.6% | 33.4% / 13.5% |
| 2025 | 34.8% / 5.1% | 29.7% / 11.0% | 33.3% / 12.7% |
| ten-year average operating margin | **5.9%** | **12.1%** | **14.2%** |

In every one of the ten years SiteOne's operating margin is between 36% and 57% of Pool Corporation's, though its gross
margin is higher: the difference is the cost to serve, test 6. Pool kept part of its 2021-22 gain (11.0% in 2025 against
10.0% to 10.7% from 2016 to 2019); SiteOne kept none of its own (5.1% against 4.5% to 5.3%).

**The field's returns over the last full cycle, judged in words.** No full landscape cycle, peak to peak, lies inside the
public record (IPO 2016; one demand peak, which the filer describes as "peak demand during the three-year COVID-19
pandemic", Item 7). Over the decade, from the filings: pre-tax operating income on tangible capital (equity plus debt and
finance leases less cash, goodwill and acquired intangibles; operating leases left out) ran 19% to 22% from FY2016 to
FY2019, 30% to 40% in FY2020 to FY2022, and 16% to 23% from FY2023 to FY2025; with the branch leases of about $460M counted
as capital it is near 15% in FY2025. On all the capital the owners have paid, goodwill included, it was 12.0% pre-tax in
FY2025 and 9.7% in FY2024. A thin-margin business works only if its capital turns: "a one percent pre-tax margin only works
in terms of return on capital if you turn your equity extraordinarily fast" **[M2017-096]**; SiteOne's tangible capital
turns about 3.8 times a year, which is what makes a 5% margin earn about 19%. Judged in words: a fair return on tangible
capital, an ordinary one on what the growth has cost, and the better years not held. The change for the better of 2021-22
is not credited, since it did not hold through the softer years that followed; the price behaviour gave it back
**[M2005-020]**. The one row in the ledger on the class of business, said of distributors, is "the distribution business is
not a wonderful business, but it is a business" **[M2024-044]**; by the convention on rows about one company it is weighed and
decides nothing alone.

**Why the box is OUT and not TOO HARD.** A castle whose future cannot be judged goes to TOO HARD, as with "a moat that’s
tenuous in any way [...] We don’t know how to valuate that" **[M2000-019]**. Here the future can be judged, and the evidence
runs one way: the filer has stated for eight years that entry is easy; the money test is answered yes by the business's own
history and by Home Depot's purchase; the price follows the commodity; the cost to serve has not fallen with scale; the
operating margin is where it was in 2016. The framework's list of what Q2 rules OUT carries the case by name: "there are
some industries that are just never going to have barriers to entry. And in those industries, you better be running very
fast" **[M2012-106]**, and "anything you do, your competitors can copy" **[M1996-017]**. The moat the speakers ask for is one
that "protects excellent returns on invested capital" **[L2007-004]**; the returns here are fair on tangible capital and
ordinary on the capital paid, and what protects them, by the filer's own account, is not a barrier.

**Contrary evidence, written down** **[M1997-127]**: gross margin widened 3.5 points and held through deflation; the large
players took eight points of share in seven years; the business is the largest and the only national full-line
distributor; private brands are about 15% of sales; the return on tangible capital is near 19% pre-tax. These say the
business is the best-placed participant in a field without a barrier, not that the field has one.

**VERDICT: OUT.** The castle is shown open on the filer's own evidence (10-K `0001650729-26-000005`, Item 1A: barriers to
entry "generally low"; the organic price record FY2021 to FY2025; operating margin 4.2% to 6.6% outside FY2021-22 against
Pool Corporation's 10.0% to 16.6% in every year) **[M2011-015]**, **[M2012-106]**, **[M2006-013]**. The file closes here.
Q3 to Q12 are NOT REACHED; the facts already found are below, under AFTER THE STOP.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file). Facts found are under AFTER THE STOP.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The ten balance sheets were read in Step 0 (above), as the brief requires when the file closes
before Q4; the other facts found are under AFTER THE STOP.

## Q5: WHO RUNS IT. STOP on integrity.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found, including the buyback prices set beside the bottom of the computed range below, are under AFTER
THE STOP.

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The operator's two reporting figures follow, under the protocol's heading.

### COMPUTATION, NOT A CLEARANCE
*(Operator rule 3: computed after Q2 closed the file; no entry language; the figures are the reporting convention of Part VII,
"The owner's price", and decide nothing.)* Inputs: owner cash from Step 0; sovereign 5.60%; floor about 10% (Q7's
CONVENTION); price $87.99 (aggregator); 43.655M shares; net debt at the latest filed balance sheet, 2026-06-28 (10-Q
`0001650729-26-000016`): long-term debt $505.7M (current $3.9M plus $501.8M) plus finance leases $137.3M less cash $87.4M,
$555.6M, plus the July 2026 repurchase of $10.0M that the 10-Q states as a subsequent event, **$565.6M**; operating leases
($485.1M) left out, as the convention says. Market value $3,841.2M; market value plus net debt $4,406.8M. Script
`scripts/compute.py`, output `compute_output.txt`.

**The range convention applied, specific by specific.**
- *The base:* the five-year average FY2021 to FY2025 of owner cash after every real cost (Step 0): **$182.3M all-equity**
  (before interest, after the company's own tax), $181.3M equity-only.
- *(a) Cycles:* the first window year, FY2021, lies inside what the filer calls "peak demand during the three-year COVID-19
  pandemic" (Item 7), but owner cash, the series that defines the cycle, did not peak there: the inflation-driven inventory
  build of FY2021-22 ($156.9M and $99.3M) held it down, and the release of FY2023-24 lifted it. No full cycle, peak to peak,
  lies in the public record (IPO 2016). The literal window is therefore the base; the FY2025 year alone is shown beside for
  scale.
- *(b) Decline:* not applicable; the growth shown is positive.
- *(c) Acquisitions:* cash paid for businesses with contingent consideration was $796.9M over the window against $911.7M of
  all-equity owner cash before purchases, a ratio of 0.87, above one half: **the serial acquirer** rule applies, and the
  central figure is the organic pair, purchases left out, with the filer's organic growth. Organic daily sales growth as the
  filer reports it, FY2022 to FY2025: 11%, flat, minus 1%, plus 1% (the 10-Ks for FY2022 to FY2025), compounding to
  **2.64% a year**. The default pair (purchases deducted, total growth credited) is shown beside: owner cash after purchases
  averaged only $23.0M over the window, with total growth of owner cash of 7.87% a year. No deal signed and unclosed was found
  in the 8-Ks of 2026. Deals closed after the window: the 2026 purchases (Reinders and others, $72.1M of cash in the first
  half, 10-Q) and the June 2026 purchase of Devil Mountain's remaining 25% for 216,994 treasury shares ($26.5M), both financed
  inside the June net debt or the share count, are credited at nothing, since no earnings of theirs are filed. No merger (a
  deal paid in shares) inside the window.
- *(d) Working capital:* counted; it is inside operating cash flow.
- *(e) Maintenance:* the filing gives no split; total spending has run near depreciation (Step 0), so the all-spending case is
  central and the depreciation variant is beside it in Step 0.
- *(f) The cap:* 2.64% is below the business's sales growth over the window (7.86% a year) and below the discount rate; owner
  cash carried ten years at it stays below the highest share of sales the business has earned (7.0% in FY2020). No cut.
- *After year ten:* zero nominal growth, discounted at 5.60%.
- *The floor tested first:* the expected return at the price, on the central pair, is **4.1% (no growth) to 5.1% (organic
  growth)**, below the floor of about 10% on every case. The price, $87.99, is **above the top of the range**. Had Q7 been
  reached, it would close OUT on the floor whatever the width **[M2003-149]**. Width, for the record: 1.28 to one.

| case | value range a share | expected return at $87.99 | fair price |
|---|---|---|---|
| **Central: all-equity, organic pair** | **$61.63 to $79.02** | 4.1% to 5.1% | **$32.93** |
| Beside: equity-only, organic pair | $74.15 to $91.44 | 4.7% to 5.8% | **$45.62** |
| Beside: all-equity, default pair (purchases deducted) | negative to $4.58 | 0.5% to 1.1% | negative |
| Beside: all-equity, organic pair, FY2025 owner cash alone ($216.8M) | $75.72 to $96.40 | 4.9% to 6.0% | $41.60 |
| Beside: all-equity, organic pair, net debt at the 2025-12-28 year-end ($329.6M, the seasonal low) | $67.04 to $84.43 | 4.4% to 5.4% | $38.34 |

**(a) VALUE RANGE: $61.63 to $79.02 a share** (all-equity basis, central) against **$87.99**; the equity-only range beside it,
$74.15 to $91.44. **(b) FAIR PRICE: $32.93 a share** on the all-equity basis (each end case valued at ten percent and the two
averaged, after the company's own tax, less net debt), **$45.62** on the equity-only basis beside it. Neither is a verdict,
and no cheap price is reported (Part VII).

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (No business the rows name, casinos, tobacco, loading schemes, is among its lines.)

---
## THE BOX
**OUT at Q2** (the castle is shown open on the filer's own evidence). Computed range beside the price, COMPUTATION, NOT A
CLEARANCE: $61.63 to $79.02 a share (all-equity, organic pair) against $87.99; fair price $32.93 all-equity, $45.62
equity-only. Integrity facts recorded, not judged (guidance and a featured adjusted figure; see AFTER THE STOP, Q5).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found, each with its source, under the question it bears on **[M1997-127]**; no verdict; the box is
unchanged, operator rule 2.)*

**Q3 (capital).** Pre-tax operating income on tangible capital about 19% in FY2025, 16% in FY2024, 19% to 22% in FY2016 to
FY2019 (Q2's table); on all capital paid, goodwill included, 12.0% in FY2025. Capital spending "0.8% to 1.3%" of sales
guided for FY2026 (10-K Item 7); the delivery fleet, held on finance leases, adds $38.1M to $61.3M a year of assets obtained
in FY2023 to FY2025 (Note 6). Growth is bought: $796.9M paid for businesses in FY2021 to FY2025 against $911.7M of owner cash
before purchases; Item 7 states "we have invested $175.9 million in 15 acquisitions since the start of the 2024 Fiscal
Year", and acquired branches contributed $220.5M of FY2025 sales (Item 7, the organic reconciliation). Equity of $1,659M at
FY2025 includes $750M of goodwill and acquired intangibles.

**Q4 (the accounts).** No confusion or suspicion found in the statements read: receivables and inventory move with sales; no
prepaid or deferred account builds out of line. Facts to weigh: the allowance for doubtful accounts rose from $4.7M (FY2017)
to $33.3M (FY2025), about 6% of gross receivables (Item 7A). Adjusted EBITDA is presented in the 10-K and featured first in
the releases; it adds back stock-based compensation ($27.0M FY2025) and "Acquisitions and other adjustments" ($8.6M FY2025,
$20.9M FY2024), which include charges "for consolidating or closing certain branch locations" in the fourth quarters of both
2025 and 2024, a recurring item. The company's debt covenants use Adjusted EBITDA (Item 7). Annual Adjusted EBITDA guidance
is given ($425M to $455M for FY2026, Exhibit 99.1, `0001104659-26-087746`), with no reconciliation provided for the forward
figure. Tax: investments in tax-advantaged renewable-energy partnerships from 2024, amortized through income tax expense
(Note 1); effective rate 22.5% FY2025.

**Q5 (the people), integrity facts recorded, not judged.** The habits Q4 carries to Q5: earnings guidance given each year on
an adjusted figure, and Adjusted EBITDA featured ahead of GAAP in the releases. The Chairman is also the Chief Executive (Doug
Black, Exhibit 99.1). No material litigation (10-K Item 3); no investigation disclosed in the filings read. Pay (DEF 14A
2026, `0001104659-26-038879`): the CEO's total for 2025 was $6,177,856 (salary $970,673, stock awards $4,199,864,
non-equity incentive $984,930); the annual incentive weights Adjusted EBITDA at 70%; the 2023-2025 performance shares paid
0% of target on the three-year EBTA decline; from 2025 the performance shares run on relative EBTA (70%) and absolute ROIC
(30%), ROIC defined as "annual EBITA divided by the average Net Assets for the four reporting quarters of the fiscal year".

**Q6 (the money and the owners).** No dividend ("We do not expect to declare or pay dividends", Item 5). Buybacks under a
$400M authorization of October 2022 that names no price: about 90,000 shares for $11.4M in FY2023 (about $127 a share, from
the statement of equity), 366,400 shares for $51.6M in FY2024 (about $141), 816,888 at an average of $119.62 in FY2025, 952,216
at $119.46 in the first half of 2026, 100,692 at $99.29 in July 2026 (10-K and 10-Q). Every average price paid sits above the
top of the computed central range ($79.02) and above the bottom ($61.63) by between 61% and 129%; the convention's test
(prices paid at or below the bottom of the Q7 range) is not met on any year, recorded here unweighed. Issuance: 2,150,000 new
shares in August 2020 for $261.7M net, about $121.7 a share (10-K FY2020). The June 2026 Devil Mountain minority buyout was
paid in 216,994 treasury shares on the holders' put option ($26.5M, 10-Q). Serial acquirer by the convention's test (ratio
0.87).

**Q9 (debt and exposures).** Net debt $555.6M at 2026-06-28, which the company puts at 1.3 times trailing Adjusted EBITDA
(Exhibit 99.1); $329.6M at the December 2025 year-end. All borrowing is floating rate (Item 7A: one point on rates adds about
$3.9M of interest). Gross long-term debt was $389.4M at FY2025, chiefly the Tranche B term loans maturing 2030-03-22; the $600M ABL, secured on inventory and receivables,
was extended to April 2031 (8-K 2026-04-27); current maturities $3.9M. Operating leases $460M at FY2025, finance leases
$134.8M. FY2025 operating income $238.1M against $35.0M of interest and other non-operating expense. Credit extended to
most customers on 30 to 60 day terms; no customer over 5% of receivables (Item 7A).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 5ef1e24d); written question by question; committed after Step 0 and
      Q1 (9a4c29fc) and after Q2 (a4b810ae), and after this close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not checked by
      the analyst, who wrote no lock); the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; no text search ran across
      `Test Runs/` (every search ran inside this run's own research folder or on the framework, the ledger and the filings).
      What was seen by accident is declared under contamination at the top.
- [x] Every v5 id resolves (`scripts/check_ids.py`: every id in the CSV, no E-id; every quoted row fragment found in its row;
      the checker's remaining flags are all filing quotes standing in the same span as an id, each read). Every filing fact
      carries its accession or names its filing.
- [x] The order was kept; Q2's STOP closed the run; everything after it is NOT REACHED or under AFTER THE STOP, and every
      valuation figure sits under COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy: OCF less SBC, all capital spending, software, and the
      fleet on finance leases (operator rule 5); the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (foundations; Q2's contrary paragraph); facts for later questions under AFTER
      THE STOP, with the integrity flag in the box line.
- [x] No point-in-time anchor; rows of any year usable. No row dated after today is cited.
- [x] Only the arithmetic lines of `tools/run.py` were used; its D&A column (intangible amortization only) was set aside, as
      its own warning said, and its owner-earnings line was not used because it leaves out the fleet.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the research folder notes).
- Honest limits: the XBRL series for FY2016 to FY2022 were transcribed from first-filed values and spot-checked against the
  filed FY2020 and FY2022 statements (contingent payments, capex), not read line by line for every year; FY2016 to FY2018
  fleet spending uses capital-lease principal as a stand-in; the rivals' margins are their parents' consolidated figures.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The fleet on finance leases.** Q7's basis puts finance leases in net debt, but neither Q4 nor Q7 says how the assets
acquired on finance leases are charged in owner cash; `tools/run.py` offers the principal paid as an alternate. On the
all-equity basis the principal is debt service and the spending is the assets obtained; on the equity-only basis the reverse
reads more naturally. I confessed a CONVENTION of this run (assets obtained on the all-equity basis, principal on the
equity-only basis). The difference is about $4M to $35M a year here.

(2) **Seasonal net debt.** The basis takes net debt "at
the latest filed balance-sheet date", which for a seasonal distributor is the June peak of inventory and borrowing ($565.6M
against $329.6M at the year-end); the rule moves the fair price by $5.41 a share. I applied it and showed the year-end beside.

(3) **The organic pair's growth.** "organic growth as the filer reports it" is a sales measure that here includes price
(18% of FY2022's 11%); the text does not say over which years it is compounded or whether price is in it. I compounded the
filer's reported figures for the four growth years of the window.

(4) **Ordinary returns at Q2 for a business whose
network was bought.** Q3's rows say to forget goodwill when judging the business and include it when judging the capital
allocation **[M2011-060]**; for a roll-up the castle and the purchases are the same thing, and the two measures here (about
19% and about 12% pre-tax) point different ways. I stated both and did not rest the OUT on either alone.

(5) **The competitor
row when every named rival is private or a subsidiary.** The brief and template ask for the rivals' own filings; here the
two that file are parents that do not report the landscape line, and the text gives no rule for that case; I used them as
indicative and said so.

(6) **A row about a class of business.** The convention on a row about one company (Q2) does not say
whether a row on a class ("the distribution business") falls under it; I treated **[M2024-044]** the same way, weighed and
deciding nothing.
