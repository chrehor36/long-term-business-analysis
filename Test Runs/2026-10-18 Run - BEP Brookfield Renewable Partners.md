# Company Run — Brookfield Renewable Partners L.P. (NYSE: BEP; TSX: BEP.UN) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure: the lines of
evidence and the competitor slot are derived by the analyst from the 20-F, not written by the dispatcher. Working folder:
`Test Runs/_research 2026-10-18 BEP/` (notes, the cite checker, the computation script; raw filings in the ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. **Filled at the fold, 2026-10-18, after the run was committed (4f664948):** not held; Brookfield Renewable Partners (BEP) does not appear in `PORTFOLIO.md`.

**Contamination, declared.** (1) A directory listing of `Test Runs/` filtered for "bep|brookfield", made at the start to
confirm no file of this name existed, showed the file names (not the contents) of other Brookfield-family runs: BAM
(2026-09-13), BN (2026-09-13, 2026-10-05 and research passes of 2026-10-05), and BIPC
(2026-10-17). None was opened; nothing in them is used. The listing itself was a search across `Test Runs/` of the kind
the blind rule forbids, made before I had weighed that clause; it is declared here as a breach of form. (2) The session
context showed recent commit subjects about BKH (an unrelated utility run) and the index lines of the operator's memory
files, which mention holdings and reviews in general and do not name BEP. Not used.

**The lines of evidence, chosen by the analyst (the brief's departure).** From the FY2025 20-F: Item 4.A and 4.B (the
portfolio, the contract profile, "Our Competitive Strengths", "Competition and Marketing", the acquisitions, asset sales
and financings of 2025 and early 2026), Item 3.D (risk factors, chiefly technology, power prices, the Brookfield
relationship and its conflicts, the tax structure), Item 5 (Part 4 proportionate segment results, Part 5 capitalization,
borrowings and cash flows, Part 9 the definitions of FFO and of proportionate information), Item 6 and Item 7.B (the
Master Services Agreement, the incentive distributions, the related-party transactions), and the audited statements with
Notes 7 (segments), 13 (PP&E at fair value, its discount rates and the historical-cost table) and 29 (related parties).
Why these: Item 4 is where the filer says what protects it and who it competes with (Q1, Q2); Item 3.D is where it names
what could break it (Q2, Q9); Item 5 and the notes are where the cash, the gains and the depreciation can be separated
(Q3, Q4, Q7); Items 6 and 7.B are where the managers are paid and conflicted (Q5, Q6).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $28.40 (BEP close 2026-10-16, the last trading day before this run; `tools/sources.py` price(), Yahoo
  chart API, **aggregator, flagged** under operator rule 5). BEPC exchangeable shares closed $28.67 the same day (same
  source, flagged); they are not used in the arithmetic.
- **Units by class** (the 20-F cover via `python Screens/cover_shares.py BEP`: LP units 305,987,962, plus four series of
  preferred units, FY2025 20-F filed 2026-02-27, accession `0001533232-26-000011`; the cover counts the LP units only).
  The per-unit base is taken from the latest interim report, the Q2 2026 6-K filed 2026-07-31 (accession
  `0001533232-26-000026`, Exhibit 99.1, "Shares, units and notes outstanding", June 30, 2026): LP units 300,111,626;
  Redeemable/Exchangeable partnership units (BRELP, held by Brookfield) 194,487,939; BEPC exchangeable shares and class
  A.2 exchangeable shares 185,599,260; total on a fully-exchanged basis 680,198,825; plus the GP interest of 3,977,260
  units. **Treatment:** the 20-F (Item 5, Part 9) says the LP units, BEPC exchangeable shares, class A.2 exchangeable
  shares and Redeemable/Exchangeable units "have the same economic attributes in all respects", each exchangeable one for
  one; they are counted as one class. The GP interest is counted with them, as the filer does for its own per-unit
  figures (Q2 2026 note: average units of 684.3 million "inclusive of ... GP interest"); its incentive distributions are a
  further claim on top of its units (Q5, Q6). **Per-unit base: 684,176,085 units.** Check against issued less
  repurchased: 305,987,962 LP units at 2025-12-31, less 5,994,833 repurchased for cancellation, plus 118,131 under the
  reinvestment plan and 366 issued on exchange, gives 300,111,626, as filed. The 5,994,833 LP units bought back match the
  5,994,833 BEPC exchangeable shares issued under the BEPC at-the-market programme in the same half (an exchange of one
  listed form for another, not a reduction). No 6-K after the interim changes the count by my reading of the 6-K list
  (the 2026-10-13 6-K, accession `0001171843-26-006567`, is the simplification meeting notice). Preferred units
  (32,000,000), class A preference shares of a subsidiary (31,035,967) and perpetual subordinated notes are senior claims
  and are not in the base.
- **Market cap:** 684,176,085 x $28.40 = **$19,431M**.
- **Sovereign for the earnings currency:** **5.43%**, the US Treasury daily par yield curve, 30-year, 10/16/2026
  (`python tools/sources.py`, issuing authority). Earnings currency judged US dollars: the filer reports and distributes
  in dollars; its earnings arise in US and Canadian dollars, euros, reais, pesos and others with no single non-dollar
  currency carrying most of them (hydro alone splits US, Canada, Brazil, Colombia), so no other issuing authority is
  better suited. The dollar choice is mine and is stated so.
- **Filings read** (operator rule 4): 20-F FY2025 (filed 2026-02-27, `0001533232-26-000011`); 20-F FY2024 (2025-02-28,
  `0001533232-25-000006`); 20-F FY2023 (2024-03-01, `0001533232-24-000005`); 20-F FY2022 (2023-03-01,
  `0001533232-23-000009`); 20-F FY2021 (2022-03-01, `0001533232-22-000007`); 20-F FY2019 (2020-02-28,
  `0001533232-20-000006`); 20-F FY2018 (2019-03-01, `0001171843-19-001411`); the Q2 2026 interim 6-K (2026-07-31,
  `0001533232-26-000026`); the 6-K of 2026-10-13 (`0001171843-26-006567`). BEP files no proxy statement; Items 6 and 7.B
  of the 20-F stand in for it. **Cross-check against the filed statement:** cash from operating activities FY2025 of
  $1,147M in the XBRL company facts equals the audited consolidated statement of cash flows (20-F FY2025, F-14); the
  cover LP unit count of 305,987,962 equals the Item 5 units table at 2025-12-31.
- `python tools/run.py BEP` returned "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (an IFRS 20-F filer).
  Every figure in this run is taken from the filed statements and notes; no line of `tools/run.py` is used.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this partnership "if the market closed for five
years" **[M1997-109]**, which turns on what the dams, farms and fees produce, not on the unit price. The market serves and
does not instruct **[M2006-077]**: the unit price is near the $29.90 at which the partnership itself sold 22,017,870 units
in November 2025 (20-F FY2025, Item 4.A), and that tells nothing about value. Who is paid to tell you **[M2020-037]** bears
hard here: the managers are employees of Brookfield, paid a fee that rises with the partnership's total capitalization
and an incentive distribution that rises with distributions (Item 7.B), so every figure the filer features is a figure its
manager is paid on; I read the audited statements first and the featured measures second. No macro view enters **[M2000-094]**:
the 20-F's case for growth is electrification, data centres and AI demand (Item 4.B), and none of it is used. Margin of
safety **[M1996-084]** is an arithmetic only at Q7. **Contrary evidence, written down as found** **[M1997-127]**: (1) the
featured "Funds From Operations" of $1,334M for 2025 includes $852M of "other income" that Note 7 says is "predominantly
associated with dispositions and monetizations of developed or non-core assets and businesses"; without it, FFO was $482M
in 2025 against $548M in 2024 and $683M in 2023, falling while the featured figure rose; (2) net income attributable to
Unitholders was negative in every year 2021 to 2025 (-$368M, -$295M, -$100M, -$464M, -$19M; Q4); (3) distributions to
Unitholders of $1,140M in 2025 exceeded FFO without the gains; (4) the hydro fleet, the largest part, earned less FFO in
2025 ($607M) than in 2021 ($668M); (5) the filer's hydro cash operating cost per MWh is above its own wind and solar (Q2).
Each is weighed where its question falls. Stating the other side's case as well as its holder would **[M2016-055]**:
the filer argues that IFRS depreciation on revalued assets far exceeds what must be reinvested, that development gains
are a recurring product of a development business, and that contracted, inflation-linked cash flows from irreplaceable
hydro grow per unit at 5% to 9% a year; that case is tested at Q3, Q4 and Q7, not assumed.

## THE STANDING RULE
Owning these units with the buyer's own money, unlevered and sized so that a fall of half or more could be borne, puts
the buyer at no risk of ruin; the rule binds the buyer's financing, not the target **[M2012-081]**, **[L2014-024]**. The
target's own debt and its calls on cash are Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The question.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**, asked by one who knows "where the perimeter
  is" **[M2010-083]**.
- **What the business is** (20-F FY2025, Item 4.B): about 47,200 MW of operating capacity (48,676 MW at June 30, 2026),
  annualized long-term-average generation of about 121,900 GWh, owned mostly through Brookfield-sponsored private funds
  in which the partnership holds a minority economic share and consolidates by voting agreements (Item 5, Part 9, "Voting
  Agreements with Affiliates"); hydroelectric in the US, Canada, Colombia and Brazil; wind; utility-scale solar;
  distributed energy and storage; "sustainable solutions" (an 11% net interest in Westinghouse, a Caribbean and Latin
  American utility, carbon capture, renewable natural gas, recycling, eFuels). About 90% of 2026 proportionate generation
  is contracted, weighted-average remaining term 13 years (Item 4.A). A development pipeline of over 200 GW, and a stated
  policy of "capital recycling": developing or buying assets and selling them "to lower cost of capital buyers" (Item 5,
  Part 9).
- **The parts, and which decides** (Q1's holding-company paragraph and Q2's business of parts, a CONVENTION of the
  framework: a part decides at more than half of five-year operating profit, or else the largest part decides). The
  filer reports proportionate segment results only before depreciation (Adjusted EBITDA) and after interest (FFO); no
  segment operating profit after depreciation is filed. I use both measures, and the answer is the same on each
  (CONVENTION of this run: operating profit read as proportionate Adjusted EBITDA, checked against FFO; rationale: the
  filing gives no segment profit after depreciation, and the two measures that it gives agree on which part is largest).
  Five years 2021 to 2025, $M, from the segment tables of the 20-Fs for FY2022 (2021 column), FY2023 (2022), FY2025 (2023
  to 2025 as restated in FY2024 and FY2025):

  | Part | Adj. EBITDA 2021 / 22 / 23 / 24 / 25 | 5-yr sum | share | FFO 5-yr sum | share |
  |---|---|---|---|---|---|
  | Hydroelectric (N. America, Brazil, Colombia) | 883 / 971 / 1,017 / 902 / 1,023 | 4,796 | 43% | 3,077 | 40% |
  | Wind | 511 / 430 / 493 / 631 / 481 | 2,546 | 23% | 1,891 | 24% |
  | Utility-scale solar | 298 / 362 / 372 / 464 / 494 | 1,990 | 18% | 1,393 | 18% |
  | Distributed energy & storage, sustainable solutions | 173 / 197 / 241 / 394 / 702 | 1,707 | 15% | 1,415 | 18% |
  | (Corporate, not a part) | 11 / 42 / 59 / 17 / (2) | | | (2,191) | |

  No part carries more than half; **hydro is the largest and decides**. The 2021 and 2022 figures for the last row combine
  the two later segments, as the FY2022 filing reported them.
- **Hydro, the deciding part, by Q1's tests.** The key variables are named by the filer and are of a kind its insiders
  write down **[M2000-105]**: generation against a long-term average simulated over 20 to 30 years of inflows (Item 5,
  Part 9); contract prices with inflation indexation and a stated contract profile (Item 4.A; Note 13 discloses the
  long-term price assumptions it uses for fair value); Brazil's generation pooled under the MRE; currency (real, peso,
  Canadian dollar); water rentals, property taxes and relicensing (Item 3.D). Do the past statements tell me the future
  ones **[M2008-033]**? For hydro, largely yes: LTA generation moved from 19,726 GWh (2021) to 20,420 GWh (2025, after a
  larger Isagen stake), revenue per MWh between $71 and $74, a physical asset with a hundred-year life. The variables are
  important and knowable **[M2006-076]**; the technology is old and does not change fast **[M1998-008]**. Hydro is inside
  the perimeter.
- **The doubts about the whole, recorded.** What the partnership will own in ten years is not knowable from its filings:
  it buys and sells parts every year (Neoen, Geronimo Power, Isagen's 15%, Aypa signed in 2026; sales of US hydro
  stakes, distributed generation, US, European and Asian portfolios), and its growth spending goes into the parts that
  do not decide. The framework reads such a company "on the parts it owns, with the policy weighed at Q6" (Q2, a business
  of parts), and Q1 is answered on the deciding part. The non-deciding sustainable-solutions bets (nuclear services,
  eFuels, carbon capture) are of the kind that "won't make it through the filter" **[M1998-008]**; they are small
  (sustainable solutions: 7% of 2025 segment Adjusted EBITDA) and do not decide. "if you have doubts about something being
  into your circle of competence, it isn't" **[M2002-092]**: I have no such doubt about a hydro fleet; I have it about the
  development and recycling business, which is weighed at Q3, Q6 and Q7 and does not decide here.
- **VERDICT: IN** (on the deciding part, hydro), with the doubt about the parts that do not decide carried forward.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now." **[M1995-038]** Asked of hydro, the deciding part; the other parts are read after.

- **The attacker with money** **[M2011-015]**. No sum of money builds a second dam on a river already dammed (the 20-F's
  hydro fleet is 239 facilities on 83 river systems, Item 4.B); the sites, water rights and licences are not for sale to an entrant, and the 20-F's Brazilian concessions run
  with a one-time 30-year renewal (Note 13). The asset "couldn’t be duplicated" **[M2012-030]**. But the attacker need
  not copy the dam: the product is electricity sold into the same grid, and the filer itself says wind and solar "are now
  among the lowest cost forms of power generation available globally" (Item 4.B) and that "If advances in technology
  further reduce the cost of producing power, the competitive advantage of our existing renewable power projects may be
  impaired or eliminated" (Item 3.D). The castle keeps its volume (a near-zero marginal cost dispatches first); what the
  attacker reaches is its price.
- **Pricing power, and the agony before a rise** **[M2005-020]**. Hydro sells under contracts, most with inflation
  escalators, and into spot markets; the filer names its competition as "natural gas, nuclear, oil and coal fired power
  generators as well as other renewable energy generators" and says "The market price of commodities, such as natural gas,
  is an important driver of energy pricing" (Item 4.B, Competition and Marketing). Average hydro revenue per MWh: $74 in
  2024, $71 in 2025, lower on Colombian spot prices in a wet year (Item 5, Part 4). The price is set by contract auctions,
  by the marginal gas plant and by hydrology; that is the gas station's position, "whatever he charged for gas was my
  price" **[M2012-109]**, softened by contracts averaging 13 years. Against it: the July 2025 Hydro Framework Agreement
  with Google for up to 3,000 MW (Item 4.A) shows buyers seeking firm clean power, which hydro alone in the fleet can
  give; whether that brings a premium is not stated in the filing.
- **The low-cost position** (Q2's commodity-business paragraph: a commodity dependence is not by itself a STOP; Q2 asks
  whether it is the low-cost producer, read from the filings **[M2006-004]**, **[M2009-059]**; a high-cost producer in a
  commodity field is OUT **[M1997-010]**). From the filer's own proportionate figures for 2025: hydro direct operating
  costs $692M over 18,551 GWh actual, about $37 a MWh; wind $242M over 8,406 GWh, about $29; utility-scale solar $148M over
  4,759 GWh, about $31 (Item 5, Part 4; my division). Hydro's cash cost per MWh is above the fleet's own wind and solar,
  chiefly water rentals and property taxes (Item 3.D names them). On capital, hydro's historical cost net of depreciation
  is $10,028M against 38,097 GWh of consolidated LTA, about $263 per annual MWh; wind $12,797M against 53,265 GWh, about
  $240 (Note 13, the historical-cost table; Item 4.B, LTA). On neither measure is hydro shown to be the low-cost producer
  in its fleet; against the gas plant that sets the price, no filing I read states the cost. What hydro has is a
  hundred-year life and a capital outlay made long ago. **Single fact against the castle, written down: the filer's own
  hydro costs more per MWh to run than its own wind and solar.**
- **Unit volume, share of mind, brand, the low bid** **[M2004-091]**. Electricity is bought on price and term; no
  customer asks for a Brookfield kilowatt-hour by name. The castle tests of brand and of the customer refusing the low bid
  do not apply to a seller of power; the test that applies is the low-cost one above.
- **Would it stand without the lord?** **[M1996-037]**, **[M2008-045]**. The dams would; hydro needs no genius. The
  development and recycling business, which the filer features as its growth, depends on Brookfield's people and capital
  relationships (Item 4.B: "we leverage our relationship with Brookfield, which we believe provides a unique competitive
  advantage"); that business is the lord, not the castle.
- **Widening or narrowing** **[M2000-075]**, **[L2005-010]**. Hydro FFO by year: $668M, $667M, $624M, $511M, $607M
  (2021 to 2025); Adjusted EBITDA $883M, $971M, $1,017M, $902M, $1,023M, with 2025 including $108M of other income and a
  larger Colombian stake bought for $1 billion in October 2025. Flat before the bought stake and the gains; not widening.
  The owner is selling pieces of it: 25% and then a further 25% of a 403 MW US hydro portfolio, the second piece to a
  BAM-managed fund (Item 4.A; Note 29), described as "non-core".
- **What could destroy, modify or reduce it** **[M2000-014]**. Cheaper wind, solar and batteries lowering the price the
  dam receives at re-contracting (Item 3.D); a Colombian or Brazilian regulatory change; drought (2024 hydro generation
  17,580 GWh against an LTA of 19,844). None removes the dam; each lowers what it earns.
- **The competitor row** (CONVENTION of this run: the 20-F names no rival company; its competition paragraph names
  fuels and technologies only. I take the two US-listed owners of contracted renewable fleets that file 10-Ks, Clearway
  Energy, Inc. and XPLR Infrastructure, LP (formerly NextEra Energy Partners); rationale: the nearest filers in the same
  trade of owning contracted generation for its cash yield. No SEC-filing owner of a large hydro fleet was found among the
  names I considered, so the hydro comparison is made inside BEP's own fleet above. Peer figures are XBRL company-facts
  transcriptions of their 10-Ks, not cross-checked line by line against the filed statements; they are used for the
  field's returns only.) Same metric for all three, operating profit over total assets, five years:

  | Filer (accession of latest 10-K / 20-F) | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|
  | BEP, revenue less direct costs, management fees and depreciation (consolidated, 20-Fs above) | 942 / 55,867 = 1.7% | 1,451 / 64,111 = 2.3% | 1,048 / 76,128 = 1.4% | 1,082 / 94,809 = 1.1% | 856 / 98,701 = 0.9% |
  | Clearway Energy, Inc., operating income (`0001628280-26-010952`) | 267 / 12,813 = 2.1% | 1,470 / 12,312 = 11.9% (includes the gain on its thermal sale) | 263 / 14,701 = 1.8% | 196 / 14,329 = 1.4% | 160 / 16,655 = 1.0% |
  | XPLR Infrastructure, LP, operating income (`0001603145-26-000007`) | 64 / 18,976 = 0.3% | 44 / 23,052 = 0.2% | -28 / 22,511 = -0.1% | -459 / 20,292 = -2.3% | -186 / 19,595 = -0.9% |

  BEP's assets are carried at fair value (revalued), which depresses its ratio; on the historical-cost basis of its PP&E
  ($37,889M at 2025-12-31 against $70,456M at fair value, Note 13) the 2025 ratio roughly doubles to about 2%, still below
  the long government rate. The peers report at historical cost under US GAAP.
- **The parts table** (Q2, a business of parts):

  | Part | share of 5-yr Adj. EBITDA | castle | decides |
  |---|---|---|---|
  | Hydroelectric | 43% | standing: irreplaceable sites, long life, little capital to stay in place; a price-taker, not shown low-cost in its own fleet | yes (largest) |
  | Wind | 23% | open: any developer can build; the filer itself sells wind farms "to lower cost of capital buyers" | no |
  | Utility-scale solar | 18% | open, as wind | no |
  | Distributed energy & storage; sustainable solutions | 15% | open or not judgeable (eFuels, carbon capture, nuclear services) | no |

- **The field's returns over the last full cycle, judged in words** (section C: "ordinary" carries no figure). The
  three filers earned operating profits of about 1% to 2% of their assets in most years of 2021 to 2025, below the long
  government rate; Clearway's one good year was a sale gain. That is a field earning ordinary returns at best, as the
  rows describe a field with competitors who "beat each other’s brains out" **[M2013-052]**, and the filer's own fair
  values discount contracted North American cash flows at 5.0% to 5.7% (Note 13), a near-bond yield. The hydro part
  is the one place where the filings point the other way: little capital is needed to keep it in place (hydro PP&E and
  construction additions of $199M in 2025 against hydro depreciation of $650M, Note 13), and its historical-cost book of
  $10,028M is small beside its earnings. Whether that is a castle that "protects excellent returns" **[L2007-004]** or an
  old outlay inflated by time, the rows' own distinction at BNSF, "an acceptable return on its purchase price" against
  "a pittance on the replacement value" **[L2023-009]**, cannot be settled from the filings: the filer reports no
  consolidated hydro earnings to set against that $10,028M, and the proportionate figures are on a fair-value base.
  The quality of a business is judged on "the capital actually needed in the business" **[M2010-090]**, and on that
  measure the deciding part looks sound.
- **Judgment.** The deciding castle stands: the dams cannot be copied, they run without a genius, they need little capital
  to stay in place, and their volume is protected by near-zero marginal cost. It is not widening; it is a price-taker in a
  commodity field; and on the filer's own figures it is not the low-cost producer within its own fleet. The rows would
  call the moat "tenuous" if its future could not be judged **[M2000-019]**; here the future can be judged (contracted,
  inflation-linked, long-lived), and what it shows is a durable asset with a capped, market-set price, not a castle
  shown to be filling in. On the deciding part the castle is standing; the evidence for "excellent returns"
  **[L2007-004]** is the weak half, and it is carried to Q3 and Q7 rather than settled here on a fair-value ratio. The
  non-deciding parts are open (wind, solar, distributed generation: no barrier to entry, a field of ordinary returns,
  **[M2012-106]**) and are carried to Q7 as ordinary businesses at no growth, as the parts paragraph directs.
- **VERDICT: IN** on the deciding part (hydro), narrowly; the other parts open, carried to Q7 at no growth.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What it has earned on the capital it needs** **[M2010-090]**. Consolidated operating profit before other income
  (revenues less direct operating costs, management service costs and depreciation) against borrowings plus total equity
  at year end (20-Fs FY2023 and FY2025, statements of income and financial position): 2021 $942M / $45,525M = 2.1%;
  2022 $1,451M / $51,136M = 2.8%; 2023 $1,048M / $59,681M = 1.8%; 2024 $1,082M / $70,846M = 1.5%; 2025 $856M / $69,866M
  = 1.2%. The base is inflated by the revaluation of PP&E (fair value $70,456M against a historical-cost net book of
  $37,889M for the revalued assets, Note 13), and the depreciation is charged on the revalued amounts; on a cost base
  the ratio would be higher, but the filer gives no historical-cost depreciation, and no reading I can make from the
  filings carries it near the returns the rows call good. A high reported return must first rule out "a cyclical peak in
  earnings, a monopolistic position, or leverage" **[L1994-009]**; here the problem is the reverse, a low return carried
  on heavy leverage (consolidated debt-to-capitalization 44% at book, Item 5, Part 5).
- **How much must be reinvested to stand still** **[L1999-024]**, **[M2000-144]**. The filer states that IFRS depreciation
  is "a significantly higher level of depreciation for our assets than we are required to reinvest in the business as
  sustaining capital expenditures" (Item 5, Part 9) and gives no sustaining-capital figure in the 20-F; the owner is
  entitled to the manager's best guess of the maintenance need **[M2000-144]**, and it is not given. What the notes allow:
  hydro, the deciding part, added $15M to operating PP&E and $184M to construction in 2025 ($4M and $155M in 2024) against
  hydro depreciation of $650M and $626M (Note 13). For hydro the speakers' best business is close: little must go back in
  **[M1998-081]**. For the whole, depreciation of $2,425M in 2025 is set against $1,500M of additions to operating PP&E
  (which include purchase-price adjustments) and $6,159M of construction additions (Note 13); wind and solar units are depreciated over "Up to 35 years", batteries "Up to 30
  years", against "Up to 115 years" for dams and hydro units (Note 1(g)), and "Depreciation
  charges [...] are almost always true costs" **[L2015-004]**.
- **What the added capital earned** **[M2001-019]**, **[M2023-081]**. Over 2021 to 2025 the group spent $17,286M on
  PP&E, $12,044M on acquisitions and $1,579M on equity-accounted investments, and received $5,093M from disposals: net
  $25,816M (consolidated cash flow statements). Over the same years: revenues rose from $4,096M to $6,407M; operating
  profit before other income fell from $942M to $856M; attributable FFO without the "other income" (Note 7) went $633M,
  $713M, $683M, $548M, $482M; attributable interest rose from $539M to $969M (Note 7); net income attributable to
  Unitholders was negative in every year. The return the filer shows on its added capital is the gain on selling some of
  it: "other income" inside FFO of $301M, $292M, $412M, $669M, $852M (Note 7 footnotes: "predominantly associated with
  dispositions and monetizations of developed or non-core assets and businesses"). Rising earnings would prove nothing
  here, "We just put way more capital into the business" **[M2023-081]**; the recurring earnings did not even rise.
- **The growth arithmetic.** The filer's own target is FFO per unit growth funded by "internally generated cash flows,
  asset recycling and upfinancing" (Item 4.B). This is the account that "requires you to keep adding money at those
  disappointing returns" **[L2007-010]**, unless the development gains are a durable return on the development capital;
  they are cash when realized (proceeds of $2,817M in 2025), but they depend on buyers paying "lower cost of capital"
  prices (Item 5, Part 9), which is a market condition, not a castle. "cash-consuming businesses, by their nature, are
  unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**. The capital-heavy business
  is admitted as a second best only where it earns "decent returns on the incremental sums they invest" **[L2009-012]**;
  a regulated return is not available here (Q7, the regulated utility, below).
- **WEIGHS AGAINST**, heavily for the whole: a capital-hungry business whose added capital has earned almost nothing at the
  operating line in five years, its shown return coming from selling assets. Hydro, the deciding part, weighs for on the
  capital needed to stay in place **[M1998-081]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, nine years** **[M2025-032]** ($M, consolidated, as filed; 2017 and 2018 from the FY2018
  20-F's summary and the FY2019 statements, 2019 from FY2019, 2020 and 2021 from FY2021, 2022 and 2023 from FY2023, 2024
  and 2025 from FY2025; 2020 onward restated for the TerraForm Power common-control combination; LP equity for 2017 is
  the XBRL transcription, not checked against the page):

  | Dec 31 | Total assets | PP&E at fair value | Goodwill | Cash | Borrowings (corporate + non-recourse) | Deferred tax liab. | Due to related parties (current) | NCI in operating subs | LP equity |
  |---|---|---|---|---|---|---|---|---|---|
  | 2017 | 30,904 | 27,096 | n/a | n/a | 11,766 | 3,588 | n/a | n/a | 3,956 |
  | 2018 | 34,103 | 29,025 | 828 | 173 | 10,718 | 4,140 | 101 | 8,129 | 4,484 |
  | 2019 | 35,691 | 30,714 | 821 | 115 | 11,004 | 4,537 | 127 | 8,742 | 4,576 |
  | 2020 | 49,722 | 44,590 | 970 | 431 | 18,082 | 5,515 | 506 | 11,100 | 3,845 |
  | 2021 | 55,867 | 49,432 | 966 | 764 | 21,529 | 6,215 | 164 | 12,303 | 4,092 |
  | 2022 | 64,111 | 54,283 | 1,526 | 998 | 24,850 | 6,507 | 588 | 14,755 | 4,096 |
  | 2023 | 76,128 | 64,005 | 1,944 | 1,141 | 29,702 | 7,174 | 835 | 18,863 | 3,963 |
  | 2024 | 94,809 | 73,475 | 5,434 | 3,135 | 34,390 | 8,439 | 4,855 | 26,168 | 3,604 |
  | 2025 | 98,701 | 70,456 | 6,019 | 2,093 | 34,892 | 9,395 | 7,071 | 24,164 | 3,970 |

  What moved and why. (1) Assets tripled, almost all in PP&E, and much of PP&E's rise is revaluation through other
  comprehensive income, not cash spent ($5,605M of fair-value gains through OCI in 2024 and $2,162M in 2025, Note 13).
  (2) The LP equity has not grown in nine years ($3,956M to $3,970M) despite units sold for cash; and it exists only by
  the revaluation surplus: at 2025-12-31 the limited partners' equity account (contributions less losses and
  distributions) stood at -$3,281M, against -$948M at 2018-12-31, with a revaluation surplus of $8,206M beside it
  (statements of changes in equity, FY2025 and FY2019). Every dollar of book equity the LP units show is an appraisal.
  (3) Borrowings tripled, to $34,892M, 90% non-recourse at the asset level (Item 5, Part 5). (4) Goodwill rose sevenfold,
  chiefly on Neoen. (5) Amounts "due to related parties", current, rose from $835M to $7,071M in two years; of it
  $4,427M is owed to Brookfield, including $2,454M, $511M and $397M "associated with" Brookfield Global Transition Fund
  and Brookfield Infrastructure Fund IV credit facilities, and the note says "Amounts due to Brookfield are unsecured,
  payable on demand" (Note 29). (6) Participating non-controlling interests are now six times the LP equity: most of
  what is consolidated belongs to Brookfield's institutional partners. What the figures cannot say: what the partnership
  itself owns of the hydro fleet's earning power, except through the filer's proportionate (non-IFRS) tables.
- **Lumped businesses.** The consolidated statements lump the partnership's share with its partners' share: the
  Unitholders' share of consolidated PP&E was $33,594M of $70,456M at 2025-12-31 and $30,949M of $73,475M a year earlier,
  42% to 48% (Note 7); "lumping them together [...] impedes analysis" **[L2008-005]**. The filer's own answer is
  the proportionate tables, which are not audited IFRS figures.
- **The real costs.** Depreciation: the featured FFO adds back all of it, and the filer says its sustaining spending is
  lower, without saying how much lower. "With rare exceptions, depreciation is an economic cost every bit as real as wages,
  materials, or taxes" **[R1996-023]**; "I’ll look at that figure when you tell me you’ll make all the capital
  expenditures" **[M2003-108]**. Deferred taxes: the filer adds them back because management does "not believe this item
  reflects the present value of the actual tax obligations" (Part 9). Management service costs ($223M) and the GP's
  incentive distributions are real costs to the units and are discussed at Q5 and Q6. Interest is rising and is real.
- **EBITDA and the featured figure in the filer's own mouth.** The 20-F leads with "Proportionate Adjusted EBITDA" and
  "Funds From Operations per Unit" (Item 5, Part 1, highlights) ahead of the net loss; it explains both and reconciles
  both. "References to EBITDA make us shudder" **[L2000-036]**. The featured FFO includes "realized disposition gains"
  (Part 9; Note 7), which made up $852M of the $1,334M in 2025, 64% of it; and it is divided by units that include the
  GP interest while the GP's incentive distributions ($151M declared in 2025 with the GP's regular distributions, Item
  5, Dividends and distributions) are not deducted from it. A management that "regularly attempts to wave away very real
  costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**. Recorded as a WEIGHING against
  and carried to Q5, as Q4's paragraph on the make-the-numbers habit directs.
- **Confusion or suspicion?** The accounts are complex but not obscure: every adjustment is defined and reconciled to
  IFRS, the historical-cost table and the fair-value assumptions are disclosed, and the related-party balances are
  itemized. I can say what the units earned after every real cost: on IFRS, a loss in each of five years (net income
  attributable to Unitholders -$368M, -$295M, -$100M, -$464M, -$19M; FY2023 and FY2025 statements of income); on the
  filer's own recurring figures, FFO without the gains of about $0.48 billion to $0.71 billion a year before any
  depreciation. That is a finding, not a confusion. The tells that live in the accounts (prepaid or deferred accounts
  building, reserves that move, profits that may not exist) **[M1995-064]**: the closest is profit booked on sales of
  assets to Brookfield-managed vehicles (a 25% US hydro stake sold to a BAM-managed fund, the Isagen 15% bought from a
  Brookfield fund, each "at a value equivalent to" a price agreed with an unaffiliated party, Note 29), which the note
  explains. Not suspicion on the record I read. No STOP.
- **VERDICT on the accounts: no STOP; WEIGHS AGAINST**, heavily: the featured figure includes asset-sale gains and omits
  depreciation, the units have lost money under IFRS in every year of the window, and the LP book equity is entirely
  appraisal **[M1994-018]**, **[L2016-006]**. The recast earnings feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** BEP has no employees of its own at the top. Its general partner (the Managing General Partner, "a
  wholly-owned subsidiary of Brookfield Corporation") controls it; its chief executive, Connor Teskey, is "the Chief
  Executive Officer of the Service Provider, a Managing Partner of Brookfield, and the President of Brookfield Asset
  Management"; the chief financial officer is a Brookfield managing partner (Item 6.A). They "are not compensated by
  BEP or our Managing General Partner; instead they are and will continue to be compensated by Brookfield" (Item 6.B);
  their pay is not in the 20-F. Brookfield holds about 47% of the economic interest on a fully-exchanged basis (Q2 2026
  interim). The unitholders do not elect the board; the simplification circular's own list of benefits includes
  "Enhanced governance framework and voting rights for public securityholders" (6-K of 2026-10-13).
- **The two yardsticks** **[M1994-008]**. How well they run the business: the fleet's operations are competent on the
  record (generation near long-term average except in drought years; an investment-grade BBB+ rating, Q2 2026 interim;
  $15 billion of non-recourse financing placed in 2025, Item 4.A). How they treat the owners: the record of the units is
  poor (LP equity account from -$948M to -$3,281M over 2018 to 2025 while units were sold; a market price of $43.15 at
  2020-12-31 and $26.97 at 2025-12-31, Yahoo year-end closes, aggregator, flagged), and the fee structure is Q6's.
- **The tells of dishonesty the rows name.** Reports that dance **[M1995-111]**: the reports do not dance; the 20-F
  states plainly that FFO includes "realized disposition gains", reconciles every non-IFRS figure, prints the historical
  cost of the revalued assets and the discount rates behind them, and spends many pages on Brookfield's conflicts. The
  key figure is not hidden **[M2007-082]**: the net loss per LP unit is in the highlights table, beside FFO. Too good to
  be true **[M2002-028]**: no. Owners as patsies **[L2001-002]**: the structure gives Brookfield a fee on the
  partnership's total capitalization and a quarter of distributions above a threshold, and the services agreement cannot
  be ended by the partnership "for any other reason" than the listed causes (Item 6.A); that is weighed at Q6 Part B as
  owner treatment, a structure disclosed since the listing, not a concealment. No sanctions or cease-trade orders in ten
  years (Item 6.A).
- **The habits carried from Q4, read with the integrity record** **[M2013-088]**. The featured per-unit figure includes
  asset-sale gains and omits depreciation **[L2016-006]**; the filer sets and meets declared per-unit targets (a 5% to 9%
  annual distribution increase, raised 5% in each year of the table from 2020 to 2026, Item 5; FFO per unit up about 10% ($1.83 to $2.01) in
  2025 and 11% in Q2 2026, with "Gains on sales from our recurring and scaling capital recycling activities" named among the drivers, Q2 2026
  interim), and the gains that close the gap are discretionary in timing. "we become downright incredulous if they
  consistently reach their declared targets" **[L2002-041]**. Read with the rest: every gain is disclosed as a gain, in
  the same paragraph that reports the growth, and the related-party sales are priced against unaffiliated bids (Note 29).
  I find a management that features the number it is paid to grow and meets its targets with sales it chooses to make,
  openly. That is a judgment on how owners are treated and how the numbers are presented; it is not, on what I read,
  evidence of dishonesty, and I do not hold a doubt about honesty that the record supports. Integrity is applied on doubt
  alone **[M2013-088]**; the doubt I hold is about alignment, which is Q6's.
- **Love of the business, ability.** The managers are investment managers whose firm is paid on assets under
  management; "do they love the business or do they love the money?" **[M2000-098]** cannot be read for people not paid
  by the company and not disclosed. Ability shows in financing and operations; the capital-allocation record for the units
  is weak (Q3, Q6). The rows care "more [...] about how our record is achieved than the precise record itself"
  **[M2012-089]**: here FFO per unit growth was made by gains, not by recurring earnings.
- **VERDICT on integrity: IN** (no evidence of dishonesty in the record read; the featured-figure habit judged as owner
  treatment, not as a lie). **Ability: WEIGHS AGAINST** for the units (operating competence for, capital-allocation record
  and how the per-unit record was made against).

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test** **[R1995-009]**, **[M1998-110]**. BEP retains nothing in the ordinary sense: distributions to
  Unitholders ($1,140M in 2025) exceed FFO without gains ($482M) and IFRS earnings (a loss), and the gap is filled by
  asset sales and new capital ("Issuance of equity instruments" of $592M, $115M, $630M, $145M and $632M in 2021 to 2025,
  cash flow statements; financing cash flows of $6,418M in 2025).
  The test is then the one the rows put to any capital the managers keep or raise: has it made more than a dollar of
  value per dollar? In market value per unit, no: $43.15 at the end of 2020 to $26.97 at the end of 2025 (aggregator,
  flagged), while units were issued and the LP account fell by $2.3 billion. Against intrinsic value, Q7 below. "almost
  any management that wants to retain money is going to rationalize it" **[M1998-110]**.
- **Buybacks** **[L1999-023]**, **[L2011-003]**. The normal course issuer bid names no price: "The price to be paid for
  our LP units under the normal course issuer bid will be the market price at the time of purchase" (Item 16E). Bought:
  1,522,975 LP units in February to May 2025 at C$29.34 to C$32.72 (Item 16E); 5,994,833 in the first half of 2026,
  matched one for one by BEPC shares sold under an at-the-market programme (Q2 2026 interim). A programme with no stated
  price weighs against unless the prices paid sit at or below the bottom of Q7's range **[L2016-002]**. *Written back
  from Q7 and committed with it:* the bottom of the range is -$60.29 a unit (all-equity; -$55.51 equity-only); every price
  paid, about C$29 to C$33 in 2025 and the market in 2026, is above it. **The buyback weighs against.** (The pairing of
  2025 purchases near C$29 to C$33 with the November 2025 sale of units at US$29.90 is noted: bought lower than sold,
  though both are above the range.)
- **Issuance and deals** **[M1995-001]**, **[L2014-012]**. Units sold: 22,017,870 LP units at $29.90 in November 2025,
  6,967,670 of them to a Brookfield subsidiary (Item 4.A); BEPC shares under an at-the-market programme of up to $400M
  from January 2026; and the simplification resolution, if approved, "will constitute voting in favor of BEP Inc.'s
  ability to conduct future issuances [...] without requiring further approval" (6-K of 2026-10-13). Each issue raises the
  fee base (Part B). The deals in the window were paid in cash (Neoen, about $6.7 billion, $537M net to BEP; Geronimo
  Power, $1.4 billion, $299M net; Isagen's 15%, $1 billion, from a Brookfield fund; Item 4.A), so Q6's one STOP, an
  all-stock deal in undervalued stock **[L2009-019]**, is not engaged in the window. (The TerraForm Power combination of
  2020, paid in shares, is before the window and is not judged here.) A serial issuer is the candidate second STOP the
  framework leaves open **[L2014-015]**: BEP issued units or exchangeable shares for cash in 2021, 2023, 2025 and 2026 and
  asks for standing authority to issue more; I weigh it heavily, not as a STOP, since the framework leaves the point open.
- **Dividends and the use of cash** **[M2004-089]**, **[L2012-015]**. The policy is "clear, consistent" (a target payout
  of about 70% of FFO and 5% to 9% annual growth, Item 4.A), but its base includes the gains, and the distribution exceeds
  the recurring cash after interest. A distribution larger than recurring earnings, raised every year by policy, is the
  opposite of "Cash at Berkshire is a residual" **[M1995-057]**.
- **Part A: WEIGHS AGAINST**, heavily.

### Part B: the pay, the board and the owners
- **The manager's pay, as the unitholders pay it.** The Base Management Fee: "$20 million (adjusted annually for
  inflation ...) plus 1.25% of the amount by which the market value of Brookfield Renewable exceeds an initial reference
  value" (Item 6.A); $223M in 2025, $204M in 2024, $205M in 2023 (statements of income), on a "Total capitalization
  value" of $26 billion against a reference of $8 billion (Note 29). Plus incentive distributions to the GP: 15% of
  quarterly distributions above $0.20 a unit and 25% above $0.2253 a unit (Item 5, Part 5), against a 2026 quarterly
  distribution of $0.392; GP interest and incentive distributions declared were $151M, $134M and $116M in 2025, 2024 and
  2023 (Item 5). Together about $374M in 2025, against FFO without gains of $482M. The fee grows with the partnership's
  market value and capitalization, so it grows with every unit issued and every dollar borrowed at the corporate level,
  whatever happens to value per unit: "the override on other people’s capital without putting up any of their own
  capital to speak of" **[M2025-050]** describes the shape, though Brookfield does hold about 47% of the units, so its
  own capital is in. The incentive distribution pays on distributions, which policy raises every year and which exceed
  recurring earnings; pay is not tied "to what is actually under the reasonable control of the person that’s being
  measured" **[M2003-019]** in the sense of per-unit value. "you get what you reward for" **[M2016-083]**.
- **Who designed it, and who can change it** **[M1997-041]**. Brookfield designed it at the listing; the partnership
  cannot terminate the services agreement except for the listed causes, and the general partner is Brookfield's.
  "The people who have their hands on the switch are the beneficiaries of the system" **[M1998-066]**.
- **The board** **[M2007-120]**. Six directors, five independent under exchange rules; the chair is a Brookfield vice
  chair; independent directors receive $165,000 a year and must hold units costing twice that (Item 6.B). Several of the
  independent directors also sit on the boards of other Brookfield-sponsored entities (Item 6.A); "independence" by
  checklist is not what the rows ask **[M2009-086]**. The board's three jobs, the right chief executive, no overreaching,
  independent judgment on acquisitions **[M2007-120]**: the chief executive is chosen by Brookfield, and conflicts are
  governed by "Conflicts Protocols" under which the independent directors "may grant prior approvals [...] in the form of
  general guidelines" (Item 6.C).
- **The owners as partners** **[L1994-023]**. Disclosure is full and candid; no earnings guidance in the GAAP sense, but
  declared growth targets for the distribution and for FFO per unit. The simplification may improve voting rights; it is
  not closed (meeting adjourned to 2026-10-29 for want of the two-thirds turnout, 6-K of 2026-10-13).
- **Part B: WEIGHS AGAINST**, heavily: pay to the manager scales with size and distributions, not with value per unit, under
  an agreement the owners cannot end.

## Q7 — WHAT IS IT WORTH? STOP.
"how much do you get back, how sure are you of getting it, when do you get it?" **[M2009-004]**, and "are you going to
have to put more cash into after you buy it?" **[M2014-068]**. Arithmetic in `Test Runs/_research 2026-10-18 BEP/compute_q7.py`,
output in `q7_output.txt` beside it; every input is typed from the filed statements named in the script.

- **Which basis is central.** The all-equity basis (Q7, On what the floor is earned). The regulated-utility paragraph
  does not apply: the deciding part, hydro, sells under contracts won in procurement and into power markets, not at a
  return a regulator allows on invested capital **[M2010-037]**; the paragraph itself says "Merchant generation and
  unregulated renewables, priced by a market, stay on the all-equity basis". The Brazilian MRE pools hydrology risk; it
  does not set a return on capital. Equity-only beside.
- **Owner cash, and how the unitholders' share is taken out of consolidated statements** (CONVENTION of this run: the
  framework builds owner cash from the company's statements, and BEP's consolidate businesses of which the Unitholders
  own 42% to 48% (Note 7); I take the group's cash before debt, from operations less all investing outlays plus disposal
  proceeds, and then add the partners' capital contributions and subtract the cash returned and distributed to them and
  to the preferred and perpetual holders, all as the cash flow statement prints them; rationale: it uses only audited
  lines and leaves the Unitholders the residual the filing shows. It understates where partners' distributions were
  funded by asset-level borrowing, which is not credited; the all-equity case below adds back the Unitholders' interest).
  $M, from the consolidated statements of cash flows (FY2023 20-F for 2021 and 2022, FY2025 20-F for 2023 to 2025):

  | | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr avg |
  |---|---|---|---|---|---|---|
  | Group cash before debt (CFO less PP&E, acquisitions, equity-accounted investments, net financial assets; plus disposals) | -1,724 | -3,449 | -2,456 | -5,492 | -7,132 | -4,051 |
  | Unitholders' share, all spending deducted (above, plus partner contributions, less partner repayments and distributions) | -1,935 | -3,033 | -1,078 | -4,459 | -8,337 | -3,768 |
  | Net purchases (acquisitions plus equity-accounted investments less disposals) | 653 | 2,548 | 1,299 | 2,237 | 1,793 | |
  | Unitholders' share, purchases left out (the organic pair) | -1,282 | -485 | 221 | -2,222 | -6,544 | -2,062 |
  | Interest attributable to Unitholders (Note 7) | 539 | 596 | 745 | 835 | 969 | 737 |

- **The specifics applied.** (c) The serial acquirer: net purchases over the window ($8,530M) exceed half of owner cash
  before purchases (which is negative), so the central figure is the organic pair, with the default pair (purchases
  deducted, total growth credited) beside. (e) Growth spending: the filing gives no sustaining-capital figure (Q3), so it
  does not allow the maintenance guess; all PP&E spending is deducted, and the depreciation variant is shown beside:
  FFO without the "other income" less depreciation attributable to Unitholders was -$289M (2021) and -$221M (2022), the
  only years the filer split depreciation by owner (Note 7 of the FY2022 20-F); for the later years, net income
  attributable to Unitholders, which is after depreciation, was negative in each (Q4). (a) No first or last year is
  described by the filer as cyclical or aberrational; capital spending rose each year by design (Item 4.B); the literal
  window is the window used. (b) Decline: every year of the central series but one is negative and the series changes
  sign once; a growth rate between its ends, or between its halves, is meaningless, so **the range is the no-growth case
  alone, said so**. (d) Working capital is inside cash from operations as filed. (f) No growth carried, so no cap is
  reached. The non-deciding parts, carried "as an ordinary business at no growth" from Q2, are inside the same series.
  The Aypa acquisition, signed in 2026 and not closed (Q2 2026 interim), would add its financing to net debt and is
  credited at nothing until its own record is filed; it can only lower the figures below. The simplification is a change
  of form, not a deal for value.
- **Net debt (all-equity basis).** Proportionate borrowings at 2026-06-30 of $17,881M (corporate $4,905M and the
  Unitholders' share of non-recourse debt $12,976M), less the Unitholders' share of cash ($871M) and marketable
  securities ($176M): **$16,834M** (Q2 2026 6-K, Borrowings and Available liquidity tables). CONVENTION of this run:
  proportionate debt rather than consolidated, because owner cash above is the Unitholders' share; preferred units,
  preference shares and perpetual notes are left out of net debt because their distributions are already deducted in
  owner cash. Operating leases left out, as the framework directs. The $4,427M due on demand to Brookfield is a
  consolidated balance and is weighed at Q9, not added here.
- **Whose tax.** Owner cash is after the company's own taxes as paid. The interest add-back for the all-equity case is
  gross (CONVENTION of this run: current income tax was a net recovery in 2024 and 2025 and small before, statements of
  income; rationale: no tax shield is in evidence to deduct, and the gross add-back is the more favourable to the
  business).
- **Value range, at the long government rate of 5.43%, no-growth case alone:** all-equity (owner cash before interest
  -$1,326M a year, less net debt) **-$60.29 a unit**; equity-only (-$2,062M a year) -$55.51 a unit; against **$28.40**.
  The default pair beside: all-equity -$106.21, equity-only -$101.44.
- **The floor, tested first** (2026-10-10). Expected return at $28.40 on the central case: all-equity -3.66% (owner cash
  before interest over market value plus net debt), equity-only -10.61%; on the default pair -8.36% and -19.39%; on the
  depreciation variant, negative. **No case in the range earns the floor at the price** **[M2003-149]**: the file closes
  OUT whatever the width. The width test is not reached.
- **The strongest case for the business, tested and not adopted.** The filer's own featured FFO for 2025, gains
  included, with no capital spending and no depreciation charged at all, is 6.87% of the units' market value; FFO without
  the gains is 2.48% (my division, `q7_output.txt`). Even the figure the manager is paid to grow, stripped of every capital
  cost, would need sustained growth to reach the floor at this price, and it is not owner cash: it adds back all
  depreciation **[L2015-004]** and counts sales of assets as earnings. "growth can destroy value if it requires cash inputs
  in the early years of a project or enterprise that exceed the discounted value of the cash that those assets will
  generate in later years" **[L2000-023]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case at ten percent, averaged; the range has
  one case, so the fair price is that case at ten percent. **All-equity (central): -$43.98 a unit**; equity-only beside:
  -$30.14 a unit; after the company's own tax. Neither is positive. The framework's fallback, "where the central fair
  price is still not positive, the alert is set on the organic pair and labelled so" (Q7 (c)), does not help: the organic
  pair is already the central case here and is negative. No price alert can be set from this run.
- **VERDICT: OUT** (Q7, the floor: no case earns about ten percent at $28.40; owner cash after every real cost has been
  negative on every construction the filings allow).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (Q7 closed the file). Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7** (the floor: owner cash after every real cost negative on every case the filings allow, so no case earns
about ten percent at the price). Value range, no-growth case alone: **-$60.29 a unit all-equity (central), -$55.51
equity-only**, against **$28.40** (2026-10-16, aggregator). Fair price: **-$43.98 all-equity (central), -$30.14
equity-only**; not positive, so no price alert can be armed from this run. Q1 IN and Q2 IN (narrowly) on hydro, the
deciding part; Q3, Q4 (no STOP), Q6 weigh against heavily; Q5 integrity IN.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged; each with its source **[M1997-127]**.)*

- **Q8, the bond.** The 30-year Treasury yields 5.43% (2026-10-16, Treasury par curve). The units' FFO including gains
  was 6.87% of their market value in 2025 and 2.48% without the gains (Q7 sensitivity).
- **Q9, debt and calls on cash.** Consolidated borrowings $34,892M at 2025-12-31, of which corporate $3,686M and
  non-recourse $31,206M; "approximately 90% of our borrowings are non-recourse", "no financial maintenance covenants" on
  the asset-level debt, corporate debt weighted term about 13 years and proportionate non-recourse about 10 years "with
  no material maturities over the next five years" (Item 4.B, Item 5 Part 5). Proportionate borrowings $17,881M at
  2026-06-30, up from $16,781M six months earlier; commercial paper $1,100M at 2026-06-30 against $194M at year end; 96%
  of proportionate borrowings fixed-rate, 16% of total borrowings floating (Q2 2026 6-K). Current "due to related
  parties" $7,071M, of which $4,427M to Brookfield, "unsecured, payable on demand", including payables of $2,454M, $511M
  and $397M "associated with" Brookfield fund credit facilities (Note 29). Consolidated pre-tax earnings over interest:
  2025 net income $712M less a tax recovery of $614M is $98M pre-tax, so ($98M + $2,457M) / $2,457M, about 1.04 times;
  2024 about 0.90 times (statements of income; coverage defined as "pre-tax earnings/interest, not EBITDA/interest"
  **[L2012-002]**). Liquidity $5,127M at 2026-06-30 (Q2 2026 6-K). Westinghouse: a contingent 20% interest in
  distributions above $17.5 billion may vest to the US Government (Item 4.A).
- **Q10.** Nothing found beyond the above.
- **Q12.** Nothing in the businesses named by the rows; renewable power and nuclear services.
- **For any later run.** The pending simplification into BEP Inc. (meeting adjourned to 2026-10-29) would change the
  units' form, the voting rights and possibly the incentive-distribution arrangement; I did not read the joint
  circular. The Aypa acquisition (signed 2026, not closed) adds roughly 3,000 MW of battery storage.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (commits 747b4ec4
      Q1-Q2, 4670fd58 Q3-Q4, 7c8c6e2c Q5-Q6, 96b2ab16 Q7 with the Q6 write-back, then this close).
- [x] Dispatched: the brief allowed per-question pathspec commits of my two paths only; the lock is the dispatching
      session's; the fold is the dispatcher's. Only my two paths were committed, never `git add -A`, never pushed.
- [ ] **Not clean.** No other run file, holding review or `PORTFOLIO.md` was opened; but at the start I listed
      `Test Runs/` filtered for "bep|brookfield", which the blind rule counts as a search, and saw the names of the
      BAM, BN and BIPC files (declared under contamination at the top; none opened, nothing used).
- [x] Every v5 id resolves (`check_cites.py`: 89 ids, every quoted fragment beside an id found in its row, 0 problems);
      no E-ids; every filing fact carries its accession; peer figures are XBRL transcriptions, flagged as such.
- [x] The order was kept; Q1 to Q6 answered in order; Q7, a STOP, closed the file; Q8 onward NOT REACHED.
- [x] Owner cash after every real cost, from the audited cash flow statements, never a net-income proxy (operator rule
      5); the featured FFO was tested as a sensitivity and not adopted. The sovereign from the issuing authority (US
      Treasury). Aggregator quotes flagged (price, year-end closes).
- [x] Contrary evidence written down as found (foundations, and at Q2, Q3, Q4); facts for later questions under AFTER THE
      STOP. No integrity flag is owed: Q5 was answered, not skipped.
- [x] Not a point-in-time run; no anchor rule engaged.
- [x] `tools/run.py` returned UNRESEARCHED for an IFRS filer; none of its output was used.
- [x] `python tools/check_framework.py` PASS before each commit.
- **Judgments a second analyst may make differently, said plainly.** (1) Q2 IN on hydro is narrow. On the filer's own
  figures hydro is not the low-cost producer in its own fleet and is a price-taker; a reader who weighs those facts
  as the commodity paragraph's "high-cost producer" would close the file OUT at Q2, a question earlier, with the same
  computation beneath it. I held it IN because the castle's durability (the sites, the life, the small capital to stay
  in place) is evident and the cost comparison the paragraph asks for, against the producer that sets the price, is not
  in any filing I read. (2) Q5 integrity IN: a reader who takes the featured, gains-inclusive per-unit figure and the
  targets met by chosen sales as a doubt on honesty would close at Q5. (3) The unitholders' share of consolidated cash
  is my construction (confessed at Q7); its sign is the same on the whole-group figure, on the organic pair, on the
  depreciation variant and on IFRS net income, so the box does not turn on it.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Owner cash for a consolidator with a minority economic share.** Q7 builds owner cash from "the company's" cash
flows and net debt "as the filing states them", and is silent on a filer whose consolidated statements are more than
half partners' money and partners' debt. I had to confess a construction (the residual after partners' cash flows) and
switch net debt to the filer's non-IFRS proportionate figure so that the two sides matched; a rule is needed for which
basis to use and how partners' debt-funded distributions are treated. (2) **The business of parts on segment figures
that stop before depreciation.** The threshold is "five-year operating profit", but this filer reports segment results
only before depreciation (Adjusted EBITDA) and after interest (FFO); I used both, and the framework does not say which
stands in. (3) **The commodity paragraph's low-cost test for a regulated-entry asset class.** It asks whether the business
is the low-cost producer from filings; for power, the price-setter is usually a gas plant whose costs no rival filing of
this run states, and the filer's own fleet shows hydro with a higher cash cost than wind and solar but a far longer life
and sunk capital. Whether "low-cost" means cash cost, all-in cost or cost against the price-setter is not said, and the
answer decides between Q2 IN and Q2 OUT here. (4) **The serial-acquirer test when owner cash before purchases is
negative.** "net purchases over the window exceed half of owner cash before purchases" is trivially met when that cash is
negative; I applied it, but the test was evidently written for a positive base. (5) **A capital-recycling developer.**
The framework counts disposals as negative capital spending in the range and has no place for a business whose stated
product is the gain on selling what it builds; the gains are real cash, yet treating them as recurring earnings would
count the same assets twice. I left them where the cash flow statement puts them. (6) **The brief's competitor slot**
asks for rivals the 20-F names; this 20-F names fuels, not firms, so the comparators are a confessed convention.
