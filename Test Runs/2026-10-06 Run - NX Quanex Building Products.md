# Company Run: Quanex Building Products Corporation (NYSE: NX), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this run by the blind rule of the
instruction that dispatched it; the analyst does not know whether the operator holds NX.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
`Screens/WATCHLIST RUN QUEUE.md`, the prepped reading list, any other run or research file about Quanex, any other
company's 2026-10-05 or 2026-10-06 run or research file, the unadopted small-cap gaps case. Seen without opening: the git
status and recent commit subjects in the session context (NWL, MD, COLL and MHO v5 runs; an untracked LRN run file); the
`Test Runs/` directory listing (two older runs whose tickers contain the letters NX: NXRT and CGNX, not opened); the
memory index line "57 gate-clearers, nothing buyable". None of these names Quanex or bears on it.

Working folder: `Test Runs/_research 2026-10-06 NX/` (filings as text, `fetch.py`, `facts.py`, `series.py`, `margins.py`,
`compute.py` and its output `compute_out.txt`, `runpy_out.txt`).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $18.91 (close 2026-10-05; aggregator quote via `tools/run.py`, flagged per operator rule 5: a live quote only).
- **Shares by class** from the latest filing's cover: one class, common, 45,826,208 shares (10-Q for the quarter to
  2026-07-31, filed 2026-09-04, accession `0001423221-26-000048`; `python Screens/cover_shares.py NX`). No other class;
  1,000,000 preferred authorized, none issued (10-K FY2025, Note 15).
- **Market cap:** $866.6M (45.826M x $18.91).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (fiscal year to 2025-10-31), filed 2025-12-12, accession
  `0001423221-25-000100` (Items 1, 1A, 3, 5, 7, 7A, 8 statements and notes 1, 2, 5 to 9, 14 to 17, 9A); 10-Q to 2026-07-31,
  accession `0001423221-26-000048` (statements, segment note, legal note, MD&A by segment, Item 4); proxy DEF 14A filed
  2026-01-28, accession `0001104659-26-007408` (pay design, ownership); 8-Ks `0001104659-26-004552` (auditor change,
  2026-01-16), `0001104659-26-002477` (Teleios observer, 2026-01-09), `0001104659-25-100856` and `0001104659-25-103181`
  (officer and director appointments), `0001104659-26-022858` (bylaws, vote results); the Tyman offer announcement, 8-K
  exhibit 99.1, accession `0001104659-24-049723` (2024-04-22). History: 10-K FY2010 `0000950123-10-115049` (selected data
  2006-2010, Engineered Products segment 2008-2010, customers 2008-2009), 10-K FY2013 `0001423221-13-000010` (segment 2011-2013),
  10-K FY2016 `0001423221-16-000026` (customers 2014-2016, segments 2014-2016), 10-K FY2019 `0001423221-19-000018`,
  10-K FY2022 `0001423221-22-000014` (customers 2020-2022); XBRL company facts for FY2009-FY2025 (first-filed values).
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025 $164,897
  thousand in the filed statement of cash flow (10-K FY2025, page 46) = $164.9M in `tools/run.py`. Capital expenditures
  $62,642 thousand = $62.6M. Both agree.
- `python tools/run.py NX`, arithmetic lines only: OCF 147.1 / 88.8 / 164.9 (FY2023/24/25), capex 37.4 / 37.1 / 62.6, D&A
  42.9 / 60.3 / 103.4. **Stock pay resolved:** the tool's SBC column takes 9.3 and 7.3 for FY2023 and FY2024 from
  AllocatedShareBasedCompensationExpense, which includes liability awards marked to the share price (Note 14: total
  expense 9.3 / 7.3 / 2.4; restricted stock units and performance shares are liability awards whose expense moves with the
  stock). Liability awards settle in cash and so already sit inside operating cash. The non-cash, equity-settled stock pay
  is the cash-flow add-back, 2.5 / 3.0 / 3.7 (statement of cash flow), and that is what this run deducts. Complete for the
  purpose: every form of stock pay is either in OCF (cash-settled) or deducted (equity-settled).

### Owner cash after every real cost (USD millions; OCF less capex less equity-settled stock pay; XBRL first-filed 10-K values; FY2010-FY2013 include the aluminum sheet business sold in 2014)
| FY | Sales | Op. income | Op. margin | Goodwill/asset impairment in op. income | Op. margin ex impairment | Owner cash | Owner cash / sales | Capex / D&A |
|---|---|---|---|---|---|---|---|---|
| 2010 | 798.3 | 37.3 | 4.7% | 0 | 4.7% | 69.9 | 8.8% | 0.52 |
| 2011 | 848.3 | 16.5 | 1.9% | 1.8 | 2.2% | 22.7 | 2.7% | 0.74 |
| 2012 | 829.0 | -25.0 | -3.0% | 0.9 | -2.9% | -22.0 | -2.7% | 1.14 |
| 2013 | 952.6 | -17.7 | -1.9% | 1.5 | -1.7% | 0.7 | 0.1% | 0.63 |
| 2014 | 595.4 | 14.3 | 2.4% | 0.5 | 2.5% | -16.9 | -2.8% | 1.00 |
| 2015 | 645.5 | 24.7 | 3.8% | 0 | 3.8% | 32.8 | 5.1% | 0.85 |
| 2016 | 928.2 | 36.4 | 3.9% | 12.6 | 5.3% | 43.1 | 4.6% | 0.70 |
| 2017 | 866.6 | 34.4 | 4.0% | 0 | 4.0% | 38.8 | 4.5% | 0.60 |
| 2018 | 889.8 | 36.4 | 4.1% | 0 | 4.1% | 76.2 | 8.6% | 0.51 |
| 2019 | 893.8 | -26.4 | -3.0% | 74.6 | 5.4% | 69.5 | 7.8% | 0.50 |
| 2020 | 851.6 | 55.3 | 6.5% | 0 | 6.5% | 74.2 | 8.7% | 0.54 |
| 2021 | 1,072.1 | 81.9 | 7.6% | 0 | 7.6% | 52.6 | 4.9% | 0.56 |
| 2022 | 1,221.5 | 111.3 | 9.1% | 0 | 9.1% | 62.6 | 5.1% | 0.83 |
| 2023 | 1,130.6 | 110.7 | 9.8% | 0 | 9.8% | 107.2 | 9.5% | 0.87 |
| 2024 | 1,277.9 | 54.8 | 4.3% | 0 | 4.3% | 48.7 | 3.8% | 0.62 |
| 2025 | 1,837.6 | -194.0 | -10.6% | 302.3 | 5.9% | 98.6 | 5.4% | 0.61 |
| TTM to 2026-07-31 | 1,863.1 | | | | | 86.3 | 4.6% | |

Five-year average (FY2021-2025) owner cash, capex basis: **$73.9M**; depreciation-only variant (D&A less amortization of
acquired intangibles, which the filer's Note 7 shows are customer relationships and trade names): $74.4M; full D&A
variant: $54.9M. Capex sat at 0.5 to 0.9 of D&A in most years because D&A carries amortization of purchased
intangibles; against depreciation alone (FY2025: $64.0M including a one-time $7.3M, Note 5) capex of $62.6M is about one
for one. Maintenance judgment: the filer does not split maintenance from growth capex; capex near depreciation is read as
roughly what keeps the plants in place. Sixteen-year owner cash total FY2010-2025: $758.7M; acquisitions paid in cash over
the same years $1,015.7M (XBRL PaymentsToAcquireBusinessesNetOfCashAcquired), plus 14,139,477 shares issued for Tyman
($450.1M) and $296.2M of Tyman debt repaid at closing (cash flow FY2024). Cumulative net income FY2009-2025: **-$42.8M**.
Pre-spin history (10-K FY2010, selected data, building products with aluminum sheet): FY2006 sales $1,043.8M, operating
income $104.8M (10.0%); FY2007 $964.0M, $88.2M (9.1%); FY2008 $868.9M, $21.1M (2.4%); FY2009 $585.0M, -$179.1M. The
Engineered Products segment alone (window and door components, before corporate costs): FY2008 7.4%, FY2009 6.7% before
its $162.2M impairment, FY2010 9.5% ("the highest in the past five years"), FY2011 7%, FY2012 6%, FY2013 8% (10-K FY2010
and FY2013).

### The balance sheets, read first (Q4's eight to ten years, read here because the file closes before Q4)
"balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**. XBRL first-filed
values, USD millions, checked for FY2024 and FY2025 against the filed balance sheet (10-K FY2025, page 42):

| FY end | Equity | Goodwill | Intangibles | Tangible equity | Cash | Debt (face) | Receivables / sales | Inventory / sales | Retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2008 | 547.8 | n/a | n/a | | 66.9 | n/a | | | |
| 2010 | 441.4 | 25.2 | n/a | | 187.2 | n/a | | | |
| 2013 | 416.2 | 71.9 | n/a | | 49.7 | n/a (1.4 at FY2012, 0.8 at FY2014) | | | |
| 2016 | 367.8 | 217.0 | 154 | -3 | 25.5 | 270 | 9.0% | 9.0% | 214 |
| 2018 | 394.2 | 219.6 | 122 | 53 | 29.0 | 211 | 9.4% | 7.8% | 243 |
| 2019 | 330.2 | 145.6 | 107 | 78 | 30.9 | 157 | 9.3% | 7.5% | 186 |
| 2020 | 355.8 | 146.2 | 93 | 117 | 51.6 | 117 | 10.3% | 7.2% | 214 |
| 2021 | 419.8 | 149.2 | 82 | 189 | 40.1 | 53 | 10.1% | 8.7% | 260 |
| 2022 | 464.8 | 137.9 | 65 | 262 | 55.1 | 31 | 7.9% | 9.9% | 337 |
| 2023 | 545.6 | 183.0 | 74 | 289 | 58.5 | 69 | 8.6% | 8.7% | 409 |
| 2024 | 1,010.7 | 574.7 | 598 | -162 | 97.7 | 763 | 15.5% (part year) | 21.6% (part year) | 430 |
| 2025 | 726.2 | 271.3 | 549 | -94 | 76.0 | 693 | 11.2% | 13.8% | 165 |
| 2026-07-31 (10-Q) | 745.4 | 273.8 | 522 | -51 | 62.1 | 663 | | | 179 |

What the figures say: book equity was $548M at the spin's first year-end (2008) and $546M fifteen years later (2023), while
the company bought back about $195M of stock and paid about $133M of dividends (XBRL, FY2010-2025); the retained earnings it
did make went out to owners or into acquisitions whose goodwill was then written off: $170.7M (FY2009), $12.6M (FY2016,
the U.S. vinyl extrusion goodwill), $74.6M (FY2019), $302.3M (FY2025, 10-K FY2025 Note 7). Goodwill steps up with each
deal (Edgetech 2011, HL Plastics 2015, Woodcraft 2015, LMI 2022 at $91.3M, Tyman 2024 at $848.6M net of cash including
$300.7M of its debt, Note 2) and steps down after. Tangible equity is negative after Tyman (-$94M at FY2025). Long-term debt went
from about $1M (tagged FY2011-2014) to $270M after Woodcraft (2016), back to $31M (2022), then to $763M with Tyman; at 2026-07-31 it is $663M
against $62M of cash, all floating-rate bank debt with $175M swapped to fixed in the third quarter of FY2026 (10-Q Note 9).
Receivables and inventory against sales stepped up with Tyman (international terms "from cash advances to 90 days", 10-K
Item 1), and inventory reserves went from about 1% to about 9% of gross inventory in one year (10-K FY2025, Critical
Accounting Policies: Inventory). What they do not say: why the inventory reserve rose ninefold; how the Tyman hardware
business performed before purchase (it filed in London, not here). What they cannot say: what the castle is worth.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether one would be content to own this "if the market closed for five years"
("Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**), and the business is a
supplier of parts to window, door and cabinet makers whose returns are set by those customers. The market serves: the
price fell from $34.64 (the reference price in the Tyman offer, April 2024) to $18.91, and the fall "just tells us prices"
("It just tells us prices." **[M2006-077]**); it instructs nothing. No macro enters: the 10-K's housing-start and
window-shipment forecasts (NAHB, Ducker, Item 1) are not used. Who is paid to tell you: the Tyman case was made by the
buyer as part of its BIGGER strategic roadmap, "moving Quanex closer to its $2 billion revenue target", with "approximately $30 million" of cost
synergies and the deal "meaningfully accretive to earnings" (8-K exhibit 99.1, `0001104659-24-049723`), and the executives'
annual bonus is half on Adjusted EBITDA measures (proxy, `0001104659-26-007408`); those statements are read as the
acquirer's own projections, not as evidence. Margin of safety: a case that needs "pencil and paper" is too close ("with pencil
and paper" **[M1996-084]**).
**Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**):
1. The Extruded Solutions segment (insulating-glass spacers, vinyl profiles, seals) earned 16% (FY2024), 6% after its
   $54.9M impairment and about 14% before it (FY2025), and 16% in the third quarter of FY2026 (10-Q); the filer holds patents
   on spacer designs and says "Our window sealant business unit relies on patents" (10-K Item 1). A part of the business may
   have a niche.
2. Pre-tax operating income before impairment and amortization (EBITA) of about $147.6M in FY2025 on tangible operating
   capital of roughly $836M (working capital about $269M, plant $412M, lease assets $155M) is about 17.7% pre-tax: the
   tangible capital the plants need is not starved of return in a decent year.
3. Price pass-through is contractual for most resin, oil-based and hardwood inputs ("we have price adjusters in place
   which effectively share the base pass-through price changes", 10-K Item 7), which protects the margin from commodity
   swings.
4. The run-rate synergy figure reported for pay purposes was $42M against a $15M goal (proxy).
5. Owner cash has been positive in thirteen of sixteen years and, at TTM $86.3M, about 10% of the market value.

## THE STANDING RULE
Owning NX for cash, sized so that a total loss is survivable, puts the buyer at no risk of ruin; bought on margin it would
("borrowed money has no place in the investor's tool kit" **[L2014-005]**). The buyer's conduct, not the target's; the
target's own debt is Q9's (not reached). "figure out what can really go wrong with this place" **[M2012-081]**.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- The test: "a reasonable fix on about what the earning power and competitive position will look like in five or 10
  years" **[M2012-065]**; the product chemistry need not be understood if "I understand the economic dynamics of the
  industry" **[M2011-014]**.
- The key variables, "trying to identify the key variables in that particular business" **[M1998-044]**: (1) unit volume
  of window, door and cabinet production, driven by remodeling and housing starts (10-K Item 1: "the primary drivers of our
  operating results are residential remodeling and replacement activity and new home construction"); (2) the spread
  between selling prices and resin, metal, wood and labour costs, governed by index adjusters and by OEM bargaining power
  (Item 1A, Item 7A); (3) what the acquisitions earn after they are paid for. None is a fast-changing technology: windows,
  doors and cabinets change slowly, and the filer's own trend list names energy standards, tariffs and commodity prices,
  not substitution. Each variable is "important and knowable" ("things that are important and knowable" **[M2006-076]**)
  from seventeen years of the company's own filings, including a full housing cycle (FY2009 through FY2025).
- What can be foreseen: a component supplier to window and door makers, cyclical with housing, whose margin is set by
  the customers' bargaining power and by its own acquisitions. The filings answer "do I understand enough about this
  business so that the financial statements will tell me" **[M2008-033]**: yes for the legacy business (seventeen years);
  less so for Tyman's hardware, whose pre-purchase record is not in an SEC filing, but its two post-purchase years are in
  the segment note.
- **VERDICT: IN.** The economics of the industry and the company's place in it can be foreseen in kind ten years out; what
  they show is Q2's question. Filing fact: same product set, same customer type, same competitive-factor language in the
  10-Ks of FY2010, FY2013 and FY2025.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**, asked knowing "all moats are subject to attack in a capitalistic
system" **[M1995-038]**.

- **The attacker with money.** "If the answer had been yes" **[M2011-015]**, the purchase is not made. Could $100M or $1bn
  take on Quanex? The filer: "Our products are sold under highly competitive conditions", "The volume of engineered building
  products that we sell in the U.S. represents a small percentage of annual domestic consumption", "The U.K. and
  International market is highly fragmented", and it competes against "the in-house operations of customers who have
  vertically integrated fenestration operations" (10-K FY2025 Item 1). The same sentences, nearly word for word, stand in the
  10-K FY2010 ("The business also competes with in-house operations of vertically integrated fenestration OEMs"). The
  attacker does not need money: the customer can make the part itself. This is the industry where "some industries that are
  just never going to have barriers to entry" **[M2012-106]** applies; and "one competitor is frequently enough to ruin a
  business" **[M2012-108]**.
- **Pricing power and the agony before a rise.** "a prayer session before you raise your prices a penny" **[M2005-020]**.
  The filer: "Our primary customers are OEMs, who have substantial leverage in setting purchasing and payment terms", and it
  manages this "by negotiating reasonable price concessions when needed" (Item 1A); the same OEM-leverage sentence stands in
  the 10-K FY2013. The first competitive factor it names is "price" (Item 1). On costs: "we have not been able to fully
  recover all of the inflationary cost increases" (Item 7, Effects of Inflation), against the row's test that "over time
  the businesses with strong competitive positions manage to pass through increases in raw material costs" **[M2005-017]**.
  The index adjusters share commodity moves "commensurate with the market at large" (Item 7A): a pass-through the whole
  industry has, not a price the company sets. In the third quarter of FY2026 the Hardware segment refunded $9.1M of tariff
  charges to customers (10-Q MD&A). Price and surcharge added $4.6M, $1.7M negative and $6.9M to the three segments' FY2025
  sales of $1.84bn (10-K MD&A): price contributed almost nothing.
- **Unit volume.** Volumes fell in every segment in FY2024 and FY2025 ($22.9M, $20.0M, $11.2M in FY2024; $4.8M, $32.5M,
  $2.4M in FY2025, 10-K MD&A) and by $10.7M in Hardware in the first nine months of FY2026 (10-Q). Housing is cyclical and
  this is not a castle test failed by itself.
- **The low-cost position.** In a commodity-like field "being the low-cost producer is all-important" **[L2000-017]**, and
  "the low-cost producer can put you out of business" **[M1997-010]**. No filing claims Quanex is the low-cost producer; it
  claims "design expertise, new technology development capability, high quality manufacturing, just-in-time delivery
  systems, customer service" (Item 1, Our Strengths). Its customers' in-house plants and "Assa Abloy, Roto, Hoppe, Veka,
  Profine" and others are named competitors; several are larger. No instance found in the filings read of a cost
  comparison with any competitor.
- **The brand in the customer's mind.** The customer is a manufacturer, not a consumer; the marks (Edgetech, Super Spacer,
  Truth, Schlegel, Mikron) are trade names to OEM buyers. The test of the low bid, "people buying candy for the low bid"
  **[M2017-009]**, is answered by the filer itself: price first, concessions when needed.
- **Would the customer still choose it over the low bid?** For the spacer business, partly: patents and engineering
  specifications. For the rest, no evidence it would: one customer above 10% of sales in FY2023, FY2024 and FY2025 (Note 1),
  two customers at 11% and 15% (FY2014) and 11% and 14% (FY2015) (10-K FY2016 Note 1), Associated Materials at 12% (FY2008)
  and Andersen at 11% (FY2009) (10-K FY2010). Concentrated buyers with their own plants set the terms.
- **Ask the competitors / the competitor row** (same metric, operating margin before the impairment lines tagged, from the
  competitors' own 10-K XBRL facts; the span is the whole span each filed):

| Company | Role | Span | Mean operating margin ex impairment | Range | Accessions (first, last) |
|---|---|---|---|---|---|
| Quanex (NX) | component supplier | FY2009-2025 | 4.1% (4.5% over 2012-2023) | -2.9% to 9.8% | `0001193125-11-346617`, `0001423221-25-000100` |
| PGT Innovations (PGTI, history; acquired 2024) | window maker | 2010-2023 | 8.2% (11.2% over 2012-2023) | -5.4% to 13.6% | `0001193125-12-116968`, `0000950170-24-019325` |
| Fortune Brands (FBIN) | branded doors, plumbing, security | 2009-2025 | 10.7% (12.0% over 2012-2023) | 1.8% to 16.4% | `0001193125-12-072886`, `0001193125-26-063960` |
| Masonite (DOOR, history; acquired 2024) | door maker | 2011-2023 | 5.6% | -0.5% to 11.3% | `0000893691-14-000022`, `0000893691-24-000011` |
| JELD-WEN (JELD) | window and door maker | 2015-2025 | 3.4% (4.5% over 2015-2023) | -2.5% to 6.6% | `0001674335-18-000038`, `0001674335-26-000043` |
| Tyman plc (history; LSE-listed, flagged) | hardware and seals supplier | not obtained | not obtained from its own filings | | no SEC filing. What the SEC record shows: Quanex's pro forma FY2023 combined sales $1,955.0M less Quanex's $1,130.6M puts Tyman near $824M (10-K FY2025 Note 2, unaudited pro forma); Quanex's Hardware segment, mostly Tyman, earned 2% (FY2024), 2% before its $163.2M impairment (FY2025), and 0.0% ($0.15M on $613.1M) in the nine months to 2026-07-31 (10-Q segment note) |

  Over the common span the supplier earned less than the window maker that buys such parts (PGT 11.2% against Quanex 4.5%,
  2012-2023) and about a third of the branded maker (FBIN 12.0%); it earned about what the commodity door and window makers
  earned (Masonite 5.6%, JELD-WEN 4.5%). The value in the chain does not stay with the component supplier.
- **Widening or narrowing.** "how wide the moat is" **[M1999-108]**: the best years are the cycle's peaks (10.0% in FY2006,
  9.8% in FY2023) and the margin has never held above 10%; the post-Tyman business earned 5.9% before impairment in FY2025
  and 5.0% in the first nine months of FY2026 (10-Q). The goodwill paid for four sets of acquired businesses was written down
  in FY2009 (goodwill and intangibles), FY2016, FY2019 and FY2025: purchased castles, each judged by the buyer to be worth more than its assets, were
  found within a few years to be worth less. That is the record of "companies whose moats proved illusory and were soon
  crossed" **[L2007-004]**.
- **What could destroy it.** "destroy, or modify, or reduce the economic strengths" **[M2000-014]**: a large customer
  integrating vertically or splitting its supply (Item 1A names both); a sole U.S. plant for spacers (Item 1A); tariff and
  sourcing shifts in hardware.
- **The commodity reading.** Where "the improvement you get one day, your competitor gets the next day" **[M2004-053]**,
  and the customer sets the price, the business is the one whose rival or buyer sets the margin ("whatever he charged for gas
  was my price" **[M2012-109]**; "he determined our profit, because we looked at his price every day" **[M2023-079]**). The
  rows' exception, the low-cost producer ("being the low-cost producer is all-important" **[L2000-017]**), is not shown here; the high-cost or average producer meets "the guy
  with the lower cost comes in and kills you" **[M2001-013]**.
- **Against, from the contrary list.** The spacer and extrusion part (contrary evidence 1) is the best evidence of a niche,
  but it is one part of a whole bought together, and its own margin fell from 16% to about 14% before impairment in FY2025
  with volume down $32.5M. A whole bought with the hardware and wood businesses inside it is judged as a whole; no rule in
  the framework lets one segment's niche carry the rest (see What in the framework was wrong or unclear).
- **VERDICT: OUT.** The castle is shown open on the evidence, not merely unjudgeable: the filer's own words for fifteen years
  (price first, OEMs with "substantial leverage", price concessions, costs not fully recovered, customers who make the part
  themselves), a seventeen-year operating margin averaging about 4% before impairments with a peak of about 10%, margins below
  its own customer type and a third of the branded maker's, and four write-downs of purchased goodwill. "therefore we leave
  it alone" **[M2000-019]**; and a lower price does not reopen it, since one cannot "turn any investment into a good deal by
  paying little" **[M2019-015]**. In the three boxes, "three boxes at the company: in, out, and too hard" **[M2006-013]**,
  this is OUT.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (the file closed at Q2). Recorded as COMPUTATION: NOT A CLEARANCE, because the owner's reporting needs
the growth cap: over FY2021-2025 aggregate owner cash rose from $52.6M to $98.6M (a 17.0% yearly rate) while about $490M of
new cash (LMI $91.3M, Tyman $398.6M net of cash) and 14.1M new shares ($450.1M) went into acquisitions and $296M of Tyman
debt was repaid; the added owner cash of about $46M a year on roughly $950M-$1,240M of added capital is about 4% to 5%, below
the 5.66% sovereign. Whether that grade is "reinvesting the capital at a very low rate of return" **[M1998-081]** is not
weighed here.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance sheets are read in Step 0. Facts found and written down for any later look, not judged here:
(a) an adverse opinion on internal control at FY2024 and FY2025 for a material weakness in "the preparation and review of
the statement of cash flows" (10-K FY2025 Item 9A and auditor's report), still not remediated at 2026-07-31 (10-Q Item 4),
the statement from which owner cash is drawn; (b) the auditor in place since 2014 (Grant Thornton) dismissed on 2026-01-13, with no
disagreements reported and the material weakness named as the one reportable event (8-K `0001104659-26-004552`); (c) a
securities class action, amended 2026-03-24, on disclosures about the Tyman acquisition and the Mexican window and door
operations, and a derivative suit (10-Q Note 8); (d) bonus metrics half on Adjusted EBITDA, which "excluded [...] asset
impairment charges, and restructuring charges" (proxy). The rows that would be applied are "The one figure we regard as
utter nonsense is the so-called EBITDA" **[M1998-086]** and "accounting can offer you a lot of insight into the character
of management" **[M1995-064]**; no verdict is drawn.

## Q5: WHO RUNS IT. STOP on integrity.
**NOT REACHED.** Facts only: George Wilson, CEO since 2020-01-01, at Quanex since the Edgetech purchase in 2011; owns
347,294 shares (about $6.6M at the price) against 2025 total pay of $3,635,424 (proxy). An activist holder, Teleios
(9.6%), withdrew its board observer on 2026-01-08 (8-K `0001104659-26-002477`).

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts only: the Tyman price was 400 pence a share, a 35.1% premium, paid as 240 pence cash plus 0.05715
Quanex shares (8-K exhibit 99.1); not wholly in stock, so the all-stock STOP is not engaged. Shares were issued at about
$31.83 (Note 2: $450.06M for 14,139,477 shares) and $32.4M of stock was bought back in FY2025 at about $18.93 a share
(1,709,119 shares, Note 15); the programme names no price. Within a year $302.3M of goodwill was impaired. The rows that
would be applied: "the acquirer typically gives up more intrinsic value than it receives" **[L1994-015]**; "we never count
on synergies when we acquire companies" **[L2016-008]**; "You can't get rich trading a hundred-dollar bill for eight tens"
**[L2014-012]**.

## Q7: WHAT IS IT WORTH? STOP.
**NOT REACHED as a judgment.** The owner asked for the figures; every number below is

### COMPUTATION: NOT A CLEARANCE
No entry language attaches to any figure here (operator rule 3).

**(a) VALUE RANGE, the Q7 convention.** Cash input: five-year average owner cash after every real cost, FY2021-2025,
$73.9M (capex basis). Growth shown in aggregate owner cash over those five years is 17.0% a year, bought with an acquisition
paid in stock and debt; carried ten years it makes year-ten owner cash of about $356M against a best-ever year of $107M, a
result that traces to an absurdity ("if you trace out the mathematics of it, you bump into absurdities, then you better
change expectations somewhat" **[M1999-067]**). CONVENTION of this run: the shown-growth end uses the whole-span
FY2010-2025 aggregate owner cash growth, 2.3% a year, the growth the business actually showed across a full cycle
including all its acquisitions; rationale: the convention says "the growth the business has actually shown" and caps it by
Q3 but names no substitute when the window's growth is bought. Ten years, then zero nominal growth, discounted at 5.66%
("use the government bond rate" **[M1996-025]**):
- no-growth end: $1,306M, **$28.51** a share;
- shown-growth end (2.3%): $1,570M, **$34.25** a share.
- Width 1.2 to 1, inside the three-to-one rule. Price **$18.91**, below the bottom of the range.
- **Whole-cycle variant** (the window holds abnormal years: FY2024 carried Tyman deal costs and a part year of Tyman; FY2023
  and FY2025 were lifted by working-capital releases of $30.0M and $23.6M of inventory; and three of the five years carried
  almost no interest while today's debt costs $49.9M a year): the FY2010-2025 average owner cash margin, unlevered by adding
  back after-tax interest (5.33% of sales), on TTM sales of $1,863.1M gives $99.2M before interest; less today's after-tax
  interest ($49.9M at an assumed 21% tax, CONVENTION of this run, the U.S. statutory rate the filer cites) gives **$59.9M**
  to equity. Range: no growth $1,058M, **$23.08**; 2.3% growth $1,271M, **$27.73**.
- Expected return at the price, no growth: 8.5% on the five-year figure, 9.96% on TTM ($86.3M), 6.9% on the whole-cycle
  figure at today's debt. Only with the 2.3% growth added does the five-year case reach 10.8%.

**(b) FAIR PRICE** (the price at or below which the central case clears the floor of about ten percent pre-tax, "our real
expectancy is below 10 percent" **[M2003-149]**). Central case: five-year owner cash, no growth (Q3's computation shows the
added capital earning below the sovereign, so growth is given no value). Tax treatment: owner cash is after the company's
interest and income taxes, and is counted as the buyer's pre-tax return; the floor is applied **on equity** (market value of
the shares).
- Central case on equity: **$16.13** ($73.9M / 10% / 45.826M shares).
- Whole-cycle variant at today's debt, on equity: **$13.06**.
- On equity plus net debt (net debt $601.3M at 2026-07-31: $663.4M debt less $62.1M cash; unlevered owner cash
  at 10% on the enterprise): five-year case **$6.10** (unlevered $88.1M); whole-cycle case **$8.53** (unlevered $99.2M).
  The equity basis is higher because the bank debt costs about 6.6% before tax, less than the 10% floor; the enterprise
  basis is the stricter test.

**(c) CHEAP PRICE** (below which no pencil is needed: "It should scream at you." **[M2009-005]**). CONVENTION of this run:
the price at which the lower of the two equity owner-cash estimates (five-year $73.9M, whole-cycle at today's debt $59.9M)
yields 15% with no growth, half again the floor, so that a 30% shortfall in owner cash still clears 10%; rationale: "buy it at
a big discount from that present value calculated using the risk-free interest rate" **[M1997-126]** names a big discount and
no number. Cheap price: **$8.71** on equity (whole-cycle). On the enterprise basis no positive price meets 15% on the
five-year case, and the whole-cycle case gives $1.32.

Against the price of $18.91: above the fair price on every basis (equity central $16.13; whole-cycle $13.06; enterprise
$6.10 to $8.53) and about twice the cheap price. Were Q2 IN, the close would be OUT at Q7 through the floor, not through the
range, since the range bottom ($23.08 to $28.51) sits above the price while the expected return at the price sits below 10%.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts only: $663M of floating-rate bank debt maturing mostly on 2029-08-01 ($566M in FY2029, Note 9),
covenants of net leverage at most 3.25 and interest cover at least 3.00, substantially all domestic assets pledged; the
whole-business criterion "Businesses earning good returns on equity while employing little or no debt" **[R1997-001]**
would be read here.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** The draft would have the buyer do nothing.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
Not asked. Window, door and cabinet components; none of the businesses the rows name.

---
## THE BOX
**OUT**, at **Q2**: the castle is shown open by the filer's own account of price competition, OEM bargaining power and
vertically integrating customers, held for fifteen years, by a seventeen-year operating margin averaging about 4% before
impairments that sits below its customer type and far below the branded maker, and by four write-downs of purchased
goodwill. Not reached as a judgment, recorded as COMPUTATION: NOT A CLEARANCE: value range $28.51 to $34.25 (whole-cycle
variant $23.08 to $27.73), fair price $16.13 on equity ($13.06 whole-cycle; $6.10 to $8.53 on equity plus net debt), cheap
price $8.71, against $18.91.

## SELF-AUDIT
- [ ] Copied to the dated file before any fetch: **yes** (the template was copied before the first EDGAR request).
      Written question by question: **no**; the reading was done first and the file was written in one pass after it,
      in question order. The value figures were computed in the working folder (`compute.py`) before the file was
      written; the Q2 verdict rests on the filing facts and the margin record, not on them, but the order was not the
      pre-registered one. Committed after each: **no**;
      the dispatching instruction forbade commits. Write-early was therefore not kept, and is confessed here.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`); every filing fact has its accession; no
      number without a row, a filing, or a CONVENTION label (the run's own: the whole-span growth substitute, the 21% tax
      on interest, the 15% cheap rule).
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; Q3 and Q7 figures carry the COMPUTATION
      label; Q4 to Q6 and Q9 record facts only, without verdicts.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): OCF less all capex less equity-settled
      stock pay, cash-settled stock pay already inside OCF; the sovereign from the U.S. Treasury; the price quote flagged as
      an aggregator's.
- [x] Contrary evidence was written down as it was found ("write it down in the first 30 minutes" **[M1997-127]**), five items, and answered at Q2.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): the run is dated today; not a
      point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its SBC line was corrected for FY2023-2024 from
      the filed cash-flow statement (see Step 0).
- [x] `python tools/check_framework.py` PASS before finishing (no commit made, by instruction).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Bought growth in the Q7 convention.** The convention carries "the growth the business has actually shown" over the
five years, measured on aggregate owner cash and "capped by the growth arithmetic of Q3". Here the five-year growth (17%) was
bought with an acquisition paid in shares and debt; Q3's cap forbids the absurd result but gives no rate to put in its
place. I used the whole-span growth (2.3%) and confessed it as a convention of this run; a rule is wanted (organic growth, or
growth net of the capital put in). (2) **Leverage changes inside the window.** Owner cash is after interest; three of the
five years carried almost no debt and the last two carry $50M of interest a year, so the five-year equity figure overstates
today's owner cash. The convention says nothing of whether the floor applies to equity or to equity plus net debt, and Q9's
"value it as if it had no debt" sits in a question this run did not reach. I gave both bases; the gap between them ($16.13
against $6.10) is large enough that the framework should choose. (3) **A whole made of parts with different castles.** The
holding-company rule reads a holding company by its parts (Q1), but an operating company with one segment that may have a
niche (spacers) and others that plainly do not (hardware at 0% for nine months) has no stated rule; I judged the whole, as
bought. (4) **"Pre-tax" in the floor.** The floor is "about ten percent pre-tax", but owner cash is after corporate tax; I
counted after-corporate-tax owner cash as the buyer's pre-tax return, which is the less strict reading of the two, and said
so. (5) **Facts found after the closing STOP.** The template marks Q3 to Q10 NOT REACHED but has no place for strong
evidence found later (the cash-flow material weakness, the auditor dismissal, the class action); I recorded them as facts
without verdicts under the questions that own them, so that a later look does not have to find them again. (6) **Tool
note.** `tools/run.py` takes the stock-pay figure from an expense tag that includes cash-settled liability awards in
FY2023-2024 and from the cash-flow add-back in FY2025, so its stock-pay column is inconsistent across years for this filer. (7) **The heading of operator rule 3.** The protocol prints "COMPUTATION" and "NOT A CLEARANCE" joined by an em dash; the standing rule against em dashes in this run's instruction made me write "COMPUTATION: NOT A CLEARANCE". The words are the protocol's; only the mark differs.
