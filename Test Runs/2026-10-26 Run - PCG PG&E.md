# Company Run — PG&E Corporation (NYSE: PCG) — 2026-10-26
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-26: the operator does not hold this name (`PORTFOLIO.md` has no PG&E row).*

**Departure stated by the brief:** the repository moved on 2026-10-25 from `C:\Users\chreh\OneDrive\Documents\BRK` to
`C:\Projects\BRK`; nothing else departs from `Screens/_daily/_dispatch_brief.md` (which this analyst did not open; the
departure is quoted from the dispatch).

**Contamination, declared and not used.** (1) `git log -3` at the start showed three commit subjects of other work: an NRG
run's template commit, the fold of an NI (NiSource) v5 run of 2026-10-23 closed "OUT at Q7, on the floor" with its range
and fair price, and an ASML note. The NI subject names a utility verdict and figures; none of it was used here, and no
NI file was opened. (2) A directory listing of `Test Runs/` (filtered for my own folder name) printed the names of other
analysts' research folders of today: ASML, NRG, OGE, PAM, PLTR, SNPS. None was opened. (3) The CSV search for utility
rows returned **[L2023-011]**, which names "California's largest utility", i.e. this company; it is a row of the ledger,
not a blind-listed file, and is used under the framework's rule for a row about one company (Q2). No other run, holding
review, `PORTFOLIO.md`, watchlist or resume file was opened, listed or searched. (4) After my last commit, `git log -4`
showed other analysts' commit subjects: a PNW run closing "Q5 ... OUT on integrity doubt" and "Q4 ... weighs against",
and the fold of an OGE run "OUT at Q7, on the floor" with its range and fair price. Seen after this run's box was
written; not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $12.63 (close 2026-10-23, the last close before this Monday's run; Yahoo chart data through
  `tools/sources.py`, **an aggregator, flagged** per operator rule 5). For orientation only: $17.43 on 2026-08-03 and
  $14.06 on 2026-09-01, the fall coming around the company's 2026-09-02 strategic review (below).
- **Shares by class.** `python Screens/cover_shares.py PCG` printed two lines from the 10-Q filed 2026-10-22
  (accession `0001004980-26-000055`): 2,680,173,293 and 264,374,809, with its "MULTIPLE CLASSES" warning. Read against the
  filing: the second figure is the common stock of Pacific Gas and Electric Company (the "Utility"), all of it held by PG&E
  Corporation, not a PCG class; the first carries the cover's own asterisk, "*Includes 477,743,590 shares of common stock
  held by Pacific Gas and Electric Company" (the Plan shares the Fire Victim Trust exchanged and sold, 2022 to 2024; FY2023
  10-K, `0001004980-24-000014`). Economic common shares: 2,680,173,293 less 477,743,590 = **2,202,429,703**, against
  2,202,416,553 outstanding on the 2026-09-30 balance sheet (the issued-less-held check; the 13,150 difference is
  October issuance under the plans). No 8-K or prospectus after the 10-Q issues shares (EDGAR list read to 2026-10-22).
  **Mandatory convertible preferred:** 32,200,000 shares of 6.000% Series A, converting automatically on 2027-12-01 at
  not more than 2.4331 and not less than 1.9465 common shares each (FY2025 10-K, `0001004980-26-000009`); at $12.63 the
  maximum rate applies, so they are counted as 78,345,820 common shares and their dividend is not charged to owner cash.
  The $2.15 billion 4.25% convertible notes due 2027 convert at about $23.18 a share with principal settled in cash
  (same 10-K): out of the money, counted as debt. **Valuation share count: 2,280,775,523.**
- **Market cap:** $27,817M on the 2,202.4M common; **$28,806M** with the convertible preferred as converted (the figure
  used below).
- **Sovereign for the earnings currency (USD):** **5.33%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-23 (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-12, `0001004980-26-000009`); 10-Q for 2026-09-30 (filed
  2026-10-22, `0001004980-26-000055`); DEF 14A (filed 2026-04-09, `0001004980-26-000020`); 8-Ks of 2026-10-22
  (`0001004980-26-000056`, results), 2026-08-31 (`0001999371-26-019256`, Senate Bill 492 and the 2026-09-02 call),
  2026-08-04 (`0001193125-26-332848`, $1.7B mortgage bonds), 2026-06-23 (`0001193125-26-279461`, credit facilities),
  2026-06-03 (`0001193125-26-255485`, $2.2B mortgage bonds), 2025-12-17 (`0001999371-25-020477`, leadership); and for the
  cycle the 10-Ks for FY2018 (`0001004980-19-000004`, covering 2016 to 2018), FY2020 (`0001004980-21-000007`), FY2022
  (`0001004980-23-000029`), FY2023 (`0001004980-24-000014`) and FY2024 (`0001004980-25-000010`). Competitors: Edison
  International 10-Ks FY2017 (`0000827052-18-000046`), FY2019 (`0000827052-20-000026`), FY2022 (`0000827052-23-000010`),
  FY2025 (`0000827052-26-000012`); Sempra 10-Ks FY2019 (`0001032208-20-000006`), FY2022 (`0001032208-23-000008`), FY2025
  (`0001032208-26-000010`); Xcel Energy 10-K FY2025 (`0000072903-26-000009`) and its XBRL company facts.
- **One figure cross-checked against the filed statement:** capital expenditures FY2025, $11,787M in the XBRL company
  facts and $11,787M in PG&E Corporation's filed statement of cash flows (FY2025 10-K); net cash from operations FY2025,
  $8,716M in both; long-term debt 2025-12-31, $57,387M in both. For Xcel, net income FY2025 $2,018M in both.
- **`python tools/run.py PCG`** printed one line and stopped: "PCG: no overlapping OCF/D&A/capex annual facts.
  UNRESEARCHED." (PG&E tags its "Depreciation, amortization, and decommissioning" under no tag the script reads). No
  arithmetic line was available from it, so its debt table (the dispatcher's caution) never printed. Every figure below
  was taken by hand from the filed statements, with the scripts in `Test Runs/_research 2026-10-26 PCG/` (`q7.py`,
  `peers.py`); the filed cash-flow lines are these ($M):

| FY | Net cash from operations | Capital expenditures | Depreciation, amortization, and decommissioning | Stock pay expense | Cash interest paid |
|---|---|---|---|---|---|
| 2016 | 4,409 | 5,709 | 2,755 | 108 | 726 |
| 2017 | 5,977 | 5,641 | 2,854 | 85 | 790 |
| 2018 | 4,752 | 6,514 | 3,036 | 89 | 786 |
| 2019 | 4,816 | 6,313 | 3,234 | 50 | 10 (in Chapter 11) |
| 2020 | (19,130) | 7,690 | 3,468 | 35 | 1,563 |
| 2021 | 2,262 | 7,689 | 3,403 | 56 | 1,404 |
| 2022 | 3,721 | 9,584 | 3,856 | 115 | 1,607 |
| 2023 | 4,747 | 9,714 | 3,738 | 91 | 2,286 |
| 2024 | 8,035 | 10,369 | 4,189 | 98 | 2,421 |
| 2025 | 8,716 | 11,787 | 4,634 | 134 | 2,665 |

  Sources: statements of cash flows in the FY2018, FY2020, FY2022 and FY2025 10-Ks (accessions above); stock pay from the
  XBRL tag `AllocatedShareBasedCompensationExpense` (transcription, flagged). 2020 includes the emergence payments
  ($5.4B cash to the Fire Victim Trust, $11.0B to the Subrogation Wildfire Trust, $1.0B to public entities, $5.2B initial
  Wildfire Fund contribution; FY2020 10-K).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, and for PG&E the answer turns on what happens to the business in the fire seasons and in Sacramento, not
on the quotation. The market serves and does not instruct: the fall from $17.43 in August to $12.63 "just tells us
prices" **[M2006-077]** and is read here for nothing else. No macro forecast enters **[M2000-094]**: the run forecasts
neither interest rates nor California politics; where the box depends on a political forecast, that is a finding about
the question, not a forecast made. Who is paid to tell you: the company's own "non-GAAP core earnings" (which leave out the
Wildfire Fund's cost) and any adviser to the strategic review are read as the seller's account **[M2011-083]**. Margin of
safety: a decision that needs pencil and paper "it’s too close to think about" **[M1996-084]**.

**Contrary evidence, written down as found [M1997-127]** (hunted hardest against the business; listed in the order found):
(1) On 2026-08-31 the company said it "does not believe Senate Bill 492 adequately addresses the financing risks created
by California’s current wildfire liability framework" and that the bill "falls short of creating the long-term durability
needed to attract affordable investment" (8-K `0001999371-26-019256`). (2) On 2026-09-02 it announced a strategic review of "the full range
of options related to how PG&E Corporation and the Utility are organized and financed", cut planned 2027 capital spending
from $13.4B to $11.4B, and withdrew its 2028 to 2030 capital forecast; "securing an investment-grade credit rating is a
foundational objective" (10-Q Q3 2026). (3) The Legislature "concluded its 2025-2026 legislative session without enacting
additional legislation to modify the state's wildfire liability framework" (same 10-Q). (4) On SCE's Eaton fire of
January 2025 the company says it "could reduce the estimated life to zero and incur up to $3.7 billion of accelerated
amortization" of its Wildfire Fund asset (same 10-Q). (5) The CPUC set the 2026 return on equity at 9.98% against the
11.30% asked (FY2025 10-K). (6) Over FY2016 to FY2025 PG&E's net income to common summed to a loss of $3,778M and the
weighted share count rose from 499M to 2,197M (XBRL, checked to the statements). (7) A criminal record: six felony
counts (San Bruno, 2016), 84 counts of involuntary manslaughter and one of unlawfully causing a fire (Camp, 2020), and
criminal complaints over Kincade and Zogg resolved by civil stipulated judgments (FY2020, FY2022, FY2023 10-Ks).
(8) "Non-GAAP core earnings" of $3,307M against GAAP $2,593M for 2025, the gap including Wildfire Fund amortization and
wildfire costs, and the bonus plan pays on the core figure (DEF 14A). For the business, found and written down with the
same care: no catastrophic fire has been attributed to PG&E since the 2022 Mosquito fire (the 10-Q names no later one);
return on equity ran 8.2% to 9.4% in 2022 to 2025; operating cash rose from $2,262M (2021) to $8,716M (2025); the FERC
set a 10.38% transmission return in August 2025.

## THE STANDING RULE
The rule binds the buyer: "Never risk permanent loss of capital." **[L2023-005]**; "We are never going to risk what we
have and need for what we don’t have and don’t need." **[M2012-081]**. For this name the zero is not a remote figure: the
equity was nearly wiped out in the last cycle (FY2019 shareholders' equity $5,136M after $14.5B of losses in two years,
then a 3.75-fold share issue at emergence). Any purchase would have to be sized so that "anything times zero is zero"
**[M2007-050]** costs the buyer only what he can lose, and bought without borrowed money. Owning PCG on those terms does
not put the buyer at risk of ruin; owning it on margin or in a size whose loss would matter would.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **The key variables, and how predictable they are** ("trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**). PG&E's earning power is, by its own
  description, "the product of the Utility’s rate of return (i.e., the cost of capital for long-term debt and equity)
  and its rate base" (FY2025 10-K). (a) **Rate base**: the CPUC-jurisdictional weighted-average rate base adopted for
  2026 is $54.0B and the 2027 GRC asks $67.0B for 2027 rising to $85.4B for 2030 (FY2025 10-K); the transmission rate
  base is set by FERC formula. Foreseeable within a range: it is filed, litigated in public and decided on a four-year
  cycle. (b) **Allowed return**: 9.98% on a 52.00% equity share for 2026 (CPUC, December 2025), 10.38% at FERC; for the
  electric utility "when you get an allowed return in the electric utility you’re almost certain of earning it, I mean,
  if you behave yourself" **[M2010-037]**. Foreseeable within a range. (c) **Wildfire liability and its offsets**: under
  inverse condemnation the Utility "can be liable for these damages and the costs of fire suppression efforts" once an
  ignition occurs and "may be unable to control the extent of damages" (10-Q Q3 2026); the offsets are insurance, the
  Wildfire Fund, the SB 254 Continuation Account and rate recovery after a prudency review. This variable is not
  predictable, and it is the one that decided the last cycle.
- **Do the past statements tell me the future ones?** **[M2008-033]** For (a) and (b), yes: the GRC and cost-of-capital
  decisions are in the filings. For (c), the past statements show the range of outcomes (2018 and 2019 losses of $6.9B and
  $7.7B; a $50.5B pool of liabilities subject to compromise at 2019-12-31) but not the next draw from it.
- **How far off could I be?** **[M2011-084]** On (a) and (b), a point or two of return. On (c), from a 9% return to the
  equity's loss, as 2019 showed.
- **Routing.** The business is a regulated monopoly whose mechanics I can state from its filings: it is not a business
  whose industry changes fast (the Q1 routing to TOO HARD does not apply), not a financial institution, and a holding
  company with one part (the Utility; PG&E Corporation's own result was a loss of $255M in the first nine months of 2026
  against the Utility's $2,595M profit, 10-Q Q3 2026). The unpredictable variable (c) is what "could destroy, modify or
  reduce" the economics five to fifteen years out, which the framework asks at Q2, test 11, and the framework places the
  regulatory climate of a utility at Q2 and Q9 (Q7, The regulated utility, citing **[L2023-011]**). I carry it there.
  *(The alternative reading, that Q1's test 4, "If something’s important but unknowable, forget it." **[M2006-076]**,
  closes the file here, gives the same box and cause one question earlier; see "What in the framework was wrong or
  unclear".)*
- **VERDICT: IN**, on the economics of the regulated business, which can be foreseen from the rate cases on file
  **[M2012-065]**, **[M2010-037]**; the wildfire variable is carried to Q2, where the castle's durability is asked.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**

- **The parts table.** PG&E Corporation reports one operating part, the Utility; the Corporation itself is a holding
  company whose own line is interest and costs (a loss of $255M in the first nine months of 2026 against the Utility's
  $2,595M; 10-Q Q3 2026). **The Utility decides** (all of five-year operating profit). Inside it, electric and gas
  distribution, generation and gas transmission are CPUC-regulated and electric transmission FERC-regulated; all earn an
  allowed return on rate base, so they are read together.
- **1. The castle questions: what keeps it standing, and how permanent?** The Utility holds the wires and pipes of its
  service area and is the regulated provider; customers who buy generation elsewhere (community choice aggregators and
  direct access) "continue to obtain transmission, distribution, metering, and billing services from the Utility"
  (FY2025 10-K). Its return is set by the regulator, and "The whole idea behind the utility industry is not to allow
  extraordinary profits." **[M2000-131]**. The permanence of the wires franchise is high; the edges erode slowly
  (San Francisco "has submitted a petition with the CPUC seeking a valuation of the Utility’s electric assets", and gas
  restrictions "have reduced, and will continue to reduce the use of natural gas", which could leave gas assets no longer
  "used and useful"; FY2025 10-K). What the castle protects is not a high return but an allowed one, and the question for
  this name is whether it protects even that.
- **2. Would it stand without the lord?** The regulated return assumes the owner keeps its side: "if you behave yourself"
  **[M2010-037]**; "We shouldn't expect our regulators to live up to their end of the bargain unless we live up to ours."
  **[L2009-011]**. PG&E's record is the case in which the operator's conduct (San Bruno 2010; the 2017 and 2018 fires)
  decided the owners' result; the castle did not stand on its own through the last cycle.
- **3. The money test.** Nobody can duplicate a transmission and distribution grid across northern and central
  California for any sum: the question "if I had a hundred million dollars and I wanted to go in and take on See’s Candy,
  could I do it?" **[M2011-015]**, asked of the grid, answers no. The castle against competitors is real.
- **4. Pricing power and the agony before a rise.** Every price is set in a proceeding: the Utility asked for an 11.30%
  equity return for 2026 and was granted 9.98% (FY2025 10-K); "the CPUC considers affordability as it adjudicates the
  Utility’s rate cases, and concerns about affordability could cause the CPUC to approve lesser amounts" (FY2025 10-K).
  That is "a prayer session before you raise your prices a penny" **[M2005-020]**, by construction of the business.
- **5 to 8. Volume, share of mind, low cost, brand, the low bid.** Not the source of this castle: the customer has no
  choice of wires. Load growth is among the topics the company names (8-K `0001004980-26-000056`), which supports rate
  base.
- **9. Ask the competitors** (their own filings): SDG&E "recorded a $351 million charge for the write-off of a
  regulatory asset associated with 2007 wildfire costs" in 2017 (Sempra FY2019 10-K, `0001032208-20-000006`); SCE carried
  its 2017 and 2018 fire costs until the CPUC approved the TKM and Woolsey cost-recovery settlements in 2025, and in January
  2025 the Eaton fire "ignited in SCE's service area in Los Angeles County and spread due to a number of contributing
  factors under conditions of an extreme Santa Ana windstorm" (EIX FY2025 10-K, `0000827052-26-000012`). The attacker in
  this field is not another utility; it is the fire, the liability law and the Legislature, and each of the three
  California owners has been hit in the span.
- **10. Widening or narrowing?** Narrowing, on the company's own evidence: the Wildfire Fund that backs the liability
  regime may be used up by another utility's fire (the company "could reduce the estimated life to zero", 10-Q Q3 2026);
  SB 254's Continuation Account "would provide up to $18 billion of liquidity" only if the administrator "determines that
  the Continuation Account is necessary" and the CPUC extends the customer charge, and SB 254 "prohibits the Utility from
  including in its equity rate base the first $2.9 billion" of new fire-risk mitigation capital (FY2025 10-K); the
  Legislature adjourned without further reform; the company itself says the new bill "falls short" and has cut its capital
  plan and withdrawn its forecast (8-K of 2026-08-31; 10-Q Q3 2026). Widening, on the same filings: no catastrophic fire
  attributed to PG&E since 2022; undergrounding under SB 884; AB 1054's prudency presumption and the cap on reimbursement
  at "20% of the equity portion of the utility’s electric transmission and distribution rate base" (FY2025 10-K).
- **11. What could destroy, modify or reduce it, five to fifteen years out?** **[M2000-014]** One ignition in a wind
  event. The last cycle of it cost $5.4B in cash (with $1.35B more deferred) plus 477 million shares, 22.19% of the
  company, to the Fire Victim Trust, $11.0B to subrogation holders and $1.0B to public entities (FY2020 10-K), against a
  market value today of $28.8B. The rows' own form: "A catastrophic event can render a single utility insolvent"
  **[L2005-019]**; "whether you earn X or go broke is not an equation that works" **[M2024-011]**; and of utilities in such
  states, "it is difficult to project both earnings and asset values in what was once regarded as among the most stable
  industries in America" **[L2023-011]**. The last row speaks of "an actual outcome at California's largest utility"
  **[L2023-011]**, this company. Under the framework's rule for a row about one company it is evidence of the speaker's
  view at its date and decides nothing alone; the box below rests on the filings and the question's own tests, with the
  row weighed beside them. Abel in 2025, of the same problem: "We really have to solve the risk side" **[M2025-040]**.

**The competitor row** (same metrics, each company's own filings; whole span FY2016 to FY2025; `peers.py`, `capex_da_out.txt`):

| Company (why) | Return on average common equity, % by year 2016 to 2025 | Cumulative net income to common / average equity | Loss years | Capex / depreciation | Basic shares, 2016 to 2025 |
|---|---|---|---|---|---|
| PG&E Corp | 8.1, 8.9, -43.0, -86.1, -10.1, -0.5, 8.2, 9.4, 9.2, 8.7 | -1.8% a year (-$3,778M) | 4 | 2.30x | 499M to 2,197M (x4.40) |
| Edison International (SCE; same state, same regime) | 10.9, 4.8, -3.8, 10.8, 5.4, 5.4, 4.4, 8.7, 9.3, 28.8 | 8.8% a year | 1 | 2.17x | 326M to 385M (x1.18) |
| SDG&E (Sempra's California electric utility) | 10.5, 7.2, 11.5, 11.7, 11.1, 10.3, 10.6, 9.9, 8.7, 5.2 | 9.1% a year | 0 | Sempra parent 3.09x | Sempra 500M to 653M (x1.30, split-adjusted) |
| Xcel Energy (out of state: an eight-state regulated utility with wildfire suits of its own, Marshall 2021 and Smokehouse Creek 2024, under non-California law) | 10.4, 10.2, 10.7, 10.8, 10.6, 10.6, 10.8, 10.3, 10.4, 9.4 | 9.9% a year | 0 | 2.52x | 509M to 587M (x1.15) |

  Sources: net income to common and equity from the 10-K statements and selected data listed in Step 0 (PG&E and Xcel
  figures are XBRL company facts checked to the filed statements at one point each; EIX common equity is total
  shareholders' equity less its preferred, the 2023 preferred inferred as $1,673M from 2024's $1,645M plus the $28M
  repurchased in 2024, flagged; SDG&E's earnings and equity from Sempra's 10-Ks, its five-year selected data for 2015 to
  2019; Xcel's fires from its FY2025 10-K). EIX's 2025 return includes the CPUC-approved TKM and Woolsey cost-recovery
  settlements ($966M after tax for TKM alone, EIX FY2025 10-K); without them its span average is lower. SDG&E's 2017 dip
  is the 2007 wildfire write-off. Sempra's capex is the parent's (Texas and LNG included), shown only for scale.

- **The field's returns over the last full cycle, judged in words.** The out-of-state utility earned close to its
  allowed return every year of the span. The three California utilities did not: PG&E lost money over the decade as a
  whole and its owners were diluted more than four-fold; SCE's owners earned a middling return, made whole only by a 2025
  recovery decision; SDG&E, the smallest exposure, earned the steadiest. The regulated-return exception that carries a
  capital-heavy utility to Q3 as a second best, "there’s no way we get rich on our utility investments. But there’s no
  way we get poor, either." **[M2009-104]**, presumes the floor of the bargain; in California over this cycle the floor
  gave way, at this company most of all. The castle against competitors stands; the castle that protects the allowed
  return did not, in the one full cycle on record.
- **A change for the better?** The bull case is that the post-2019 regime (AB 1054's fund and prudency standard, SB 254's
  Continuation Account, PG&E's mitigation and undergrounding, four years without a catastrophic PG&E fire) has repaired
  the bargain. Such changes happen: the railroads "were a terrible business for decades and decades and decades and then
  they got good." **[M2017-026]**. The framework credits one only on a full cycle in which the behaviour held (Q2, Change),
  and the cycle that would test this one has not run: the first large draw on the fund is another utility's (Eaton), the
  company's own reading of it is that its fund asset's life may go to zero, and the Legislature has not acted.
- **Can the future be judged?** "In some businesses that’s very — it’s impossible — to figure — at least it’s impossible
  for us to figure — and then we just — we don’t even think about it then." **[M2000-014]**. Whether a catastrophic
  ignition occurs in the next ten fire seasons, what it costs under inverse condemnation, and what the Legislature and the
  CPUC then do, are forecasts the insiders do not write down: the company withdrew its 2028 to 2030 capital forecast and
  opened a review of how the companies "are organized and financed" (10-Q Q3 2026). That is the insiders' test: "They
  would say, “That’s too hard.”" **[M2000-105]**. The moat is tenuous, and "it’s just too risky. We don’t know how to
  valuate that, and therefore we leave it alone." **[M2000-019]**.
- **Not OUT, and why.** A castle shown on the evidence to be filling in closes OUT. The evidence here does not show the
  allowed return being competed away or the franchise lost; it shows a protection whose durability depends on events and
  legislation that have not happened. The filings say what the bargain is; no filing can say whether it will hold. That
  is the TOO HARD case of the STOP paragraph, not the OUT case.
- **Cause: NATURE, not WORK.** The deciding question is not answered by a filing not yet read: "We couldn't solve this
  problem, moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**. The company's
  own management, with every document, withdrew its forecast. No research pass is written; a lower price does not reopen
  the box.
- **Re-look condition, dated.** The framework's condition as written: the first fiscal year in which the Utility's
  electric or gas deliveries, or its field's, fall, read from the 10-K. **CONVENTION of this run:** beside it, the first
  PG&E 10-K filed after the Wildfire Fund administrator and the CPUC have resolved SCE's Eaton fire claims (fund draws
  made, reimbursement decided), read for whether the participating utility's equity was protected as AB 1054 and SB 254
  provide. Rationale: the volume trigger was written for a cycle shown in sales; this castle's cycle is shown in the
  liability regime's first full test, and the Eaton resolution is that test and is public.
- **VERDICT: TOO HARD (NATURE)** at Q2 **[M2000-014]**, **[M2000-019]**, **[M2006-013]**: the castle against
  competitors stands; whether it protects even the allowed return through the next ten to twenty fire seasons cannot be
  judged, by the company's own forecasting as much as by mine.

## Q3 to Q10 and Q12: NOT REACHED
The STOP at Q2 closed the file. Q3 to Q10 and Q12 are not answered; what was found for them is under AFTER THE STOP,
and the figures Q7 would build are under COMPUTATION, NOT A CLEARANCE, at the owner's request.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q2**: the regulated franchise stands against competitors, but whether the bargain
that protects its allowed return survives California's wildfire liability regime over the next ten to twenty years is a
forecast the company's own management has declined to write down **[M2000-014]**, **[M2000-105]**, **[M2000-019]**.
Re-look: the framework's volume condition, and beside it (CONVENTION of this run) the first PG&E 10-K after SCE's Eaton
fire claims are resolved through the Wildfire Fund and the CPUC. **Integrity facts recorded, not judged.** COMPUTATION
(not a clearance): value range, the no-growth case alone, **$10.66** a share against **$12.63**; fair price **$5.68**
(equity-only, central for a regulated utility); all-equity beside, $0.53 and a negative fair price.

## COMPUTATION, NOT A CLEARANCE
*Every figure in this section is arithmetic made after the STOP at Q2, at the owner's request; none is a clearance, a
verdict or entry language (operator rule 3).* Built by Q7's range convention as the framework states it; scripts and
output in `Test Runs/_research 2026-10-26 PCG/q7.py` and `q7_out.txt`.

- **Basis.** A regulated utility: the equity-only basis is central (Q7, The regulated utility, **[L2017-012]**): owner
  cash after interest and after the company's own tax, against the market value of the shares ($28,806M, the
  convertible preferred counted as converted). All-equity beside.
- **Owner cash, the window FY2021 to FY2025** ($M; net cash from operations, less the maintenance guess, less stock pay,
  less the Utility's preferred dividends, less the principal repaid on the SB 901 and AB 1054 recovery bonds, which leaves
  their dedicated customer charge out with them as the convention directs):

| FY | Operations | less D&A (maintenance guess) | less stock pay | less Utility preferred | less recovery-bond principal | Owner cash | Share of revenue |
|---|---|---|---|---|---|---|---|
| 2021 | 2,262 | 3,403 | 56 | 14 | 0 | (1,211) | -5.9% |
| 2022 | 3,721 | 3,856 | 115 | 13 | 51 | (314) | -1.4% |
| 2023 | 4,747 | 3,738 | 91 | 14 | 168 | 736 | 3.0% |
| 2024 | 8,035 | 4,189 | 98 | 14 | 175 | 3,559 | 14.6% |
| 2025 | 8,716 | 4,634 | 134 | 14 | 223 | 3,711 | 14.9% |
| **Average** | | | | | | **1,296** | |

  The maintenance guess is the filed "Depreciation, amortization, and decommissioning", since the filing states no
  maintenance figure (specific (e): the central case is maintenance-only where the guess is allowed; depreciation is the
  only guess the filing allows). Tax: the company's own; it paid almost no cash tax (federal net operating loss
  carryforward $38.3B, of which $34,957M post-2017 never expires, and California $34.1B expiring 2039 to 2041; FY2025
  10-K). The shelter does not run out inside ten years, so the carryforward convention of Q7 (Whose tax) does not apply.
- **Growth.** The series changes sign (first two years average $(762)M, last two $3,635M), so by specific (b) the growth
  between the halves is meaningless and **the range is the no-growth case alone, said so**. The literal compound rate is
  not defined. (Revenue grew 4.84% a year, 2021 to 2025.)
- **The range, equity-only (central):** no growth, at the 30-year Treasury of 5.33%: $1,296M / 0.0533 = $24,319M =
  **$10.66 a share**, against **$12.63**. Owner cash on the price: 4.50%.
- **The floor, tested first:** no case in the range earns about ten percent at $12.63 (4.50% on the no-growth case);
  were Q7 reached, it would close OUT on the floor whatever the width **[M2003-149]**.
- **Fair price (Part VII), equity-only, central:** the no-growth case at ten percent, $1,296M / 0.10 = $12,962M =
  **$5.68 a share** (one case, so the average of the ends is that case).
- **All-equity, beside:** owner cash before interest $3,496M (adding back the $2,077M average cash interest and the
  recovery-bond principal, the bonds then counted in debt); net debt at 2026-09-30 $64,376M (short-term borrowings
  $2,205M, long-term debt current $1,474M and noncurrent $61,347M including $11.5B of VIE recovery bonds and receivables
  financing, plus $252M Utility preferred, less $902M cash; operating leases left out; 10-Q Q3 2026). No-growth at 5.33%:
  $65,595M less $64,376M = $1,219M = **$0.53 a share**; at ten percent, $34,962M less $64,376M, a **negative** fair price
  ($-12.90).
- **Utility debt credit (stated as required, not used in the central case):** long-term debt excluding the recovery
  bonds rose from $37,316M (2020-12-31) to $48,065M (2025-12-31), $2,150M a year; growth spending (capital spending
  above the maintenance guess) averaged $5,865M; the cap at the CPUC's allowed long-term debt share of 47.50% (2026 cost
  of capital; FERC's is 49.7%, the CPUC share decides as the larger rate base) is $2,786M, so the credit is $2,150M a
  year. Growth spending in year one $5,865M gross ($3,715M net of the credit), year ten $8,972M gross; none after year
  ten. These enter only a growth case, which specific (b) removes from the range.
- **Beside, not a range end (for the record of what growth would do):** carried at the revenue growth of 4.84% with the
  growth spending and the credit grown with it and stopped at year ten, the case is worth $0.57 a share at 5.33% and
  $-4.12 at ten percent: on the window's figures the growth bought is worth less than its cost, the inversion of
  specific (e) ("growth can destroy value"). All-spending owner cash, debt credit added, averages $(2,419)M a year.
- **The window, shown against its base years** **[L2005-003]**: the filer describes 2021 and 2022 as carrying payments
  to the Fire Victim Trust ($758M and $592M) and in 2022 $778M of wildfire insurance premiums (FY2022 and FY2023 10-Ks).
  Those are costs of this business's catastrophes, so they stay in. The last two years alone average $3,635M of owner
  cash (12.6% on the price), and the twelve months to 2026-09-30 about $2,670M; the five-year rule exists so that no
  single good year sets the base, and here it is the difference between a figure below the floor and one above it. The
  width of that disagreement is itself the Q2 finding in numbers.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed, no verdict, the box unchanged (operator rule 2), each with its source* **[M1997-127]**.

**Q3, capital in and earned.** Capital spending ran 2.30 times depreciation over FY2016 to FY2025 and 2.48 times over
FY2021 to FY2025 (statements of cash flows). The CPUC-jurisdictional rate base adopted for 2026 is $54.0B; the 2027 GRC
asks $67.0B for 2027 rising to $85.4B for 2030 (FY2025 10-K); the 2027 capital plan was cut to $11.4B and 2028 to 2030
withdrawn (10-Q Q3 2026). Realized return on average equity: 8.2%, 9.4%, 9.2%, 8.7% in 2022 to 2025 against allowed
returns of about 10%; over the whole span a loss (Q2 table). SB 254 keeps the first $2.9B of new mitigation capital out of
the equity rate base (FY2025 10-K).

**Q4, the balance sheets first, ten years** ($M at year end; PG&E Corporation; FY2018, FY2020, FY2022, FY2025 10-Ks
and XBRL company facts):

| Year | Total assets | Shareholders' equity | Long-term debt (incl. current) | Short-term borrowings | Cash | Reinvested earnings | Regulatory assets (noncurrent) |
|---|---|---|---|---|---|---|---|
| 2016 | 68,598 | 17,940 | 16,920 | 1,516 | 177 | 5,751 | 7,951 |
| 2017 | 68,012 | 19,220 | 18,198 | 931 | 449 | 6,596 | 3,793 |
| 2018 | 76,995 | 12,651 | 40,634 | 3,435 | 1,668 | (250) | 4,964 |
| 2019 | 85,196 | 5,136 | in $50,546 subject to compromise | DIP 1,500 | 1,570 | (7,892) | 6,066 |
| 2020 | 97,856 | 21,001 | 37,316 | 3,547 | 484 | (9,196) | 8,978 |
| 2021 | 103,327 | 20,971 | 42,706 | 2,184 | 291 | (9,284) | 9,207 |
| 2022 | 118,644 | 22,823 | 50,010 | 2,055 | 734 | (7,542) | 16,443 |
| 2023 | 125,698 | 25,040 | 52,351 | 3,971 | 635 | (5,321) | 17,189 |
| 2024 | 133,660 | 30,149 | 55,715 | 1,523 | 940 | (2,966) | 15,561 |
| 2025 | 141,611 | 32,540 | 58,208 | 2,675 | 713 | (650) | 15,981 |

What the figures say **[M2025-032]**: equity was cut by two-thirds by the fire losses of 2018 and 2019 and rebuilt in 2020
by issuing shares (common stock carried at $13,038M in 2019 and $30,224M in 2020), not by earnings; reinvested earnings
were still negative ($650M) at the end of 2025 after four profitable years. Debt more than tripled, from $16.9B to $58.2B
(of which $10.1B is recovery bonds serviced by customer charges); regulatory assets doubled; 2018's long-term debt shows
$18.6B classified as current on the eve of the Chapter 11 filing. There is no goodwill to read. Cash is kept small and
liquidity is borrowed ($6.25B Utility revolver to 2031, 8-K `0001193125-26-279461`). What the balance sheet cannot say
is the size of the next fire; the Wildfire Fund asset ($3.66B at 2026-09-30) may be written down by up to $3.7B on the
Eaton information (10-Q Q3 2026). Real costs: depreciation is charged; stock pay $134M (2025); the company features
"Non-GAAP core earnings" of $3,307M ($1.50 a share) against GAAP $2,593M ($1.18), excluding among other items the
amortization of the Wildfire Fund contribution ($253M after tax) and "Wildfire-related costs, net of insurance" ($97M)
(DEF 14A `0001004980-26-000020`, Exhibit A reconciliation). Recorded here for Q4 and carried for Q5 as the framework
directs; not weighed.

**Q5, integrity facts (recorded, not judged).** (1) 2016: a federal jury found the Utility guilty on one count of
obstructing a federal agency proceeding and five counts under the Natural Gas Pipeline Safety Act (San Bruno); sentence
of January 2017 included five years' probation and a monitor; the court later found a probation violation on reporting
(FY2020 10-K, `0001004980-21-000007`). (2) 2020: the Utility pleaded guilty to 84 counts of involuntary manslaughter and
one count of unlawfully causing a fire (2018 Camp fire), paying the maximum fine of about $3.5M plus $0.5M (same 10-K).
(3) 2021: the Sonoma County District Attorney charged five felonies and 28 misdemeanors over the 2019 Kincade fire,
resolved in April 2022 by a civil stipulated judgment of $20.25M "without the Utility admitting any liability" (FY2022
10-K, `0001004980-23-000029`). (4) 2021: the Shasta County District Attorney charged 11 felonies and 20 misdemeanors over
the 2020 Zogg and other fires; all criminal charges dismissed with prejudice under a civil stipulated judgment of
May 2023, $50M of expense (FY2023 10-K, `0001004980-24-000014`). (5) 2022: a civil stipulated judgment with five county
District Attorneys resolved any state criminal prosecution over the 2021 Dixie fire, $34.75M not recoverable in rates,
no admission (FY2022 10-K). (6) The CPUC's Wildfires OII remedies continue to be charged (2025 "Investigation remedies"
$112M after tax; DEF 14A). (7) The featured non-GAAP figure and its use in pay (Q4 above). (8) Management: Patricia
Poppe, CEO since January 2021 (DEF 14A); the Utility's CEO from 2026-01-01 is Sumeet Singh (8-K `0001999371-25-020477`).

**Q6, the money and the owners.** Dividends: $921M (2016) and $1,021M (2017) paid, then none from 2018 to 2023;
reinstated at $86M (2024) and $220M (2025); raised in December 2025 to 20 cents a year, "targeting a dividend payout
ratio of approximately 20% of core earnings by 2028" (10-Q Q3 2026). Issuance over the span: $822M and $395M of common
in 2016 and 2017; at emergence in 2020 $7,582M of common, $1,304M of equity units and 477 million shares to the Fire
Victim Trust; $2.15B of convertible notes (December 2023); $1,128M of common and $1,579M of mandatory convertible
preferred (2024); $1.0B of junior subordinated notes (February 2026) (cash-flow statements; 10-Q Q3 2026). The weighted
basic share count rose from 499M (2016) to 2,197M (2025). No share repurchases in the span. **Q6's buyback line, written
back from the computation:** there were no repurchases to read against the bottom of the computed range ($10.66). No
acquisition or all-stock deal in the span. Pay: CEO total compensation $19,812,481 for 2025, pay ratio 100 to 1, short-term
incentive paid at 139.0% of target with non-GAAP core EPS among the metrics (DEF 14A).

**Q8, the alternatives.** The 30-year Treasury yields 5.33% (2026-10-23). The computed owner-cash yield on the price
is 4.50% on the five-year window.

**Q9, the target's debt and exposures.** Debt $65.0B at 2026-09-30 (short-term $2.2B; long-term current $1.5B;
noncurrent $61.3B) against equity market value $28.8B. Cash interest $2,665M in 2025 against pretax income of $2,423M:
(2,423 + 2,665) / 2,665 = about 1.9 times, before any fire. Maturities: Utility mortgage bonds $600M (2026) and $3.0B
(2027); the Corporation's $2.15B convertible notes (2027) and $1.0B notes (2028) (FY2025 10-K). Not investment grade at
the stated objective (10-Q Q3 2026); the 10-Q names "increased borrowing costs and collateral posting requirements" as a
consequence of the Legislature's inaction. One event: a single catastrophic fire; per-year retention of $1.0B before
the Wildfire Fund (10-Q Q3 2026). Exposures that grow because the owner is solvent: inverse condemnation liability.

**Q10.** Nothing to record beyond the box.

**Q12.** An electric and gas utility: not a business the rows name. The record of fatal fires is under Q5.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early).
      Commits: template and notes; Step 0 to Q1; Q2; the box, computation and facts; this audit.
- [x] Dispatched: the brief granted per-question pathspec commits of my two paths only; no lock contention met.
      Folding into the register is the dispatcher's (operator rule ten); a run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. What was seen by accident
      (three commit subjects, six research-folder names) is declared under contamination at the top and not used.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-26 PCG/check_ids.py`: no E-ids; every M/L/R id in
      the CSV; every quoted fragment beside an id found in that row); every filing fact carries its accession; numbers
      carry a filing or a CONVENTION.
- [x] The order was kept; Q1 IN, Q2 TOO HARD (NATURE) closed the file; nothing after it is a clearance, and the
      arithmetic after it is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence was written down as it was found, under the foundations; the facts for later questions are under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor applies.
- [x] `tools/run.py` produced no arithmetic (it refused the filer, "UNRESEARCHED"); nothing it prints was used. The
      dispatcher's caution about its debt table did not arise; debt was read from the balance sheets.
- [x] `python tools/check_framework.py` PASS before the final commit (see the reply).
- **Honest weak points of this run.** (1) The box rests on a judgment between OUT and TOO HARD at Q2 and between Q1 and
  Q2 as its home; I give my reasons above and the other readings below. (2) Competitor figures for Xcel and part of
  PG&E's ten-year series are XBRL company facts checked to the filed statement at one point each, not read line by line;
  EIX's 2023 preferred is inferred. (3) SDG&E is compared on its own earnings, but Sempra's capex ratio is the parent's.
  (4) The maintenance guess is depreciation including decommissioning and regulatory amortization; the filing gives no
  better. (5) I did not read the 2026-09-02 investor presentation itself (it is not on EDGAR as an exhibit I found); its
  content is taken from the 10-Q's summary.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Where a catastrophe-liability question lives.** Q1's test 4 ("If something’s important but unknowable, forget
it." **[M2006-076]**) and test 5 could close a business like this at Q1; Q2's test 11 **[M2000-014]** and the Q7 utility
paragraph ("the regulatory climate at Q2 and Q9") place it at Q2; Q9 carries "A catastrophic event can render a single
utility insolvent" **[L2005-019]** as a weighing. Three homes for one risk. I closed at Q2, the home the text names for
the regulatory climate; the box and its cause are the same at Q1, but a run that put the question only at Q9 would
reach Q7 and close on the floor instead, with a different box. A sentence saying which question owns an uncapped
liability that can take the equity to zero would settle it. (2) **The change-for-the-better re-look condition** is
written as a fall in volume; for a utility whose cycle is a liability regime, not sales, it does not test the question,
and I confessed a CONVENTION of this run beside it. (3) **Specific (b) and the regulated utility.** A utility's
owner cash after maintenance can change sign across a five-year window for reasons that are regulatory timing (balancing
accounts, as here: $2,266M of under-collection in 2021), so the range collapses to one case and the growth spending
and debt credit of the 2026-10-23 utility amendment never enter the central figure. The text does not say whether the
utility convention means the growth case to be computed anyway; I showed it beside, not as a range end. (4) **The
five-year window against two good years** moves the owner-cash yield from 4.5% to 12.6%; the framework's window is
deliberate **[L2005-003]**, but for a company emerging from bankruptcy the window is dominated by the emergence
aftermath, and the text has no rule for a window that straddles a reorganization. (5) **Shares held by a subsidiary.**
The cover count includes 477.7M shares held by the Utility; `cover_shares.py` printed the gross figure without the
cover's own footnote. Read correctly here, but a less careful run would overstate the share count by 22%.
