# Company Run: MDU Resources Group, Inc. (NYSE: MDU), 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch (commit c7ad2740). Dispatched blind run under
the canonical brief `Screens/_daily/_dispatch_brief.md`, with the one departure the brief states (the lines of evidence and
the competitors derived by the analyst from the filing). Working folder: `Test Runs/_research 2026-10-18 MDU/` (notes,
`compute.py` and `peers.py` for every sum below, `row.py` and `check_run.py`; raw filings in its ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (da309836): `PORTFOLIO.md` read for this one ticker; the operator does not hold MDU (no line names MDU, MDU Resources, Montana-Dakota, Knife River or Everus).*

**Contamination, declared.** Seen by accident and not used: the directory listing of `Test Runs/` made to confirm that this
run's paths were free showed two other run files dated today (HOKCY, XNGSY) and their research folders; the session's opening
git status listed recent commit subjects for the HOKCY run, including its question-by-question verdicts, and untracked files
in two other companies' research folders (AYI, ARCB); the memory index loaded with the session carries one line on the
queue's state (counts of gate-clearers, a paused wave and its next name). None of it concerns MDU, Knife River or Everus, and
none of it was read further or used. No other run file, holding review, `PORTFOLIO.md` or blind-listed file was opened,
listed or searched.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $19.00 (close 2026-10-16, printed by `python tools/run.py MDU`; an aggregator quote, live quote only, flagged
  per operator rule 5).
- **Shares by class:** one class, common stock, $1.00 par: 210,349,456 shares outstanding at 2026-07-30 (cover of the 10-Q
  for the quarter to 2026-06-30, filed 2026-08-06, accession `0000067716-26-000072`; `python Screens/cover_shares.py MDU`
  prints the same). Checked: the 10-Q balance sheet shows 210,349,456 shares issued at 2026-06-30 and no treasury stock, so
  issued less treasury equals the cover count. No 8-K or prospectus has been filed since the 10-Q (EDGAR submissions list,
  read 2026-10-18). **Beside the count, not in it:** forward sale agreements from the December 2025 offering could still
  be settled by delivery of about 7.4 million shares for about $139.6 million (10-Q, Note on equity), on or before
  2027-12-06.
- **Market cap:** 210.349 million x $19.00 = **$3,996.6M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, the 30-year par yield on the US Treasury daily par yield curve,
  2026-10-16 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-20, `0000067716-26-000014` (Items 1, 1A, 7, 7A, 8 with
  Notes 6, 9, 11, 14 and 17); 10-Q for the quarter to 2026-06-30, filed 2026-08-06, `0000067716-26-000072`; proxy statement
  (DEF 14A) filed 2026-04-01, `0000067716-26-000040`; 8-K earnings releases of 2025-02-06 (`0000067716-25-000007`),
  2025-11-06 (`0000067716-25-000087`), 2026-02-05 (`0000067716-26-000008`) and 2026-08-06 (`0000067716-26-000064`);
  8-K of 2026-01-16 on the WBI private shelf (`0000067716-26-000005`); for the window and the cycle, the 10-Ks for FY2024
  (`0000067716-25-000016`), FY2023 (`0000067716-24-000017`), FY2022 (`0000067716-23-000017`) and FY2019
  (`0000067716-20-000010`); and Everus Construction Group's Form 10/A of 2024-10-09, Exhibit 99.1
  (`0001628280-24-042608`), for the construction-services cash flows of 2021 (see the window, below). **One figure
  cross-checked against the filed statement:** `tools/run.py` prints FY2025 operating cash flow of 473.4 and equity of
  2,773 ($M); the filed statements show 473,365 and 2,772,917 ($ thousands). They agree.
- **`python tools/run.py MDU`, arithmetic lines only.** Its three as-filed years (2023 to 2025) mix discontinued operations
  into operating cash: owner earnings after all capital spending -157.0, -28.9, -303.6 (mean -163.2); after depreciation
  136.7, 293.8, 260.1 (mean 230.2). It found no securities, other stock pay, intangible, software or other spending line
  beside capital spending. Its yield and growth lines are not used (Part VII). The window this run uses is built below.
- **How the window was built.** MDU separated Knife River on 2023-05-31 and Everus on 2024-10-31; each later 10-K restates
  earlier years with the separated business in discontinued operations. The window is FY2021 to FY2025, **continuing
  operations only** (the electric, natural gas distribution and pipeline segments and Other): FY2023 to FY2025 from the
  FY2025 10-K's cash flow statement, FY2022 from the FY2024 10-K's, both as restated for both separations. No filing
  restates FY2021 for both. **CONVENTION of this run:** FY2021 is built as the FY2023 10-K's continuing operations (which
  still contained Everus) less Everus's own FY2021 figures in its Form 10 (operating cash 85.4, capital spending 27.3,
  depreciation 20.3, stock pay 1.7, $M). Rationale: it is the only filed route to a utility-only 2021. Tested on FY2022, the
  same subtraction gives capital spending, depreciation and stock pay equal to the restated figures to the decimal and
  operating cash of 333.1 against the restated 321.6 (3.6% high, because some corporate overhead moved to Other on
  restatement); FY2021 operating cash may be high by a similar amount.

| $M, continuing operations | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|
| Operating cash flow | 213.5 | 321.6 | 305.3 | 411.8 | 474.1 | |
| Stock-based pay | 11.1 | 7.9 | 5.5 | 8.4 | 6.6 | |
| Capital spending | 457.9 | 442.6 | 484.1 | 522.8 | 770.4 | |
| Cost of removal, net of salvage (investing) | -11.4 | -11.8 | +1.2 | -5.5 | -11.3 | |
| Depreciation and amortization | 178.0 | 188.6 | 190.4 | 200.1 | 206.7 | |
| Interest expense | 70.8 | 80.7 | 104.6 | 108.3 | 107.7 | |
| **Owner cash after all spending** (OCF - stock pay - capex + removal) | -266.9 | -140.7 | -183.1 | -125.0 | -314.1 | **-206.0** |
| Owner cash after depreciation (OCF - stock pay - D&A) | 24.4 | 125.1 | 109.4 | 203.3 | 260.8 | **144.6** |
| Same, before interest (all-equity basis) | 80.3 | 188.9 | 192.0 | 288.9 | 345.9 | **219.2** |

Owner cash is never a net-income proxy here (operator rule 5): every line is the filed cash flow statement's. Interest is
added back at 21% (**CONVENTION of this run:** the federal statutory rate the filer's tax note reconciles from; the
company's own effective rate, about 9% in 2025, is held down by production tax credits that do not shelter interest). The
2025 capital spending includes the final $264.6M paid for a 49% interest in Badger Wind Farm, acquired and placed in service
on 2025-12-31 (10-K, Item 7, Capital expenditures, note (d)), an asset purchase paid in cash and reported as capital
spending. Stock pay is resolved: it is the only stock-pay line the cash flow statements carry, and the proxy grants no
options.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, and "Would I be happy buying this stock if the
market closed for five years?" **[M1997-109]**. For this name the market-closed question sends the analyst to the regulated
rate base and what it earns, not to the dividend or the quote. The second bears too: the price "doesn’t tell us anything. It
just tells us prices." **[M2006-077]**, so the run sets the price against the cash and nothing else. No view on rates or gas
prices is taken: "macro conclusions are — just never enter into the discussion." **[M2000-094]**. Who is paid to tell: the company issues earnings guidance and
a long-term earnings growth objective, and sells shares to fund its plan; both are read as the seller's projection, not as
evidence. **Contrary evidence, written down as found [M1997-127]:** (1) the deciding segment, natural gas distribution,
earned 1.4% on its segment assets in 2025 and 1.5% in 2017 (Q2 parts table); (2) Intermountain Gas, a subsidiary, breached
its minimum interest coverage covenant for the period to 2025-09-30, cross-defaulting notes at MDU Energy Capital and the
revolving credit agreements until waivers were obtained (10-K, Item 7, Debt resources); (3) owner cash after all capital
spending was negative in every year of the window (table above); (4) Washington, 35% of gas retail revenue in 2025, adopted
building code amendments that "will significantly limit the use of natural gas for space and water heating" in new and
retrofitted buildings, with the company's challenge dismissed at district court and pending on appeal (10-K, Item 7,
Legislation and rulemaking); (5) the February 2025 guidance assumed "No equity issuances", and the company sold 11.7 million
shares forward in December 2025 and began an at-the-market programme (8-K 2025-02-06; 10-K Note 11); (6) a pipeline
project of $2.7 billion to $3.2 billion is in development against a market value of $4.0 billion (8-K 2026-08-06).

## THE STANDING RULE
The buyer's conduct: a purchase of this name would be for cash, held without margin, in a size that a fall of half would
not force a sale, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**; borrowed
money "can prevent you from playing out your hand" **[M2004-065]**. Nothing in owning a regulated utility's common stock puts
the buyer at risk of ruin if it is so bought. The target's own debt is Q9's. **No breach.**

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**. MDU is three regulated monopolies (10-K, Item 1): Montana-Dakota's electric utility
  in North Dakota, Montana, South Dakota and Wyoming (146,550 retail customers; rate base $1.8B); natural gas distribution
  through Montana-Dakota, Cascade and Intermountain in eight states (1,082,329 customers; rate base $2.2B); and WBI Energy
  Transmission, a FERC-regulated interstate pipeline and storage system of 3,800 miles (net plant $1.0B). Its earnings are
  the return the commissions allow on the rate base, less what it fails to earn through lag, plus pipeline contracts.
- **The key variables and whether they are foreseeable** ("trying to identify the key variables [...] and evaluating how
  predictable they were first" **[M1998-044]**): (1) rate base growth, set by the company's own capital plan ($3.1B for
  2026-2030, 8-K 2026-02-05) and commission approval; (2) the allowed return, 9.5% to 9.7% on equity in the cases finalized
  or settled in 2025 and 2026 (10-K Note 6); (3) how much of the allowed return is earned, which the filings show year by
  year; (4) customer growth, 1.5% in 2025 (10-K, Item 7, Outlook); (5) state policy on gas, chiefly Washington and Oregon.
  The first four are knowable from filings and rate orders. The fifth is a forecast of politics and courts, but it moves
  the slope of growth and the risk of stranded cost, not the existence of the franchise; the 10-K reports Washington and
  Oregon carbon compliance costs as "being recovered through customer rates" (Item 7, Legislation and rulemaking). "If
  something’s important but unknowable, forget it." **[M2006-076]**: the policy variable is important and only partly knowable; it is carried to Q2 as the castle's main
  threat, where the framework sends change ("Rapid change is owned by Q2").
- **Would the insiders write it down?** The tech insiders of the row "would not want to put down on paper their
  predictions" **[M2000-105]**; these do. The company publishes a five-year capital plan, a rate base
  history (8.7% compound growth over five years for the utility segments, 10-K Item 7) and an earnings objective; the
  commissions publish allowed returns. Utility insiders do write the ten-year economics down; that is the regulatory compact.
- **Do the past statements tell the future ones?** The row asks whether "the financial statements will tell me the
  information that’s useful to me in making a judgment about what the future financial statements are going to look like"
  **[M2008-033]**: for the utilities, largely yes; the segment notes
  for 2017 to 2025 show the same three businesses earning a narrow band of returns (Q2). For the pipeline, less so: WBI's
  earnings rose from $20.6M in 2017 to $68.2M in 2025 on Bakken-driven expansions, and the proposed Bakken East project
  ($2.7B to $3.2B, 1.4 Bcf a day design, final investment decision not yet taken; 8-K 2026-08-06) could make the pipeline
  the largest part. A project that is not decided is weighed at Q6 and Q9, not assumed.
- **Do I doubt it is inside?** "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**: there is no doubt for the business as it stands. A regulated utility with no derivatives
  book, whose two sides can be read from the filings, is inside the perimeter; the doubts are about returns and price,
  which are later questions.
- **Routing.** No fast-changing technology closes this at Q1. Electrification and gas restrictions are slow change in a
  part of the territory; Q2 owns it.
- **VERDICT: IN.** The ten-year economics of a rate-regulated delivery business can be pictured from its rate base, allowed
  returns and earned returns, all in the filings **[M2012-065]**, **[M1998-044]**. Filing fact: three reportable segments, all
  regulated by state commissions or FERC (10-K Item 1, `0000067716-26-000014`).

---
## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The question:** "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. Parts with different economics are read separately, since "lumping them
together, as is done in standard financial statements, impedes analysis" **[L2008-005]**.

**The parts table** (segment operating income, $M, from the segment notes and MD&A of the 10-Ks for FY2022, FY2023 and
FY2025; the framework's CONVENTION for a business of parts: a part decides at more than half of five-year operating
profit, else the largest decides):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year total | Share | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Natural gas distribution (Montana-Dakota, Cascade, Intermountain; 8 states) | 89.2 | 91.9 | 92.2 | 92.6 | 109.5 | 475.4 | 37.8% | franchised local monopoly, regulated return; narrowing slowly in Washington and Oregon | **yes (largest)** |
| Electric (Montana-Dakota; ND, MT, SD, WY) | 66.3 | 79.7 | 92.8 | 94.2 | 79.6 | 412.6 | 32.8% | franchised local monopoly, regulated return | no |
| Pipeline (WBI Energy Transmission, FERC) | 48.1 | 55.5 | 69.2 | 94.5 | 101.1 | 368.4 | 29.3% | location near four basins, storage, contracts; competes with other pipelines | no |

No part carries more than half; natural gas distribution is the largest and decides. The file closes on its castle.

**The castle tests, with the filing fact for each (deciding part first):**
- **The attacker with money.** A second gas distribution network in a franchised town is neither permitted nor sensible;
  the case is the railroad, "You really couldn’t create another railroad" **[M2013-054]**. The 10-K: the operations "have
  obtained and hold, or are in the process of renewing, valid and existing franchises" in every municipality that requires
  one (Item 1). Bypass exists at the edges ("certain customers have bypassed the distribution systems by directly accessing
  transmission pipelines", without material effect). **Stands.**
- **Pricing power and the agony before a rise.** The business has none of its own: the commission sets the price, and every
  rise is a filed case, the "prayer session before you raise your prices a penny" **[M2005-020]** made formal. Gas cost
  passes through; such utilities "are pass-through organizations" **[M2012-013]**. Cases decided in 2025 and early 2026:
  Washington +7.9% then +2.6% at 9.5% ROE, less a $3.7M reduction for forecast plant not placed in service; Idaho +4.2% at
  9.5%; Montana +8.6% at 9.6%; Wyoming +11.7% at 9.65%; Oregon filed +15.8% at 10.4% and settled at $12.2M against $16.4M
  asked (10-K Note 6; 8-K 2026-08-06). The rows' own reading: "The whole idea behind the utility industry is not to allow
  extraordinary profits." **[M2000-131]**.
- **Unit volume and share of mind.** Gas customers 1,049,275 (2023), 1,065,593 (2024), 1,082,329 (2025); retail volumes
  122.6, 119.5, 120.2 MMdk; "the average customer consumption has tended to decline as more efficient appliances and
  furnaces are installed" (10-K Item 1). Customers grow about 1.5% a year; use per customer falls. Decoupling in Washington
  and Oregon pays an average revenue per customer regardless of use.
- **Would the customer still choose it over the low bid?** There is no low bid for the pipe to the house; the alternative
  is another fuel. The 10-K names that competition: "between natural gas and other fuels and forms of energy".
- **Ask the competitors.** The 10-K names no rival that files with the SEC (it names rural electric cooperatives,
  municipal systems, on-site generators and "several pipelines", none by name; Black Hills Power appears only as a supplier
  under a power contract). **CONVENTION of this run:** the comparators are three companies from the proxy's own 2025
  compensation and rTSR peer groups whose service territories overlap MDU's: Black Hills Corp. (BKH; electric and gas in
  Wyoming, South Dakota, Montana and other states), NorthWestern Energy (NWE; electric and gas in Montana and South Dakota)
  and Avista Corp. (AVA; electric and gas in Washington, Idaho and Oregon). Rationale: the company chose them as its
  yardstick, and the overlap means many of the same commissions set their returns.
- **Widening or narrowing.** The test is "how wide the moat is and whether it’s likely to widen further or shrink on you"
  **[M1999-108]**. Narrowing, slowly, in the two states that carry 43% of gas retail revenue (Washington 35%, Oregon 8%,
  2025). Washington's Climate Commitment Act (cap and invest, effective 2023) and Oregon's Climate Protection Program
  require the gas utilities to cut emissions; Washington's building code amendments of 2023 "will significantly limit the
  use of natural gas for space and water heating in new and retrofitted commercial and residential buildings"; the
  company's federal challenge was dismissed and is on appeal (Ninth Circuit argued 2026-02-10); Initiative 2066, approved
  by voters to bar the code from discouraging gas, was ruled unconstitutional by the King County Superior Court in May 2025
  and is before the Washington Supreme Court (10-K, Item 7). The risk factor: decarbonization policies "could slow or
  reduce future customer additions", and codes may "discourage new natural gas hookups, potentially impacting the
  Company's long-term growth assumptions" (Item 1A). In the other six states (57% of gas retail revenue) no such rule is
  reported. And "slow change can be much harder to perceive, and can lull you to sleep easier" **[M2014-038]**.
- **What could destroy, modify or reduce it, five to fifteen years out.** The row asks what "will destroy, or modify, or
  reduce the economic strengths" **[M2000-014]**. The newspaper test, "if cable and satellite broadcasting, as well as the
  internet, had come along first, newspapers as we know them probably would never have existed" **[L2006-008]**: in
  Washington, a gas network for new buildings would by statute hardly be built today. Against destruction: the existing
  network serves existing buildings, the code reaches new and retrofitted ones, and where "societal demands are just
  changing" the commissions are less inclined to refuse stranded cost than where assets were stranded "because of rank
  foolishness" **[M2017-094]**. The regulatory hazard itself is a narrated mistake: "I did not anticipate or even consider
  the adverse developments in regulatory returns" **[L2023-011]**, and "values change and they don’t always change upward"
  **[M2025-045]**. The other parts: electric demand is rising with data centers (a 180 MW Applied Digital load since 2023;
  an approved agreement for 350 MW more and a 430 MW agreement pending approval; 10-K Item 7 and 8-K 2026-08-06), and the
  pipeline sits near four producing basins with Bakken gas production "at or near record levels" (10-K Item 7, Pipeline
  Outlook); WBI's firm contracts with its affiliate Montana-Dakota, 19% of subscribed firm demand, mostly expire in June
  2027, and one third-party customer gave 17% of 2025 segment revenue (Item 1).

**The competitor row** (net income over average equity and over average total assets, FY2017 to FY2025, from each filer's
10-K XBRL facts, earliest-filed values; `peers.py`; accessions of the latest year: BKH `0001193125-26-046028`, AVA
`0001193125-26-067872`, NWE `0001993004-26-000006`, earlier NWE years under CIK 73088):

| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | mean |
|---|---|---|---|---|---|---|---|---|---|---|
| BKH return on equity | 10.7% | 13.3% | 8.8% | 9.2% | 8.9% | 8.9% | 8.4% | 8.1% | 8.0% | 9.4% |
| NWE return on equity | 9.4% | 10.5% | 10.2% | 7.5% | 8.5% | 7.3% | 7.1% | 7.9% | 6.3% | 8.3% |
| AVA return on equity | 6.9% | 7.8% | 10.6% | 6.5% | 7.0% | 6.9% | 7.1% | 7.1% | 7.3% | 7.5% |
| BKH return on assets | 2.69% | 3.79% | 2.74% | 2.91% | 2.75% | 2.76% | 2.73% | 2.78% | 2.79% | 2.88% |
| NWE return on assets | 2.98% | 3.56% | 3.50% | 2.52% | 2.84% | 2.60% | 2.60% | 2.87% | 2.20% | 2.85% |
| AVA return on assets | 2.14% | 2.42% | 3.32% | 2.07% | 2.22% | 2.17% | 2.26% | 2.30% | 2.37% | 2.36% |
| MDU three utility segments, segment net income over average segment assets | | 2.52% | 2.57% | 2.72% | 2.68% | 2.37% | 2.67% | 2.83% | 2.64% | 2.62% (2018-25) |

MDU's equity before 2024 held the construction businesses, so its consolidated return on equity is comparable only in
FY2025: 191.4 over average equity of 2,731.7, **7.0%** (10-K FY2025). The deciding part, natural gas distribution, earned
segment net income of $32.2M on segment assets of $2,201M in 2017 (1.46%) and $56.1M on $3,909M in 2025 (1.43%), the lowest
of the three parts and below every comparator's company-wide figure; the gas segment's assets carry the company's whole
goodwill of $345.7M (10-K, Critical accounting estimates), which earns nothing in rates. The segment-asset basis includes
allocated common property and is not identical to the comparators' total assets; the comparison is of kind, not of decimals.

**The field's returns over the last full cycle, judged in words.** The span 2017 to 2025 holds a pandemic year, the gas
price spike of 2021 to 2022 and the inflation of 2021 to 2023. Across it the four companies earned what regulated utilities
earn: ordinary returns, steady in a band, never high, which is the bargain the rows describe, "in utilities the trade has
been the compact has been that you get a modest return" **[M2024-011]**. The framework's rule: a standing castle that
protects only ordinary returns closes OUT, except that a return set by a regulator is carried to Q3 as a second best (Q2,
What it rules OUT), on "there’s no way we get rich on our utility investments. But there’s no way we get poor, either."
**[M2009-104]**. These returns are set by commissions, so the exception applies, and the earned shortfall at the gas part is
carried to Q3.

**A castle shown open?** No. **A future that cannot be judged?** The Washington and Oregon policy is the hardest question in
the file. It is judged here as slow narrowing of growth in 43% of the deciding part, not as a castle whose future cannot be
pictured: the network, the franchises and the cost recovery stand, and the threat is to additions and to the size of future
rate base in two states. A stricter reader could send the gas part to TOO HARD (NATURE) on the policy forecast; that reading
is recorded under the framework gaps, and on this file it would not change the outcome, since no case clears the floor at
the price (Q7, computed either way).

- **VERDICT: IN**, on the deciding part's franchised monopoly **[M2013-054]**, **[M1995-038]**, with its regulator-set,
  ordinary return carried to Q3 as a second best **[M2009-104]**, and the narrowing in Washington and Oregon carried
  forward as the strongest threat **[M2014-038]**, **[M1999-108]**. Filing facts: franchises held (10-K Item 1); allowed
  returns 9.5% to 9.65% in the gas cases decided in 2025 (Note 6); gas segment return on assets 1.46% (2017) and 1.43% (2025).

---
## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What it earns on the capital it needs.** The measure is the capital "actually needed in the business" **[M2010-090]**.
  FY2025: income from continuing operations 191.4 plus after-tax interest (107.7 x 0.79 = 85.1) is 276.5 on capital
  employed of 5,422 (equity 2,772.9 plus borrowings 2,676.9 less cash 28.2, at 2025-12-31) = **5.1%** before financing.
  The common equity earned **7.0%** (Q2). The commissions allowed 9.5% to 9.7% on equity in the cases decided in 2025 and
  2026 (10-K Note 6), so the company earns about two-thirds of what it is allowed; the gap is largest at natural gas
  distribution (segment return on assets 1.43% in 2025, Q2), where the $345.7M of purchased goodwill sits outside rate
  base, and where Intermountain failed its interest coverage covenant in 2025 (10-K, Item 7, Debt resources).
- **Reinvestment to stand still and to grow.** Capital spending ran 2.6, 2.3, 2.5, 2.6 and 3.7 times depreciation in 2021
  to 2025 (Step 0 table; 3.7 includes the $264.6M Badger Wind purchase). The plan is $3.1B for 2026 to 2030 (8-K
  2026-02-05), about $620M a year against depreciation running near $220M (10-Q: $109.4M in the first half of 2026), and the
  Bakken East project of $2.7B to $3.2B is not in it. Part of the spending is compulsory: the 10-K names pipeline "safety
  and integrity replacement projects driven by PHMSA regulations", "system replacements" and a MISO capacity need "by May
  of 2028" (Item 1; Item 7). The rows: "To earn more, their owners must invest more." **[L2011-019]**; "you have to keep
  putting more and more money into a public utility. And you’d better hope that the rate of return allowed is commensurate"
  **[M2005-052]**; and they "have tried to avoid places where there was a lot of compulsory reinvestment just in order to
  stand still" **[M1997-016]**.
- **What the added capital earns.** Owner cash after depreciation, before interest and before working-capital swings, rose
  from 210.3 (2022) to 268.2 (2025), an increase of 57.8, against spending above depreciation of 886.6 in 2022 to 2024
  (`compute.py`): about **6.5%** a year in cash on the growth capital, before the inflation of operating costs that rate
  relief also had to cover. That is above the long government rate (5.43%) and well below the floor of about ten percent
  that Q7 applies. "whether that’s good or bad depends on what we earn on that incremental $130 million over time"
  **[M2001-019]**; "we’re not earning a higher rate of return on capital than we were when we started. We just put way
  more capital into the business" **[M2023-081]**. The rows measure the utility's return on "the operating earnings after
  depreciation", and like it only "as long as we are going to get returns on the added capital investment" **[M2014-086]**.
- **The growth arithmetic and its cap.** The growth is bought, not earned: owner cash after all spending was negative in
  every year (mean -206.0, Step 0), and the gap was filled with debt and, from 2025, new shares (Q6). The three grades of
  the 1998 answer: the second best "takes more money, but the rate at which you invest — reinvest — the money to get that
  growth is a very satisfactory rate"; the worst is "forced to grow to stay in the game at all" at "a very low rate of
  return" **[M1998-081]**. This business sits between them: a regulated return near the long rate on each added dollar,
  part of it compulsory.
- **WEIGHS AGAINST.** A capital-heavy business is a second best only on "reasonable expectations of earning decent
  returns on the incremental sums they invest" **[L2009-012]**, and "cash-consuming businesses, by their nature, are
  unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**; this one earns about 5% on
  its capital, 7.0% on its equity against 9.5% allowed, and about 6.5% in cash on its added capital, with spending set to
  rise. (The "little or no debt" criterion is applied at Q9.)

---
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, before the income account** **[M2025-032]** ($M; `tools/run.py` first-filed
XBRL table, read against the filed balance sheets of the 10-Ks named in Step 0 and the 10-Q):

| year-end | assets | equity | cash | receivables | inventory | goodwill | long-term debt (non-current) | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 6,284 | 2,316 | 46 | 630 | 238 | 632 | 1,747 | 912 |
| 2017 | 6,335 | 2,429 | 35 | 727 | 227 | 632 | 1,566 | 1,041 |
| 2018 | 6,988 | 2,567 | 54 | 723 | 287 | 665 | 1,857 | 1,164 |
| 2019 | 7,683 | 2,847 | 66 | 837 | 278 | 681 | 2,227 | 1,337 |
| 2020 | 8,053 | 3,079 | 60 | 874 | 291 | 715 | 2,212 | 1,558 |
| 2021 | 8,910 | 3,383 | 54 | 947 | 336 | 765 | 2,594 | 1,762 |
| 2022 | 9,661 | 3,587 | 81 | 1,306 | 388 | 764 | 2,763 | 1,951 |
| 2023 | 7,833 | 2,905 | 77 | 943 | 87 | 489 | 2,237 | 1,254 |
| 2024 | 7,039 | 2,691 | 67 | 274 | 45 | 346 | 2,131 | 1,030 |
| 2025 | 7,622 | 2,773 | 28 | 259 | 39 | 346 | 2,532 | 1,109 |
| 2026-06-30 (10-Q) | 7,712 | 2,927 | 46 | 152 | 19 | 346 | 2,572 | 1,152 |

**What moved and why.** (1) The years to 2022 include the two construction businesses, as first filed; the breaks at 2023
and 2024 are the separations, not losses: retained earnings fell by $970.1M at the Knife River distribution and by $400.3M at
the Everus distribution (statements of equity, 10-K FY2025), and with them went most of the receivables (1,306 to 259),
the inventory (388 to 39) and the goodwill (764 to 346). (2) What is left is the utility balance sheet: goodwill of $345.7M,
all at natural gas distribution, about an eighth of equity; net plant of $5,960M at 2025-12-31 against $5,344M a year
before. (3) Debt: borrowings were 2,293 at 2024-12-31 (2,131 plus 162 current), 2,677 at 2025-12-31 (2,532 plus 145) and
2,577 at 2026-06-30 (2,572 plus 5), with cash of 28 to 67; debt is about 49% of debt plus equity at 2025-12-31. Equity rose
by $81.2M (4.3 million forward shares, March 2026) and $29.6M (1.3 million at-the-market shares, second quarter) in 2026
(10-Q statement of equity). (4) Regulatory assets fell from 537.8 to 476.8 in 2025 while regulatory liabilities rose to 620.9;
$174.3M of regulatory assets earn no return (10-K Note 6). (5) Environmental allowances and the matching obligations under
the Washington and Oregon programmes are growing (non-current allowances 66.2 at 2024-12-31, 112.4 at 2025-12-31, 162.2 at
2026-06-30; non-current obligations 58.5, 108.4, 153.7), a pass-through that ties up cash between purchase and recovery (10-K
Item 7: "the purchase of allowances could impact the Company's operating cash flow"). (6) Asset retirement obligations of
$431.6M and a pension deficit of only $18.5M (10-K Item 7) are the long liabilities; the multiemployer pension exposure "cannot
be determined in advance" (Item 7). **What the figures do not say and cannot say:** the earned return by state, the
standalone coverage at Intermountain after its covenant breach, and how much of the capital spending is maintenance; the
filing does not split maintenance from growth.

- **The real costs.** Depreciation is a real cost **[L2015-004]**, and for a network under federal pipe-replacement rules
  it is probably short of what keeps the business in place, as the rows say of railroads: "merely spending their
  depreciation expense will not keep them in the same place" **[M2016-092]**. The run uses depreciation as the
  maintenance figure only because the filing offers no other guess, and says so at Q7. Stock pay is expensed and deducted
  (Step 0); the company grants no options. Restructuring: none recurring; the separation costs sat in discontinued
  operations and in Other through 2024. EBITDA: not featured in the releases read; the goodwill test uses peer EBITDA
  multiples inside the 10-K, which is the auditor's market test, not a figure offered as earnings.
- **The accounts' tells.** No prepaid or deferred balance building out of line (regulatory assets fell in 2025); no
  reserves released into earnings found; the critical audit matter is rate regulation, as for every utility. The covenant
  breach was told plainly in the 10-K, with its cross-defaults and cures. A management that "does explain to you in clear
  terms what’s going on" is "a plus" **[M1994-018]**.
- **The habits carried to Q5.** Earnings guidance every year (2025: $0.88 to $0.98, narrowed to $0.90 to $0.95, actual
  $0.93; 2026: $0.93 to $1.00) and a long-term objective of 6% to 8% growth in earnings per share (8-Ks 2025-02-06,
  2025-11-06, 2026-02-05, 2026-08-06). The FY2024 release featured "adjusted income from continuing operations" beside
  GAAP, adjusting out a gain of $186.6M and the separation costs (8-K 2025-02-06); the FY2025 and 2026 releases lead with
  GAAP. The 2025 guidance assumed "No equity issuances"; the forward sale was struck in December 2025. Recorded as a
  weighing against, guidance being what the row calls "the scourge of earnings" **[L2019-006]**, and
  carried to Q5 as "things that they do in public in relation to their investors and the promises they make"
  **[M2004-067]**.
- **The recast earnings that feed Q7.** Owner cash after depreciation, before interest: 219.2 a year over FY2021 to FY2025
  (Step 0); after all spending: negative every year.
- **VERDICT on the accounts: IN** (no confusion, no suspicion: the figures can be read and reconciled, including the
  restatement for two separations); **WEIGHS AGAINST** on the guidance habit and a depreciation charge that is probably
  short of maintenance **[L2019-006]**, **[M2016-092]**. Filing facts: 10-K FY2025 `0000067716-26-000014`, statements of
  equity and Note 6; 10-Q `0000067716-26-000072`.

---
## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The people.** Nicole A. Kivisto, president and chief executive since January 2024 (proxy: PEO for 2024 with the prior
  CEO, who retired that month); Jason L. Vollmer, chief financial officer; an independent chair of the board (proxy,
  Message From Our Chair; director fees show a chair retainer of $95,000 paid separately from the CEO). For a marketable
  stake the rows read rather than meet: the two yardsticks are "how well they run the business" and "how well that they
  treat their owners" **[M1994-008]**.
- **The tells of dishonesty, sought.** The proxy: CEO total pay $4.81M in 2025 and $5.63M in 2024; pay ratio about 42 to 1;
  no options, no employment agreements, no tax gross-ups, no perquisites beyond employees', anti-hedging and anti-pledging
  rules, a clawback, double-trigger change-in-control terms, no in-flight changes of targets (proxy, What We Don't Do). How
  they "treat themselves versus how they treat the shareholders" **[M1994-009]**: modestly, for a company of this size.
  The reports: the 10-K tells the Intermountain covenant default, the cross-defaults it triggered and the waivers, in the
  main text of Liquidity, not in a footnote; it tells the $3.7M Washington revenue reduction for forecast plant not placed
  in service; it tells the $2.0M regulatory commission complaint order of January 2026 (Note 17). No reserve release and no
  restatement for error found in the filings read; no government investigation is disclosed in Note 17. A sweep of the four
  earnings releases read for "mistake" found none: the releases speak of execution, not of what went wrong.
- **The habits carried from Q4, read with the integrity record.** Guidance each year, kept inside a range and never
  claimed as beaten; an EPS growth objective; an adjusted figure featured once (FY2024 release), adjusting out a gain as
  well as costs; the 2025 guidance's "No equity issuances" followed in December 2025 by a forward sale settling in 2026,
  which the company then disclosed as its 2026-2027 funding plan (8-K 2026-02-05). Read together, this is the ordinary
  habit of a listed utility, recorded against, not a sign of purpose; "If you’ve got doubts, forget it." **[M2013-088]**:
  no doubt about honesty is raised by what was read.
- **Love of the business; the same after being paid.** Insiders as a group own 976,459 shares, 0.5% (proxy, record date);
  the CEO 217,029 shares, about $4.1M at $19.00, a little over four times her 2025 salary; directors' holdings of 4,849 to
  17,594 shares are of the size a few years of the $150,000 annual stock award would give, and the proxy does not show any
  bought "with their savings, rather than simply having been the recipients of grants" **[L2019-008]**.
  The stock ownership policy (5x salary for the CEO) is a rule, not a choice. Nothing found either way on love of the work
  beyond the record.
- **Ability, the weighing.** For: two separations executed (2023, 2024); gas rate relief in Washington, Montana, South Dakota and Wyoming in 2025 (10-K Item 7); a data center served "with an
  approach that requires minimal new capital investment" (10-K Item 1). Against: the deciding part earns 1.4% on its assets
  and the company 7.0% on equity against 9.5% allowed (Q2, Q3); a subsidiary failed an interest coverage covenant in 2025;
  electric operation and maintenance expense rose 17.2% in 2025 (10-K Item 7). The rows put the business first, "we still
  look to the underlying business, though" **[M1996-037]**.
- **VERDICT on integrity: IN** (no doubt found **[M2013-088]**; candid on the covenant default **[M1994-009]**); **ability
  WEIGHS AGAINST**, on earned returns well below allowed and the covenant breach **[M1994-008]**.

---
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The retention test.** The rule: retention must deliver "at least $1 of market value for each $1 retained" over a
  five-year span **[R1995-009]**, read also against intrinsic value. The post-separation company has two years of record,
  so the test is run on what the retained and raised money earns. In 2025 it kept $80.2M of earnings (191.4 less dividends
  declared of 111.2) and spent $770.4M on plant, the rest from new debt (net +$385.9M) and, from 2026, new shares (10-K FY2025
  cash flow statement; 10-Q). The added capital earns about 6.5% in cash (Q3). Market leg: the shares sell at about 1.37
  times book (2,926.9 of equity, 210.35 million shares, $13.91 a share, against $19.00), so the market pays more than a dollar
  for each dollar kept. Intrinsic leg: a dollar put to work at about 6.5% is worth more than a dollar at the long rate of
  5.43% and about 65 cents at ten percent. The forward question, "Can you keep using all of the capital you generate,
  effectively, for a very long time?" **[M2010-097]**, is answered by the plan: all of it and more, at a regulated return. **Weighs
  against at the floor; passes the market leg.**
- **Buybacks.** None since the separations. The statements of equity show small repurchases in 2021 to 2023 ($6.7M,
  $7.4M and $4.8M; in 2023, 153,622 shares, all reissued on the vesting of stock awards the same year), purchases made to
  feed vesting, which the rows rule out as a reason: buying "to cover options. That actually isn’t the best reason to buy
  in shares" **[M2014-008]**. *Written back from Q7:* the company as it now stands has bought back no shares; the 2021 to
  2023 purchases were made at prices for a company that still held Knife River and Everus (2023: $4.8M for 153,622 shares,
  about $31.32 each) and cannot be set against this run's range of $7.16 to $9.70 a share; none is shown at or below the
  bottom of a range for the business bought, and no price was named, the omission the rows call "puzzling" since a
  repurchase is "entirely purchase-price dependent" **[L2016-002]**. Weighs against, on trivial sums.
- **Issuance and deals.** "We will issue common stock only when we receive as much in business value as we give."
  **[R1995-010]**. MDU sold 11,675,126 shares forward at a public price of $19.70 in December 2025 (4.3 million settled in
  March 2026 for $81.3M; 7.4 million left, about $139.6M) and 1,343,432 shares at the market in the second quarter of 2026
  for $29.6M net, under a $400M programme with $370M left (10-K Note 11; 10-Q). Its plan is $150M to $175M of equity in 2026
  and $100M to $125M in 2027 "to support near-term capital expenditures for growth" (8-K 2026-02-05). Set against Q7's range
  (below), the shares were sold above the value per share this run computes, so on the issue test the old owners received
  more than they gave. The issuance is not a sign of promotion here but a funding model: a utility whose spending runs at
  nearly three times depreciation must keep selling shares. Serial issuance stays the framework's candidate second STOP,
  "we have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**; a programmed issuer to fund
  regulated plant is weighed against, not stopped. **No all-stock deal**: the Badger Wind interest was paid in cash, so the
  one STOP of Part A, for an undervalued acquirer's all-stock deal **[L2009-019]**, does not arise.
- **The project in development.** Bakken East, $2.7B to $3.2B, with precedent agreements for nearly 1.2 Bcf a day, a
  final investment decision before a FERC filing expected in the fourth quarter of 2026, in-service in late 2029 and 2030;
  "the company continues to evaluate all financing options" including partnership (8-K 2026-08-06). The North Dakota
  Industrial Commission selected it for firm capacity commitments of up to $50M a year for ten years (10-K Item 7). Its cost
  is about two-thirds of today's market value; it is a decision management has not yet made, and the run cannot value it
  (no filed return, no financing). Recorded here and at Q9, not credited at Q7.
- **Dividends.** A target payout of 60% to 70% of earnings (8-K 2026-02-05), a ratio policy of the kind the rows call
  "nuts" **[M2000-051]**, paid by a company that sells new shares in the same year: $108.2M of dividends paid in 2025 and
  $111.0M of shares sold in the first half of 2026. The policy is at least "clear, consistent and rational" in being
  stated **[L2012-015]**, but a dividend is right when a company "expects to regularly earn more than it can profitably
  employ in its business" **[M2004-089]**, and this one employs more than it earns.
- **Part A: WEIGHS AGAINST.** Growth capital at about 6.5%, a ratio dividend financed in part by share sales, and a
  programmed issuer; no STOP.

### Part B: the pay, the board and the owners
- **Pay tied to what the person controls.** The annual plan pays on adjusted income from continuing operations, customer
  satisfaction, reliability and safety; the long-term plan is 70% performance shares on three-year cumulative adjusted EPS
  and relative total return against twenty utility peers, 30% restricted stock units that vest on time alone (proxy, CD&A).
  No element charges for the capital used. The rows: "When capital invested in an operation is significant, we also both
  charge managers a high rate for incremental capital they employ" **[L1994-019]**; "In a capital-intensive business, you
  have to have something that — you have to have a factor in the compensation arrangement that includes a capital cost
  element." **[M2009-081]**; "a batting average that does not include a cost of capital is a phony batting average"
  **[M1995-010]**. Here EPS can be raised by spending more capital at a return near the long rate, and the plan pays for it.
  The time-vested units are pay that arrives whatever happens, systems that "payoff no matter what happens"
  **[M1999-018]**.
- **Who designs it.** The committee uses a consultant and positions pay "near the median of comparable positions at peer
  companies" (proxy), the comparative-data habit the rows name: "comp committees have become slaves to comparative data"
  **[L2005-015]**.
- **The board and the owners.** An independent chair separate from the chief executive; a three-member independent
  compensation committee; annual say-on-pay; majority voting (proxy). Directors receive $110,000 cash and $150,000 in stock
  a year. Owners are told the numbers plainly (Q4, Q5) and given guidance (carried from Q4).
- **Part B: WEIGHS AGAINST**, mildly: pay on adjusted EPS with no capital charge in a business whose EPS is bought with
  capital **[M2009-081]**, **[L1994-019]**; against it, an independent chair and plain reporting.

---
## Q7: WHAT IS IT WORTH? STOP.
**The definition and the rate.** Value is how many birds, how sure, how soon, at "the yield on long-term U.S. bonds"
**[L2000-021]**: "use the government bond rate" **[M1996-025]**, here 5.43% (Step 0). The cash counted is what comes out after
what must go back in, "are you going to have to put more cash into after you buy it?" **[M2014-068]**.

**The construction** (Q7's range CONVENTION, the four specifics of the PG re-test and the six specifics (a) to (f); every sum
in `compute.py`):
- **Base.** Owner cash after every real cost, five-year mean, FY2021 to FY2025, continuing operations (Step 0 table). Four
  specifics: (1) growth is measured on aggregate owner cash, not per share; (2) all spending is deducted in the
  all-spending case, with the depreciation variant beside it, and the maintenance judgment stated (below); (3) after year
  ten, zero nominal growth; (4) a price above the top of the range closes OUT.
- **(e) Maintenance central.** The filing gives no maintenance figure; it names replacement and safety programmes inside
  one capital total. The only guess the filing allows is depreciation, "not inappropriate in most companies to use as a
  proxy for required capital expenditures" **[M1998-127]**, and for this network probably short of it (Q4). The central case
  is therefore owner cash after depreciation, before interest (all-equity basis): **$219.2M a year**. The growth spending
  (capital spending above depreciation, net of removal cost; mean $350.6M a year) is charged against the growth it buys, at
  the cash return it has shown: owner cash before working-capital swings rose $57.8M from 2022 to 2025 on $886.6M of such
  spending in 2022 to 2024, **6.52%** (Q3).
- **The two ends.** Case A, no growth: $219.2M a year, level, no growth spending. Case B, shown growth: each year's base
  plus 6.52% on the growth spending of all earlier years, less that year's growth spending of $350.6M, for ten years; then
  growth and growth spending stop, and the stream is held level (owner cash $447.8M by year ten, about 7.4% a year).
- **(f) The cap.** Case B's year-ten owner cash would be about a tenth of revenue if revenue grew at its own 2021 to 2025
  pace, below the highest share earned in the filings read (18.4% in 2025); no rate above the discount rate is carried after
  year ten. Not binding.
- **(a) Cycles.** No end year is a cyclical peak or trough on the filer's own description. Working capital swung: the line
  that carries the cost deferrals, other current assets, moved -48.5 in 2023, +81.0 in 2024 and +54.5 in 2025 (cash flow
  statements), and the filer describes the 2023 to 2024 fuel and purchased power deferral and its recovery over two years
  from April 2024 (10-K Item 7). Both the draw and its recovery fall inside the window, so the literal five-year mean is
  kept. Beside it, the working-capital-neutral base
  (2022 to 2025, $236.8M) gives case A **$8.70** a share.
- **(b) Decline.** The depreciation-basis series rises. The all-spending series is negative in every year (all-equity mean
  -$131.4M); a level negative stream has no positive value (about -$23.54 a share at 5.43%), shown beside, not used as an end.
- **(c) Acquisitions.** The one purchase in the window, the 49% Badger Wind interest ($264.6M, December 2025), was paid in
  cash and sits inside capital spending, so it is deducted with the total growth credited. Purchases average about a quarter
  of owner cash before purchases ($52.9M a year against $219.2M), so the serial-acquirer rule does not apply. No merger. No signed, unclosed deal; Bakken East is a
  project, not an acquisition, with no filed record of earnings or financing, so it is left out and not valued (Q6).
- **(d) Working capital** is counted in the literal base (above).
- **Tax.** The company's own tax, no conversion. Its low effective rate comes from production tax credits that the North
  Dakota renewable rider returns to customers (10-K Item 7: lower tracker revenue "partially associated with higher
  production tax credits offset in income tax benefit"); the rows: in utilities "all benefit of lower tax rates goes to
  customers" **[M2017-031]**. No shelter is priced separately.
- **Basis.** All-equity: owner cash before interest against market value plus net debt. Net debt at 2026-06-30: borrowings
  $2,577.2M (long-term $2,572.5M plus current $4.7M) less cash $46.3M = **$2,530.9M** (10-Q); operating leases ($61.1M of
  payments, 10-K) left out, as the convention says. Enterprise value at the price: $3,996.6M + $2,530.9M = **$6,527.5M**.
  The equity-only figures are beside it.

**The floor, tested first.** The expected return at the price, all-equity: **case A 3.36%** ($219.2M on $6,527.5M); **case B
4.31%** (the rate at which case B's stream is worth $6,527.5M); the working-capital-neutral case A 3.63%; a deliberately
generous case B in which every added dollar earns 9.5% in cash, the allowed return on equity, 5.15%. **No case earns the floor
of about ten percent at the price** **[M2003-149]**: "So, there’s just a point at which we drop out of the game." **[M2003-149]**.
The file closes OUT on the floor, whatever the width (Q7, The floor is tested first).

**COMPUTATION, NOT A CLEARANCE beyond this point in Q7** (the range and the fair price are reported at the owner's request;
the box was decided by the floor).
- **Value range** (all-equity, at 5.43%, per share on 210,349,456 shares): **$7.16 (case A) to $9.70 (case B)** against
  **$19.00**. The width is 1.35 to 1; the price is about twice the top. Equity-only beside: $9.60 to $12.66. With the
  forward shares settled (7.4 million more shares, $139.6M more cash), case A is $7.56. The literal `tools/run.py` window,
  as filed and mixing discontinued operations, shown beside and not used: owner cash after depreciation 230.2 (three years)
  and 257.8 (five years); after all spending -163.2 and -86.4 ($M).
- **Growth at the two rates.** At 5.43% the growth case is worth more than the level case, because the added capital's
  6.52% cash return is above the bond; at ten percent it is worth less (case A -$1.61, case B -$5.17 a share, all-equity),
  the inversion the rows name, "growth can destroy value if it requires cash inputs in the early years of a project or
  enterprise that exceed the discounted value of the cash that those assets will generate in later years" **[L2000-023]**.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, the two averaged,
  after the company's own tax. **All-equity (central): -$3.39 a share**, that is, no positive price: at ten percent the
  operating business is worth less than its net debt on both cases ($2,192M and $1,444M of enterprise value against
  $2,530.9M of net debt). **Equity-only, beside: $3.86 a share** (case A $6.87, case B $0.85). No cheap price is reported.
- **VERDICT: OUT**, on the floor: the best case defensible from the filings returns about 4.3% at $19.00, against a floor of
  about ten percent **[M2003-149]**, **[L2002-020]**; and the price sits far above the top of the range at the long rate, which
  closes OUT by the same convention **[L2013-012]**. Filing facts: 10-K FY2025 cash flow statement and Item 7 Capital
  expenditures (`0000067716-26-000014`); 10-Q balance sheet (`0000067716-26-000072`).

---
## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP. **NOT REACHED** (closed at Q7).
## Q9: COULD IT RUIN US? WEIGHING. **NOT REACHED** (facts recorded under AFTER THE STOP).
## Q10: IS IT THE FAT PITCH? WEIGHING. **NOT REACHED.**
## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? **NOT REACHED** (facts recorded under AFTER THE STOP).

---
## THE BOX
**OUT, at Q7 on the floor:** value range $7.16 to $9.70 a share (all-equity, at the 5.43% Treasury rate) against $19.00;
the best case returns about 4.3% at the price; fair price all-equity below zero (-$3.39), equity-only $3.86. Q1 IN, Q2 IN
(gas distribution decides; regulator-set ordinary returns), Q3 against, Q4 accounts IN and against, Q5 integrity IN and
ability against, Q6 against in both parts. Integrity was answered (IN), so no integrity flag is needed.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; the box is unchanged; operator rule 2; [M1997-127].)*
- **Q8.** The bond: the 30-year Treasury yields 5.43% (Step 0); the cases above return 3.4% to 4.3% on the enterprise at the
  price.
- **Q9.** Borrowings $2,577.2M at 2026-06-30, about 49% of debt plus equity at 2025-12-31; pre-tax earnings over interest
  2.96 times in 2025 ((211.0 + 107.7) / 107.7, the coverage definition of **[L2012-002]**); 12.2% of debt at floating rates;
  maturities of $144.7M in 2026 (all but $4.7M repaid by June 2026) and $274.7M in 2027 (10-K Item 7A); investment-grade
  ratings at all rated issuers (10-K Item 7). Intermountain breached its minimum interest coverage covenant at 2025-09-30,
  which cross-defaulted MDU Energy Capital's notes and the revolving credit agreements until waived. Risk factors name
  wildfires, pipeline explosions and cyberattacks among hazards, with insurance that "may not fully mitigate losses" (Item
  1A); one utility can be ruined by one event, "A catastrophic event can render a single utility insolvent" **[L2005-019]**.
  Bakken East would cost $2.7B to $3.2B, financing not settled (8-K 2026-08-06). Multiemployer pension contributions
  "cannot be determined in advance" (10-K Item 7). Purchase commitments of $1,799.9M (10-K Item 7).
- **Q10.** Nothing found.
- **Q12.** No business the framework names (casinos, tobacco, distributor loading, gambling). The company owns shares of
  three coal plants and is subject to EPA rules on them (10-K Item 1A, Item 7).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit c7ad2740); written question by question; committed after each
      (790e48de Step 0 to Q1; a3778194 Q2; dca66b13 Q3; 70694cea Q4; 32bf20e5 Q5; 04a62d28 Q6; 927af863 Q7 with the Q6
      write-back; the closing commit for this audit). The research was read in large part before Q1 was written (the 10-K,
      10-Q, proxy and releases were fetched and read first), so write-early held for the sections, not for the reading.
- [x] Dispatched: the brief allowed per-question pathspec commits of this file and the research folder only; the lock is the
      dispatching session's (operator rule ten). This run binds nothing until it is folded into the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (a
      directory listing showing two other runs of today, the session's opening git status with another run's commit
      subjects, a memory index line on the queue) is declared under Contamination and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment set beside an id is in that row
      (`check_run.py` in the research folder: 0 problems); no E-ids. Every filing fact carries its document and accession
      (Step 0 lists them); the comparators' figures carry theirs. Numbers not from a filing or a row are labelled
      CONVENTION (the FY2021 construction, the 21% interest add-back, the comparators) or are the framework's own (the
      floor, the range construction, the fair price).
- [x] The order was kept. Q1 and Q2 IN; Q3, Q4 (weighing half), Q5 (ability), Q6 recorded and carried; Q7 closed OUT on
      the floor, tested first; the range and the fair price after it are headed COMPUTATION, NOT A CLEARANCE; Q8 to Q12 not
      reached; facts for them written under AFTER THE STOP.
- [x] Owner cash after every real cost, from the filed cash flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the US Treasury (issuing authority), dated 2026-10-16; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found, in the foundations paragraph, before any verdict **[M1997-127]**.
- [x] Point-in-time: not a point-in-time run; no anchor bars any row.
- [x] Only the arithmetic lines of `tools/run.py` were used (its as-filed window is shown beside, not used).
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Windows across separations.** Q7's five-year average assumes the filings give five comparable years; a company that
spun off two businesses inside the window has no filing that restates the first year for both. The run built FY2021 by
subtracting the spun company's own Form 10 figures and confessed it as a CONVENTION of the run, tested on FY2022. A rule
saying which restatement governs and how a missing year is built would make two runs agree. (2) **Q2's regulated-return
exception** sends a regulator-set ordinary return to Q3 as a second best, but says nothing of a business that earns well
below the return its regulator sets (here 7.0% on equity, and 1.4% on assets at the deciding part, against 9.5% allowed).
The run carried the shortfall to Q3; whether a persistent shortfall is itself evidence of a castle filling in, or of
management, is not said. (3) **Policy as the threat to a deciding part.** Washington's building code and the litigation over
it are a forecast of politics and courts covering 43% of the deciding part's revenue. The framework's TOO HARD (NATURE)
paragraph is written for industries whose insiders would not write a forecast down; it does not say how to treat a
regulated business whose own forecast is plain but whose state's policy is not. The run judged it slow narrowing at Q2 and
recorded the stricter reading; with no case clearing the floor, the box is the same either way. (4) **Specific (e) and the
growth case.** "Where the filing allows the maintenance guess" does not say whether depreciation counts as such a guess when
the filing offers none; and "the growth spending charged against the growth it buys" gives no method. The run measured the
cash return the growth spending has shown (6.52%) and built case B from it; at the long rate that growth adds value, at ten
percent it destroys it, so which end is the top depends on the rate, a case (e)'s inversion clause does not foresee. (5)
**The all-equity add-back** of interest after tax names no tax rate; the company's effective rate is held down by credits
that pass to customers, so the run used the 21% statutory rate and said so. (6) **A negative fair price.** Part VII defines
the fair price as an average of two ends valued at ten percent; when both ends are worth less than net debt the figure is
negative, and the text does not say how to report it or what alert it sets. The run reports it as -$3.39 ("no positive
price") with the equity-only $3.86 beside. (7) **Forward sale agreements** are neither shares outstanding nor debt; the
framework's share-count and net-debt rules do not mention them. The run kept them out of the central figure and showed the
effect beside it. (8) **Comparators when the 10-K names none**: the brief covers it, the framework's competitor row does not;
the run took them from the proxy's own peer groups as a CONVENTION.
