# Company Run — Sterling Infrastructure, Inc. (Nasdaq: STRL) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching
session at the fold, after the run was committed (ea283ced): `PORTFOLIO.md` read for this ticker only; not held.*

**Dispatch.** A blind analyst's purchase run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure:
the lines of evidence are derived by the analyst from the FY2025 10-K's Item 1, Item 1A and Item 7, and the competitors are
the rivals the 10-K names (it names none; see Q2). The lock is held by the dispatching session (operator rule ten).

**Contamination declared.** The first directory check of `Test Runs/` for today's date (made to confirm this run's file name
was free) printed the names of other run files and research folders dated 2026-10-16 for other companies. No file of them
was opened and nothing in them was used; no file for STRL or Sterling Construction appeared in that listing. The commit
subjects in the session's git context name another company's run (TEUFF); not opened, not used. Nothing else of the
blind-listed files was seen.

**Lines of evidence chosen, and from which item of the FY2025 10-K (accession 0000874238-26-000024):**
1. *Item 1:* what the deciding part sells and to whom: E-Infrastructure site development and (since CEC) mission-critical
   electrical work for data centers, semiconductor fabrication, manufacturing and distribution; customer concentration
   (top four customers 27% of segment revenue in 2025, 31% in 2024, 40% in 2023); the company's own account of its
   competition and of the "convergence" it expects in a weaker market; the shift from low-bid highway work (79% of revenue
   in 2016, 9% at 2025) and the pre-2015 gross margin of about 4%.
2. *Item 1A:* E-Infrastructure demand "is cyclical"; fixed-unit-price and lump-sum contract risk; termination for
   convenience; dependence on a limited number of significant customers; acquisitions; working capital and bonding.
3. *Item 7:* segment revenue and operating margin by year (read back to 2019 through the FY2020, FY2022, FY2023 and FY2024
   10-Ks); Contract Capital and the operating cash it releases; acquisitions (CEC $562M, Drake $25M) and capital spending;
   distributions to noncontrolling interests; the debt and its covenants.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $424.36 (close 2026-10-16; Yahoo Finance chart feed through `tools/sources.py`; **aggregator, flagged**, live
  quote only per operator rule 5). The same feed shows the stock at $881.92 on 2026-06-25 and $1,005.68 as its 52-week high;
  the fall to $424.36 is a price fact, not evidence about the business (foundations).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **30,588,518** outstanding
  (10-Q for the quarter ended 2026-06-30, filed 2026-08-04, accession `0000874238-26-000103`, cover as of 2026-07-31;
  `python Screens/cover_shares.py STRL`). Check against issued less treasury: the same 10-Q's balance sheet shows 31,487
  thousand issued and 795 thousand treasury, 30,692 thousand outstanding at 2026-06-30; the cover count a month later is
  103 thousand lower, consistent with the open repurchase programme (no filing after the 10-Q states a share issue; the
  8-Ks after it, of 2026-08-03, 2026-07-10 and 2026-10-05, carry no share issuance). The cover count is used.
- **Market cap:** 30.588518M x $424.36 = **$12,980.5M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-15 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-26, accession `0000874238-26-000024` (Items 1, 1A, 7, 8:
  statements, Notes 3, 9, 12, 20); 10-Q Q2 2026, filed 2026-08-04, `0000874238-26-000103` (statements, Notes 3, 9, 18,
  MD&A, Part II Item 2); DEF 14A filed 2026-03-25, `0000874238-26-000042` (ownership, CD&A, summary compensation);
  8-Ks `0001193125-25-142774` (CEC asset purchase, 2025-06-18), `0000874238-26-000093` (Second Amended and Restated Credit
  Agreement, 2026-07-08), `0000874238-26-000095` (general counsel's retirement notice, 2026-07-10),
  `0000874238-26-000100` (Q2 2026 results and EX-99.1 press release, 2026-08-03), `0000874238-26-000110` (new general
  counsel, 2026-10-05); for the cycle: 10-K FY2020 `0000874238-21-000010`, FY2022 `0000874238-23-000023`, FY2023
  `0000874238-24-000032`, FY2024 `0000874238-25-000025`.
  **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $439,988
  thousand on the filed Consolidated Statement of Cash Flows (10-K FY2025, `0000874238-26-000024`), against $440.0M in
  the tagged series `tools/run.py` printed. They agree.
- `python tools/run.py STRL`, arithmetic lines only (output kept in the research folder): OCF $478.6M / $497.1M / $440.0M
  (2023 to 2025), SBC $14.6M / $19.0M / $24.2M, capital spending $64.4M / $81.0M / $77.3M, D&A $57.4M / $68.4M / $77.1M,
  finance-lease principal $0.1M to $0.2M a year. The tool's three-year owner-cash mean ($378.4M capex basis) and its
  five-year figure ($276.2M) are transcription; the run's own recast is at Q7 below (owner cash after every real cost:
  stock pay, all capital spending net of equipment sales, distributions to noncontrolling partners, the tax the 2021 to
  2022 loss carryforwards sheltered). SBC is resolved and complete (ShareBasedCompensation each year, matching the filed
  cash-flow line). The tool's warning lines do not apply (D&A includes depreciation; intangible amortization of $22.2M in
  2025 is separate in the filing and is read at Q7). Nothing the tool printed as a rule, id or verdict is used (Part VII).

### The balance sheets, ten year-ends, read before the income account **[M2025-032]**
*(Read here in Step 0 because the file closes before Q4, as the template asks.)* `tools/run.py` table (first-filed XBRL
vintage), checked against the filed balance sheets of FY2025 and Q2 2026 and the FY2020 to FY2024 10-Ks named above, USD
millions:

| year-end | assets | equity | cash | goodwill | intangibles | LT debt (non-current) | retained earnings | contract liabilities |
|---|---|---|---|---|---|---|---|---|
| 2016 | 302 | 107 | 43 | 55 | 0 | 2 | -102 | n/a |
| 2017 | 463 | 141 | 84 | 85 | 45 | 86 | -90 | 62 |
| 2018 | 483 | 164 | 94 | 85 | 42 | 79 | -65 | 62 |
| 2019 | 962 | 220 | 46 | 192 | 256 | 391 | -25 | 85 |
| 2020 | 953 | 267 | 66 | 192 | 245 | 291 | 17 | 114 |
| 2021 | 1,231 | 359 | 82 | 260 | 303 | 429 | 80 | 128 |
| 2022 | 1,442 | 475 | 182 | 263 | 299 | 399 | 186 | 239 |
| 2023 | 1,777 | 619 | 472 | 281 | 328 | 315 | 325 | 444 |
| 2024 | 2,017 | 808 | 664 | 265 | 316 | 290 | 582 | 509 |
| 2025 | 2,634 | 1,109 | 391 | 585 | 555 | 276 | 873 | 652 |
| 2026-06-30 (10-Q) | 3,194 | 1,357 | 464 | 616 | 660 | 269 (+15 current) | 1,124 | 803 |

What moved and why. **Equity against goodwill and intangibles:** equity rose ten-fold, from $107M to $1,357M, but goodwill
and intangibles rose from $55M to $1,276M; Sterling stockholders' equity less goodwill and intangibles was $81M at
2026-06-30. The growth of the asset side is bought businesses: Plateau (2019), Petillo (2022), the plumbing and
foundation businesses (2022 to 2025), CEC (2025, $562M) and Stone Ridge (2026, $178M). **Retained earnings:** an
accumulated deficit of $102M in 2016 (the filer's own account: low-bid heavy highway work at about 4% gross margin before
2015) turned to $1,124M, of which $542M was added in 2025 and the first half of 2026. **Cash:** from $43M to a peak of
$664M (2024), back to $391M after the CEC purchase, $464M at mid-2026, of which $158M sits in consolidated construction
joint ventures (VIEs). **Debt:** borrowed for Plateau ($391M in 2019) and paid down since; the term loan of $285M was
repaid on 2026-07-02 from a new $1.5B revolver with $90M drawn (8-K `0000874238-26-000093`). **Working capital:** contract
liabilities (customers' advance billings) rose from $62M to $803M, faster than sales; the operating cash released by
operating assets and liabilities was $252.5M in 2023 and $199.8M in 2024 (filed cash-flow statements). What the figures
say: the cash of 2023 and 2024 was in large part customers' money paid ahead of the work. What they do not say: whether
that money stays when the projects end; in 2025 and 2026 receivables rose ($247M at 2024, $501M at 2025, $771M at
2026-06-30) as the CEC electrical work came in, and accounts receivable plus contract assets now exceed contract
liabilities ($927M against $803M at mid-2026; $302M against $509M at 2024). The direction of the working-capital
cushion has turned. What they cannot say: what the hyperscale and semiconductor customers will spend after the backlog.
**Contrary evidence, written down as found [M1997-127]:** a large part of the five-year operating cash is customers'
prepayment that reverses when volume falls; the tangible equity behind the business is small; the balance-sheet growth is
mostly purchased.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would own this "if the market closed for five years" **[M1997-109]**, and the
fall in the quote from $881.92 in June to $424.36 tells nothing about the business; "It just tells us prices" **[M2006-077]**.
The foundation that bears hardest here is the analyst's habit of looking for "what’s wrong in things" and "what you’re
missing" **[M2025-013]**: the name comes after a year in which revenue nearly doubled and a price that rose and halved, the
setting in which an analyst's own hopes are easiest to confuse with the business. Who is paid to tell you: the company's
own releases feature EBITDA, adjusted EBITDA and adjusted earnings per share that exclude stock pay (Q4 facts below).
No macro view enters. **Contrary evidence, written down as found [M1997-127]:** (1) the 10-K's own Item 1 says that in a
less favourable market small and large contractors would converge on its mid-level market and that this "could increase
competitive bidding pressure and reduce both revenue growth and margins"; (2) the same company earned about 4% gross margin
on its base business before 2015; (3) the field's margins rose at the same time as Sterling's (Q2 table); (4) customer
prepayments carried a large part of the 2023 and 2024 operating cash.

## THE STANDING RULE
Nothing in this file asks the buyer to borrow, to give anyone the right to demand cash of the buyer, or to size a position
that could end the buyer; a part-interest bought with the buyer's own money cannot by itself "risk what we have and need for
what we don’t have and don’t need" **[M2012-081]**, and the rule "Never risk permanent loss of capital" **[L2023-005]** is
met by the financing and the size, which are the buyer's. No breach.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** "can I understand it?" **[M1995-051]**, where understanding means "a reasonable fix
  on about what the earning power and competitive position will look like in five or 10 years" and "how the industry will
  develop and where the company will stand within the industry" **[M2012-065]**. The product can stay opaque if "I
  understand the economic dynamics of the industry", "are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **What the business is, from the filings.** Three reported segments (10-K FY2025, `0000874238-26-000024`, Note 20 and
  Item 7). E-Infrastructure Solutions: site development (clearing, excavation, grading, utilities) and, since CEC,
  electrical and mechanical work, for "large, blue-chip end users"; $1,466.8M revenue and $346.0M operating income in 2025
  (23.6%); 78% of revenue in Q2 2026, with mission-critical projects 92% of its backlog (EX-99.1,
  `0000874238-26-000100`). Transportation Solutions: highway, bridge, airport and rail work for state DOTs, $640.7M, 12.1%.
  Building Solutions: residential and commercial concrete foundations and plumbing in Texas and Arizona, $382.6M, 10.2%.
  The economics are those of a contractor: revenue is backlog burned at a margin set at the bid or negotiation and kept or
  lost in execution; the capital is equipment, people and contract working capital; contracts are mostly fixed-unit-price or
  lump-sum and can be terminated for convenience (Item 1, Contracts).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) the volume of mission-critical site and
  electrical work let in Sterling's regions; (2) the margin that work carries against rival bidders; (3) execution on fixed
  contracts; (4) the working capital customers will advance. The first is the customers' capital spending, read from the
  outside; the second is the castle question. The past statements tell the shape of the future statements (revenue from
  backlog, margin from mix), so test 3 of the draft, whether the statements "will tell me the information that’s useful to
  me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**, is met for
  the mechanics.
- **Routing.** The industry's own technology (earthmoving, concrete, electrical installation) does not change fast; the
  uncertainty is in the customers' demand and in whether rivals will compete the margin away. The draft sends the durability
  of a margin to Q2 and the rapid-change case to Q1 only where the business's own industry changes fast **[M2012-065]**,
  **[L2009-005]**. Not a bank, not a holding company; the segments are read by parts at Q2 (section B of the gaps case).
- **Contrary evidence, written down as found [M1997-127]:** where the deciding part will stand in ten years depends on the
  data-center and semiconductor building programmes of a few very large customers, and "Just because Charlie and I can
  clearly see dramatic growth ahead for an industry does not mean we can judge what its profit margins and returns on
  capital will be as a host of competitors battle for supremacy" **[L2009-005]**. That is a doubt about the margin's
  durability, which the draft owns at Q2; it is carried there, not dismissed. If I doubted that the mechanics of the
  business were inside the circle, the rule would be "it isn’t" **[M2002-092]**; I do not: a site contractor's economics
  can be read from its filings.
- **VERDICT: IN.** The economics of a regional site, electrical, highway and foundation contractor are understood from its
  filings **[M1995-051]**, **[M2011-014]**; the open question, whether the E-Infrastructure margin lasts, is the castle
  question and goes to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**, asked of a moat that
"protects excellent returns on invested capital" against competitors who "will repeatedly assault" it **[L2007-004]**.

**The parts table** (section B of the gaps case; segment operating income, 10-Ks FY2022 `0000874238-23-000023`, FY2023
`0000874238-24-000032`, FY2025 `0000874238-26-000024`, USD millions; 2024 as recast in the FY2025 10-K):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share | decides |
|---|---|---|---|---|---|---|---|---|
| E-Infrastructure Solutions | 80.5 | 121.5 | 141.0 | 203.4 | 346.0 | 892.4 | 67.7% | **yes (more than half)** |
| Transportation Solutions | 19.9 | 26.6 | 41.9 | 50.9 | 77.8 | 217.1 | 16.5% | no |
| Building Solutions | 32.6 | 36.7 | 46.2 | 53.8 | 39.1 | 208.4 | 15.8% | no |

The file closes on E-Infrastructure Solutions. Its own record (same 10-Ks, and FY2020 `0000874238-21-000010` for 2020;
H1 2026 from the 10-Q `0000874238-26-000103`):

| E-Infrastructure | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 |
|---|---|---|---|---|---|---|---|
| revenue $M | 397.3 | 468.8 | 905.3 | 937.4 | 923.7 | 1,466.8 | 1,502.7 |
| operating margin | 19.3% | 17.2% | 13.4% | 15.0% | 22.0% | 23.6% | 22.9% |
| filer's driver | Plateau full year | site development volume | Petillo acquired (lower-margin scopes) | advanced manufacturing and data centers up; e-commerce down | manufacturing timing and warehouses down, data centers up | data centers up; CEC from 2025-09 | large mission-critical projects; CEC; Stone Ridge from 2026-06 |

**The competitor row.** The 10-K names no rival: its Item 1 says only that competitors "vary widely, from small local
contractors to large international construction companies", and Item 1A that it competes "with many international,
national, regional and local construction firms". **The rivals below are therefore a CONVENTION of this run**, chosen as
SEC filers in the work the deciding part does: Granite Construction (GVA, CIK 0000861459; heavy civil and site work),
Primoris Services (PRIM, CIK 0001361538; utility, energy and civil infrastructure), EMCOR Group (EME, CIK 0000105634;
mission-critical electrical and mechanical construction, the work CEC brought). Rationale: no rival is named, and these
three file audited statements over the whole span. Metric: consolidated operating income over revenue, from each filer's
10-K tagged statements (every accession in `Test Runs/_research 2026-10-16 STRL/competitors_opmargin.txt`; FY2025: STRL
`0000874238-26-000024`, GVA `0000861459-26-000004`, PRIM `0001104659-26-018677`, EME `0000105634-26-000025`). Transcribed
from the tagged statements, not read in the rivals' filed documents; said so.

| operating margin | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | mean 2016-22 | mean 2023-25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STRL | -0.7% | 2.7% | 4.1% | 3.4% | 6.6% | 6.8% | 9.0% | 10.4% | 12.5% | 16.3% | 4.6% | 13.1% |
| GVA | 3.7% | 3.3% | 1.9% | -2.4% | -4.4% | 0.0% | 2.6% | 2.3% | 5.2% | 6.4% | 0.7% | 4.6% |
| PRIM | 2.9% | 4.5% | 4.4% | 4.5% | 4.7% | 4.9% | 4.4% | 4.4% | 5.0% | 5.4% | 4.3% | 4.9% |
| EME | 4.1% | 4.3% | 5.0% | 5.0% | 2.9% | 5.4% | 5.1% | 7.0% | 9.2% | 10.1% | 4.5% | 8.8% |

Compared over the whole span, never one year: from 2016 to 2022 Sterling as a whole earned what the field earned (4.6%
against 0.7% to 4.5%); from 2023 the field's margins rose with it (EME's doubled), so part of Sterling's rise is the field's
demand, not Sterling's alone. Against that, the E-Infrastructure part earned 13% to 19% in 2020 to 2023, above every rival's
consolidated margin in those years, before the margin rise of 2024 to 2026. (A segment margin carries no corporate overhead
and a consolidated margin does; the comparison is not like for like, and is said so.)

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent* **[M1995-038]**. The filer's own answer: "our ability to consistently provide on-time
   delivery and schedule assurance to our customers through successful project management and execution has become a key
   source of competitive differentiation", with the focus on "large, time-sensitive mission-critical projects where our
   superior capabilities are valued by our customers" (Item 1, Business Strategy). The factor is execution by crews and
   project managers; Item 1A says the business "depends on our ability to attract and retain talented employees" and that
   it faces "competition for experienced workers in all of our markets" (Item 1, Human Capital). Permanence is not shown.
2. *The attacker with money.* "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do
   it? [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. Earthmoving equipment can be bought;
   the 10-K itself names the attacker: larger national and international firms "that currently do not have a significant
   presence in our geographic markets, if they so desire, could establish a presence" (Item 1A, said of heavy highway), and
   in a weaker market "a convergence from both the small local contractors and large international construction companies
   into our targeted mid-level market" (Item 1, Competition). The company claims no barrier against money.
3. *Would the customer still choose it over the low bid* **[M2017-009]**. Contracts "are awarded on a competitively bid
   basis or negotiated bid basis" and "substantially all" of backlog is fixed-unit-price or lump-sum (Item 1, Contracts);
   for mission-critical work the filer reports schedule assurance valued above price, but the customers are few and large
   (top four 27% to 40% of segment revenue), can terminate for convenience, and the filer's own convergence paragraph says
   margins fall when bidding tightens. Whether the customer stays when the low bid is lower has not been tested in a year
   when the customers' building programmes fell.
4. *Pricing power and the agony before a rise.* "You can learn a lot about [...] the durability of the economics of a
   business by observing the behavior of — the price behavior." **[M2005-020]**. Margin in backlog rose from 16.7% (2024
   Q4) to 17.8% (2025 Q4) in a rising market (Item 7, Backlog); no year of falling demand is on the record for this part,
   so the price behaviour that matters has not been observed.
5. *The low-cost position.* No filing states a cost per unit of work against rivals; Sterling's claim is execution, not low
   cost. Where a field is commodity-like the rows' warning is that "commodity businesses have risk unless you’re the
   low-cost producer" **[M1997-010]**.
6. *Brand in the customer's mind; unit volume.* The customers are hyperscalers, colocation providers and manufacturers; no
   filing shows that they ask for Sterling by name rather than by qualification and schedule. Volume: E-Infrastructure
   revenue fell 1.5% in 2024 while the filer reports data-center volume rising that year; the deciding volume has not fallen.
7. *Ask the competitors.* Not on the public record for this field; no rival's statement about Sterling was found.
8. *Widening or narrowing* **[M1999-108]**. Widening in margin since 2022; the field widened at the same time (table above).
9. *What could destroy, modify or reduce it* **[M2000-014]**. The end or pause of the data-center and semiconductor
   programmes (mission-critical projects were 92% of E-Infrastructure backlog at 2026-06-30, EX-99.1 of
   `0000874238-26-000100`), which the 10-K calls "cyclical" demand (Item 1A); entry by larger firms; the loss of one of a few
   large customers (Item 1A, "We are dependent on a limited number of significant customers"). "one competitor is
   frequently enough to ruin a business" **[M2012-108]**.

**The field's returns over the last full cycle** (section C). The field's consolidated margins from 2016 to 2022 were thin
(GVA lost money in 2019 and 2020; PRIM and EME about 4% to 5%), and Sterling's were the same. Whether that is "ordinary" on
the capital employed is not settled by margins alone (contractors run on little capital, and the return on capital of the
rivals was not computed here), so the field is not shown to earn only ordinary returns and the file is not closed OUT on
that ground. The rows' commodity mark fits the transportation and building parts closely, "you can have only two
competitors and they’re still terrible businesses" **[M2013-052]**; it is not shown for the deciding part.

**The deciding finding: a change for the better, not yet tested by a cycle.** The company was a low-bid highway contractor
at about 4% gross margin before 2015 (Item 1); its deciding part has earned 13% to 24% since 2020, and 22% to 24% since
2024, all in years when the volume of its deciding market (data centers, advanced manufacturing) rose. The rows record that
such changes happen, "the railroads were a terrible business for decades and decades and decades and then they got good"
**[M2017-026]**, and they read a bad year by whether the competitive position held through it: "we believe you should view
last year's figures as reflecting a cyclical problem, not a secular one" **[L1995-022]**. Under Q2's rule a change for the
better is credited only on a full cycle in which the price behaviour held (**[M2005-020]**, **[L1995-022]**); no such cycle
is on the record for E-Infrastructure. The 2024 revenue dip of 1.5% is not that cycle: the filer ties it to the timing of
advanced-manufacturing projects and lower warehouse volume "partly offset by higher volume from data centers" (10-K FY2024,
`0000874238-25-000025`), so the deciding demand rose. Only a downturn can answer the question, and study does not cure
that: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries."
**[L1993-023]**. The castle is not shown open on the evidence (the deciding part's margins above the field's before the
boom are the evidence against OUT), and its future cannot be judged until the demand falls: "We don’t know how to valuate
that, and therefore we leave it alone." **[M2000-019]**.

**Contrary evidence, written down as found [M1997-127]:** for the castle: the deciding part's margin stayed between 13% and
19% from 2020 to 2023, through the 2023 decline in e-commerce distribution work the filer reports, and above the rivals'
consolidated margins; customers re-award phased work (unsigned awards of $1.28B and a "future phase" pipeline above $1.4B,
EX-99.1). Against the castle: the company's own convergence paragraph; its 4% history; the field's simultaneous margin rise;
customer concentration and termination for convenience.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**, **[M2000-019]**, **[L1993-023]**. Cause NATURE: the deciding question,
  whether E-Infrastructure's margin holds when its customers' building programmes fall, is answered only by that downturn.
  **Dated re-look condition:** the first fiscal year in which E-Infrastructure Solutions' revenue falls with no acquisition
  offsetting it, or in which the 10-K reports lower data-center or mission-critical volume for the segment, read from that
  year's 10-K; then Q2 is put again on the segment's operating margin in that year against 2023 to 2025.
- **Q3 to Q12: NOT REACHED** (operator rule 2). Facts already found are written under AFTER THE STOP below; the Q7
  arithmetic below is headed COMPUTATION, NOT A CLEARANCE.

## Q3 TO Q6: NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q7: WHAT IS IT WORTH? COMPUTATION, NOT A CLEARANCE
*The file closed at Q2. Everything in this section is arithmetic for the operator's two reporting figures (Part VII, The
owner's price; the brief's reporting convention). It carries no verdict and no entry language (operator rule 3); the box is
not changed by it (operator rule 2).*

**The cash input, recast** (filed cash-flow statements of the 10-Ks named in Step 0; USD millions; arithmetic in
`Test Runs/_research 2026-10-16 STRL/q7_compute.py`, output beside it). Owner cash = operating cash flow less stock pay,
less capital spending net of equipment sales, less distributions to noncontrolling owners, less the tax the federal and
state loss carryforwards sheltered in 2021 and 2022 (federal NOL $58.7M at 2020 year-end, about nil by 2022; computed at
the statutory rate under Q7, Whose tax; about $13M, split evenly). All-equity basis: plus net interest expense after tax
at 24% (the effective rate of 2024 and 2025), so that cash and its interest are not both counted.

| | 2021 | 2022 | 2023 | 2024 | 2025 | five-year mean |
|---|---|---|---|---|---|---|
| OCF as filed | 151.6 | 219.1 | 478.6 | 497.1 | 440.0 | |
| stock pay | 11.8 | 12.7 | 14.6 | 19.0 | 24.2 | |
| capital spending less equipment sales | 42.6 | 56.0 | 50.6 | 70.8 | 71.6 | |
| depreciation (D&A less intangible amortization) | 22.7 | 38.0 | 42.2 | 51.4 | 54.9 | |
| distributions to noncontrolling owners | 2.5 | 0.0 | 2.5 | 0.0 | 40.1 | |
| owner cash, equity-only, all spending | 88.2 | 143.9 | 411.0 | 407.3 | 304.1 | 270.9 |
| owner cash, all-equity, all spending | 102.9 | 158.9 | 422.5 | 405.5 | 302.1 | 278.4 |
| owner cash, all-equity, maintenance only | 122.8 | 176.9 | 430.9 | 424.9 | 318.8 | **294.8** |
| of which operating working capital released | 20.3 | 29.4 | 252.5 | 199.8 | 9.4 | 102.3 |
| cash paid for businesses, net of disposals | 180.9 | 18.0 | 37.2 | 11.2 | 480.3 | 145.5 |

- **Maintenance (specific e).** The filing says capital equipment "is acquired as needed by increased levels of production
  and to replace retiring equipment" (Item 7); the guess allowed is depreciation as the maintenance charge, so the central
  case is owner cash after depreciation, with spending above it charged against the growth it buys; all spending is shown
  beside. Management guides 2026 capital spending at $100M to $110M (not used; a projection).
- **Acquisitions (specific c), the serial acquirer.** Net cash purchases over the window, $727.6M, exceed half of owner
  cash before purchases ($695.9M). By the serial-acquirer convention the central figure is the organic pair: purchases
  left out, growth the organic growth the filer reports. The filer reports acquired revenue by year: Petillo $288.8M of
  2022's increase; 2023 "9.1% generated from organic growth"; the Texas plumbing business $61.1M of 2024's; in 2025 the
  increase of $610.2M excluding RHB, of which Drake and CEC were 9% of revenue ($224.1M). Organic revenue growth: 4.7%,
  9.1%, 4.2%, 20.5%; compound **9.44% a year**, 2021 to 2025. Applying the organic revenue rate to owner cash is ours,
  confessed here: the filer reports no organic owner-cash figure.
- **Growth shown and the cap (specific f).** Aggregate all-equity owner cash grew 30.9% a year (2021 to 2025). Carried ten
  years from the mean it would reach about $4,340M against sales of about $7,733M at the window's 12.0% sales growth, 56%
  of sales against the highest share earned in the filings read, 21.4% (2023): "if you trace out the mathematics of it,
  you bump into absurdities, then you better change expectations somewhat" **[M1999-067]**. The total-growth case is cut
  to sales growth, 12.0% (sales $1,581.8M in 2021 as reported, $2,490.0M in 2025); the organic 9.44% is under the cut.
- **Cycles and aberrational years (specific a).** The filer calls no year of the window aberrational. Two facts make the
  end years doubtful **[L2005-003]**: 2023 and 2024 carry $452M of working capital released by customers' advance
  billings, and 2021 predates the data-center build. The working-capital release is not tied by the filer to one contract
  (it cites "the increased size and duration of its projects"), so it stays inside the central figure, with the range
  without it shown beside (specific d).
- **Deals after the window.** Stone Ridge (closed 2026-06-01; $178.0M, of which $140.0M cash, $27.4M stock, earn-out up
  to $15M): no earnings filed (the 10-Q calls its results immaterial to date), credited at nothing; the cash paid is
  already out of the 2026-06-30 cash and the shares are in the cover count. No deal signed and not closed was found.
- **Net debt at the latest filed date** (10-Q 2026-06-30): borrowings $283.9M (current $15.1M, long-term $268.7M) plus
  finance leases $0.3M, less cash $464.5M, **net cash $180.6M**. Subsequent event stated by the filing: the term loan was
  repaid on 2026-07-02 from the new revolver ($90M drawn) and cash, no change to net debt. Left out and said so: operating
  leases ($52.9M); earn-out liabilities (about $57M at 2025 year-end, plus Stone Ridge's); $157.6M of the cash sits in
  consolidated construction joint ventures, part of it the partners'.
- **The rate.** 5.43%, the 30-year Treasury, 2026-10-15. Ten years at the growth case, then zero nominal growth.

**The range** (per share, all-equity basis less net debt, 30,588,518 shares):

| case | base $M | growth | no-growth end | growth end | top/bottom | fair price (each end at 10%, averaged) |
|---|---|---|---|---|---|---|
| **CENTRAL: all-equity, maintenance only, organic pair** | 294.8 | 9.44% | **$183** | **$383** | 2.1 | **$147** |
| equity-only, maintenance only, organic pair (beside) | 287.4 | 9.44% | $173 | $367 | 2.1 | $137 |
| all-equity, all spending, organic pair | 278.4 | 9.44% | $173 | $362 | 2.1 | $139 |
| equity-only, all spending, organic pair | 270.9 | 9.44% | $163 | $346 | 2.1 | $129 |
| default pair: purchases deducted, total growth cut to 12.0% | 149.3 | 12.0% | $96 | $240 | 2.6 | $87 |
| central without the working-capital release | 192.6 | 9.44% | $122 | $252 | 2.1 | $98 |
| literal window, shown growth uncut (absurd by the cap; shown only) | 294.8 | 30.9% | $183 | $1,934 | 10.9 | not a case |

**How Q7 would close, had it been reached.** The floor is tested first: at $424.36 (enterprise value $12,800.0M) the
central growth case returns about 4.95% a year and the no-growth case 2.30%, against the floor of about ten percent
**[M2003-149]**; no case of the range earns it. It would close OUT on the floor, whatever the width (2.1 to 1, narrower than
three). The price sits above the top of every case but the uncut one, which the cap removes.

**The two reporting figures (COMPUTATION, NOT A CLEARANCE; a reporting convention, not a verdict):**
- **(a) VALUE RANGE:** **$183 to $383 a share** (central: all-equity, maintenance-only, organic pair), against **$424.36**.
- **(b) FAIR PRICE:** **$147 a share** on the all-equity basis (each end case valued at ten percent, the two averaged; owner
  cash after the company's own tax, no conversion); **$137** on the equity-only basis beside it. The central figure is the
  all-equity one.

## Q8 TO Q10, Q12: NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q2**: the deciding part, E-Infrastructure Solutions (67.7% of five-year segment operating
profit), shows a change for the better (a 4%-gross-margin low-bid contractor before 2015; 22% to 24% segment margins since
2024) that no downturn of its customers' building has yet tested; re-look when E-Infrastructure revenue falls with no
acquisition offsetting it, or its 10-K reports lower data-center or mission-critical volume, and put Q2 again on that
year's segment margin. COMPUTATION beside it, not a clearance: range $183 to $383 against $424.36; fair price $147
(all-equity), $137 (equity-only). Integrity facts recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.*

**Bearing on Q3 (capital).** Sterling stockholders' equity less goodwill and intangibles: $81M at 2026-06-30; capital
employed less goodwill and intangibles is negative (equity $1,390.5M plus borrowings $283.9M less cash $464.5M, goodwill
$616.2M and intangibles $660.0M: about -$66M), because customers' advance billings ($802.6M of contract liabilities) fund
the work (10-Q `0000874238-26-000103`). With goodwill counted, 2025 operating income after tax at 24% ($308.5M) against
equity plus debt less cash at 2025 year-end ($1,006.7M) is about 31%. Capital spending net of equipment sales ran 1.2 to 1.9
times depreciation in 2021 to 2025. CEC: $561.6M paid (of which $79.5M in stock, earn-out up to $80M); its operating contribution was $19.4M in
four months of 2025 and $37.5M in the first half of 2026 (Item 7; 10-Q MD&A).

**Bearing on Q4 (the accounts).** (1) The company's release features EBITDA, adjusted EBITDA and adjusted net income and
EPS that exclude "non-cash stock-based compensation", intangible amortization, acquisition costs and earn-out expense
(EX-99.1 of `0000874238-26-000100`, its definitions); the rows call stock-based compensation "the most egregious example"
of real expenses owners are told to ignore **[L2015-003]** and EBITDA "utter nonsense" **[M1998-086]**. (2) Annual
guidance is given and was raised on 2026-08-03 (same release). (3) Revenue is recognized over time on cost-to-cost
estimates; substantially all backlog is fixed-unit-price or lump-sum (10-K Item 7, Critical Accounting Estimates; Item 1).
(4) 2024 net income carried a $91.3M non-cash gain on deconsolidating RHB (10-K FY2025, income statement). (5) The FY2025
internal-control assessment excluded Drake and CEC, 30% of assets and 9% of revenue, as SEC guidance permits (10-K Item 9A and the auditor's report).
(6) Receivables rose from $247M (2024) to $771M (2026-06-30) as revenue doubled. No restatement, no qualified opinion and
no building prepaid or deferred account was found in the filings read; the working-capital and receivable movements are
explained by the filer by mix and acquisitions.

**Bearing on Q5 (who runs it).** Joseph A. Cutillo, chief executive, director since 2017 (proxy `0000874238-26-000042`);
the chairman, Roger A. Cregg, is a separate independent director; seven of eight directors independent. Cutillo owned
369,839 shares at 2026-03-10 (about 1%); directors and officers 1.6%; ownership guidelines (5 times salary for the CEO,
5 times the cash retainer for directors); hedging and pledging prohibited. 2025 summary compensation for the CEO $8.41M
(salary $1.10M, stock awards $4.68M, non-equity incentive $2.53M). A named executive was "terminated without cause on March
14, 2025". The general counsel gave notice of retirement on 2026-07-06 and a successor was named on 2026-10-05 (8-Ks
`0000874238-26-000095`, `0000874238-26-000110`). Some CEC sellers "are now related parties"; a $15M payable to them is
tied to a pre-close receivable (10-Q Note 16, Related Party Transactions). **Integrity facts for a later run to answer** (the rule there: "If you’ve got doubts, forget it."
**[M2013-088]**): the featured adjusted figures that exclude stock pay **[L2016-006]**; earnings guidance, raised mid-year
**[L2019-006]**; incentive pay on adjusted figures (next paragraph); with the make-the-numbers habit, carried here under
section A of the gaps case **[L2002-041]**. Recorded, not judged.

**Bearing on Q6 (the money and the owners).** Annual incentive 2025: 75% on Adjusted EBITDA, paid at 200% of target
("above the maximum level"); performance shares two-thirds on three-year cumulative adjusted EPS and one-third on relative
total shareholder return (proxy CD&A). Buybacks: 604 thousand shares for $70.6M in 2024 (about $117 a share), 440 thousand
for $74.2M in 2025 (about $169), 69 thousand for $35.3M in the first half of 2026 (about $511; the June purchases 29
thousand at an average of $799.55); the $400M programme of 2025-11-12 names no price above which it stops (10-K Note 13; 10-Q Part II Item 2). Read against the COMPUTATION range (Q6's convention, written back here only as a fact): the 2024
and 2025 average prices sit below its bottom of $183; the 2026 purchases sit above its top of $383. Shares issued in deals:
$79.5M (CEC), $27.4M (Stone Ridge), smaller amounts in 2017, 2019, 2021 and 2022; no deal paid wholly or mostly in stock
was found, so Q6's all-stock STOP would not be engaged. No dividend. Distributions to joint-venture partners $40.1M (2025).

**Bearing on Q9 (could it ruin us).** After 2026-07-02: $90M drawn on a $1.5B secured revolver maturing 2031, against $464.5M
of cash at 2026-06-30; covenants net leverage at most 3.50 (4.00 in a covenant holiday after a deal over $250M) and interest
coverage at least 3.00 (8-K `0000874238-26-000093`). The surety is indemnified and holds a security interest in receivables
and "all proceeds and other rights under our construction contracts" (Item 1; Item 7, Bonding). Contracts can be terminated
for convenience; customer concentration as at Q2; multiemployer pension plans (Item 1A). $802.6M of contract liabilities is
work owed against cash already received; in a fall in volume that cushion runs off.

**Bearing on Q12.** None of the businesses the rows name.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `9aef4b18`); written question by question; committed after each
      (`523b2011` Step 0 to Q1, `50a4d493` Q2, then this section).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (a lock file was
      present in `Screens/_daily/` when the run began, seen in a listing, not touched). Folding is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One listing of `Test Runs/` filtered to
      today's date showed other companies' file names; declared under contamination at the top, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (check script in the research folder); every filing fact carries
      its accession or names the filing; numbers without a filing are labelled CONVENTION or computed in the script.
- [x] The order was kept; Q2's STOP closed the file; nothing after it is a clearance; Q7 is headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost (stock pay, all capital spending, minority distributions, the sheltered tax), never
      a net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as found at the foundations, Step 0, Q1 and Q2 **[M1997-127]**; facts for later
      questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor rule applies.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the final commit (run 2026-10-16, all checks OK); the run's own
      check script `check_cites.py` (no E-ids, every id in the v5 ledger, every quoted fragment in its row): 38 ids, 0 problems.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The re-look condition of Q2, section C, meets a mixed year.** The rule's trigger is "the first fiscal year in which
the business's volume or its field's volume falls". E-Infrastructure revenue fell 1.5% in 2024 while its deciding demand
(data centers) rose; read literally, the trigger has already fired and the question should be put again now, on a year
whose margin rose for reasons of mix. The run read the trigger as the deciding demand falling and said so; the text does
not say whether "volume" means the part's revenue or the demand that decides it. (2) **The serial-acquirer central figure
needs an organic growth of owner cash the filer never reports.** The convention asks for "organic growth as the filer
reports it"; filers report organic revenue at most, and this one only by naming acquired revenue year by year. The run
compounded the filer's organic revenue growth and applied it to owner cash, a step of ours, confessed in Q7. (3) **The
five-year mean lags a business doubling in a year.** The window's mean ($294.8M all-equity, maintenance) sits below 2025
alone and far below the first half of 2026 ($328.0M of operating cash in six months); specific (a) moves the base only for an
aberrational end year, and the filer calls none aberrational. The rows' warning about picked base years **[L2005-003]** cuts
both ways here, and the text gives no rule for a window that is all rise. The run kept the convention. (4) **Working capital
that is customers' money.** Specific (d) counts working capital and sets aside a single-event draw, but says nothing of a
multi-year release by advance billings that will reverse when growth stops; the run kept it in the central figure and showed
the range without it beside. (5) **Competitors when the 10-K names none.** The brief makes the choice a CONVENTION of the
run; the run used consolidated margins of three SEC filers against a segment margin, which is not like for like, and said
so.
