# Company Run — American Water Works Company, Inc. (NYSE: AWK) — 2026-10-28
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch (commit
`cc8b1ffe`). A dispatched blind run; working folder `Test Runs/_research 2026-10-28 AWK/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-28: the operator does not hold this name (`PORTFOLIO.md` has no AWK row).*

**Contamination, declared:** seen by accident at session start, not opened and not used: the git status listed another
company's research folder name (`_research 2026-09-27 ARCB`); the recent-commit subjects named another company's v5 re-run
folded OUT at Q7 (AQN-U); the session's memory index carried queue-state lines (wave counts, a count of gate-clearers, no
ticker for this company). None names AWK. The framework's own Q7 utility paragraph mentions sixteen utilities run on
2026-10-17 and 2026-10-18 without names; that is framework text, read as framework text.

**The lines of evidence, chosen from the 10-K's Item 1, Item 1A and Item 7 (the brief's second departure):**
(1) **regulation and rate-making**: the castle is a state franchise whose return a commission sets (Item 1, Regulation and
Rate Making; Item 1A first risk; Item 7 General Rate Cases), so the allowed returns and capital structures in the orders
were read; (2) **capital intensity and its funding**: a $46 to $48 billion ten-year plan, PFAS and lead-line mandates,
equity forwards and debt (Item 1 Capital Investment; Item 1A capital and indebtedness risks; Item 7 Liquidity, Capital
Structure); (3) **acquisitions and the Essential merger**, a stock-for-stock deal that also brings a gas utility (Item 1;
Item 1A merger risks; Item 7); (4) **what can take the franchise or the cash**: condemnation (Monterey), contamination and
dam liability, affordability and regulatory climate (Item 1 Condemnation; Item 1A; Item 3). Chosen because these four are
what the filing itself says decide the earnings and their certainty; MSG ("Other", 8% of revenue) is read only as a part.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $141.10 (close 2026-10-27, as printed by `tools/run.py`; an aggregator quote, live quote only, flagged per
  operator rule 5).
- **Shares:** one class, common stock $0.01 par, **198,728,989** outstanding as of 2026-07-20, from the cover of the
  10-Q for 2026-06-30 filed 2026-07-29 (accession `0001410636-26-000120`; `python Screens/cover_shares.py AWK`). Check:
  issued 204,215,977 less treasury 5,487,769 = 198,728,208 at 2026-06-30 on the same 10-Q's balance sheet (781 shares
  apart, plan issuance). No 8-K after the 10-Q reports a share issuance (the 8-Ks of 2026-09-09, 2026-09-16 and 2026-09-17
  are a debt offering and the merger settlement). **Beside, not counted:** 4,694,836 shares remain to be issued under
  the August 2025 forward sale agreements, settlement at the company's choice by 2026-12-31 (10-Q, Note on equity forwards).
- **Market cap:** $141.10 x 198.729M = **$28,041M**.
- **Sovereign for the earnings currency (USD):** **5.30%**, US Treasury daily par yield curve, 30-year, 2026-10-27
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for 2025, filed 2026-02-18, `0001410636-26-000034` (Items 1, 1A, 3, 7, 8:
  statements, segment note, rate orders); 10-Q for 2026-06-30, filed 2026-07-29, `0001410636-26-000120` (statements,
  forwards, Nexus closing, rate filings); proxy DEF 14A filed 2026-03-24, `0001193125-26-120668`; the joint proxy
  statement/prospectus for the Essential merger (424B3, filed 2025-12-31, `0001193125-25-337598`: board's reasons,
  projections, the advisers' analyses); 8-K of 2026-09-17, `0001410636-26-000143` (Pennsylvania settlement); Rule 425
  of 2026-10-27, `0001193125-26-434246`; the 10-K for 2023 (`0001410636-24-000050`) and for 2021
  (`0001410636-22-000048`) for the 2021 and 2022 statements and the 2020 balance sheet. No 10-Q for 2026-09-30 is on
  EDGAR as of today (the filing list's latest 10-Q is 2026-07-29). Competitors: see Q2.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities 2025, **$2,059M**
  on the Consolidated Statements of Cash Flows (10-K `0001410636-26-000034`), equal to the XBRL figure `tools/run.py`
  printed.
- **`tools/run.py AWK`, arithmetic lines only** (Part VII; its rules and labels not read): OCF 1,874 / 2,045 / 2,059,
  SBC 25 / 36 / 32, D&A 704 / 788 / 894, capex 2,575 / 2,856 / 3,126 for 2023 to 2025 (USD millions), all equal to the
  statements. **Corrected against the filing:** the tool's capex line leaves out "Removal costs from property, plant and
  equipment retirements, net" (109, 123, 159, 152, 175 for 2021 to 2025), which is cash spent on the plant and is counted
  as capital spending in this run; and the tool's "d3" debt column is total capitalization (equity plus long-term debt),
  not debt. SBC is resolved and complete (one stock-pay line; no options since 2017, proxy).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the water business will pay its owner over decades, "Would I be happy buying
this stock if the market closed for five years?" **[M1997-109]**. The market serves and does not instruct: the merger's
own adviser priced AWK by a cost-of-capital model and exit multiples, and the analyst rates in the joint proxy are
quotations, "It just tells us prices." **[M2006-077]**; neither is used. No macro view enters: the long rate is used as
the yardstick and nothing is forecast about rates, "macro conclusions are — just never enter into the discussion."
**[M2000-094]**. Who is paid to tell you: the projections in the joint proxy were prepared by the managements for a deal
they recommend, and the fairness opinions are bankers' (contingent fees, joint proxy); they are read as context and never
used as inputs. The analyst's habits: look for "what’s wrong in things" **[M2025-013]**. **Contrary evidence, written down
as found**: (i) owner cash after all capital spending was negative in every year of the window, between
-$449M and -$1,340M; the business has needed outside money every year (equity of $1,688M in 2023, $476M in 2026, debt every
year); (ii) the company's own capital structure moved from 44.2% equity to 40.6% in two years (10-K, Capital Structure);
(iii) the Essential merger adds a natural-gas distribution business the filer itself lists as a new risk; (iv) management
features an adjusted EPS figure and states 7-9% EPS and dividend growth targets, and the board pays on adjusted EPS. Each
was written down when found, since otherwise the mind "would reject contrary evidence to cherished beliefs" **[M1997-127]**.

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money puts no buyer at risk of ruin; the target's own debt (about $16B)
is weighed at Q9, not here. "it would be almost impossible to go broke without borrowed money being in the equation."
**[M1999-005]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**. The rows ask first to "identify the key variables in that particular business, and evaluating how predictable they
  were" **[M1998-044]**; here they are four and the filing states each: the rate
  base (the capital invested: $3.2B in 2025, a $46-48B ten-year plan, Item 1); the return the commissions allow on it (orders
  of 2024-2025 at 9.60% to 10.20% on equity with equity shares of 44.19% to 52.57%, Item 7); the lag between spending and
  rates (surcharges, future test years, Item 1 table); and customer counts (3,572 thousand at 2025, +0.8% a year organically
  plus acquisitions, Item 1). Each is predictable in the sense the rows ask: "the financial statements will tell me the
  information that’s useful to me in making a judgment about what the future financial statements are going to look like"
  **[M2008-033]**. The product does not change: no technology substitutes for a water main, and the forecast is about
  commissions and customers, not invention. The speakers held that an allowed return is close to certain, "when you get an
  allowed return in the electric utility you’re almost certain of earning it" **[M2010-037]**, and that utilities sell an
  essential under a cap, "The whole idea behind the utility industry is not to allow extraordinary profits." **[M2000-131]**.
- **What could put the ten years out of reach**, weighed: the regulatory climate can break, "I did not anticipate or even
  consider the adverse developments in regulatory returns" **[L2023-011]**; the filer names the same risk first in Item 1A
  and names 14 commissions, none above a quarter of revenue (Pennsylvania 24.1%, New Jersey 23.4%, Item 1 table), so the
  climate is a diversified variable, not a single forecast. PFAS ($2B capital, up to $50M a year of expense) and lead lines
  ($1.5B 2026-2030) are mandated spending the filer expects to recover in rates (Item 1); they are capital and lag
  questions (Q3, Q7), not opacity. The insiders do write this forecast down (rate filings state the capital, the return and
  the structure for the test years), the opposite of "That’s too hard." **[M2000-105]**.
- **Routing.** Not a fast-changing industry. Not a bank. A holding company read by its parts (Q1, A holding company): the
  Regulated Businesses carry more than all of the consolidated net income in each of 2023-2025 (Q2, parts table) and are
  understood; "Other" (MSG, 50-year military contracts, $7.4B backlog) does not decide. The unclosed Essential merger would
  add a gas distribution part; it is not owned at the price date and is valued beside (Q7 (c)), and it would be under a
  third of the combined company (joint proxy: Essential holders about 31%).
- **VERDICT: IN.** The economics ten years out can be foreseen in the sense **[M2012-065]** asks, from the rate orders and
  the plan the filer states; doubt about the perimeter was looked for and not found on the deciding part, the test being "if you have doubts
  about something being into your circle of competence, it isn’t" **[M2002-092]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing" **[M1995-038]**. The castle is the one the rows
name as "a natural franchise because of surface capabilities" **[M1995-037]**: a pipe network in the ground, held under
certificates of public convenience and necessity, whose price a commission sets.
- **The attacker with money.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do
  it?" **[M2011-015]**. The filer: its utilities "generally do not face direct competition in their existing markets
  because (i) the Company operates in those markets pursuant to franchises [...] and (ii) the high cost of constructing a
  new water and wastewater system in an existing market creates a significant barrier to market entry" (10-K Item 1,
  Competition). A second main down the same street is the railroad case, "You really couldn’t create another railroad"
  **[M2013-054]**; and one competitor would need the commission's certificate first. The competition the filer names is
  for **acquisitions** of municipal systems (Essential, American States Water, California Water Service, infrastructure funds),
  not for the customer.
- **Pricing power and the agony before a rise.** "you can almost measure the strength of a business over time by the agony
  they go through in determining whether a price increase can be sustained" **[M2005-020]**. Here the agony is
  institutional: every rise is petitioned, litigated and set by a commission (2025 authorizations $250M annualized across
  nine orders; pending requests in New Jersey, Pennsylvania, Illinois, Missouri, California, Virginia, Kentucky; Item 7 and
  10-Q). Requests are cut (Virginia asked $22M, settled at $16M; Illinois cut its own ask from $119M to $107M; California's
  decoupling mechanism was denied in 2024 and on rehearing in 2025). The power is a monopoly's with the price capped,
  "a business that’s a monopoly or a near monopoly" **[M2010-092]**, under "The whole idea behind the utility industry is
  not to allow extraordinary profits." **[M2000-131]**. The cap is the price of the castle, and the speakers name its
  failure mode, customer outrage at rising bills, "nationalize the whole thing" **[M2009-088]**; the filer answers it with
  average residential bills "at or below 1% of median household income" (Item 1, Affordability).
- **Unit volume.** Customers 3,188 thousand (2023), 3,217 (2024), 3,242 (2025) on water, plus wastewater 298 / 329 / 330;
  organic additions about 18,900 a year and acquisitions 20,900 in 2025 and about 52,700 in the first half of 2026 (Nexus
  closed 2026-06-01, $319M, 47,000 connections). Volume per customer moves with weather and conservation; two states
  (California, Illinois) decouple revenue from volume (Item 1, Seasonality).
- **The low-cost position and the low bid.** Not the test that decides here: the customer has no low bid to take, since
  the service area is exclusive. What a regulator rewards is cost discipline at the rate case, "There is no hiding your
  history when you stand before these regulators." **[L2008-008]**. Operating margin is 34.3% a year on average 2016-2025
  against 35.7% at Essential, 28.3% at American States, 16.8% at California Water (competitor row below), so AWK is not the
  high-cost operator in its field.
- **Ask the competitors.** The rivals the filer names compete to buy systems, and each of the three that file reports the
  same franchise form (their 10-Ks); none reports entering another utility's certificated area.
- **Widening or narrowing**: "whether it’s likely to widen further or shrink on you" **[M1999-108]**. Widening: more states allow future test years (Missouri from 2026-07-01 by
  Senate Bill 4), infrastructure surcharges in nine states, fair-market-value acquisition laws in twelve (Item 1). Narrowing:
  California's denial of decoupling; affordability pressure as bills carry PFAS and lead-line capital; the Monterey
  condemnation (40,000 customers, an offer of $448.8M rejected in 2023, the case pending; Item 3). The rows warn that the
  political compact itself is the exposure, "railroads, utilities, insurance companies, are all very much affected by the
  political process" **[M2012-074]**, and that it can break, "it is difficult to project both earnings and asset values
  in what was once regarded as among the most stable industries in America" **[L2023-011]**; the instance there was wildfire liability in
  electric utilities, and the filer reports the same no-fault property claims exist against water utilities in California
  (Item 1, Condemnation and Eminent Domain). Judged: slowly widening in law, under steady political pressure in rates; not
  filling in on the evidence of the window, where every year's orders granted increases.
- **What could destroy it**, "what can happen — say five, 10, 15 years from now — that will destroy, or modify, or reduce
  the economic strengths" **[M2000-014]**: a public taking, which pays for the assets (the
  law fixes compensation, Item 1), so it shrinks the castle without emptying it; contamination liability (PFAS designated
  hazardous under CERCLA in 2024; the company a passive receiver seeking legislative protection; Item 1); a commission that
  stops allowing a return (the "adverse developments in regulatory returns" **[L2023-011]**). None is shown on the filings to be under way at a scale that decides.

**The competitor row** (net income / average common equity, and operating income / revenue, each filer's own XBRL from its
10-Ks, latest vintage per year; `compare.py`, `compare_out.txt`):

| filer (latest 10-K accession) | mean ROE 2016-2025 | range | mean operating margin | revenue growth 2016-2025 |
|---|---|---|---|---|
| AWK (`0001410636-26-000034`) | 11.0% (10.2% without 2021, which carries the $747M pre-tax gain on the HOS and New York sales) | 8.0% to 18.4% | 34.3% | 5.0% a year |
| Essential Utilities (`0000078128-26-000050`) | 9.5% | 6.7% to 13.1% | 35.7% | 13.1% a year (Peoples gas bought 2020) |
| American States Water (`0001628280-26-009114`) | 13.6% | 11.2% to 16.8% | 28.3% (2017-2025) | 5.1% a year (2017-2025) |
| California Water Service (`0001628280-26-012444`) | 8.9% | 3.8% to 12.4% | 16.8% | 5.6% a year |

Named rivals not taken: Algonquin Power & Utilities (outside the brief's limit of three) and Nexus Water Group (privately
held, by the 10-K's own description; no SEC filings to read). Operating cash less capital spending was negative for AWK in
nine of the ten years and for every rival in most years where the tag is filed (the rivals tag capex inconsistently; the
comparison is carried on returns and margins, which all four file).

**The parts table** (segment note, 10-K `0001410636-26-000034`, Note 20; net income is the segment measure filed):

| part | net income 2023 / 2024 / 2025 ($M) | share of consolidated | castle | decides |
|---|---|---|---|---|
| Regulated Businesses | 971 / 1,065 / 1,137 | above 100% each year (Other is a loss) | the franchise above | **yes** |
| Other (MSG, a municipal contract, corporate) | -27 / -14 / -26 | negative | 50-year military contracts, terminable for convenience with cost recovery | no |

**The field's returns over the last full cycle.** The filer and the three rivals earned about 9% to 14% on equity over ten
years (table), with no year of loss: ordinary returns, but **set by regulators** (allowed equity returns of 9.60% to 10.20% in
AWK's orders of 2024-2025). Q2's list makes this the stated exception: "A return set by a regulator is the exception, carried
to Q3 as a second best" (framework, Q2), on "there’s no way we get rich on our utility investments. But there’s no way we
get poor, either." **[M2009-104]**. Not OUT on ordinary returns; carried to Q3.

- **VERDICT: IN.** The castle stands because no one can lay a second network and the certificate is exclusive, "a
  natural franchise" **[M1995-037]**; its weakness is that its price and return are political, "very much affected by the
  political process" **[M2012-074]**, which is a cap on the castle, not evidence that it is filling in. Not "a moat that’s
  tenuous in any way" **[M2000-019]**: the rows' own utility rows treat the allowed return as close to certain, "you’re almost
  certain of earning it" **[M2010-037]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed.** Net income over average common equity averaged 10.2% a year 2016-2025 without
  2021 (11.0% with it; competitor row, Q2). Of the capital-heavy business the rows ask only "decent returns on the
  incremental sums they invest" **[L2009-012]**, and accept it as "the second-best choice, still a good choice" **[M2018-055]**.
- **What the added capital earned, 2020 to 2025** (statements, 10-Ks `0001410636-22-000048` and `0001410636-26-000034`).
  On the equity: common equity rose $4,383M (6,454 to 10,837, of which $1,688M was new stock in 2023) and net income rose
  $402M (709 to 1,111): **about 9.2%** on the added equity, near the allowed returns. On all the capital: debt and equity
  together rose about $9,287M (17,394 to 26,681, short-term debt included) and operating income rose $631M (1,248 to
  1,879), about **5.3% after tax** at the 21.9% effective rate, which is the long government rate. The speakers measure this
  return "by the operating earnings after depreciation" **[M2014-086]**, and that measure says the equity's 9% is made by
  borrowing about three fifths of the capital; the rows read a high return for "a cyclical peak in earnings, a monopolistic
  position, or leverage" **[L1994-009]**, and here it is the last two, by design of the rate-making.
- **Reinvestment to stand still and to grow.** Capital spending with removal costs ran 2.9x to 3.7x depreciation every year
  2021-2025 (1,873 to 3,301 against D&A 636 to 894). The owner is entitled to the maintenance guess, "that’s my best guess. And I think the shareholders are
  entitled to my best guess" **[M2000-144]**; here it is the depreciation charge:
  "Every year we spend amounts equal to our depreciation charge simply to stay in the same economic place"
  **[L2000-035]**, the charge being "not inappropriate in most companies to use as a proxy for required capital
  expenditures" **[M1998-127]**; the filer's own split (renewal 70% of the ten-year plan, Item 7) does not separate
  maintenance from growth in the rows' sense, since replaced pipe enters the rate base and earns. On that guess the growth
  spending averaged $1,933M a year plus $204M of acquisitions, against owner cash after maintenance of about $1,000M: the
  business takes in more than it throws off every year, and the gap is borrowed or issued. Much of it is compulsory
  (PFAS by 2029, lead lines by 2037, pipe renewal toward a 100-year cycle; Item 1), which is the condition the speakers
  avoided, "a lot of compulsory reinvestment just in order to stand still" **[M1997-016]**, and inflation makes it worse,
  "To earn more, their owners must invest more." **[L2011-019]**.
- **For it, in the rows:** the pattern of a growing utility is the one they liked, "when it comes from a growing utility,
  we like it" **[M2014-088]**, because the added money earns the allowed return.
- **WEIGHS AGAINST**, narrowly. A second best the rows accept, "still a good choice" **[M2018-055]**, but the added
  equity earns the allowed return only through leverage, and the added capital as a whole, "measured by the operating earnings
  after depreciation" **[M2014-086]**, earned about the long government rate; and the reinvestment is large, continuous and
  largely compulsory, the "compulsory reinvestment just in order to stand still" **[M1997-016]**. ("Little or no debt" is
  applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends**, "balance sheets over an 8 or 10 year period before I even look at the
  income account" **[M2025-032]** (`tools/run.py` table, first-filed XBRL vintages; the 2020,
  2021, 2024 and 2025 columns checked against the filed balance sheets; USD millions; total debt = short-term debt +
  current portion of long-term debt + long-term debt with preferred):

| year-end | assets | equity | goodwill | receivables | total debt | debt / (debt + equity) | retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 18,482 | 5,218 | 1,345 | 269 | 7,182 | 57.9% | -873 |
| 2017 | 19,482 | 5,385 | 1,379 | 272 | 7,725 | 58.9% | -723 |
| 2018 | 21,223 | 5,864 | 1,575 | 301 | 8,611 | 59.5% | -464 |
| 2019 | 22,682 | 6,121 | 1,501 | 294 | 9,458 | 60.7% | -207 |
| 2020 | 24,766 | 6,454 | 1,504 | 321 | 10,944 | 62.9% | 102 |
| 2021 | 26,075 | 7,298 | 1,139 | 271 | 10,985 | 60.1% | 925 |
| 2022 | 27,787 | 7,693 | 1,143 | 334 | 12,385 | 61.7% | 1,267 |
| 2023 | 30,298 | 9,797 | 1,143 | 339 | 12,372 | 55.8% | 1,659 |
| 2024 | 32,830 | 10,332 | 1,144 | 416 | 14,037 | 57.6% | 2,112 |
| 2025 | 35,442 | 10,837 | 1,156 | 395 | 15,847 | 59.4% | 2,575 |

  What moved and why. Assets nearly doubled, all of it plant (net PP&E $30,576M of $35,442M at 2025). Debt grew 2.2x
  against equity 2.1x; the debt share was held between about 56% and 63% only because equity was issued ($183M 2018,
  $1,688M 2023, $476M in June 2026 with 4.7M shares still to come). Goodwill is a shrinking tenth of equity (it fell in 2021
  with the HOS sale) and receivables kept pace with revenue (8.1% of revenue in 2016, 7.7% in 2025): no account is
  "building up suspiciously high" against sales **[M1995-064]**. Retained earnings were a deficit until 2020. Cash is held near nil and
  working capital is a deficit (Item 1A, indebtedness); the business lives on commercial paper and the capital markets,
  which is Q9's question. What the figures cannot say: the rate base the commissions recognize is not on the balance sheet
  (the merger proxy gives a combined $33.5B at 2024 for both companies, AWK's share not separated), and deferred taxes of
  $3,190M are not equity, "I don’t think I would look at that as a hidden form of equity" **[M2015-030]**.
- **The real costs.** Depreciation is real, "almost always true costs" **[L2015-004]**, and here it is the maintenance guess
  (Q3). Stock pay is small ($17M to $36M a year) and is deducted. No recurring restructuring line; merger costs $13M in 2025.
  The removal costs of retired plant ($109M to $175M a year) sit in investing cash, not in earnings, and are charged as
  capital spending in this run (Step 0). The 2021 and 2022 figures carry the sale of the Homeowner Services Group and of the
  New York utility: a $747M pre-tax gain in 2021 net income and $280M of tax on the gains paid in 2022 operating cash (the
  filer's own description, 10-K 2023 MD&A); the seller note ($795M at 10%) paid interest into 2024-2025 earnings and was
  repaid in February 2026 (10-Q). Owner cash is therefore figured from cash flows with those items named (Q7), never from
  net income.
- **The filer's own mouth.** EBITDA appears only in the merger projections the managements gave the advisers (joint proxy),
  not as an earnings measure in the 10-K. The 10-K features **adjusted EPS** beside GAAP: $5.64 against $5.69 (2025),
  $5.18 against $5.39 (2024), $4.77 against $4.90 (2023); the adjustments take out favorable weather and the seller note's
  added interest and put back merger costs, so in each year the featured figure is **lower** than GAAP. That is the reverse of
  "attempts to wave away very real costs" **[L2016-006]**; it is still a featured adjusted figure, and the company states
  7-9% EPS and dividend growth targets (joint proxy, board's reasons) and pays its officers on adjusted EPS (proxy). Recorded
  as a weighing against and carried to Q5: "we become downright incredulous if they consistently reach their declared
  targets" **[L2002-041]**; the scourge the rows name is earnings "guidance" **[L2019-006]**.
- **VERDICT on the accounts: no confusion, no suspicion; WEIGHS AGAINST, mildly** (the targets and the adjusted-EPS pay,
  carried to Q5). Preoccupation of this kind is "a negative" the rows will not use "as a total exclusionary factor"
  **[M1994-018]**; nothing in the accounts confuses, the case of "when the accounting confuses you" **[M1995-063]**. The recast earnings feed Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** John C. Griffith, President and Chief Executive Officer since May 2025, promoted from the leadership team on M.
  Susan Hardwick's retirement (proxy: "CEO transitions in 2022 and 2025, each of which resulted in the promotion of an
  existing member of the Company’s executive leadership team"); an independent Board Chair (Karl Kurz), who would remain
  Chair of the combined company, with Essential's chief executive as Executive Vice Chair (proxy). Chair and chief executive
  are separate, which is the arrangement the rows prefer, since "I've seen how hard it is to replace a mediocre CEO if that
  person is also Chairman." **[L2014-026]**.
- **The two yardsticks**: "how well they run the business" and "how well that they treat their owners" **[M1994-008]**.
  Run: rate-case execution across 14 commissions, ROE held near 10% for a decade, an operating margin above two of the three
  rivals (Q2), customer counts and acquisitions rising, a ten-year capital plan disclosed by purpose. Treat the owners: total
  shareholder return of $93.81 on $100 over 2021-2025 against $158.66 for the company's own pay peer group (proxy, pay versus
  performance table), while equity was issued twice; the hand dealt included a long government rate that rose, which hurt
  every utility's price, but the peer group bore the same rate.
- **The tells of dishonesty, read in the filings:** none found. Item 3 carries operational litigation (main breaks, a
  chemical spill class action, Monterey), no restatement, no regulator finding against the reporting; the risk factors are
  full and specific, including against the merger the managers recommend; the featured adjusted EPS sits below GAAP in each
  year (Q4). The reports tell an owner "the things that we would want to know about if we owned a hundred percent of the
  company" **[M1998-036]**, with one exception recorded below (the pay version of EPS).
- **The habits carried from Q4.** The company states 7-9% EPS and dividend growth targets and has met them (reported
  adjusted EPS $4.77, $5.18, $5.64 for 2023-2025, growth of 8.6% and 8.9%). "we become downright incredulous if they
  consistently reach their declared targets" **[L2002-041]**. Read with the rest: in a regulated utility the earnings path is
  set in advance by orders on a known rate base, so meeting a growth target is what the rate-making produces, and the
  accounts show no tell of reserves or deferrals building (Q4). The pay version of adjusted EPS, however, is computed
  differently from the version reported to owners: for pay it keeps favorable weather (so $4.89 and $5.32 for 2023 and 2024
  against the reported $4.77 and $5.18), and it added back the 2021 $45M gift to the company's own charitable foundation
  (proxy, Appendix A, Parts A and B); and from December 2025 the committee removed the $0.02 floor on management's
  adjustments to the pay EPS (proxy). Recorded as a weighing on pay at Q6 Part B; it is not a misstatement (both figures are
  reconciled in public), and it does not raise doubt about honesty in the sense of "If you’ve got doubts, forget it." **[M2013-088]**.
- **Love of the business; after the cheque.** A hired management of a public utility; no seller's cheque to survive. The
  succession was internal twice, the board's job as the rows state it, "the next generation of leaders is identified and
  ready to take over tomorrow" **[L2011-001]**.
- **VERDICT on integrity: IN** ("If you’ve got doubts, forget it." **[M2013-088]**: doubts were sought in the 10-K, the
  proxy and the merger documents and none on honesty was found). **Ability WEIGHS FOR**, modestly: a regulated business run
  competently against its rivals on the yardstick of "what they’ve accomplished and what their competitors have
  accomplished" **[M1994-008]**, with owner returns poor over the five years.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test.** Over 2021-2025 the company retained $2,473M of earnings (retained earnings 102 to 2,575; 10-Ks)
  and raised $1,688M of new equity. The market leg, "at least $1 of market value for each $1 retained" **[R1995-009]**, fails:
  $100 invested at the end of 2020 was worth $93.81 with dividends at the end of 2025 (proxy, pay versus performance table).
  The 2009 rewrite asks also whether the stock "consistently sell at a premium to book" **[R2009-002]**: it did, at about 2.4x
  book at the price date ($141.10 against $11,665M of equity on 198.7M shares, $58.70). The forward question, "Can you keep
  using all of the capital you generate, effectively, for a very long time?" **[M2010-097]**: yes, more than all of it, at the
  allowed return (Q3). Mixed; the five-year market leg against.
- **Dividends while issuing.** Dividends of $428M to $633M a year (about 57% of 2025 net income), raised 7-9% a year, paid by a
  business that issues stock and borrows to fund its plan: owners are paid out and then sold new shares. The rows pay out
  when a company "expects to regularly earn more than it can profitably employ in its business" **[M2004-089]**, the reverse
  of this case. The policy is at least "clear, consistent" **[L2012-015]**. Weighs against, mildly.
- **Buybacks.** An "anti-dilutive stock repurchase program" authorized in 2015 "to mitigate the dilutive effect of shares
  issued" under the plans: 4,860,000 shares bought from April 2015 to 2025, none in 2025, no price named (10-K Item 5). The rows
  rule out exactly this motive, "It’s got nothing to do with preventing dilution." **[M2016-049]**, and the absence of a price,
  "almost never refer to a price above which repurchases will be eschewed" **[L2016-002]**. The prices paid were not read in
  this run (older 10-Ks). Against the bottom of the Q7 range: *written back at Q7, below.*
- **Issuance and deals.** Equity sold in 2023 ($1,688M for 12.7M shares) and by forwards at $139.657 a share (8.1M shares,
  3.4M settled in June 2026), plus plan issuance; the test is "We will issue common stock only when we receive as much in
  business value as we give" **[R1995-010]**: *written back at Q7.* Serial issuance is the framework's candidate second STOP
  (Q6, Issuance and deals; open in section VI), on "we have never invested in companies that are hell-bent on issuing shares"
  **[L2014-015]**; here issuance funds mandated plant on a regulator's equity ratio, roughly one large issue in three years,
  and is weighed, not taken as a STOP. Tuck-in acquisitions average $204M a year; the largest, Nexus, cost $319M for an
  estimated $200M of rate base (10-K Item 7; 10-Q), a premium the fair-market-value laws let the company seek in rates, and
  a price above the earning base whatever the rates allow. "Only if we receive less in value than we give. That’s the key to
  it." **[M1995-001]**.
- **The Essential merger (signed 2025-10-26, unclosed): an all-stock deal**, 0.305 AWK shares per Essential share, about 86.35M
  new AWK shares (283,117,816 Essential shares at 2026-02-19, its 10-K `0000078128-26-000050`), Essential holders to own about
  31% (joint proxy). The one STOP in Part A: "If shares of a prospective acquirer are selling below their intrinsic value, it's
  impossible for that buyer to make a sensible deal in an all-stock deal." **[L2009-019]**; *the STOP needs Q7's range and is
  written back at Q7.* The board's reasons count on efficiencies and first-year EPS accretion (joint proxy, board's reasons),
  where the rows "never count on synergies" **[L2016-008]**, judge "on a 10-year basis" **[M1999-061]**, and ask "are you
  getting more than you’re giving?" **[M2007-123]**; and the deal adds a gas distribution business the filer lists as a new
  risk. The buyer's owners are "concurrently selling part of their interest in everything they own" **[L2005-004]**.
### Part B: the pay, the board and the owners
- **Pay** (proxy DEF 14A, `0001193125-26-120668`). Chief executive $7,055,667 for 2025 (ratio to the median employee 73 to 1).
  Annual plan: 50% adjusted EPS, then customer satisfaction, safety, water quality, workforce measures (paid 141.5% of target).
  Long-term plan: 30% restricted units, 70% performance units (compounded EPS growth 35%, relative TSR 20%, ROE 15%); no
  options since 2017; clawback; hedging and pledging banned; ownership guidelines. For: no lottery-ticket options, an ROE
  measure that charges for capital in part. Against: the EPS paid on keeps favorable weather, which no manager controls, where
  the rows tie pay "to what is actually under the reasonable control of the person that’s being measured" **[M2003-019]**;
  the 2021 gift of $45M of company money to the company's foundation was added back for pay, where "the company's money is the
  owners' money" **[L1993-030]**; EPS growth is paid in a business whose EPS grows by putting in more capital, and "you get what
  you reward for" **[M2016-083]**; an outside compensation consultant advises the committee, which Berkshire avoids, "we do not
  bring in compensation consultants" **[M2004-016]**; the committee widened management's room to adjust the paid EPS from
  December 2025. The sums are not the sin the rows name, "any compensation sins are generally of minor importance compared to
  the sin of having somebody that’s mediocre running a huge company" **[M2007-006]**.
- **The board.** Independent chair separate from the chief executive (Q5); internal succession twice. Director share
  purchases with their own savings were not read in this run.
- **The owners.** Candid filings (Q5); growth targets stated, the "guidance" the rows call a scourge **[L2019-006]**.
- **WEIGHS AGAINST (Part A)**: a five-year retention record that failed the market leg, dividends paid out by a company that
  sells new stock, an anti-dilutive buyback with no price, and acquisitions above their earning base; the merger's STOP and the
  issuance test are written back at Q7. **WEIGHS AGAINST, mildly (Part B)**: pay largely on an adjusted EPS that keeps what the
  managers do not control.

## Q7 — WHAT IS IT WORTH? STOP.
"how much do you get back, how sure are you of getting it, when do you get it?" **[M2009-004]**, and "are you going to have to
put more cash into after you buy it?" **[M2014-068]**. Arithmetic in `value.py`, output `value_out.txt` (USD millions).
- **The basis.** The deciding part earns a return a regulator allows on its invested capital (Q2), so the central figure is
  the **equity-only** basis, the exception the row itself makes for "the fixed-asset commitments at our regulated utilities"
  **[L2017-012]** (framework, Q7, The regulated utility): owner cash after interest and after the company's own tax (21.9%
  effective, 2023-2025), against the market value of the shares, with the long-term debt raised for the plant credited against
  the growth spending. The all-equity figure is shown beside and never decides.
- **The cash input, equity-only, maintenance-only (specific (e)).** Owner cash = operating cash - stock pay - the maintenance
  guess (the depreciation charge, Q3, spent "simply to stay in the same economic place" **[L2000-035]**): 788 / 711 / 1,145 / 1,221 / 1,133 for 2021-2025, **average $999.6M**.
  The 2022 figure has the $280M of tax on the HOS and New York sale gains added back (literal 431), and the $472M and $608M of
  sale proceeds are left out of net acquisitions: **CONVENTION of this run**, rationale: the sales are one event whose cash and
  whose tax belong together, and neither is owner cash of the business that remains; the literal window is shown beside.
  Specific (a) asks for a full-cycle base where an end year is aberrational; a regulated utility shows no cycle, and the filer
  itself names 2021-2022's items, so the items are removed by name instead (said so).
- **Growth spending** (capital spending with removal costs, above the depreciation guess) averaged $1,933M, plus acquisitions
  of $204M (specific (c), deducted with the total growth credited; net purchases are about a fifth of owner cash before
  purchases, so not the serial-acquirer case): **$2,137M a year**. In the growth case it grows with the growth rate and stops
  after year ten: **$2,285M charged in year one, $4,180M in year ten, none after.**
- **Utility debt credit** (framework, Q7, The regulated utility, as amended 2026-10-23). Long-term debt with current
  maturities, preferred left out: $9,658M at 2020-12-31 (FY2021 10-K) to $14,256M at 2025-12-31: **$919.6M a year**; commercial
  paper and cash left out; no securitization bonds found. **Cap:** the 10-K states an allowed debt share with a rate base for
  six jurisdictions only (Illinois 51.00% on $2.2B, Missouri 50.00% on $3.2B as the company's view, Kentucky 47.74% on $667M,
  Iowa 47.43% on $262M, Tennessee 55.81% on about $300M, Virginia 54.33% on $369M as the company's view), $7.0B in all, which is
  less than half of the Regulated Businesses' rate base (the 10-K states no total; these six states carry well under half of
  segment revenue and net utility plant is $30.6B), so the cap is the business's **own long-term debt share of long-term
  capital at 2026-06-30: 55.4%** (14,489 / (14,489 + 3 + 11,665), 10-Q). 55.4% of $2,137M = $1,184M, above the $919.6M raised,
  so **the credit is $919.6M a year** ($983M in year one, $1,799M in year ten, stopping with the growth spending). (The
  rate-base-weighted stated shares, 50.5%, would cap at $1,079M: the same credit.)
- **The growth rate.** Shown growth of aggregate owner cash, 2021 to 2025 end years: **9.50% a year** (788 to 1,133). Specific
  (f): carried ten years it would need owner cash at 27.9% of sales against the highest share in the statements read, 27.0%
  (2023), so the growth carried is **the business's own sales growth, 6.94% a year** (operating revenues 3,930 to 5,140,
  2021-2025), below the discount rate; the shown rate's result is written beside. "what the farm produces is all you’re going
  to get from the farm" **[M1999-067]**.
- **The rate:** 5.30%, the long Treasury, "the yield on long-term U.S. bonds" **[L2000-021]**; after year ten, zero nominal
  growth.

**Value range (equity-only, central):**

| case | value | per share |
|---|---|---|
| no growth (owner cash $999.6M a year, flat) | $18,861M | **$94.91** |
| growth at 6.94% for ten years, growth spending charged net of the debt credit, then flat | $19,642M | **$98.84** |

Width 1.04 to 1. Beside, not deciding: shown growth 9.50% uncut, $126.70; the literal window (2022 tax left in), $89.59 to
$89.56; specific (c) taken literally (sale proceeds netted against purchases), $89.59 to $101.41; the seller note's interest
taken out of the window (it was repaid in February 2026), $91.05 to $92.12; the all-spending case with the debt credit and no
growth credited, **-$25.98**; the **all-equity basis** (owner cash before interest $1,358.9M, all growth spending charged, net
debt $15,800M at 2026-06-30: short-term 1,499 + long-term 14,489 + preferred 3 - cash 191; operating leases left out), **$49.51
(no growth) to $28.42 (growth)**. The signed, unclosed **Essential merger**, valued beside as if closed on Essential's own filed
record (owner cash after maintenance $430.6M a year 2021-2025, 10-Ks `0001562762-24-000047` and `0000078128-26-000050`; 86.35M
new shares): no-growth **$94.66** a share against $94.91 alone; the box is decided without it.

- **The floor, tested first.** At $141.10 (market value $28,041M) the expected return is **3.56%** on the no-growth case, **4.23%**
  on the growth case, **4.96%** even on the uncut 9.50%: no case clears about ten percent, "there’s just a point at which we drop
  out of the game" **[M2003-149]**, and the floor is applied to owner cash after the company's tax as Q7 (Whose tax) says,
  "discounting future after-tax streams of cash at at least a 10 percent rate" **[M1994-004]**. The price is also above the top of the range ($98.84), which closes OUT by the floor convention however wide
  the range. A wide-range TOO HARD does not arise.
- **Fair price (a reporting figure, never a verdict; Part VII): $39.41 a share** on the equity-only basis (central for a
  regulated utility): the no-growth case valued at ten percent is $50.30, the growth case $28.53 (at ten percent the growth
  bought is worth less than its cost, "growth can destroy value" **[L2000-023]**), averaged. On the all-equity basis beside, the
  two ends at ten percent are -$11.13 and -$61.56: **no positive fair price**. Tax: the company's own, no conversion. No cheap
  price is reported.
- **Specific (e) and the utility credit as run:** growth spending $2,285M in year one, $4,180M in year ten, none after; debt
  credit $919.6M a year in the base ($983M year one, $1,799M year ten), cap 55.4% (own long-term debt share of long-term capital,
  2026-06-30, since stated allowed shares cover under half of the deciding part's rate base).
- **VERDICT: OUT.** The value range is **$94.91 to $98.84 a share against $141.10**; no case earns the floor at the price,
  "we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**, and the speakers' own utility rows say why the price, not the business, decides: "there’s no way we get rich on
  our utility investments" **[M2009-104]**.

### Written back to Q6, with the range (committed with Q7)
- **Buyback line.** The anti-dilutive buyback names no price; the prices paid from 2015 to 2024 were not read, so they cannot be
  shown to sit at or below the bottom of the range ($94.91); by Q6's convention the programme **weighs against**.
- **Issuance line.** Stock was sold at about $133 (2023) and $139.66 (forwards), above the top of the range ($98.84): on this
  run's range the company issued "only when we receive as much in business value as we give" **[R1995-010]**, which weighs **for** continuing owners on that
  line.
- **The merger STOP.** AWK at $141.10 sits above its range, so its stock is not "selling below their intrinsic value" in the
  sense of **[L2009-019]**: **the STOP is not triggered.** Value given against value got, on the same method: 86.35M shares x
  $94.91 = $8,195M given, against Essential's own no-growth value on the same basis of $8,125M; about even at intrinsic value, and
  at the price $12,184M of AWK stock for it.
- Part A stays **WEIGHS AGAINST** (retention market leg, dividends while issuing, the unpriced buyback, acquisitions above their
  base), with the issuance line for.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (Q7 closed OUT); facts below under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT, at Q7** (the floor, tested first): value range **$94.91 to $98.84 a share** (equity-only, the regulated utility's central
basis) against **$141.10**; no case earns about ten percent at the price (3.6% to 5.0%). Q1 IN, Q2 IN (a regulated franchise
with ordinary, regulator-set returns), Q3 weighs against narrowly, Q4 accounts clean (weighs against mildly), Q5 integrity IN,
Q6 weighs against (the merger's STOP not triggered: the stock is above its range). Fair price (reporting figure) $39.41
equity-only; no positive fair price on the all-equity basis. Not TOO HARD: the cash can be estimated and the range is narrow.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Q7 closed the file; written down, not weighed; the box unchanged, operator rule 2.)* Each written down as found, "write it down in the first 30 minutes" **[M1997-127]**.
- **Q8, the alternatives.** The long Treasury yields 5.30% (2026-10-27); the expected return at the price computed above is
  3.56% to 4.96% (`value_out.txt`).
- **Q9, the target's debt and exposures.** Total debt $15,847M at 2025-12-31 (short-term $1,588M, current maturities $1,479M,
  long-term $12,780M with preferred; 10-K) and $15,991M at 2026-06-30 (10-Q); "our working capital [...] was in a deficit
  position" (10-K Item 1A); debt-to-capitalization 0.59 under a 0.70 covenant (10-K, Debt Covenants). Coverage on the rows'
  definition, "pre-tax earnings/interest, not EBITDA/interest" **[L2012-002]**: (1,422 + 615) / 615 = 3.3x for 2025. Parent company depends on
  subsidiary dividends and guarantees MSG's performance (10-K Item 1A). Fourteen regulated states, none above a quarter of
  revenue (10-K Item 1). A termination fee of $835M payable by AWK to Essential in certain circumstances (10-K Item 1A). The 3.625%
  exchangeable notes ($1,035M) matured and were repaid in cash on 2026-06-15 (10-Q). Liabilities the filer names: dams, main
  failures, contamination (PFAS under CERCLA), cyber, no-fault property claims against utilities in California (10-K Items 1,
  1A). The acquisition criterion "little or no debt" **[R1997-001]** is stated for whole businesses.
- **Q10.** Nothing found beyond the price.
- **Q12.** A water and wastewater utility; none of the named businesses. Nothing found that would fail the newspaper test in the
  filings read.
- No integrity facts beyond those answered at Q5.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `cc8b1ffe`); written question by question; committed after each
      question with a pathspec of the two paths (Step 0 to Q1, Q2, Q3, Q4, Q5, Q6, Q7 with the Q6 write-back, close).
- [x] Dispatched analyst: the brief allowed the per-question commits; the lock is the dispatching session's; the run binds
      only once folded into the register by the dispatcher (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under Contamination at the top and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_cites.py` in the research folder (ids exist, every
      quoted fragment beside an id is in that row, no E-ids); every filing fact carries its accession or names its filing.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q12 are not reached and nothing after Q7 is
      a clearance.
- [x] Owner cash from operating cash less stock pay less capital spending (maintenance guess central, all spending beside),
      never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP.
- [x] Not a point-in-time run; no row dated after an anchor arises.
- [x] Only the arithmetic lines of `tools/run.py` were used, and two of them were corrected against the filing (removal costs
      left out of capex; the "d3" column is capitalization, not debt).
- [ ] **One departure, confessed:** the Q7 arithmetic (`value.py`) was first run in the research folder while Q1 to Q4 were
      still open, as preparation; its output file was headed COMPUTATION, NOT A CLEARANCE (operator rule 3) from the Q2 commit
      on, carried no entry language, and was written into the run only at Q7. The Q1 commit contains that output without the
      heading.
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the closing commit's message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Divestitures inside the window.** Specific (c) nets "businesses sold" against purchases, and specific (a) asks for a
full-cycle base when an end year is aberrational; neither fits a non-cyclical utility whose 2021 and 2022 carry the sale of a
business (proceeds of $1,080M in investing cash, $280M of tax on the gains inside 2022 operating cash, the sold operations'
cash inside 2021). Taken literally, (c) credits the proceeds as negative purchases while the tax stays in operating cash. I
removed both sides as one event (a CONVENTION of this run) and showed the literal readings beside; the box does not turn on it.
(2) **The utility cap's "less than half of the deciding part's rate base"** needs a total rate base the 10-K does not state; I
judged it from revenue shares and net plant, and the credit was below either cap, so it did not decide here, but a closer case
would need a rule for where the total comes from. (3) **Cap (f)'s "highest share of sales the business has earned in the
filings read"** depends on how many years were read: the statements read (2019-2025) give 27.0% and trigger the cut, while the
XBRL ten-year series shows 28.2% in 2017, which would not; the rule should fix the span (I used the statements read). (4) **Q6's
merger STOP needs Q7's range** and Q6 comes first; the framework says so for buybacks but not for the all-stock STOP, nor whether
it applies to a signed deal not yet closed (I wrote it back at Q7 and applied it to the signed deal). (5) **Q3 for a regulated
utility**: Q2 carries regulator-set returns to Q3 as a second best, but Q3 gives no measure of "decent" for the added capital;
on equity the added capital earned about 9%, on all capital after tax about the long government rate, which read opposite ways.
I followed "It’s measured by the operating earnings after depreciation." **[M2014-086]**. (6) **The maintenance guess for a utility**: replaced pipe
enters the rate base and earns, so depreciation as maintenance ("amounts equal to our depreciation charge" **[L2000-035]**) charges to the equity alone spending that the
regulator finances at about half debt; the debt credit reaches only the growth spending by the 2026-10-23 amendment, which is
conservative here and is how I ran it.
