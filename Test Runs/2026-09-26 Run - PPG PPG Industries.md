# Company Run — PPG Industries, Inc. (PPG) — 2026-09-26
**WAVE 7 name 44 of 218. Claimed at dispatch 2026-09-26 ~02:45 by an unattended run agent (claim commit `36ddb81f`). RESULT: Q1 IN, Q2 OUT (on the business); the file closed at Q2.**

**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.49%** · date **09/25/2026** (the newest row on the curve when struck, ~02:50 on 2026-09-26) · source (issuing authority) **US Treasury daily par yield curve, 30 Yr**, struck fresh for this run by `strike.py`; raw CSV saved as `Test Runs/_research 2026-09-26 PPG/treasury_2026.csv`. Prior rows 5.47% (09/24) and 5.40% (09/23). **Not inherited from any brief or run; FRED not used.**
- FX: PPG reports in US dollars and is quoted in US dollars on the NYSE. About two-thirds of 2025 sales were outside the US and Canada (FY2025 10-K, net sales by region: US and Canada $5,372M, EMEA $5,368M, Asia Pacific $2,937M, Latin America $2,198M, of $15,875M), so most earnings are translated from euros, pesos and other currencies. The filer states *"the Company generally purchases raw materials, incurs manufacturing costs and sells finished goods in the same currency"*. The reporting currency and the quote currency are the same, and the sovereign is struck for the reporting currency. No ADR.

**Registrant.** CIK 0000079879, PPG INDUSTRIES INC, Pennsylvania (incorporated 1883), fiscal year to December 31, Pittsburgh.

**Price, shares, cap.**
- Price **$107.52**, NYSE close **2026-09-25**, Yahoo chart endpoint (aggregator, live quote only, **flagged**); raw response saved as `price_raw.json`. Prior closes 106.32 (09/24), 107.20 (09/23).
- Shares **222.3 million** common, from the **cover of the 10-Q for the quarter to 2026-06-30, filed 2026-07-29, accession `0000079879-26-000252`**: *"As of June 30, 2026, 222.3 million shares of the Registrant’s common stock, par value $1.66 2/3 per share, were outstanding."* The cover rounds to a tenth of a million (plus or minus about $5M of cap at this price); the last exact count is the 10-K cover, *"As of January 31, 2026, 223,494,714 shares"*. One class. **`python Screens/cover_shares.py PPG` found the right filing and returned "NO COVER SHARE COUNT PARSED - read the filing by hand"**, which was done (tooling note below).
- **Market cap $23,901.7M** (107.52 x 222.3M). `tools/run.py` used 222.9M (the dei count at 2026-03-31) for $23.97B; the difference is 0.3%.

**The screen's cap flag, resolved: NEITHER figure is wrong; they are struck on different dates.** The screen set a cap of $25,436M (about $114 a share on 222.9M shares, a price from late August or early September 2026) against the 10-K's *"aggregate market value of common stock held by non-affiliates as of June 30, 2025, was $ 25,642 million"*. PPG closed at **$113.75 on 2025-06-30**, and $25,642M / $113.75 = **225.4M shares**, which is what PPG had outstanding in mid-2025 (weighted average 226.8M in Q2 2025, 10-Q). The 10-K cover repeats the test on its own date: $25,824M of float at 2026-01-31 against 223,494,714 shares is $115.55 a share, and the close on 2026-01-30 was $115.63. So non-affiliates hold essentially every share, and a cap struck fourteen months later, after the price moved from $113.75 to $107.52 and about 3M shares were retired, can sit below a float struck on an earlier date. The screen's flag compares numbers from two dates as though they were one; it is a tooling observation, not a data error.

**Newer than the screen row.** The row's newest periodic is 2026-03-31; **EDGAR carries a 10-Q for 2026-06-30** (above), read for this run. 8-Ks since the FY2025 10-K: 2026-04-15 (Item 2.02, Q1 release), 2026-04-21 (Items 5.02, 5.07: annual meeting, MSU award form), 2026-04-28 (Item 2.02, and Item 5.02: Jamie A. Beggs to join as CFO on 2026-07-06 on the retirement of Vincent J. Morales, announced 2025-11-28), 2026-07-28 (Item 2.02, Q2 release). Before the 10-K: 2025-11-03 (Items 1.01, 2.03: $700M of 4.375% notes due 2031), 2025-12-11 (a director). **No merger, tender, spin-off or sale agreement appears in any filing since the FY2024 10-K.**

**deal_note, opened: EMPTY BECAUSE NOTHING IS DEAL-SHAPED, and the quote is not a spread.** The portfolio moves are all completed and filed: the **US and Canada architectural coatings business sold to American Industrial Partners on December 2, 2024** (*"PPG received $ 516 million in proceeds and recorded a loss on the sale of $ 285 million"*, FY2024 10-K), the silicas products business sold in Q4 2024 (a $129M gain), the remaining Russian business held for sale at 2024 year-end (a $146M impairment) and later sold, and in H1 2026 **$145M of business acquisitions** (10-Q cash-flow statement; *"Acquisitions (+3%)"* in Performance Coatings in the Q2 release), 0.6% of the cap. PPG is the seller or the buyer in each, never a target, and nothing is pending.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (Note 3 working capital, Note 10 borrowings, Note 15 contingencies read in the 10-K text; the discontinued-operations note of FY2024 for the US and Canada sale)
- **10-K for FY2025, filed 2026-02-19, accession `0000079879-26-000046`** (Items 1, 1A, 7, 8); **10-Q for the quarter to 2026-06-30, filed 2026-07-29, accession `0000079879-26-000252`**; for the series, 10-Ks FY2024 `0000079879-25-000034`, FY2023 `0000079879-24-000040`, FY2022 `0000079879-23-000007`, FY2021 `0000079879-22-000009`, FY2020 `0000079879-21-000008`, FY2019 `0000079879-20-000008`, FY2017 `0000079879-18-000010`, FY2016 `0000079879-17-000009`, FY2014 `0000079879-15-000009`; DEF 14A filed 2026-03-05 `0000079879-26-000088`; the 8-K EX-99 releases of 2026-01-27, 2026-04-15 and 2026-07-28.
- **Figure cross-checked against the filed statement:** FY2025 *"Cash from operating activities - continuing operations 1,936"* and *"Cash from operating activities 1,941"* in the filed Consolidated Statement of Cash Flows. `tools/run.py` reads **1,941** (the total, including $5M from discontinued operations) and pairs it with continuing-operations capex of $778M. For FY2023 it reads 2,411, of which **$117M is the discontinued US and Canada architectural business** (continuing: 2,294). The tag agrees with the statement; the perimeter it mixes is recorded below as a tooling defect.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language.** PPG buys resins, solvents, titanium dioxide, pigments, epoxy and additives (*"Raw materials represent PPG’s single largest production cost component"*), mixes them in plants on four continents into paint, coatings, sealants and a few specialty materials, and sells them three ways. (1) **Global Architectural Coatings**, $3,838M of 2025 sales, segment income $599M (15.6%): house paint in Europe, Mexico and Asia Pacific (Comex, Sigma, Tikkurila, Johnstone's and others) sold through its own and concessionaire stores, home centres and dealers. (2) **Performance Coatings**, $5,513M, segment income $1,148M (20.8%): aircraft coatings, sealants and transparencies; car-repair paint sold through distributors to body shops; protective and marine coatings; road-marking paint (Ennis-Flint). (3) **Industrial Coatings**, $6,524M, segment income $875M (13.4%): paint applied in customers' own factories, on car bodies, appliances, equipment and the insides of cans, often under contracts whose price is tied to a raw-material index (*"lower index-based selling prices for certain customer contracts"*, FY2025 MD&A). Selling and administration took 21.7% of 2025 sales, R&D 2.8% ($446M). Pretax income from continuing operations was **$2,045M**; operating cash from continuing operations **$1,936M**; capital spending **$778M**. Revenue moves with volume in the served markets, currency (two-thirds of sales are outside the US and Canada), and price actions that the company itself describes as covering cost: *"In the second quarter we covered about 90% of the cost of goods sold inflation and expect to cover 100% by the fourth quarter"* (CEO, Q2 2026 release).
- **The scarce input this business controls.** Formulations and the approvals that go with them: an aircraft coating or sealant is specified by the airframe maker, an OEM line coating is qualified onto the customer's paint shop, a can coating onto the canmaker's line, a refinish system into the body shop's mixing equipment and colour database (*"PPG LINQ subscriptions and PPG Moonwalk installations"*). In architectural paint, brands and a store and concessionaire network (Comex in Mexico). The registrant claims no raw material that others cannot buy: supply is managed *"by establishing contracts with multiple sources and identifying alternative materials"*. Whether these positions are a franchise is Q2's question.
- **Will the fundamentals look broadly the same in ten years?** The chemistry and the channels are old and slow: PPG has sold coatings since the nineteenth century, raw materials are the same classes named in the FY2014 10-K, and R&D has held at 2.7-2.8% of sales. **The perimeter has not been stable and the filings show it**: the glass businesses sold (2016-2017; *"Net proceeds from the sale of businesses"* $1,094M and $593M in those years' cash-flow statements), Transitions Optical sold (2014), commodity chemicals separated (2013), Comex bought (2014, part of $2,427M of 2014 acquisitions), Tikkurila, Ennis-Flint, Wörwag, Cetelon and VersaFlex bought (2021, $2,137M), and the US and Canada architectural business, which PPG built by buying Akzo Nobel's North American architectural business in 2013 (526 stores), sold in 2024 for $516M at a $285M loss. The company since 2017 has been a pure coatings company, and the way a coating earns money has not changed.
- **Relatively simple and stable in character [E3-31]?** Yes for the product and the economics, which I can write down without the company's language; the portfolio churn is a fact about capital allocation, taken at Q2 and Q3. **This is not [E4-46]'s months-of-study case**: the Q2 test turns on documents in hand.
- **VERDICT: [x] IN**: the money is made visibly, by formulating commodity inputs into specified or branded coatings sold to factories, body shops, contractors and consumers, with price set by cost recovery and by position in each niche. **IN is not a finding on the franchise.**
## Q2 — IS IT A FRANCHISE? **[E3-03]**

*Every PPG figure below is read from the filed statements and MD&A of the 10-Ks named at Step 0 (extractions `cf_*_flat.txt`, `bs_flat.txt`, `bridges.txt`, `roc_out.txt` in the research folder). Peer margin series from XBRL with one figure per peer checked against its filed statement; AkzoNobel from its own F-4/A filed with the SEC (below).*

**[E3-03], criterion by criterion.** *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no close substitute and; (3) is not subject to price regulation. The existence of all three conditions will be demonstrated by a company's ability to regularly price its product or service aggressively and thereby to earn high rates of return on capital."* The same 1991 passage gives the other class: *"In contrast, “a business” earns exceptional profits only if it is the low-cost operator or if supply of its product or service is tight"* **[E3-43]**.

- **(1) Needed or desired [x]: passes.** Every car body, aircraft, can, appliance and house is coated; $15,875M of 2025 sales.
- **(2) No close substitute [ ]: fails for most of the company, in the registrant's own words and in its own growth plan.**
  - 10-K FY2025, Item 1: *"The coatings industry is highly competitive and consists of several large firms with global presence and many firms supplying local or regional markets. PPG competes in its primary markets with the world’s largest coatings companies, most of which have global operations, and with many regional coatings companies."* **Price is named among the "Major Competitive Factors" in all three segments**, and each segment names its global competitors: Akzo Nobel, Hempel, Nippon Paint, Jotun and Sherwin-Williams (architectural); Akzo Nobel, Axalta, BASF, Hempel, Kansai, Jotun, Nippon Paint, RPM, Sherwin-Williams and 3M (performance); Akzo Nobel, Axalta, BASF, Kansai, Nippon Paint and Sherwin-Williams (industrial).
  - Item 1A: *"an increase in competition may cause us to lose market share or lose customers, adversely impacting our sales volumes, or compel us to reduce prices to remain competitive"*.
  - **The largest segment is priced by formula.** Industrial Coatings, $6,524M or 41% of 2025 sales, sells to car makers and other manufacturers under contracts with *"lower index-based selling prices for certain customer contracts"* (FY2025 MD&A); its price fell **3% in 2024 and 1% in 2025** as raw materials eased (segment bridges), and in Q2 2026 *"Price was flat for the quarter, following previous price declines, as we executed new pricing actions"* (release of 2026-07-28). A price that follows an input index down is a pass-through, not a franchise price.
  - **Customers move between suppliers, and PPG's plan depends on it.** FY2025 MD&A: *"share gains in both the packaging coatings business and the protective and marine business"*, *"share gains in Europe aided by expanding regional regulations"* (packaging), traffic *"market share gains across North America"*, automotive OEM *"PPG outperformed the market in the third and fourth quarters of 2025 driven by share gains"*; Q2 2026 release: *"we are delivering on previously communicated share gains in all three businesses"*. A customer that can be won from Akzo, Axalta or BASF can be lost to them; the substitutes are the other qualified suppliers.
  - **The company describes its price as cost recovery.** CEO, Q2 2026 release: *"Costs have risen for raw materials, energy, logistics and packaging across the coatings value chain. In the second quarter we covered about 90% of the cost of goods sold inflation and expect to cover 100% by the fourth quarter"*; 10-K FY2025: *"The Company will carefully monitor all costs during 2026 and assess the need for additional selling price increases."* That is [E4-37]'s measure read in the registrant's own terms: price is decided against cost, and success is stated as covering it.
- **(3) Not subject to price regulation [x]: passes.** No administered price; traffic-marking paint is sold into government tenders, which is a buyer, not a regulator.

**The demonstration clause, read on every consolidated revenue bridge from 2014 to 2025.** PPG publishes a price-versus-volume split each year, so the physical series exists here, which [E4-55] asks for:

| year | organic volume | selling price | 10-K |
|---|---|---|---|
| 2014 | +3% | +1% | FY2014 |
| 2015 | +1% | not named | FY2016 |
| 2016 | +1% | not named | FY2016 |
| 2017 | +1% | *"Slightly higher"* | FY2017 |
| 2018 | *"Slightly higher"* | +2% | FY2018 |
| 2019 | **-3%** | +2% | FY2019 |
| 2020 | **-10%** | +1% | FY2020 |
| 2021 | +5% | +5% | FY2021 |
| 2022 | **-3%** | **+11%** | FY2022 |
| 2023 | **-2%** | +5% | FY2023 |
| 2024 | **-1%** | not named (Industrial -3%) | FY2024 |
| 2025 | +1% | +1% | FY2025 |
| H1 2026 (Q2) | +2% | +2% | release 2026-07-28 |

- **Volume over twelve years: about minus 6 to 7%, compounded** (the named percentages, 2014-2025; the "slightly" years taken at zero to one point). **Price over the same years: about plus 30%**, of which **21 points came in 2021-2023**, the years the company was recovering raw-material inflation (the FY2022 segment text gives the reason: *"In 2022, all businesses within the Performance Coatings reportable business segment achieved higher selling prices consistent with our focus on mitigating raw material and other cost inflation"*). Outside that window price ran **0 to 2% a year, about the general rate of inflation**, including +2% and +1% in 2019 and 2020 when volume fell 3% and 10%. This is the Precision Steel shape [E4-55], mild: dollar sales held by price while physical volume slipped.
- **The price did not widen the spread.** Gross margin (sales less cost of sales before D&A; 2015-2022 from each year's own 10-K, 2023-2025 from the FY2025 10-K): 2015 44.4%, 2016 45.3%, 2017 44.4%, 2018 41.5%, 2019 42.9%, 2020 43.8%, 2021 38.8%, 2022 37.1%, 2023 40.4%, 2024 41.6%, 2025 41.3%. The perimeter moved under this series (the US and Canada stores until 2024, glass until 2017), so it is not relied on alone; it agrees with the CEO's own description: the 2021-2023 prices bought back the cost increase and did not carry the margin above where it had been.
- **Earnings on the capital the owner has put in, falling as capital was added.** EBIT (pretax from continuing operations plus interest expense less interest income) on capital (debt plus total equity less cash and short-term investments), each year from its own 10-K (`roc.py`):

| year-end | EBIT as filed | named one-offs inside it | capital incl. goodwill | return as filed | one-offs added back |
|---|---|---|---|---|---|
| 2014 | $1,553M | $317M debt refinancing charge | $8,107M | 19.2% | 23.1% |
| 2016 | $926M | $968M pension settlement | $7,466M | 12.4% | 25.4% |
| 2019 | $1,761M | $176M restructuring | $9,182M | 19.2% | 21.1% |
| 2022 | $1,494M | $278M impairment and restructuring | $12,371M | 12.1% | 14.3% |
| 2025 | $2,133M | $30M restructuring and impairment | $13,186M | 16.2% | 16.4% |

  **From 2019 to 2025 capital rose by about $4.0bn and EBIT before one-offs by about $0.2bn ($1,937M to $2,163M): roughly 6% pretax on the added capital**, against a 30-year Treasury of 5.49%. The perimeter changed under the comparison (glass and the US stores out, Tikkurila, Ennis-Flint and others in), so the figure is a rough reading, not a measurement; its direction does not depend on the perimeter, because every year of the series was bought or sold into. Business acquisitions paid in cash, from the cash-flow statements, sum to **about $8.7bn from 2012 to 2025** (2013 $983M, 2014 $2,113M, 2019 $643M, 2020 $1,169M, 2021 $2,137M among them) against **about $5.4bn of disposal proceeds**, and **sales were $15,360M in 2014 as filed and $15,875M in 2025**. [E2-44]'s second characteristic, dollar growth *"with only minor additional investment of capital"*, is not what these filings show.
- **Segment returns [E2-56]:** Performance Coatings earns the most (segment income 17.7% of sales in 2022, 19.9% 2023, 21.8% 2024, 20.8% 2025, FY2024 and FY2025 10-Ks, current perimeter), with aerospace coatings the growth line (*"double-digit percentage"* organic growth in 2025, backlog about $315M). Industrial Coatings earned 13.0% (2018), 14.1% (2019), 10.5% (2021), 9.2% (2022), 13.7% (2023), 13.4% (2024), 13.4% (2025). Architectural 17.3% (2024), 15.6% (2025). The company-level answer is the blend; the segment with the best position is about a third of sales.

**[E4-04] and [E4-23]:** no technology-rebuild dependence found (R&D a steady 2.7-2.8% of sales; coatings chemistry is not a race each generation) and no superstar dependence; neither is relied on.

**Direction [E4-32]:** margin up in 2024-2025 by selling the weaker pieces (the US and Canada stores, silicas, Russia) and by restructuring (*"anticipated annualized pre-tax savings of approximately $175 million"*); return on the owner's capital down from 21-25% (2014-2019, one-offs out) to 14-16% (2022-2025); volume down over twelve years. **Flat to narrowing.**

**THE COMPETITOR ROW — required [E3-28].** Same metric for every name: **(pretax income from continuing operations + interest expense) / revenue**, from each filer's XBRL (`peers.py`, `peers_out.txt`), one figure per peer checked against its filed 10-K. AkzoNobel files no 10-K; its IFRS operating income (before financing and associates, nearest to the same construction) is read from its **F-4/A filed with the SEC on 2026-06-18, accession `0001193125-26-275378`**, filed for its merger with Axalta.

| Company | 2016 | 2019 | 2021 | 2023 | 2025 | source, and the figure checked |
|---|---|---|---|---|---|---|
| **PPG** | 6.3% (pension settlement) | 11.8% | 11.5% | 11.9% | **14.4%** | 10-Ks above; 2025 pretax $2,045M, interest $241M, sales $15,875M in the filed statement |
| **Sherwin-Williams** | 14.8% | 13.0% | 13.0% | 15.3% | **16.1%** | 10-K FY2025 `0000089800-26-000008`: net sales $23,574.3M, income before income taxes $3,338.2M, interest expense $465.0M |
| **Axalta** | 6.4% | 11.0% | 10.7% | 11.0% | **14.1%** | 10-K FY2025 `0001628280-26-008008`: net sales $5,117M, income before income taxes $546M |
| **RPM** (fiscal years to May; the column is the year ending in the following May) | 6.9% | 9.2% | 10.4% | 12.3% | **12.5%** | 10-K FY2026 `0001193125-26-312142`: net sales $7,863,422K, interest expense $111.5M |
| **AkzoNobel** (IFRS operating income / revenue) | n/a | n/a | n/a | 9.6% | 11.5% (about 7.6% before €390M of "other results") | F-4/A: revenue €10,668M, €10,711M, €10,158M and operating income €1,029M, €917M, €1,164M for 2023, 2024, 2025 |

- **Peers named: 5 of the 10 companies the registrant names** (Sherwin-Williams, Axalta, RPM and AkzoNobel in full; PPG itself). **Not obtainable from SEC filings:** Nippon Paint and Kansai (Japanese; EDINET blocked by a paid key, the rung named in section II of the framework), Jotun and Hempel (Norwegian and Danish, privately held, file nothing with the SEC), BASF (German, files no 10-K; its coatings business is not separately filed), 3M (files a 10-K, but coatings are not a segment, so no like-for-like figure exists). **The verdict does not rest on the row**: it rests on the registrant's own statements under criterion (2), its own bridges and its own returns. The row is read for the attacker's test [E2-45].
- **What the row shows [E3-61]:** the one name in the field with a structural position the others lack, Sherwin-Williams (its own stores), earns 1.2 to 3.4 points more than PPG in every year shown (more in 2016, PPG's pension-settlement year). PPG sits with Axalta, which is being bought by AkzoNobel (0.3 to 1.1 points apart), level with or ahead of RPM (ahead by up to 2.6 points, behind by 0.4 in 2023), and ahead of AkzoNobel. AkzoNobel's own F-4/A describes the market PPG faces: 2025 *"organic sales flat as volume decreased and fully offset positive pricing impacts"*. A second-tier position in an oligopoly whose members win and lose accounts from each other.
- **Untapped pricing power [E3-33], [E5-28]:** not claimed and not visible; PPG is one of several global majors in every segment, not a near-monopoly.
- **[E2-53], the dominance test:** fails; no segment is described as dominant, and the company's growth plan is share taken from peers.
- **Class: [x] NONE at the company level** (a narrower position in aerospace coatings, whose sales the filings do not state separately, is recorded and does not carry the company) · **Direction: flat to narrowing.**

**THE STRONGEST EVIDENCE AGAINST THIS VERDICT, hunted hardest [E4-26, E3-41, E4-51].**
1. **Price rose in years volume fell** (2019 +2% on -3%, 2020 +1% on -10%, 2022 +11% on -3%, 2023 +5% on -2%). That is the literal form of [E2-44]'s first characteristic, *"increase prices rather easily (even when product demand is flat and capacity is not fully utilized)"*.
2. **The returns on the operating assets are high.** On capital net of goodwill and intangibles the returns above are 43% (2025), 75% (2019) and 99% (2014, 2016) pretax, and [E2-43] says the return on *"unleveraged net tangible assets [...] is the best guide to the economic attractiveness of the operation"*. Coatings are a small share of what they protect (an aircraft, a car body, a can), which is the structure that lets a supplier hold price.
3. **Performance Coatings is widening**: segment margin 17.7% (2022) to 20.8% (2025), aerospace growing at double digits with a backlog, refinish tied to body shops through mixing systems and software subscriptions.
4. **Two earlier runs of this framework judged coatings franchises IN**: Sherwin-Williams (WIDE at its stores, NARROW elsewhere) and RPM (NARROW, on 13-18% pretax on all capital), in files dated 2026-08-31. PPG's 2025 return on all capital (16.2%) is inside RPM's band and its operating margin is above RPM's.
5. **54 consecutive annual dividend increases** and dividends paid since 1899.

**Answered.** (1) The price rises in down-volume years were +1% and +2% in 2019-2020, about the general rate of inflation in those years, and the large ones (2022-2023) were bought back from raw-material inflation the CEO says the company is still trying to cover; [E2-44]'s test is price *"without fear of significant loss of either market share or unit volume"*, and the registrant's risk factor says the fear is present. The largest segment cuts price when its index falls. (2) High returns on tangible assets with 14-16% pretax on what the owner has paid, and about 6% on the capital added since 2019, is [E2-43]'s distinction and [E2-56]'s camouflage: the operations are attractive, the owner's capital has been deployed into them at a price that leaves ordinary returns, and [E2-73] judges the operators on the first figure, not the business. (3) A third of the company widening while the largest segment is index-priced is a segment finding [E2-56]; the unit of the test is the company [E4-08]. (4) **This file and the RPM file read comparable total-capital returns differently, and the difference is recorded rather than smoothed**: RPM publishes no price-versus-volume split (its run carried that as a defect), PPG publishes one every year, and the published split shows twelve years of flat-to-falling volume and price at about the rate of inflation outside a cost-recovery window. A reader who weighs the 12-19% pretax band as the RPM run did would class PPG NARROW; the corpus's own demonstration clause asks for price taken *"aggressively"* and returns that are *"high"*, and neither is in these filings. The inconsistency is carried to the fold for the operator, not resolved by preference. (5) A dividend record shows a durable company, which is Q4's question, not Q2's.

- **VERDICT: [x] OUT**: on the business. **[E3-03] criterion (2) fails for most of the company in the registrant's own words** (*"highly competitive"*, price a major competitive factor in every segment, competition able to *"compel us to reduce prices to remain competitive"*), in its pricing mechanism (41% of sales index-priced, price cut in 2024 and 2025 as inputs fell), and in its own growth plan, which is share taken from the same named rivals. **The demonstration clause fails on the company's own bridges**: twelve years of flat-to-falling volume, price at about the rate of inflation outside a cost-recovery window the CEO describes as covering cost, and a return on the owner's capital that fell from 21-25% to 14-16% pretax while about $8.7bn of acquisitions were paid for. PPG is [E3-43]'s *"a business"*: a competent, well-run member of a coatings oligopoly, earning ordinary returns on what it cost, with one narrower position (aerospace) inside it. **The file closes here.** Q3 to Q6 are not opened as gates; the material gathered beneath the close follows without verdicts.
## MATERIAL BENEATH THE CLOSE: recorded, not governing

*The file closed at Q2, OUT on the business. What follows is recorded the way the BDC, USPH, HUBG and CAH runs recorded
theirs: no verdict box is ticked for Q3-Q6, nothing here reopens Q2, and nothing here is a clearance. It is written
down because the brief asked for it (the screen row's claims to be refuted) and because a later re-look should not
have to fetch it again.*

### Q3 prompts (no verdict)

- **Weight case, as it would be declared.** Q2 found [E3-43]'s *"a business"*, and the same passage says such a business
  *"can be killed by poor management"*: daily execution would be ticked [E3-38]. Leverage: gross debt $7,308M and cash
  and short-term investments $2,219M at 2025 year-end (net debt $5.3bn at 2026-06-30, Q2 release); covenant ratio of
  Total Indebtedness to Total Capitalization 47% against a 60% limit (10-K). Not ticked as a gate on its own. Control:
  no.
- **[E4-29] fires in the filings and the releases.** The 10-K's own MD&A reports *"Segment income before interest, taxes,
  depreciation and amortization (EBITDA)"* for every segment, and the Q4 2025 release leads with *"Segment margin of 17%
  and segment EBITDA margin of 19%"* and publishes *"Adjusted EBITDA"* and *"Adjusted EBITDA margin"* ($2,749M, 17.3% for
  2025). The depreciation removed is not small: capex ran at **1.9-2.0 times the depreciation line in 2024-2025**
  ($721M and $778M against $360M and $403M). The amortization exclusion from adjusted EPS ($0.41 a share in 2025) is a
  different matter: [E2-43] itself says amortization of purchased goodwill *"should be ignored"* in judging the
  operation, so it is not scored here.
- **[E3-53] / [E5-33], the restructuring charge, fires as a series.** A business-restructuring charge appears in the income
  statement in **eleven of the fourteen years 2012-2025** (2012 $176M, 2013 $98M, 2015 $140M, 2016 $197M, 2018 $66M,
  2019 $176M, 2020 $174M, 2021 $31M, 2022 $33M, 2024 $233M, 2025 $6M; about $1.3bn in all), and each is removed from
  adjusted EPS. A cost that recurs in eleven years of fourteen is an operating cost; the owner-earnings figures below
  keep it (they start from operating cash, which pays it).
- **[E4-27], what pay vests on (DEF 14A filed 2026-03-05, `0000079879-26-000088`).** Annual bonus: *"adjusted earnings per
  diluted share from continuing operations (weighted 50%), adjusted cash flow from operating activities (weighted 20%),
  and organic sales growth (weighted 30%)"*; the EPS used adds back amortization, restructuring, environmental,
  impairment and tax items and *"one half of the earnings impact (positive or negative) of foreign currency translation
  versus plan"*. Long-term: three equal parts, stock options, TSR shares against the S&P 500 (the 2023-2025 grant paid
  **0%** at the 19th percentile), and performance RSUs on adjusted EPS growth (100% at 10% a year) and **an 11% "cash flow
  return on capital"**, which the company reports at **15.4% (2023), 12.6% (2024), 10.0% (2025)**: its own return
  measure fell below its own bar in 2025. **Nothing vests on a return on capital that includes what acquisitions cost
  in the way Q2 measured it.** Organic sales growth at 30% of the bonus pays for volume and price, including price taken
  to cover cost.
- **[E4-22] third flag / [E3-48]: projections are a practice.** Quarterly guidance; a full-year adjusted EPS range
  (*"Reaffirming full-year 2026 adjusted EPS guidance range of $7.70 to $8.10"*, 2026-07-28); an April 15, 2026 release
  whose headline is *"PPG expects first quarter 2026 financial results to exceed previous guidance"*. Against its own
  2025 plan (the bonus target, $7.90 adjusted EPS, 3.3% organic growth) the outturn was $7.58 reported adjusted ($7.45 on
  the committee's measure) and 2.0%.
- **[E2-30] (2), [E2-56], [E4-39]: capital allocation on the record.** About $8.7bn of acquisitions 2012-2025 and $5.4bn of
  disposals (Q2). The US architectural position was built by buying Akzo Nobel's North American architectural business in
  April 2013 (526 stores; 2013 acquisitions paid $983M) and **sold with the rest of the US and Canada business on
  2024-12-02 for $516M at a $285M loss**; Tikkurila was bought in 2021 for *"$ 1.7 billion, net of cash acquired"* with
  *"goodwill of $ 1.1 billion"*. No post-mortem of either against its announcement case was found in the documents read
  (the 10-K records the loss). **Buybacks [E5-08]:** $790M for 6.9M shares in 2025 (about $114 a share) and $752M for
  5.8M in 2024 (about $130), against the no-growth values in the computation below ($43-64 a share at the ~10% floor,
  $78-117 at the sovereign), which is a capital-allocation flag on condition (2), stated with the humility clause
  [E4-13]: management knows the business better than this file does. Condition (1) is met (the dividend has been
  paid since 1899 and raised 54 years running, and the revolver is undrawn).
- **The candor read [E2-26].** The 10-K reconciles every adjusted item separately, line by line, with tax effects, and
  publishes a price-versus-volume bridge for the company and each segment every year: **the half-owner test passes on the
  disclosure itself**, and this file's Q2 could only be written because of it. No finding of personal misconduct in any
  document read [E5-16]; a pass here would be the absence of a found disqualifier, not a finding of honesty [E5-17].
- **Tells [E4-30], [E5-15]:** cash taxes paid against pretax income 21% (2019), 32% (2022), 29% (2023), 35% (2024), 21%
  (2025), no falling trend; weighted average shares fell from about 237M (2019, net income $1,243M at $5.25 basic) to 223.0M (Q2 2026) and the cover count to 222.3M, no serial issuance.

### Q4 prompts: owner earnings the corpus's way [E2-23], every window [E4-25]

**Construction.** Operating cash flow from continuing operations (the latest 10-K that shows each year), less the
stock-compensation line, less the non-controlling interests' share of continuing income, less (c) at two ends: **full
capital expenditure** and **the income statement's "Depreciation" line** (D&A less the amortization of acquired
intangibles, which the 10-K's own reconciliation calls *"Acquisition-related amortization expense"*; the brief's
question whether acquired amortization sits inside the D&A capex end is answered yes, $107-172M a year, and it is taken
out of this end). No net-income proxy anywhere (operator rule 5). (c) is a guess [E2-09]; depreciation is the corpus
default [E3-44], and PPG is not in the [E5-20] class (capex ran 0.8-1.7 times depreciation 2012-2023; the 1.9-2.0 times of
2024-2025 is named by the filer as *"modernization and productivity improvements, expansion of existing businesses"* and
guided down to *"$650 million to $700 million"* for 2026). Inputs in `oe.py`; output `oe_out.md`.

**SBC resolves and is complete.** The cash-flow line equals the note's *"Total stock-based compensation"* ($46M, $42M,
$56M for 2025-2023). The savings-plan match (*"Compensation expense and cash contributions related to the Company match
[...] $ 38 million , $ 52 million and $ 49 million"*) is paid in cash and so is already inside operating cash; no stock
is contributed to a plan outside the SBC line. SBC is 2-5% of operating cash: immaterial to any conclusion, and at the
[E3-70] grant-value measure (options granted at $32.93-43.83 fair value a share in 2023-2025; TSR awards of 76,925
contingent shares at $114.39 grant-date fair value in 2025) no larger in any way that moves a figure.

**Non-controlling interests: present and small.** Continuing income attributable to NCI $16-39M a year 2022-2025
(total NCI equity $156M); subtracted every year. The brief's USPH finding does not bite materially here: it moves the
mean by about $20-30M.

**By year ($M):**

| FY | 10-K | OCF | SBC | NCI | capex | depreciation line | OE, c = capex | OE, c = depreciation | acquisitions paid | disposals | noted inside OCF |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2012 | FY2014 | 1,410 | 71 | 17 | 330 | 292 | 992 | 1,030 | 122 | 0 | |
| 2013 | FY2014 | 1,562 | 81 | 23 | 494 | 333 | 964 | 1,125 | 983 | 940 | |
| 2014 | FY2016 | 1,718 | 71 | 24 | 564 | 324 | 1,059 | 1,299 | 2,113 | 1,625 | |
| 2015 | FY2016 | 1,735 | 54 | 21 | 454 | 339 | 1,206 | 1,321 | 320 | 47 | pension contributions $273M |
| 2016 | FY2016 | 1,241 | 39 | 22 | 402 | 341 | 778 | 839 | 349 | 1,094 | asbestos settlement funding $813M; pension contributions $204M |
| 2017 | FY2019 | 1,551 | 35 | 21 | 360 | 331 | 1,135 | 1,164 | 225 | 593 | |
| 2018 | FY2019 | 1,487 | 37 | 17 | 411 | 354 | 1,022 | 1,079 | 378 | 0 | |
| 2019 | FY2019 | 2,084 | 39 | 26 | 413 | 375 | 1,606 | 1,644 | 643 | 0 | |
| 2020 | FY2022 | 2,130 | 44 | 15 | 304 | 371 | 1,700 | 1,767 | 1,169 | 0 | total OCF, US and Canada stores inside |
| 2021 | FY2022 | 1,562 | 57 | 21 | 371 | 389 | 1,095 | 1,113 | 2,137 | 47 | total OCF, US and Canada stores inside |
| 2022 | FY2024 | 1,000 | 34 | 28 | 486 | 357 | 452 | 581 | 114 | 117 | |
| 2023 | FY2025 | 2,294 | 56 | 39 | 516 | 360 | 1,683 | 1,839 | 109 | 36 | |
| 2024 | FY2025 | 1,391 | 42 | 33 | 721 | 360 | 595 | 956 | 31 | 831 | |
| 2025 | FY2025 | 1,936 | 46 | 16 | 778 | 403 | 1,096 | 1,471 | 1 | 43 | |

No year sits near or below zero; the low is **2022, $452-581M** (inventory and receivables built $425M in the
raw-material inflation), and working capital swings of $300-500M move single years by a third, which is why no single year
is used [E2-23].

**Every window ending 2025, and two earlier ones, on the cap of $23,901.7M:**

| window | OE mean, c = capex | OE mean, c = depreciation | yield on cap | acquisitions paid a year |
|---|---|---|---|---|
| 3y 2023-2025 | $1,125M | $1,422M | 4.71-5.95% | $47M |
| 4y 2022-2025 (the clean perimeter, US stores out) | $956M | $1,212M | 4.00-5.07% | $64M |
| **5y 2021-2025, the default [E2-42]** | **$984M** | **$1,192M** | **4.12-4.99%** | $478M |
| 6y 2020-2025 | $1,104M | $1,288M | 4.62-5.39% | $594M |
| 7y 2019-2025 | $1,175M | $1,339M | 4.92-5.60% | $601M |
| 8y 2018-2025 | $1,156M | $1,306M | 4.84-5.47% | $573M |
| 9y 2017-2025 (pure coatings since glass left) | $1,154M | $1,290M | 4.83-5.40% | $534M |
| 10y 2016-2025 | $1,116M | $1,245M | 4.67-5.21% | $516M |
| 11y 2015-2025 | $1,124M | $1,252M | 4.70-5.24% | $498M |
| 12y 2014-2025 | $1,119M | $1,256M | 4.68-5.26% | $632M |
| 13y 2013-2025 | $1,107M | $1,246M | 4.63-5.21% | $659M |
| 14y 2012-2025, every filed year read | $1,099M | $1,231M | 4.60-5.15% | $621M |
| 5y 2016-2020 | $1,248M | $1,299M | 5.22-5.43% | $553M |
| 5y 2012-2016 | $1,000M | $1,123M | 4.18-4.70% | $777M |

**Combined range across every window and both ends: $956M to $1,422M (4.0% to 5.9% on the cap).** The windows agree
with each other to within about 15% on either end, a narrow spread; what is wide is the capex band in the latest
three years, because capex doubled against depreciation. **Owner earnings have not grown in fourteen years**: $1.0-1.1bn
in 2012-2016, $1.1-1.3bn over the latest decade, while about $8.7bn was paid for acquisitions and $5.4bn received for
disposals. That is the Q2 finding in cash.

**The screen row, refuted or confirmed.** *oe_bottom $1,014M / oe_top $1,314M*: near this file's 5-year $984-1,192M and
3-year $1,125-1,422M; the screen used total operating cash (FY2023 includes $117M from the discontinued US and Canada
business) and subtracted no NCI. *acq_note "$2,392M, 9% of cap, inside the window"*: **confirmed** as a sum of five
outflows (2021 $2,137M, 2022 $114M, 2023 $109M, 2024 $31M, 2025 $1M), not an absolute-value artifact this time, but
**incomplete**: it names no disposals, and $1,074M of disposal proceeds (continuing and discontinued) came in over the
same five years. *deal_note empty*: confirmed at Step 0. *spread_caveat, "CANNOT see variation older than the 5-year
window"*: rebuilt over every window 3 to 14 years; the older windows do not change the picture. *cap_flag*: resolved at
Step 0 as a two-date comparison.

**Staying power [E5-11], scored as it would be.** (1) Operating cash of $1.0-2.3bn in every year 2012-2025. (2) $2,219M
of cash and short-term investments at 2025 year-end, $1.6bn at 2026-06-30; an undrawn $2.3bn revolver (counted as
nothing [E5-39]). (3) Debt due $702M in 2026 and $2,725M in 2027-2028 (the $1,233M euro term loan, extended in January 2026 to January 2029),
interest $241M against EBIT of $2,133M (about 9x) [E2-54]; pensions accrued $550M and other postretirement $392M;
environmental reserves $206M with $100-200M more *"reasonably possible"*; asbestos claims against a subsidiary acquired
in 2013 still pending. No near-term requirement is out of proportion to operating cash.

**The named death, as a signature only: #11 THE PASS-THROUGH** (the company lives; price follows cost, in the largest
segment by contractual index, and the owner's return on added capital compresses toward the bond rate), **with [E2-56]'s
camouflage as a feature** (a steady core paying for $8.7bn of acquisitions that left owner earnings where they were). Not
entered in the index's instances column (the file closed at Q2); no new shape.

### COMPUTATION — NOT A CLEARANCE

*Arithmetic only, produced after the file closed at Q2; it carries no entry language and no box (operator rule 3).*
- **Yield**: 4.0-5.9% on the $23,901.7M cap across every window and both (c) ends (5-year 4.1-5.0%), against the 5.49%
  Treasury and the ~10% floor [E4-28].
- **No-growth value** (owner earnings / rate): at 10%, $9.6-14.2bn, **about $43-64 a share**; at the 5.49% sovereign,
  $17.4-25.9bn, **about $78-117 a share**; the quote is $107.52.
- **What the price needs to reach the floor**: about 4-6 points a year of perpetual owner-earnings growth, from a
  business whose owner earnings have not grown in fourteen years and whose volume has not grown in twelve; nominal price
  at about the rate of inflation would supply part of it and has not, so far, appeared in owner earnings. The [E4-35] base
  rate governs any claim to more.
- **Windage count**: one (the conservative end is reported beside the other, not stacked).

### Q6: reversal conditions, in words (no alert: the file failed on the business)

*No price band is armed and no PORTFOLIO.md row is written (the QLYS ruling: a Q2 failure is about the business).* What would
reopen Q2, from filings: **(1)** organic volume growing across a cycle while price stays positive in years when the
industrial index falls, i.e. price that does not follow cost; **(2)** the return on the owner's total capital (as
constructed in Q2) rising back above its 2014-2019 level of 21-25% pretax without a disposal doing it; **(3)** the
Industrial Coatings segment moving off index-based contracts; **(4)** a segment disclosure showing aerospace coatings large
enough, and earning enough, to carry the company (a filing that states its sales and income separately).

## Q5: not opened. Q6: not opened as a gate (reversal conditions in words above).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT**; the file closed at Q2; Q3-Q6 recorded beneath
      the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on the filings named.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued.
- [x] Step 0: the filing was read, with accession number (10-K FY2025 `0000079879-26-000046`, 10-Q Q2 2026
      `0000079879-26-000252`, and the series); a figure was cross-checked (FY2025 operating cash $1,936M continuing /
      $1,941M total in the filed statement against the tag).
- [x] Owner earnings on a multi-year mean; every window 3 to 14 years stated; capex band disclosed as a judgment; SBC and
      NCI subtracted; no net-income proxy.
- [x] Competitor row filled from the registrant's own named competitors, identical construction, one figure per peer
      checked against its filing; the five named competitors not obtainable from SEC filings are named with the reason;
      the verdict is stated not to rest on the row.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (US Treasury, 30 Yr, 09/25/2026, 5.49%).
- [x] Value stated as a round-number range, not a point estimate (in the computation only; Q5 not opened).
- [x] One bar chosen, not both; windage count stated: n/a at Q5 (not opened); the computation's windage count is one.
- [x] Prices dated; aggregator used for live quotes only and flagged (Yahoo chart endpoint, close 2026-09-25).
- [x] Run committed to git (claim `36ddb81f`; Step 0 and Q1 `409cca3b`; Q2 `97c5f93f`; this section and the register in
      the next commit).
- [x] **Every ledger id cited in this file resolved against `principle_ledger.csv`** by script before the commit.
- [x] **The strongest evidence against the verdict is recorded and answered** [E4-26], including the inconsistency with
      the RPM run of 2026-08-31, which is carried to the fold for the operator rather than resolved here.

**Tooling defects, reported, not patched.**
1. **`Screens/cover_shares.py`** found the right filing (the 10-Q of 2026-07-29) and returned *"NO COVER SHARE COUNT
   PARSED - read the filing by hand"*: the cover states the count in words and in millions (*"222.3 million shares"*),
   which the parser's header-units logic noticed (*"shares in Millions"*) but did not read.
2. **`tools/run.py`** reads total operating cash (`NetCashProvidedByUsedInOperatingActivities`, which includes
   discontinued operations: $117M in FY2023, $29M in FY2024) and pairs it with continuing-operations capex, a mixed
   perimeter; it subtracts no non-controlling interests; and it prints *"GROWTH THE PRICE ASSUMES -9.2%"* for a yield of
   5.03-5.69% against a 5.49% rate without saying which owner-earnings figure produced the sign. Not used.
3. **The screen's `cap_flag`** compares a cap struck at a 2026 price with a float struck at the 2025-06-30 price and calls
   one of them wrong; both were right at their dates (Step 0).
4. **The screen's `acq_note`** sums acquisitions and never nets or mentions disposals ($1,074M received inside the same
   five-year window), so "9% of cap" overstates the net capital put into purchases over the window.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **FAIL at Q2 (OUT, on the business).** A member of the coatings oligopoly whose price, in the registrant's
  own words, recovers cost (41% of sales on index-based contracts, cut in 2024 and 2025), whose growth plan is share
  taken from the rivals it names, whose volume fell over twelve years of published bridges, and whose return on the
  owner's capital fell from 21-25% to 14-16% pretax while about $8.7bn of acquisitions left owner earnings at $1.0-1.4bn.
  Q1 IN. Price $107.52 (2026-09-25) x 222.3M shares (10-Q cover `0000079879-26-000252`) = $23,901.7M; sovereign 5.49%
  (Treasury 30Y, 09/25/2026).
- **If UNRESEARCHED — THE WORK ORDER:** n/a
- **If UNKNOWABLE:** n/a
