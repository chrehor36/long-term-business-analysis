# Company Run — The Manitowoc Company, Inc. (NYSE: MTW) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, after the run was committed: not held (`PORTFOLIO.md` read for this one ticker, 2026-10-13).*

**Dispatch.** A purchase run of record dispatched to a blind analyst under `Screens/_daily/_dispatch_brief.md` with its
slots filled; the brief departs from the canonical one in one place, which it states (the lines of evidence and the
competitors are taken by the analyst from the 10-K, not written by the dispatcher). Working folder
`Test Runs/_research 2026-10-13 MTW/` (notes, fetch script, owner-cash script and its output, ledger rows read; raw
filings in its `cache/`, gitignored).

**Contamination, declared.** (1) The session's opening git status and recent commit subjects showed the fold and run
commits of another company, TEX (Terex Corporation), dated 2026-10-13, including its box and figures. Terex is named in
MTW's 10-K as a rival, and its own SEC filings are read below for the competitor row; the TEX run file, its research
folder and its fold were not opened, and nothing of the commit subjects is used. (2) The session's memory index named the
queue state in general terms (a wave paused, gate-clearers counted, "nothing buyable"); nothing about MTW. No other
blind-listed file was opened, listed or searched.

**Lines of evidence chosen, and why** (from the 10-K for 2025, Items 1, 1A and 7, accession 0001193125-26-057356).
Item 1 says the company makes and services cranes (crawler, tower, mobile hydraulic) in three geographic segments, names
its rivals (Liebherr, Tadano, Terex, Sany, XCMG, Zoomlion and others) and claims brand, resale value, distribution and
aftermarket as its advantages. Item 1A names cyclicality, price competition from rivals "better positioned to compete on
price", low-cost Chinese competition, steel and tariffs, leverage (second-lien notes at 9.25%), residual-value guarantees
and buyback commitments, pensions, goodwill, an EPA consent decree and product liability. Item 7 shows a 2.4% operating
margin, an adjusted ROIC of 5.3%, segment losses in Europe, and a $45.6M EPA payment inside 2025's operating cash. So
the lines read: (a) margins and returns through the last two cycles, standalone (2016 to 2025) and as the Crane segment
of the former parent (2005 to 2015); (b) the segment split, to find the deciding part; (c) price realisation through the
2021 to 2023 inflation; (d) the one SEC-filing rival's crane results over its last eight years in the business; (e) the
balance sheets 2016 to 2025; (f) cash flows including the receivables securitization that moved collections into
investing through 2019; (g) acquisitions (Aspen and H&E's crane business 2021, Honnen 2022, Ring Power 2025); (h) debt,
leases, pensions, guarantees; (i) buybacks, stock pay, the proxy's pay metrics; (j) litigation and the EPA matter.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $21.91 (2026-10-13; `tools/run.py` live quote, an aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class of common stock, **36,061,969** shares outstanding as of
  June 30, 2026 (10-Q for the quarter ended 2026-06-30, filed 2026-08-07, accession `0001193125-26-340218`; the cover
  sentence reads "As of June 30, 2026, the registrant had 36,061,969 shares of common stock"). `python
  Screens/cover_shares.py MTW` parsed no cover count and asked for the filing to be read by hand, which was done. Check:
  the balance sheet gives 40,793,983 shares issued and 36,061,969 outstanding, so 4,732,014 in treasury; the only 8-K
  filed after that 10-Q (2026-08-25, accession `0001193125-26-365102`, Item 7.01, a conference presentation) changes no
  share count. An amended omnibus plan approved 2026-05-05 authorises up to 1,800,000 more shares for awards (8-K
  `0001193125-26-209097`).
- **Market cap:** $790.1M (36.062M × $21.91).
- **Sovereign for the earnings currency (USD):** 5.60%, the 30-year par yield on the US Treasury daily par yield curve,
  dated 2026-10-09 (the issuing authority; read by `tools/run.py`'s sources library).
- **Filings read** (operator rule 4): the 10-K for 2025 (filed 2026-02-18, `0001193125-26-057356`); the 10-Ks for
  2024 (`0000950170-25-024838`), 2023 (`0000950170-24-019452`), 2022 (`0000950170-23-004241`), 2021
  (`0000950170-22-001624`), 2020 (`0001564590-21-005680`), 2019 (`0001564590-20-004745`), 2018
  (`0001564590-19-002823`), 2016 (`0000061986-17-000007`), 2015 (`0000061986-16-000073`) and 2010
  (`0001104659-11-011464`); the latest 10-Q (`0001193125-26-340218`); the proxy filed 2026-03-20
  (`0001193125-26-117619`); the 8-Ks of 2026-01-21, 2026-03-30, 2026-03-31, 2026-05-06 and 2026-08-25. Rival filings:
  Terex 10-Ks for 2013 (`0000097216-14-000027`), 2015 (`0000097216-16-000245`) and 2018 (`0000097216-19-000024`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities 2025, $22.2M in
  the filed cash-flow statement and in Item 7 of `0001193125-26-057356`, equals the tagged figure `tools/run.py` prints;
  net sales 2025, $2,240.9M, likewise.
- `python tools/run.py MTW` arithmetic lines only (`Test Runs/_research 2026-10-13 MTW/run_py_output.txt`): on the
  tool's own definition (operating cash less stock pay less capital spending) the three-year mean is -$19.4M and the
  five-year mean -$4.6M; the depreciation basis is worse (-$27.7M and -$11.3M). The tool's operating cash for 2016 to
  2019 is as filed and omits the receivables collections the filer classified as investing; the run's own series below
  restores them. Nothing the tool prints as a rule or a verdict is used (Part VII, the tooling).

**Owner cash, recast from the filed cash-flow statements** (`Test Runs/_research 2026-10-13 MTW/owner_cash.py`, output
beside it; USD millions). Owner cash = operating cash (2017 to 2019 with "Cash receipts on sold accounts receivable", which
the filer classified as investing, added back: $402.8M, $553.1M, $126.3M) less stock pay, less capital spending, plus
proceeds from fixed assets sold; purchases of businesses shown apart. The all-equity column adds back interest expense
after the 21% US statutory rate.

| year | equity-only owner cash | all-equity owner cash | businesses bought (net) |
|---|---|---|---|
| 2017 | 47.5 | 78.5 | 0 |
| 2018 | 14.0 | 44.9 | 0 |
| 2019 | 45.6 | 71.4 | 0 |
| 2020 | -66.9 | -43.9 | 0 |
| 2021 | 29.0 | 51.8 | 186.2 (Aspen; H&E crane business) |
| 2022 | 8.1 | 33.1 | -2.3 (price adjustment) |
| 2023 | -20.3 | 6.5 | 0 |
| 2024 | -2.6 | 27.7 | 0 |
| 2025 | -23.9 | 5.9 | 12.9 (Ring Power assets) |

Five-year (2021 to 2025) mean before purchases: equity-only -$1.9M, all-equity $25.0M; with purchases deducted -$41.3M
and -$14.4M. The 2025 figure carries the $45.6M "payment to settle a legal matter with the U.S. EPA and associated
environmental mitigation project" (Item 7, `0001193125-26-057356`). Stock pay $9.5M in 2025, deducted in full.

**The balance sheets, 2016 to 2025, read in Step 0** (the file closes before Q4; `tools/run.py`'s ten-year table checked
against the filed balance sheets of the 10-Ks listed). What moved, and what it says **[M2025-032]**:
- **Retained earnings fell over the decade**, $247M (2016) to $206M (2025), with no dividend paid in either 2024 or 2025
  ("no cash dividends were declared or paid", Item 5) and none tagged in 2017 to 2021. Ten years of a standalone crane
  business added nothing to retained earnings.
- **Equity** rose only from $590M to $695M (stock pay and currency, not earnings); **goodwill** fell from $300M to $80M
  through impairments, the last $166.5M in 2022 in the Americas segment (10-K 2023, `0000950170-24-019452`), so most of
  the goodwill of the old Crane business and of the 2021 distribution purchases has been written off.
- **Inventory** rose from $429M to $684M at end-2025 and $785M at 2026-06-30, against sales up from $1,613M to $2,241M:
  26.6% of sales in 2016, 30.5% in 2025. The proxy says 2025's "elevated inventory levels" came with "the Great Trade
  Reset" (`0001193125-26-117619`), and the pay plan replaced net working capital with Days Inventory Outstanding as a
  metric.
- **Receivables** $134M to $281M (8.3% to 12.5% of sales); the rise follows the end of the securitization program in
  2019 and 2020, which had kept receivables off the balance sheet, not a loosening of terms as far as the filings say.
- **Debt** $282M to $461M (and $473.5M principal at 2026-06-30), cash $70M to $77M ($95.8M at 2026-06-30).
- What they cannot say: whether the inventory build is cyclical or a loss of position; the filings attribute it to
  tariffs and demand timing.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would own this crane business if the market closed for five years
**[M1997-109]**, which turns the run entirely on the business's earnings over cycles, not on the 2021 to 2025 quotation
(the 10-K's own table shows annual returns of +39.67%, -50.73%, +82.21%, -45.30% and +31.33%). No macro forecast enters:
the construction cycle is read from the filings' own history, not predicted. Who is paid to tell you: the company leads
with Adjusted EBITDA and Adjusted ROIC and pays on them (proxy). The analyst's habits: look for "what’s wrong in things"
**[M2025-013]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) orders rose 22.7% in 2025 to
$2,359.0M and backlog 22.0% to $793.5M (Item 7), and the Americas segment earned 7.6% to 9.2% before corporate costs in
each year 2021 to 2025, so the North American business is not failing; (2) the filer reports $15.5M of "price realization
and favorable product mix" in the Americas in 2025 and "price realization" in 2019; (3) the Cranes segment of the former
parent earned 14.3% to 14.5% operating margins in 2007 and 2008 (10-K 2010), so the business has earned well at a peak;
(4) the aftermarket and "non-new machine" strategy, if it works, lowers capital and cyclicality. Each is weighed at Q2.

## THE STANDING RULE
Owning a small part-interest in MTW bought for cash, unlevered, does not put the buyer at risk of ruin: the rule binds
the buyer's conduct, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**,
and nothing in a cash purchase of listed shares gives anyone a call on the buyer **[L2014-024]**. The target's own
leverage is Q9's, not this rule's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **The key variables** **[M1998-044]**: (1) the construction and infrastructure cycle, which sets unit volume; (2) the
  price the company can get against Liebherr, Tadano and the Chinese makers; (3) steel and component costs and tariffs;
  (4) the share of sales from parts, service, rental and used machines. The product is slow-changing: lattice-boom
  crawlers, tower cranes and hydraulic mobiles are the same machines the 2010 and 2015 10-Ks describe, and the 10-K for
  2025 describes eleven updated all-terrain models and fourteen tower models since 2021 as refinements (longer booms,
  lighter, telematics), not a change of what a crane is. The filer's boilerplate says its markets are "characterized by
  changing technology" (Item 1A); the product history in four 10-Ks fifteen years apart does not bear that out.
- **Foreseeable?** The volume variable is cyclical and not forecastable year by year, but the economics across a cycle
  are on the record: two standalone cycles (2016 to 2025) and the former Crane segment's numbers since 2005. Whether the
  past statements tell me the future ones **[M2008-033]**: the cycle repeats in the record, and the question of the
  company's position within its industry is Q2's. Would insiders write down a ten-year view of a crane maker's economics?
  The filer itself publishes long-term aspirations (12% Adjusted EBITDA margin, 15% Adjusted ROIC), which is an
  insider writing one down, whatever its worth. This is not the tech field of the row, where insiders asked for ten-year
  economics would answer "They would say, “That’s too hard.”" **[M2000-105]**. The figures can be read: "if you can’t make a decision on something like PetroChina off the
  figures, forget about going further" **[M2008-069]**; these figures decide it either way. As with a business whose
  chemistry is opaque, what matters is "the economic dynamics of the industry" **[M2011-014]**, and they are readable
  here: a cyclical, steel-heavy, dealer-sold capital good with a large aftermarket.
- **Doubt test** **[M2002-092]**: no doubt that the business is understood well enough to judge its castle and its
  returns. The parts: the three segments are geographic sales regions of one crane business, not businesses with
  different economics, so Q1 is answered for the whole.
- **VERDICT: IN.** The economics can be pictured ten years out in the sense the rows ask: a cyclical crane maker whose
  earning power is shown over two cycles in its own filings **[M2012-065]**, **[M2000-037]**, **[M2008-069]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (segment operating income before unallocated corporate costs, five years 2021 to 2025, USD millions;
10-Ks for 2023 `0000950170-24-019452` and 2025 `0001193125-26-057356`). The three segments are geographic regions of
one crane business, but the filer reports them with different economics, so they are read apart **[L2008-005]**.

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Americas | 57.3 | -88.8 (83.1 before the $171.9M impairment) | 111.7 | 103.7 | 95.7 | 279.6 (451.5 before impairment) | 70.7% (79.6%) of the segments' net sum | read below | **yes, more than half** |
| EURAF | 8.9 | -3.2 | -7.9 | -46.6 | -42.9 | -91.7 | negative | open on its own record: losses in four of five years against Liebherr and the Chinese makers | no |
| MEAP | 30.9 | 40.2 | 52.3 | 39.4 | 44.6 | 207.4 | 52.5% (36.6% before impairment) | not read separately | no (the Americas is larger and above half) |

Unallocated corporate costs are not in these figures: "Other corporate expenses" $63.6M (2023), $44.7M (2024), $43.6M
(2025), plus restructuring and amortisation (10-K 2025, Note 17).

**The deciding part, the Americas: segment margins through the cycle** (segment operating income over segment sales,
before corporate costs; 10-Ks for 2019, 2020, 2023 and 2025):

| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | nine years |
|---|---|---|---|---|---|---|---|---|---|---|
| sales | 693.6 | 882.7 | 969.7 | 626.1 | 757.6 | 1,013.0 | 1,211.2 | 1,197.6 | 1,259.9 | 8,611.4 |
| operating income | 6.8 | 58.8 | 113.4 | 32.1 | 57.3 | 83.1* | 111.7 | 103.7 | 95.7 | 662.6 |
| margin | 1.0% | 6.7% | 11.7% | 5.1% | 7.6% | 8.2% | 9.2% | 8.7% | 7.6% | 7.7% |

*before the 2022 goodwill and intangible impairment of $171.9M, recorded in this segment. The Americas holds the
distribution business bought in 2021 for $186.2M, whose reporting unit carried goodwill into that impairment.

**The old Crane segment through the cycle before** (operating earnings over sales, before corporate costs; 10-K 2010
`0001104659-11-011464` and 10-K 2015 `0000061986-16-000073`, Selected Financial Data):

| 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 |
|---|---|---|---|---|---|---|---|---|---|---|
| 7.1% | 12.6% | 14.5% | 14.3% | 6.3% | 5.1% | 5.6% | 7.0% | 8.7% | 7.1% | 3.4% |

(Crane operating earnings $115.5M, $280.6M, $470.5M, $555.6M, $145.0M, $89.8M, $118.8M, $170.5M, $218.8M, $163.9M,
$64.3M; sales from $1,628.7M in 2005 to $3,882.9M in 2008 and $1,865.7M in 2015.)

**The standalone company through two cycles** (XBRL transcription of the filed statements, checked against Item 7 for
2025):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| operating income, $M | -143.0 | 8.4 | -19.3 | 108.4 | 38.6 | 46.5 | -93.0 | 92.4 | 51.8 | 53.8 |
| operating margin | -8.9% | 0.5% | -1.0% | 5.9% | 2.7% | 2.7% | -4.6% (3.9% before impairment) | 4.1% | 2.4% | 2.4% |
| gross margin | 15.7% | 17.8% | 17.8% | 18.8% | 17.6% | 17.9% | 17.9% | 19.1% | 17.2% | 18.1% |

Ten years: operating income $144.4M on sales of $18,718M, 0.8%; with the 2022 impairment added back, $316.3M, 1.7%.
The company's own "Adjusted ROIC" (adjusted operating profit taxed at 15%, over invested capital) was 5.3% for 2025 and
6.0% for 2024 ($52.5M over $999.5M; $58.1M over $969.9M; Item 7), against a long Treasury of 5.60%.

**The competitor row** (same metric, operating income over sales, from the rivals' own filings; the rivals are those
the 10-K names in Item 1):

| rival | files with SEC? | metric over the span | source |
|---|---|---|---|
| Terex, Cranes segment | yes | 2011 1.8%, 2012 8.5%, 2013 5.7%, 2014 4.8%, 2015 3.4%, 2016 -25.0% (with a goodwill impairment of about $176M and about $92M of severance and restructuring), 2017 -1.2%, 2018 -3.4%; then sold its Demag mobile cranes to Tadano and announced its exit from the North American mobile crane lines (agreement of 2019-02-22) | Terex 10-Ks `0000097216-14-000027`, `0000097216-16-000245`, `0000097216-19-000024` |
| Tadano | **no**, a Japanese filer; its English integrated reports were sought from its own site, which refused the download three times on 2026-10-13; not read | not obtained | flagged |
| Liebherr | **no**, private; publishes a group report; not read | not obtained | flagged |
| Sany, XCMG, Zoomlion, Liugong, Yongmao, Dahan, ZTM | **no**, Chinese filers; not read | not obtained | flagged |
| Hitachi Sumitomo, Kobelco, Link-Belt | **no**, Japanese parents; not read | not obtained | flagged |
| Broderson, Elliott, Locatelli, Cattaneo, Comansa, Favelle Favco, Jaso, Raimondi, Saez, Stafford/SOIMA, Vicario, Wolffkran | **no**; not read | not obtained | flagged |

Only one named rival files with the SEC, and its crane record over eight years is no better than Manitowoc's, ending in
losses and exit.

**The castle tests, each with its filing fact.**
- **What keeps it standing, and how permanent**: the row's own warning is that "most moats aren’t worth a damn"
  **[M1995-038]**. The filer names brand names with competitive resale values, quality, its distributor network, broad
  lines and in-house service as its advantages (Item 1). These are real, but the test is what they protect: across two
  standalone cycles, a 0.8% to 1.7% operating margin and a retained-earnings account that shrank over ten years.
- **The attacker with money** **[M2011-015]**: the filer lists rivals with "greater financial, marketing, manufacturing,
  and distribution resources" who may be "better positioned to compete on price" through "low-cost labor, raw materials,
  components, facilities or other operating items, or willingness to sell at lower margins than us", and warns of
  "Low-cost competition from China" (Item 1A). In Europe the attackers are already inside the walls: losses in four years
  of five.
- **Pricing power and the agony before a rise** **[M2005-020]**: gross margin held between 17.2% and 19.1% through the
  2021 to 2023 inflation, so prices followed costs but did not widen the margin; in 2025 the Americas booked $15.5M of
  "price realization and favorable product mix" while $6.1M of net tariff costs went unrecovered and its operating
  income fell $8.0M (Item 7). Price that follows cost is not the strength the row measures.
- **Unit volume and share of mind**: orders rose 22.7% in 2025 (Item 7), but sales over the decade went from $1,613M
  (2016) to $2,241M (2025), well below the $3,883M the Crane segment sold in 2008; no filing read gives market share.
- **The low-cost position**: no filing read says Manitowoc is the low-cost producer, and the filer says rivals are better
  placed on price; "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**.
- **Would the customer choose it over the low bid?** The filer says customers weigh "overall total cost of ownership,
  which includes an attractive resale value" (Item 1): a reason a buyer pays something for the brand, and the margins
  show how little.
- **Ask the competitors**: the one rival on the SEC record answered by selling its mobile cranes and leaving the North
  American mobile crane lines.
- **Widening or narrowing** **[M1999-108]**: the Crane business earned about 14% at the 2007 and 2008 peak; at the 2019
  and 2023 peaks the standalone company earned 5.9% and 4.1%, and the Americas 11.7% and 9.2% before corporate costs.
  The peaks are lower, and Europe has turned to losses. The question is "whether it’s likely to widen further or shrink
  on you" **[M1999-108]**, and the record shows shrinking.
- **What could destroy, modify or reduce it** **[M2000-014]**: the Chinese makers the filer names; tariffs that now
  shelter the Americas and could be lifted; "one competitor is frequently enough to ruin a business" **[M2012-108]**.

**The field's returns over the last full cycle, judged in words** (section C). Over 2016 to 2025, two full cycles,
Manitowoc earned a low single-digit operating margin and, on its own adjusted measure, a return on invested capital at or
below the long government rate; the deciding part earned 7.7% of sales over nine years before the company's unallocated
costs, on a business that carries inventory of 30.5% of sales. The one SEC-filing rival earned less and left. The castle
the speakers ask for "protects excellent returns on invested capital" **[L2007-004]**, the great business will "earn a
high return on capital employed for a very long period of time" **[M2007-023]**. The filings show a field whose durable
players earn ordinary returns at best through a full cycle; "you can have only two competitors and they’re still
terrible businesses" **[M2013-052]**. The moat is judged, not measured, "You have to understand the businesses."
**[M1999-108]**; judged in words, this one protects ordinary returns.

**Why not TOO HARD.** The tenuous-moat row sends a castle to TOO HARD because "We don’t know how to valuate that"
**[M2000-019]**; here the returns are known from two cycles of the company's own filings and the rival's, so that reason
does not apply (Q2, What it rules OUT, the standing castle that protects only ordinary returns). No change for the better
is on the record: the aftermarket strategy (CRANES+50, launched in 2021) is the filer's stated plan, and a change is
credited only on a full cycle; the row sorts a year by asking whether it is "a cyclical problem, not a secular one"
**[L1995-022]**, and no full cycle has yet been run under the plan. Price does not reopen it: "What you can’t do is turn any
investment into a good deal by paying little" **[M2019-015]**.

- **VERDICT: OUT.** The deciding part's castle, read with the whole company's and the one SEC-filing rival's returns over
  full cycles, protects only ordinary returns, and the filer places the price advantage with its rivals **[L2007-004]**,
  **[M2013-052]**, **[M1997-010]**, **[M2006-013]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (closed at Q2; the balance sheets were read in Step 0).
## Q5 — WHO RUNS IT. NOT REACHED (closed at Q2; integrity facts recorded below, not judged).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 — WHAT IS IT WORTH. NOT REACHED as a clearance; the reporting figures are below, under COMPUTATION, NOT A CLEARANCE.
## Q8 — BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED (facts below).
## Q10 — THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD. NOT REACHED; cranes are not among the named businesses.

---
## THE BOX
**OUT at Q2.** The deciding part, the Americas (71% of five-year segment profit, 80% before the 2022 impairment), has a
castle that protects only ordinary returns on the filer's own two standalone cycles and on the one SEC-filing rival's
record, and the filer places the price advantage with its rivals. Not TOO HARD, so no research pass is opened.
COMPUTATION beneath the stop: value range $1.30 a share (the no-growth case alone, all-equity, cycle base) against
$21.91; fair price negative (-$3.88 all-equity, -$0.25 equity-only); no case earns the floor at the price. **Integrity
facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box is unchanged.)*

**Q3, capital.** Capital spending $37.5M in 2025 against depreciation $59.9M, of which $18.8M was rental fleet; 2026
guided at $45M to $50M, about $25M of it rental fleet (Item 7, `0001193125-26-057356`). Inventory 30.5% of 2025 sales
($683.9M), $785.3M at 2026-06-30 (10-Q `0001193125-26-340218`). Adjusted ROIC 5.3% (2025), 6.0% (2024), on the
company's own definition with a 15% tax rate. The 2021 distribution purchases cost $186.2M; the Americas reporting unit
was impaired by $171.9M in 2022.

**Q4, the accounts.** The company features Adjusted EBITDA ($121.7M for 2025 in the proxy's opening summary) and
publishes long-term "aspirations" of a 12% Adjusted EBITDA margin and 15% Adjusted ROIC (Item 1). The 2024 adjusted
figures exclude $8.9M of EPA costs as "other non-recurring items". Restructuring charges appear every year 2016 to 2025
($27.2M in 2017, $4.9M in 2025). Net income for 2024 ($55.8M) exceeded operating income ($51.8M) because of a $57.5M
valuation-allowance release; net income for 2025 was $7.2M. Warranty payments $39.3M in 2025. Operating cash for 2016 to
2019 is understated in the operating line by the securitization collections the filer classified as investing ($453.9M,
$402.8M, $553.1M, $126.3M), disclosed in the filings (10-K 2018, 10-K 2020). Two receivables factoring programs outside
the US (€25.0M and €40.0M) are accounted as sales.

**Q5, integrity (recorded, not judged).** On March 28, 2025 a federal court entered a consent decree between the company
and the United States over "alleged violations of the Transition Program for Equipment Manufacturers" for cranes made
between January 1, 2014 and July 31, 2017; the company paid a civil penalty of $42.6M plus $0.6M interest and is
completing a $2.6M emissions mitigation project (10-K 2025, Note 18). The EPA's information request dated from July 2017
and concerned about 1,420 engines (10-K 2023, `0000950170-24-019452`); the 10-K for 2023 described "confidential
discussions" with the government. The 10-K for 2023 records charges "for certain product-related lawsuits" in the
Americas. Pay: the short-term plan weighs Adjusted EBITDA at 50%; the 2025 long-term awards pay on three-year average
Adjusted ROIC (60%) and Non-New Machine Sales (40%) with relative TSR as modifier (proxy `0001193125-26-117619`). The
chief executive since 2020 owns 1.8% and directors and officers 3.96%; none has pledged shares. Shareholders approved
1,800,000 more plan shares on 2026-05-05 (about 5% of the count). One director received 2,532,836 votes withheld against
roughly 500,000 for each other nominee (8-K `0001193125-26-209097`). The human resources chief resigned in March 2026 and
the general counsel took the role (8-Ks `0001193125-26-130512`, `0001193125-26-133438`).

**Q6, the money.** No dividends. Share repurchases $7.4M (2019), $12.0M (2020), $3.0M (2022), $5.5M (2023), $5.7M
(2024), none in 2025; no stated repurchase price found in the filings read. Acquisitions: Aspen and the H&E crane
business (2021, $186.2M), Honnen's rental fleet assets (2022), Ring Power territories and assets (2025, $12.9M).

**Q9, debt and exposures.** Debt principal $473.5M at 2026-06-30: $300.0M senior secured second-lien notes at 9.25% due
October 1, 2031; $158.5M drawn on the $325.0M asset-based revolver due September 18, 2029, secured first on inventory,
receivables and fixed assets; $15.0M other. Cash $95.8M. 2025 pre-tax income $12.4M against interest expense $37.7M;
operating income $53.8M, 1.4 times interest. Buyback commitments to customers' lenders $39.8M and residual value
guarantees (Item 7 and Item 1A). Operating lease commitments $82.2M. Pension and retiree plans underfunded by $46.4M.
Purchase obligations $984.6M. Covenants restrict dividends and buybacks. The filer says "Certain of our businesses also
have experienced claims relating to past alleged asbestos exposure" and "have not to date incurred material costs"
(Item 1A); the v5 text carries the row on asbestos as a candidate at Q9, not a ruling.

## COMPUTATION, NOT A CLEARANCE
*(Figures computed after the closing STOP; no verdict, no entry language; operator rule 3.)*

**Inputs.** Price $21.91 (aggregator, flagged); 36,061,969 shares; market cap $790.1M. Net debt at 2026-06-30, the
latest filed balance sheet: debt principal $473.5M (total debt $469.5M plus $4.0M deferred financing costs) less cash
$95.8M = **$377.7M**; operating leases left out (stated: $82.2M of commitments at end-2025); no subsequent event stated by
that filing changes it; no inventory-secured floor-plan debt. Sovereign 5.60%. Floor about 10% (Q7's CONVENTION),
applied to owner cash after the company's own tax; the company pays little cash tax under valuation allowances, so the
all-equity figure adds interest back after the 21% US statutory rate (Q7, Whose tax).

**The series and the base** (Step 0 table; `owner_cash.py`). (a) The last year of the five-year window, 2025, carries a
$45.6M EPA penalty and mitigation payment the filer describes as a settlement, an aberrational year on the filer's own
description, so the central base is the last full cycle, peak to peak 2019 to 2023 (operating income peaks of $108.4M and
$92.4M); the literal window 2021 to 2025 is shown beside. (b) Owner cash changes sign within every window, so no growth
rate is meaningful and the range is the no-growth case alone, said so. (c) Net purchases over the window ($196.8M)
exceed half of owner cash before purchases (which is negative), so the serial-acquirer specific makes the central figure
the organic pair, purchases left out; the default pair with purchases deducted is shown beside. (d) Working capital is
counted inside operating cash. (e) The filing does not allow a maintenance guess: capital spending ran below depreciation
in 2024 and 2025 and the filer gives no split beyond rental fleet, so the all-spending case is central. (f) No growth
is carried, so the cap does not bind.

| case | owner cash a year | value a share at 5.60% | value a share at 10% | cash yield at the price |
|---|---|---|---|---|
| **central: all-equity, 2019 to 2023 cycle, before purchases** | **$23.8M** | **$1.30** | **-$3.88** | **2.04%** |
| equity-only, same base | -$0.9M | -$0.45 | -$0.25 | -0.11% |
| all-equity, literal window 2021 to 2025 | $25.0M | $1.90 | -$3.55 | 2.14% |
| equity-only, literal window | -$1.9M | -$0.96 | -$0.54 | -0.25% |
| all-equity, literal window, EPA payment added back | $34.1M | $6.41 | -$1.02 | 2.92% |
| all-equity, nine years 2017 to 2025 | $30.6M | $4.70 | -$1.98 | 2.62% |
| all-equity, cycle, the 2019 $75.0M receivables repurchase treated as financing | $38.8M | $8.73 | $0.28 | 3.32% |
| all-equity, cycle, purchases deducted (default pair) | -$13.0M | -$16.91 | -$14.08 | -1.11% |

Ceiling check, outside the convention (which allows no growth here): the best base, nine years all-equity with the EPA
payment added back ($35.7M), grown at the 2021 to 2025 sales rate of 6.83% for ten years and then flat, is worth $19.93 a
share at 5.60% and $5.37 at 10%, both below $21.91.

**The floor, tested first.** Earning about 10% at the price needs about $116.8M a year of all-equity owner cash
($79.0M equity-only); the best case on the table yields 3.32%. **No case earns the floor at the price.**

**The two reporting figures (a reporting convention, Part VII; not verdicts).**
- **(a) Value range:** **$1.30 a share** (all-equity, the no-growth case alone, 2019 to 2023 cycle base, purchases left
  out), against **$21.91**. Equity-only beside: -$0.45. Literal window beside: $1.90 all-equity, -$0.96 equity-only.
  The width test does not apply to a single case.
- **(b) Fair price** (the midpoint valued at ten percent; with one case, that case): **-$3.88 a share all-equity**
  (central), **-$0.25 equity-only** beside. Negative: no positive price at which the central case earns the floor. No
  cheap price is reported.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `d7cf1b4d`); written question by question; committed after Q1
      (`905198b2`), after Q2 (`bdb121df`) and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits and states the lock is held by the dispatching session;
      the fold is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the TEX commit subjects and the
      memory index lines seen by accident are declared under contamination and not used. The Terex figures come from
      Terex's own 10-Ks.
- [x] Every v5 id resolves (`check_ids.py`: every id in the CSV, every quoted fragment beside an id in that row, no
      E-ids); every filing fact has its accession; the numbers carry a filing or a CONVENTION.
- [x] The order was kept; Q2's STOP closed the run; the figures after it are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay deducted, all capital spending deducted, acquisitions shown), never a
      net-income proxy; the sovereign from the Treasury curve; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (Foundations) and weighed at Q2; facts for later questions under AFTER THE
      STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its operating cash for 2016 to 2019 was corrected for the
      securitization collections from the filed statements.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded in the commit).
- Shortfalls, stated: Tadano's own report could not be downloaded and Liebherr's was not read, so the competitor row
  rests on one SEC-filing rival; the Americas segment's capital is not disclosed (the filer says its chief decision maker
  does not use segment assets), so the deciding part's return is read from margins and the company-wide return, not
  from segment capital; the old Crane segment figures before 2016 are before the former parent's corporate costs.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2's OUT for ordinary returns asks for "the filer's and the rivals' own filings".** Here only one named rival files
with the SEC and it left the business in 2019; the large rivals (Liebherr, Tadano, the Chinese makers) publish outside
the SEC and one refused the download. I closed OUT on the filer's own two cycles plus the one rival, since the question
is whether this castle protects excellent returns, which the filer's own record answers; the text does not say whether
the rivals' filings are required or only supporting, and a stricter reading would send the name to TOO HARD (WORK) for
want of Tadano's report. (2) **The parts threshold with a losing part.** "More than half of five-year operating profit"
does not say whether a part's share is of the net sum or of the positive parts; with EURAF losing money, the Americas is
71% of the net sum and 57% of the positive parts (279.6 of 487.0), and MEAP is 52.5% of the net sum. Two parts can both
exceed half of a net sum. I took the larger, which is above half on either reading; the text should say which. (3)
**Specific (b) when owner cash changes sign** gives a single-case "range", so the width test and the "ends" of Part
VII's fair price have nothing to work on, and the fair price comes out negative. The text does not say how a negative
fair price is reported; I report the number and say no positive price earns the floor. (4) **Specific (a) and a legal
penalty.** Whether a one-time civil penalty makes a year aberrational is not said; it is a real cost and a one-time one.
I took the filer's description as making 2025 aberrational for the base (peak-to-peak cycle) and showed the literal
window and an added-back case beside; the box does not depend on it. (5) **The serial-acquirer test** compares net
purchases with half of owner cash before purchases; when that owner cash is negative the test is met by any purchase at
all, which is probably not what was meant. (6) **`tools/run.py`** prints operating cash as filed; for issuers with a
receivables securitization before 2020 the filed operating line omits collections classified as investing, so the tool's
longer window misstates owner cash for those years. The tool should flag "cash receipts on sold receivables" as it
flags securities inside operating cash.
