# Company Run — Diebold Nixdorf, Incorporated (NYSE: DBD) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The dispatch's blind rule forbids opening `PORTFOLIO.md`,
any holding review, the resume-state files, the run queue, the prepped reading list and any other run file on this
company, and I opened none of them. I do not know whether the operator holds or wants this name.
**Contamination declared:** the session's recent commit subjects name other 2026-10-05 runs and their boxes (HUBB, ATKR,
ETN, electrical trades); none concerns this company or its industry, and I did not open those files. `tools/run.py`
printed v4 material besides its arithmetic; only the arithmetic lines were read (Part VII). I have general background
knowledge of the company's history (the 2016 Wincor Nixdorf combination, the 2023 Chapter 11); every fact used below is
taken from a filing and carries its accession.

Working folder: `Test Runs/_research 2026-10-05 DBD/` (filing texts, the fetch scripts, the arithmetic).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $65.19 (2026-10-05, from `tools/run.py`; **aggregator quote, flagged** per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **33,946,588** shares (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-29, accession `0000028823-26-000033`; `python Screens/cover_shares.py DBD`).
  The 10-K cover gave 35,173,038 at 2026-01-30 (accession `0000028823-26-000008`); the fall is the buyback (Q6).
  No second class; no warrants outstanding after emergence (the predecessor's equity warrants were eliminated, 10-K FY2025
  statement of changes in equity).
- **Market cap:** $65.19 x 33.947M = **$2,213M**. Net debt at 2025-12-31: $950.0M notes less $416.4M cash and short-term
  investments = $533.6M; enterprise value about **$2,747M** (pensions and leases not added; see Q9).
- **Sovereign for the earnings currency:** the company reports in US dollars, and its debt and buyback are in dollars, so
  the earnings currency is taken as USD, **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (`python tools/sources.py`). About 76% of revenue is earned outside the US (10-K FY2025, risk factors), much of it in
  euros (EUR 30-year 3.72%, ECB, same date); the dollar rate is the higher and so the conservative one for the value.
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-12, accession `0000028823-26-000008` (business, MD&A,
  risk factors, the statements of financial position, earnings, cash flows and changes in equity, and notes 2, 8, 10,
  11, 13 and 18, the others by heading only); 10-Q Q2 2026, filed 2026-07-29, accession
  `0000028823-26-000033`; proxy DEF 14A filed 2026-04-02, accession `0001193125-26-140284`; 10-K FY2024 (`0000028823-25-000022`),
  10-K FY2023 (`0000028823-24-000025`, fresh-start accounting), 10-K FY2022 (`0000028823-23-000078`, the year before the
  filing); further filings named where used. **One figure cross-checked against the filed statement:** net cash provided
  by operating activities FY2025 **$300.7M**, statement of cash flows, 10-K FY2025 p. 27, agrees with the MD&A summary
  ($300.7M) and with the XBRL fact for the same tag.
- `python tools/run.py DBD` arithmetic: its owner-earnings table drew **2008 to 2010** XBRL values (OCF 282, 297, 273)
  because the post-emergence filings changed tags; the table is stale and is **not used**. Its balance-sheet ten-year
  table (2018 to 2025, accessions listed in the research folder) is used in the balance-sheet reading, read against the
  filed statements. Owner cash is computed below from the filed cash-flow statements (`arithmetic.py` and
  `arithmetic_out.txt` in the research folder).

## THE FOUNDATIONS (not a gate)
Three bear on this name. **A share is a business:** the question is whether I would be content to own Diebold Nixdorf
"if the market closed for five years" **[M1997-109]**. The stock has risen about 230% since its first trading day after
emergence (proxy DEF 14A 2026, `0001193125-26-140284`, pay-versus-performance section: $100.00 to $330.04 from
2023-08-14 to 2025-12-31), and the rows say a rise "is never a reason to buy it" **[L2013-007]**. **Who is paid to tell
you:** the company's framing is a model that "generates sustainable free cash flow with a stable, predictable financial
profile" (proxy, opening letter) and an adjusted EBITDA of about $485M (proxy, CD&A); management's long-term pay rides
on adjusted EBITDA (recorded below), so the framing is read as the seller's own projection: "don’t ask the barber
whether you need a haircut" **[M2011-083]**. **The analyst's habits:** look for "what’s wrong in things" and "what
you’re missing" **[M2025-013]**, and write contrary evidence down at once **[M1997-127]**.

**Contrary evidence, written down as found [M1997-127]:**
1. FY2025 operating cash $300.7M; owner cash after capital spending, capitalized software and stock pay $226.9M, about
   10% of today's market value; two straight years of improvement; S&P raised the issuer rating to B+ (2025-09-18) and
   Moody's to B1 (2025-12-16) (10-K FY2025, liquidity section).
2. Services are "over 56%" of revenue and carry no backlog figure because they recur (10-K FY2025, product backlog
   paragraph). "Nearly two-thirds of the world’s top 100 financial institutions" use the company's solutions; in retail,
   "21 of the top 25 European retailers" (10-K FY2025, business).
3. In the West the self-service banking field has two makers of size, this company and NCR Atleos, each naming the other
   (NCR Atleos 10-K FY2025, competition, `0001628280-26-012576`): the shape of an oligopoly.
4. Debt cut from $2,585.8M (long-term debt and capital leases, 2022-12-31, XBRL as filed in 10-K FY2022
   `0000028823-23-000078`) to $970.7M (2025-12-31, 10-K FY2025 note 11); interest expense $155.3M (2024) to $85.7M (2025).
5. In FY2025 the tangible capital the business uses looks small against its operating profit: receivables $609.4M plus
   inventories $521.0M less payables $431.1M and deferred revenue $325.8M is $373.5M of working capital, plus net PP&E
   $286.0M, against operating profit $242.0M (10-K FY2025, balance sheet and income statement). The rows measure a
   business by "the capital actually needed in the business" **[M2010-090]**. Recorded as found; weighed at Q2 against
   the ten years before it.

## THE STANDING RULE
The rule binds the buyer's conduct, not the target's **[M2012-081]**, **[L2023-005]**. A purchase of this common stock
for cash, with no borrowed money **[L2014-005]**, sized so that its total loss could be borne, would not put the buyer at
risk of ruin. The target's own debt belongs to Q9. Nothing in this run is a purchase.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the rows put it:** "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years", with "some notion of how the industry will develop and where the company will stand within
  the industry" **[M2012-065]**; the key variables named and "how predictable they were" **[M1998-044]**.
- **What the business is** (10-K FY2025, `0000028823-26-000008`, business, MD&A, note 18). Banking, 73.5% of FY2025 net
  sales ($2,797.0M of $3,805.7M): ATMs, cash recyclers and teller automation, their installation, maintenance and managed
  services, and the Vynamic software. Retail, 26.5% ($1,008.7M): point-of-sale, self-checkout and kiosks with service and
  software, mostly for European grocers and fuel retailers. Services $2,168.9M, products $1,636.8M. About 76% of revenue
  is earned outside the US. About 20,000 employees; plants in North Canton (Ohio), Paderborn (Germany) and Manaus
  (Brazil); some products made in China and India, one line through a joint venture whose partner's Chinese parent is on
  the US Entity List (risk factors).
- **The key variables, and how foreseeable each is:**
  1. Bank demand for machines: replacement cycles, branch automation, cash recyclers. Replacement-driven and cyclical
     with bank capital budgets (risk factors: the cyclical risk "is magnified for capital goods purchases such as ATMs").
     Foreseeable in direction.
  2. Cash use. The company's own risk factor: "Consumer transition towards non-cash payment alternatives has accelerated
     in recent years", which could bring "a decline in the usage of ATMs". The direction in mature markets is down; the
     pace, country by country, I cannot write down. This is slow change, which the rows warn "can be much harder to
     perceive, and can lull you to sleep easier" **[M2014-038]**. Recorded as contrary.
  3. The price of service contracts, which carry the earnings. Contested by design: the company offers "multi-vendor
     service capability in North America" (10-K FY2025, banking value drivers), its rival services "our own units or
     third-party units" (NCR Atleos 10-K FY2025, global services network), and the company "perceives competition to be
     fragmented, especially in the product-related services segment", including "local and regional third-party
     providers" (10-K FY2025, competition). Foreseeable in kind.
  4. Retail checkout hardware and software (self-checkout, the AI loss-prevention product). The faster-moving half, and
     the rows warn that "it’s easy to sort of think you understand retail, and then subsequently find out you don’t"
     **[M2014-052]**.
- **The routing.** This is not a fast-changing industry in the sense of the routing rule **[M1998-008]**: ATMs and
  checkouts are replaced on long cycles and the industry's change runs over decades. I can give a fix on the economics in
  kind: a mature, slowly shrinking developed-market hardware base with a recurring but contested service tail, some
  emerging-market growth, and two Western incumbents facing Asian makers. That is a fix on the economics, not on the
  product **[M2000-104]**, and it is the fix Q2 tests. What I cannot fix is the pace of the cash decline and the retail
  software outcome; and "if you have doubts about something being into your circle of competence, it isn’t"
  **[M2002-092]**. I weigh it this way: the doubt is about how fast a mediocre economics erodes, not about what kind of
  economics it is, and the decision does not turn on the retail forecast (Banking is 80% of segment operating profit,
  $506.6M of $631.5M, 10-K FY2025 note 18). A stricter reader would close here, TOO HARD on the retail half and the pace
  of cash decline; the box would still hold no purchase (see the last section).
- **VERDICT: IN, narrowly**, on **[M2012-065]**, **[M2000-104]**, **[M1998-044]**, with the doubt of **[M2002-092]** and
  **[M2014-038]** recorded, not dismissed. Passes to Q2, where the competitive position is tested on the record.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**. A moat is what "protects excellent returns on invested capital", and it is
the castle "earning high returns" that competitors assault **[L2007-004]**. For this company the first fact is that the
castle did not stand: the equity was cancelled in 2023. Each test below carries its filing fact.

- **The record: did anything protect excellent returns?** No. GAAP operating margin (operating income over revenue, XBRL
  `OperatingIncomeLoss` and the revenue tags as filed in each 10-K; FY2023 adds the predecessor and successor periods,
  10-K FY2025): 2016 -5.1%, 2017 -2.0%, 2018 -7.1%, 2019 -0.6%, 2020 0.6%, 2021 3.5%, 2022 -6.1%, 2023 2.3%, 2024 4.9%,
  2025 6.4%; the ten-year mean is about **-0.3%**. Before the 2016 Wincor Nixdorf combination the stand-alone company
  earned -0.1%, 5.2%, 3.4%, -5.4%, 6.0% and 2.4% in 2010 to 2015 (XBRL as filed, last in 10-K FY2015
  `0000028823-16-000157`). Sixteen years, and the best is the latest, 6.4%. Shareholders' equity went from $961.2M (2010)
  to -$1,380.9M (2022) (XBRL `StockholdersEquity`). The FY2022 10-K (`0000028823-23-000078`, risk factors) carried
  "substantial doubt as to the Company’s ability to continue as a going concern"; on 2023-08-11 each old equity interest
  was "extinguished, cancelled and discharged without any distribution" and first-lien lenders took 98% of the new stock
  (10-K FY2023, `0000028823-24-000025`, note 2). There were never excellent returns to protect.
- **Pricing power, and the agony before a rise** **[M2005-020]**. When costs rose in 2022 the company could not pass them
  on: "Product gross margin decreased 960 basis points ... While the Company is focused on obtaining price increases to
  offset the inflationary costs, long lead times between order entry and revenue recognition do not allow for pricing
  actions to take immediate effect" (10-K FY2022, MD&A). The same year it ran an "initiative to reduce low margin
  services contracts" (ibid.), and the FY2025 10-K still names "a focus on improving pricing discipline" as a growth
  priority (business). FY2025 service gross margin fell 80 basis points to 24.0% on "operational cost pressures"
  (MD&A). The test reads the strength of a business by its price behaviour; this behaviour is the weak case.
- **The low-cost position** **[L2000-017]**, **[M1997-010]**. Not shown. The company's own words: "All phases of the
  Company's business are highly competitive ... The Company encounters competition in price"; "Local providers ... may
  have a substantial advantage"; competitors "could cause a reduction in the prices for some of its services and
  products as a result of intensified price competition" (10-K FY2025, risk factors). Its named banking rivals include
  Hyosung TNS, GRG Banking, Hitachi, OKI and Glory (10-K FY2025, competition). Its largest Western rival makes its
  machines mainly in Chennai, India (NCR Atleos 10-K FY2025, manufacturing); this company runs plants in Ohio, Germany
  and Brazil. Twenty thousand people servicing machines in more than 100 countries, selling a machine rivals ship in from
  abroad, is the case the rows name: "a business that has a very high labor content and that has a product that can be
  shipped in from abroad very easily" **[M2007-116]**. In such a field "the guy with the lower cost comes in and kills
  you" **[M2001-013]**, and "a company must lower its costs to competitive levels or face extinction" **[L1994-035]**;
  this one reached the edge in 2023.
- **The competitor's own words.** NCR Atleos writes of the industry: "This industry is characterized by rapidly changing
  technology, disruptive technological innovation, evolving industry standards, frequent new product introductions,
  price and cost reductions, and increasingly greater commoditization of products making differentiation difficult"
  (NCR Atleos 10-K FY2025, risk factors). Two firms are no cure: "you can have only two competitors and they’re still
  terrible businesses, they beat each other’s brains out" **[M2013-052]**.
- **Would the customer still choose it over the low bid?** **[M2017-009]**, **[L2004-003]**. The service book, the part
  that ought to hold the customer, is open to rivals by design (multi-vendor service, Q1 variable 3); the company had to
  shed low-margin service contracts in 2022. No filing fact shows a customer paying more to stay. The failing answer is a
  product "that has a whole bunch of competitors" **[M2023-074]**.
- **Unit volume** **[M1999-054]**. Revenue fell from $4,609.3M (2017) to $3,805.7M (2025) (XBRL as filed; part of the fall
  is divestitures and currency). Product backlog fell from about $1,400M (2022-12-31, 10-K FY2022) to $790.1M (2024) and
  $733.1M (2025) (10-K FY2025). The company names the volume threat it cannot control: fewer ATMs as cash use falls.
- **The money test** **[M2011-015]**. The combined company had operating losses in five of the seven years after the 2016
  combination while it promised "approximately $160 of cost synergies over three years" (10-K FY2016,
  `0000028823-17-000052`) and then "net operating profit savings of approximately $240 by the year 2020" (10-K FY2017,
  `0000028823-18-000066`). Savings that never reached the owners are the mark the rows describe: "the improvement you get
  one day, your competitor gets the next day" **[M2004-053]**. And "one competitor is frequently enough to ruin a
  business" **[M2012-108]**; this company names seven.
- **Widening or narrowing?** **[M1999-108]**, **[M2000-075]**. Since emergence the margin has risen (4.9% to 6.4%) on lower
  interest, cost programmes and product mix: the contrary evidence above, two years long. The castle question is why
  competitors will not take the gain back, and no filing fact answers it. The company began another restructuring, the
  Operational Evolution Program, expected to cost $80M, in Q4 2025 (10-K FY2025 note 10); FY2025 is the sixteenth year in
  a row with restructuring charges (XBRL `RestructuringCharges`, 2010 to 2025, about $850M in total). "A moat that must
  be continuously rebuilt will eventually be no moat at all" **[L2007-005]**.
- **What could destroy, modify or reduce it** **[M2000-014]**: the fall of cash use in mature markets, price competition
  from Asian makers, and consolidation among bank customers. All three are in the company's own risk factors.

**The competitor row** (same metric, GAAP operating income over revenue, from each filer's own 10-K):

| Company | 2024 | 2025 | Other | Source |
|---|---|---|---|---|
| Diebold Nixdorf | 4.9% ($182.1M / $3,751.1M) | 6.4% ($242.0M / $3,805.7M) | ten-year mean 2016-2025 about -0.3%; owner cash FY2025 $226.9M, 6.0% of revenue | 10-K FY2025 `0000028823-26-000008` |
| NCR Atleos (ATMs, services, the Allpoint network) | 10.2% ($437M / $4,305M) | 11.0% ($478M / $4,354M) | Self-Service Banking segment adjusted EBITDA 26.1% of segment revenue (the filer's only segment profit figure; an EBITDA figure, shown for scale only); OCF $356M less capex $117M less stock pay $34M = $205M, 4.7% of revenue | 10-K FY2025 `0001628280-26-012576` |
| NCR Voyix (retail and restaurant POS) | -1.3% (-$38M / $2,818M) | 1.0% ($26M / $2,687M) | operating cash flow -$210M in 2025 | 10-K FY2025 `0000070866-26-000006` |
| NCR, before the 2023 split (ATM and POS together) | | | 2014 to 2019: 5.4%, 2.1%, 10.3%, 10.6%, 3.0%, 8.8% | XBRL as filed, last in 10-K FY2019 `0000070866-20-000007` |
| Hyosung TNS, GRG Banking, Toshiba (retail) | not obtained | not obtained | non-SEC filers; no filing read; **flagged** | none |

Reading of the row: this company earns about half the margin of its nearest Western rival, and that rival reaches 10% to
11% only with the Allpoint network (29% of its revenue) inside it. In retail the rival earns about nothing. The row shows
a field in which the stronger of two incumbents earns a modest margin and calls its own products increasingly
commoditized.

- **The close.** A castle shown open on the evidence closes OUT **[M2011-015]**. The framework's list of what Q2 rules out
  names the high-cost producer in a commodity field (**[L1994-035]**, **[M1997-010]**, **[M2001-013]**) and the business
  whose returns rivals can copy (**[M1996-017]**). The two good years since emergence do not reopen it, and a low price
  would not: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "marginal
  businesses purchased at cheap prices may be attractive as short-term investments, they are the wrong foundation on
  which to build a large and enduring enterprise" **[L2014-009]**.
- **Why OUT and not TOO HARD.** TOO HARD is for a castle whose future cannot be judged **[M2000-019]**. This castle's past
  is on the record and judges it: sixteen years of filings, a going-concern warning, a bankruptcy, a failed price
  pass-through and the rival's own word "commoditization". The question is knowable and was answered.
- **VERDICT: OUT**, on **[M1995-038]**, **[L2007-004]**, **[M2005-020]**, **[M2007-116]**, **[M2001-013]**,
  **[L1994-035]**, **[M2013-052]**, **[M2004-053]**, **[M2011-015]**, **[L2007-005]**. The run closes here. Q3 to Q10
  are NOT REACHED; nothing below is a clearance.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (closed at Q2). The balance-sheet reading the dispatch asked for is
in the computation section below and is not a verdict.
## Q5 — WHO RUNS IT. NOT REACHED (closed at Q2).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (closed at Q2).
## Q7 — WHAT IS IT WORTH. NOT REACHED (closed at Q2). The arithmetic below is computation only.
## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED (closed at Q2).
## Q9 — COULD IT RUIN US. NOT REACHED (closed at Q2). Debt facts are recorded below.
## Q10 — THE FAT PITCH. NOT REACHED (closed at Q2). What the framework would have the buyer do: nothing. "If you really
think a business is declining, most of the time you should avoid it" **[M2012-062]**.
## Q12 (optional) — NOT ASKED. None of the businesses Q12 names is involved.

---
## THE BOX
**OUT, at Q2**: the castle shown open on the evidence (sixteen years of thin or negative operating margins, the 2022
failure to pass costs through, the equity cancelled in the 2023 Chapter 11, a rival that calls the products increasingly
commoditized). Q1 passed narrowly. Q7 was not reached; the figures below are computation, not a range of record.

---
## COMPUTATION — NOT A CLEARANCE
*Written at the owner's request after the closing STOP. Nothing here carries entry language (operator rule 3). The
headings follow the questions they would have fed.*

### The balance sheets, read before the income account (the Q4 reading, as computation)
The rows ask for "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.
Figures in USD millions at December 31; equity and debt from XBRL as filed (`StockholdersEquity`,
`LongTermDebtAndCapitalLeaseObligations`); the other lines from `tools/run.py`'s ten-year table (first-filed XBRL vintage,
accessions `0000028823-19-000069` to `0000028823-26-000008`), checked against the FY2025 and FY2022 filed statements;
sales from the filed income statements.

| Year-end | Equity | Goodwill + intangibles | Long-term debt incl. leases | Cash (run.py tag, excl. restricted; filed 2025 incl. restricted $387.3M) | Receivables / sales | Inventory / sales |
|---|---|---|---|---|---|---|
| 2015 (pre-combination) | 412.4 | 229.0 | 606.2 | | | |
| 2016 | 591.4 | 1,771.2 | 1,691.4 | | | |
| 2017 | 445.5 | 1,819.5 | 1,787.1 | | | |
| 2018 | -149.7 | 1,422.8 | 2,190.0 | | 16.1% | 13.3% |
| 2019 | -530.3 | 1,266.3 | 2,108.7 | | 14.0% | 10.6% |
| 2020 | -827.1 | 1,249.0 | 2,335.7 | | 16.6% | 12.8% |
| 2021 | -845.1 | 1,091.1 | 2,245.6 | | 15.2% | 13.9% |
| 2022 | -1,380.9 | 959.9 | 2,585.8 | 307 | 17.7% | 17.0% |
| 2023 (fresh start) | 1,063.8 | 1,503.6 | 1,252.4 | 550 | 19.2% | 15.7% |
| 2024 | 929.8 | 1,365.0 | 965.8 | 296 | 15.7% | 14.1% |
| 2025 | 1,099.9 | 1,434.8 | 970.7 | 369 | 16.0% | 13.7% |

*(2023 ratios use combined predecessor and successor sales of $3,760.5M.)* What the figures say: from 2016 the company
carried purchased goodwill and intangibles of $1.8B against equity of $0.6B, then lost the equity entirely by 2018 and
kept losing it through 2022, while debt rose from $0.6B to $2.6B; retained earnings reached -$1,406.7M before the
reorganization (10-K FY2025, statement of changes in equity, predecessor column). Receivables and inventory held at 14%
to 17% of sales apart from the 2022 inventory build (supply chain); no sign there of receivables or inventory running
away from sales. What they do not say: the post-2023 equity is not earned capital. Fresh-start accounting wrote the
balance sheet to a negotiated enterprise value of $2,150.0M, the bottom of the disclosure statement's range of $2,150.0M
to $2,450.0M (10-K FY2023 note 3), and allocated $1.5B of it to goodwill and intangibles; tangible equity at 2025-12-31 is
about **-$335M** ($1,099.9M less $642.4M less $792.4M). What they cannot say: whether the fresh-start intangibles
($792.4M net, of which customer relationships $505.2M over 15.2 years; total amortization expense $94.4M in 2025 and
$103.7M in 2024, 10-K FY2025 note 8) will keep their value. **How the 2023 break was handled:** cash flows are added across
the break (predecessor plus successor periods), since cash is cash; balance-sheet ratios to sales are compared across it,
since receivables and inventory were not much revalued; equity, goodwill, intangibles and depreciation are not compared
across it; owner cash deducts capital spending, not depreciation, so the fresh-start amortization does not enter it.

**The real costs** (the Q4 reading, as computation). Restructuring every year 2010 to 2025, about $850M in all, and a new
$80M programme in Q4 2025: a recurring cost, not a one-time one **[L2016-007]**. Stock pay $12.1M (2025), deducted below
**[L2015-003]**. Pensions: the US plan is underfunded by $74.2M and the non-US plans are overfunded by $69.0M (10-K
FY2025 note 13); small against the business, and real **[M2005-057]**. Adjusted EBITDA of about $485M is the figure the
company features and pays on (proxy: long-term performance cash 75% on cumulative adjusted EBITDA); the rows call the
figure "utter nonsense" **[M1998-086]** and put the count of purchases among people talking it at "about zero"
**[M2002-026]**. GAAP operating profit was $242.0M and owner cash $226.9M in the same year.

### Owner cash after every real cost (the Q7 input, as computation)
Operating cash less capital expenditures, less capitalized software, less stock pay, from the filed cash-flow statements
(USD millions; 2016 and 2017 software is the filed line "increase in certain other assets"; 2018 and 2019 software from
XBRL `PaymentsToDevelopSoftware`; sources per year in `arithmetic.py`):

| Year | OCF | Capex | Software | Stock pay | Owner cash |
|---|---|---|---|---|---|
| 2016 | 28.7 | 39.5 | 28.2 | 22.2 | -61.2 |
| 2017 | 37.1 | 69.4 | 41.1 | 33.9 | -107.3 |
| 2018 | -104.1 | 58.5 | 29.8 | 36.6 | -229.0 |
| 2019 | 135.8 | 42.9 | 23.1 | 24.0 | 45.8 |
| 2020 | 18.0 | 27.5 | 17.2 | 14.9 | -41.6 |
| 2021 | 123.3 | 20.2 | 31.1 | 13.8 | 58.2 |
| 2022 | -387.9 | 24.4 | 28.7 | 13.4 | -454.4 |
| 2023 | -257.0 | 24.9 | 22.9 | 5.2 | -310.0 |
| 2024 | 149.2 | 17.4 | 23.0 | 9.7 | 99.1 |
| 2025 | 300.7 | 37.4 | 24.3 | 12.1 | 226.9 |

Five-year mean 2021-2025: **-$76.0M**. Ten-year sum 2016-2025: **-$773M**. The 2025 figure includes $65.8M and the 2024
figure $62.1M of working-capital inflow (the filed changes in receivables, inventories, tax, payables, deferred revenue,
salaries, restructuring accrual and other); the beginning and terminal years of any trend here are aberrational
**[L2005-003]**. H1 2026: operating cash $18.1M, capital expenditures $13.4M, capitalized software $12.9M (10-Q Q2 2026,
`0000028823-26-000033`); owner cash for the half is negative before stock pay (the business is seasonal toward Q4).

### Value range, fair-price band and cheap price (the Q7 arithmetic, as computation)
- **Under the framework's CONVENTION** (five-year mean of owner cash, carried at the growth shown, capped by Q3, ten years
  then no growth, at the sovereign): the five-year mean is negative (-$76.0M), so the no-growth end of the range is
  negative and no range can be built. Had Q7 been reached, the convention could not estimate the cash stream, which the
  framework's section I sends to TOO HARD at Q7; the rows behind it speak of a range "so wide that no useful conclusion
  can be reached" **[L2000-025]**, and refuse to cure it with a bigger discount **[M2007-022]**.
- **A variant, not the convention, shown only because the owner asked for figures:** post-emergence years only (2024 and
  2025), owner cash before cash interest and without the working-capital inflow ($186.4M and $220.2M, mean $203.3M), less
  interest on the $950.0M notes at 7.75% ($73.6M), plus 2025 interest income ($8.9M): **$138.6M a year, $4.08 a share** on
  33,946,588 shares. Growth shown: revenue 2021-2025 compounded at **-0.64%** a year ($3,905.2M to $3,805.7M); owner-cash
  growth cannot be measured across a negative base. Discounted at 5.63%:
  - shown-growth end (-0.64% for ten years, then zero): **$69.15 a share**;
  - no-growth end: **$72.51 a share**.
  - **Variant range $69 to $73 against $65.19.** The range is narrow because it rests on two years; it does not carry the
    sixteen years before them.
- **Pre-tax and after-tax.** Owner cash is after the company's taxes and before the buyer's. The floor (CONVENTION: about
  ten percent pre-tax) is applied to it directly, as the 1994 statement of the figure applies "at least a 10 percent
  rate" to "after-tax streams of cash" **[M1994-004]**: expected return = owner-cash yield at the price plus growth. No
  further conversion is made. (Had the floor been converted as an after-tax 7.9%, at the 21% US federal rate, the floor
  prices below would be $47.78 to $51.67.)
- **Expected return at $65.19:** 6.26% with no growth; 5.62% at the shown growth. Below the floor of about ten percent
  **[M2003-149]**.
- **Fair-price band** (prices inside the range at which the expected return is at or above the floor): **none**. The floor
  is met only at or below **$38.35** (shown growth) to **$40.82** (no growth), well under the bottom of the variant range.
- **Cheap price** (below which the case would need no pencil **[M1996-084]**, **[M2009-005]**): **about $35**, CONVENTION,
  ours: half the bottom of the variant range ($69.15 / 2 = $34.46), the "big discount from that present value" of
  **[M1997-126]** set at one half because the business's own record is so unstable. It is a figure for the operator's
  alert file only. Q2 closed the file OUT, and a price does not reopen Q2 **[M2019-015]**.

### Facts recorded for a later run (Q5, Q6, Q9), not judged
- **Management.** Octavio Marquez, CEO since March 2022 (SVP Americas 2016 to 2020, then head of global banking; at the
  company since 2014), led it through the 2023 Chapter 11. 2025 total pay $8,694,401: salary $850,000, stock awards
  $3,075,002, non-equity incentive $4,740,267 (proxy, summary compensation table). Annual incentive: non-GAAP operating
  profit 40%, levered free cash flow 40%, constant-currency revenue 20%; long-term performance cash: cumulative adjusted
  EBITDA 75%, cumulative revenue 25%; 2024 performance options vest at stock-price hurdles up to $95 a share (proxy, CD&A).
- **Owners.** Funds associated with Capital World Investors about 32.4% and Millstreet Capital Management about 14.5% of
  the stock (10-K FY2025, risk factors).
- **Buybacks, no price named.** The programme's timing, price and size "will depend on prevailing stock prices" (10-K
  FY2025). Prices paid: 2025, 2,307,275 shares for $128.0M (about $55.48); Q1 2026, 746,610 shares for $55.0M (about
  $73.67); Q2 2026, 751,648 shares for $60.0M (about $79.82) (10-K FY2025; 10-Q Q2 2026). The 2026 purchases sit above the
  top of the variant range ($72.51); H1 2026 buybacks of $121.0M against H1 owner cash below zero.
- **Debt.** $950.0M 7.75% senior secured notes due 2030-03-31, secured on substantially all assets; $310.0M revolver due
  2029-12-18, undrawn, $285.7M available; cash and short-term investments $416.4M (2025-12-31); covenants limit debt,
  dividends and buybacks (10-K FY2025 note 11 and liquidity section). Operating lease obligations $165.5M.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed after each**: the dispatch
  forbids commits, so the write-early discipline was kept in the file only.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script; see below); every filing fact has its
  accession or names the filing whose accession is given in Step 0; no number without a row, a filing or a CONVENTION
  label.
- [x] The order was kept; Q2 closed the run; everything after it is marked NOT REACHED or COMPUTATION.
- [x] Owner cash after every real cost (capital spending, capitalized software, stock pay), never a net-income proxy; the
  sovereign from the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found (five items in the foundations; the cash-decline doubt at Q1; the
  post-emergence improvement at Q2).
- [x] Not a point-in-time run; no anchor rule applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings table was stale (2008 to 2010 tags) and
  was replaced by hand from the filed statements.
- [x] `python tools/check_framework.py` PASS (run 2026-10-05 after the file was complete); no commit
  was made, by instruction.
- Honest limits: Hyosung TNS, GRG Banking and Toshiba were not read (non-SEC); NCR Atleos's segment figure is an EBITDA
  figure; the 2016 to 2019 software lines are approximations from the filed "certain other assets" line and XBRL; the
  2023 bankruptcy plan documents themselves (disclosure statement) were read only through the 10-K FY2023 notes.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Q1's doubt rule against a slow-change business.** The routing sends fast change to Q1 TOO HARD, and
**[M2002-092]** says a doubt means outside; but the rows also say slow change is the harder to perceive **[M2014-038]**.
For a business whose change is slow but certain in direction (cash use falling), the framework does not say whether a
doubt about the pace, rather than the kind, of the economics is the doubt **[M2002-092]** means. I passed Q1 narrowly
and let Q2 decide on the record; a reader who closed at Q1 would reach the same no-purchase by a different box (TOO HARD,
and then the question of WORK or NATURE, which for the pace of cash decline is probably NATURE). The framework should say
which. (2) **Fresh-start accounting and the Q7 convention.** The convention's five-year mean of owner cash spans the
bankruptcy and is negative, so the range cannot be built; the convention does not say whether the years before a
reorganization count (they are the same business, so I counted them) or how to treat a base that is negative. I
reported the convention's failure and a labelled two-year variant; the framework should say whether a negative
five-year mean is TOO HARD at Q7 by itself. (3) **Pre-tax against after-tax for the floor.** The dispatch asked how I
converted. The CONVENTION says "about ten percent pre-tax", while the 1994 row that first states the figure applies it
to "after-tax streams of cash" **[M1994-004]**. Owner cash is after the company's tax and before the buyer's, so I
applied ten percent to it directly and showed the alternative; the convention should say which tax "pre-tax" is before.

