# Company Run — Duke Energy Corporation (NYSE: DUK) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template before any fetch.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-22, after the run was committed (eac4982f): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Dispatched run.** Written by a dispatched analyst under the canonical brief, with the brief's one stated departure (the
lines of evidence are derived by the analyst from Items 1, 1A and 7 of the 10-K, below). Research folder:
`Test Runs/_research 2026-10-18 DUK/` (notes, the run.py print, the fetch and check scripts; raw filings in its ignored
`cache/`).

**Resumed 2026-10-22.** The session of 2026-10-18 closed after Q1 (stopped by a usage limit or session end, not an error;
last commit "DUK run: Step 0, foundations, standing rule, Q1 IN"). This analyst resumed from Q2 on 2026-10-22 under the same
brief, read the run file and `notes.md` first, and reused the research folder without refetching: Step 0's price, share
count, sovereign and filings stand as dated 2026-10-16 and 2026-10-18 (the price is not refreshed, so that every figure in the
file is on one date). The lines of evidence written in Step 0 by the earlier session are kept as written. The resume
session's contamination is declared below as item (6).

**Contamination, declared and not used.** (1) The session's opening git status listed the subjects of the five latest
commits, which concern another company's run of today (a utility closed at Q7, with the topics of its framework notes
named: net or gross debt credit, whose debt share, credit inside the maintenance case); I read the subjects only, used none
of its figures or resolutions, and decided the same questions below from the framework text. (2) A directory listing of
`Test Runs/` made to check that no DUK file existed showed the file names of other companies' runs dated today (many
utilities); none was opened. (3) The project memory index loaded at session start carries one line on queue state (counts of
gate-clearers and reviews owed, nothing about this name). (4) `tools/_cache/duk_tmp/`, the session's working directory,
already held a Duke 10-K, a submissions file and four 8-Ks when the run began (timestamped 18:46 today, not made by this
analyst); I did not use them and fetched every filing afresh from EDGAR into my own `cache/`. (5) The adopted case file
behind Q7's "The regulated utility" paragraph was not opened, because it may discuss named utilities; the paragraph is
applied from the framework text alone. (6) *Resume session, 2026-10-22:* the opening git status again listed five recent commit
subjects, which name another utility's run closed OUT at Q7 with its range, fair price and framework-note topics (net or
gross debt credit, whose debt share, credit inside the maintenance case, spin-off in the window); and the session's memory
index carries one queue-state line (counts, no name). I used none of their figures or resolutions; where this run meets
the same questions it decides them from the framework text and says how.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $121.47 (close 2026-10-16, the last trading day before the run date; `tools/run.py` quote, an aggregator,
  flagged per operator rule 5: live quote only).
- **Shares by class:** one class of common, **779,702,193** shares outstanding at July 31, 2026, from the cover of the 10-Q
  for the period ended 2026-06-30 (accession `0001326160-26-000040`, filed 2026-08-04; `python Screens/cover_shares.py DUK`).
  The script also prints 100 and 89,663,086 shares: these are the covers of the subsidiary registrants (Progress Energy and
  Piedmont, 100 each, and Duke Energy Ohio, 89,663,086, all owned by Duke Energy) in the combined filing, not Duke shares.
  Check against the balance sheet: "780 million and 778 million shares outstanding at 2026 and 2025" (the 10-Q's condensed
  balance sheet); no treasury stock line. Filed after the 10-Q: the 8-K of 2026-08-13 (accession
  `0001104659-26-095903`) records 40,000,000 equity units of $50 each, whose stock purchase contracts settle into common
  "no later than August 1, 2029" (not shares today); the FY2025 10-K (Note 20) records 4,238,007 shares priced under
  2025 ATM forward contracts at initial forward prices of $116.02 to $117.94, to settle "by December 31, 2026" (not yet
  issued at 2026-06-30 by the 10-Q's count). The 3.000% convertible notes due 2029 convert at 6.2277 shares per $1,000, a
  conversion price of about $160.57 (10-Q), above the price. The count used is **779.702M**; the forward shares and the
  2029 purchase-contract shares are carried as a dilution note at Q6, not added.
- **Market cap:** 779.702M x $121.47 = **$94,710M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield on the US Treasury daily par yield
  curve, 10/16/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the FY2025 10-K (`duk-20251231.htm`, filed 2026-02-26, accession
  `0001326160-26-000014`): Item 1, Item 1A, Item 7, the consolidated statements, Notes 2, 3, 4, 7, 20 in part; the FY2023
  10-K (`0001326160-24-000037`, filed 2024-02-23) and FY2021 10-K (`0001326160-22-000072`, filed 2022-02-24) for the cash
  flow statements of 2019 to 2023; the FY2020 10-K (`0001326160-21-000063`) for the record of 2020; the 10-Q for Q2 2026
  (`0001326160-26-000040`, filed 2026-08-04); the 2026 proxy (DEF 14A, accession `0001104659-26-032443`, filed 2026-03-20);
  the 8-Ks of 2026-03-03 (Brookfield first closing, `0001104659-26-022610`), 2026-04-01 (Tennessee sale closed,
  `0001104659-26-038007`), 2026-07-06 and 2026-07-17 (North Carolina settlements, `0001104659-26-080476`,
  `0001104659-26-084653`), 2026-08-05 (Progress settlement, `0001104659-26-091159`), 2026-08-13 (equity units,
  `0001104659-26-095903`), 2026-09-25 (director, `0001104659-26-110588`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, FY2025, **$12,330M**
  on the filed Consolidated Statement of Cash Flows of the 10-K (`0001326160-26-000014`), equal to the XBRL figure
  `tools/run.py` printed. Also checked: long-term debt $80,108M and stockholders' equity $51,842M at 2025-12-31 on the filed
  balance sheet, equal to the run.py ten-year table.
- `tools/run.py DUK` arithmetic lines only (print in the research folder): OCF FY2023 to FY2025 $9,878M, $12,328M,
  $12,330M; capital expenditures $12,604M, $12,280M, $14,024M; D&A (cash-flow line, including nuclear fuel and accretion)
  $6,084M, $6,419M, $7,704M; stock pay (`AllocatedShareBasedCompensationExpense`) $97M, $96M, $102M; finance-lease principal
  $160M, $113M, $64M. Owner cash after all capital spending is negative in each of the three years (−$2,823M, −$48M,
  −$1,796M as run.py computes it, before any debt credit). The run.py "receivables" of $16M at 2025 is the VIE line only;
  the filed balance sheet shows trade receivables of $4,214M beside it after the receivables-financing VIEs were
  terminated (10-K balance sheet). Nothing run.py prints as a rule, an id or a verdict was used (Part VII, the tooling).

**The lines of evidence this name needs, chosen from Items 1, 1A and 7** (the brief's departure; my choice, stated):
1. *The regulatory compact and its terms* (Item 1: "Services are priced by state commission-approved rates designed to
   include the costs of providing these services and a reasonable return on invested capital"; the rate-case tables of
   allowed ROE and equity ratio; Item 1A's first regulatory risk). This is what earns the money, so it is Q1, Q2 and Q7.
2. *The capital programme and how it is funded* (Item 7: $17,750M, $19,500M and $21,200M projected for 2026 to 2028,
   "between approximately $200 billion and $220 billion" over the decade; $9 billion of debt in 2026; "$10 billion of common
   stock equity from 2027-2030"; the two minority sales). This is Q3, Q6 and Q9.
3. *The balance sheet and the holding-company debt* (Item 7, capitalization 63% debt in 2025; the covenant at 65%; the
   ratings; Item 1A "Duke Energy is a holding company and depends on the cash flows from its subsidiaries"). Q4 and Q9.
4. *The demand forecast* (Item 1 and Item 7: data centers, "load growth acceleration", weak industrial sales; Item 1A on
   "lack of growth or slower growth"). The growth that justifies the capital, so Q1, Q2 and Q7.
5. *The disallowance and impairment record* (Item 7's special items; the Commercial Renewables losses of 2022 and 2023;
   the pipeline cancellation of 2020; coal ash; the 2024 South Carolina impairments). Evidence on the castle (Q2), the
   accounts (Q4) and the people (Q5, Q6).
6. *Storms, nuclear and other single events* (Item 1A natural disasters and nuclear; the 2024 hurricanes). Q9.
7. *Pay and the adjusted figure* (Item 7: "Adjusted EPS is also used as a basis to determine employee incentive bonuses";
   the proxy). Q4 carried to Q5 and Q6.

## THE FOUNDATIONS (not a gate)
A share of Duke is a claim on the cash a regulated grid earns, and the test is whether I would hold it "if the market
closed for five years" **[M1997-109]**; for a utility the answer turns on the regulators, not the quotation, so the market
"just tells us prices" **[M2006-077]**. No macro view of interest rates or of the AI build-out enters as a forecast
**[M2000-094]**, though the company's own demand forecast is evidence to be read. *Who is paid to tell you* bears hard
here: the 10-K's language ("constructive regulatory outcomes", "unprecedented long-term growth") is the seller's, and
the barrier to a disinterested view is that every adviser to a $200 billion capital plan is paid by it **[M2020-037]**. The
margin of safety is the attitude for Q7: "if you have to actually do it on — with pencil and paper, it’s too close to think
about" **[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]**: (i) owner cash after all capital
spending was negative in every year read, so the dividend has been paid with borrowed and newly issued money; (ii) the
holding company's capitalization is 63% debt (2025, Item 7), against the 47% debt share the commissions allow the
operating utilities; (iii) the company asked the North Carolina commission for a 10.95% return and settled at 9.8% in
2026 (8-Ks of July and August 2026), so its own requests run about a point above what it gets; (iv) the bonus is paid on
adjusted EPS (Item 7).

## THE STANDING RULE
A part-interest bought for cash, unlevered and sized within the buyer's means, cannot put the buyer at risk of ruin
whatever the target's own debt; the target's leverage is weighed at Q9, and the rule asks only that the buyer not borrow
to own it: "We are never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**;
"Never risk permanent loss of capital." **[L2023-005]**. Nothing in this name requires the buyer to give anyone the switch.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from Item 1.** Two segments: Electric Utilities and Infrastructure (EU&I), regulated electric utilities
  in the Carolinas, Florida, Indiana, Ohio and Kentucky serving "approximately 8.7 million customers" and owning
  "approximately 55,713 MW of generation capacity"; Gas Utilities and Infrastructure (GU&I), about 1.8 million gas
  customers before the Tennessee sale. EU&I's segment income was $5,337M of a consolidated $4,912M available to common in
  2025 (Other carries the holding-company interest), so the electric part decides by any measure (Q2, a business of parts).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) the rate base, set by the capital the
  commissions approve, which the company itself plans ten years out ($200 to $220 billion, Item 7); (2) the allowed return
  on equity and equity share, which the Item 1 tables show in a narrow band over the three years of cases listed (ROE 9.5%
  to 10.3%, equity 50.5% to 53%; the 2026 North Carolina settlements at 9.8% on 53%, 8-Ks of 2026-07-17 and 2026-08-05);
  (3) regulatory lag and disallowances; (4) volume, which matters less where rates are decoupled (Item 1: "decoupled rates
  in North Carolina"). Fuel is passed through: "changes in fuel costs from year to year have no material impact on
  operating results of EU&I, unless a commission finds a portion of such costs to have been imprudent" (Item 1). The
  speakers' own reading of the category: "when you get an allowed return in the electric utility you’re almost certain of
  earning it, I mean, if you behave yourself." **[M2010-037]**; "in the end they give us a fair return on the assets
  employed, and we will get that return whatever the assets may be." **[M2008-024]**.
- **The tests.** Where will it be in ten years **[M2000-037]**: a larger regulated asset base earning about the allowed
  return, if the commissions keep the compact; the "reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]** is available because the earning power is a regulated
  return on a planned base. Would the insiders write it down **[M2000-105]**: they do, in the ten-year capital plan and the
  rate filings, which is the opposite of the tech case. Do the past statements tell me the future ones **[M2008-033]**:
  largely, through regulatory accounting; the exception is the regulatory asset and liability accounts, which are large
  ($16.3B of regulatory assets and $17.0B of regulatory liabilities at 2025-12-31, 10-K balance sheet) and read at Q4.
  How far off could I be **[M2011-084]**: on the return, a narrow range; on the size of the base, wider, because the demand
  that justifies $200 billion is a forecast (data centers, Item 7), and on the political climate, which the speakers name
  as the one way the category can fail: "the regulatory climate in a few states has raised the specter of zero
  profitability or even bankruptcy [...] it is difficult to project both earnings and asset values in what was once
  regarded as among the most stable industries in America." **[L2023-011]**. That row speaks of named western states; the
  Item 1 tables for Duke's six states show allowed returns that have not moved out of their band. It is carried to Q2 and
  Q9 as the threat, not here as a bar.
- **Routing.** No fast-changing technology decides the economics: the competitive threat Item 1 names is "on-site
  generation from commercial or industrial customers and distributed generation, such as private solar", which is read
  at Q2 as a possible erosion of the castle, not a reason the ten-year economics cannot be seen. Not a bank. Not a holding
  company of unlike parts in the Q1 sense: both segments are regulated utilities, and the deciding part is EU&I.
- **VERDICT: IN.** The economics are a regulated return on a planned and filed asset base, foreseeable within a stated
  band **[M2010-037]**, **[M2012-065]**, with the regulatory climate carried forward as the risk **[L2023-011]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
*(Written 2026-10-22, the resume session.)*

**The parts table** (Q2, a business of parts; segment income as the 10-Ks define it, "income from continuing operations net
of income attributable to NCI and preferred stock dividends", after the segment's own interest and tax; USD millions; FY2021
from the FY2021 10-K `0001326160-22-000072`, FY2022 and FY2023 from the FY2023 10-K `0001326160-24-000037`, FY2024 and FY2025
from the FY2025 10-K `0001326160-26-000014`):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share of the two segments | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Electric Utilities and Infrastructure | 3,850 | 3,929 | 4,223 | 4,770 | 5,337 | 22,109 | 90% | exclusive retail franchise in five of its six states; regulated return | **yes** (more than half) |
| Gas Utilities and Infrastructure | 396 | 468 | 519 | 454 | 559 | 2,396 | 10% | regulated local distribution, competing with electricity for heat (Item 1) | no |

Commercial Renewables (segment income $201M in 2021) was moved to discontinued operations in Q4 2022 and sold in October 2023
(FY2023 10-K, Item 1); "Other" is a loss each year (holding-company interest). The file is decided on EU&I.

**The castle tests, on EU&I.**
- *What keeps it standing, and how permanent* **[M1995-038]**: law, not a brand. "EU&I’s businesses operate as the sole
  supplier of electricity within their service territories, with the exception of Ohio, which has a competitive electricity
  supply market for generation service" and "Services are priced by state commission-approved rates designed to include the
  costs of providing these services and a reasonable return on invested capital" (10-K Item 1). In Ohio, Duke "earns retail
  margin [...] on the transmission and distribution of electricity, but not on the cost of the underlying energy" (Item 1).
  The speakers' description of the same arrangement: "Our regulated electric utilities, offering monopoly service in most
  cases, operate in a symbiotic manner with the customers in their service areas" and "We shouldn't expect our regulators to
  live up to their end of the bargain unless we live up to ours." **[L2009-011]**.
- *Would it stand without the lord* **[L2007-006]**: yes in the sense the test asks; the franchise does not depend on a
  person. The rows add that efficiency now matters where it once did not: "Historically, the survival of a local electric
  company did not depend on its efficiency. [...] That's all changing." **[L2015-007]**.
- *The money test* **[M2011-015]**: a rival with any sum cannot string a second distribution grid into a franchised
  territory. The attackers the filing itself names are of another kind: "on-site generation from commercial or industrial
  customers and distributed generation, such as private solar" (Item 1); "other utilities and energy suppliers that
  construct or install generation facilities directly for customers, as well as [...] customers who develop their own
  generation capabilities", and "the establishment of municipal utilities" (Item 1A); and deregulation with stranded costs
  (Item 1A). The rows' answer to distributed energy: "probably the best defense is to have very low-cost energy" **[M2015-025]**.
- *Pricing power and the agony before a rise* **[M2005-020]**: every price rise is a rate case, the prayer session made into
  a legal procedure, and the company does not get what it asks: it asked the North Carolina commission for 10.95% on 53%
  equity in both 2025 North Carolina cases (10-K Item 1 table, pending cases) and settled at 9.8% (8-Ks of 2026-07-17 and
  2026-08-05, cited in Q1); in South Carolina in 2024 the commission disallowed part of the settled environmental costs and
  Duke recorded a $33M impairment (10-K Note 4). The rows expect exactly this of the category and do not count it a defect
  of the castle: "The whole idea behind the utility industry is not to allow extraordinary profits. But we think it’s a very
  good business." **[M2000-131]**; "in utilities the trade has been the compact has been that you get a modest return."
  **[M2024-011]**.
- *Unit volume* **[M1999-054]**: retail GWh sales rose in 2025 (Duke Energy Carolinas 92,889 against 91,096; Duke Energy
  Progress 71,376 against 69,059; 10-K Item 7 segment table); "Weather-normal sales volumes have shown growth in 2025 [...]
  due primarily to continued residential customer growth and strength in the commercial sector including data center usage.
  Industrial sales remained soft" (Item 1).
- *The low-cost position* **[M2015-025]**: Duke's rates against its neighbours' are not stated in the filings read; no
  instance found by a search of the 10-K for rate comparisons. The castle is not decided on it; the gap is carried to Q9 as a
  bearing on the political climate (high bills invite the political response, below).
- *Brand, and the low bid* **[M2017-009]**: not the test here; the retail customer has no low bid to take outside Ohio's
  generation supply and the wholesale market. The filing records the customer's mood instead: "customer satisfaction across
  our industry continues to be impacted by inflationary pressures and the impact of ongoing rate case activity on customer
  bills" (Item 7).
- *Ask the competitors* **[M1999-130]**: the comparator row below, from their own filings.
- *Widening or narrowing* **[M1999-108]**: the territory is widening (87 economic development projects won in 2025,
  "representing over $30 billion in new capital investment", Item 7); the terms are not: the allowed returns in the Item 1
  table sit between 9.5% and 10.3% across the cases listed, and the 2026 North Carolina settlements at 9.8% are inside that band.
  Neither direction is shown on the return; the size of the base grows.
- *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**: (i) the regulatory climate, the one
  way the speakers record a regulated moat breaking: "the regulatory climate in a few states has raised the specter of zero
  profitability or even bankruptcy" **[L2023-011]**, and of that case, "certain of the attitudes demonstrated by that
  particular example have analogues throughout the utility system" **[M2025-045]**; (ii) the bill itself, which a capital
  programme of $200 to $220 billion over ten years (Item 7) raises, and the rows name the visible bill as the trigger: "if
  they see that bill going up [...] they’re going to get mad. [...] It’s the — it’s something they can’t give up. And it’s
  very visible." **[M2009-088]**; (iii) generation built for a forecast load that does not arrive, "particularly if usage of
  electricity by data centers is less than currently projected" (10-K forward-looking statements), which the rows say a
  commission may not let into the rate base if the stranding was foolish **[M2017-094]**; (iv) deregulation and stranded
  costs (Item 1A). Each is a threat to the return's level, not to the franchise's existence, and each is read again at Q9.

**The comparator row** (the field's returns over the window). The 10-K names no rival company (a search of the FY2025 10-K for
"competit" finds only the categories quoted above). **CONVENTION (of this run):** the comparators are The Southern Company
(CIK 92122), Dominion Energy (CIK 715957) and American Electric Power (CIK 4904), three large regulated electric utilities of
the Southeast and Midwest that are in Duke's own compensation peer group in its 2026 proxy (`0001104659-26-032443`; the group
also names NextEra, Exelon, Edison International and PG&E, and eleven non-utilities). Rationale: the filer names no rival,
and its own peer list is the nearest thing to the company's choice. Same metrics, from each company's 10-K XBRL facts
(first-filed value for each year; `peers2.py`, print in `peers_output.txt`; transcription from the filed tags, not
re-read against each filed statement):

| FY2016 to FY2025 means | Operating income ÷ average tangible assets (assets less goodwill) | Net income to common ÷ average equity |
|---|---|---|
| Duke Energy | 4.32% | 6.7% |
| Southern | 4.45% | 11.2% |
| Dominion | 3.83% | 9.7% |
| AEP | 3.98% | 10.0% |

Latest 10-K accessions: DUK `0001326160-26-000014`, SO `0000092122-26-000006`, D `0001193125-26-063120`, AEP
`0000004904-26-000013`. The field earns about four percent before interest and tax on its tangible assets in every year
and for every name; no name and no year breaks out of a band of roughly two to seven percent. Duke's return on its own book
equity is the lowest of the four over the decade, for two visible reasons: its equity carries $19,010M of goodwill (37% of
$51,842M equity at 2025-12-31, 10-K balance sheet), and its GAAP earnings carried large special charges (Q4).

**The field's returns, judged in words.** Ordinary. A durable castle that protects only ordinary returns closes OUT under
Q2's list, but that list names the exception in the framework's own words, "A return set by a regulator is the exception,
carried to Q3 as a second best" (Q2, What it rules OUT), on these rows: "there’s no way we get rich on our utility
investments. But there’s no way we get poor, either." **[M2009-104]**; "we are today quite willing to enter businesses that
regularly require large capital expenditures" **[L2009-012]**. EU&I's return is set by commissions in five states and FERC (Item 1), so the ordinary return is not
an OUT here; it is carried to Q3 and priced at Q7.

**Contrary evidence, written down as found** **[M1997-127]**: the lowest return on equity of the four comparators over ten
years; the request-against-grant gap of about a point; the regulated-moat failure the speakers narrate in their own utility
**[L2023-011]**; and a castle whose terms depend on the bill staying tolerable while the company plans to roughly double its
capital spending rate (Item 7, $17,750M in 2026 rising to $21,200M in 2028 against $14,024M in 2025).

- **VERDICT: IN.** The castle stands by law and by a compact whose terms in Duke's states have held within a stated band
  **[L2009-011]**, **[M2024-011]**; the moat is not tenuous in the sense that sends a castle to TOO HARD **[M2000-019]**, because
  the threats are to the level of a return that the filings let me read, not to the franchise. The returns it protects are
  ordinary, set by a regulator, and carried to Q3 as a second best **[M2009-104]**; the regulatory climate is carried to Q9
  **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What it earns on the capital it needs** **[M2010-090]**, read on tangible capital, goodwill left out for the business
  and counted for the allocation **[M2011-060]**. Income from continuing operations (including the minority share) plus
  interest expense less a 21% shield (CONVENTION, of this run: the federal statutory rate, the 10-K's own reconciliation
  line; rationale: a common shield across years, since the company's cash tax is near nil), over average debt on the face
  of the balance sheet plus Duke's stockholders' equity less goodwill (10-K statements, accessions in Step 0):

  | | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|
  | after-tax return before interest on tangible capital | 5.7% | 5.6% | 6.3% | 6.5% | 6.7% |

  Tangible capital rose from $91,397M at 2020 to $122,668M at 2025; the return before interest on the capital added
  between the 2021 and 2025 averages was about 10.4% after the shield. That incremental figure includes the rate increases
  granted on the old base and the equity component of AFUDC ($328M of non-cash income in 2025, cash-flow statement), so it
  overstates what the new dollars alone earn. Pre-tax operating income over tangible assets averaged 4.32% over ten years
  against a field of 3.83% to 4.45% (Q2 comparator row). On the owners' own book equity, net income to common averaged 6.7%
  over 2016 to 2025, the lowest of the four, and the speakers' judgment of that level held long is plain: "if you have a
  business that’s earning 5 or 6 percent on equity and you hold it for a long time, you are not going to do well in
  investing." **[M1998-006]**.
- **How much must go back to stand still, and how much to grow** **[L2000-035]**. Capital expenditures ran $9,715M,
  $11,367M, $12,604M, $12,280M and $14,024M in 2021 to 2025, against a cash-flow depreciation line (including nuclear fuel
  and accretion) of $5,663M to $7,704M: about 1.8 to 1.9 times depreciation. Item 7 plans $17,750M, $19,500M and $21,200M for
  2026 to 2028. The filing gives no split between maintenance and growth (searched: Item 7's capital table is by function,
  generation, transmission, distribution, environmental). The rows' own description of the category: "To earn more,
  their owners must invest more." **[L2011-019]**; "it costs a lot more money to maintain capital expenditures now in dollar
  terms than it would’ve 30 years ago" **[M2005-052]**; "it just keeps eating up more and more money, and your depreciation
  charges are inadequate" **[M2015-049]**. Operating cash flow has not covered capital spending in any year of the decade read
  (Step 0; `run_py_output.txt`), let alone the dividend.
- **The growth arithmetic.** Earnings rose (GAAP net income to common $3,802M in 2021 to $4,912M in 2025) because capital
  rose (debt on the face of the balance sheet $67,139M to $89,836M, tangible capital up by $31,271M from 2020): "we’re not
  earning a higher rate of return on capital than we were when we started. We just put way more capital into the business"
  **[M2023-081]**. Per share, GAAP EPS went from $4.94 to $6.31 while weighted shares rose from 769M to 777M (XBRL, FY2021
  and FY2025 10-Ks).
- **The second-best test.** The rows admit the capital-heavy regulated business as a second best on one condition: "We
  expect only that these businesses have reasonable expectations of earning decent returns on the incremental sums they
  invest." **[L2009-012]**; "they’re good enough" **[M2018-056]**; and the measure of that return "is not measured by the
  cash minus the increased capital investment we’re making. It’s measured by the operating earnings after depreciation."
  **[M2014-086]**. On that measure Duke's added capital earns about the allowed return, a fair one, not a rich one
  **[M2009-104]**.
- **WEIGHS AGAINST, narrowly.** The added capital earns roughly what the commissions allow **[L2009-012]**, **[M2014-086]**,
  which is the second-best grade **[M1998-081]**, **[M2018-055]**; against it, the reinvestment is compulsory and growing
  faster than the cash **[L2011-019]**, **[M2015-049]**, and the owners' return on their own book over ten years has been in the
  band the speakers say does not reward holding **[M1998-006]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (the `tools/run.py` table, first-filed
  XBRL of each 10-K, accessions listed in `run_py_output.txt`; 2025 and 2024 checked against the filed balance sheet of
  `0001326160-26-000014`; USD millions):

  | year-end | assets | equity | goodwill | debt on the face (current LTD + short-term + LTD) | debt ÷ (debt + equity) | retained earnings | cash |
  |---|---|---|---|---|---|---|---|
  | 2016 | 132,761 | 41,033 | 19,425 | 50,382 | 55% | 2,384 | 392 |
  | 2018 | 145,392 | 43,817 | 19,303 | 57,939 | 57% | 3,113 | 442 |
  | 2020 | 162,388 | 47,964 | 19,303 | 62,736 | 57% | 2,471 | 259 |
  | 2022 | 178,086 | 49,322 | 19,303 | 75,167 | 60% | 2,637 | 409 |
  | 2024 | 186,343 | 50,127 | 19,303 | 84,273 | 63% | 3,431 | 314 |
  | 2025 | 195,736 | 51,842 | 19,010 | 89,836 | 63% | 5,056 | 245 |

  *What moved and why.* Assets grew 47% and debt 78% while equity grew 26%: the growth was financed more by borrowing than
  by owners, and the debt share of capital rose eight points in nine years. Goodwill is flat at about $19.3B (the 2012
  Progress merger and the 2016 Piedmont purchase) and is 37% of equity, so a third of the owners' book earns nothing a
  commission allows (inference from the allowed-return tables, which set returns on rate base; no filing sentence read
  states it either way). Retained earnings never exceeded $5.1B on equity of $41B to $52B: almost all of each year's earnings
  went out as dividends, and the equity's growth came from new shares (issuance in 2016, 2018, 2019, 2020 and 2024 of $731M,
  $1,838M, $384M, $2,745M and $405M, XBRL cash-flow facts) and from preferred stock. Cash is a few hundred million against
  $90B of debt every year: the subsidiaries run on commercial paper and the money pool (Item 7). Receivables fell to $16M in
  2025 on the VIE line only; trade receivables of $4,214M sit beside it after the receivables-financing VIEs were ended
  (Step 0). Regulatory assets $16.3B and regulatory liabilities $17.0B at 2025 (balance sheet) are the accounts that only a
  commission's order turns into cash or refunds. "Neither one gives you the total answer on anything" **[M2025-032]**: what the
  balance sheets say is a business borrowing faster than it earns and paying out what it earns.
- **The real costs.** Depreciation is a real cost here and probably understated against replacement: "Depreciation charges
  [...] are almost always true costs" **[L2015-004]**, and capex has run near twice it (Q3). The non-cash equity component
  of AFUDC ($198M, $233M, $328M in 2023 to 2025) is booked as income before any customer pays it. Stock pay is small
  ($88M to $102M a year) and is in the owner-cash figures. The "one-time" items recur: GAAP EPS against the company's
  adjusted EPS, 2019 to 2025 (10-K MD&A, each year's accession in Step 0 or above): $5.06 against $5.06; $1.72 against $5.12
  (pipeline cancellation, coal ash settlement); $4.94 against $5.24; $3.17 against $5.27; $3.54 against $5.56 (Commercial
  Renewables sale, loss of $1,725M pre-tax in 2023 per the cash-flow statement); $5.71 against $5.90; $6.31 against $6.31.
  The sum over seven years is $30.45 GAAP against $38.46 adjusted: the excluded items were about a fifth of the featured
  figure, real write-offs of real capital. Cash taxes are near nil: "Duke Energy does not expect to be a significant federal
  cash taxpayer until around 2030" (Item 7), and transferable credits sold for $723M, $558M and $28M in 2025, 2024 and 2023 are
  in operating cash flow while their value is owed back to customers as a regulatory liability ("Deferred nuclear PTC.
  Represents the net realizable value of nuclear PTCs that will be passed back to customers over time", Note 4). Deferred
  taxes are not equity to the owner of a utility: "I don’t think I would look at that as a hidden form of equity" **[M2015-030]**.
- **The tells.** No prepaid or deferred account building out of line with the business that the filing does not explain;
  the regulatory assets are itemised by order and recovery period (Note 4). The adjusted figure is featured: "management
  also evaluates financial performance based on adjusted EPS" and "Adjusted EPS is also used as a basis to determine
  employee incentive bonuses" (Item 7); the company gives earnings guidance and reports against it ("We achieved our 2025
  financial commitments by delivering earnings growth above the midpoint of our adjusted earnings guidance range", Item 7).
  These are the habits the framework records here and carries to Q5: "a management that regularly attempts to wave away
  very real costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; "the scourge of earnings
  "guidance" and the desire of CEOs to "hit the number."" **[L2019-006]**. In Duke's favour, each special item is named,
  footnoted and reconciled in the MD&A, which is what the rows ask: "Charlie and I want managements, in their commentary, to
  describe unusual items � good or bad � that affect the GAAP numbers." **[L2016-006]**.
- **VERDICT on the accounts: IN** (no confusion: the statements, the special items and the regulatory accounts reconcile and
  are explained; no suspicion raised by the statements themselves **[M1994-018]**). **WEIGHS AGAINST** as a weighing: an
  adjusted figure featured and paid on, guidance given and reported against, and "one-time" charges that have recurred to a
  fifth of the featured figure **[L2016-006]**, **[L2019-006]**; carried to Q5. The recast earnings feed Q7 as owner cash
  after every capital outlay, with the transferable-credit receipts named as a liability to customers.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
*Who.* Harry K. Sideris, President and CEO and a director from April 1, 2025, a company executive before that; Lynn J. Good,
CEO from 2013, retired April 1, 2025; Theodore F. Craver, Jr., Independent Chair from the same date (2026 proxy,
`0001104659-26-032443`). This is a part-interest bought in the market, so the reading tests carry the weight, not the
after-the-sale test.

**Integrity, the record read** (the first and only STOP here; "If you’ve got doubts, forget it." **[M2013-088]**):
- *The habits carried from Q4.* Adjusted EPS featured and reconciled; public guidance each year; the STI's EPS target is
  "set in the middle of this guidance range at $6.30" for 2025, and the 2025 result was $6.31 adjusted and GAAP alike, which
  the proxy calls "above our earnings guidance midpoint". The rows read these as "things that they do in public in relation
  to their investors and the promises they make" **[M2004-067]**, and the danger they name is a habit: "we become downright
  incredulous if they consistently reach their declared targets" **[L2002-041]**. The record read does not show a habit of
  beating: adjusted EPS fell short of the prior year's level in no year but grew by as little as $0.03 (2022) and the
  company's own words for 2020 were "within its adjusted EPS guidance range" (FY2020 10-K); I did not read each year's
  guidance, so whether targets were "consistently" reached is not established either way.
- *The reports.* The special items are named, sized and footnoted every year (Q4), and GAAP equalled adjusted in 2019 and
  2025, the end years of the series; the write-offs (the pipeline, the coal ash settlement, the renewables sale) were put
  through GAAP, not hidden. "If you find a management that doesn’t care about the accounting but does explain to you in clear
  terms what’s going on, I think you should regard that as a plus" **[M1994-018]**: the explanation is clear, the caring about
  the adjusted figure is not absent.
- *The legal record in the filings read.* The FY2025 10-K's exhibit index still lists the "Plea Agreement between Duke Energy
  Corporation and the Court of the Eastern District of North Carolina in connection with the May 14, 2015, Dan River Grand
  Jury Settlement"; that was corporate environmental misconduct under the prior chief executive, eleven years before this
  run, with coal ash basin closure still costing "approximately $8 billion to $9 billion of which approximately $4.8 billion
  has been spent through 2025" (Item 7). The NTE antitrust counterclaims, revived on appeal in 2024, were settled in March
  2026 for an amount "not material" (10-Q, `0001326160-26-000040`). No restatement, no SEC enforcement and no accounting
  investigation found in the 10-K, 10-Q, proxy or 8-Ks read (searched for "restat", "investigation", "plea").
- *How they talk about mistakes* **[L2024-003]**: the word "mistake" does not appear in the 10-K or the proxy (search count
  zero); the pipeline and the renewables exit are described by their charges and their reasons, not as errors. The
  taboo the 2024 row names "always made me nervous" **[L2024-003]**; it weighs, it does not prove dishonesty.
- *The proxy, self against owners* **[M1994-009]**: CEO pay $13,652,630 for 2025 against a median employee's $132,604; a
  change-in-control multiple of 2.99 for the CEO against two for the others; personal use of the corporate aircraft; hedging
  and pledging banned; a clawback; directors' holdings of a few thousand to a few tens of thousands of shares each against
  778,117,625 outstanding (proxy ownership table). Ordinary for the field; nothing in it reads as self-dealing.

**Integrity: IN, a judgment made with the record above in front of it.** The doubt the rows close on is doubt about whether
the people will deal honestly with the owners **[M2013-088]**, **[M2016-033]**; what the filings show is a management that
features a flattering figure but reconciles it in full **[M1994-018]**, pays itself on that figure (weighed at Q6), and carries
an eleven-year-old corporate plea from an earlier regime. I do not find in the record read a misleading report on the
figure that matters, a reserve that moves, or a promise broken to owners; the adjusted-EPS habit is recorded against them
and carried to Q6's pay test, not treated as proof. *(A stricter reader could close here on the habit plus the plea; I
record that I considered it and did not, because the rows' tells of dishonesty, reports that dance and figures obscured
**[M2004-067]**, are not what the reconciled statements show.)*

**Ability, the WEIGHING** **[M1994-008]**. The hand dealt is a regulated franchise in growing Southeastern states. Inside the
franchise the record is competent: rate cases settled across six states at returns inside the band, customer and load
growth won ("87 economic development projects in 2025", Item 7), and the 2024 hurricanes recovered through a Florida
surcharge (Item 7). Outside it, the capital record is poor: the Atlantic Coast Pipeline investment written off in 2020
(GAAP EPS $1.72 against $5.12 adjusted), and Commercial Renewables built up and then sold in 2023 at a pre-tax loss of
$1,725M (cash-flow statement). The rows weight ability lightly where the business carries the manager **[M1995-110]**, and the
regulated core does. **Ability WEIGHS AGAINST, narrowly**, on the two non-regulated losses, which are the
capital-allocation half of the first yardstick **[M1994-008]**.

- **VERDICT on integrity: IN; ability WEIGHS AGAINST**, with the Q4 habits carried to Q6 Part B.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
"What do we do with the money, as it comes in?" **[M2001-111]**. Here the question is reversed: the money does not come in;
it is raised.

**Part A: the money.**
- *The retention test* **[R1995-009]**. Little is retained to test. Over 2016 to 2025, GAAP EPS summed to $41.68 and
  dividends declared to $38.355 a share (XBRL, the ten 10-Ks): 92% paid out, about $3.33 a share kept in ten years, while the
  weighted share count rose from 691M to 777M. The test that matters is the one on new capital: owner cash after all
  capital spending was negative in every year of the window (Q7), so each year's dividend of $3.1B to $3.3B was paid from
  borrowing, new shares and the sale of pieces of the business. The rows' rule for paying out is for "a company that expects
  to regularly earn more than it can profitably employ in its business" **[M2004-089]**; Duke is the opposite case, and pays
  anyway. The policy is "clear, consistent" **[L2012-015]** ("a cash dividend on its common stock for the 99th consecutive
  year", Item 7), and the rows say a capital-hungry utility must court its suppliers of money: "if you’re going to need lots
  of money, you probably ought to behave in a way that encourages people to give you lots of money." **[M2025-046]**. That
  is the best reading of the dividend: a cost of raising equity, not a distribution of surplus.
- *Issuance and deals: value given against value got* **[M1995-001]**. (i) Common stock: ATM and forward sales in 2024 and
  2025 (forwards on 4,238,007 shares at $116.02 to $117.94, Note 20); equity units of $2,000M in August 2026 whose purchase
  contracts settle into common by 2029 (8-K `0001104659-26-095903`); and the stated plan: "Duke Energy plans to issue $10
  billion of common stock equity from 2027-2030 through the dividend reinvestment and ATM programs" (10-K, Item 7). (ii)
  Minority stakes in the best parts: 19.9% of Duke Energy Indiana to GIC (2021 to 2022, $1,575M and $1,377M received in those
  years, XBRL) and up to 19.7% of Florida Progress to Brookfield for $6B; the first closing sold 9.19% for about $2.8B, and
  "The difference between the cash consideration received [...] and the carrying value of the noncontrolling interest was
  $1,941 million and was recorded as an increase to equity" (10-Q). The Florida price, about 3.3 times the carrying value of
  the interest sold ($2,770M net of costs against $829M, arithmetic of this run), is value got well above book; whether it is above intrinsic value is Q7's question, and against Q7's range
  (below) it looks like a sale at a good price. The investor also holds "the rights to require Progress Energy to acquire
  Investor's membership interest" in specified circumstances (10-Q): a contingent call on Duke's cash, carried to Q9. (iii)
  The Tennessee gas business sold to Spire for $2,501M received, a pre-tax gain of $368M (10-Q). No all-stock acquisition in
  the window: the narrower STOP **[L2009-019]** does not arise.
- *Serial issuance* **[L2014-015]**: shares outstanding up about 12% in ten years and a further $10B of common planned for
  2027 to 2030 (at the Step 0 price, about 82M shares, a tenth of today's count, arithmetic of this run). The rows' warning is
  of companies "hell-bent on issuing shares"; Duke issues because the commissions require about half of each new dollar of
  rate base to be equity (the 53% equity ratios of Item 1), not to promote the stock. The framework carries serial issuance as
  a candidate second STOP left unresolved in section VI; I weigh it, heavily, and do not close on it.
- *Buybacks.* None in the window (no repurchase line in any cash-flow statement read). The buyback test against the bottom of
  the Q7 range *(written back with Q7)*: there are no repurchase prices to set against the bottom of the central range,
  $71.06 a share, so the test does not engage; and the company has no "available funds [...] beyond the near-term needs of
  the business" **[L1999-023]** to buy with. The reverse test applies to its issuance: the 2025 forward sales at $116.02 to
  $117.94 were priced above the top of Q7's central range ($109.64), which by **[M1996-013]** read the other way does not harm
  continuing holders; the planned $10B of 2027 to 2030 will be sold at whatever price obtains then.
- **Part A WEIGHS AGAINST**: a dividend paid with raised money **[M2004-089]**, a standing plan of share issuance
  **[L2014-015]**, and the business's best parts sold in slices to fund the plan; in its favour, the slices fetched prices well
  above book **[M1995-001]**.

**Part B: the pay, the board and the owners.**
- *Pay tied to what the person controls, and a capital charge* **[M2003-019]**, **[M2009-081]**. STI 2025: 85% corporate
  objectives with an adjusted-EPS "circuit breaker" at $6.22, the EPS target set at the midpoint of public guidance, maximum
  200% on EPS and 175% on the others (O&M expense, operational excellence, customer satisfaction, energy modernization).
  LTI: 70% performance shares on three-year cumulative adjusted EPS (40%), total shareholder return relative to the utility
  index (40%) and safety (20%); 30% restricted stock units that vest on time alone. The 2023 to 2025 performance shares paid
  136.72% of target (proxy). No measure charges for the capital employed, in a business that adds $12B to $14B of it a year:
  "In a capital-intensive business, you have to have something that [...] includes a capital cost element." **[M2009-081]**.
  An EPS target can be met by adding rate base at any return above the cost of the debt that funds it; "you get what you
  reward for" **[M2016-083]**. Time-vested units pay "no matter what happens" **[M1999-018]**; relative TSR rides the
  sector's market.
- *Guidance* **[L2019-006]**: given every year and tied into the bonus; the rows call it "a totally destructive policy"
  **[M2022-054]**.
- *The board.* An Independent Chair separate from the CEO since April 2025 (proxy) answers the row on a chief executive who
  also chairs; directors hold shares, but in amounts of thousands against grants (ownership table), and the rows prefer
  shares bought "with their savings" **[L2019-008]**; the filings read do not say which were bought.
- *The owners' money on other causes.* A Political Expenditures Policy and a "Biannual Corporate Political Expenditures
  Report" (proxy): the company spends corporate funds on political activity, which Buffett called, of his own managers, "a
  breach of trust with Berkshire" **[M2017-103]** (a row about Berkshire's own conduct, applied here by inversion as Q6 directs).
- **Part B WEIGHS AGAINST**: pay on adjusted EPS without a capital charge in the most capital-hungry business there is
  **[M2009-081]**, guidance tied to the bonus **[M2022-054]**, and political spending **[M2017-103]**; in its favour, an
  independent chair, a hedging ban and a clawback.

- **WEIGHS AGAINST** on both parts.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, at
the long government rate, 5.43% (Step 0) **[M1996-025]**, held as a range. Arithmetic in `q7.py`, print in `q7_output.txt`.

**The basis: the regulated utility (Q7, The regulated utility, 2026-10-18).** EU&I decides (Q2, 90% of five-year segment
income) and earns a return a regulator allows: "when you get an allowed return in the electric utility you’re almost certain
of earning it" **[M2010-037]**; the debt exception is the row's own, "the fixed-asset commitments at our regulated utilities"
**[L2017-012]**. So the central figure is **equity-only**: owner cash after interest and after the company's own tax, against
the market value of the shares, $94,710M; the all-equity figure is shown beside and does not decide.

**The owner-cash series** (USD millions; FY2021 to FY2025, the five-year window; filed cash-flow statements, accessions in Step
0, 2023 to 2025 checked line by line against the FY2025 filed statement; 2021 and 2022 from first-filed XBRL):

| | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| Operating cash flow (after interest and the company's cash tax; working capital counted, (d)) | 8,290 | 5,927 | 9,878 | 12,328 | 12,330 | |
| less stock pay | 88 | 100 | 97 | 96 | 102 | |
| less finance-lease principal | 219 | 151 | 160 | 113 | 64 | |
| less preferred dividends; less distributions to minority holders | 172 | 246 | 165 | 138 | 87 | |
| less the maintenance guess: the depreciation, amortization and accretion line including nuclear fuel | 5,663 | 5,843 | 6,084 | 6,419 | 7,704 | |
| **M, maintenance-only (central, (e))** | 2,148 | −413 | 3,372 | 5,562 | 4,373 | **3,008** |
| capital expenditures (all) | 9,715 | 11,367 | 12,604 | 12,280 | 14,024 | |
| net long-term debt raised (issued less redeemed) | 3,758 | 7,478 | 5,291 | 5,599 | 6,239 | |
| debt credit: net LTD raised, capped at 47% of capex | 3,758 | 5,342 | 5,291 | 5,599 | 6,239 | |
| **A, all spending, debt credited (beside)** | 1,854 | −595 | 2,143 | 5,300 | 4,292 | **2,599** |
| A0, all spending, no credit (literal) | −1,904 | −5,937 | −3,148 | −299 | −1,947 | −2,647 |

*Choices, each stated.* (1) **The maintenance guess** **[M2000-144]**: the filing gives no split of maintenance and growth
spending (Q3); I take the depreciation line as the guess, "the depreciation charge is not inappropriate in most companies to
use as a proxy for required capital expenditures" **[M1998-127]**, using the larger cash-flow line (it includes nuclear fuel,
which is bought inside capex) so as not to flatter; inflation makes the true figure higher **[M2005-052]**. (2) **The debt
credit.** Credited in the all-spending case only, as net long-term debt raised (issuance less redemption), capped at the
allowed debt share of 47% (the 53% equity of the North Carolina orders in the Item 1 table; the table's range is 47% to 49.5%
debt). **CONVENTION (of this run):** *net, not gross*: rationale, debt issued to repay maturing debt funds no new fixed asset,
and the paragraph credits the debt "to fund the fixed assets [...] against the capital spending it funded". **CONVENTION (of
this run):** *no debt credit inside the maintenance case*: rationale, a base that is only maintained needs no net new
borrowing, and the debt actually raised in the window bought the growth of the base, which the maintenance case does not
charge and does credit through the growth rate; crediting it there would count the same borrowing twice. The case with that
credit (47% of the maintenance line) is shown beside as M+credit so that the choice is visible. (3) **No cycle base (a):** the
end years are not aberrational on the filer's own description (2021: "positive rate case contributions and higher volumes";
2025: "recovery of growing infrastructure investments", FY2021 and FY2025 MD&A); the weak middle year, 2022, is the fuel
under-recovery year inside the window. The literal window is the base. (4) **Acquisitions (c):** none in the window; the
Commercial Renewables cash flows sit in 2021 to 2023 and are small (segment income $201M in 2021); not adjusted. (5) **Deals
closed after the window and before the price date:** the Tennessee sale ($2,501M received, 2026-03-31) and the first Florida
minority closing (9.19% for about $2.8B, 2026-03-03) are in the 2026-06-30 balance sheet. Their effect on equity-only owner
cash, lower minority-free earnings (9.19% of Duke Energy Florida's 2025 net income of $1,193M is about $110M; Tennessee's
earnings are not separately filed) against interest saved on about $5.3B of proceeds (about $170M a year at the window's
interest cost after a 21% shield), nets to roughly nothing on a base of $3.0B; it is not put into the range, and it could not
move any case to the floor. (6) **Whose tax:** the company's own cash tax, no conversion, in the central figure (Q7, Whose
tax). The carryforward clause applies, because "Duke Energy does not expect to be a significant federal cash taxpayer until
around 2030" (Item 7); it is computed beside, as far as the filing allows (below). (7) **The cap (f):** the shown growth of
owner cash, end year to end year, is 19.45% a year (M) and 23.35% (A); carried ten years it would need owner cash of about a
third of sales against a highest share in the window of 18.5% (M) and 17.6% (A), so the growth carried is the business's own
sales growth over the window, 6.47%, held at the discount rate, **5.43%**, since (f) says the cut is "never above the discount rate"
(the framework's words); the rows behind the cap: "when the compound rate becomes higher than the discount rate"
**[M1997-095]**, and "if you trace out the mathematics of it, you bump into absurdities, then you better change expectations
somewhat" **[M1999-067]**. After year ten, zero nominal growth.

**The range** (each case: ten years at the carried growth, then none, at 5.43%; per share on 779.702M):

| Case (equity-only) | no-growth end | growth end | width | return at $121.47, no-growth / growth |
|---|---|---|---|---|
| **M, maintenance-only (central)** | **$71.06** | **$109.64** | 1.54× | **3.18% / 4.94%** |
| A, all spending, debt credited | $61.38 | $94.72 | 1.54× | 2.74% / 4.31% |
| A less "Other" investing outflows ($333M to $1,079M a year, not explained in the MD&A) | $43.13 | $66.55 | 1.54× | 1.93% / 3.09% |
| M+credit (the double count, shown so the choice is visible) | $141.47 | $218.28 | 1.54× | 6.32% / 9.26% |
| M, tax-adjusted (credit receipts owed to customers removed; the $523M carryforward utilization of FY2024 taken off every year and its value to 2029 added back) | $54.88 | $83.39 | 1.52× | 2.39% / 3.79% |
| A0, all spending, no credit | mean not positive: no value | | | |

All-equity beside: owner cash before interest (cash interest paid less a 21% shield added back), no debt credit, less net
debt of $92,565M (the 10-Q's notes payable $2,330M, current long-term debt $6,666M and long-term debt $82,242M, less cash
$673M, at 2026-06-30, `0001326160-26-000040`; plus the $2,000M of equity-unit notes of the 8-K of 2026-08-13): the
maintenance case gives $5.95 to $73.65 a share; the all-spending case has a mean that is not positive.

**The floor, tested first** (2026-10-10). At $121.47 no case earns the floor of about ten percent **[M2003-149]**: the central
case returns 3.18% to 4.94%, below the 5.43% bond itself; the most generous case on the page, the one I judge a double count,
returns 9.26% at its top. "So, there’s just a point at which we drop out of the game." **[M2003-149]**. The price also sits above
the top of the central range ($109.64), which closes OUT by the same convention. The width (1.54 to one) is not reached as a
question. The rows anticipated this exact case: "there’s no way we get rich on our utility investments" **[M2009-104]**, and a
utility at a full price closes OUT as the regulated-utility paragraph says.

- **Value range (central, equity-only, maintenance case): $71.06 to $109.64 a share against $121.47.**
- **Fair price (reporting figure, Part VII; not a verdict, not entry language): $47.30 a share**, equity-only, central (each
  end of the maintenance case valued at ten percent, $38.58 and $56.02, averaged), after the company's own tax. Beside it:
  **all-equity −$35.73 (not positive)**; equity-only all-spending with debt credit $40.86; tax-adjusted central $37.09.
- **VERDICT: OUT.** No case the analyst can defend earns the floor at the price **[M2003-149]**, and the price is above the top
  of the range **[L2013-012]**; this is not a close call needing a pencil **[M2009-005]**, it is a price that asks for growth
  the capital already pays for.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7**: no case earns the floor at $121.47 (close 2026-10-16); the central equity-only range is **$71.06 to $109.64**
a share, the price above its top; fair price $47.30 equity-only (all-equity −$35.73, not positive). Q1 IN, Q2 IN, Q3 weighs
against, Q4 IN on the accounts and weighs against, Q5 integrity IN and ability weighs against, Q6 weighs against.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Bearing on Q8 (the bond).** The 30-year Treasury par yield was 5.43% on 2026-10-16 (Step 0); the central case's return at
  the price is 3.18% to 4.94% (Q7 table).
- **Bearing on Q9 (debt and exposures).** Debt on the face of the balance sheet $89,836M at 2025-12-31 and $91,238M at
  2026-06-30 (10-K; 10-Q), plus the $2,000M equity units of August 2026; debt 63% of debt plus equity at 2025 against a credit
  facility covenant that "requir[es] the debt-to-total capitalization ratio to not exceed 65% for each borrower, excluding
  Piedmont" (10-K Item 7). Ratings at February 2026: Duke Energy Corporation Baa2 (Moody's) and BBB+ (S&P) issuer, stable;
  Duke Energy Carolinas senior secured Aa3 and A (Item 7). Pre-tax earnings plus interest over interest (income before taxes
  from continuing operations plus interest expense, XBRL): 2.65 in 2021, 2.67 in 2022, 2.58 in 2023, 2.53 in 2024, 2.57 in
  2025, and 1.39 in 2020, the pipeline year. A $2B 364-day parent term loan drawn at 2025-12-31 (Note 7). Holding-company
  interest sits in "Other" (Item 1). Brookfield holds rights "to require Progress Energy to acquire Investor's membership
  interest in Florida Progress under certain specified circumstances" (10-Q). The 2024 hurricane season's restoration costs
  were paid in 2024 and 2025 and recovered through a Florida surcharge (Item 7); Item 1A names nuclear operation and natural
  disasters among the risks. Coal ash basin closure is estimated at $8B to $9B, $4.8B spent through 2025 (Item 7).
- **Bearing on Q9 and Q2 (the regulatory climate).** The 2026 North Carolina settlements at 9.8% on 53% equity against 10.95%
  requested (8-Ks of 2026-07-17 and 2026-08-05); the planned capital of $17,750M to $21,200M a year for 2026 to 2028 (Item 7).
- **Bearing on Q10.** Nothing found beyond the above.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (session of 2026-10-18); written question by question; committed after each
      question in both sessions (Step 0 to Q1 on 2026-10-18; Q2, Q3, Q4, Q5, Q6, Q7 and the close on 2026-10-22).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is held by the dispatching session; the fold
      into the register is the dispatcher's (operator rule ten). The POSITION NOTE is left for the dispatcher.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched in the resume session; what was seen
      by accident (commit subjects, a memory line) is declared under contamination, items (1) to (6), and not used.
- [x] Every v5 id resolves (checked by `check_run.py` in the research folder); every filing fact carries its accession or
      names the filing listed in Step 0 with its accession; comparators' accessions are in Q2.
- [x] The order was kept; Q7 was the first STOP to fail and closed the run; nothing after it is a clearance, and Q8 to Q12 are
      marked NOT REACHED.
- [x] Owner cash after every real cost, never a net-income proxy: operating cash flow less stock pay, lease principal,
      preferred and minority distributions, and capital spending (maintenance guess or all spending), with the debt credit
      stated (operator rule 5). Sovereign from the US Treasury, dated; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as found, in the foundations, Q2, Q3, Q4, Q5 and Q6.
- [x] Not a point-in-time run; no anchor bars rows.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 text, ids and floor were not.
- [x] `python tools/check_framework.py` PASS before each commit that touched the run file in the resume session.
- Honest limits: the maintenance figure is a guess (depreciation), stated; the comparators' figures are first-filed XBRL
  facts, not re-read against each filed statement; 2021 and 2022 cash-flow inputs are XBRL, not re-read against the filed
  FY2022 statement (the FY2022 10-K was not fetched); the "Other" investing outflow is not explained in the filings read; the
  carryforward shelter rests on one year's stated utilization; Tennessee's own earnings were not found.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The regulated-utility paragraph (Q7, 2026-10-18) does not say whether the debt credited is gross or net of debt
redeemed, nor whether it is credited inside the maintenance case.** Gross issuance ($8,956M to $11,891M a year) would credit
refinancing as if it funded new assets; and crediting debt in the maintenance case, which already credits the growth the
debt bought, counts the borrowing twice. I chose net, and no credit in the maintenance case, confessed as CONVENTIONS of this
run, and showed the double-count case beside: it returns 9.26% at its top, so the choice does not decide this box, but for a
cheaper utility it would (that case's growth end earns ten percent at about $111.53 a share, arithmetic of this run, so at
any price below that the choice alone would decide the floor test). (2) **"Whose tax" meets regulation
awkwardly.** The carryforward clause asks for owner cash at the statutory rate with the shelter's value added; at a utility,
rates are set on normalised tax, deferred taxes reduce the rate base **[M2015-030]**, and sold credits are owed back to
customers **[M2017-031]**, so the clause's recompute is not obviously the owner's economics. I kept the central figure on the
company's own tax and computed the clause beside, as far as one year's stated utilization allows. (3) **The cap (f)'s "never
above the discount rate" is ambiguous inside the ten years**, where the same specific says "the shown rate is the cap": I
held the sales-growth cut (6.47%) at the discount rate (5.43%); at 6.47% the central top is $119.13 and the double-count case
returns 9.89%, so the box is unchanged, but the reading should be fixed. (4) **Q2's comparator rule assumes the 10-K names
rivals.** A franchise monopoly's 10-K names categories of competition, not companies; I took three utilities from the proxy's
own pay peer group and confessed it. (5) **Q2's "ordinary returns" OUT and its regulator exception** leave unsaid what the
exception does at Q3 beyond "second best"; the run weighed the regulated return as Q3's second grade and let Q7 decide.
