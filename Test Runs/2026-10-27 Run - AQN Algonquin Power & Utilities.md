# Company Run — Algonquin Power & Utilities Corp. (NYSE and TSX: AQN) — 2026-10-27
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED.

*Dispatched blind run. Copied from the template and committed at 999f4088 on 2026-10-27 before any fetch; that session was
ended by a usage limit with no section filled. Resumed 2026-10-28 from the research folder (framework notes, helper scripts
and the cached filings), without refetching what was cached; the framework was read again in full. The file keeps its name
and date. Price and sovereign are those of 2026-10-27, the last close and curve available on the resume.*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the
dispatching session at the fold, 2026-10-28: the operator does not hold this name (`PORTFOLIO.md` has no AQN or Algonquin row).*

**Contamination, declared.** Seen by accident and not used: the session context's git status (file names under another
company's research folder and daily digest file names), five recent commit subjects about another company's run, and the
memory index lines on queue state (counts, no names). Nothing about this company or any former name of it was seen. No other
run file, research pass, holding review, `PORTFOLIO.md` or blind-listed Screens file was opened, listed or searched; the only
directory listings made were of this run's own research folder.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $5.42 (NYSE close 2026-10-27; Yahoo chart feed via `tools/sources.py` `price()`; **aggregator, flagged**, live quote only, operator rule 5).
- **Shares by class:** one class of common shares. Cover of the 40-F for FY2025: 768,351,419 (filed 2026-03-06, accession
  `0001174169-26-000015`; `python Screens/cover_shares.py AQN`). Checked against the latest interim report: 769,747,684 common
  shares outstanding at 2026-06-30 (Q2 2026 interim statements, note 9(a), 6-K filed 2026-08-07, accession
  `0001174169-26-000031`; the note's opening balance, 768,351,419, matches the cover). No treasury shares are reported. The only
  later 6-K (2026-08-28, accession `0001174169-26-000038`, the Suralis sale) issues no shares; the Q2 2026 MD&A (same 6-K, exhibit 99.2,
  Equity) states 769,901,895 issued and outstanding at 2026-08-06, the latest filed count. The count used is **769,901,895**.
  Not added: 6,591,551 PSUs and RSUs outstanding (0.86% of the shares; management information circular dated 2026-05-19, 6-K
  accession `0001140361-26-022268`, exhibit 99.4). Preferred shares Series A and D ($184.3M book) are a senior claim, not common.
- **Market cap:** $5.42 × 769.90M = **$4,173M**.
- **Sovereign for the earnings currency:** the statements are in US dollars and the earnings are mainly American (2025 revenue
  in the United States $1,955.7M of $2,433.6M, note 19). **US Treasury daily par yield curve, 30-year: 5.30%, 2026-10-27**
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 40-F for FY2025 (filed 2026-03-06, accession `0001174169-26-000015`): the audited
  statements (`aqunf-20251231.htm`), the Annual Information Form (exhibit 99.1) and the MD&A (exhibit 99.3); the Q2 2026 interim
  report (6-K 2026-08-07, accession `0001174169-26-000031`: statements and MD&A, exhibit 99.2); the management information
  circular dated 2026-05-19 (6-K 2026-05-20, accession `0001140361-26-022268`, exhibit 99.4); the 6-Ks of 2026-04-08
  (`0001140361-26-013837`), 2026-05-13 (`0001140361-26-020883`, the $1.15B notes), 2026-06-29 (`0001140361-26-026756`, meeting
  results) and 2026-08-28 (`0001174169-26-000038`, Suralis); for the last cycle and the balance sheets, the audited statements
  in the 40-Fs for FY2023 (`0001174169-24-000019`), FY2021 (`0001174169-22-000021`), FY2019 (`0001174169-20-000018`, exhibit
  99.2) and FY2017 (`0001628280-18-002905`, exhibit 99.2; **stated in Canadian dollars**). **The lines of evidence (the brief's
  one stated departure):** derived by this run from the AIF's description of the business (the 10-K Item 1 equivalent), the
  AIF's risk factors (Item 1A) and exhibit 99.3, the MD&A (Item 7). The Q1 2026 interim report (6-K 2026-05-08,
  `0001174169-26-000020`) was listed and not read; the Q2 report's six-month figures cover it.
  **One figure cross-checked:** cash from operating activities 2025, $593.6M on the filed cash flow statement; the MD&A states
  that it "increased by $111.9 million" over 2024's $481.7M (481.7 + 111.9 = 593.6). The cover share count was checked against note 9(a).
- **`python tools/run.py AQN`:** failed: "AQN: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (the company facts
  carry the cash flow tags only to 2017). **Every figure in this run is taken from the filed statements**, said so here.
  The arithmetic lines below are this run's own, from the statements ($M):

| Year | Cash from operations | Additions to PP&E (cash) | Depreciation and amortization | Stock pay (non-cash, added back in operations) | Acquisitions, cash | Divestiture proceeds | Accession |
|---|---|---|---|---|---|---|---|
| 2021 | 157.5 | 1,345.0 | 403.0 | 8.4 | 0 | 0 | 0001174169-22-000021 |
| 2022 | 619.1 | 1,089.0 | 455.5 | 10.9 | 632.8 | 0 | 0001174169-24-000019 |
| 2023 | 628.0 | 1,026.2 | 467.0 | 10.4 | 0 | 0 | 0001174169-24-000019 |
| 2024 | 481.7 (discontinued 121.3) | 872.4 | 476.7 (discontinued 81.0) | 18.4 | 0 | 1,106.7 | 0001174169-26-000015 |
| 2025 | 593.6 | 771.9 | 400.3 | 13.0 | 0 | 1,957.2 net of costs | 0001174169-26-000015 |
| H1 2026 | 322.1 (H1 2025: 326.4) | 284.5 | 214.2 | 4.2 | 0 | 0 | 0001174169-26-000031 |

  **Stock pay** is added back inside cash from operations; this run does not deduct it again, so owner cash below overstates by
  about $13M a year (said so; immaterial to the box, and it makes every case more favourable to the name). Increases in
  long-term investments (Atlantica and renewable joint ventures: 622.3, 221.3, 243.7, 115.0, 4.9) are outside the table.
  **Literal five-year window (2021 to 2025):** cash from operations averages $496.0M; additions to PP&E average $1,020.9M;
  depreciation averages $440.5M. Owner cash after all capital spending, after interest and the company's tax, is negative in
  every year (average **-$524.9M**, before preferred dividends). The window includes the renewable energy business sold on
  2025-01-08 and the Atlantica stake sold in December 2024; how the base is built for the business as now owned is at Q7.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own these utilities "if the market closed for five years" **[M1997-109]**, which turns
on the cash they produce after the capital they consume, not on the quote. The market serves and does not instruct **[M2006-077]**: the circular records a
TSX close of C$8.44 at 2025-12-31 and the stock now trades at $5.42 in New York; the fall says nothing by itself about value. Who is paid to tell you: the
company features a non-GAAP "Adjusted Net Earnings per common share", gives a yearly outlook (MD&A, Financial Outlook) and pays its executives on that
figure (circular); the outlook is the seller's projection and is not used. No macro forecast enters: the rate is today's curve. **Contrary evidence,
written down as found** **[M1997-127]**: (1) owner cash after capital spending is negative in each of the last five years; (2) two state regulators moved to
dismiss rate cases over the reliability of the company's financial data and over billing (New Hampshire, 2023 to 2025; Missouri, 2025); (3) a gas explosion
at Lexington, Missouri on 2025-04-09 killed a minor; (4) the share count rose from 274.1M (2016 cover) to 769.7M; (5) the deficit widened from C$556.0M
(2016) to $2,961.3M (2025). Each is carried to the question it bears on.

## THE STANDING RULE
A part-interest bought for cash, unlevered, and sized so that a fall of half or more can be sat through, "to have it go down 50 percent" **[M2020-022]**,
carries no ruin to the buyer. The rule is the buyer's conduct, "never going to risk what we have and need" **[M2012-081]**, and borrowed money to own it is
excluded: "borrowed money has no place" **[L2014-005]**. The target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What it is (AIF and note 19, accession `0001174169-26-000015`).** After the sale of the renewable energy business (excluding hydro) on 2025-01-08 and
  of the Atlantica stake in December 2024, AQN is a holding company of cost-of-service regulated utilities: the Regulated Services Group (about 1,272,000
  customer connections; electric in Arkansas, California, Kansas, Missouri, Nevada, New Hampshire, Oklahoma and Bermuda; water and wastewater in Arizona,
  Arkansas, California, Illinois, Missouri, New York, Texas and Chile; gas in Georgia, Illinois, Iowa, Massachusetts, Missouri, New Hampshire, New York
  and New Brunswick), 14 Canadian hydro plants (about 104 MW net), and a Corporate Group that carries the corporate debt. The AIF says the utilities "have
  geographic monopolies in their service territories" and set rates "under a cost-of-service methodology".
- **The parts (Q1's holding-company paragraph, at Q2's threshold).** 2025 operating income: Regulated Services $508.6M, Hydro $19.2M, Corporate -$23.1M
  (note 19). Regulated Services carries far more than half and decides. Within it the largest utility is Empire District Electric (Missouri, Kansas,
  Oklahoma, Arkansas); no utility-by-utility profit is filed.
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The key variables **[M1998-044]** of a cost-of-service utility are two: the
  rate base (the capital the regulators let it earn on) and the return it actually earns on that base against the return allowed. The first is foreseeable
  from the capital plan and the filed rate cases ("utility capital expenditures of approximately $3.2 billion expected for 2026 through 2028", MD&A). The
  second is the variable the filings show moving: the allowed equity returns stated in the 2025 MD&A run from 9.3% (New England Natural Gas, settled) to
  10% (CalPeco's current authorized ROE; Empire's request), on equity ratios of 47.1% debt / 52.9% equity to 62% equity, while earnings to common
  shareholders were $255.9M (2021), -$220.7M (2022), $20.3M (2023), -$1,391.0M (2024) and $170.3M (2025). The gap is explained in the filings by named
  causes (regulatory lag, the billing system, the sold businesses and their write-downs), so it can be read; whether it closes is a question for Q2 and Q3,
  not a failure to understand.
- **Abroad** **[M2000-141]**: incorporated under the Canada Business Corporations Act, with the stated intention to redomicile to the United States (Q2 2026
  MD&A, approval sought in the first half of 2027). Bermuda (BELCO, 62% equity ratio and 9.38% ROE authorized for 2026 to 2027, MD&A) and Chile (Suralis,
  under an agreement to sell) are small and do not decide; their tax treatment is stated in note 16 (Bermuda substance-based tax credits; the Pillar Two safe
  harbour). The rows ask a lower price, not a pass, for a less familiar country: "We wanted to get paid more for going into China" **[M2006-021]**.
- **Do I doubt it is inside?** "if you have doubts about something being into your circle of competence" **[M2002-092]**. The
  deciding part is a set of American rate-regulated monopolies whose economics are set in public dockets; the decision can be made "off the figures"
  **[M2008-069]**. No doubt about the circle; the doubts are about the returns, which belong to later questions.
- **VERDICT: IN.** A rate-regulated distribution utility, read from its rate cases and statements **[M2012-065]**, **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question is "why is that castle still standing" **[M1995-038]**, asked from the attacker's side.

- **The parts table** (note 19 of each 40-F; five-year operating income 2021 to 2025, $M; the business as now owned):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year share | Castle | Decides |
|---|---|---|---|---|---|---|---|---|
| Regulated Services Group | 399.5 | 459.3 | 471.2 | 440.1 | 508.6 | well over half of every year | regulated geographic monopolies | **yes** |
| Hydro Group (inside Renewables until 2024) | n/a | n/a | n/a | 20.2 | 19.2 | about 4% of 2024 to 2025 | small hydro under water rights and contracts | no |
| Renewable Energy Group (sold 2025-01-08) | 24.9 | -36.1 | 11.6 | discontinued | sold | negative to small | merchant and contracted generation | not owned |
| Corporate | -5.2 | -21.2 | -16.9 | -14.2 | -23.1 | cost | none | no |

  Regulated Services carries more than half of the five-year operating profit and decides (Q2, a business of parts). Hydro
  does not decide and is carried to Q7 as an ordinary business at no growth.
- **1. The castle questions.** The AIF: the utilities "have geographic monopolies in their service territories"; competition
  at the electric systems "is primarily from other energy sources and on-site generation", and at the gas systems "with other
  methods of heating, including electricity, oil, and propane". The reason the customer comes is that there is no other wire,
  main or pipe; the reason it lasts is the franchise and the commission, not the management.
- **2. Without the lord.** A cost-of-service franchise does not need a superstar; it needs a management that can file
  reliable numbers and bill correctly, which is exactly where this one has failed (below). That is a weight on the return
  (Q3, Q5), not a breach in the franchise.
- **3. The money test** **[M2011-015]**: "could I do it?" No: a rival cannot build a second distribution grid in Joplin or a
  second water system in Litchfield Park. One taking is on the record: the Town of Apple Valley's condemnation of the Apple
  Valley water system (note 20(a)(ii)): the Court of Appeal on 2025-01-15 reversed the finding that the Town had no right to
  take it; the California Supreme Court granted review on 2025-04-23 and the matter is pending. The AIF's risk factors say
  the systems "could be subject to condemnation or other methods of taking by government entities". The attacker here is
  the government, not a competitor, and it pays a price for what it takes.
- **4. Pricing power and the agony before a rise** **[M2005-020]**: "the agony they go through in determining whether a price
  increase can be sustained". For a regulated utility every rise is a public proceeding, and the filings show the agony in
  full (MD&A, Regulatory Proceedings): Granite State Electric asked $15.5M and received $5.5M after the New Hampshire
  Department of Energy moved to dismiss the case and the commission ordered an independent audit of the company's financial
  information; EnergyNorth Gas asked $27.5M and settled at the $8.7M of temporary rates, after the same motion; Empire District
  Electric's case (final position $168M) drew motions to dismiss from the Missouri commission staff and the Public Counsel in
  February 2025, and ended at $97M "phased in over 3 years once the performance metrics have been met for three consecutive
  months", the Public Counsel having recommended no increase "citing ongoing billing issues"; Midstates Gas asked $13.2M and
  got $9.1M; BELCO's 2026 revenue was cut by $3.6M. The price is the regulator's, which is the nature of the castle.
- **5 to 8. Volume, low cost, brand, the low bid.** Not the tests for a franchise monopoly: the customer has no low bid to
  take. Volume (MD&A): electric sales 6,714.4 GWh in 2025 against 6,644.2 in 2024; gas customer connections flat at about
  363,000; water connections up about 1%.
- **9. Ask the competitors.** The filing names no rival companies (a text search of the AIF for "compet" finds only the
  substitute-energy sentences above and generic risk language). **CONVENTION of this run:** the comparison set is three
  American multi-state rate-regulated utilities that file with the SEC and share regulators or terrain with the deciding part:
  Evergy (Missouri and Kansas, beside Empire), Ameren (the Missouri commission) and Black Hills (small multi-state electric and
  gas, a similar size). Rationale: the brief asks for rivals from their own filings, the filer names none, and a franchise
  monopoly's "rivals" are the peers its regulators compare it with.

  **The competitor row** (operating income over year-end net PP&E, and net earnings over year-end equity; each company's
  10-K figures from the SEC company facts, the latest-filed value per year; AQN from its own note 19 and statements):

| Company | Metric | 2021 | 2022 | 2023 | 2024 | 2025 | Accession (latest 10-K or 40-F used) |
|---|---|---|---|---|---|---|---|
| AQN Regulated Services | operating income / segment net PP&E | 5.4% | 5.4% | 5.3% | 4.7% | 5.3% | 0001174169-26-000015, -24-000019, -22-000021 |
| AQN consolidated | earnings to common / common equity | 4.5% | -4.4% | 0.4% | -30.7% | 3.8% | same |
| Evergy | operating income / net PP&E | 6.5% | 5.7% | 5.4% | 5.9% | 5.8% | 0001711269-26-000017 (2023 to 2025), -25-000004, -24-000007 |
| Evergy | net income / equity | 9.5% | 7.9% | 7.6% | 8.8% | 8.4% | same |
| Ameren | operating income / net PP&E | 4.6% | 4.8% | 4.6% | 4.2% | 5.2% | 0001002910-26-000009, -25-000055, -24-000056 |
| Ameren | earnings to common / equity | 10.2% | 10.2% | 10.2% | 9.8% | 10.9% | same |
| Black Hills | operating income / net PP&E | 6.3% | 6.7% | 6.6% | 6.6% | 6.5% | 0001193125-26-046028, 0000950170-25-018647, 0000950170-24-015090 |
| Black Hills | net income / equity | 8.5% | 8.6% | 8.1% | 7.8% | 7.6% | same |

  The operating return of AQN's utilities on their plant sits inside the peers' band (below Evergy and Black Hills, above
  Ameren). What does not sit inside it is what reaches the common owner: the peers earned 7.6% to 10.9% on equity in every
  year; AQN earned at most 4.5%, and lost money in two of the five years. Part of the gap is the sold businesses and their
  write-downs (2024's $1,357.3M impairment, note 23(b)); part is in the continuing business (2025 continuing earnings to
  common $208.0M on common equity of $4,456.8M, 4.7%, of which $76.4M is HLBV income allocated from tax-equity partners, Q4).
- **10. Widening or narrowing** **[M1999-108]**: "how wide the moat is" and which way it moves. The franchise is not narrowing;
  the return the regulators allow it to collect is, for now, being held back by its own service failures (Empire's increase
  is conditioned on billing metrics; New Hampshire's on audited data). That is a moat being taxed by its keeper's conduct, and
  it bears on Q3 and Q5.
- **11. What could destroy, modify or reduce it** **[M2000-014]**: "destroy, or modify, or reduce the economic strengths".
  (a) The regulatory climate, the row's own mistake: "it is difficult to project both earnings and asset values"
  **[L2023-011]**; here shown in four states' dockets. (b) Wildfire in California (Mountain View Fire, 2020: losses accrued
  $178.4M against insurance of $116.0M and a regulatory memorandum account of $71.5M, recovery applied for, one lawsuit
  pending, note 20). (c) Gas safety (Lexington, Missouri, 2025-04-09: a minor died; $152.2M accrued against $149.0M of
  insurance recoveries; the Missouri Attorney General's petition and a commission investigative docket opened 2025-10-09,
  note 20). (d) Electrification and policy against natural gas (AIF). (e) Condemnation (Apple Valley). None of these is shown
  on the evidence to be filling the franchise in; each is a reduction of the return, or a loss to be weighed at Q9.
- **The field's returns over the last full cycle.** The peers' own filings show the field earning regulated returns of about
  8% to 11% on equity through 2021 to 2025, a span that includes the 2022 to 2023 rise in rates and costs. Those are ordinary
  returns, protected by a castle that stands; Q2's list sends that to OUT except that "A return set by a regulator is the
  exception, carried to Q3 as a second best" (Q2, What it rules OUT), on the rows "no way we get rich on our utility
  investments" **[M2009-104]** and "decent returns on the incremental sums they invest" **[L2009-012]**. The deciding part earns
  "an allowed return" set by commissions **[M2010-037]**, so the exception applies and the return is carried to Q3, where AQN's
  shortfall against its own allowed returns and its peers is weighed.
- **VERDICT: IN.** The franchise castles of the deciding part stand **[M2011-015]**; the return is regulator-set and is carried
  to Q3 as a second best **[M2009-104]**, **[L2009-012]**, with the regulatory climate carried to Q3 and Q9 **[L2023-011]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The capital-heavy business is admitted as a second best only on "decent returns on the incremental sums they invest" **[L2009-012]**;
"cash-consuming businesses, by their nature, are unattractive unless the cash they consume gets to earn a reasonable return" **[M2012-057]**.

- **1. What it earns on the capital it needs** **[M2010-090]** ("the capital actually needed in the business"). The deciding part's
  operating income over its own net PP&E was 5.4%, 5.4%, 5.3%, 4.7% and 5.3% in 2021 to 2025 (note 19), pre-tax and before
  interest; the peers earned 4.2% to 6.7% on the same measure (Q2 row). On the owners' equity the continuing business earned
  4.7% in 2025 ($208.0M continuing earnings to common, after preferred dividends, on $4,456.8M of common equity); on tangible
  common equity (less goodwill of $1,320.1M and intangibles of $69.7M) about 6.8%. The peers earned 7.6% to 10.9% on equity.
  The difference sits below the operating line: the Corporate Group's own interest ($140.2M in 2025, $170.9M in 2024, note 19)
  is a second layer of debt at the parent, on top of the utilities' own ($141.4M), and the continuing earnings include $76.4M
  of HLBV income allocated from tax-equity partners in the Empire wind farms (Q4).
- **2. Reinvestment to stand still, and to grow** **[L2000-035]**: "Every year we spend amounts equal to our depreciation charge
  simply to stay in the same economic place". The filer states its own maintenance figure (MD&A, Summary of Property, Plant and
  Equipment Expenditures): "Sustaining" capital, "Capital spend to support existing systems (e.g. asset replacements, safety &
  reliability projects)", was $610.5M in 2024 and $499.7M in 2025 at Regulated Services (plus Hydro $6.6M and $5.3M), against
  depreciation of $395.7M and $400.3M; "Growth" capital was $146.7M and $103.8M. Sustaining spending ran $105M to $221M a year
  above depreciation, the case the rows name: "spend more than its depreciation charge to simply maintain its present level
  of business" **[L2023-009]**. TTM to 2026-06-30: sustaining $483.3M, growth $123.6M (Q2 2026 MD&A). The plan is "approximately
  $3.2 billion expected for 2026 through 2028", about $1.07B a year against depreciation of about $410M.
- **3. The growth arithmetic** **[M2001-019]**: "whether that’s good or bad depends on what we earn on that incremental" capital.
  From 2021 to 2025 the deciding part's net PP&E rose $2,184.4M ($7,394.2M to $9,578.6M) and its operating income rose $109.1M
  ($399.5M to $508.6M): about 5.0% pre-tax on the added plant, about 3.7% after a 25% tax, before the interest on the debt that
  funded it. The added capital includes the 2022 acquisition paid in cash ($632.8M, "Acquisitions of operating entities").
  Rising earnings with no rise in the rate earned is the case narrated in **[M2023-081]**: "we’re not earning a higher rate of return
  on capital than we were when we started". Owner cash after all capital spending was negative in every year of the window
  (Step 0), so growth has been financed by borrowing, asset sales and share issuance, not by the business.
- **4. The capital-heavy business as second best.** The rows accept a utility at a fair return, "no way we get rich on our
  utility investments" **[M2009-104]**; this one has not been earning the fair return on what reaches the owner, and its
  incremental capital earns below its peers'.
- **WEIGHS AGAINST.** The capital it consumes has earned about 5% pre-tax at the operating line and under 5% for the common
  owner, short of the "reasonable return" the second best needs **[M2012-057]**, **[L2009-012]**, with maintenance spending above
  depreciation **[L2023-009]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them, before the income account** **[M2025-032]** ("balance sheets over an 8 or 10 year
  period before I even look at the income account"). From the filed statements (`tools/run.py` printed none); year-end, $M;
  **2016 and 2017 in Canadian dollars** as filed (FY2017 40-F exhibit 99.2), 2018 onward in US dollars:

| Year-end | Cash | Receivables | Net PP&E | Goodwill | Intangibles | Regulatory assets (current + long) | Long-term debt incl. current | Equity to shareholders | Deficit | Non-controlling interests | Common shares (stated capital) | Shares outstanding (cover) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 (C$) | 110.4 | 189.7 | 4,889.9 | 306.6 | 65.0 | n/r | 3,913.4 + C$358.6 convertibles | 1,923.6 | -556.0 | 562.4 | 1,972.2 | 274.1M |
| 2017 (C$) | 54.6 | 306.9 | 7,909.5 | 1,196.2 | 64.1 | n/r | 3,863.3 | 3,409.0 | -617.8 | 756.0 | 3,713.0 | 431.8M |
| 2018 | 46.8 | 245.7 | 6,393.6 | 954.3 | 55.0 | 401.1 (long) | 3,336.8 | 3,177.6 | -595.3 | 519.9 | 3,562.4 | 488.9M |
| 2019 | 62.5 | 259.1 | 7,231.7 | 1,031.7 | 47.6 | 509.7 (long) | 3,931.9 | 3,875.1 | -367.1 | 531.5 | 4,017.0 | 524.2M |
| 2020 | 101.6 | 324.8 | 8,241.8 | 1,208.4 | 114.9 | 846.5 | 4,538.5 | 5,203.6 | 45.8 | 458.6 (+327.2 redeemable) | 4,935.3 | 597.1M |
| 2021 | 125.2 | 403.4 | 11,042.4 | 1,201.2 | 105.1 | 1,167.6 | 6,211.4 | 5,859.0 | -288.4 | 1,523.1 (+319.5 redeemable) | 6,032.8 | n/r |
| 2022 | 57.6 | 528.1 | 11,944.9 | 1,320.6 | 96.7 | 1,271.5 | 7,512.0 | 5,219.6 | -997.9 | 1,616.8 (+319.4) | 6,183.9 | n/r |
| 2023 | 56.1 | 524.2 | 12,517.5 | 1,324.1 | 93.9 | 1,327.7 | 8,516.0 | 5,039.6 | -1,279.7 | 1,584.8 (+318.4) | 6,230.0 | n/r |
| 2024 | 34.8 | 422.6 | 9,450.1 (+3,219.8 held for sale) | 1,312.2 | 69.1 | 1,321.0 | 6,698.7 (+1,348.7 held for sale) | 4,707.9 | -2,929.9 | 1,468.3 | 7,391.3 | 767.3M (Q2 2026 note 9(a), opening 2025) |
| 2025 | 32.7 | 494.8 | 9,749.9 | 1,320.1 | 69.7 | 1,395.9 | 6,532.9 | 4,641.1 | -2,961.3 | 407.2 | 7,401.7 | 768.4M |
| 2026-06-30 | 55.0 | 359.8 | 9,782.9 | 1,317.5 | 71.8 | 1,416.9 | 6,635.7 | 4,620.9 | -2,974.4 | 356.3 | 7,409.0 | 769.7M |

  (n/r: not read in this run. Accessions: 0001628280-18-002905; 0001174169-20-000018; 0001174169-22-000021;
  0001174169-24-000019; 0001174169-26-000015; 0001174169-26-000031.)
  **What the figures say.** (1) **Issuance, not retention, built the company.** Stated common capital rose from C$1,972.2M to
  $7,409.0M and the shares from 274.1M to 769.7M, while equity to shareholders rose only from C$1,923.6M to $4,620.9M: the
  deficit widened from C$556.0M to $2,974.4M. Earnings to common over 2021 to 2025 summed to -$1,165.2M while cash dividends to
  common summed to $1,494.6M (cash flow statements): the dividends were paid from capital raised. (2) **Debt** grew from C$3.9B
  to $6.6B, and the debt-to-equity mix moved against the owner: long-term debt is now 1.4 times equity to shareholders
  (6,635.7 / 4,620.9), with $1.1B and C$400M of subordinated hybrid notes (due 2079 to 2082) at the parent. (3) **Goodwill**
  ($1.32B) is 28% of equity to shareholders and 30% of common equity (less the preferred shares at book); it came with the 2017 Empire
  acquisition (goodwill C$306.6M to C$1,196.2M that year) and later utility purchases. (4) **Regulatory assets** grew from
  $846.5M (2020) to $1,416.9M: deferred costs to be recovered from customers, of which $260.0M is the securitized cost of the
  February 2021 storm (note 6(a), bonds issued by Empire on 2024-01-30 for $301.5M); a deferral is a cost not yet collected, and
  its collection depends on the regulators of Q2. (5) **Receivables**: $494.8M at 2025 year-end on 2025 revenue of $2,433.6M, about 74 days; $359.8M at
  2026-06-30, lower by season; nothing out of line with sales. (6) **The 2024 write-down** of the renewables ($1,357.3M) is
  the balance sheet admitting that capital put into that business was worth much less than its cost. **What they cannot say**:
  the rate base by utility, which is not filed; the equity actually earning in each utility; what the regulators will allow.
- **The real costs.** Depreciation is real and here understated as a measure of maintenance: the filer's own sustaining capital
  exceeds it by $105M to $221M a year (Q3) **[L2015-004]** ("almost always true costs"). Stock pay ($13.0M in 2025) is charged
  in earnings. "Restructuring costs" described as "one-time costs related to the Company's ongoing simplification" appear two
  years running ($27.0M in 2024, $38.7M in 2025, note 17), plus "other miscellaneous write-downs"; they are recurring and are
  kept in owner cash. Deferred tax: the utility's deferred taxes are not "a hidden form of equity" **[M2015-030]**; owner cash
  takes the company's actual cash tax (a net refund of $73.4M in 2025, $56.7M in 2024, note: cash flow supplement), which flatters
  2025 and is shown at Q7. **HLBV income**: $76.4M of 2025 Regulated Services earnings is the "net effect of non-controlling
  interests", "primarily ... HLBV income from Empire Electric" (MD&A note 6 to the segment table), an allocation of the
  tax-equity partners' book losses to the common owner; it is not cash in the year, and owner cash (built from the cash flow
  statement) leaves it out.
- **EBITDA in the filer's mouth.** The company dropped "Adjusted EBITDA" and "Adjusted Funds from Operations" in 2025 ("these
  metrics were relevant mainly to the Company's former renewable energy group", MD&A); it now features "Adjusted Net Earnings"
  and "EBIT". No EBITDA talk in the current filings: not the count-to-zero case.
- **The tells** **[M1995-064]** ("accounting can offer you a lot of insight into the character of management"). (a) **The adjusted
  figure featured** **[L2016-006]**: "Adjusted Net Earnings per common share" leads the MD&A, its adjustments ($50.8M in 2025,
  $166.8M in 2024) include restructuring, litigation and "other typically non-recurring or unusual items", and the executives
  are paid on it (Q5, Q6). (b) **Guidance and beating it** **[L2019-006]**, **[L2002-041]**: the MD&A gives an outlook
  ($0.35 to $0.37 for 2026; $0.38 to $0.42 for 2027, cut from the earlier 2027 figure by "slightly more than $0.03" for tax) and
  reports that 2025's figure "exceeded the top end of Company’s previously provided guidance range by $0.02", "driven by
  accelerated realization of operating expense savings, lower depreciation expense resulting from authorized deferrals, and tax
  adjustments". Two of the three named drivers are accounting (a depreciation deferral and tax adjustments). (c) **Data
  reliability questioned by regulators**: in New Hampshire the Department of Energy moved to dismiss two rate cases and the
  commission rejected the company's third-party report and "ordered an independent audit facilitated by the DOE" (MD&A); the AIF's
  risk factors say "there is additional risk that financial data required for rate filings could be difficult to produce or the
  data is deemed unreliable for ratemaking purposes" after the systems update. Against these: the auditor (Ernst & Young, since
  2013) gives an unqualified opinion on the statements and on internal control at 2025-12-31, management concludes internal
  control effective, and no restatement is reported in the filings read.
- **Confusion or suspicion?** The statements can be read: the discontinued business is separated in note 23 with its cash flows,
  the cash statement reconciles to the MD&A, the segment table reconciles to the income statement. The questioned data are the
  regulatory filings' inputs after a systems change, settled in both New Hampshire cases; the regulators did not find the GAAP
  statements false. That is not "when the accounting confuses you" **[M1995-063]** at the level of the audited accounts, and no
  statement-level tell (reserves that move, profits that may not exist) was found. The habits (a) to (c) are a WEIGHING against
  **[M1994-018]** and are carried to Q5.
- **VERDICT on the accounts: WEIGHS AGAINST** (no STOP). The accounts can be read; owner cash is built from the cash flow statement,
  not from the featured figure; the adjusted figure, the beaten guidance and the regulators' doubts about data are carried to Q5
  **[L2016-006]**, **[L2019-006]**, **[M1994-018]**. The recast feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who they are** (circular dated 2026-05-19, chair's letter). The management is almost wholly new: Roderick West, Chief
  Executive Officer from 2025-03-07 (after an interim chief executive, Chris Huskilson, paid as CEO in 2023 to 2025); a new
  Chief Financial Officer (Robert Stefani) and Chief Operating Officer (Peter Norgeot) from 2026-01-05, after an interim CFO in
  2025; new regulatory, customer and human-resources chiefs. The record of 2016 to 2024 (the issuance, the renewables build
  and write-down, the systems change behind the billing and data problems) was made by people who have left. The new team's
  own record is about eighteen months.
- **The two yardsticks** **[M1994-008]**: "how well they run the business" against "the hand they were dealt", and "how well that
  they treat their owners". Running the business: the hand dealt in 2025 was a utility group with regulators doubting its data
  and billing; the record since is two contentious cases settled (EnergyNorth, Granite State), Empire's $97M settlement won
  but conditioned on billing and customer-service metrics, the CalPeco settlement (a proposed decision issued), the New England gas settlement, the
  redomicile announced, the Suralis sale agreed. Against: the Lexington explosion (2025-04-09, a minor killed; the Missouri Attorney
  General's petition and a commission safety docket, note 20). Treating owners: TSR of $100 invested at 2021-01-01 worth $53.27
  at 2025-12-31 against $210.84 for the S&P/TSX Composite (circular, performance graph); the dividend cut (cash dividends to
  common $378.6M in 2022, $201.3M in 2025).
- **The tells, read from the documents** (for a stock the speakers read rather than meet).
  (a) *The reports and the letter* **[M1998-036]**: the 40-F is candid about the bad news: the MD&A sets out the New Hampshire
  motions to dismiss, the independent audit, the Public Counsel's "ongoing billing issues", and the AIF warns that rate-filing
  data could be "deemed unreliable". That is the information an owner would want, and it counts for them. The circular is
  different: the chair's letter opens "2025 was a year marked by disciplined execution", and the circular (408,000 characters
  of text) does not name the Lexington explosion once; it appears only as "the overall safety context for the year", for
  which the board cut the scorecard by 15.1 points after the safety metric had "exceeded target". The customer-experience
  metric (SAP systems) also "exceeded target" in the year Missouri's increase was conditioned on billing metrics. That is the
  taboo the rows distrust: "mistake" or "wrong" as forbidden words, "That taboo, implying managerial perfection, always made me
  nervous" **[L2024-003]**.
  (b) *The habits carried from Q4*: the adjusted figure featured **[L2016-006]**, the outlook given each year and 2025's beat
  "by $0.02" with a depreciation deferral and tax adjustments among the drivers **[L2002-041]**, **[L2019-006]**.
  (c) *Bad news told*: the 40-F tells it at once, as **[M1998-039]** asks ("tell us the bad news immediately"); the dividend cut
  and the strategic sale were announced and executed.
  (d) *No instance found* in the filings read (the 40-F, its AIF and MD&A, the Q2 2026 report, the circular, the 2026 6-Ks)
  of a restatement, a regulator's finding of falsity, a securities fraud claim (a text search for "class action" across the
  AIF, the MD&A and both sets of statements found none), or self-dealing.
- **Integrity, the STOP** **[M2013-088]** ("If you’ve got doubts, forget it"). The doubt this file holds is about tone and
  incentive, not truthfulness: the pay document softens a fatal year; the featured figure and the beaten guidance are habits
  the rows distrust. The public record of what happened (the 40-F) is complete and plain, the auditor's opinions are clean, and
  the people who built the troubled record have been replaced. Read together, the record does not show the people to be
  dishonest; it shows a management whose public tone is managed. This is the closest call in the file before Q7, and it is
  recorded as such for any later run that reaches this question again.
- **Love of the business; ability.** No owner-founder; the chief executive holds 71,415 shares (about $0.4M at $5.42) against
  a guideline of seven times salary, $8,750,000, which he has time to meet (circular). Ability is shown so far in settlements
  reached and assets sold, not yet in the return earned (Q3), and the business is one that needs management to file and bill
  correctly, so it weighs: "the number one risk factor is that this business gets the wrong management" **[M2021-042]**.
- **VERDICT on integrity: IN** (no dishonesty shown; the doubts stated are about candour of tone and incentives, and are
  carried, not dismissed) **[M1998-036]**, **[L2024-003]**, **[M2013-088]**. **Ability WEIGHS AGAINST**: a new team without a
  record of earning the allowed return, in a business whose return depends on it **[M1994-008]**, **[M2021-042]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test.** The check "after three or four years" **[M1998-110]**, and "at least $1 of market value for each $1
  retained" tested "on a five-year rolling basis" **[R1995-009]**. Over 2021 to 2025 the company retained nothing: earnings to common summed to
  -$1,165.2M and cash dividends to common to $1,494.6M (Q4). The capital came from owners and lenders instead: common stated
  capital rose $1,368.9M (end-2021 to end-2025, Q4 table) and long-term debt rose from $4,538.5M (2020) to $6,532.9M (2025) after
  $1,374.8M was repaid from the renewables sale. On the market leg, $100 invested on 2021-01-01 with dividends reinvested was
  worth $53.27 at 2025-12-31 (circular). Capital put to work over the cycle lost value for the owners, at the market and at
  book (the $1,357.3M write-down, note 23). Fails, on both legs.
- **Buybacks.** No repurchase of common shares in 2021 to 2025 or in H1 2026 (no instance in the five cash flow statements or
  the Q2 2026 statement; the only share purchases are "Shares surrendered to fund withholding taxes"). *Written back from Q7:*
  with no repurchases there are no prices paid to set against the bottom of the Q7 range (central -$3.70 a share; the most
  favourable variant's bottom $4.48 at the sovereign); the test is empty, and weighs neither way.
- **Issuance and deals** **[R1995-010]** ("only when we receive as much in business value as we give"). The shares rose from
  274.1M (2016) to 769.7M: 431.8M in 2017 (the Empire acquisition, funded by subscription receipts), then steady issuance through
  the dividend reinvestment plan and offerings ($985.6M in 2021 alone, cash flow statement), and 77,293,314 shares in 2024 on
  settlement of the 2021 equity units ($1,150.0M, about $14.88 a share, statement of equity). That last issuance was at a price
  far above today's and above the 2024 market, so it gave less than it got; the earlier ones bought the renewables that were
  written down and the utilities that earn below their peers (Q3). The rows: "we have never invested in companies that are
  hell-bent on issuing shares" **[L2014-015]**; the framework carries serial issuance as a candidate second STOP, unresolved, and
  this run weighs it. Since the strategic review the issuance has stopped (2025: $0.8M; H1 2026: $1.3M), and the Suralis sale
  and the redomicile are cash and structure, not shares. **All-stock deal in undervalued stock:** none in the window (the 2022
  acquisition, $632.8M, was paid in cash); the STOP does not apply.
- **Dividends** **[L2012-015]** ("clear, consistent and rational"): the dividend was paid out of capital for years and then cut
  (cash dividends to common: $378.6M in 2022, $322.5M in 2023, $285.1M in 2024 with more shares, $201.3M in 2025; $0.065 a
  quarter now). A dividend funded by issuance and debt is the opposite of "earn more than it can profitably employ" **[M2004-089]**.
- **Part A WEIGHS AGAINST**: retention failed on both legs, and issuance built a business that earns below its peers
  **[R1995-009]**, **[L2014-015]**.

**Part B: the pay, the board and the owners.**
- **Pay** (circular): the short-term plan is 60% financial (Adjusted Net EPS and FFO) and 40% non-financial; the 2025 scorecard
  paid 145% of target, the Adjusted Net EPS leg "achieving stretch target", after the board's 15.1-point safety cut. Long-term
  awards were 50% RSUs and 50% PSUs in 2025 (PSUs on relative TSR among other measures; RSUs vest on time alone). The plan for
  share units was raised from 14,000,000 to 29,000,000 treasury shares (passed at the 2026 meeting). Pay on a featured adjusted
  figure the management itself defines is not "tying performance to what is actually under the reasonable control" of the person in a
  clean way **[M2003-019]**, and RSUs that pay at any price are the upside without the downside **[L1994-020]** ("a partner in both
  directions"). Say on pay passed with 96.94% (meeting results, 6-K 2026-06-29).
- **The board** changed its chief executive twice and most officers in three years, sold the business it had built and cut
  the dividend: it acted, which the rows ask of those who learn of a problem **[M2017-005]** ("they didn’t act" is the failure).
- **Owners as partners.** No buyback, no split; the information in the 40-F is full; earnings guidance is given **[L2019-006]**.
- **Part B WEIGHS AGAINST**: pay on the company's own adjusted earnings at 145% of target in a fatal year, with time-vested units
  **[M2003-019]**, **[L1994-020]**; the board's willingness to act is counted for it **[M2017-005]**.

## Q7 — WHAT IS IT WORTH? STOP.
"how much do you get back, how sure are you of getting it, when do you get it?" (Q7's opening row, **[M2009-004]**), at the long
government rate, as a range. The arithmetic is `q7.py` in the research folder; its full output, every case below, is `q7_out.txt`.

- **The basis.** The deciding part (Regulated Services) earns a return its regulators allow on its invested capital **[M2010-037]**
  ("when you get an allowed return in the electric utility"), so the regulated-utility paragraph applies: the debt dedicated
  to "the fixed-asset commitments at our regulated utilities" is the exception **[L2017-012]**. **Central: equity-only** (owner
  cash after interest and after the company's tax, against the market value of the common shares, $4,173M), with the
  long-term debt raised for the fixed assets credited against the growth spending; **all-equity beside**.
- **The base. CONVENTION of this run:** the five-year average cannot be taken on the business as now owned: the cash flow
  statements of 2021 to 2023 combine the renewable energy business (sold 2025-01-08) and the Atlantica dividends (stake sold
  December 2024) with the utilities, and no filing separates them; the FY2025 40-F presents two years on the continuing
  business (2024 restated, with the discontinued cash flows given in note 23(c): operating $121.3M, investing -$196.0M; 2025).
  The **central base is the average of those two fiscal years** (FY2024 continuing, FY2025), with **FY2025 alone** and the **TTM to
  2026-06-30** beside, and the **literal five-year window** beside. Rationale: the cash the buyer gets is the continuing
  business's, and "no single year sets the base" is best kept by the two full years the filer itself presents. 2024 continuing
  still carries about $76.3M of Atlantica dividends and about $81M more interest than 2025 (debt repaid from the sale
  proceeds); the two roughly offset and neither is adjusted, said so. Literal window: equity owner cash after depreciation
  $46.1M a year ($1.13 a share at the sovereign, no growth); after all capital spending -$534.3M a year.

| Base ($M) | Cash from operations | Sustaining capex (filer's) | Growth capex (filer's) | Depreciation | Preferred dividends | Interest paid |
|---|---|---|---|---|---|---|
| FY2024 continuing | 360.4 (481.7 less 121.3) | 617.1 | 146.7 | 395.7 | 10.5 | 377.3 (432.7 less 55.4 discontinued) |
| FY2025 | 593.6 | 505.0 | 103.8 | 400.3 | 10.5 | 312.1 |
| **Central: average** | **477.0** | **561.1** | **125.2** | **398.0** | **10.5** | **344.7** |
| TTM to 2026-06-30 | 589.3 | 488.6 | 123.6 | 412.2 | 10.5 | 299.1 |

  (Sustaining and growth capital from the MD&A tables, accrual basis, Hydro's $6.6M and $5.3M counted as sustaining; TTM Hydro
  taken at the 2025 figure, said so. Working capital is counted, inside cash from operations, specific (d). The company's own
  cash tax is used: a net refund of $73.4M in 2025, which flatters FY2025 and the TTM; Whose tax.)
- **Maintenance, specific (e).** The filing allows the guess: it states "Sustaining" capital as "Capital spend to support existing
  systems". **Central maintenance = the filer's sustaining capital**; depreciation as maintenance **[M1998-127]** is shown beside,
  and it is the more favourable to the name because sustaining runs above depreciation (Q3, **[L2023-009]**).
- **Growth shown, capped by Q3.** On the deciding part's operating income after depreciation (the measure **[M2014-086]** names:
  "It’s measured by the operating earnings after depreciation"), 2022 to 2025, after the 2022 acquisition closed: $459.3M to
  $508.6M, **3.5% a year (central, organic)**. Total growth 2021 to 2025, acquisition included: $399.5M to $508.6M, 6.2% a year,
  shown beside; specific (c): the acquisition ($632.8M in 2022) falls outside the two base years, so the base carries no
  acquisition spending and the organic rate is the one consistent with it. Neither rate runs past the discount rate; the cap of
  (f) does not bind (owner cash is far below any share of sales the business has earned). Carried ten years, then zero nominal growth.
- **Growth spending, specific (e), and the utility debt credit.** Growth spending (above the sustaining guess) $125.2M in the
  base, **$129.6M in year one and $176.6M in year ten** of the central growth case (grown at 3.5%), none after. Debt credit: the
  increase in long-term debt over 2021 to 2025, borrowings due after a year and their current maturities, with commercial
  paper, revolving and bank facilities left out, and the Empire securitized utility tariff bonds ($305.5M issued 2024-01-30,
  repaid from a dedicated customer charge, note 6(a)) left out with their charge: end-2020 $4,040.6M, end-2025 $6,112.9M, less
  $305.5M: **$353.4M a year**. Against growth spending only, **capped at 57.1%, the business's own long-term debt share of
  long-term capital at 2026-06-30** ($6,635.7M / ($6,635.7M + total equity $4,977.2M)); the filing states allowed equity
  ratios for single utilities (47.1% debt at New England Natural Gas, 38% at BELCO, about 47% asked at Empire) but no rate base
  by utility, so it cannot be shown that the stated shares cover half the deciding part's rate base, and the own-share rule
  applies (said so; excluding commercial paper the share would be 55.0%, lower). The cap binds: **credit $71.6M in the base,
  $74.1M in year one, $101.0M in year ten**, growing and stopping with the growth spending.
- **The range, central (equity-only, filer's sustaining, 3.5%), at 5.30%:** owner cash after maintenance in the base is
  **-$94.5M** a year (477.0 - 561.1 - 10.5). No-growth case **-$2.32** a share; growth case **-$3.70**: growing a negative stream
  makes it more negative, so the growth case is the bottom and the no-growth case the top (specific (b)'s ordering; the base,
  not the growth, is the finding). **Range: -$3.70 to -$2.32 a share against $5.42.**
- **The variants beside** (all equity-only unless marked; per share; range at 5.30%, then each end at 10%):

| Base | Maintenance | Growth | Owner cash after maintenance ($M) | Range at 5.30% (no-growth / growth) | At 10% (no-growth / growth) | Fair price |
|---|---|---|---|---|---|---|
| **Central: avg 2024c and 2025** | **sustaining** | **3.5%** | **-94.5** | **-$2.32 / -$3.70** | **-$1.23 / -$2.07** | **-$1.65** |
| FY2025 | sustaining | 3.5% | 78.1 | $1.91 / $2.01 | $1.01 / $0.87 | $0.94 |
| TTM to 2026-06-30 | sustaining | 3.5% | 90.2 | $2.21 / $2.30 | $1.17 / $0.99 | $1.08 |
| Central base | depreciation | 3.5% | 68.5 | $1.68 / $0.76 | $0.89 / -$0.04 | $0.43 |
| FY2025 | depreciation | 6.2% (total) | 182.8 | $4.48 / $6.15 | $2.37 / $2.68 | **$2.53 (the most favourable case found)** |
| TTM to 2026-06-30 | depreciation | 6.2% (total) | 166.6 | $4.08 / $5.55 | $2.16 / $2.39 | $2.28 |
| All-equity, central base | sustaining | 3.5% | 174.5 before interest | -$4.51 / -$4.61 | -$6.52 / -$7.09 | -$6.81 |
| All-equity, FY2025 | depreciation | 6.2% | 427.4 before interest | $1.69 / $5.60 | -$3.24 / -$2.53 | -$2.88 |

  (All-equity: owner cash before interest, the interest paid added back after a 25% tax shield, **CONVENTION of this run**, a
  blended US federal and state rate, the statutory rates being 15% Canadian federal plus provincial and 21% US federal plus
  state; against market value plus net debt at 2026-06-30, long-term debt $6,635.7M including commercial paper and bank lines,
  less cash $55.0M, = $6,580.7M, with the preferred shares at book, $184.3M, added as a senior claim; operating leases "not
  significant" per note 1 and left out. No growth spending credit on this basis.)
- **The floor, tested first** **[M2003-149]** ("there’s just a point at which we drop out of the game"). The highest value at ten
  percent of any case in this run is **$2.68** a share (FY2025 base, depreciation as maintenance, 6.2% growth, equity-only), against
  a price of $5.42. **No case earns the floor at the price.** OUT, whatever the width.
- **Beside the floor.** Even at the government rate, the most favourable range found ($4.48 to $6.15) holds the price inside it:
  not a screamer **[M2009-005]** ("It should scream at you"), **[M1996-084]**. On the all-equity basis, ten percent on the
  enterprise does not cover the debt in any case.
- **The signed, unclosed deal, beside (specific (c)).** The Suralis sale (6-K 2026-08-28: about $126.5M, plus up to $1.5M
  earn-out, proceeds "to be used for debt paydown"): valued as if closed, the proceeds reduce net debt by $126.5M, at most
  **+$0.16 a share** on either basis, less the owner cash Suralis now contributes, which is not filed separately (Chile is inside
  "Other regions", $376.4M of revenue with Bermuda). It cannot move any case to the floor. The box is decided on the central figure.
- **Whose tax.** The company's own cash tax is used (refunds in 2024 and 2025). No carryforward schedule was read; recomputing
  2025 at a statutory rate would lower owner cash further (by at least the $73.4M refund), so the convention's correction can
  only lower the figures above, and the box is unchanged. Said so.
- **Value range (central):** **-$3.70 to -$2.32 a share against $5.42** (equity-only, the utility basis). The most favourable
  case found: $4.48 to $6.15 at the sovereign.
- **Fair price (a reporting figure, never a verdict; Part VII):** central, equity-only (the regulated-utility basis):
  **-$1.65 a share** (each end valued at ten percent: -$1.23 and -$2.07, averaged); the all-equity figure beside: **-$6.81**.
  After the company's own tax. The most favourable variant found gives $2.53 (equity-only) and -$2.88 (all-equity). No
  cheap price is reported. Growth spending (above maintenance) $129.6M in year one, $176.6M in year ten, none after. Utility debt
  credit: long-term debt increase $353.4M a year, against growth spending only, cap 57.1% (the business's own long-term debt
  share of long-term capital; the filing's allowed shares do not cover a stated half of rate base), binding.
- **VERDICT: OUT.** No case earns the floor of about ten percent at $5.42 **[M2003-149]**; the floor is tested first, and the
  price would sit inside even the most favourable range at the government rate **[M2009-005]**. The rows expected that a utility at
  a full price closes OUT: "no way we get rich on our utility investments" **[M2009-104]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed the file OUT). Facts under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED** (and not asked by the operator for this run).

---
## THE BOX
**OUT at Q7, on the floor:** no case earns about ten percent at $5.42; central range (equity-only, the regulated-utility basis)
**-$3.70 to -$2.32 a share against $5.42**, the most favourable case found $4.48 to $6.15 at the government rate. Q1 IN, Q2 IN
(regulated return carried as a second best), Q3 against, Q4 against (no STOP), Q5 integrity IN with doubts on candour of tone
recorded and ability against, Q6 against on both parts.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.
- **Bears on Q8 (the bond).** The 30-year Treasury yields 5.30% (2026-10-27). Equity owner cash after maintenance over the market
  value: central -2.3% (-$94.5M / $4,173M); the most favourable base 4.4% ($182.8M, FY2025 with depreciation as maintenance).
  The bond is the first filter **[M1997-089]**.
- **Bears on Q9 (debt and exposures).**
  - Pre-tax earnings over interest, the rows' definition **[L2012-002]** ("pre-tax earnings/interest, not EBITDA/interest"):
    2025 (211.0 + 282.5) / 282.5 = **1.75x**; H1 2026 (88.2 + 149.7) / 149.7 = **1.59x**. The rows ask for earning power that
    "amply covers" interest even in bad years **[L2010-012]**, and value diversity among utilities at about "a 2:1 ratio"
    **[L2005-019]**; AQN has the diversity (some fifteen jurisdictions) and less than that cover.
  - Debt: long-term debt $6,635.7M at 2026-06-30, of which commercial paper $460.0M and bank lines $100.1M; principal due within
    a year $923.8M, in one to three years $153.0M, in four to five years $1,755.3M, after five years $3,855.6M (Q2 2026 MD&A,
    contractual obligations); credit facilities $1,880.8M with $560.1M drawn and $34.5M of letters of credit. Subordinated hybrid
    notes $1.1B and C$400M (2079 to 2082) that the company "anticipates repaying ... in advance of maturity". A second layer of
    debt at the parent (Corporate Group interest $140.2M in 2025). Ratings: BBB (S&P, DBRS, Fitch) at AQN; Baa2 (Moody's) at Liberty
    Utilities Co. Refinancing is assumed in the plan; the rows warn that "maturities must actually be met by payment" when
    credit is short **[L2010-020]**.
  - Liabilities without a stated upper end: the Mountain View Fire (2020, California; $178.4M accrued; "the Company cannot
    estimate the upper end of the range of reasonably possible losses"); the Lexington gas explosion (2025, Missouri; $152.2M
    accrued against $149.0M of insurance; "cannot currently estimate the upper end"; the Attorney General's petition; the
    commission's pipeline-safety docket). Condemnation of Apple Valley water pending at the California Supreme Court. The rows
    pass up businesses for "product liability potential" **[M2001-008]**.
  - Little or no debt **[R1997-001]**: the criterion is for whole businesses; this is a part-interest, and the debt is heavy.
- **Bears on Q10.** Nothing found.
- **Integrity (Q5) was answered in the file**, IN, with the doubts about candour of tone recorded at Q5; any later run of this
  name reads them first.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 999f4088, 2026-10-27); written question by question on the resume and
      committed after each: Step 0 to Q1 (a113d4bb), Q2 (bbad03e7), Q3 (56dbefa2), Q4 (27a991d8), Q5 (5aff8ca7), Q6 (36b21bb4),
      Q7 with Q6's buyback line written back (37052393), the close (this commit). **Departure, declared:** the Q7 arithmetic
      (`q7.py`, `q7_out.txt`) was computed while the filings were being read, before Q2 to Q6 were written, and was committed with
      the first resume commit. It is screening arithmetic headed COMPUTATION in its own file, it carried no entry language, and
      nothing in Q1 to Q6 cites it. Operator rule 9 applies to it: an analyst who has seen that the price fails the floor has an
      incentive to answer the earlier gates loosely, since they no longer decide the box; each gate was answered on its own
      filing evidence, and Q4 and Q5 were the ones watched for this.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's; the fold is the
      dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review, `PORTFOLIO.md` or blind-listed Screens file was opened, listed or searched; what was
      seen by accident (other companies' file names and commit subjects, memory counts) is declared under contamination and
      was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row (`check_run.py`
      in the research folder, result in `check_run_out.txt`); every filing fact carries its document and accession; the
      numbers not from a filing or a row are labelled CONVENTION of this run (the base, the comparison set, the 25% tax shield).
- [x] The order was kept; Q7 was the first STOP that failed; nothing after it is a clearance, and the facts after it are not weighed.
- [x] Owner cash from the cash flow statement after every capital spending case, never a net-income proxy (operator rule 5); the
      HLBV income and the featured adjusted figure are left out. Stock pay is not deducted a second time inside cash from
      operations (about $13M a year, declared at Step 0; it makes every case more favourable). The sovereign is the Treasury's
      own curve; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as found (the foundations' list and each question); facts after the STOP are under
      AFTER THE STOP. No integrity flag is needed in the box line, because Q5 was answered.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` failed on this 40-F filer and printed no arithmetic; none of its output was used; every figure is from the
      filed statements.
- [x] `python tools/check_framework.py` PASS before the closing commit (result in `check_framework_out.txt`).
- **What I could not get:** utility-by-utility rate base and earned returns (not filed); a continuing-business cash flow for
  2021 to 2023 (not separated in any filing); Suralis's own owner cash (not filed separately); the tax carryforward schedule
  (not read); the 2016 to 2017 balance sheets in US dollars (filed in Canadian dollars).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **A sale of most of the business inside the window.** Q7's specific (c) says how to treat acquisitions, mergers,
deals closed after the window and signed unclosed deals, but not a divestiture inside the window that removes a large part of what
the window's cash flows describe; here the renewables and Atlantica were in four of the five cash flow statements and no filing
separates them before 2024. I confessed a CONVENTION of this run (the two fiscal years the filer presents on the continuing
business, with FY2025, the TTM and the literal window beside), and the box does not depend on it, because no variant earns the
floor. (2) **"Sustaining" capital at a regulated utility.** Specific (e) takes the maintenance guess "where the filing allows";
this filer states "Sustaining" capital, but sustaining spending at a utility enters rate base and earns the allowed return, so
charging it all as maintenance in a no-growth case is harsh, and charging only depreciation is generous; the text does not say
which, so I made the filer's own figure central and showed depreciation beside. (3) **The utility debt credit's cap.** The rule
uses the filing's allowed debt share "where the filing states an allowed share" for at least half of the deciding part's rate base,
but a filer that states allowed shares case by case and never states rate base by utility leaves the test undecidable; I used the
own-share fallback and said so. It is also unsaid whether the own share counts commercial paper, which the credit itself excludes
(57.1% with it, 55.0% without; I used the higher). (4) **A non-positive central fair price for a utility.** Part VII defines the
fair price but says nothing about the alert when it is negative on the utility's central basis (the serial-acquirer case has such
a rule); I report the figure as computed, with the variants beside. Also unstated: the tax rate for adding interest back on the
all-equity basis (I used 25%, confessed).
