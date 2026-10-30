# Company Run: Element Solutions Inc (NYSE: ESI), 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under the canonical brief `Screens/_daily/_dispatch_brief.md`; working folder `Test Runs/_research 2026-10-07 ESI/` (raw
filings under its `cache/` subfolder, ignored). Every judgment cites a v5 ledger id in bold; every filing fact carries its
accession. A STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.

**The business, as filed.** Formerly Platform Specialty Products Corporation (renamed Element Solutions on 2019-01-31, the
day the agricultural business, Arysta, was sold to UPL for net cash proceeds of $4.28 billion). Two segments: Electronics
(about 70% of 2025 sales: Assembly Solutions, solder pastes, fluxes and other assembly materials; Circuitry Solutions,
circuit-board metallization and finishes; Semiconductor Solutions, wafer-level plating and die-attach materials) and
Specialties (renamed from "Industrial & Specialty" in the fourth quarter of 2025: industrial surface finishing and
offshore hydraulic fluids; the flexographic plate business, MacDermid Graphics Solutions, sold 2025-02-28 for about $320
million). Two acquisitions closed after the last fiscal year: EFC Gases & Advanced Materials (2026-01-02, about $367
million) and Micromax (2026-02-02, about $494 million). **A merger agreement under which Solstice Advanced Materials was to
acquire ESI (0.500 Solstice shares plus $10.00 cash per share) was signed 2026-07-06 and mutually terminated 2026-08-27
with no fee paid** (8-K 0001104659-26-080825; 8-K 0001104659-26-102559). The brief's one-line description does not name it;
see the closing section.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared** (seen by accident, not used): the session context showed recent commit subjects naming other
companies' v5 re-runs and their Q7 closes, other companies' research-folder names in the git status, the dispatcher's lock
line ("interactive v5 re-runs batch 5"), and memory-index lines about the queue and the opportunity set. The brief itself
says earlier Element Solutions or Platform Specialty run files exist; none was opened, listed or searched. Nothing from any
of these entered a judgment below.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $36.62 a share, intraday 2026-10-07 about 12:23 New York time (Yahoo chart via `tools/sources.py`; **aggregator,
  live quote only, flagged** under operator rule 5). The prior close was $37.74 (2026-10-06). 52-week range $22.86 to $49.25
  (same aggregator). The stock was $25.94 on 2026-01-02 and $47.75 on 2026-06-30.
- **Shares by class** from the latest filing's cover: one class, common stock, **243,690,914** (10-Q for the quarter ended
  2026-06-30, filed 2026-07-28, accession `0001590714-26-000065`; `python Screens/cover_shares.py ESI`). Check: the 10-K
  cover gave 243.6 million as of 2026-04-22 on the tool's dei line, and issued shares were 270.5 million at 2026-03-31
  with treasury shares making up the difference. No 8-K or prospectus after the 10-Q issues shares (the Solstice merger
  would have, and was terminated). Outstanding awards (RSUs, PRSUs, the EFC executives' 1.45 million performance RSUs and
  an EFC earn-out of up to 1.16 million shares or $30 million) are not added to the count; they are stock pay, counted in
  owner cash.
- **Market cap:** $36.62 x 243.69M = **$8,924M**. Net debt at 2026-06-30: total debt $2,119.4M less cash $189.6M =
  **$1,929.8M** (10-Q `0001590714-26-000065`, Note 6 and the balance sheet; finance leases not separately stated in the
  debt note; operating leases left out). Enterprise value about $10,854M.
- **Sovereign for the earnings currency:** the reporting and XBRL currency is USD (79% of 2025 sales arose outside the U.S.,
  in many currencies, but the owner's cash is measured in dollars). **5.64%**, US Treasury daily par yield curve, 30-year,
  2026-10-06 (`python tools/run.py ESI`, which calls `tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-18, `0001590714-26-000018` (Items 1, 1A, 7, Notes 22 and
  23); 10-K FY2024 `0001590714-25-000022`; FY2023 `0001590714-24-000054`; FY2022 `0001590714-23-000027`; FY2021
  `0001590714-22-000029`; FY2020 `0001590714-21-000021`; FY2019 `0001590714-20-000023`; FY2018 `0001590714-19-000040`
  (segment tables, organic growth, cash-flow supplements); 10-Q 2026-06-30 `0001590714-26-000065`; proxy (DEF 14A) filed
  2026-03-23 `0001590714-26-000034`; 8-Ks of 2026-07-06 (`0001104659-26-080825`, merger agreement; `0001104659-26-080612`,
  joint press release), 2026-08-27 (`0001104659-26-102559`, termination and press release).
- **One figure cross-checked against the filed statement:** cash provided by operating activities 2025, $289.8M, in the
  FY2025 10-K's liquidity table (`0001590714-26-000018`), equals the XBRL value `tools/run.py` printed; cash and
  equivalents at 2025-12-31, $626.5M on the 10-Q's comparative balance sheet, equals the tool's $626M.
- `python tools/run.py ESI`, arithmetic lines only (Part VII; nothing it prints as a rule, id or verdict is used):

| FY | OCF | stock pay | capex | D&A | OCF - stock pay - capex |
|---|---|---|---|---|---|
| 2021 | 326.0 | 40.1 | 46.3 | 163.7 | 239.6 |
| 2022 | 295.9 | 17.7 | 47.8 | 161.6 | 230.4 |
| 2023 | 333.6 | 9.4 | 52.7 | 166.7 | 271.5 |
| 2024 | 362.0 | 14.8 | 68.4 | 158.0 | 278.8 |
| 2025 | 289.8 | 59.1 | 62.2 | 151.2 | 168.5 |

  USD millions, as filed (XBRL, checked against the 10-K tables for 2023 to 2025). Five-year mean **$237.8M**; the tool's
  "other window" line gives the same. Stock pay resolved: the 2025 figure includes the $37.1M "2025 executive share grants"
  (Note 22 reconciliation) and is counted as a cost. D&A is about 27% depreciation and 73% amortization of purchased
  intangibles (2025: depreciation $41.1M, amortization $110.1M). The tool found no securities, other stock-pay, software or
  mine lines in the window.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this if the market closed for five years
**[M1997-109]**, and the quotation tells me nothing except a price **[M2006-077]**. That foundation bears hard here: the
price nearly doubled between January and June 2026 and then fell a quarter on the merger news, while the business filed
the same two segments throughout; nothing in that movement is evidence about value. Margin of safety is an attitude here
and arithmetic at Q7: "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**. No macro view enters **[M2000-094]**: the AI-server demand the filings credit for 2025 and 2026 organic
growth is recorded as a fact about the business's recent sales, not as a forecast. Who is paid to tell me: the merger press
release of 2026-07-06 and the termination release of 2026-08-27 are sellers' documents ("you do not get impartial advice
from Wall Street — (laughs) — when there’s (an) enormous amount of fees possible from one action" **[M2020-037]**), and the
featured "Adjusted EBITDA" is management's own number; both are read against the GAAP statements. The analyst's habits: I
look for "what’s wrong in things" **[M2025-013]**, and I must state the management's case better than they can before
disagreeing with it **[M2016-055]**; I do so at Q5. **Contrary evidence, written down as found** **[M1997-127]**: (1) the
filer's own risk factor, "The specialty chemicals industry is subject to constant and rapid technological change, product
obsolescence, price erosion, evolving standards, finite product lifecycles" (10-K FY2025, Item 1A); (2) the 2022 "stretch"
awards, missed, cancelled and replaced by shares vesting the same day (proxy 2026, CD&A); (3) owner cash fell to $168.5M in
2025 while Adjusted EBITDA rose to $547.6M; (4) the competitor that bought the leading circuit-board chemistry franchise
(MKS, Atotech) wrote down $1.3 billion of it within a year. Each is carried to the question it bears on.

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money, unlevered, puts the buyer at no risk of ruin from this name:
"borrowed money has no place in the investor's tool kit" **[L2014-005]**; the rule is the buyer's conduct, and nothing in
this run proposes leverage, options or a size that could end the buyer's game **[M2012-081]**, **[M2004-065]**. The
target's own debt is weighed at Q9, not here.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" **[M2012-065]**, "a reasonable probability of being able to asses where the business will be in 10 years"
**[M2000-037]**; the product may stay opaque if "I understand the economic dynamics of the industry" **[M2011-014]** (said of
a petroleum-additives business, the nearest case in the rows to a formulator of process chemicals). Under the parts
reading (Q1, A holding company, extended to segments on 2026-10-06), the part that matters is the one that decides at Q2:
Electronics, 68.6% of five-year segment profit (table at Q2).

**The key variables and whether they are foreseeable** **[M1998-044]**:
1. *Volume of electronics manufactured* (circuit boards, assemblies, packaged chips): the products are "consumed by
   customers as part of their production process, providing us with reliable and recurring revenue as products are
   replenished" (10-K FY2025, Item 1). Volume follows world electronics output, with cycles (2019 -4%, 2020 -3%, 2023 -5%
   organic) and recoveries (2021 +13%, 2022 +5%, 2024 +4%, 2025 +6%; organic as filed, 10-Ks FY2019 to FY2025). Foreseeable
   in direction over ten years, not in timing.
2. *ESI's share of the specifications*: the filer says its products are "integral to customer product performance" while
   "typically represent[ing] only a small portion of our customers' costs", and that "operational risks and switching costs
   make it difficult for our customers to change suppliers" (Item 1). No customer is 10% of sales in 2023, 2024 or 2025.
3. *The margin on the chemistry*: Electronics Adjusted EBITDA margin 21.4% (2018), 23.3% (2019), 23.7% (2020), 23.5%
   (2021, as recast), 22.4% (2022), 22.5% (2023), 23.1% (2024), 21.4% (2025) (segment tables, 10-Ks FY2019 to FY2025). Eight
   years inside about two points, through a pandemic, an inflation, a metal-price spike and an electronics destock.
4. *Metal prices*: about half of Assembly Solutions' sales are metal content "whose price fluctuations are generally passed
   through to our customers" (Item 1); they move reported sales (+$143.4M in 2021, -$61.5M in 2023, +$64.4M in 2025) and
   the gross margin, much less the profit dollars. Hedged with metal derivatives whose realized losses ($30.3M in 2025)
   the segment profit includes (Note 22, footnote 1).

**Do the past statements tell me the future ones?** **[M2008-033]** Mostly yes for the operating line: the segment record
is long, the reconciliations are complete, and the margin series above is narrow. Less so for the whole company, which
buys and sells businesses nearly every year (2021, 2023, 2025, 2026), so the statements of ten years hence will describe a
different set of businesses.

**Contrary evidence, against understanding.** The filer writes that its industry "is subject to constant and rapid
technological change, product obsolescence, price erosion, evolving standards, finite product lifecycles" and that "Our
markets are competitive and subject to rapid changes in technology" (10-K FY2025, Items 1A and 1). The rows send that case
to TOO HARD: "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of
its long-term economics" **[L1993-023]**; where "the future technology could hurt the business as it presently exists [...]
it won’t make it through the filter" **[M1998-008]**. Test 6 cuts the same way: across the field (ESI, MKS's Atotech,
Qnity, Henkel, Senju, Uyemura, the rivals the 10-K names) I cannot say which supplier will hold which process in
ten years **[M2012-067]**, **[L2009-005]**.

**The judgment.** The rows define understanding as the economics, not the chemistry **[M2011-014]**, **[M2012-065]**. The
deciding segment's economics are a consumables-and-service model whose margin has held within two points for eight years
through every condition the period offered; that record is the filing fact that speaks to "how far off we can be"
**[M2011-084]**, and it says not far, for the margin. The risk-factor sentence is a general statement about "the specialty
chemicals industry", and the operating record of the deciding segment does not show the price erosion or obsolescence it
warns of. My doubt is concentrated in Semiconductor Solutions (wafer-level plating, die attach: 20% of Electronics sales,
about 14% of the company), where the technology of packaging is changing fastest; that business does not decide.
Inside the circle, narrowly: the insiders would not write a ten-year forecast of the semiconductor-packaging line
**[M2000-105]**, but the decision does not rest on it. I record that "if you have doubts about something being into your
circle of competence, it isn’t" **[M2002-092]**, and that a second analyst could fairly close this file here TOO HARD
(NATURE) on the filer's own risk factor; I do not, because the doubt attaches to a part that does not decide.

**VERDICT: IN** (narrowly), on the deciding segment's eight-year margin record and the consumable model the 10-K describes;
the fast-changing semiconductor line carried to Q2 as the main threat.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is the 1995 one: "why is that castle still standing? And what’s going to keep it standing or cause it not to
be standing" over the next decades, and "how permanent are they?" **[M1995-038]**; the moat is what "protects excellent
returns on invested capital" **[L2007-004]**.

**The parts table** (business of parts, Q2 CONVENTION of 2026-10-06). The filer reports no segment operating profit; its
only segment profit measure is Adjusted EBITDA, so the shares below are of five-year segment Adjusted EBITDA
(*CONVENTION of this run*: the filer's own segment profit measure stands in for operating profit; depreciation, the only
item between the two at segment level, is allocated $25.5M to Electronics and $15.5M to Specialties in 2025, so the
shares would barely move). Figures as last presented: 2021 from the FY2022 10-K recast, 2022 from the FY2023 10-K, 2023 to
2025 from the FY2025 10-K (`0001590714-23-000027`, `0001590714-24-000054`, `0001590714-26-000018`); USD millions.

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Electronics | 372.0 | 360.7 | 317.7 | 361.5 | 382.2 | 1,794.1 | 68.6% | see the tests below | **yes** (more than half) |
| Specialties (Industrial & Specialty until Q4 2025) | 152.8 | 165.9 | 164.6 | 173.2 | 165.4 | 821.9 | 31.4% | narrower: industrial plating chemistry, flat organic sales in 2025, European volume declines (10-K FY2025, MD&A) | no |

The file closes on Electronics. Specialties is not shown open on the evidence (its margin rose from 17.7% in 2022 to 21.6%
in 2025, partly by selling the lower-margin Graphics business); were it open it would be carried to Q7 at no growth.

**The castle tests, each with its filing fact (Electronics):**
1. *Key factors and their permanence* **[M1995-038]**. The 10-K names them: consumables "replenished in order to continue
   production"; products that are "a small portion of our customers' costs" yet "integral to customer product
   performance"; "operational risks and switching costs make it difficult for our customers to change suppliers"; about 40%
   of 5,200 employees are chemists or technical service and sales staff; qualification "into their supply chains" with
   customers and OEMs (Item 1). The brands are old (Alpha, Kester, MacDermid, Enthone lines). The model is decentralized
   and depends on no named lord in the castle.
2. *The attacker with money* **[M2011-015]**. The field's own case: MKS bought Atotech, the largest circuit-board plating
   chemistry supplier, in August 2022 and recorded goodwill and intangible impairments at that division (MSD) of $1.3
   billion in the quarter ended 2023-06-30, "in part due to softer industry demand, particularly in the personal computer
   and smartphone markets" (MKS 10-K FY2023, `0000950170-24-021071`). Atotech's last 20-F showed 2021 revenue of $1,499.2M
   (`0001193125-22-100614`); MKS reports MSD revenue of $1,181M (2024) and $1,323M (2025) (MKS 10-K FY2025,
   `0001193125-26-066820`; IFRS against U.S. GAAP and a change of owner, so the comparison is indicative only). In the same
   span ESI's Electronics sales rose from about $1.58 billion (2021) to $1.79 billion (2025), helped by metal prices.
   Money bought a franchise in this field; it did not buy growth against the incumbents.
3. *Pricing power, and the agony before a rise* **[M2005-020]**. ESI does not split price from volume. Through the
   2021-2022 inflation the Electronics margin moved from 23.5% to 22.4% and recovered to 23.1% in 2024; metals are passed
   through by contract, and "over time the businesses with strong competitive positions manage to pass through increases in
   raw material costs" **[M2005-017]**. Against: the 2025 Electronics gross margin fell 170 basis points on "higher prices
   for pass-through tin and silver" (MD&A), and the nearest rival with a split shows price falling every year: Qnity's
   Interconnect Solutions "local price & product mix" -2% in 2024 and -2% in 2025, Semiconductor Technologies -2% and -1%
   (Qnity 10-K FY2025, `0002058873-26-000010`); DuPont Electronics & Industrial -1% (2020), 0% (2021), 0% (2023), -2% (2024)
   (DuPont 10-Ks FY2021 `0001666700-22-000009`, FY2024 `0001666700-25-000005`). The field gives a little price each year and
   earns it back on volume and new products. The filer's own risk factor names "price erosion".
4. *Unit volume and share of mind*. Organic sales growth in Electronics: +10% in 2025 (Assembly +8%, Circuitry +10%,
   Semiconductor +13%), and +13% for the company in the first half of 2026 (10-Q). No consumer brand; the share that
   counts is the share of qualified specifications, which the filings do not quantify.
5. *The low-cost position*. Not claimed by the filer and not shown; the model sells performance and service, not price.
6. *Would the customer still choose it over the low bid?* **[M2017-009]**, **[M2016-009]**. The filer's account is that
   the chemistry is a small cost carrying a large risk to the customer's yield, which is the parachute case; the filings
   give no direct evidence of a customer paying more than a rival's bid.
7. *Ask the competitors* **[M1999-130]**: not done; no scuttlebutt was taken in this run. ESI lists MKS, Qnity, Henkel,
   Senju and Uyemura as its main Electronics competitors (Item 1).
8. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. The Electronics margin has neither widened nor narrowed in
   eight years (21.4% in 2018, 21.4% in 2025, 23.7% at the top). Relative to Atotech under MKS, ESI grew while MSD
   shrank.
9. *What could destroy, modify or reduce it* **[M2000-014]**: (a) a change in how chips and boards are packaged or
   joined that makes a plating or soldering step unnecessary (the filer's "product obsolescence" and "finite product
   lifecycles"); (b) China, 22% of 2025 sales ($557.9M, Note 22), and the tariff and export-control risks the 10-K lists;
   (c) metal-price spikes squeezing the margin before the pass-through catches up; (d) consolidation among rivals, which
   the 10-K names ("Further consolidation within our industry [...] could result in larger competitors"). "A moat that
   must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**: R&D is 2.6% of sales ($67.6M in
   2025), which argues the rebuilding is incremental, not wholesale.

**The competitor row** (each filer's own segment profit measure, as a margin on its own sales; the metrics differ and are
named):

| filer | metric | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | accession |
|---|---|---|---|---|---|---|---|---|---|
| ESI Electronics | segment Adj. EBITDA % | 23.3 | 23.7 | 23.5 | 22.4 | 22.5 | 23.1 | 21.4 | ESI 10-Ks above |
| ESI Specialties | segment Adj. EBITDA % | 21.8 | 21.3 | 18.7 | 17.7 | 17.9 | 19.3 | 21.6 | ESI 10-Ks above |
| Atotech EL (electronics chemistry and equipment) | segment Adj. EBITDA % | 35.4 | 32.5 | 33.7 | bought by MKS | | | | 20-F `0001193125-22-100614` |
| Atotech GMF (metal finishing) | segment Adj. EBITDA % | 27.4 | 24.0 | 24.6 | | | | | same |
| DuPont Electronics & Industrial | Operating EBITDA % | 32.7 | 31.4 | 31.7 | 31.0 | 27.6 | 29.0 | spun as Qnity | `0001666700-22-000009`, `0001666700-25-000005` |
| Qnity Interconnect Solutions | Adj. Operating EBITDA % | | | | | 18.7 | 23.8 | 25.5 | `0002058873-26-000010` |
| Qnity Semiconductor Technologies | Adj. Operating EBITDA % | | | | | 34.5 | 36.1 | 35.8 | same |
| MKS MSD (Atotech) | segment gross margin % | | | | | | 56.1 | 54.1 | `0001193125-26-066820` |
| Entegris Materials Solutions (SCEM before 2023) | segment profit % | | 18.8 | 22.0 | 15.8 | 17.5 | 20.4 | 19.7 | `0001101302-23-000021`, `0001101302-26-000012` |

Non-filers flagged: Henkel, Senju Metal Industry and Uyemura (named by ESI), Umicore and Heraeus (named in the brief) file
no U.S. reports; Atotech filed 20-Fs for 2020 and 2021 only. Entegris is not among the rivals ESI names; it is shown because
the brief asked. ESI's margins are lower than DuPont's and Atotech's partly because about half of Assembly Solutions' sales
are metal passed through at little margin.

**The field's returns over the last full cycle, judged in words.** The cycle in the window runs from the 2021 rebound
through the 2023 destock (ESI organic -5%, DuPont E&I volume -11%) to the 2025 recovery. On the capital the business
needs **[M2010-090]**, ESI's pre-tax earnings before amortization (operating profit plus amortization, plus the 2023
goodwill impairment) against equity plus net debt less goodwill and intangibles ran from about 47% to 74% a year, 2021 to
2025 (from the balance sheets in Q4; 2025: $452M on $775M). The rivals' margins sit at or above ESI's through the same
trough. What is ordinary is the return on the prices paid for these franchises: ESI earns about 10% to 12% pre-tax on total
capital including goodwill, and MKS wrote off $1.3 billion of what it paid. The rows judge the business on the capital it
needs and the purchase on what was paid **[M2010-090]**, so this is not the standing castle that protects only ordinary
returns.

**Contrary evidence, written down** **[M1997-127]**: the field gives price every year (Qnity, DuPont); the filer warns of
obsolescence and price erosion; the semiconductor line sits in the fastest-changing part of the field; no scuttlebutt was
done; and the steadiness of the segment margin is partly the metal pass-through smoothing a gross margin that moved from
42.4% (2020) to 37.4% (2022) and back to 42.0% (2025).

**VERDICT: IN** for the deciding part, Electronics: a consumable, qualified, technically serviced position whose margin has
held for eight years through a destock and an inflation, in a field whose rivals earn similar or higher margins on little
tangible capital. The tenuous-moat close, "We don’t know how to valuate that" **[M2000-019]**, is for a moat the record
shows to be tenuous, and none of the threats above is shown on the filings to be filling this one in.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The question: "does it look like it has good economics? Has it earned high returns on capital?" **[M1995-051]**, measured
"in terms of the capital actually needed in the business" **[M2010-090]**, on tangible assets, with goodwill left for the
judgment of capital allocation **[M2011-060]**.

**Return on the capital actually needed** (USD millions; operating profit plus amortization of intangibles, plus the 2023
goodwill impairment, against equity plus debt less cash less goodwill and intangibles, year-end balances from `tools/run.py`
checked to the 10-Ks; pre-tax):

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| operating profit | 299.9 | 325.3 | 173.6 | 343.9 | 342.2 |
| + amortization (+ impairment 2023) | 124.0 | 120.0 | 204.0 | 118.0 | 110.0 |
| = earnings before amortization | 423.9 | 445.3 | 377.6 | 461.9 | 452.2 |
| tangible capital employed | 575 | 742 | 755 | 984 | 775 |
| pre-tax return on it | 74% | 60% | 50% | 47% | 58% |
| total capital incl. goodwill (equity + net debt) | 4,058 | 3,961 | 3,971 | 3,848 | 3,674 |
| pre-tax return on it | 10.4% | 11.2% | 9.5% | 12.0% | 12.3% |

These figures are before the 2025 executive share grant is removed or added back: it sits inside 2025 operating profit as a
cost, and stays there. A high reported return is checked for "a cyclical peak in earnings, a monopolistic position, or
leverage" **[L1994-009]**: the window includes the 2023 trough and the return stayed near 50%; the return is on tangible
capital, so leverage does not make it.

**Reinvestment to stand still and to grow.** Capital spending ran $46.3M to $68.4M a year (1.9% to 2.8% of sales) against
depreciation of $39.7M to $42.6M; the filer expects about $75M in 2026 (MD&A) and states that its "existing fixed asset
base is well-maintained and, accordingly, requires low ongoing capital expenditures" (Item 1). The filing gives no
maintenance figure, so the owner's entitlement to "my best guess" of it **[M2000-144]**, **[L1999-024]** is met only by
depreciation as the proxy, "not inappropriate in most companies" **[M1998-127]**: about $41M a year, the rest of capital
spending growth. Working capital is the larger call on cash: receivables and inventory rise with sales and with metal
prices (operating cash in the first half of 2026 was $33.0M against $98.6M a year earlier, "primarily driven by higher
investment in working capital from rising metals prices", 10-Q MD&A).

**What the added capital earns.** The growth the company buys comes mostly by acquisition: $536.5M in 2021 (Coventya and
others), $214.8M in 2023, $861M in early 2026 (EFC and Micromax, 10-Q Note 2, of which $293M is goodwill), against
$321.2M received for Graphics in 2025. Net of the sale, total capital employed barely moved from 2021 to 2025 while earnings
before amortization rose from $424M to $452M, about 7% in four years; organic sales in the same years grew about 10%. The
organic business is the "best business" grade, more money with little put up **[M1998-081]**; the acquired growth is bought
at prices that earn the 10% to 12% the table shows on total capital, which the rows place with the capital allocation
question, not with the business **[M2011-060]**.

**WEIGHS FOR**: the business needs little tangible capital and earns very high pre-tax returns on it through a full cycle
**[M1995-051]**, **[M2010-090]**; the qualification, carried to Q6, is that most growth capital goes into acquisitions at
prices that earn ordinary returns, and the "little or no debt" criterion is applied at Q9.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, nine year-ends, before the income account** **[M2025-032]** (USD millions; first-filed XBRL
vintage printed by `tools/run.py`, read against the filed statements of the 10-Ks listed at Step 0; 2026-06-30 from the
10-Q):

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 10,252 | 2,743 | 478 | 1,156 | 490 | 4,201 | 3,137 | 5,480 | -870 |
| 2018 | 9,402 | 2,109 | 234 | 382 | 188 | 2,183 | 1,024 | 5,376 | -1,195 |
| 2019 | 4,324 | 2,221 | 190 | 364 | 200 | 2,180 | 944 | 1,521 | -1,536 |
| 2020 | 4,483 | 2,320 | 292 | 403 | 203 | 2,253 | 856 | 1,516 | -1,473 |
| 2021 | 5,138 | 2,481 | 330 | 492 | 274 | 2,526 | 957 | 1,907 | -1,332 |
| 2022 | 4,904 | 2,332 | 266 | 456 | 291 | 2,413 | 806 | 1,895 | -1,224 |
| 2023 | 4,974 | 2,328 | 289 | 462 | 299 | 2,337 | 879 | 1,932 | -1,183 |
| 2024 | 4,874 | 2,383 | 359 | 440 | 246 | 2,132 | 732 | 1,824 | -1,017 |
| 2025 | 5,101 | 2,674 | 626 | 518 | 295 | 2,242 | 657 | 1,626 | -905 |
| 2026-06-30 | 5,784 | 2,813 | 190 | not read | not read | 2,537 | 1,005 | 2,119 | not read |

What moved and why. (1) **2017-2019, the Platform roll-up unwound.** In 2017 Platform carried $5.5 billion of debt against
$7.3 billion of goodwill and intangibles; at the end of 2018 the agricultural business (Arysta) was held for sale, and the
FY2018 net loss from discontinued operations of $243M was "primarily due to the estimated impairment on the Arysta Sale of
$450 million" (10-K FY2019, `0001590714-20-000023`). The sale closed 2019-01-31 for net cash of $4.28 billion, and debt fell
from $5.4 billion to $1.5 billion. Platform reported net losses in every year 2014 to 2018 (XBRL: -$29.9M, -$308.6M, -$73.7M,
-$296.2M, -$324.4M); the accumulated deficit, -$1.5 billion at the end of 2019, is that record. (2) **2019-2025, a steady
business.** Equity $2.2 to $2.7 billion; goodwill $2.1 to $2.5 billion and intangibles amortizing down from $957M to $657M,
so tangible equity is negative (2025: about -$225M), as is usual for a company built from purchases. The deficit narrowed
every year from 2019 (-$1,536M) to 2025 (-$905M). Debt held at $1.5 to $1.9 billion. (3) **Receivables and inventory against
sales** **[M1995-064]**: receivables 19.8% of sales (2019), 20.5% (2021), 17.9% (2022), 19.8% (2023), 17.9% (2024), 20.3%
(2025); inventory 10.9%, 11.4%, 11.4%, 12.8%, 10.0%, 11.6%. No drift that the sales do not explain; no prepaid or deferred
account found building. (4) **2026: debt-financed purchases.** Goodwill up $295M and intangibles up $348M with EFC and
Micromax; cash down $437M and debt up $494M; the half-year's working capital absorbed the operating cash (Q3). What the
figures cannot say **[M2025-032]**: how much of the purchased intangibles depletes, and what the new businesses earn (the
10-Q says the acquisitions "were not significant" and presents no pro forma or post-acquisition results).

**The real costs.**
- *Depreciation* ($39.7M to $42.6M a year) sits below capital spending ($46.3M to $68.4M); depreciation is "almost always
  true costs" **[L2015-004]**, **[R1996-023]**, and owner cash below deducts the whole of capital spending, which is the
  larger.
- *Amortization of purchased intangibles* ($110M to $124M a year) is added back: "reported earnings plus [...] purchase
  accounting adjustments" are the rows' usual reading **[M1997-015]**, but "Some truly deplete over time" **[L2012-003]**.
  The developed technology among them does deplete; its replacement is paid through research spending ($67.6M in 2025)
  already charged in the accounts, so the add-back does not double count. Stated as this run's reading.
- *Stock pay* is a cost **[L2015-003]**: $40.1M (2021), $17.7M, $9.4M, $14.8M, $59.1M (2025). Owner cash deducts it in full.
- *Restructuring and the recurring "one-time"*: restructuring in every year ($11.4M, $7.8M, $5.6M, 2023 to 2025);
  "acquisition, integration and transaction expenses" in every year ($16.8M, $21.7M, $34.9M); "Other, net" in every year
  ($13.1M, $27.2M, $12.1M) (Note 22, FY2025). Each is excluded from the featured figure; "to tell owners year after year,
  "Don't count this," when management is simply making business adjustments that are necessary, is misleading"
  **[L2016-007]**. They are in GAAP operating profit and in operating cash, so owner cash counts them.
- *Metal hedges*: realized losses ($30.3M in 2025, $15.4M in 2024) are inside segment Adjusted EBITDA; only unrealized marks
  are excluded. Correctly counted.
- *Pensions*: the domestic plan overfunded by $5.0M, the foreign plans underfunded by $13.4M (MD&A). Immaterial.
- *Taxes*: cash taxes paid $73.7M, $87.2M, $98.8M (2023 to 2025, cash-flow supplement); the 2024 book charge was lowered by a
  $40.8M release of U.K. valuation allowances, which is not cash. Owner cash uses operating cash, so the company's own cash
  tax is what is counted.

**EBITDA in the filer's own mouth.** The chief operating decision maker allocates resources on "net sales and Adjusted
EBITDA" (Note 22); the segments are reported only on it; the annual bonus is paid on adjusted EBITDA, adjusted for metals,
currency and divestitures to reach the "Maximum" 200% payout in 2025 (proxy 2026, CD&A); the merger release sold the
combination on "a 26% adjusted EBITDA margin including run-rate synergies" and "net leverage of approximately 3.5x at
close" (`0001104659-26-080612`). The rows: "The one figure we regard as utter nonsense is the so-called EBITDA"
**[M1998-086]**; "where people are talking about EBITDA, is going to be about zero" **[M2002-026]**; "bullshit earnings"
**[M2003-109]**. **And the item that matters most here:** the reconciliation from net income to Adjusted EBITDA for 2025
adds back "2025 executive share grants" of $37.1M, the shares the board granted to five executives in December 2025 (Q5).
The executives' own pay is waved out of the measure on which their bonuses are paid and on which the company is presented:
"a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us
nervous" **[L2016-006]**; of those who wanted their stocks to float higher, the rows say they "found they could do it a lot
easier if they didn’t count compensation expenses" **[M2003-112]**.

**Guidance and targets.** The company gives guidance ("the momentum in our business continues unabated and in-line with
our guidance", CEO, termination release, 8-K `0001104659-26-102559`) and sets adjusted-EPS and adjusted-EBITDA targets for
pay. Recorded **[L2019-006]**, **[L2002-041]**, carried to Q5.

**Confusion or suspicion from the accounts themselves?** None found. The statements are clear, the reconciliations
complete, the balance-sheet ratios steady, and no reserve, prepaid or deferred account moves suspiciously **[M1995-064]**;
nothing confuses **[M1995-063]**. The tells found are in what management features and pays itself on, which the
framework weighs here and judges at Q5. Preoccupation with adjusted figures is "a negative" and not "a total exclusionary
factor" **[M1994-018]**.

**The recast earnings for Q7.** Owner cash = cash from operations less stock pay less all capital spending: $239.6M,
$230.4M, $271.5M, $278.8M, $168.5M (2021 to 2025), mean $237.8M; "a figure calculated after interest, taxes,
depreciation, amortization and all forms of compensation" **[L2021-003]**, with amortization of purchased intangibles
read as above. On the 2025 Adjusted EBITDA of $547.6M, owner cash was 31 cents on the dollar.

**VERDICT on the accounts: no STOP (neither confusion nor suspicion in the statements); WEIGHS AGAINST**, for the featured
adjusted figure that excludes the executives' own share grant and the yearly "non-recurring" items, EBITDA as the measure
of management, and guidance; all carried to Q5.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The question in the row that asks it whole: "do we really want to be in partnership with this person" **[M2015-005]**;
judged by "two yardsticks": "how well they run the business" against "the hand they were dealt", and "how well that they
treat their owners" **[M1994-008]**, read in the proxy, "how they treat themselves versus how they treat the shareholders"
**[M1994-009]**. The people: Benjamin Gliklich, CEO since January 2019, at the company since May 2014 (Platform's corporate
development, then COO and head of operations and strategy); Sir Martin Franklin, founder (Platform, 2013), Executive Chairman
since 2019, retiring from the board at the 2026 meeting; Ian Ashken, director, Franklin's co-founder at Jarden, proposed as
independent non-executive chairman (proxy 2026, `0001590714-26-000034`).

### The first yardstick: how well they run it (ability, the WEIGHING)
The hand dealt in 2019 was the remains of a leveraged roll-up: $5.4 billion of debt at the end of 2018, an agricultural
business written down by $450 million and sold for $4.28 billion, five straight years of net losses (Q4). Since then: debt
cut to $1.5 to $1.9 billion and held there; the Electronics margin held inside two points for seven years; organic growth
in five of seven years; the lower-margin Graphics business sold for about $320 million at a $66.5M gain; Electronics grew
while the largest rival franchise, Atotech under MKS, shrank (Q2). Measured against what the competitors accomplished in the
same field and cycle **[M1994-008]**, that is a good operating record. **Ability WEIGHS FOR.**

### The second yardstick and the integrity record (the STOP)
**The habits carried from Q4.** The featured Adjusted EBITDA leaves out restructuring, acquisition costs and "Other, net"
every year, and in 2025 leaves out the executives' own $37.1M share grant; the company gives guidance and pays itself on
adjusted targets; the proxy's highlights call 2025 "record results" while GAAP net income fell 22% (from $244.5M to $191.0M)
and owner cash fell 40% (from $278.8M to $168.5M).

**What the proxy shows of how they treat themselves.**
1. *The stretch awards, missed and replaced.* In 2022 the board granted "stretch" awards whose target was "to double
   adjusted earnings per share from 2021 to 2026". In 2025 the Compensation Committee, with FW Cook, found the target
   "unattainable", cancelled the awards "due to their lack of incentive value", and the board granted 750,000 shares to the
   CEO, 240,000 to the CFO, 160,000 and 90,000 to two other officers, and **225,000 to the Executive Chairman**, "to
   partially remediate the discrepancy between executive total compensation and the Company’s performance". The shares
   vested the day they were granted, 2025-12-10, worth about 75% of the original stretch awards' value, locked up in thirds
   over three years and subject to clawback (proxy 2026, CD&A, "Recent Developments" and "December 2025 Share Awards"). The
   CEO's reported pay for 2025 was $26.48M, against $6.91M for 2024 and $4.78M for 2023 (Summary Compensation Table).
2. *The grant waved out of the measure.* The $37.1M cost of those shares is added back in the Adjusted EBITDA the company
   features and pays bonuses on (Q4, Note 22).
3. *The sale seven months later.* On 2026-07-06 the board agreed to sell the company to Solstice. Under the agreement, PSUs
   held by executives with change-in-control agreements would vest "based on performance deemed achieved at (i) 200% of
   the target performance level for awards granted in 2024 and 2026 and (ii) 300% of the target performance level for
   awards granted in 2025" (8-K `0001104659-26-080825`, Item 1.01). The proxy's table of payments on a termination without cause or for good reason around a change in control showed
   $18.8M for the CEO had it occurred at the end of 2025 (salary $3.30M, bonus $3.63M, accelerated awards $11.85M). The deal was terminated on 2026-08-27 "based on
   constructive feedback from our shareholders", the chairman saying the shareholders "appreciate the strength of our
   management team" (8-K `0001104659-26-102559`, Exhibit 99.1).
4. *The founder's arrangements.* Under an advisory agreement of 2013, Mariposa Capital, "an affiliate of Sir Martin", was
   paid "an annual services fee of $2.0 million" in 2025, and will keep advising "for a minimum of three years" after he
   leaves the board; the Miami headquarters is leased from "An affiliate of Sir Martin" (proxy 2026, Transactions with
   Related Parties). The same founder's Platform issued shares heavily to build the roll-up (diluted shares 203.2M in 2015,
   288.2M in 2018, XBRL) and lost money on it.

**Management's case, stated as well as I can** **[M2016-055]**. Shareholders earned top-quartile returns over three and five
years while the CEO's pay sat in the bottom quartile of the peer group; the stretch target was set off a 2021 base that the
board now calls a post-pandemic record, so it measured the base year's luck and not the managers' work, which the rows
themselves warn of **[L2005-003]**; the replacement paid 75% of the original value, "a below-threshold payout", in shares
locked up for three years; the annual bonus was adjusted for metals, currency and divestitures precisely so that pay
follows what the managers control **[M2003-019]**; the executives own a great deal of stock (the CEO 1,274,328 shares,
about $47M at today's price; the founder 12,585,913); the say-on-pay vote in 2025 passed with 93.92% (before the grant); and
when the owners objected to the Solstice deal the board listened and ended it at no cost. No director or officer has been
in a material legal proceeding in ten years (proxy, "Involvement in Certain Legal Proceedings"), and no restatement or
accounting tell was found at Q4.

**The rows, against that case.** "alignment means being a partner in both directions, not just on the upside. Many
"alignment" plans flunk this basic test" **[L1994-020]**: the stretch award's downside was the executives' to bear, and
when it arrived the board paid three quarters of the upside anyway; that is a plan that will "payoff no matter what
happens" **[M1999-018]**. The justification offered is the stock's relative return, the ride the rows refuse to pay for
**[M2000-062]**, and the Executive Chairman who received 225,000 shares sits on the board that approved them: "it’s a very
strange form of negotiation when the beneficiary is the one that also really does all the design" **[M1997-041]**. The
same grant was then excluded from the figure the company features **[L2016-006]**, and within seven months the same
board agreed a sale that would have paid the 2025 awards at three times target. "you don’t find people saying, you know,
“We’re a wonderful partnership,” and then voting themselves, you know, huge options" **[M2018-069]**; the 10-K's stated
"primary long-term measures of success" include "the growth in the intrinsic value of our shares". The first factor of
agency cost is the one this record raises, "the guy favors himself at the expense of the shareholders" **[M1995-109]**,
and the 1993 letter's third factor is exactly the "certainty with which management can be counted on to channel the
rewards from the business to the shareholders rather than to itself" **[L1993-020]**.

**The judgment.** Nothing here is hidden: every fact above is in the company's own filings, and no tell of dishonesty in
the accounts was found. The question the rows put is not whether a rule was broken but whether I can count on these people
to channel the rewards to the owners, and on this record I doubt it: the pay was rewritten when it failed, waved out of the
featured profit, and set to multiply on a sale that the owners themselves had to stop. The rows apply integrity on doubt,
not proof: "If you’ve got doubts, forget it." **[M2013-088]**; "we rule out 90 percent of the times. And we may be wrong
about a fair number that we’re ruling out." **[M2007-092]**. The lock-up and the clawback do not answer the doubt; they govern the shares after
they were given, not the decision to give them.

**VERDICT on integrity: OUT** (doubt about the treatment of owners, read with the adjusted-figure habit carried from Q4;
**[M2013-088]**). **Ability WEIGHS FOR.** The file closes here. Q6 to Q12 are NOT REACHED; the facts already found for them
are written under AFTER THE STOP, and every figure after this line is a COMPUTATION, NOT A CLEARANCE.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7: WHAT IS IT WORTH? NOT REACHED (computation for the reporting figures under AFTER THE STOP).
## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9: COULD IT RUIN US? NOT REACHED.
## Q10: IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT at Q5 (integrity, on doubt about the treatment of owners: the missed stretch awards replaced by shares vesting the
same day, that grant excluded from the featured Adjusted EBITDA, and a sale agreed seven months later with 2025 awards
vesting at 300% of target; read with the adjusted-figure habit carried from Q4).** Q1 IN (narrowly), Q2 IN, Q3 WEIGHS FOR,
Q4 WEIGHS AGAINST, Q5 ability WEIGHS FOR. Not a TOO HARD; Q11 belongs to a holding review. For the reporting figures, a
COMPUTATION, NOT A CLEARANCE: value range $4.56 to $5.78 a share (all-equity, default pair, cycle reading) against $36.62.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.

**Bearing on Q6 (the money and the owners).**
- Buybacks (cash-flow statements and XBRL): $507.1M in 2019 after the Arysta sale, $55.7M (2020), $19.6M for about 0.9M
  shares (2021, about $22 a share), $151.0M for about 8.0M shares (2022, about $19), none in 2023 or 2024, $25.0M for 1.2M
  shares (2025, about $21). About $556M of authorization remained at 2025-12-31; the 10-K describes the authorization only by the dollars
  remaining, and no price above which buying stops was found in the filings read ("entirely purchase-price dependent" **[L2016-002]**; "below its intrinsic value,
  conservatively-calculated" **[L1999-023]**). The prices paid since 2021 sit above every end of the computed range below.
- Dividends: $0.08 a share quarterly since late 2021; $77.8M paid in 2025.
- Deals: Arysta sold 2019 for $4.28 billion after a $450M estimated impairment; Graphics sold 2025 for about $320M at a
  $66.5M gain; acquisitions $536.5M (2021), $214.8M (2023), $861M (2026, debt and cash; $293M of it goodwill). The
  Solstice agreement would have exchanged ESI shares for 0.500 Solstice shares and $10.00 cash; ESI was the target, so the
  undervalued-acquirer STOP **[L2009-019]** does not describe it.
- Issuance: no share-paid acquisition found since 2019; an EFC earn-out of up to 1.16 million shares; 1.45 million
  performance RSUs granted to EFC executives (grant-date value $37.5M, 10-Q Note 2). Platform's earlier serial issuance
  (diluted shares 203.2M in 2015, 288.2M in 2018) is the founder's record **[L2014-015]**.
- Retention test **[R1995-009]**: not run.

**Bearing on Q7: the reporting figures, a COMPUTATION, NOT A CLEARANCE** (`Test Runs/_research 2026-10-07 ESI/q7_computation.py`
and its output, committed beside this file). Value is "the discounted value of the cash that can be taken out of a
business" **[R1996-018]**, as a range **[L2000-024]**, at the 30-year Treasury, 5.64%; ten years at the growth shown, then
zero nominal growth (Q7 CONVENTION).
- *Cash input.* Owner cash after every real cost, as Q4 recast it: operating cash (after the company's own cash taxes and
  working capital) less all stock pay less all capital spending, 2021 to 2025: $239.6M, $230.4M, $271.5M, $278.8M,
  $168.5M; mean $237.8M. All-equity basis (central): net interest added back after tax, giving $282.4M, $270.8M, $310.4M,
  $323.3M, $210.7M, mean $279.5M (*CONVENTION of this run*: interest expense, net, added back at the U.S. statutory 21%,
  because the framework names no rate for the shield and most of the debt is borrowed in the U.S.).
- *(a) Cycles.* The filer itself calls 2021 "record 2021 results that were impacted by the post-pandemic market rebound"
  (proxy 2026, CD&A), so the window's first year is aberrational on its own description. The window holds one cycle
  (2021 rebound, 2023 destock, 2025 recovery) and no earlier cycle is comparable (the Platform years carry Arysta), so the
  five-year mean is taken as the cycle base and the growth is measured between the halves of the window, 2021-2022 against
  2024-2025 (*CONVENTION of this run*, borrowed from specific (b)'s fallback, because (a) asks for two cycles and the
  filings give one). Literal window beside.
- *(b) Decline.* Total growth on owner cash is negative on both readings (all-equity: -1.18% a year between the halves,
  -7.06% between the end years), so it is carried as negative and makes the bottom; no growth is the top **[M2006-058]**.
- *(c) Acquisitions.* Default pair: businesses bought net of businesses sold, mean $91.3M a year (2021 $536.5M, 2022
  $22.6M, 2023 $214.8M, 2024 $3.9M, 2025 -$321.2M), deducted, and the total growth credited **[M1998-080]**,
  **[M2014-068]**. Organic pair beside: acquisitions left out, only the filer's organic growth credited, 2.40% a year
  (+5%, -5%, +4%, +6% for 2022 to 2025). The 2026 deals, closed after the window, are valued on their own filed record:
  the 10-Q presents no pro forma or post-acquisition results, only gross profit, so they are credited at nothing, and their
  financing is already inside net debt at 2026-06-30.
- *(d) Working capital* is inside operating cash. *(e) Growth spending:* the filing gives no maintenance figure; the
  all-spending case is central; charging only depreciation ($41M) instead of all capital spending ($55.5M mean) would add
  about $14.5M a year to the base and moves no conclusion. *(f) The cap:* no growth is carried after year ten
  **[M1997-095]**.
- *Whose tax:* the company's own (cash taxes inside operating cash); no carryforward shelter was priced.
- *Basis:* all-equity, less net debt of $1,929.8M at 2026-06-30 **[L2017-004]**; equity-only beside (owner cash after
  interest, less the $861M paid for the 2026 deals, which the window's interest does not carry).

| case | all-equity range a share | fair price (midpoint at the floor) | equity-only range | equity-only fair price |
|---|---|---|---|---|
| **default pair, cycle reading (central)** | **$4.56 to $5.78** | **-$0.50** | $5.83 to $7.12 | $2.15 |
| default pair, literal window (beside) | -$0.03 to $5.78 | -$1.82 | $1.99 to $7.12 | $1.01 |
| organic pair (beside) | $12.42 to $16.69 | $4.53 | $13.77 to $17.39 | $7.05 |

  The fair price is the price at which the case at the midpoint of the range (growth halfway between the two ends) earns
  the floor of about ten percent **[M2003-149]**, **[L2002-020]**, **[M1994-004]** (Q7 CONVENTION) on owner cash after the
  company's own tax, discounted at 10% instead of the sovereign; a negative figure means the midpoint case does not cover
  the net debt at the floor, so the default pairs give no positive fair price. At $36.62 the price is above the top of every
  case, by more than double the top of the organic pair; owner cash yields 2.58% on the enterprise value against the
  5.64% bond. Had Q7 been reached it would have closed OUT by the floor however the range is read (Q7 specific (f)); no
  pencil was needed to see it **[M2009-005]**.

**Bearing on Q8.** The bond yields 5.64%; the mean owner cash before interest is 2.58% of the enterprise value and the
mean owner cash after interest 2.66% of the market value **[M1997-089]**.

**Bearing on Q9.** Debt $2,119.4M at 2026-06-30: term loans $1,272.9M (SOFR plus 1.75%, due 2030), $800M of 3.875% notes due
2028, $50.0M drawn on a revolver due 2031; $469M of availability; covenants met (10-Q Note 6, MD&A). The 2028 notes are "the
first significant debt principal payment" (10-K FY2025, MD&A), the maturity that "must actually be met by payment" if credit
is short **[L2010-020]**. Coverage on the rows' definition, pre-tax earnings over interest **[L2012-002]**: 2025 pre-tax
$265.6M plus net interest $53.4M, over $53.4M, about 6.0 times. Interest-rate and cross-currency swaps convert $350M of the
2026 add-on loans to fixed-rate euro debt; metal derivatives hedge Assembly inventory. The "little or no debt" criterion
**[R1997-001]** is stated for whole businesses.

**Bearing on Q12.** No business named in Q12 is among ESI's; offshore hydraulic fluids for oil and gas production are
about 3.5% of 2025 sales ($89.4M).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `6e47120e`); written question by question; committed after each
      (Q1 `2a9736f6`, Q2 `f9ef3934`, Q3 `d454fdca`, Q4 `82d6eb95`, Q5 `a98a012b`, close in the next commit).
- [x] Dispatched: the brief granted per-question pathspec commits; the lock in `Screens/_daily/` was present, written by the
      dispatching session ("interactive v5 re-runs batch 5", 2026-10-07 12:22), and was not touched. The fold is the
      dispatcher's; this run binds nothing until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; no listing of `Test Runs/` was
      made; the blind-listed items seen by accident are declared under CONTAMINATION at the top and not used. One file was
      briefly written to the repository root by a background fetch whose working directory was lost (a Qnity 10-K text
      dump); it was moved into the ignored `cache/` folder at once and never committed.
- [x] Every v5 id resolves (`check_ids.py`: no E-ids, every M/L/R id in the CSV, every quoted fragment beside an id
      found in that row); every filing fact carries its accession or names its filing.
- [x] The order was kept; Q5 failed on integrity and closed the run; nothing after it is a clearance, and the Q7 figures
      are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, from operating cash less all stock pay and all capital spending; never a
      net-income proxy (operator rule 5). The sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found (foundations, Q1, Q2); the facts for later questions are under AFTER THE
      STOP. Q5 itself judged the integrity facts, so no "integrity facts recorded, not judged" flag is needed.
- [x] Not a point-in-time run; rows of any date may be cited.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before every commit.
- Honest limits: no scuttlebutt; the competitors' returns on tangible capital were not computed (margins only); the
  retention test and the buyback-against-value test were not run (Q6 not reached); the 2019 and 2020 owner cash and the
  2026 acquisitions' earnings were not read; the proxy's peer-group TSR claims were not checked.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Pay after the fact sits between Q5 and Q6.** Q6 Part B says "no row found makes a pay plan alone a stop", while Q5
   applies integrity on doubt and reads the treatment of owners as its second yardstick; Q4's carried habits are judged at
   Q5. A board's decision to replace a missed award, then exclude it from the featured figure, is neither a plan nor an
   accounting tell. This run judged it at Q5 with the Q4 habits; a second analyst could weigh it at Q6 Part B and close at
   Q7 on price, with the same box OUT. The framework should say where a pay decision made after the outcome is judged.
2. **Q1 has no rule for the filer's own risk-factor language against its operating record.** ESI's 10-K says its industry
   is subject to "constant and rapid technological change", which matches the TOO HARD routing word for word, while eight
   years of segment margins say the economics have been steady. I weighed the record over the boilerplate and recorded
   that a second analyst could close Q1 TOO HARD (NATURE). The parts convention also stops at reported segments; my doubt
   was about a business line inside the deciding segment, which the convention does not reach.
3. **Q7 specific (a) assumes two cycles.** It asks for growth "between the averages of successive cycles"; a five-year
   window usually holds one, and the earlier years here belong to a different company (Platform with Arysta). I used the
   halves of the window, specific (b)'s fallback, and confessed it.
4. **Q7 specific (c), "credited at nothing where no earnings are filed".** The 10-Q files the acquired businesses' gross
   profit but not their earnings; I read gross profit as not earnings. The rule should say what counts.
5. **The all-equity basis needs a tax rate for the interest shield** and the framework names none; I used the U.S.
   statutory 21% and confessed it.
6. **A negative fair price** arises whenever the midpoint case at 10% is worth less than net debt; Part VII does not say how
   to report it. I reported the negative figure and said what it means.
7. **The template's parts table asks for "share of five-year operating profit"**, which ESI does not file by segment; I used
   the filer's segment Adjusted EBITDA and confessed it.

**Where this brief erred** (the dispatcher asked; every brief so far has contained an error):
- The slot "one line on the business, with any recent rename, merger or spin named" omits the largest recent event: the
  merger agreement with Solstice Advanced Materials signed 2026-07-06 and terminated 2026-08-27 (and, with it, the 300%
  award acceleration that bears on Q5). It also omits the two 2026 acquisitions ($861M), and it names the segment
  "Industrial & Specialty", renamed "Specialties" in the fourth quarter of 2025.
- It points the 2019 Arysta sale at "Q7's specifics on divestitures", but the sale closed 2019-01-31, outside the five-year
  window (2021 to 2025), so specific (c) does not reach it; the divestiture inside the window is the 2025 Graphics sale.
- Its competitor list includes Entegris, which ESI does not name, and omits three rivals ESI does name (Henkel, Senju,
  Uyemura), all non-filers that should have been flagged; Qnity was in fact spun off from DuPont on 2025-11-01; and
  Atotech's 20-Fs cover 2020 and 2021, the second filed in April 2022, so "before 2022" is loose.
