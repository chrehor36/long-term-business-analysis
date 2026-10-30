# Company Run — Ryerson Holding Corporation (NYSE: RYZ, formerly RYI) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`,
so the analyst does not know whether the operator holds RYZ. Working folder: `Test Runs/_research 2026-10-05 RYZ/`.

**CONTAMINATION, declared.** (1) The session context showed the subjects of recent commits, which name other runs' boxes
(GENC and AROC OUT at Q2, MTRN TOO HARD at Q1, MBUU OUT); none concerns Ryerson or a metals distributor, and none was
opened. (2) The analyst carries general prior knowledge of Ryerson, Reliance and the service-center trade from training;
every fact below is taken from a filing read in this run, and where the filing did not supply a fact it is marked so.
(3) No other `Test Runs/` file on Ryerson or Olympic Steel, no holding review, no RESUME STATE, no queue file and no reading
list was opened. (4) `tools/run.py` printed no v4 ids or rules this time; only its arithmetic lines were used.

**The company changed this year.** Ryerson merged with Olympic Steel (ZEUS) on 2026-02-13 in an all-stock deal, 1.7105
Ryerson shares per Olympic share, about 19.5 million new shares; the ticker moved from RYI to RYZ on 2026-02-24 (8-K
2026-02-13, accession 0001193125-26-051335). Everything per share below is on the post-merger count. The IPO was
**August 2014** at $11.00 (424B4, accession 0001193125-14-303162), not 2010: the 2010 to 2013 S-1 filings never priced.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $27.15 (2026-10-05, aggregator quote via `tools/run.py`; aggregator flagged per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: 51,898,653 common, one class, as of 2026-07-24 (10-Q for the quarter
  to 2026-06-30, filed 2026-07-29, accession `0001193125-26-323769`; `python Screens/cover_shares.py RYZ` agrees). This is
  the post-merger count: 60,233,293 issued less 8,342,140 in treasury at 2026-06-30 (same 10-Q). Pre-merger diluted shares
  were 32.1 million for 2025 (10-K FY2025).
- **Market cap:** $1,409M. **Net debt** at 2026-06-30: $913M (total debt $955.2M, all under the asset-based Ryerson Credit
  Facility, less cash $41.9M; same 10-Q). Operating lease liabilities a further $373.6M (current $41.7M, noncurrent $331.9M).
- **Sovereign for the earnings currency:** USD 30-year par yield 5.63%, US Treasury daily par yield curve, 2026-10-02 (the
  issuing authority, as printed by `tools/run.py` from `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-23, accession 0001193125-26-062397): business, risk factors,
  MD&A, liquidity, pension, debt; 10-Q Q2 2026 (0001193125-26-323769) and Q1 2026 (0001193125-26-209016); proxy DEF 14A
  2026-03-18 (0001193125-26-114120): ownership, pay; 8-K merger close (0001193125-26-051335); 8-K auditor change
  2024-12-03 (0000950170-24-134222: EY dismissed after a proposal process, no disagreements, KPMG appointed for FY2025).
  For the long span, the selected-data tables and MD&A of the 10-Ks for FY2010 (0001193125-11-067235), FY2011
  (0001193125-12-107289), FY2014 (0001193125-15-094069), FY2016 (0001564590-17-004120), FY2018 (0001564590-19-006287), FY2020
  (0001564590-21-008111), FY2022 (0000950170-23-003768) and FY2024 (0000950170-25-024199); the 2014 IPO prospectus.
  The merger prospectus (424B3, 0001193125-26-012942) was downloaded and searched only for deal terms, not read.
- **One figure cross-checked against the filed statement:** operating cash flow 2025 $87.0M (XBRL, and the 10-K FY2025 MD&A
  cash-flow table: "Net cash provided by operating activities 87.0"); total assets 2025-12-31 $2,405M in the `tools/run.py`
  table against $2,404.7M in the comparative column of the Q2 2026 10-Q balance sheet.
- `tools/run.py` arithmetic lines (Ryerson alone, pre-merger shares in its OE but the post-merger cover count in its cap,
  so its yield lines are **not usable**: they set three years of Ryerson-only cash against the combined company's market
  value). Checked against the filings: OCF 2023-2025 $365.1M, $204.9M, $87.0M; capex $121.9M, $99.6M, $51.5M; D&A $62.5M,
  $77.6M, $79.7M; stock pay $13.8M, $11.6M, $8.7M (cash-flow statement line; it covers all equity awards, directors'
  grants included; the separate director figure was not extracted). Current debt is trivial (short-term foreign debt
  $2.6M); the facility matures 2031-02-13.

### The long record, from the filings (Ryerson alone, $M; tons in thousands)
Sources: selected-data tables of the 10-Ks named above for 2006-2018; XBRL and 10-K MD&A for 2019-2025. 2007 joins the
predecessor (to 2007-10-19) and successor periods of the Platinum buyout. LIFO: + is expense, - is income, from each
year's MD&A sentence.

| Year | Sales | Gross profit | Op. profit | Tons | GP/ton $ | Op/ton $ | Op margin | LIFO | OCF | Capex | D&A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2006 | 5,909 | 858 | 184 | 3,292 | 261 | 56 | 3.1% | n/a | -261 | 36 | 40 |
| 2007 | 6,002 | 866 | 171 | 3,033 | 285 | 57 | 2.9% | 69.5 liq. gain | 618 | 61 | 40 |
| 2008 | 5,310 | 713 | 127 | 2,505 | 285 | 51 | 2.4% | +91 | 281 | 30 | 38 |
| 2009 | 3,066 | 456 | -42 | 1,881 | 242 | -22 | -1.4% | -174 | 285 | 23 | 37 |
| 2010 | 3,896 | 540 | 20 | 2,252 | 240 | 9 | 0.5% | +52 | -199 | 27 | 38 |
| 2011 | 4,730 | 659 | 99 | 2,433 | 271 | 41 | 2.1% | +49 | 55 | 47 | 43 |
| 2012 | 4,025 | 710 | 200 | 2,149 | 330 | 93 | 5.0% | -63 | 187 | 41 | 47 |
| 2013 | 3,460 | 617 | 125 | 2,038 | 303 | 61 | 3.6% | -33 | 48 | 20 | 47 |
| 2014 | 3,622 | 594 | 83 | 2,024 | 293 | 41 | 2.3% | +42 | -73 | 22 | 46 |
| 2015 | 3,167 | 568 | 108 | 1,897 | 299 | 57 | 3.4% | -97 (and a $38M lower-of-cost charge) | 259 | 22 | 44 |
| 2016 | 2,860 | 571 | 122 | 1,903 | 300 | 64 | 4.3% | +7 | 25 | 23 | 43 |
| 2017 | 3,365 | 583 | 101 | 2,000 | 291 | 51 | 3.0% | +44 | -3 | 25 | 47 |
| 2018 | 4,408 | 758 | 139 | 2,268 | 334 | 61 | 3.2% | +90 | 57 | 38 | 53 |
| 2019 | 4,502 | 828 | 211 | 2,381 | 348 | 89 | 4.7% | -69 | 193 | 46 | 58 |
| 2020 | 3,467 | 621 | 65 | 2,009 | 309 | 32 | 1.9% | -12 | 278 | 26 | 54 |
| 2021 | 5,675 | 1,147 | 545 | 2,095 | 547 | 260 | 9.6% | +366 | 35 | 59 | 56 |
| 2022 | 6,324 | 1,310 | 579 | 2,029 | 646 | 285 | 9.2% | -58 | 501 | 105 | 59 |
| 2023 | 5,109 | 1,022 | 228 | 1,943 | 526 | 117 | 4.5% | -98 | 365 | 122 | 63 |
| 2024 | 4,599 | 834 | 32 | 1,937 | 431 | 16 | 0.7% | -53 | 205 | 100 | 78 |
| 2025 | 4,571 | 782 | -31 | 1,947 | 402 | -16 | -0.7% | +56 | 87 | 52 | 80 |

Arithmetic over 2009-2025 (seventeen years, three troughs and one spike): operating profit $2,583M in total, of which the
two spike years 2021 and 2022 supplied $1,124M (43.5%); the other fifteen years averaged $97M a year, a 2.5% margin. Mean
operating margin 3.3%, median 3.2%. Net LIFO over the seventeen years: $49M of expense, so the price level ended near where
it began and the LIFO charges roughly cancel. Operating expense per ton rose from $205 (2006) to $416 (2025, $809.6M over
1,947 thousand tons) while gross profit per ton rose from $261 to $402.

**How much of the profit is metal price and how much is service.** LIFO charges cost of sales at near replacement cost, so
inventory holding gains are mostly kept out of reported gross profit (2021: $366M of LIFO expense removed). The spread
still widens when prices spike: gross profit per ton ran $291 to $348 in 2015-2020 and $547 to $646 in 2021-2022. On the
table's own arithmetic, the service business earns about $97M a year of operating profit (the fifteen non-spike years),
and the spikes are where the rest of the seventeen-year total came from.

### Owner cash after every real cost (operator rule 5; never a net-income proxy)
Equity basis = operating cash flow less capital spending less stock pay (stock pay is added back inside OCF, so it is taken
out again). Acquisitions are shown, not deducted.

| Year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ryerson owner cash, $M | 0.4 | -29.8 | 15.7 | 144.2 | 250.0 | -29.8 | 387.0 | 229.4 | 93.7 | 26.8 |
| Acquisitions, $M | 1.1 | 50.3 | 169.7 | 0 | 0 | 14.5 | 57.0 | 137.8 | 44.1 | 0 |

Five-year average 2021-2025: **$141.4M** (Ryerson). Olympic Steel, from its own filings (OCF less capex less stock pay,
XBRL of its 10-Ks, last filed 10-K FY2024, accession 0001437749-25-004742): 2020 $50.7M, 2021 -$158.4M, 2022 $164.7M,
2023 $152.1M, 2024 $2.2M; five-year average **$42.3M**. Combined five-year figure: **$183.7M**. Capex against D&A: 0.5 to
0.8 times in 2013-2020 (the Platinum years), 1.3 to 1.95 times in 2022-2024 (the modernization program: Shelbyville KY,
Norcross GA, Dallas, Los Angeles), 0.65 times in 2025; the filer guides "up to approximately $50 million for 2026 with a
focus on productivity enhancing projects and maintenance" against combined D&A of $55.1M in the first half of 2026. The
filing does not split maintenance from growth; depreciation is the nearest figure for the maintenance need.

### The balance sheets, ten years and more, read before the income account (Q4's instruction, done here because the file closes at Q2)
`tools/run.py` table for 2016-2025 (first-filed XBRL), with the selected-data tables for 2006-2015 behind it. What moved:
- **Equity was negative for eight year-ends (2010 to 2017)**, from -$182.5M (2010) to -$293.9M (2012) and back to -$7.4M
  (2017). The cause in the filings: a $213.8M dividend paid in 2010 (plus $56.5M in 2009 and $35.0M in 2012, cash-flow
  statements; the 10-K FY2010 dates the large one 2010-01-29), alongside the 14 1/2% Senior Discount Notes issued in the
  first quarter of 2010 ($483M due by 2015 in the FY2010 contractual-obligations table) and a $5.0M yearly Platinum
  monitoring fee, while the pension plan was short by $359M (10-K FY2011). Debt stood near $1.2B to $1.3B from 2010 to 2014 against equity below zero.
- **The repair came from the 2014 IPO and the 2021-2022 spike.** IPO net proceeds of about $110.7M went to redeem $99.5M
  of 11.25% notes and to pay Platinum Advisors $25.0M for terminating its services agreement (424B4). Debt fell to $367M
  at 2022 year-end; retained earnings went from -$112M (2016) to $692M (2022).
- **Inventory and receivables move with price, not with tons.** Inventory $563M (2016), $832M (2021), $648M (2025);
  receivables $326M (2016), $631M (2021), $461M (2025), against tons that were 1,903 thousand in 2016 and 1,947 thousand in
  2025. The working capital is the business's main capital, and it absorbs cash when prices rise (2021 OCF $35.0M on
  record operating profit; first half 2026 OCF -$157.8M) and releases it when they fall (2009, 2015, 2020, 2022-2023).
- **Goodwill is small** ($103M in 2016, $162M in 2025, $164.4M after the merger); a $70.0M "gain on bargain purchase" on
  the 2018 Central Steel and Wire acquisition passed through other income (10-K FY2018).
- **Pension:** unfunded $359M (2011), $277M (2014), $181M (2018), $73.0M (2022), $33.1M plus $30.7M of retiree
  medical (2025). Contributions of $7.5M (2009) to $55.4M (2014) a year came out of operating cash (10-Ks FY2011, FY2014, FY2018, FY2024).
- **After the merger** (10-Q Q2 2026): total assets $3,841.7M, debt $955.2M, Ryerson equity $1,288.4M, of which $535.4M is
  the stock issued for Olympic (statement of equity: 19,528 thousand shares, $535.4M, about $27.42 a share).
- What the figures cannot say: how much of the post-merger balance sheet is provisional (the purchase price allocation is
  preliminary, "those adjustments may be material", Q2 10-Q); and how much inventory reduction over 2009-2025 was a one-time
  release that flattered the seventeen-year cash flow.

## THE FOUNDATIONS (not a gate)
Two foundations bear hardest. A share is a business: the question is whether one would be content to own this "if the
market closed for five years" **[M1997-109]**, and for a spread business the answer depends on the average spread over a
cycle, not on this year's metal price. And "macro conclusions are — just never enter into the discussion" **[M2000-094]**: the temptation with a metals
distributor is to buy a view on steel prices or tariffs (the 10-K devotes pages to Section 232), which the rule forbids; the
run reads the seventeen-year record instead. One does not get "impartial advice" where "there’s (an) enormous amount of fees possible from one action" **[M2020-037]**: the merger was sold on "$120 million
in annual synergies by the beginning of 2028" (10-K FY2025), a projection, and "we’ve never looked at a projection"
**[M1995-050]**; it is not used below. **Contrary evidence, written down as found**, since the mind "would reject contrary evidence to cherished beliefs" **[M1997-127]**, looking for "what’s
wrong in things" **[M2025-013]** and, the other way, for what the case against might be missing:
- Against: the filer says competition "is based principally on price" and that it faces "increased pressure from online
  businesses that compete with price transparency" (10-K FY2025, Item 1A). Tons fell from 3,292 thousand (2006) to 1,947
  thousand (2025); from 2,433 thousand (2011) to 1,947 thousand, down 20%, although Central Steel and Wire added about 187
  thousand tons in 2018 (2,268 total against 2,081 same-store, 10-K FY2018). Operating loss in 2025 (-$30.8M) and 2009.
  Reliance, selling at a lower average price per ton in 2025 ($2,244 against Ryerson's $2,348), made about $159 of
  operating profit a ton against Ryerson's -$16.
- Against, found while reading Q5 and Q6 material that the run does not reach (facts, not verdicts): the chief executive
  was paid $17,857,908 for 2025, including a special grant of 600,000 restricted stock units ($13,602,000) "to align his
  total compensation with that of our Peer Group", in a year with a net loss of $56.4M; incentive pay is measured on
  "Adjusted EBITDA, excluding LIFO" (DEF 14A 2026). The merger was paid wholly in Ryerson stock.
- For: the business has existed since 1842; in 2025 its North American volume fell 0.4% against an industry decline of
  1.5% (MSCI, cited in the 10-K), a share gain; nearly 80% of what it sells is processed; about 40,000 customers, none above
  6% of sales; the balance sheet and pension were repaired from a deep hole; the merger makes it the second-largest North
  American service center.

## THE STANDING RULE
A cash purchase of a listed stock, no borrowed money, which "has no place in the investor's tool kit" **[L2014-005]**, sized so that the
buyer is never "going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. Nothing about owning RYZ forces the buyer into ruin; the target's own debt is Q9's
question, not reached.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- The test: "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]**; "where the business will be in 10 years" **[M2000-037]**. The product needs no chemistry: what matters is
  "the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- The key variables, "evaluating how predictable they were first, because that is the first step" **[M1998-044]**: tons sold (industrial production), the spread per ton (metal prices and competitors'
  pricing), and cost per ton (warehousing, delivery, people). Year to year the first two cannot be predicted (the filer:
  "cyclical and volatile in both demand and pricing, and difficult to predict", 10-K FY2025 MD&A). Across a cycle they can:
  twenty years of filed statements show the same shape, a gross profit per ton near $240 to $350 in ordinary years, an
  operating profit per ton near zero to $90, and spikes when metal prices jump. That is the third test, whether "the
  financial statements will tell me the information that’s useful to me in making a judgment about what the future
  financial statements are going to look like" **[M2008-033]**: here they do. The industry's insiders write such forecasts
  down every month (the MSCI shipment series quoted in both Ryerson's and Reliance's 10-Ks), so this is not the case of
  insiders who "would say, “That’s too hard.”" **[M2000-105]**.
- Routing: not a fast-changing technology business; not a bank; not a holding company. The post-merger company is two
  businesses of the same kind, read together.
- Doubt test, "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**: the doubt is about next year's metal price, which is "important but unknowable" **[M2006-076]**
  for a year and unimportant across a cycle; the economics of the trade are not in doubt.
- **VERDICT: IN.** The ten-year shape of the business can be foreseen from its own filings: a cyclical, fragmented,
  price-competitive spread business, which is "some notion of how the industry will develop and where the company will stand
  within the industry" **[M2012-065]**. What that shape is worth is Q2's question.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. The answer the rows require is a moat "that protects excellent returns on invested
capital" **[L2007-004]**. Ryerson's returns have never been excellent across a cycle (operating profit on total assets
7.5% pre-tax over 2009-2025, below), so the question is narrower: is there any barrier at all, and is Ryerson the one who
holds it?

**The commodity test, from the filer's own words.** "The metals services industry itself is highly fragmented and
competitive. [...] Competition is based principally on price, service, quality, production capabilities, inventory
availability, and timely delivery. We are experiencing increased pressure from online businesses that compete with price
transparency." (10-K FY2025, Item 1A). "When metals prices decline, customer demands for lower prices and our competitors’
responses to those demands could result in lower sale prices" and "When metals prices increase, competitive conditions will
influence how much of the price increase we may pass on to our customers." (MD&A). That is the commodity of the rows:
"the product is available from many suppliers [...] Consequently, price competition [...] is usually fierce." **[L2004-003]**;
and the business whose price the rival sets: "whatever he charged for gas was my price." **[M2012-109]**, "he determined our
profit, because we looked at his price every day." **[M2023-079]**. Olympic Steel and Worthington Steel say the same of
themselves (below), so the merger joins two price-takers.

**The one exception, the low-cost operator.** "Another way to prosper in a commodity-type business is to be the low-cost
operator." **[L2004-007]**; "when a company is selling a product with commodity-like economic characteristics, being the
low-cost producer is all-important." **[L2000-017]**. The cost that counts is relative, "if your costs are on parity or less — labor costs — than your other major
competitors, that is much more important to you than the absolute level" **[M2001-013]**, and "The figures are available."
**[M2009-059]**. The competitor row:

| Company (own filings) | Span | Operating margin, aggregate | Operating profit / total assets, aggregate | Losing years (operating) | Source |
|---|---|---|---|---|---|
| **Ryerson** | 2009-2025 | **3.65%** | **7.49%** | 2009, 2025 (2010 and 2024 near zero) | 10-Ks above, XBRL |
| **Reliance (RS)** | 2009-2025 | **8.63%** | **11.75%** | none; lowest 4.7% (2009) | 10-K FY2025, accession 0001104659-26-020651, and XBRL |
| **Olympic Steel (ZEUS)** | 2011-2024 | 2.59% (Ryerson 4.44% same years) | 5.55% (Ryerson 9.33%) | 2009, 2014, 2015; 2020 at $0.6M | 10-K FY2024, accession 0001437749-25-004742, and XBRL |
| **Worthington Steel (WS)** | FY2022-FY2026 (years to May) | 3.89% (Ryerson 2021-2025: 5.15%) | not computed (assets from FY2023 only) | FY2026 at -$1.4M | 10-K FY2026, accession 0001968487-26-000026, and XBRL |
| **Russel Metals** | not obtained | | | | non-SEC filer (SEDAR+); not fetched in this run, flagged |

The two smaller peers describe their own trade as Ryerson does: Olympic Steel, "We compete on the basis of price, [...]"
(10-K FY2024, Competition); Worthington Steel, "The steel processing industry is fragmented and highly competitive. [...]
Competition is primarily on the basis of price, product quality and the ability to meet delivery requirements." (10-K
FY2026). Ryerson's margins sit above both of them and far below Reliance.

Same metric, one year, from the two 10-Ks: in 2025 Reliance sold 6,388.1 thousand tons at $2,244 a ton and made operating
profit of $1,012.7M, about **$159 a ton**; Ryerson sold 1,947 thousand tons at $2,348 a ton and lost **$16 a ton**. Reliance's
own account of the difference: "A focus on as-needed inventory management and small orders with quick turnaround and
increasing levels and types of value-added processing generates higher gross profit margins compared to servicing large
orders with volume pricing" (average order $3,120), and "only a small portion of our business is subject to long-term
contractual pricing arrangements" (RS 10-K FY2025). Ryerson: "Many of our larger customers commit to purchase on a regular
basis at agreed upon or indexed prices for periods ranging from three to twelve months" (10-K FY2025, Item 1). In 2025
Reliance grew tons 6.2% against an industry decline of 1.0%; Ryerson grew 0.5%. Classification differs (Ryerson charges
processing costs to cost of materials; Reliance's cost of sales excludes depreciation and warehousing), so gross margins
are not compared; operating profit per ton and the seventeen-year operating margin are like for like. On every
like-for-like measure across the whole span, the low-cost, high-spread operator in this field is Reliance, by a wide margin,
and Ryerson is not. "commodity businesses have risk unless you’re the low-cost producer, because the low-cost producer can
put you out of business. Our textile business was not the low-cost producer." **[M1997-010]**

**The other castle tests, each with its filing fact.**
- *The attacker with money*, "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?"
  **[M2011-015]**: the industry is "highly fragmented" with "a few large competitors, but most of the
  market is served by small local and regional competitors" (10-K FY2025). Reliance has been attacking with money for years
  (it calls its low share an "opportunity for further strategic growth", RS 10-K FY2025). Nothing in Ryerson's filings
  describes a barrier an attacker could not buy: equipment, trucks and inventory are what the filer itself says customers
  will not buy for themselves, which a rival can.
- *Pricing power*, "the agony they go through in determining whether a price increase can be sustained" **[M2005-020]**: the filer passes through price rises only as "competitive
  conditions will influence"; gross margin fell 100 basis points in 2025 "as the soft demand environment challenged
  tariff-supported average selling prices".
- *Unit volume*, where the rows ask for "a lot more unit cases sold" **[M1999-054]**: tons down 20% from 2011 to 2025 despite acquisitions; down 41% from 2006 (part of the
  2007-2009 fall may be Platinum's exit plan of facility closures recorded at the 2007 buyout, FY2010 10-K; the filings read
  do not attribute the tons).
- *Widening or narrowing*, since "the competitive position of each of our businesses grows either weaker or stronger"
  **[L2005-010]**: operating profit per ton $56 (2006), $41 (2014), $61 (2018), -$16 (2025); cost
  per ton up from $205 to $416 while gross profit per ton went from $261 to $402. The business has, in the newspaper letter's
  phrase, "lost still another notch" **[L1995-023]**, visible in the spread between those two lines.
- *Ask the competitors*, "which one would it be and why?" **[M1999-130]**: from the public record only. Reliance's 10-K names no rival; it reports taking share
  in a falling market. No competitor interview was possible.
- *Would the customer choose it over the low bid*: the opposite of See’s, where "it wouldn’t be a question of people buying
  candy for the low bid" **[M2017-009]**; here competition is "principally on price", and online price transparency grows.
- *What could destroy it*: nothing sudden is visible; the risk is the slow one, the rival with lower costs: "sooner or later, the nature of
  a capitalist society is that the guy with the lower cost comes in and kills you" **[M2001-013]**.

**Hunting the other side.** The castle is still standing in the sense that Ryerson has existed since 1842 and gained a
little share in 2025. But the rows' castle protects returns, and a business can survive for a century as an average
competitor: "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**; "there are some
industries that are just never going to have barriers to entry. And in those industries, you better be running very fast"
**[M2012-106]**. The merger's synergy figure is a projection, "a ritual that managers go through to justify doing what they wanted to do in the
first place" **[M1995-050]**, and is not evidence. Scale is the one argument
for the combined company, and the seventeen-year record answers it: Reliance's advantage, on its own account, comes from
small orders and spot pricing, not from size alone, and Ryerson at about two million tons a year was already one of the
largest in the field while earning a third of Reliance's margin.

**Routing.** The castle is not unknowable: the evidence on the record shows it, in the filer's words and the competitors'
numbers over a whole cycle. A castle shown on the evidence to be open closes OUT: "If the answer had been yes, we wouldn’t have
done it." **[M2011-015]**. The framework's own list of what Q2 rules out names the high-cost producer in a commodity field
and the business whose price a competitor sets; the rows behind the first: "In an unregulated commodity business, a company
must lower its costs to competitive levels or face extinction." **[L1994-035]**. Price does not reopen it: "What you can’t do is
turn any investment into a good deal by paying little" **[M2019-015]**; such businesses "are the wrong foundation on which
to build a large and enduring enterprise" **[L2014-009]**.

- **VERDICT: OUT.** A price-taker in a commodity distribution business, not the low-cost operator: over 2009-2025 it earned
  an aggregate 3.65% operating margin against Reliance's 8.63%, and in 2025 lost $16 a ton where Reliance made $159 at a
  lower selling price. In the rows' words, "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**,
  and "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**

---
### COMPUTATION — NOT A CLEARANCE
*The file closed OUT at Q2. What follows is arithmetic reported at the owner's request (not a rule change). It carries no
entry language, and none of it reopens Q2: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.*

**(a) VALUE RANGE, per the Q7 convention.** Cash input: the combined five-year owner cash, **$183.7M** (Ryerson 2021-2025
$141.4M plus Olympic 2020-2024 $42.3M, the last five years each filed). Growth shown: aggregate owner cash swings in sign
inside the window (Ryerson: -$29.8M, $387.0M, $229.4M, $93.7M, $26.8M) and yields no rate, so growth is measured on tons
sold, 2021 to 2025, **-1.8% a year** (CONVENTION of this run, confessed below). Ten years at that rate, then zero nominal
growth, at 5.63%; the other end at zero growth throughout.
- Range: **$2,827M to $3,263M of equity, $54.47 to $62.86 a share**, width 1.15 to 1. Price $27.15. Owner-cash yield on
  the price 13.0%.
- Read mechanically, the convention would place the price far below the bottom of a narrow range. It is wrong for this
  business, and the run says so rather than use it: the window 2021-2025 contains the cycle's spike (2021-2022 alone gave
  43.5% of seventeen years of operating profit), and the warning about "a base year in which earnings were poor" **[L2005-003]**
  applies in reverse to an average that contains the best years of two decades.

**Central case (for the fair price): the full cycle.** Unlevered owner cash (operating profit after a 25% tax, a
CONVENTION, plus D&A, less capex, less stock pay) averaged over Ryerson 2009-2025 ($115.9M) and Olympic 2009-2024
($25.2M): **$141.0M**; less after-tax interest on today's debt (second-quarter 2026 interest $14.3M, annualized $57.2M, after
tax $42.9M): **$98.1M a year to equity**. Growth: zero (tons 1,881 thousand in 2009, 1,947 thousand in 2025). No-growth value
at 5.63%: $1,743M, **$33.59 a share**. Expected pre-tax return at $27.15 on this case: **7.0%**, below the floor of about ten
percent pre-tax (Q7's CONVENTION,
after "we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]** and "a very high
probability of at least 10% pre-tax returns" **[L2002-020]**).

**(b) FAIR PRICE:** the price at which the central case returns the floor of about ten percent pre-tax: $98.1M / 0.10 =
$981M, **$18.91 a share**, about 30% below the price. After-tax equivalent, at an investor tax of 23.8% (20% long-term gains
or qualified dividends plus 3.8% net investment income tax): **7.6%**.

**(c) CHEAP PRICE**, rule stated: the price at which the worst five-year stretch in the combined record, carrying today's
debt, still returns the ten percent floor at zero growth, so that the case is not one where "if you have to actually do it on — with pencil and paper,
it’s too close to think about" **[M1996-084]**, and so that it answers "what the worst case is" **[M2019-023]**. Worst window 2009-2013: combined unlevered owner cash $64.8M a year, less $42.9M after-tax interest, $21.9M;
at 10%, $219M, **$4.22 a share**.

| | per share | against $27.15 |
|---|---|---|
| Value range (convention, five-year window) | $54.47 to $62.86 | price 50% below the bottom; the input is spike-inflated |
| Central no-growth value (full cycle) | $33.59 | price 19% below |
| **Fair price** (10% pre-tax, central case) | **$18.91** | price 44% above |
| **Cheap price** (worst stretch still earns 10%) | **$4.22** | price 6.4 times |

---
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2). Facts recorded for the record only: operating profit on total assets 7.5% pre-tax over
2009-2025 (aggregate), and working capital consumes cash in every price rise.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The balance sheets were read in Step 0, "over an 8 or 10 year period before I even look at
the income account" **[M2025-032]**. Noted, not judged: incentive pay is set
on "Adjusted EBITDA, excluding LIFO" (DEF 14A 2026); 2018 earnings included a $70.0M bargain-purchase gain.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. The pay facts written down under the foundations are not a judgment of integrity.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts for the record: buybacks $50.0M (2022), $113.9M (2023), $51.0M (2024), none in 2025; regular
quarterly dividends since the third quarter of 2021, $0.1875 a quarter in 2025 and 2026 (10-K FY2022; 10-Q Q2 2026); 1.6M
shares bought back from Platinum in 2022 (10-K FY2022); the Olympic merger paid wholly in stock (19.5M shares, about $27.42 each by the
statement of equity). The framework's one STOP in Part A concerns an all-stock deal by an undervalued acquirer; it was not
tested because Q7 was not reached.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a verdict. The arithmetic is in the COMPUTATION block above.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts: debt $955.2M under an asset-based facility with a borrowing base of receivables and inventory and a
springing fixed-charge covenant (10-K FY2025, Item 1A); availability $668M at 2026-06-30.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT ASKED (closed at Q2).

---
## THE BOX
**OUT at Q2.** A price-taker in a commodity distribution business and not its low-cost operator: 2009-2025 operating
margin 3.65% against Reliance's 8.63%, operating profit $-16 a ton in 2025 against Reliance's $159, tons down 20% since 2011
despite acquisitions. "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; "Another way to
prosper in a commodity-type business is to be the low-cost operator." **[L2004-007]**; Ryerson is not that operator. Computation only: price $27.15 against a
convention range of $54.47 to $62.86 (spike-inflated input), a full-cycle no-growth value of $33.59, a fair price of $18.91
and a cheap price of $4.22.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written question by question after the reading, in one pass; **not
      committed**, by the dispatching instruction for this run (no commits); the write-early protocol was therefore not
      followed in its commit half.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, with every quoted fragment beside an id
      matched inside that row); every filing fact has its accession; numbers come from filings or are labelled
      COMPUTATION or CONVENTION.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance, and the arithmetic after it is headed
      COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost from cash flow, capex and stock pay, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found, both ways, lest the mind "reject contrary evidence to cherished
      beliefs" **[M1997-127]**.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its yield lines were set aside (Ryerson-only cash against
      the combined market value).
- [x] `python tools/check_framework.py` PASS (run after this file was written; result in the reply).
- Gaps, stated: Russel Metals not obtained (non-SEC); no industry tonnage series over the span from a primary source (the
  MSCI figures appear only one year at a time inside the 10-Ks); the merger prospectus not read beyond terms; Olympic's
  2025 full year not filed; the director-only stock pay figure not extracted; no competitor, customer or supplier
  conversation (public record only).

**CONVENTIONS of this run, confessed.** (1) Growth for the convention's shown-growth end measured on tons sold, because
aggregate owner cash changes sign inside the window and gives no rate; rationale: tons are the volume of the business and
are filed every year. (2) The post-merger company's five-year cash is Ryerson 2021-2025 plus Olympic 2020-2024, the last
five filed years of each; rationale: the convention has no rule for a merger and these are the latest filed figures. (3) A
25% tax on operating profit in the full-cycle central case (21% federal plus state); rationale: the unlevered figure needs a
tax and Ryerson's reported tax lines are distorted by valuation allowances in 2009 and 2013. (4) The central case for the
fair price uses the full 2009-2025 cycle, not the convention's five years; rationale: the owner asked for "your central
case", and the five-year window contains the spike. (5) The cheap-price rule (worst five-year stretch still earns the
floor); rationale: the owner asked that the rule be stated, and it is the plainest form of "what the worst case is"
**[M2019-023]**.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
The Q7 range convention fails on a cyclical spread business, and nothing in it warns. A five-year average is a fair base
for a steady business; here the last five years contain the best two years of two decades, so the convention gives a
narrow range ($54 to $63) far above any full-cycle value ($34 no-growth), and the price would look like a screamer to an
analyst who reached Q7 without reading the long record. The three-to-one width test cannot catch it, because the two ends
differ only by the growth rate, not by the cycle. The framework already carries the rows for the cure ("a base year in which earnings were poor can produce a
breathtaking, but meaningless, growth rate" **[L2005-003]**, and "what the worst case is" **[M2019-023]**); a sentence saying "for a business whose earnings swing with a
commodity price, the average covers a whole cycle shown in the filings" would close the gap. Second, "growth measured on
the aggregate owner cash" is undefined when owner cash changes sign; this run measured it on tons and confessed it. Third,
the convention is silent on a company that has just merged; this run summed the two histories. Fourth, Q2's commodity
exception, "the low-cost operator", gives no measure for comparing companies whose income statements classify costs
differently; the run used operating profit per ton and the whole-span operating margin, which is ours. Fifth, the template
asks for the Q4 balance-sheet reading under Q4, but the brief asked for it in Step 0 when the file closes earlier; the
template does not say so, and a run closing at Q1 or Q2 would skip it.
