# Company Run — Oil States International, Inc. (NYSE: OIS) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-16, after the run was committed: not held (`PORTFOLIO.md` carries no line for
OIS or Oil States).*

**Dispatch.** A dispatched blind run under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the two departures
the brief states: the lines of evidence are derived by the analyst from the FY2025 10-K, and the competitors are the rivals
the 10-K itself names. Template copied to this file before any fetch (commit `b8088ab5`). Working folder
`Test Runs/_research 2026-10-16 OIS/` (notes, fetch and arithmetic scripts tracked; raw filings and XBRL dumps under its
gitignored `cache/`).

**Contamination, declared and not used.** (1) The session's opening context showed the last commit subjects of the
repository, which describe another company's v5 run (USAC, closed OUT at Q2 on ordinary returns over the cycle, with its
computed range and fair price), and file names of research folders of other companies in the git status. (2) My first
directory command listed the `Test Runs/` file names dated 2026-10-1x (other companies' run file names only; no OIS file
appeared in that listing, and I searched for none). (3) The memory index loaded with the session carries one-line notes
on the queue's state (counts of gate-clearers, a paused wave). None of this names Oil States; none was opened or used. The
USAC subject is the one that could anchor this run (an energy-services name closed at Q2), so the Q2 judgment below is
built from Oil States' and its named rivals' own filings only, and the reader should know the anchor was in view.

**Lines of evidence chosen from the FY2025 10-K (Items 1, 1A, 7), and why.** Item 1 and Item 7 say demand "is cyclical and
substantially dependent upon activity levels in the oil and natural gas industry" (10-K FY2025, accession
0001121484-26-000007, Item 1, Our Industry) and report three segments with very different results, so the lines are:
(i) segment revenue, operating income and assets over the whole span the filings cover since the 2014 Civeo spin-off
(2014 to 2025), because a cyclical supplier can only be judged over a full cycle and the parts differ; (ii) the named
competitors' returns over the same span; (iii) pricing and competition in the filer's own words (Item 1A: "relatively few
barriers to entry", "oversupply", bid-basis contracts); (iv) acquisitions, goodwill and impairments (GEODynamics 2018, the
goodwill impairments of 2019, 2020 and 2024, the long-lived impairments of 2025), because they show what capital put in
has earned; (v) debt and its refinancing (the 2026 convertible notes, the new cash-flow credit agreement), buybacks and
their prices, and stock pay; (vi) the auditor change and the chief-executive succession of 2026 for the people. Customer
concentration was checked and set aside: no customer above 10% of revenue in 2023 to 2025 (Note 13). Litigation: the 10-K
states routine claims; the one recent item read is a 2022 litigation settlement gain in the offshore segment (10-K FY2022,
accession 0001121484-23-000008, Note 14).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $7.94 (close 2026-10-15; aggregator quote via `tools/run.py`, flagged per operator rule 5, live quote only).
- **Shares by class** from the latest filing's cover: one class, 60,322,619 shares as of 2026-07-24 (10-Q for the quarter to
  2026-06-30, filed 2026-07-30, accession 0001121484-26-000033; `python Screens/cover_shares.py OIS`). Checked against
  the balance sheet of the same 10-Q: 82,179,784 issued less 21,836,542 treasury = 60,343,242 at 2026-06-30, consistent.
  No 8-K or prospectus filed after the 10-Q (the EDGAR list shows the 10-Q and its 8-K of 2026-07-30 as the latest filings).
  The 529,428 shares issued on 2026-04-01 to retire the 2026 notes are inside the count.
- **Market cap:** $479M (7.94 × 60.32M).
- **Sovereign for the earnings currency (USD):** 5.43%, US Treasury daily par yield curve, 30-year, 2026-10-15 (issuing
  authority, via `tools/run.py`'s sovereign line).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-03-04, accession 0001121484-26-000007 (Items 1, 1A, 7,
  Notes 2, 3, 13, goodwill note, cash flow statement); 10-Q for 2026-06-30, filed 2026-07-30, accession
  0001121484-26-000033 (balance sheet, debt note, segments, equity note); proxy DEF 14A filed 2026-03-27, accession
  0001121484-26-000017 (fetched; read only for the facts listed under AFTER THE STOP); for the cycle, the segment notes of
  the 10-Ks for FY2015 (0001437749-16-025723), FY2017 (0001121484-18-000022), FY2019 (0001121484-20-000042), FY2022
  (0001121484-23-000008) and FY2023 (0001121484-24-000021). **One figure cross-checked against the filed statement:**
  net cash provided by operating activities FY2025 $105,123 thousand on the filed cash flow statement of the 10-K
  (0001121484-26-000007) against $105.1M in the XBRL series `tools/run.py` printed; capital expenditures $31,191 thousand
  against $31.2M; both agree.
- **`python tools/run.py OIS`, arithmetic lines only** (its yields, growth-implied line and windows are not used as rules):
  OCF 2023 / 2024 / 2025 = 56.6 / 45.9 / 105.1; SBC 7.0 / 8.7 / 7.7; capex 30.7 / 37.5 / 31.2; D&A 60.8 / 54.7 / 47.4
  (USD millions). Its "other window" (five years) gives owner cash after all capital spending of 14.5 a year and, on the
  depreciation basis, minus 20.3 a year. No securities inside operating cash, no other stock-pay line, no intangible or
  software payment beside capex was found by the tool. SBC resolved from the cash-flow add-back each year.
- **Owner cash after every real cost** (operating cash flow less stock pay less all capital spending; acquisitions listed
  separately), USD millions, from the XBRL series of each year's first-filed 10-K, transcription only:

| year | OCF | SBC | capex | owner cash (capex) | owner cash (D&A basis) | cash interest paid | acquisitions paid |
|---|---|---|---|---|---|---|---|
| 2014 | 438.0 | 25.6 | 199.3 | 213.1 | 287.6 | 40.4 | 0.2 |
| 2015 | 256.1 | 21.8 | 114.7 | 119.6 | 103.0 | 5.6 | 33.4 |
| 2016 | 149.3 | 21.3 | 29.7 | 98.3 | 9.3 | 3.9 | 0.0 |
| 2017 | 95.4 | 23.0 | 35.2 | 37.2 | -35.3 | 4.2 | 12.9 |
| 2018 | 103.2 | 22.6 | 88.0 | -7.4 | -42.9 | 9.9 | 379.7 |
| 2019 | 137.4 | 16.8 | 56.1 | 64.5 | -2.7 | 9.6 | 0.0 |
| 2020 | 132.8 | 8.4 | 12.7 | 111.7 | 25.9 | 6.4 | 0.0 |
| 2021 | 7.2 | 7.9 | 17.5 | -18.2 | -81.4 | 6.5 | 0.0 |
| 2022 | 32.9 | 6.9 | 20.3 | 5.7 | -41.3 | 8.3 | 8.1 |
| 2023 | 56.6 | 7.0 | 30.7 | 18.9 | -11.2 | 7.9 | 0.0 |
| 2024 | 45.9 | 8.7 | 37.5 | -0.3 | -17.5 | 7.4 | 0.0 |
| 2025 | 105.1 | 7.7 | 31.2 | 66.2 | 50.0 | 7.2 | 0.0 |

  Five-year average 2021 to 2025: 14.5 after all capital spending; minus 20.3 on the depreciation basis. 2014's OCF is the
  first-filed figure of the spin-off year and may carry Civeo's cash flow to the spin date (not separated here; 2014 is
  not used in any base below). 2020's owner cash includes a $36.8M net income-tax refund (taxes paid negative, XBRL
  `IncomeTaxesPaidNet`) and a large receivables release.
- **The balance sheets, ten year-ends, read first** (the template places this at Q4; the file may close before Q4, so it is
  read here, from the table `tools/run.py` printed and the filed statements behind it):

| year-end | assets | equity | cash | receivables | inventory | goodwill | intangibles | debt on face | retained earnings | revenue |
|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 1,728 | 1,224 | 8 | 233 | 221 | 482 | 230 | 274 | 798 | 1,017 |
| 2020 | 1,152 | 758 | 72 | 163 | 170 | 76 | 206 | 201 | 329 | 638 |
| 2021 | 1,086 | 696 | 53 | 186 | 169 | 76 | 186 | 179 | 282 | 573 |
| 2022 | 1,064 | 690 | 42 | 219 | 183 | 79 | 170 | 153 | 272 | 738 |
| 2023 | 1,046 | 710 | 47 | 203 | 202 | 80 | 153 | 136 | 285 | 782 |
| 2024 | 1,005 | 681 | 65 | 194 | 215 | 70 | 126 | 125 | 274 | 693 |
| 2025 | 883 | 573 | 70 | 202 | 183 | 71 | 31 | 55 | 164 | 669 |
| 2026-06-30 | 839 | 581 | 20 | n/r | n/r | n/r | n/r | 18 | n/r | n/r |

  Earlier year-ends from the XBRL series: assets 1,810 (2014), 1,599 (2015), 1,384 (2016), 1,302 (2017), 2,004 (2018);
  equity 1,341 / 1,256 / 1,204 / 1,133 / 1,440; goodwill 252 / 264 / 263 / 268 / 647. (USD millions; n/r = not read.)
  **What moved and why.** Equity fell from $1,341M (2014) to $573M (2025) while revenue fell from $1,820M to $669M; the
  fall is not paid out to owners (buybacks 2017 to 2025 total about $55M, XBRL `PaymentsForRepurchaseOfCommonStock`) but written off: goodwill rose to $647M with the
  2018 GEODynamics and Falcon purchases and was then impaired by $165.0M (2019), $406.1M (2020) and $10.0M (2024), and
  intangibles fell from $230M (2019) to $31M (2025) through amortization and the 2025 impairments ($121.1M of non-cash
  impairments in 2025, 10-K FY2025 Item 1, Recent Developments). Retained earnings fell from $798M (2019) to $164M (2025).
  Receivables against sales rose from 23% (2019) to 30% (2025); inventory against sales from 22% to 27%, with a $20.8M
  inventory impairment in 2025 (10-K FY2025, consolidated results, note (1)). Debt fell from $274M (2019) to $18M at
  2026-06-30 after the 2026 convertible notes were bought back in 2025 and retired on 2026-04-01 with $50.5M of cash and
  529,428 shares (10-Q, accession 0001121484-26-000033, Note 4). What the figures say: a balance sheet now nearly free of
  debt, carried at a book value that the business's own earnings have repeatedly failed to support; what they do not say:
  whether the remaining $547M of offshore-segment assets will earn more than they have over the cycle.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is a share is a business: the question is whether I would be content to own this
business "if the market closed for five years" **[M1997-109]**, and that turns on what its operations earn over a whole
oil-and-gas cycle, not on the oil price. No macro forecast enters ("macro conclusions are — just never enter into the discussion"
**[M2000-094]**): the oil price and rig count are not forecast here; they matter only as the cycle the filings already record. The habit applied: look for "what’s wrong in
things" **[M2025-013]**, starting from the evidence against. **Contrary evidence, written down as found** **[M1997-127]**:
(1) the company reported an operating loss in eight of the eleven years 2015 to 2025 (profits only in 2015, 2022 and 2023) (XBRL `OperatingIncomeLoss`, each
year's first-filed 10-K); (2) its own risk factor says its markets have "relatively few barriers to entry" and that "Many
contracts are awarded on a bid basis, which further increases competition based on price" (10-K FY2025, Item 1A);
(3) the 2018 GEODynamics purchase ($615M of cash, shares and a note) has been impaired through goodwill and long-lived
charges in 2019, 2020, 2024 and 2025; (4) for the case: the offshore segment earned $69.2M of operating income in 2025 on
$546.8M of segment assets, with backlog up to $435M (10-K FY2025, Note 13 and Item 1).

## THE STANDING RULE
Owning a small part of this business, bought with cash and no borrowing, puts the buyer at no risk of ruin: the rule binds
the buyer's conduct, "We are never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**, and the rows name borrowing as the danger: "the only way smart people can get clobbered, really, is through leverage" **[M2004-065]**. Nothing about the purchase calls for leverage.
The target's own debt is weighed at Q9 if reached.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as stated:** understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**; the chemistry may stay opaque if "I understand the economic dynamics of
  the industry" **[M2011-014]**.
- **The key variables and whether they are foreseeable.** Oil States sells engineered capital equipment and consumables
  to oil and gas producers and service companies in three segments (10-K FY2025, Item 1): Offshore Manufactured Products
  (64% of 2025 revenue; flexible bearings, connectors, risers, cranes, mooring, subsea pipeline products, with a military
  and other line of $40.5M), Completion and Production Services (17%; U.S. well-site pressure control and extended-reach
  tools, on day rates) and Downhole Technologies (18%; perforating systems and consumable downhole tools). The variables
  are (a) customers' capital spending on deepwater and international projects, which drives the offshore segment and its
  backlog; (b) U.S. land completions, which drive the other two; (c) Oil States' position against much larger rivals and
  many small ones. The first two are the oil cycle; neither is forecast here, and the rows forbid making that the test:
  "We don’t think we can predict commodity prices." **[M2016-025]**. What can be read is how the business has done
  through the cycle, "off the figures" **[M2008-069]**, and the filings cover two downturns (2015 to 2017, 2019 to 2021)
  and two recoveries. The economics that matter (what it earns on its assets through a cycle, and whether its position
  against rivals is improving) are knowable from those filings and the rivals': "The figures are available." **[M2009-059]**.
- **Routing.** This is not a fast-changing technology business in the sense of the routing rule: the products (flexible
  joints "in operation for over 80 years" in the offshore line; perforating charges; pressure-control equipment) change by
  increments (10-K FY2025, Item 1). Dependence on oil-and-gas spending is "never by itself a STOP at Q1 or Q2" (the
  framework's commodity paragraph); the cost and return position is a Q2
  question. Doubt is recorded: insiders might "not want to put down on paper their predictions" for the U.S. land business ten years out **[M2000-105]**, but that
  question is whether its castle stands, which the figures answer at Q2, not whether its economics can be read.
- **VERDICT: IN.** The economic dynamics (a cyclical supplier of engineered equipment and consumables whose earnings follow
  its customers' capital spending) can be read off ten years of filings: what counts is that "I understand the economic
  dynamics of the industry" **[M2011-014]**, and the decision is made "off the figures" **[M2008-069]**. The question of
  its position goes to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. A moat is what "protects excellent returns on invested capital"
**[L2007-004]**.

**The parts table** (business of parts, the framework's Q2 paragraph; segments read separately because "lumping them
together [...] impedes analysis" **[L2008-005]**). Five-year segment operating income 2021 to 2025, USD millions, as filed
(10-K FY2022, 0001121484-23-000008, Note 14, for 2021 and 2022; 10-K FY2025, 0001121484-26-000007, Note 13, for 2023 to
2025, which restates 2023 for the 2024 realignment of operations between segments):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | castle | decides |
|---|---|---|---|---|---|---|---|---|
| Offshore (Manufactured) Products | 15.4 | 45.3 | 56.3 | 65.3 | 69.2 | 251.5 | engineered niche products (flexible joints, connectors, risers), patents; returns below | **yes**: carries more than the whole of the segments' five-year operating profit |
| Well Site Services / Completion and Production Services | -34.5 | 4.9 | 13.9 | -23.2 | 4.0 | -34.9 | open on the filer's own words (below) | no |
| Downhole Technologies | -13.5 | -6.7 | -5.9 | -20.9 | -124.3 | -171.3 | open: a $615M purchase written down (below) | no |
| Corporate | -32.3 | -40.6 | -41.1 | -22.8 | -46.8 | -183.6 | | |
| total (agrees with XBRL `OperatingIncomeLoss`) | -64.8 | 2.9 | 23.2 | -1.7 | -98.0 | -138.4 | | |

The offshore segment decides. The two land segments are open on the evidence and do not decide; under the paragraph they
would be carried to Q7 as ordinary businesses at no growth (both lost money over the five years).

**The castle tests, each with its filing fact (the deciding part first, then the whole).**
- **The field's returns over the last full cycle (section C), the deciding test here.** The offshore segment, pre-tax
  operating income on segment total assets less its goodwill, as filed, before any share of corporate costs (segment and
  goodwill notes of the 10-Ks for FY2015, FY2017, FY2019, FY2022 and FY2025, accessions in Step 0). The segment's
  composition changed in 2017 (renamed Offshore/Manufactured Products, with its short-cycle manufactured products shown
  separately; the filer states "There have been no operational, reporting or other material changes related to the
  Offshore/Manufactured Products segment", 10-K FY2017, 0001121484-18-000022, Note 1) and in 2024 (a realignment of
  operations between two segments, 10-K FY2025, Note 1):

| year | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| revenue | 961.6 | 724.1 | 508.8 | 381.9 | 394.1 | 402.9 | 340.3 | 298.7 | 381.7 | 381.7 | 397.9 | 431.1 |
| operating income | 200.1 | 146.4 | 87.1 | 38.2 | 38.9 | 36.0 | -80.8 | 15.4 | 45.3 | 56.3 | 65.3 | 69.2 |
| segment total assets | 983.5 | 930.9 | 810.5 | 760.1 | 683.3 | 677.0 | 548.0 | 541.3 | 556.8 | 521.9 | 510.4 | 546.8 |
| segment goodwill | 145.8 | 159.4 | 158.6 | 162.9 | 162.5 | 162.8 | 76.5 | 76.4 | 79.3 | 79.9 | 69.7 | 70.5 |
| margin | 20.8% | 20.2% | 17.1% | 10.0% | 9.9% | 8.9% | -23.7% | 5.2% | 11.9% | 14.7% | 16.4% | 16.1% |
| on assets less goodwill | 23.9% | 19.0% | 13.4% | 6.4% | 7.5% | 7.0% | -17.1% | 3.3% | 9.5% | 12.7% | 14.8% | 14.5% |

  2020 includes an $86.5M goodwill and a $16.2M inventory impairment; 2022 includes a $6.1M litigation gain (10-K
  FY2022, Note 14). Over 2014 to 2025, peak to recovery, with the 2020 goodwill charge added back, the segment earned about
  12% pre-tax on its assets less goodwill before corporate costs; after a share of corporate costs in proportion to revenue
  (a CONVENTION of this run, below) about 8% pre-tax, roughly 6% after a 21% tax. The high years are the two peaks (2014 to
  2016 and 2023 to 2025); the six years 2017 to 2022 averaged about 6% pre-tax before corporate costs and about 2% after.
  The whole company earned operating income on total assets of 17.1% in 2014 and then 3.4%, -5.0%, -5.7%, -0.3%, -13.2%,
  -46.4%, -6.0%, 0.3%, 2.2%, -0.2%, -11.1% (2015 to 2025); about -0.6% a year on average with goodwill impairments added
  back. (Arithmetic in `Test Runs/_research 2026-10-16 OIS/omp.py` and `rivals.py`.)
- **The competitor row** (same metric, operating income on total assets, from the rivals' own filings, as reported
  including their impairments; XBRL of each year's first-filed annual report). The 10-K names the offshore segment's
  rivals: "Our main competitors in this segment include Baker Hughes Company, Hutchinson Group (a subsidiary of Total
  S.A.), NOV Inc., OneSubsea (a joint venture between SLB, Aker Solutions and Subsea 7) and TenarisHydril (a division of
  Tenaris S.A.)" (10-K FY2025, Item 1). Taken: NOV (10-K), Baker Hughes (10-K; Baker Hughes Incorporated to 2016, Baker
  Hughes Company from 2017) and Tenaris (20-F, IFRS), the three named rivals that file their own annual reports with the
  SEC, compared over the whole span. **Flagged, not taken:** Hutchinson and OneSubsea do not file with the SEC in their own
  names (their parents' filings were not read for them and would not isolate them). The land segments' rivals are not
  named in the 10-K ("many smaller companies" and "the larger oilfield service companies", Item 1).

| filer | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | span average | goodwill impairments added back |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NOV (FY2025 10-K 0001193125-26-048350) | 10.8% | -1.5% | -11.4% | -1.4% | 1.1% | -47.8% | -24.4% | -1.4% | 2.6% | 5.8% | 7.7% | 4.4% | -2.9% | 0.8% |
| Baker Hughes (BHI to 2016, last 0000808362-17-000006; BKR from 2017, FY2024 10-K 0001701605-25-000035) | 9.9% | -10.0% | -8.5% | -0.2% | 1.3% | 2.0% | -42.0% | 3.7% | 3.5% | 6.3% | 8.0% | n/t | -1.8% | 1.7% |
| Tenaris (FY2025 20-F 0001554855-26-000490) | n/t | n/t | -0.4% | 2.3% | 6.1% | 5.6% | -4.8% | 4.9% | 16.9% | 20.5% | 11.8% | 11.4% | 8.5% | not separated |
| Oil States (whole company) | 17.1% | 3.4% | -5.0% | -5.7% | -0.3% | -13.2% | -46.4% | -6.0% | 0.3% | 2.2% | -0.2% | -11.1% | -4.3% | -0.6% |

  n/t: not tagged in the XBRL series read (Baker Hughes' 2025 operating income; Tenaris before 2016 on the IFRS tags
  read). Judged in words: over the cycle the named field earned ordinary returns on its assets or less; the best of the
  three, Tenaris, averaged about 8.5% pre-tax and was high only in 2022 to 2025. Oil States earned less than every named
  rival on the whole company and, in its best part, earned well only at the two peaks.
- **The attacker with money**: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do it?" **[M2011-015]**. The filer of its own markets: "The markets in which we operate are highly
  competitive and certain of them, particularly those supporting U.S. land driven activities, have relatively few barriers
  to entry" and "These large national and multi-national companies have greater financial, technical and other resources,
  and greater name recognition than we do" (10-K FY2025, Item 1A). That is the field the rows warn of: "there are some
  industries that are just never going to have barriers to entry" **[M2012-106]**.
- **Pricing power and the agony before a rise** **[M2005-020]**. The filer: the oversupply has led to "competitive
  pressures and reduced prices we can charge our customers for these services and products", and "As a result of
  competition, we may lose market share or be unable to maintain or increase prices for our present products and services"
  (10-K FY2025, Item 1A); in 2025 tariffs "increased the cost of certain products we manufacture in the United States"
  while "competitive market conditions" cut the land businesses (Item 1, Recent Developments; Item 7). Through the last
  inflation the offshore margin rose, from 5.2% (2021) to 16.1% (2025), on volume and backlog recovery; whether that is
  pricing power or the upswing cannot be told from the filings until a downturn tests it, and the 2014 to 2016 margins of
  17% to 21% fell to 9% to 10% by 2017 to 2019. Strong positions "manage to pass through increases in raw material costs" over time **[M2005-017]**;
  the land segments did not.
- **Would the customer still choose it over the low bid?** The filer: "Many contracts are awarded on a bid basis, which
  further increases competition based on price" (Item 1A); its list of principal competitive factors ends "and price".
- **The low-cost position** (the commodity-business test: measure it "more by cost of production" **[M2006-004]**; "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**). No filing read states Oil
  States is the low-cost producer in any line: no instance found in the 10-K FY2025 Items 1, 1A and 7, read in full and
  searched for "cost", "low-cost" and "compet". It describes its rivals as larger, with greater resources, and its own
  answer to the land downturn as "management’s decision to exit certain underperforming locations, service lines and
  product offerings in the United States" (Item 1, Recent Developments).
- **The brand and share of mind.** The offshore names (FlexJoint®, Merlin®) and its "over 80 years" of operation (Item 1)
  are real assets in a niche; the filings give no market share; on the return record above they have not kept returns high
  outside the peaks.
- **Ask the competitors**, "which one would it be and why?" **[M1999-130]**: not possible from the public record read; no instance found in the rivals'
  data read (XBRL only) of any statement about Oil States.
- **Widening or narrowing**, "whether it’s likely to widen further or shrink on you" **[M1999-108]**. In the land businesses, narrowing on the filer's own account: drilling exited
  (rigs sold August 2024), flowback and well testing exited (2024), and "the exit of certain product offerings and
  technologies" in Downhole Technologies with $112.7M of impairments in 2025 (Item 7, segment note (3)). The Downhole
  business was bought in 2018 for about $615M ($295.4M cash, 8.66M shares valued at $294.9M, a $25.0M note; 10-K FY2019,
  0001121484-20-000042) and carries $148.6M of total assets at 2025 year-end after goodwill impairments of $165.0M (2019)
  and $192.5M (2020) and the 2025 charges. The offshore segment's backlog widened ($311M to $435M in 2025, bookings $554M,
  book-to-bill 1.3x, Item 7): the upswing of the cycle, not yet a full cycle's evidence.
- **What could "destroy, or modify, or reduce the economic strengths"** **[M2000-014]**: customers' capital spending (the 10-K's first risk factor);
  consolidation of customers and competitors "using size and purchasing power to seek pricing or other concessions"
  (Item 1A); tariffs on imported components (Item 7); the larger rivals' resources.

**The judgment.** The deciding part is a standing castle in the narrow sense: the offshore business has survived two deep
downturns and holds niche product lines. Over the last full cycle, 2014 to 2025, it protected only ordinary returns: about
12% pre-tax on its assets less goodwill before any corporate cost and about 8% after a share of it, with six straight
years (2017 to 2022) at low single digits, while the whole company lost money at the operating line in eight of eleven
years. The named rivals earned ordinary returns or less over the same span. That is the case the framework sends to OUT,
the standing castle that protects only ordinary returns, since the moat is what "protects excellent returns on invested
capital" **[L2007-004]** and "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**;
"ordinary" is judged in words, since "there’s no formula that gives you that precisely" **[M1999-108]**. The 2023 to 2025 rise in the
offshore margin is a change for the better; the framework credits such a change only on a full cycle, and the row it rests
on reads durability from "the price behavior" **[M2005-020]**; it is the upswing the filings have already shown once (2014 to 2016, then 2017 to 2019) and is not
credited. The land segments are open on the filer's own words ("relatively few barriers to entry", oversupply, bid-basis
pricing) and on their losses. A low price does not reopen the castle: "What you can’t do is turn any investment into a
good deal by paying little" **[M2019-015]**; a low-return business held long does not do well "Even if you buy it cheap
to start with" **[M1998-006]**.

**CONVENTION of this run:** the corporate costs, which the filer does not allocate, are shared among the segments in
proportion to revenue, for the "after corporate costs" figures only. Rationale: the corporate line carries stock pay and
governance the segments need; revenue is the plainest key, and the before-allocation figure is shown first so that the
judgment does not rest on the key.

- **VERDICT: OUT.** A standing castle that protects only ordinary returns over the full cycle, on the filer's and its
  named rivals' own filings (the framework's Q2 list, What it rules OUT). The rows behind it: a moat "protects excellent
  returns on invested capital" **[L2007-004]**; "you can have only two competitors and they’re still terrible businesses"
  **[M2013-052]**; the moat is judged, "You have to understand the businesses." **[M1999-108]**; and the boxes are "in,
  out, and too hard" **[M2006-013]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. WEIGHING.
NOT REACHED (the file closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0; facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. WEIGHING.
NOT REACHED. Facts found (buybacks and their prices, the 2018 purchase, pay) are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH. STOP.
NOT REACHED as a question. The two reporting figures the owner asks for are computed below under **COMPUTATION, NOT A
CLEARANCE** (operator rule 3); they are not a verdict and carry no entry language.

## Q8 — BETTER THAN THE ALTERNATIVES. STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US. WEIGHING.
NOT REACHED. Debt facts are under AFTER THE STOP.

## Q10 — THE FAT PITCH. WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2** (a standing castle that protects only ordinary returns over the full cycle: the deciding offshore segment
earned about 12% pre-tax on its assets less goodwill over 2014 to 2025 before corporate costs and about 8% after a share of
them, low single digits from 2017 to 2022; the company lost money at the operating line in eight of eleven years; the named
rivals NOV, Baker Hughes and Tenaris earned ordinary returns or less; the filer itself states "relatively few barriers to
entry" and bid-basis pricing); integrity facts recorded, not judged. COMPUTATION beneath the stop: value $5.95 to $13.69 a
share all-equity against $7.94; fair price $5.58 all-equity ($4.68 equity-only); no case of the range earns the floor at
the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found ("write it down in the first 30 minutes" **[M1997-127]**); no verdict; the box unchanged (operator rule 2).

**Bearing on Q3 (capital).**
- Capital spending has run below depreciation and amortization every year from 2016 to 2025 (capex 29.7 / 35.2 / 88.0 /
  56.1 / 12.7 / 17.5 / 20.3 / 30.7 / 37.5 / 31.2 against D&A 118.7 / 107.7 / 123.5 / 123.3 / 98.5 / 80.7 / 67.3 / 60.8 /
  54.7 / 47.4, USD millions, XBRL series), while the land businesses were shrunk by exits; the filing gives no maintenance
  figure. 2025 offshore segment capex $17.6M against its D&A $15.2M (10-K FY2025, Note 13).
- The 2018 purchases: GEODynamics, about $615M in total ($295.4M cash net of cash acquired, 8.66M shares valued at $294.9M,
  a $25.0M note) and Falcon, together $379.7M of cash paid for businesses in 2018 (10-K FY2019, 0001121484-20-000042;
  XBRL `PaymentsToAcquireBusinessesNetOfCashAcquired`). By the framework's definition the GEODynamics deal is an
  acquisition (cash and note $320.4M against shares $294.9M; the larger part cash). Goodwill impairments in its segment of
  $165.0M (2019) and $192.5M (2020), the 2024 transferred goodwill of $10.0M impaired, and $112.7M of long-lived and
  inventory impairments in 2025.

**Bearing on Q4 (the accounts).**
- Impairment charges in six of the seven years 2019 to 2025 (none found for 2022): goodwill 2019, 2020, 2024; long-lived
  and other 2019, 2020, 2021, 2023, 2024, 2025; inventory 2020, 2021, 2025 (XBRL series and the segment notes cited
  above); restructuring and facility-exit charges in 2020 to 2025. A "one-time" charge that recurs.
- The earnings release for the quarter to 2026-06-30 leads with "Adjusted EBITDA (a non-GAAP measure(1)) of $19 million
  rose 14% from the prior quarter" (8-K filed 2026-07-30, accession 0001121484-26-000031, Exhibit 99.1); the chief
  executive's quotation in it says "Adjusted EBITDA was in line with our expectations". The 2025 stock-based performance
  award is set on "a predefined cumulative EBITDA target" (DEF 14A, 0001121484-26-000017). The credit agreement's
  covenants are set on "Consolidated EBITDA", which excludes impairments and stock-based compensation (10-Q,
  0001121484-26-000033, Note 4). Under the framework these are recorded at Q4 as a weighing and carried to Q5; not weighed
  here.
- Auditor: Ernst & Young dismissed and Deloitte engaged on 2025-02-27; the 8-K states no disagreements and no reportable
  events, and EY's reports for 2023 and 2024 were unqualified (8-K filed 2025-03-04, accession 0001121484-25-000035).
- Receivables rose from 23% of revenue (2019) to 30% (2025); inventory from 22% to 27% (Step 0 table).

**Bearing on Q5 (the people; integrity facts recorded, not judged).**
- The adjusted-EBITDA lead and EBITDA-based pay above.
- Pay: the chief executive in 2025, Cindy B. Taylor, received total compensation of $5,079,386, including $1,654,244 of
  non-equity incentive pay (up from $1,141,473 in 2024), in a year of a $109.4M net loss (DEF 14A, Summary Compensation
  Table, 0001121484-26-000017; 10-K FY2025).
- Succession: Ms. Taylor retired as chief executive effective 2026-05-01; Lloyd A. Hajdik, formerly chief financial
  officer, is President and CEO; on 2026-07-09 his executive agreement was amended to restructure severance, including a
  lump sum of 3.0 times salary plus target bonus on a qualifying termination within 24 months after a change of control
  (8-K filed 2026-07-13, accession 0001121484-26-000029).

**Bearing on Q6 (the money and the owners).**
- Buybacks and their prices: 3.3M shares for $16.6M in 2025, about $5.03 a share (10-K FY2025, Item 1); 583,541 shares for
  $5.1M in the first half of 2026, about $8.74 a share; $19.6M of the $50M authorization left at 2026-06-30, expiring
  October 2026 (10-Q, 0001121484-26-000033, Note 6); $14.2M in 2024 and $6.9M in 2023 (XBRL). Against the COMPUTATION
  below (bottom of range $5.95 all-equity), the 2025 average price sits below the bottom and the 2026 average above it.
  Recorded, not weighed (Q6 was not reached).
- Shares issued: 8.66M shares at $34.05 for GEODynamics in 2018; 529,428 shares to retire the 2026 notes on 2026-04-01.
- No dividend.

**Bearing on Q9 (debt).**
- Debt at 2026-06-30: revolver $16.4M carried (net of $2.2M deferred costs), other debt and finance leases $2.0M; cash
  $19.8M. At 2026-07-28: $6.2M revolver and $20.0M term loan drawn, $15.9M of letters of credit, $52.9M available; the
  term-loan commitment lapsed on 2026-07-28. Covenants: interest cover at least 3.0 times and net leverage no more than 2.5
  times "Consolidated EBITDA" (10-Q, Note 4). The 2026 convertible notes ($135.0M issued 2021) were bought back in part in
  2025 ($70.8M principal) and retired on 2026-04-01.

---
## COMPUTATION, NOT A CLEARANCE
*The file closed at Q2. These figures are arithmetic for the owner's two reporting figures (Part VII, The owner's price;
How the fair price is computed). They are not a verdict and carry no entry language (operator rule 3). Every input is in
Step 0; the arithmetic is `Test Runs/_research 2026-10-16 OIS/q7calc.py`.*

**Built by Q7's range convention, specifics applied in order.**
- **Floor and rate.** Sovereign 5.43% (USD 30-year, Treasury, 2026-10-15); floor about ten percent (Q7 CONVENTION),
  applied to owner cash after the company's own tax as paid (Q7, Whose tax). The company paid little cash tax over the
  span because it lost money; no carryforward or credit is being used up that runs out inside ten years and is priced
  separately (the 10-K FY2025 records valuation allowances on U.S. deferred tax assets), so no shelter is added.
- **(a) Cycles.** The first year of the literal window, 2021, is the trough: revenue $573.2M, the lowest in the record, with
  restructuring the filer ties to the pandemic ("During 2021, the Company continued its restructuring efforts which began
  in 2020 due to the COVID-19 pandemic", 10-K FY2023, 0001121484-24-000021, Note 4). The base is the last full cycle,
  trough to trough on revenue, 2017 ($670.6M) to 2021 ($573.2M), inclusive. The literal window 2021 to 2025 is shown beside.
- **(c) Acquisitions.** Cash paid for businesses 2017 to 2021: $392.6M (GEODynamics and Falcon in 2018, $12.9M in 2017),
  against owner cash before purchases of $187.8M over the five years: net purchases exceed half of owner cash before
  purchases, so by the serial-acquirer convention the central figure is the organic pair (purchases left out, growth on
  the business as it stood). The default pair (purchases deducted) is beside: owner cash of minus $41.0M a year, no
  positive value.
- **(b) Decline.** Owner cash averaged $37.6M a year over 2017 to 2021 (organic) and $22.6M a year over 2022 to 2025: a
  decline of about 10.7% a year between the two averages (midpoints mid-2019 and mid-2023). The decline is carried as the
  bottom of the range; the no-growth case is the top.
- **(d) Working capital** is inside operating cash flow throughout. 2020's figure includes a $36.8M net tax refund and a
  receivables release; were the refund taken out, the cycle base would fall by about $7.4M a year.
- **(e) Growth spending.** The filing gives no maintenance figure; capital spending ran below depreciation every year, so
  the all-spending case is used, with the depreciation-basis owner cash beside: minus $27.3M a year over 2017 to 2021 and
  minus $20.3M a year over 2021 to 2025 (no positive value on that basis).
- **(f) The cap.** Not engaged: no positive growth is carried.
- **Basis.** All-equity central (owner cash before interest: cash interest paid added back, $7.3M a year over 2017 to 2021,
  with no tax effect because the U.S. operations carry losses under a valuation allowance; a CONVENTION of this
  computation, rationale: interest that saves no tax is added back whole), against market value plus net debt. Net debt at
  2026-06-30: revolver principal about $18.6M plus other debt and finance leases $2.0M less cash $19.8M = $0.8M; operating
  leases left out. The 10-Q states borrowings of $26.2M at 2026-07-28 but not the cash at that date, so that event is not
  added; were it added with cash unchanged, the per-share figures would fall by about $0.13. Equity-only beside.

**The range (zero nominal growth after year ten, discounted at 5.43%), per share on 60.32M shares:**

| case | owner cash a year | value | per share, all-equity | per share, equity-only |
|---|---|---|---|---|
| top: cycle base 2017 to 2021, no growth | $44.9M all-equity / $37.6M equity-only | $826M / $692M | **$13.69** | $11.47 |
| bottom: same base, declining 10.7% a year for ten years | $44.9M / $37.6M at the start | $360M / $301M | **$5.95** | $4.99 |
| beside: literal window 2021 to 2025, no growth (the series changes sign, so no growth rate) | $21.9M / $14.5M | $404M / $266M | $6.68 | $4.41 |

- **The floor tested first.** Expected return at $7.94: top case 9.4%, bottom case 3.8%, literal window 4.6% (all-equity);
  7.8%, 3.1% and 3.0% equity-only. **No case earns the floor of about ten percent at the price**; the top case comes
  nearest and rests on a base that includes the 2020 tax refund. Were Q7 reached, it would close OUT on the floor,
  "there’s just a point at which we drop out of the game" **[M2003-149]**, before the width test.
- **Width.** Top over bottom about 2.3 to 1, under the three-to-one line.
- **VALUE RANGE (reporting figure): $5.95 to $13.69 a share, all-equity, against $7.94.**
- **FAIR PRICE (reporting figure): $5.58 a share all-equity** (each end case valued at ten percent: $449M and $226M,
  averaged $337M, less $0.8M net debt); **$4.68 equity-only** beside. On the literal window alone the figure would be
  $3.62 all-equity. No cheap price is reported.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `b8088ab5`); written question by question; committed after Step 0
      and Q1 (`4056a2c0`), after Q2 (`f3596f13`), and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits of my two paths; the lock is the dispatching session's
      (I neither wrote nor read it); the fold is the dispatcher's. This run binds nothing until it is in the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One listing of `Test Runs/` file names
      dated 2026-10-1x was made before I set the listing aside, and the session context showed other runs' commit subjects
      and a memory index; all declared under Contamination at the head, none used.
- [x] Every v5 id cited is checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-16 OIS/check_ids.py`
      (no E-ids; every id present; every quoted fragment beside an id found in that row). Every filing fact carries its
      accession or its XBRL series and filer.
- [x] The order was kept: Q1 IN, Q2 OUT closed the file; Q3 to Q12 NOT REACHED; every figure after the stop is under
      AFTER THE STOP or COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (operating cash less stock pay less all capital spending), never a net-income
      proxy; the sovereign from the Treasury curve; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations; the Q2 tests); facts for later questions under AFTER THE
      STOP; the integrity flag is in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yields, implied growth and windows were not used as rules.
- [x] `python tools/check_framework.py` PASS before the final commit.

Honest limits of this run: the rivals' figures are XBRL transcription from their own filings, not read in their statements
(one cross-check was made on Oil States only); Baker Hughes' 2025 and Tenaris' pre-2016 figures were not tagged in the
series read; the offshore segment's composition changed in 2017 and 2024, so its series is not perfectly like for like;
the corporate-cost share is this run's convention; the land segments' rivals are unnamed in the 10-K and were not
compared; the proxy was read only for the facts listed.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Ordinary returns of the deciding part, before or after corporate costs.** The business-of-parts paragraph measures
"five-year operating profit" by part, and section C judges "the field's returns" in words, but neither says whether a
part's return is read before or after the costs the filer keeps at the centre. Here it moves the offshore segment from
about 12% to about 8% pre-tax over the cycle, and a reader could call the first figure not ordinary. I showed both and
judged on the cycle's shape (low single digits for six straight years, high only at the peaks) and on the rivals; a rule
is needed. (2) **Which full cycle.** Section C says "a full cycle" and Q7 (a) says "peak to peak, or trough to trough",
but neither says which series defines it at Q2 (revenue, operating income, owner cash), and for this filer owner cash runs
against the cycle (working capital is released in downturns), so revenue and owner cash give different cycles. I used
revenue for the cycle at Q7 and the whole 2014 to 2025 span at Q2, and said so. (3) **The serial-acquirer test on a window
with one large deal.** The convention triggers on net purchases above half of owner cash before purchases over the window;
one 2018 purchase triggers it for a company that has made no other material purchase since, which is not what "serial"
describes. I applied it as written. (4) **The number of rivals.** The brief and the template say "up to three that file
with the SEC"; the 10-K names five for one segment and none for the other two, which carry most of the losses; the
framework does not say what stands in for a named rival where the filer names none.
