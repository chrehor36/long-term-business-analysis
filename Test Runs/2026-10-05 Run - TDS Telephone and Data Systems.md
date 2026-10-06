# Company Run: Telephone and Data Systems, Inc. (NYSE: TDS), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from the template before any fetch; working folder `Test Runs/_research 2026-10-05 TDS/`.)*

**POSITION NOTE, declared before any verdict:** not known to this analyst. `PORTFOLIO.md` is on this run's blind list
and was not opened, so whether the operator holds TDS was not checked.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
the run queue, the prepped reading list, any other `Test Runs/` file about TDS (a listing of `Test Runs/` filtered for
"TDS" returned none), other companies' 2026-10-05 run or research files, and the not-adopted gaps case. Seen without
opening: the file names in `Test Runs/` (other 2026-10-05 runs, holding reviews and research passes, none about TDS),
and the subjects of the five most recent commits (PENN OUT at Q2, YELP TOO HARD at Q1, ROCK TOO HARD (WORK) at Q2, ENR
OUT at Q2, a session-state commit), each giving a "fair" and a "cheap" price for another company. A session memory index
loaded with the project says the watchlist holds "57 gate-clearers, nothing buyable"; it names no company. None of this
concerns TDS or its industry; the only possible influence is the habit, seen in those subjects, of reporting cheap at
roughly half of fair, and this run sets its own cheap rule below without reference to them.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $35.11, close 2026-10-05 (Yahoo chart API via `tools/sources.py`; **aggregator, live quote only**, operator
  rule 5). Same source: Array Digital Infrastructure (NYSE: AD) $34.50; TDS Series UU depositary share $19.595, Series
  VV $17.82 (par $25 each).
- **Shares by class:** 107.6 million Common Shares and 7.5 million Series A Common Shares as of 2026-06-30 (10-Q cover,
  filed 2026-08-07, accession `0001051512-26-000063`); the balance sheet gives 107,573 thousand Common and 7,543
  thousand Series A outstanding, 115,116 thousand in all. `python Screens/cover_shares.py TDS` parsed no cover count
  ("read the filing by hand"); the count above is read by hand. "Series A Common Shares are convertible on a
  share-for-share basis into Common Shares", carry ten votes a share in matters other than the election of directors, and
  elect eight of the twelve directors (10-K FY2025, equity note); the two classes are added for the per-share arithmetic.
- **Market cap:** 115.116M × $35.11 = **$4,042M** (common equity only). Ahead of it: preferred, 44,400 shares at
  $25,000 liquidation value = **$1,110M** (6.625% Series UU, 16,800 shares, issued March 2021; 6.000% Series VV, 27,600
  shares, issued August 2021; 10-K FY2023, `0001051512-24-000010`), dividends $69.2M a year; at the quoted depositary
  prices the preferred trade at about $821M.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): TDS 10-K FY2025, filed 2026-02-24, `0001051512-26-000011`; TDS 10-Q Q2 2026,
  filed 2026-08-07, `0001051512-26-000063`; TDS proxy (DEF 14A) filed 2026-04-08, `0001051512-26-000024`; Array 10-K
  FY2025, filed 2026-02-20, `0000821130-26-000012`; Array 10-Q Q2 2026, filed 2026-08-07, `0000821130-26-000046`;
  TDS 8-Ks of 2026-01-13 (`0001051512-26-000002`, AT&T spectrum close, Array $10.25 special dividend), 2026-05-08
  (`0001051512-26-000039`, all-stock proposal for the Array minority, exhibits 99.1 and 99.2), 2026-06-01
  (`0001051512-26-000055`, Verizon spectrum close, Array $11.00 special dividend), 2026-09-02 (`0001051512-26-000070`,
  proposal withdrawn, buybacks to restart); for the ten-year record the TDS 10-Ks FY2023 (`0001051512-24-000010`) and
  FY2021 (`0001051512-22-000013`) and the annual-report exhibits 13 to the 10-Ks FY2019 (`0001051512-20-000014`),
  FY2017 (`0001051512-18-000009`) and FY2015 (`0001051512-16-000077`); the FY2024 10-K (`0001051512-25-000011`) was
  fetched and searched only.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025,
  $589,889 thousand in the filed cash-flow statement (continuing $338,284 plus discontinued $251,605;
  `0001051512-26-000011`) against $590M in `tools/run.py`. Agrees.
- **`python tools/run.py TDS` arithmetic lines only** (Part VII; nothing it prints as a rule or verdict is used; output
  saved as `_research 2026-10-05 TDS/run_py_output.txt`). OCF less SBC less capex: 2023 $478M, 2024 $761M, 2025
  $170M; capex alternate with the $359M of Array dividends to minority holders: 2025 −$188M. **These years are not the
  business that is for sale today.** Until 1 August 2025 the cash flows include the UScellular wireless business sold to
  T-Mobile; from then on they include gains and taxes on spectrum sales. The tool's three-year and five-year means are
  therefore not used as owner cash; the parts are read separately below (the tool's own warning says the window spread is
  "part of the range, not a tiebreak").

**What TDS is today, from the filings.** Three operating parts and two stocks of assets.
1. **TDS Telecom** (100%): wireline, cable and fiber broadband in small to mid-sized and rural towns in 30 states; 1.05
   million connections at 2026-06-30; FY2025 operating revenues $1,038.4M, Adjusted OIBDA $318.9M, operating income
   $19.7M after a $23.1M gain on sales of markets, capex $406.4M; 2026 capex guidance $550M to $600M in the 10-K, and
   $625M to $675M for TDS in all in the 10-Q, of which Array $25M to $35M.
2. **Array Digital Infrastructure** (81.9%; 70.79M of 86.48M shares): the former UScellular. It sold its wireless
   operations to T-Mobile on 1 August 2025 for $4,293.8M ($2,628.8M cash and $1,665.0M of debt assumed) and now owns
   4,456 towers (tenancy 0.98 at 2026-06-30, counting T-Mobile's committed minimum of 2,015 sites and excluding about
   1,800 interim sites T-Mobile may cancel at will through January 2028), holds minority stakes in wireless
   partnerships managed by Verizon and AT&T (equity earnings FY2025 $173.8M; distributions to TDS FY2025 $215.6M,
   including $67.8M of specials), and holds spectrum: $1,584.7M at book not under any sale agreement, "primarily
   C-Band", plus two small T-Mobile sales pending ($10.2M and $19.6M).
3. **Corporate** ("All other"): FY2025 operating loss $24.5M.
4. **Cash** (consolidated $2,194.0M at 2026-06-30, against accrued taxes $260.1M and debt principal $694.1M, nearly all
   of it Array's: a $325M CoBank term loan and $363.9M of retained senior notes). "TDS does not have direct access to
   Array cash" (10-Q). The spectrum proceeds reached TDS as Array special dividends: $23.00 (August 2025), $10.25
   ($725.6M to TDS, February 2026), $11.00 ($778.7M to TDS, June 2026).
5. **Preferred** $1,110M at liquidation value, ahead of the common.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: would I be content to own this "if the market closed for five years"
**[M1997-109]**? TDS today is chiefly a pile of sale proceeds and a fiber-building telephone company; owning it closed
for five years means owning whatever the controlling family builds with the proceeds, since the common holders cannot
direct the cash (Q5 facts below). The market serves and does not instruct **[M2006-077]**: the price of $35.11 is
read only against value, never as evidence that the spectrum sales have released value. Margin of safety: if the
case needs pencil and paper, "it’s too close to think about" **[M1996-084]**; a sum-of-parts holding company with five
parts and a preferred ahead of the common is a pencil case by construction, and that is written down here before any
figure. The analyst's habits: look for "what’s wrong in things" **[M2025-013]**; scuttlebutt aimed "to possibly reject
your original hypothesis" **[M1998-144]**; state the other side's case better than its holder before disagreeing
**[M2016-055]** (done at Q2).

**Contrary evidence, written down as found** **[M1997-127]**:
- *Against the business:* TDS Telecom's goodwill of $547M was written off in full in Q4 2023 (10-K FY2023,
  `0001051512-24-000010`); the same Telecom segment's operating income has gone from $110M (2020 and 2021) to $19.7M
  (2025, including a $23.1M gain on sale) to a loss of $12.0M in H1 2026, while its capex ran $368M to $577M a year.
- *Against the business:* the Array towers carry 0.98 tenants per tower (10-Q), and DISH Wireless, a tenant, stopped
  paying and filed for bankruptcy in June 2026; about 1,800 interim T-Mobile leases are expected to be cancelled by
  January 2028 (Array MD&A).
- *Against the owners' interest:* in May 2026 TDS proposed to buy the Array minority in an all-stock deal "at-market",
  while holding a $523.9M buyback authorization; it withdrew on 1 September 2026, "not able to reach agreement on the
  form of consideration and value" (8-K `0001051512-26-000070`).
- *For the business, found and kept:* TDS Telecom's fiber connections grow (incumbent fiber +11%, expansion fiber +27%
  year on year at 2026-06-30), 1Gig+ service reaches 80% of the footprint, and E-ACAM regulatory support runs to 2038;
  the remaining C-band spectrum is a saleable asset with a book value of $1,584.7M; TDS ex-Array holds about $1.8B of net
  cash at 2026-06-30 (computed below).

## THE STANDING RULE
Owning TDS common bought with the buyer's own money, unlevered and sized so that a fall of half would not force a sale,
puts the buyer at no risk of ruin; "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and
nothing in this name calls for it. The rule is the buyer's conduct, not the target's; TDS's own debt and preferred are
Q9's subject and are recorded below as facts only.

---
## Q1. CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in that particular
business, and evaluating how predictable they were first" **[M1998-044]**. A holding company is understood by its parts:
"a part that cannot be, and that matters, keeps the whole outside the circle" (the framework's CONVENTION, Q1). The row
the framework carries OPEN against that reading is **[M2023-031]**, the trading houses understood "as a group".

| Part | What it earns from | Key variables | Foreseeable from the filings? |
|---|---|---|---|
| TDS Telecom | monthly broadband, video and voice subscriptions in 30 states; wholesale access; E-ACAM support to 2038 | homes passed with fiber, penetration of fiber passings, revenue per connection, the decline rate of copper, cable, voice and video, capex per passing, the E-ACAM build obligation (about 270,000 locations, 10-K FY2023) | the variables are named, measured and reported every quarter; their direction is foreseeable (copper and legacy decline, fiber grows, capex stays heavy); their *level* in ten years turns on the castle (Q2) |
| Array towers | rent per tenant per tower with escalators | tenants per tower, the T-Mobile MLA (2,015 sites for at least 15 years, about 600 extended for 15 years), the interim sites leaving by January 2028, ground rent | yes: contracted rents, a three-carrier customer base named by the filer |
| Wireless partnerships | cash distributions from minority stakes in partnerships run by Verizon and AT&T | the distributions received | yes, as cash received: $180M, $145M, $150M, $169M, $148M ordinary in 2021 to 2025 (XBRL `EquityMethodInvestmentDividendsOrDistributions`, specials of $67.8M taken out of 2025 per the 10-K) |
| Spectrum held | nothing until sold | the price a carrier will pay | a one-time sale value, not an earnings stream; stated at book |
| Cash and preferred | | | stated values |

**Does the industry change too fast for a ten-year fix?** Wired broadband is not a new technology, and the change that
matters (fiber replacing copper and coaxial cable, fixed wireless and satellite as substitutes, which the filer names) is
visible in the filer's own numbers rather than hidden in a laboratory. I can say where each variable is heading; what I
cannot do from Q1 alone is say whether the fiber build will earn its capital, and that is the castle question, which
the routing gives to Q2: rapid change closes Q1 only where it puts the ten-year economics "out of reach" (framework Q1,
the routing fixed), and at Q2 a castle "being filled in on the evidence closes OUT" (framework Q2, the routing with Q1).

**Doubt written down.** "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**. My doubt is not whether I can see the economics of a rural broadband network (I can: a wire to the house,
a monthly bill, a cable or wireless rival, a heavy build cost), but whether its competitive position holds; that doubt is
the subject of Q2 and is answered there on the evidence. Test 3, "do I understand enough about this business so that the
financial statements will tell me" what the future ones will look like **[M2008-033]**: for Telecom the segment tables
give revenue by market type, connections by technology, Adjusted OIBDA and capex every quarter since at least 2018, so
the statements do tell me what to watch.

**VERDICT: IN** (the parts are understandable economically and the deciding variables are reported; the doubt is the
castle's, and is carried to Q2). **[M2012-065]**, **[M1998-044]**, **[M2008-033]**.

## Q2. WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The question is asked of the
part that matters most to the earnings and to the capital: TDS Telecom, 84.5% of FY2025 continuing operating revenues
($1,038.4M of $1,228.2M) and about 95% of the 2026 capex guidance. The towers are read beside it.

**CONVENTION (this run's, confessed):** the by-parts reading the framework states for Q1 is carried into Q2: a part that
matters, whose castle is shown open on the evidence, closes the whole OUT. Rationale: the 1995 row asks the moat
first and the use of the proceeds after ("then if we feel good about the moat, then we try to figure out whether [...]
he’s likely to do something stupid with the proceeds" **[M1995-038]**), and at TDS the proceeds of the asset sales are
being sent into this part.

### TDS Telecom, the castle tests, each with its filing fact

**The ten-year record of the segment** (10-K segment and non-GAAP tables; $M; operating income as reported; "ex" removes
the 2023 goodwill impairment and the gains on sales of markets):

| Year | Revenue | Adj. OIBDA | D&A | Operating income | ex impairment and gains | Capex | Source |
|---|---|---|---|---|---|---|---|
| 2018 | 927 | | | 93 | 93 | 232 | ex. 13 FY2019 `0001051512-20-000014` |
| 2019 | 930 | | | 107 | 107 | 316 | same |
| 2020 | 976 | 314 | 203 | 110 | 110 | 368 | 10-K FY2021 `0001051512-22-000013` |
| 2021 | 1,006 | 310 | 198 | 110 | 110 | 411 | same |
| 2022 | 1,020 | 288 | 215 | 66 | 66 | 556 | 10-K FY2023 `0001051512-24-000010` |
| 2023 | 1,028 | 279 | 245 | (523) | 24 | 577 | same ($547M goodwill impairment) |
| 2024 | 1,061 | 340 | 271 | 105 | 56 | 324 | 10-K FY2025 `0001051512-26-000011` ($49.1M gain on sale) |
| 2025 | 1,038 | 319 | 300 | 20 | (3) | 406 | same ($23.1M gain on sale) |
| H1 2026 | 498 | 140 | 146 | (12) | (12) | 305 | 10-Q `0001051512-26-000063` |

Eight years, about $3.2B of capex (2018 to 2025), revenue up 12%, operating income from about $100M to about nothing. 2015
to 2017 revenue of $1,158M, $1,151M and $1,140M (ex. 13 FY2017, `0001051512-18-000009`) included the hosted and managed
services unit later separated, so it is not on the same basis and is not joined to the table.

1. **The money test: could a well-funded attacker take it?** "if I had a hundred million dollars and I wanted to go in
   and take on See’s Candy, could I do it? [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**.
   The filing answers it twice, both times yes. TDS itself is the attacker with money in its "Expansion Markets",
   defined as "markets utilizing fiber networks in areas where TDS does not serve as the cable or incumbent service
   provider": expansion residential revenue rose 34% in 2025 to $152.5M and 25% in Q2 2026. And TDS is the attacked in
   its own cable markets, where cable residential revenue fell 9% in 2025 and 10% in H1 2026 and cable broadband
   connections fell from 188,200 to 176,100 in the year to June 2026. Broadband in a town is the failing answer's
   airline: "you can create another airline. [...] Very easily, and you have people that like to do it." **[M2013-054]**.
   The filer lists its rivals as "wireline providers, cable providers, fiber overbuilders, VoIP providers, satellite
   providers, wireless providers and providers using other emerging technologies" (10-K FY2025, Item 1).
2. **Pricing power and the agony before a rise.** "you can almost measure the strength of a business over time by the
   agony they go through in determining whether a price increase can be sustained" **[M2005-020]**. Residential revenue
   per connection rose 1% in 2025 "due primarily to price increases" and 1% in H1 2026 "due primarily to price increases,
   partially offset by promotional activity and customer product mix" (10-K; 10-Q); the filer says it "continues to improve
   the efficiency of its cost structure to enhance its ability to compete with price-based initiatives from competitors"
   (10-K, Item 1). A business whose price rises are eaten by promotions and whose cost programme exists to answer rivals'
   prices is the prayer session, not the toll bridge.
3. **Unit volume.** Total connections fell 4% in 2025 (1,126,300 to 1,079,500) and 5% in the year to June 2026
   (1,108,800 to 1,054,200); residential broadband rose only 2% though fiber was added; incumbent copper broadband fell
   22% and 27%; voice 12% and 16%; video 8% and 9%; commercial 9% and 11%. Part of the 2025 fall is divestiture (19,400
   connections); the rest is the business.
4. **The low-cost position.** "Being the low-cost producer, for example, is a terribly important moat." **[M2018-043]**.
   The filer's own risk factor reads the other way: "TDS’ lack of scale relative to larger competitors that may have greater
   financial and other resources than TDS could cause TDS to be unable to compete successfully" (10-Q risk factors). No
   claim of a cost advantage over cable or the wireless carriers is made anywhere in the filings read.
5. **Would the customer still choose it over the low bid?** Subscriptions are month to month: customers "may cancel their
   subscriptions at the end of any monthly term without incurring penalties" (10-K, revenue note). Residential fiber churn
   1.2% a month and total broadband churn 1.7% a month in Q2 2026, both up from 1.1% and 1.5% a year earlier (10-Q).
6. **Widening or narrowing?** "whether it’s likely to widen further or shrink on you" **[M1999-108]**. Narrowing, on four
   readings of the segment: the operating income column above; the goodwill impairment of the whole Telecom reporting unit
   in 2023, management's own finding that the unit was worth less than its carrying value; Adjusted OIBDA margin from
   32% (2020) to 31% (2025) to 28% (H1 2026); and the incumbent markets, where even with 52% of incumbent addresses now on
   fiber, incumbent residential revenue fell 6% in 2025 and 10% in H1 2026 (part of it divestiture). The newspaper row's
   word fits: the industry "has lost still another notch" **[L1995-023]**.
7. **What could destroy, modify or reduce it, five to fifteen years out?** "what can happen [...] that will destroy, or
   modify, or reduce the economic strengths" **[M2000-014]**: the filer names it, "Increasing competition in the wireline
   industry, including fixed wireless and satellites" and "Artificial intelligence advancements may put TDS at a
   competitive disadvantage" (10-Q risk factors), and the regulatory support it lives partly on: "There is no assurance
   that these financial support payments will continue" (10-K, Item 1A).
8. **Is the moat maintained or rebuilt?** "A moat that must be continuously rebuilt will eventually be no moat at all."
   **[L2007-005]**. The copper plant is being replaced with fiber; the cable plant was upgraded with DOCSIS; the filer
   says "changes in technology have required substantial investments in TDS’ networks to remain competitive; this is
   expected to continue in 2026 and future years" (10-Q, Capital Expenditures). Capex ran above D&A in every year from
   2020 to 2025, by $53M (2024) to $341M (2022) a year, and 2026 guidance is about twice D&A. The spending is compulsory: "you have to spend
   money like crazy if it’s attractive to spend money, and you have to spend it the same way if it’s unattractive"
   **[M1998-128]**.

**The competitor row** (same metric, operating income over revenue, and capex over revenue, from the competitors' own
10-K XBRL facts, first-filed vintage, read as transcription; latest 10-K accession named; the competitors' filings were not
read beyond the tagged statements, which is flagged):

| Company | Span | Operating margin, start → end | Capex / revenue, recent | Shape | Latest 10-K |
|---|---|---|---|---|---|
| TDS Telecom | 2018-2025 | 10.0% → 1.9% (−0.3% ex gain); H1 2026 −2.4% | 39% (2025), 56% (2023) | fiber build funded by parent | `0001051512-26-000011` |
| Shentel (SHEN) | 2020-2025, continuing operations after its wireless sale to T-Mobile | −0.5% → −6.4%; positive in one year of six (2023, 3.5%) | 100% (2025: capex $359M, revenue $358M) | the same plan: wireless sold, proceeds into fiber (Glo Fiber) | `0000354963-26-000125` |
| Consolidated Communications (CNSL) | 2009-2023 | 17.5% → −14.2% (2020 10.4%, 2022 −7.8%) | 52% (2022), 46% (2023) | rural ILEC, fiber build from 2021 | `0001558370-24-002414` (FY2023, last in the record) |
| Frontier (FYBR) | 2008-2024 | 28.7% → 5.9% | 47% (2024), 56% (2023) | rural ILEC, net losses 2015 to 2020 and 2024 in the tagged record, fiber build | `0001562762-25-000028` (FY2024) |

Over every span the rural-wireline operators that turned to fiber show falling operating margins while capex ran at a
third to all of revenue. No operator in the row shows the fiber build lifting returns over its own span. Asked as the
competitor test, "which one would it be, and why?" **[M2025-043]**: none of the four is the one I would want to own for
ten years on these numbers, and I would not know which to short, because they look alike.

### The towers, read beside it
Towers can be a castle: American Tower's operating margin went from 30.0% (2017) to 45.5% (2025), SBA's from 23.7%
(2016) to 47.7% (2025), Crown Castle's from 24.2% (2016) to 48.7% (2025) (XBRL, 10-Ks `0001053507-26-000035`,
`0001034054-26-000002`, `0001051470-26-000016`); the Array filing says zoning "can block tower construction". Array's
towers do not yet show that castle. Tenancy is 0.98; tower operating income in H1 2026, taking out the $566.5M of
spectrum gains, $4.7M of disposal losses and $7.6M of strategic-review costs, was about $5.9M on $106.1M of revenue,
about 5.5%, and that revenue includes $14.9M of interim T-Mobile rent that is expected to run off by January 2028 (Array
10-Q). Its customers are three carriers, and the fourth (DISH) has failed. "one competitor is frequently enough to ruin a
business" **[M2012-108]**; here one *customer's* consolidation made the towers what they are. I do not close the file on
the towers: the low tenancy may be cured by colocation, and their castle is a TOO HARD question at worst. The file closes
on Telecom.

### The other side's case, stated as well as I can **[M2016-055]**
Fiber is the last wire a town will need; once TDS's glass is in the ground, a second fiber builder will not come
because the town cannot pay for two, cable must spend to keep up, and fixed wireless and satellite are capacity-limited.
The present losses are build-phase accounting: depreciation on new fiber before penetration matures, legacy declines
that will end when copper is gone, and E-ACAM support that pays for rural build to 2038. On that view the segment's
falling profit is the J-curve, not the moat filling in.

**Why I do not accept it on the evidence.** (a) The J-curve claim is a projection; the record shows the segment's
profit falling for five years while the build ran, and the four operators in the competitor row that made the same
claim show the same falling margins over their whole spans. (b) TDS's own entry into other towns' broadband with fiber is
proof that a town with an incumbent wire can be entered with money, the failing answer of **[M2011-015]**. (c) Where TDS
has already put fiber in its own incumbent towns (52% of incumbent addresses), incumbent residential revenue is still
falling. (d) Churn is rising, not falling. (e) The filer itself names fixed wireless and satellite as competition. The
evidence is not silence about the future (which would be TOO HARD); it is a measured record of a castle losing ground.

**VERDICT: OUT.** TDS Telecom's castle is shown on the filed evidence to be filling in: rivals with money enter and take
customers (the airline answer, **[M2013-054]**, failing **[M2011-015]**), price rises are eaten by promotions (the prayer
session, **[M2005-020]**), connections and legacy revenue fall, operating income has gone from about $110M to a loss
while some $3.2B of capital went in, and the reporting unit's goodwill was written off in full; the moat is being rebuilt,
not widened (**[L2007-005]**, **[M1999-108]**). "If you really think a business is declining, most of the time you should
avoid it." **[M2012-062]**. By the framework's Q2 routing, a castle "being filled in on the evidence closes OUT"; the
box is the rows' "out" of the three **[M2006-013]**.
Price does not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.
The file closes here.

---
## Q3. HOW MUCH CAPITAL MUST GO IN. WEIGHING.
**NOT REACHED** (the file closed OUT at Q2). Facts gathered, no weighing: the company's own pay metric, "Return on
Capital", was 4.0% (2021), 1.8% (2022), −1.7% (2023), 3.7% (2024) and 1.1% (2025) (proxy, Pay Versus Performance,
`0001051512-26-000024`).

## Q4. DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion.
**NOT REACHED as a verdict.** The template asks for the balance sheets in Step 0 when the file closes before Q4; they
were read, and are recorded here as reading only. "balance sheets over an 8 or 10 year period before I even look at the
income account" **[M2025-032]**.

**Ten year-ends, consolidated** (`tools/run.py` first-filed XBRL table, transcription; $M), with what moved and why, from
the filings:

| Year-end | Assets | Equity (incl. preferred from 2021) | Cash | Goodwill | Retained earnings | Debt on the face |
|---|---|---|---|---|---|---|
| 2016 | 9,446 | 4,144 | 900 | 766 | 2,454 | 2,445 |
| 2017 | 9,295 | 4,269 | 619 | 509 | 2,525 | 2,457 |
| 2018 | 9,783 | 4,560 | 921 | 509 | 2,656 | 2,439 |
| 2019 | 10,781 | 4,653 | 465 | 547 | 2,672 | 2,326 |
| 2020 | 12,525 | 4,804 | 1,429 | 547 | 2,802 | 3,429 |
| 2021 | 13,493 | 5,927 | 367 | 547 | 2,812 | 2,934 |
| 2022 | 14,550 | 5,849 | 360 | 547 | 2,699 | 3,750 |
| 2023 | 13,921 | 5,202 | 236 | 0 | 2,023 | 4,106 |
| 2024 | 13,682 | 5,091 | 364 | nil | 1,849 | 4,082 |
| 2025 | 8,398 | 4,802 | 766 | nil | 1,694 | 829 |
| 2026-06-30 (10-Q) | 8,383 | 5,171 | 2,194 | nil | 2,022 | 680 |

- **What the figures say.** Assets rose by about $5B from 2019 to 2022 and fell back by $5.5B in 2025. The rise was
  spectrum and debt: UScellular paid $1,283M for C-band licenses in Auction 107 (2021) and $580M for 3.45 GHz licenses in
  Auction 110 (paid January and February 2022), financed in part with $1B of 6.25% and 5.5% senior notes due 2069 and
  2070 issued in 2020 (10-K FY2021); TDS issued $1,110M of perpetual preferred in 2021. The fall is the T-Mobile sale.
- **Goodwill** went to zero in two steps: $262M in 2017 (UScellular and the hosted and managed services unit, ex. 13
  FY2017) and $547M in 2023 (TDS Telecom). Every dollar of goodwill on the 2016 balance sheet has been written off.
- **Retained earnings** fell from $2,454M (2016) to $1,694M (2025): over ten years the company earned less for its
  common holders than it paid them in dividends (common dividends $657M over 2016 to 2025, XBRL `DividendsCommonStock`;
  cut to $0.16 a share a year from mid-2024). The 2026 rise to $2,022M is the spectrum-sale gains.
- **Common equity** (equity less the $1,074M carrying value of the preferred) was $3,728M at 2025 against $4,144M at
  2016: less common equity after ten years, on a weighted share count that rose from 110M (2016) to 115M (2025).
- **Debt** rose to $4.1B in 2023 and was cut to $0.7B with the sale proceeds; what is left is Array's.
- **What they can't say.** The book value of the remaining spectrum ($1,584.7M) says what was paid, not what a carrier
  will pay; Array recorded spectrum impairments of $136.2M in 2024 and $47.7M in 2025 (Array MD&A). The equity-method
  investments carry $475M on the books against about $150M a year of distributions; the book understates them.
- **The income account in the filer's own mouth.** The segment measure reported to the chief operating decision maker
  is "Adjusted EBITDA" (10-Q, Supplemental Information), which adds back depreciation that runs at $300M a year at
  Telecom alone. Not weighed here (file closed).

## Q5. WHO RUNS IT. **NOT REACHED.** Facts gathered, no verdict:
- Control: the TDS Voting Trust (1989) holds 95.6% of the Series A shares, elects eight of twelve directors, and holds
  56.8% of the vote on other matters; TDS is a "controlled company" under NYSE rules (proxy). Three Carlson trustees sit
  on the board; Walter C. D. Carlson became President and CEO on 1 February 2025 (also Chair); LeRoy T. Carlson, Jr. is
  Vice Chair; Anthony J. M. Carlson became CEO of Array in November 2025 (proxy).
- Pay: Walter Carlson's terms are a $850,000 salary, a target bonus of 115% of salary and a $3,000,000 long-term target;
  LeRoy Carlson, Jr.'s summary-compensation total was $9.6M (2024) and $9.7M (2023), compensation actually paid $38.9M
  (2024); the outgoing TDS Telecom CEO received a $2,000,000 lump sum on stepping down in 2025 (proxy).
- Five-year TSR in the proxy: $100 at end-2020 became $260.75 at end-2025, against $123.65 for the peer index; the long
  record on the aggregator's monthly closes (flagged): $51.32 (December 2006), $26.72 (December 2015), $12.69 (December
  2022), $35.11 today, plus dividends.

## Q6. WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. **NOT REACHED.** Facts gathered, no verdict:
- The proceeds are going into Telecom's fiber build ($625M to $675M of 2026 capex) and into a buyback programme
  ($523.9M authorized; 2,843,427 shares bought in 2025 at an average $38.03; no price limit stated in the filings read).
- In May 2026 TDS proposed to buy the Array minority for 0.86 TDS share per Array share, "an at-market offer", all stock,
  while stating it "will not entertain any third-party offers for Array or its assets" (8-K `0001051512-26-000039`); it
  withdrew the proposal on 1 September 2026 (8-K `0001051512-26-000070`). The framework's one Part A STOP concerns an
  all-stock deal *made* by an acquirer whose stock is below value **[L2009-019]**; this one was proposed and withdrawn,
  and whether TDS stock was then below value is a Q7 question this file does not reach.
- The common dividend was cut from $0.185 a quarter (2023) to $0.04 (from Q2 2024); the board says future dividends are
  uncertain (10-Q).

## Q7. WHAT IS IT WORTH. **NOT REACHED.** Reported at the owner's request, all **COMPUTATION - NOT A CLEARANCE**:
These figures carry no entry language and clear nothing. Script: `_research 2026-10-05 TDS/parts.py`. Anchor 2026-06-30
balance sheets; sovereign 5.66%; floor about 10% pre-tax (framework CONVENTION, Q7).

**Read by parts** (the framework's Q7 CONVENTION built per part, because the consolidated five-year window mixes a sold
business with sale gains):
- **Stated values, to the common.** TDS ex-Array net cash = consolidated cash $2,194.0M less accrued taxes $260.1M less
  debt principal $694.1M, less Array's own net cash (cash $416.4M − accrued taxes $317.4M − debt $688.9M = −$589.9M):
  **$1,830M**. Plus 81.86% of Array's net cash (−$483M) and of its spectrum at stated values ($1,584.7M book plus
  $29.8M of pending contract prices: $1,322M). Less the preferred at liquidation value ($1,110M). **= $1,558M, $13.54 a
  share.** Pre-tax: no tax is taken on future spectrum gains or on the $601M consolidated deferred tax liability.
- **Streams, pre-tax, $M a year:** partnerships, distributions received $133M (H1 2026 × 2) to $158M (2021 to 2025
  ordinary average; no growth shown), at 81.86%; towers −$9M (H1 2026 run-rate without the interim T-Mobile rent, less
  $30M capex) to +$36M (H1 2026 Adjusted OIBDA × 2 less $30M capex), at 81.86%; corporate −$30M to −$40M; **Telecom,
  two variants as the convention requires**: owner cash after *all* capex, five-year average 2021 to 2025 = −$148M
  (−101, −268, −298, +16, −87); after D&A instead of capex, five-year average = +$61M (112, 73, 34, 69, 19), falling.
- **VALUE RANGE (depreciation variant for Telecom):** $24.12 (no-growth low streams, Telecom at nil) to **$42.78**
  (high streams, Telecom at its D&A average carried flat) a share, about 1.8 to 1. **With Telecom on the all-capex basis
  the convention prescribes, the low end falls to $0.34**, and the range is wider than a hundred to one, which by the
  framework's three-to-one rule is TOO HARD on the arithmetic alone. Against **$35.11**: the price sits inside the
  narrower range and nowhere near a screamer.
- **FAIR PRICE: about $24.50** a share. Rule: the stated-value net assets ($13.54) plus the central pre-tax streams
  attributable to the common ($126M a year: the midpoint of each part, Telecom at the midpoint of nil and its D&A
  average) capitalised at the 10% pre-tax floor. Tax treatment: pre-tax throughout, consistent with the floor as the
  framework states it; no tax is provided on future spectrum gains.
- **CHEAP PRICE: about $6** a share. Rule (this run's, confessed): every part at its worst variant shown (partnerships
  $133M, towers −$9M, Telecom on the all-capex basis −$148M, corporate −$40M; −$86M a year in all), capitalised at the
  10% floor, plus the stated-value net assets. Below it the purchase would clear the floor even if the fiber build never
  earns and keeps consuming cash at its five-year rate; no pencil would be needed.

## Q8, Q9, Q10, Q12: **NOT REACHED.**
Q9 facts gathered, no weighing: debt principal $694.1M, all Array's, maturities $293M in 2030 and $366M thereafter
(10-Q market-risk table); covenants of 3.50 times leverage and 3.00 times interest coverage; ratings Ba1 / BBB- / BB+
(10-K); the preferred is perpetual and ranks ahead of the common; Array tenants are concentrated, "particularly reliant on
its relationship with T-Mobile" (10-Q risk factors).

---
## THE BOX
**OUT at Q2.** TDS Telecom, the part that earns 84.5% of continuing revenue and receives nearly all the capital, has a
castle shown on the evidence to be filling in: rivals enter with money, prices rise only against promotions, connections
and legacy revenue fall, the segment's operating income fell from about $110M to a loss while about $3.2B of capex went
in, and its goodwill was written off in full; four rural-wireline peers show the same over their whole spans. Q3 to Q12
not reached. COMPUTATION - NOT A CLEARANCE: value range $24.12 to $42.78 a share on the depreciation variant (low end
$0.34 on the all-capex basis), fair about $24.50, cheap about $6, against $35.11.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Not committed after each: the
      dispatching instruction for this run forbids commits; the file was written through Q2 before the computation
      sections were added.*
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      checked against that row); every filing fact has its accession; numbers without a row or filing are labelled
      CONVENTION or computation.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance; the Q7 figures
      are headed COMPUTATION - NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): Telecom shown after all capex and,
      beside it, after D&A; partnerships counted as distributions received; the sovereign from the Treasury; the price
      and the preferred and Array quotes flagged as aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, including the evidence for the business.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` run after writing: **PASS** (TEST RUNS: phantom ids in 0 files; V5 SCOPE: 0
      citations outside the v5 sources). A separate script (`_research 2026-10-05 TDS/check_ids.py`) found no E-ids,
      30 distinct v5 ids all present in the ledger, and every quoted fragment immediately beside an id inside that row.
- [x] The protocol's required heading (operator rule 3) is written with a hyphen in place of its dash, under the
      dispatching instruction's no-em-dash rule; the words are unchanged.
- Weak points, honestly: the competitor rows are XBRL transcription, not read filings; the 2018 and 2019 Telecom figures
  are read from a badly rendered exhibit and are the segment's wireline-plus-cable totals; the tower operating income
  for H1 2026 is my recast from the segment table, not a filer figure; "the part that matters" is a judgment made under
  this run's own CONVENTION.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The by-parts rule stops at Q1.** The framework reads a holding company by its parts for understanding (Q1) and
counts equity-method income as dividends (Q4), but says nothing about the castle of a holding company whose parts have
different castles. TDS has an open castle (Telecom), an unproven one (towers at 0.98 tenancy), passive partnership stakes
with no castle of their own to judge, and stocks of cash and spectrum. I carried the Q1 rule into Q2 and confessed it as
this run's CONVENTION; a second analyst could as well have closed TOO HARD on the towers, or treated TDS as a cash box
and skipped Q2. (2) **OUT and TOO HARD for a castle under construction.** The fiber half of Telecom is new; Q2 says a
castle "being filled in on the evidence closes OUT" and one "whose future cannot be judged closes TOO HARD", but gives
no rule for a part that is being *built*, where the bull case is a projection and the record is a falling one. I chose
OUT because the record is measured and the peers' records agree; the line is a judgment. (3) **The Q7 range convention
breaks on a builder.** "the cash input deducts all capital spending" gives Telecom a negative value that grows with the
build, and the depreciation variant gives a positive one; the convention asks for "the maintenance judgment stated where
the filing allows one", and TDS's filing does not split maintenance from growth capex, so the range is either 1.8 to 1 or
more than a hundred to one depending on a choice the framework leaves open. (4) **No rule for cash the buyer cannot
reach.** Most of TDS's value today is cash, spectrum and partnership distributions controlled by a voting trust; the
framework values stated assets at stated values and has no line for cash that a controller has said it will spend on the
business the analyst just found open. (5) `cover_shares.py` parsed no cover count for TDS or Array; read by hand.
