# Company Run — DTE Energy Company (NYSE: DTE) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to its dated name before any fetch** (commit
721fe7b5, before the first EDGAR request).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-18, after the run was committed (d876563d): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Dispatched run.** Written by a dispatched analyst under the brief of 2026-10-18 (an unattended overnight cycle), with
per-question pathspec commits of this file and `Test Runs/_research 2026-10-18 DTE/` only. The lock is the dispatching
session's (operator rule 10 (b)); this analyst did not touch it.

**Contamination, declared and not used.** (1) A directory listing of `Test Runs/`, made only to confirm that this run's
file and folder did not yet exist, showed the names of other run files dated 2026-10-18, among them utilities (CMS Energy,
Ameren, AEP, Alliant, Consolidated Edison, CenterPoint, Dominion and others) and an ADDENDUM of the same date. None was
opened. CMS Energy is the other Michigan utility and is used below as a competitor from its own SEC filings only.
(2) The session's starting context showed recent commit subjects, among them a Dominion (D) run's fold, with its Q7 box and
figures and framework notes ("net or gross debt credit", "whose debt share"). Not used; the debt-credit reading below was
made from Q7's text, and where the same ambiguity arises it is written down in this run's own words. (3) The adopted case
`Framework/v5/CASE 2026-10-18 - the regulated utility's fair price, decided from the corpus.md`, read for Q7's method
(adopted, so not on the blind list), names sixteen utilities that closed OUT on 2026-10-17 and 2026-10-18. Not used.
(4) The memory index loaded into the session names counts and states of the queue. Not used.

**Lines of evidence chosen from the 10-K** (Item 1, Item 1A, Item 7 of 0000936340-26-000054), as the brief asks:
(a) the Michigan rate regulation of the two utilities (authorized returns, rate cases, disallowances, the 10% cap on
retail access); (b) the capital programme ($30B electric and $4.5B gas over 2026-2030 against cash from operations of
about $3.9B in 2026) and how it is funded (debt, $500-600M a year of new equity 2026-2028); (c) the non-utility parts
(DTE Vantage, whose renewable-gas profits rest on federal and California credit programmes; Energy Trading, a
marked-to-market derivatives book); (d) the generation transition (coal retirements to 2032, Michigan's 100% clean
standard by 2040); (e) the data-centre contracts (Oracle 1.4 GW, Google 1.0 GW); (f) the parent's leverage and the
collateral it could be asked for.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $129.73 (close 2026-10-16, the last close before the run date; Yahoo Finance chart API through
  `tools/sources.py price()`; **aggregator, flagged per operator rule 5**, used for the live quote only).
- **Shares by class** from the latest filing's cover: DTE Energy common stock, without par value, **208,088,069** at
  2026-06-30 (10-Q for Q2 2026, filed 2026-07-28, accession `0000936340-26-000146`; `python Screens/cover_shares.py DTE`).
  The tool also printed 138,632,324, which the same cover identifies as DTE Electric's common stock, "indirectly-owned by
  DTE Energy"; it is not a second class of DTE shares and is not added. Cross-check: the 10-Q balance sheet states
  208,088,069 shares issued and outstanding at 2026-06-30; there are no treasury shares (no par stock, shares issued =
  outstanding). Filed after the 10-Q: the 8-Ks carry items 2.02, 5.02 and 7.01 only, none an issuance. The 10-Q (Note on equity) reports forward sale agreements
  under the at-the-market programme for about 3.7 million shares (2.5M at $144.41 and 1.2M at $141.96), unsettled at
  2026-06-30 and to be settled by 2026-12-31; they are left out of the count and named here.
- **Market cap:** $129.73 x 208.088M = **$26,995M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 10/16/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-17, `0000936340-26-000054` (Items 1, 1A, 5, 7, 8 and
  Notes 1-23 read); 10-Q for Q2 2026, filed 2026-07-28, `0000936340-26-000146`; DEF 14A filed 2026-03-12,
  `0000936340-26-000062`; 10-Ks for FY2023 `0000936340-24-000076`, FY2021 `0000936340-22-000077`, FY2019
  `0000936340-20-000127` and FY2017 `0000936340-18-000082` (balance sheets, cash flows, segment tables); 8-Ks
  `0000936340-25-000216` (credit facilities), `0000936340-25-000228` (Oracle), `0000936340-26-000068` (Google),
  `0000936340-26-000126` ($1.0B junior subordinated debentures), the 8-K of 2025-12-19 `0001193125-25-326913` (the
  $1.5B equity distribution agreement), `0000936340-26-000154` (a director's retirement); earnings releases, exhibit 99.1 of `0000936340-26-000051` (Q4 2025) and of `0000936340-26-000144` (Q2 2026).
  **One figure cross-checked against the filed statement:** net cash from operating activities 2025, $3,409M in the filed
  Consolidated Statements of Cash Flows (10-K page 62), equals the XBRL fact NetCashProvidedByUsedInOperatingActivities
  for FY2025 (3,409); depreciation and amortization 2025, $1,841M, likewise equal.
- `python tools/run.py DTE` printed one line only: "DTE: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (the
  utility's capital spending is tagged under the filer's own labels). No arithmetic line was available from it. **Every
  figure below is taken from the filed statements by hand** (script and outputs in `Test Runs/_research 2026-10-18 DTE/`,
  `q7.py` and `q7_out.txt`), so the tool contributed no number and no rule.
- **Owner cash by year (equity-only basis, the company's own tax, after interest; $M)** = net cash from operations, less
  maintenance spending taken as depreciation and amortization plus nuclear fuel amortization (the guess, Q3), less stock
  pay (Note 21: 71, 62, 48, 54, 60). Working capital is inside operating cash, so it is counted.

  | | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|
  | Net cash from operations | 3,067 | 1,977 | 3,220 | 3,643 | 3,409 |
  | D&A + nuclear fuel | 1,517 | 1,510 | 1,665 | 1,787 | 1,908 |
  | Stock pay | 71 | 62 | 48 | 54 | 60 |
  | **Owner cash, maintenance only** | **1,479** | **405** | **1,507** | **1,802** | **1,441** |
  | Capital spending, utility + non-utility | 3,772 | 3,378 | 3,934 | 4,467 | 4,429 |
  | Acquisition (Note 4) | 0 | 0 | 0 | 0 | 210 |
  | Notes receivable, net of collections (DTE Vantage projects) | 74 | 30 | 86 | 449 | 578 |
  | Long-term debt issued less redeemed | 935 | 584 | 1,551 | 2,394 | 3,138 |

  Average of the four years after the separation of DT Midstream (2022-2025): **$1,289M** a year; the literal five-year
  window (2021-2025) $1,327M. Capital spending ran at 2.2 to 2.5 times depreciation and nuclear fuel in every year shown. Stock pay is
  resolved: no line in operating cash adds it back by name, so it is deducted as a real cost whether or not it sits in
  "Other"; it is complete as Note 21 states it.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the margin of safety: the price is to be set against a value computed at the long
government rate, and "if you have to actually do it on — with pencil and paper, it’s too close to think about"
**[M1996-084]**. A share of DTE is a claim on a regulated business whose cash the owner sees only after the regulator
allows it, so "a share is a business" here means a business whose prices are set by others. No macro view enters: the
rate case schedule and the capital plan are read as filed, not forecast. Who is paid to tell you: the filer's own releases
feature "operating earnings" and guidance (Q4, Q5). **Contrary evidence, written down as found** ("write it down in the first 30 minutes" **[M1997-127]**): (1) the
company has paid out more in dividends than its operations leave after maintenance in one of the five years and relies
on new debt every year for the rest of its spending; (2) the parent's book equity ($12,154M at 2026-06-30) is less than
DTE Electric's own equity alone ($12,426M), so the gas utility, the non-utility parts and the goodwill are carried on
parent-level debt; (3) operating earnings exclude regulatory disallowances that recur each year; (4) the bonus measure
paid at 200% on that adjusted figure.

## THE STANDING RULE
The buyer's own conduct: a purchase of these shares for cash, unlevered and sized within means, carries no ruin outcome
for the buyer, "We are never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
borrowing to buy would breach it, "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's
own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as stated:** understanding means "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years" **[M2012-065]**; "a reasonable probability of being able to asses where the business
  will be in 10 years" **[M2000-037]**.
- **The key variables, and how predictable they are** ("trying to identify the key variables in that particular business,
  and evaluating how predictable they were first" **[M1998-044]**): for the regulated utilities, (i) the rate base, set
  by capital spending the MPSC approves; (ii) the authorized return on equity, 9.9% for DTE Electric and 9.8% for DTE Gas
  (10-K Note 9, `0000936340-26-000054`), re-affirmed at 9.9% in the MPSC order of 2026-02-19 (10-Q Q2 2026,
  `0000936340-26-000146`), against 10.75% asked; (iii) the equity share of the capital the regulator allows; (iv) the lag
  and the disallowances between spending and recovery. Each is written in a filing or an order and moves slowly. The
  rows' own statement of the business: "when you get an allowed return in the electric utility you’re almost certain of
  earning it, I mean, if you behave yourself" **[M2010-037]**. The test "do I understand enough about this business so that
  the financial statements will tell me the information that’s useful to me in making a judgment about what the future
  financial statements are going to look like" **[M2008-033]** is met for the utilities: the 10-K publishes a five-year
  capital plan by category and the rate cases publish the test years.
- **What is less foreseeable**, and whether it decides: the Energy Trading book (a marked-to-market derivatives portfolio
  "routinely has speculative trading positions", Item 1A) and DTE Vantage's renewable-gas income, which "are also dependent
  on the federal Renewable Fuel Standard and California's Low Carbon Fuel Standard" (Item 1A). Under the business-of-parts
  reading these do not decide: over 2021-2025 Electric earned $4,822M of segment net income, Gas $1,332M, Vantage $702M,
  Energy Trading $409M (FY2023 and FY2025 10-K segment tables), so Electric is 66% of the positive segment earnings and the
  largest part by far (see the parts table at Q2). Q1's holding-company reading asks only whether the parts that matter can
  be understood; Energy Trading at 6% and Vantage at 10% do not matter in that sense, and doubt about them does not carry the
  whole outside the circle.
- **Is it important and knowable?** ("things that are important and knowable" **[M2006-076]**) The deciding question for Electric is the regulatory compact over ten
  years, which is knowable in its mechanism and uncertain in its climate; the rows treat that uncertainty as a castle
  question, "the regulatory climate in a few states has raised the specter of zero profitability" **[L2023-011]**, which is
  Q2's.
- **Routing:** not a fast-changing industry in the sense of Q1's routing; the generation mix changes (coal to gas,
  renewables and storage by 2032), but the economics of a regulated return on rate base are the same whichever plant is
  built. The technology threat (distributed generation, storage) is named in Item 1A and is a castle question.
- **VERDICT: IN.** The deciding part is a rate-regulated electric utility whose earning power over ten years is set by
  rate base and an authorized return that are filed and slow to move, so "a reasonable fix on about what the earning power
  and competitive position will look like in five or 10 years" **[M2012-065]** is available for it, and "when you get an
  allowed return in the electric utility you’re almost certain of earning it" **[M2010-037]**; the parts that cannot be
  foreseen are small and do not decide.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. For the deciding
part the castle is a legal one: the franchise and the regulator. Each test, with its filing fact (10-K
`0000936340-26-000054` unless stated):
- **The attacker with money** ("if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I
  do it?" **[M2011-015]**): the distribution franchise cannot be duplicated by a rival with capital;
  "Competition in the regulated electric distribution business is primarily from the on-site generation of industrial
  customers and from distributed generation applications"; "DTE Electric does not expect significant competition for
  distribution to any group of customers in the near term" (Item 1). Supply competition is capped by statute: "Energy
  legislation enacted by the State of Michigan has placed a 10% cap on total retail access", with retail access at about
  10% of retail sales in 2023, 2024 and 2025 (Item 1). The money test passes in the form the rows give it for a railroad
  against an airline, "You really couldn’t create another railroad" **[M2013-054]**: no one can build a second grid in
  southeastern Michigan.
- **Pricing power and the agony before a rise** ("you can almost measure the strength of a business over time by the
  agony they go through in determining whether a price increase can be sustained" **[M2005-020]**): the business has no pricing power of its own; every rise
  is a rate case, the prayer session the row describes. The record: DTE Electric asked for $574M and a 10.75% return on
  2025-04-24 and received $242M and 9.9% on 2026-02-19 (10-Q Q2 2026, `0000936340-26-000146`); DTE Gas asked for $163M and
  10.25% (order expected September 2026); a new electric case asks $474M and 10.25% (filed 2026-04-28). The regulator also
  disallows: $28M of power-supply costs in 2025, capital spending written off of $25M (2023 order) and $12M (2025 order),
  $3M at gas (2024 order) (Item 7). So the castle protects the right to earn an allowed return, not the right to price.
- **Unit volume** ("We measure it by unit cases sold" **[M1999-054]**), read as deliveries: DTE Electric sales and deliveries 43,504, 44,420 and 44,592
  thousand MWh in 2023-2025, flat but for weather (Item 7); gas markets 303, 292 and 309 Bcf. Two hyperscale contracts are
  signed: Oracle, about 1.4 GW through February 2045, with "minimum monthly charges and, if applicable, termination fees"
  (`0000936340-25-000228`); Google, 1.0 GW through December 2047, on the same terms (`0000936340-26-000068`). Volume may
  grow; it has not yet.
- **The low-cost position, and the low bid** ("it wouldn’t be a question of people buying candy for the low bid"
  **[M2017-009]**): not tested by a market; the
  customer has no choice of wires. Affordability is the regulator's test instead, and the 10-K names it among the risks:
  compliance "can negatively affect the affordability of the rates charged to customers" (Item 1A).
- **Ask the competitors** ("which one would it be and why?" **[M1999-130]**): no rival names DTE in a filing read; the nearest is Consumers Energy (CMS),
  which co-owns the Ludington pumped-storage plant with DTE Electric (Note 7) and serves the rest of lower Michigan under the
  same commission.
- **Widening or narrowing** ("whether it’s likely to widen further or shrink on you" **[M1999-108]**; "grows either
  weaker or stronger" **[L2005-010]**): the authorized return has stood at 9.9% (electric) and 9.8%
  (gas) through the latest orders, and requests above it were refused. The franchise is not narrowing on the filings; the
  regulatory climate is the thing to watch, "it is difficult to project both earnings and asset values in what was once
  regarded as among the most stable industries in America" **[L2023-011]**.
- **What could destroy, modify or reduce it** ("destroy, or modify, or reduce the economic strengths" **[M2000-014]**):
  (i) the compact itself, as the 2023 letter narrates of other states, "the regulatory climate in a few states has raised
  the specter of zero profitability or even bankruptcy" **[L2023-011]**; "whether you earn X or go broke is not an equation that works" **[M2024-011]**; (ii)
  technology: advances "could make portions of our electric system power supply and/or distribution facilities obsolete
  prior to the end of their useful lives" (Item 1A), the question the 2006 letter asks of newspapers, "if cable and satellite broadcasting, as well as the internet, had
  come along first, newspapers as we know them probably would never have existed" **[L2006-008]**, asked of a grid; (iii) a
  catastrophe on a single system, "A catastrophic event can render a single utility insolvent" **[L2005-019]** (wildfire is
  not named in this 10-K; storms and a nuclear plant are). None of the three is shown on the filings to be filling the moat
  in; each is a weight carried to Q9.

**The competitor row.** The 10-K names no rival company in its competition sections (Item 1 names "alternative electric
suppliers", "on-site generation", "other natural gas transportation providers" and, for trading, "electric and gas
marketers, financial institutions, traders, utilities" generically). **CONVENTION of this run:** the rivals compared are
three regulated electric-and-gas utilities of the same region that file with the SEC: CMS Energy (the other Michigan
utility, same commission), WEC Energy Group (Wisconsin, MISO) and Xcel Energy (upper Midwest, MISO); rationale: a
franchised monopoly has no rival for its customers, so the comparison that tests whether its returns are ordinary is
against peers earning regulated returns under neighbouring regulators. Named rivals that do not file: none are named, so
none are flagged. Metric: net income attributable to common over average common equity, every year 2016-2025, from each
filer's 10-K XBRL facts (transcription, flagged; the DTE row checked against the filed statements; script `peers.py`).

| Year | DTE | CMS | WEC | XEL |
|---|---|---|---|---|
| 2016 | 9.8% | 13.5% | 10.6% | 10.4% |
| 2017 | 12.2% | 10.6% | 13.0% | 10.2% |
| 2018 | 11.3% | 14.3% | n/a | 10.7% |
| 2019 | 10.7% | 13.9% | n/a | 10.8% |
| 2020 | 11.4% | 14.4% | 11.5% | 10.6% |
| 2021 | 8.6% | 22.3% | 11.9% | 10.6% |
| 2022 | 11.3% | 12.3% | 12.4% | 10.8% |
| 2023 | 13.0% | 12.2% | 11.2% | 10.3% |
| 2024 | 12.3% | 12.7% | 12.3% | 10.4% |
| 2025 | 12.2% | 12.3% | 11.6% | 9.4% |
| Average | 11.3% | 13.8% | 11.8% (8 yrs) | 10.4% |

Sources: DTE `0000936340-26-000054`; CMS `0000811156-26-000004`; WEC `0000783325-26-000018`; XEL `0000072903-26-000009`
(latest 10-Ks; earlier years from the same filers' earlier 10-K facts). WEC's 2018 and 2019 year-end equity facts were not
found in the tagged data (n/a). 2021 is distorted at DTE (the DT Midstream separation and a $294M after-tax loss on
extinguishing debt, FY2021 10-K MD&A) and at CMS (its 2021 net income includes discontinued operations in the tagged
fact). **What the row says:** the four earn the same kind of return, about ten to fourteen percent on book equity, in
every year; none breaks away and none falls behind. **What it does not say:** DTE's consolidated figure is lifted by the
parent's leverage. DTE Electric alone earned $1,152M in 2025 on average equity of $11,784M (equity $11,154M and $12,414M,
DTE Electric balance sheet in the same 10-K), 9.8%, the authorized 9.9% almost to the point; the parent's equity ($12,303M
at 2025-12-31) is smaller than DTE Electric's own, so the consolidated 12.2% is the regulated return with the gearing of
parent debt laid over it, "we could make it almost any number you want if we just used enough leverage" **[M2001-054]**.

**The parts table** (five-year segment net income attributable, 2021-2025, from the filer's segment tables in the FY2023
and FY2025 10-Ks; the filer reports segment net income, which is used as the operating-profit measure, said so):

| Part | 2021-2025 net income | Share of positive segments | Castle | Decides |
|---|---|---|---|---|
| Electric (DTE Electric) | $4,822M | 66% | regulated franchise; return set by the MPSC | **yes (over half)** |
| Gas (DTE Gas) | $1,332M | 18% | regulated franchise; same commission | no |
| DTE Vantage | $702M | 10% | contract energy services and renewable gas; profits tied to credit programmes and steel ("Lower demand and prices in the Steel business", Item 7) | no |
| Energy Trading | $409M | 6% | none claimed; "Competitors with greater access to capital, or at a lower cost, may have a competitive advantage" (Item 1) | no |
| Corporate and Other | -$1,123M | n/a | holding-company interest and tax | n/a |

**The field's returns over the last full cycle**, judged in words: the regulated field earns the return its regulators
allow, about ten percent on the regulated equity, steadily, with no cycle in the ordinary sense. The rows call it what it
is: "there’s no way we get rich on our utility investments. But there’s no way we get poor, either" **[M2009-104]**; "You
can't expect to earn outsized profits in regulated utilities, but the industry offers owners the opportunity to deploy
large sums at fair returns" **[L2005-005]**. Q2's rule that a standing castle protecting only ordinary returns closes OUT
carries its own exception, "A return set by a regulator", which is "carried to Q3 as a second best" (Q2, What it rules
OUT). That exception governs here.

- **VERDICT: IN.** The deciding part's castle stands on the filings: a statutory franchise with competition capped at 10%
  of retail sales, an authorized return re-affirmed in the latest order, and no rival able to duplicate the grid, "You
  really couldn’t create another railroad" **[M2013-054]**. It protects a fair return, not "excellent returns on invested
  capital" **[L2007-004]**, which the framework sends to Q3 as a second best, "there’s no way we get rich on our utility
  investments" **[M2009-104]**. What could break it, the compact and the technology, is carried to Q9.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** ("we’re defining it in terms of the capital actually needed in the business"
  **[M2010-090]**; "return on tangible assets" **[M2011-060]**): in 2025 operating income was $2,374M against debt of $26,023M
  and equity of $12,303M less goodwill of $1,993M, $36,333M of tangible capital: **6.5% before tax**. DTE Electric alone:
  operating income $1,644M on its debt (current $754M, short-term $652M, long-term $12,419M) and equity ($12,414M), $26,239M:
  **6.3% before tax** (10-K `0000936340-26-000054`, DTE Electric statements). On its own equity DTE Electric earned 9.8%, the
  authorized return. These are the returns of a business whose return is fixed by its regulator, not earned against rivals.
- **Reinvestment to stand still and to grow** ("expenditures that a company must make to maintain its competitive position"
  and "optional outlays, aimed at business growth" **[L1999-024]**): capital spending was 2.5x, 2.2x, 2.4x, 2.5x and 2.3x
  depreciation and nuclear fuel in 2021-2025 (Step 0 table). The 10-K's plan for 2026-2030 is $30B at DTE Electric ($11B
  distribution, $4B base infrastructure, $15B cleaner generation), $4.5B at DTE Gas ($2.7B base infrastructure, $1.8B gas
  renewal) and about $2.0B at DTE Vantage, against "cash from operations in 2026 will be approximately $3.9 billion" and 2026
  capital spending of "approximately $6.8 billion" (Item 7). Much of it is compulsory: the remaining coal units retire by
  2032 and "Generation from the retired facilities will continue to be replaced or offset", and Michigan law requires a 100%
  clean energy portfolio by 2040 (Item 1, Item 7). The rows name the trap, "you have to spend money like crazy if it’s
  attractive to spend money, and you have to spend it the same way if it’s unattractive" **[M1998-128]**, and the
  utility's place in it, "Certain other companies � think of our regulated utilities, for example � fail it because
  inflation places heavy capital requirements on them. To earn more, their owners must invest more." **[L2011-019]**
- **What the added capital earned** ("It’s measured by the operating earnings after depreciation." **[M2014-086]**): from
  2021 to 2025 operating income rose $879M ($1,495M to $2,374M) while debt plus equity rose $11,458M ($26,868M to $38,326M):
  **7.7% before tax on the added capital**, about what the regulator allows on a capital structure of half debt. On the
  equity alone the gain looks larger because the added capital was mostly borrowed (long-term debt issued less redeemed,
  $8,602M of the $11,458M).
- **The growth arithmetic and its caps:** growth of owner cash follows growth of rate base, and rate base grows only with
  spending above depreciation, about 80% of it borrowed; the owner gets more only by putting more in, "The good one pays an
  attractive rate of interest that will be earned also on deposits that are added" **[L2007-010]** at best, and the rate here
  is the regulated one. Q7 carries the cap that follows: the growth of owner cash cannot outrun the business's own sales.
- **WEIGHS AGAINST.** The added capital earns the decent, regulated return the rows accept of a second-best business, "as
  the second-best choice, still a good choice, the answer is yes" **[M2018-055]**, on the condition of "decent returns on the
  incremental sums they invest" **[L2009-012]**, which is met; but the capital needed is heavy, compulsory and growing, and
  the business has never in the window produced cash beyond its spending without new debt.
  The "little or no debt" criterion is applied at Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them** ("balance sheets over an 8 or 10 year period before I even look at the income
account" **[M2025-032]**). DTE Energy consolidated, $M, each year from its own 10-K (FY2017, FY2019, FY2021, FY2023, FY2025;
2026-06-30 from the 10-Q). Total debt = short-term borrowings + current and long-term debt, securitization bonds, junior
subordinated debentures and finance leases.

| Dec 31 | Total assets | PP&E net | Goodwill | Regulatory assets (non-current) | Customer receivables | Revenue | Cash | Total debt | Equity | Retained earnings | Debt / (debt + equity) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 32,041 | 19,730 | 2,286 | 3,871 | 1,522 | 10,630 | 92 | 11,782 | 9,011 | 5,114 | 56.7% |
| 2017 | 33,767 | 20,721 | 2,293 | 3,723 | 1,758 | 12,607 | 66 | 12,915 | 9,512 | 5,643 | 57.6% |
| 2018 | 36,288 | 21,650 | 2,293 | 4,568 | 1,789 | 14,212 | 71 | 14,242 | 10,237 | 6,112 | 58.2% |
| 2019 | 41,882 | 25,317 | 2,464 | 4,171 | 1,642 | 12,669 | 93 | 17,450 | 11,672 | 6,587 | 59.9% |
| 2020 | 45,496 | 24,499 | 1,993 | 4,125 | 1,542 | 11,423 (restated, continuing) | 472 | 19,508 | 12,425 | 7,156 | 61.1% |
| 2021 | 39,719 | 26,944 | 1,993 | 3,482 | 1,695 | 14,964 | 28 | 18,163 | 8,705 | 3,438 | 67.6% |
| 2022 | 42,683 | 28,767 | 1,993 | 3,886 | 2,038 | 19,228 | 33 | 19,159 | 10,397 | 3,808 | 64.8% |
| 2023 | 44,755 | 28,169 | 1,993 | 6,209 | 1,632 | 12,745 | 26 | 20,845 | 11,050 | 4,404 | 65.4% |
| 2024 | 48,846 | 30,893 | 1,993 | 6,771 | 1,690 | 12,457 | 24 | 23,053 | 11,699 | 4,946 | 66.3% |
| 2025 | 54,066 | 33,653 | 1,993 | 7,380 (+619 securitized) | 2,031 | 15,814 | 208 | 26,023 | 12,303 | 5,484 | 67.9% |
| 2026-06-30 | 56,234 | 35,496 | 1,993 | 7,593 (+582 securitized) | 1,683 | n/a | 42 | 27,584 | 12,149 | 5,283 | 69.4% |

**What moved and why.** (1) **Debt against equity:** debt rose 2.3 times ($11.8B to $27.6B) while equity rose 35% ($9.0B
to $12.1B); book equity is lower today than at the end of 2020 ($12.4B), because the 2021 separation of DT Midstream took
$3,973M of net assets out (FY2023 10-K cash flow supplement) and dividends have taken about 60% of each year's earnings
since. The debt share of capital rose from 57% to 69%. (2) **Goodwill** is flat at $1,993M since the midstream goodwill left
with the spin-off; it is 16% of equity, and the parent's equity ($12,303M) is less than DTE Electric's alone ($12,414M), so
on the consolidated books the gas utility, the non-utility parts and the goodwill are carried by parent debt. (3)
**Regulatory assets** doubled ($3.9B to $8.0B with the securitized part); the step in 2023 is the reclassification of the
undepreciated cost of the retiring Belle River and Monroe coal plants from plant to a regulatory asset after the 2023
Integrated Resource Plan settlement (gross plant fell from $39,346M to $37,274M in the same year; Note 9 describes "Recoverable
undepreciated costs on retiring plants", of which "$ 1.05 billion" is to be recovered through future securitizations). What
the figures cannot say: these $8.2B are claims on future customers' bills, good only as long as the commission keeps
granting them; the auditor names "Accounting for the Effects of New, or Changes to Existing, Regulatory Matters" its critical
audit matter. (4) **Receivables** track revenue, which swings with gas prices through Energy Trading (revenue $19.2B in 2022,
$12.5B in 2024); customer receivables were 14.3% of revenue in 2016 and 12.8% in 2025, no build-up. (5) **Cash** is never
more than $0.5B; liquidity is the revolving credit ($2.8B across the three borrowers, `0000936340-25-000216`) and commercial
paper. (6) **Retained earnings** fell by half in 2021 (the spin-off) and have rebuilt to $5.3B.

**The real costs.**
- **Depreciation** is a real cost ("Depreciation charges are a more complicated subject but are almost always true costs"
  **[L2015-004]**); it is used below as the maintenance guess ("the depreciation charge is not inappropriate in most
  companies to use as a proxy for required capital expenditures" **[M1998-127]**), with the warning the rows give for this
  very industry, "if you’re in a business such as the utility business or the railroad business, it just keeps eating up more
  and more money, and your depreciation charges are inadequate" **[M2015-049]**. D&A includes the 15-year amortization of the
  undepreciated Monroe plant (Item 7), a recovery of past spending, so the proxy runs high in that part and low in the
  inflation part; no better guess is in the filing. The 10-K's own "base infrastructure" figure ($6.7B over five years for
  the two utilities, $1.34B a year) is shown as a generous variant at Q7.
- **Stock pay** $60M (2025), $54M, $48M (Note 21): deducted. No options granted since 2010 (DEF 14A).
- **EBITDA in the filer's own mouth:** no instance found (a text search of the 10-K, the two earnings releases and the proxy
  for "EBITDA" returns none).
- **Taxes:** the company paid almost no cash income tax (cash paid, net, $(5)M, $(3)M, $(3)M in 2023, 2022, 2021, FY2023
  10-K); production tax credits cut the 2025 effective rate by 10.4 points (Note 10); tax credit carryforwards of $1.6B
  "expire from 2034 through 2047" (Note 10). The utility's credits reduce customer rates by the filer's own account ("DTE
  Electric expects these tax credits to reduce the cost of owning assets [...] thereby reducing customer rate impacts", Item
  1), and of deferred taxes in a utility the rows say "I don’t think I would look at that as a hidden form of equity"
  **[M2015-030]**. Operating cash is used as filed, after the company's own tax.
- **The recurring "one-time":** the filer's featured figure is "operating earnings", "the primary performance measurement for
  external communications with analysts and investors" (Q4 2025 release, `0000936340-26-000051`). It excludes, among others,
  "MPSC disallowance of power supply costs previously recorded" ($33M pre-tax in 2025), the Fermi 1 decommissioning revision
  ($47M), an "Estimated litigation outcome regarding EES Coke Battery" and mark-to-market timing at Energy Trading; 2025
  operating earnings were $1,530M against reported $1,462M ($7.36 against $7.03 a share). Disallowances recur: $25M (2023
  order), $12M (2025 order), $3M (gas, 2024 order), $28M (2025 PSCR order) (Item 7). The rows: "to tell owners year after
  year, "Don't count this," when management is simply making business adjustments that are necessary, is misleading."
  **[L2016-007]**; "a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share
  earnings" makes us nervous" **[L2016-006]**. And the company gives guidance: "DTE Energy confirms 2026 operating EPS
  guidance of $7.59 to $7.73." (Q2 2026 release, `0000936340-26-000144`), "the scourge of earnings "guidance"" **[L2019-006]**.
  These are recorded here as a weighing against and carried to Q5.
- **What the accounts say well:** the MD&A explains the Energy Trading timing in plain terms ("a $70 million unfavorable
  change in timing-related gains primarily related to gas strategies subject to reversal in future periods", Item 7), a
  management that "does explain to you in clear terms what’s going on" **[M1994-018]**. No tell from the accounts themselves
  was found: no prepaid or deferred account building beyond the regulatory assets explained above, receivables in line with
  sales, no reserve released into earnings.
- **VERDICT on the accounts: WEIGHS AGAINST.** No confusion and no suspicion in the statements; the figures are readable and
  the recast earnings feed Q7 (owner cash, Step 0). Against: the featured adjusted figure removes recurring costs and the
  company guides to it, carried to Q5 as evidence on the people; and the balance sheet shows
  a debt share rising every year since 2016 and parent equity smaller than the main subsidiary's, carried to Q9.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The people** (DEF 14A `0000936340-26-000062`; 8-Ks): Joi M. Harris, President and CEO since 2025-09-08 (President and
  Chief Operating Officer before); Gerardo Norcia, Executive Chairman since 2025-09-08 (Chairman and CEO until 2025-09-07);
  David Ruud, Vice Chairman and CFO. Eleven of thirteen nominees independent; a Lead Independent Director since 2023.
- **The first yardstick, the record against the hand dealt** ("how well they run the business [...] You have to have some
  understanding of the hand they were dealt" **[M1994-008]**): the hand is a franchise with an allowed return; the record is
  that DTE Electric earned 9.8% on its equity in 2025 against 9.9% allowed (Q2), the commission re-affirmed the return in
  February 2026, credit stayed investment grade, and the company reports outage time down 70% from 2023 to 2024 and a further
  60% in 2025 (Q4 2025 release; the company's own measure, not audited). Against: the regulator disallowed costs in each
  recent order (Q2), and DTE Vantage's steel business is the subject of EPA notices of violation under the Clean Air Act
  since 2019 with "estimated litigation penalties in the Steel business of $13 million" in 2025 (Note 18; Item 7).
- **The second yardstick, how they treat the owners** ("how well that they treat their owners" **[M1994-008]**; "read the
  proxy statements, see what they think of — see how they treat themselves versus how they treat the shareholders"
  **[M1994-009]**): see Q6, Part B. In brief: named-executive pay of about $41M in 2025, of which the Executive Chairman
  (the former CEO) $14.2M and the new CEO $6.7M; no options since 2010; hedging and pledging prohibited; all executives meet
  ownership guidelines.
- **The habits carried from Q4, read with the integrity record.** (1) The featured adjusted figure: "operating earnings" are
  "the primary performance measurement for external communications"; they exclude disallowances that recur every year. (2)
  Guidance: "DTE Energy confirms 2026 operating EPS guidance of $7.59 to $7.73." (3) The bonus: 20% of the 2025 annual
  incentive paid at the 200% maximum on "DTE Energy Adjusted Operating Earnings Per Share" of $7.36 against a target of
  $7.16 and a maximum of $7.23; reported diluted EPS was $7.03, below the $7.09 threshold, so on the GAAP figure that
  component would have paid nothing (DEF 14A; 10-K). The rows: "a management that regularly attempts to wave away very real
  costs by highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**; "I hate, with a passion, rewarding
  anything that can be easily faked." **[M1996-089]**; "Managers that always promise to "make the numbers" will at some point
  be tempted to make up the numbers." **[L2002-041]**. **What weighs the other way, found in the same documents:** the
  adjustments run in both directions (a $25M Vantage gain excluded in 2024, a $27M gain on an equity investment excluded in
  2025, mark-to-market gains excluded as well as losses; Q4 2025 release), every item is reconciled line by line with its
  income-statement caption, and the 2024 operating figure ($1,416M) was within 1% of reported ($1,404M). No restatement, no
  qualified opinion (PwC, auditor since 2008), and no instance in the filings read of a target met by an accounting change.
- **Love of the business; the same after being paid:** not testable for a part-interest bought in the market; the
  speakers say as much: "In terms of sizing up managements — obviously if we’re going to buy the whole business, that’s a
  different question." **[M2007-081]** is the row for this; for a stock the reading tests carry the weight.
- **How they talk:** the 10-K and the releases are written by a reporting department ("Secured landmark agreement",
  "historic gains"), and no letter from the chief executive to the owners is in the filings read; "if it’s clearly the
  product of some investor relations department or outside consultant or something of the sort, you know, that tells you
  something about the individual" **[M2007-083]**. No mistake is narrated in the filings read; the disallowances are reported
  as variances, not as errors.
- **VERDICT on integrity: IN** (a close call, stated): what the record read shows is a presentation habit and a pay design,
  not a dishonest statement. The adjusted figure is reconciled, cuts both ways and sits close to GAAP, so the record does not
  show "the reports are essentially a little dishonest, or biased" **[M1995-111]**; the habit is "a negative" that the rows
  "can’t afford to use [...] as a total exclusionary factor" **[M1994-018]**. Doubt would close the file, "If you’ve got doubts,
  forget it." **[M2013-088]**; the doubt this run has is about the incentive the bonus creates, which is Q6's, not about the
  truth of what is reported. **Ability: WEIGHS FOR, slightly**: the allowed return is earned and the regulator's latest order
  re-affirmed it, which is what ability means in this hand; it weighs only slightly because "The really great business is one
  that doesn’t require good management" **[M1996-037]** and a utility's record is largely the regulator's.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** ("We test the wisdom of retaining earnings by assessing whether retention, over time, delivers
  shareholders at least $1 of market value for each $1 retained." **[R1995-009]**; "if after three or four years, you’ve
  found that the dollars we’ve retained hasn’t created more of that in value, then the presumption becomes very strong"
  **[M1998-110]**). Span: the four years after the separation, end-2021 to end-2025 (the earlier years hold a business since
  given to the owners). Market value: $119.54 x 193.748M = $23,161M at 2021-12-31; $128.98 x 207.745M = $26,795M at
  2025-12-31 (closes from the aggregator, flagged; share counts from the filed equity statements): **+$3,634M**. Capital the
  owners put in: earnings retained $2,056M (net income $5,346M less dividends declared $3,290M, 2022-2025) plus new shares
  $1,404M (the 2022 equity-unit settlement $1,300M and plan issuance $35M, $35M, $34M) less the 2022 repurchase $55M:
  **$3,405M**. **$1.07 of market value for each $1 put in**: the test is met, barely, on the market leg; on book value the
  equity rose $3,595M, the same as the capital put in, so nothing was added beyond the money itself.
- **Dividends** ("a company that expects to regularly earn more than it can profitably employ in its business, should be
  paying out dividends" **[M2004-089]**): DTE does not earn more than it can employ; it spends more than its operations
  bring in every year, yet pays about 60% of earnings as dividends ($871M in 2025, "approximately $1.0 billion in 2026") while
  planning to sell "$500 million to $600 million of equity in 2026" and as much again in 2027 and 2028 (Item 7). The owners
  are paid with one hand and asked for new money with the other. Weighs against.
- **Buybacks:** $66M in 2021 and $55M in 2022 (465 thousand shares, about $118 a share; FY2023 10-K equity statement), no
  price stated in any filing read; in the fourth quarter of 2025 only shares withheld for tax on vesting (10-K Item 5).
  ("repurchase announcements almost never refer to a price above which repurchases will be eschewed" **[L2016-002]**.)
  **Buyback line, written back from Q7:** the 2022 purchases at about $118 a share sit above the bottom of Q7's range,
  $114.06 (central, at the sovereign), and far above the fair price of $59.23; under the framework's convention for a
  programme that names no price, the purchases weigh against.
- **Issuance and deals** ("We will issue common stock only when we receive as much in business value as we give."
  **[R1995-010]**): equity units were sold in 2016 ($654M, FY2017 10-K), common stock and equity units in 2019 ($1,023M and $1,265M,
  FY2019 10-K; the units settled in shares in 2022), and shares are being sold again (the $1.5B at-the-market programme of December 2025, forwards for about 3.7 million shares at
  $141.96 to $144.41 in 2026); shares rose from 179.4M at the end of 2016 (FY2017 10-K equity statement) to 208.1M. This is a serial issuer by plan, the candidate
  second STOP of Q6 ("we have never invested in companies that are hell-bent on issuing shares" **[L2014-015]**), weighed here
  as the framework leaves it unresolved. The only acquisition in the window is a $216M cogeneration plant bought for cash in
  2025 (Note 4); no all-stock deal, so Q6's STOP ("it's impossible for that buyer to make a sensible deal in an all-stock
  deal" **[L2009-019]**) does not arise.
- **Part A: WEIGHS AGAINST**: retention barely passes; the dividend is paid out of money raised again from the owners and
  lenders; the share count grows by plan.

**Part B: the pay, the board and the owners** (DEF 14A `0000936340-26-000062`).
- **Pay tied to what the person controls** ("tying performance to what is actually under the reasonable control of the person
  that’s being measured" **[M2003-019]**): the annual plan pays on adjusted operating EPS (20%), "Cash from Operations" (20%,
  $3,532M by the plan's measure against $3,409M in the filed cash flow statement), customer satisfaction, safety and
  reliability measures (the operating measures are within management's control and fit the business). The long-term plan is
  70% performance shares, 80% of them on total shareholder return against nineteen utility peers and 20% on cumulative
  operating EPS, and 30% time-based restricted stock. Relative return is a price measure, partly a "lottery ticket"
  arrangement "whose ultimate value [...] is totally out of the control of the person whose behavior we would like to affect"
  **[L1996-018]**; the restricted stock pays whatever happens, "they design systems that payoff no matter what happens"
  **[M1999-018]**; and the earnings measures are the company's own adjusted figures (Q5).
- **How they treat themselves:** total named-executive pay about $41M (2025) against net income of $1,462M; the Executive
  Chairman, who stepped down as CEO in September 2025, was paid $14.2M with a long-term grant target of 625% of salary, more
  than twice the new CEO. The former CEO remaining as executive chair with the larger pay is the arrangement the rows warn of
  in its milder form, "how hard it is to replace a mediocre CEO if that person is also Chairman" **[L2014-026]**; here the
  CEO is not chairman, and a Lead Independent Director sets agendas.
- **The board:** non-employee directors are paid $125,000 in cash and $175,000 in phantom shares a year (2026 programme);
  "A director getting $150,000 a year from a company, who needs it, is not an independent director." **[M2005-090]** (no
  director's need is known; the level is recorded). Ownership guidelines are met with phantom and restricted shares counted,
  not shares bought: "purchasing shares with their savings, rather than simply having been the recipients of grants"
  **[L2019-008]** is not shown.
- **The owners as partners:** guidance is given every quarter; the rows' own practice, inverted into a test: "We don’t give
  out earnings guidance. We think it’s silly." **[M2016-002]**.
- **Part B: WEIGHS AGAINST**: the largest financial measures are figures management defines and guides to, the long-term
  pay rides the share price against peers, and a third of it pays regardless.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at the long government rate, held as a range. Arithmetic: `Test Runs/_research 2026-10-18 DTE/q7.py`, output `q7_out.txt`
(computed during the Step 0 reading and headed COMPUTATION, NOT A CLEARANCE until Q1 to Q4 had closed; operator rule 3).

**The basis.** The deciding part (Electric, 66% of five-year segment earnings) earns a return its regulator allows, so Q7,
The regulated utility, governs: the exception is the row's own, "to assign a large portion of our debt to any individual
business would generally be fallacious (leaving aside certain exceptions, such as debt dedicated to Clayton's lending
portfolio or to the fixed-asset commitments at our regulated utilities)" **[L2017-012]**, and "when you get an allowed
return in the electric utility you’re almost certain of earning it" **[M2010-037]**. **Central: the equity-only basis**, owner
cash after interest and after the company's own tax, against the market value of the shares ($26,995M), with the long-term
debt raised over the window to fund the fixed assets credited against their spending up to the debt share of capital.
**All-equity basis beside.** DTE Vantage and Energy Trading are not split out; they are 16% of five-year segment earnings and
are left on the same basis as the whole, said so (the cash statements are not reported by segment).

**The inputs and the specifics, one by one.**
- **The window. CONVENTION of this run:** the central window is the four years after the separation of DT Midstream
  (2022-2025), with the literal five-year window (2021-2025) beside; rationale: DT Midstream was given to the owners on
  2021-07-01, so 2021's operating cash, capital spending and depreciation include half a year of a business the buyer of
  today's shares does not get, and the rows value "the cash that can be taken out of a business" **[R1996-018]**; the
  framework's specifics name mergers and acquisitions inside a window, not a spin-off.
- **(a) Cycles:** a regulated utility has no business cycle in the filings; 2022 is a low year for owner cash ($405M)
  because "Regulatory assets and liabilities" drew $766M of cash in that year's statement (FY2023 10-K), returned in 2023
  (+$594M) and 2024 (+$586M). It is kept in the average, where it belongs as working capital (d), and it makes the end-year
  growth rate meaningless, "a base year in which earnings were poor can produce a breathtaking, but meaningless, growth rate"
  **[L2005-003]**.
- **(b) Decline or meaningless rate:** owner cash rose from $405M (2022) to $1,441M (2025), 52.7% a year between end years,
  meaningless by the row above; between the halves of the window (2022-2023 average $956M, 2024-2025 average $1,622M) 30.2% a
  year.
- **(f) The cap:** 30.2% carried ten years would make owner cash $18.1B, 144% of utility revenue grown at its own rate,
  against a highest share earned in the window of 22.6% (2024, $1,802M of $7,990M): an absurdity, "if you trace out the
  mathematics of it, you bump into absurdities, then you better change expectations somewhat" **[M1999-067]**. The growth
  carried is the business's own sales growth over the same window, measured the same way (between halves): **utility
  revenue, 3.53% a year** ($7,855M average of 2022-2023 to $8,420M of 2024-2025). **CONVENTION of this run:** "sales" here is
  utility operating revenue, not consolidated revenue; rationale: consolidated revenue is dominated by Energy Trading's gross
  commodity turnover ($6.5B of $15.8B in 2025) and fell from $19.2B to $15.8B over the window on gas prices, which says
  nothing of the business's growth. Shown beside: utility revenue between end years, 2.39%.
- **(c) Acquisitions:** $210M in 2025 (Note 4), deducted as spending, total growth credited; net purchases are far below half
  of owner cash, so the serial-acquirer rule does not apply. DTE Vantage's investment in notes receivable for its on-site
  projects (net $1,143M over 2022-2025) is counted as spending for growth too, said so: it is capital put into projects that
  earn the segment's interest income (Item 7).
- **(d) Working capital** is inside net cash from operations and is counted every year.
- **(e) Maintenance central:** maintenance is guessed at depreciation and amortization plus nuclear fuel amortization
  ("the depreciation charge is not inappropriate in most companies to use as a proxy for required capital expenditures"
  **[M1998-127]**; "the shareholders are entitled to my best guess" **[M2000-144]**). Central owner cash, maintenance only,
  equity-only: **$1,289M a year** (2022-2025). Growth spending is charged against the growth it buys: capital spending
  ($16,208M), the acquisition ($210M) and the notes ($1,143M), less maintenance ($6,870M), less the debt credited ($7,667M),
  leaves **$756M a year** of growth spending carried by the equity.
- **The debt credit.** Long-term debt issued less redeemed, 2022-2025: $7,667M (issued $14,300M, redeemed $6,633M; filed cash
  flow statements). The cap is the debt share of capital the regulator allows "as the filing states it": no instance found (a
  text search of the 10-K and the Q2 10-Q for "capital structure" returns none; Note 9 states the authorized returns only),
  so the business's own debt share at the latest filed date is used: 69.4% consolidated at 2026-06-30 ($27,584M of debt,
  $12,154M of equity), cap $11,251M; DTE Electric's own, 55.3%, cap $8,971M, beside. Neither binds; $7,667M is credited
  either way. **Reading of this run, stated:** the debt credited is net of redemptions, because the gross figure includes the
  refinancing of debt that funded assets built before the window, and crediting it would credit old borrowing against new
  spending.
- **The tax:** the company's own tax as paid. The carryforwards "expire from 2034 through 2047" (Note 10), mostly beyond ten
  years, and the utility's production credits reduce customer rates by the filer's own account (Item 1), so the
  statutory-rate recomputation of Q7, Whose tax, is not applied; DTE Vantage's own credits ($84M, $71M, $60M in 2025-2023,
  Item 7) carry no stated expiry and are left as filed, said so.
- **The rate:** 5.43%, the 30-year Treasury, 2026-10-16. Ten years at the growth carried, then zero nominal growth.

**COMPUTATION** (per share, 208.088M shares):

| Case | Owner cash | Growth carried | Value at 5.43% | Value at 10% | Expected return at $129.73 |
|---|---|---|---|---|---|
| No growth, maintenance only (central) | $1,289M | 0% | **$114.06** | $61.93 | 4.8% |
| Growth, growth spending of $756M a year charged | $1,289M | 3.53% | **$123.78** | $56.53 | 5.2% |
| Beside: literal window 2021-2025, no growth / growth (2.73%, spending $884M) | $1,327M | 0% / 2.73% | $117.42 / $113.94 | $63.76 / $50.73 | 4.9% / 4.9% |
| Beside: generous maintenance (the filed 2026-2030 "base infrastructure" plan, $1,340M a year) | $1,666M | 0% / 3.53% | $147.47 / $154.37 | $80.07 / $68.48 | 6.2% / 6.2% |
| Beside: all spending charged, debt credited (series changes sign, no growth) | $533M | 0% | $47.15 | $25.60 | n/a |
| Beside: all-equity basis (owner cash before interest $1,890M, less net debt $27,542M) | $1,890M | 0% | $34.87 | -$41.55 | n/a |

At 10% the growth case is worth less than the no-growth case ($56.53 against $61.93): the growth bought costs more than it
returns at the floor, "growth can destroy value if it requires cash inputs in the early years of a project or enterprise
that exceed the discounted value of the cash that those assets will generate in later years" **[L2000-023]**. At the range's own rate
(5.43%) the growth case is the top of the range; at the floor it falls below the no-growth case, and by specific (e)
that inversion is recorded as the finding. To earn ten percent at today's price with the growth spending as charged, owner
cash would have to grow 12.9% a year for ten years, almost four times the business's own sales growth.

- **Value range (central, equity-only): $114.06 to $123.78 a share against $129.73.** Width 1.09 to 1.
- **The floor, tested first:** no case earns the floor at the price. The best case this run can defend, the generous
  maintenance guess, returns 6.2% a year at $129.73; the central cases 4.8% and 5.2%, below the 30-year Treasury at 5.43%.
  "we don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**; "if government bond rates
  were 2 percent, we’re not going to buy a business to earn 3 or 3 1/2 percent expectancy over the years" **[M2007-095]**.
- **The price against the range:** above the top of the central range, which closes OUT under the floor convention whatever
  the width.
- **Fair price (a reporting figure, never a verdict; Part VII):** **$59.23 a share on the equity-only basis (central for a
  regulated utility)**, the average of the two end cases valued at ten percent ($61.93 and $56.53), after the company's own
  tax, with the debt raised for the fixed assets credited up to the debt share of capital. **All-equity beside: -$41.55, not
  positive** (no-growth case at ten percent, owner cash before interest against market value plus net debt of $27,542M at
  2026-06-30; no subsequent event stated in the 10-Q adds to it; operating leases left out). No cheap price is reported.
  Beside, not central: literal window $57.24; generous maintenance $74.28. The unsettled forward sales (about 3.7M shares at
  $141.96 to $144.41) would issue shares at more than twice the fair price; they change no figure above.
- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case: "there’s just a point at which we drop out
  of the game" **[M2003-149]**. A regulated utility at a full price closes OUT, "there’s no way we get rich on our utility
  investments" **[M2009-104]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (closed at Q7).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (closed at Q7). Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (closed at Q7).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (closed at Q7). Facts under AFTER THE STOP.

---
## THE BOX
**OUT at Q7.** Equity-only range $114.06 to $123.78 a share against $129.73 (30-year Treasury 5.43%); no case earns the floor
(best defensible case 6.2%, central 4.8% to 5.2%); fair price $59.23 equity-only, all-equity -$41.55 beside, not positive.
Q1 and Q2 IN; Q3, Q4 and Q6 weigh against; Q5 integrity IN on a close call, with the adjusted-earnings bonus recorded.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found ("write it down in the first 30 minutes" **[M1997-127]**); no verdict; the box unchanged.
- **Q8 (the bond):** the expected return at the price on the central cases (4.8%, 5.2%) is below the 30-year Treasury's
  5.43% on the same day.
- **Q9 (debt and exposures):** coverage, pre-tax earnings plus interest over interest, 2.0x (2021), 2.6x, 3.0x, 2.4x, 2.5x
  (2025) and 1.7x for the first half of 2026 (10-Q: pre-tax $430M, interest $594M); debt share of capital 69.4% at 2026-06-30
  (the credit agreement's own covenant is total funded debt to capitalization of no more than 0.70 for DTE Energy and 0.65
  for DTE Electric and DTE Gas, measured by the agreements' definitions, which are not the figure above; the covenant limited
  dividends to "$ 2.1 billion of DTE Energy's Retained earnings of $ 5.5 billion" at 2025-12-31, Note 16); scheduled
  maturities $1,352M (2026), $1,730M, $1,987M, $1,962M, $2,504M (2030) (Note 14); "contractual obligation to post collateral
  in the form of cash or letters of credit in the event of a downgrade to below investment grade [...] was $483 million"
  (Item 7); 2026 capital spending of about $6.8B against cash from operations of about $3.9B, the gap to be borrowed or
  issued; the parent's equity smaller than DTE Electric's own (Q4); Energy Trading "routinely has speculative trading
  positions" (Item 1A); a nuclear plant (Fermi 2) with decommissioning trusts of $2,552M; two data-centre customers (Oracle
  1.4 GW, Google 1.0 GW) with minimum charges, termination fees and parent credit support; REF guarantees with a maximum
  potential liability of $201M (Note 18); a single service territory, "A catastrophic event can render a single utility
  insolvent" **[L2005-019]**.
- **Q12 (how the money is made):** EES Coke, DTE Vantage's metallurgical coke battery in Michigan, is the subject of EPA
  notices of violation under the Clean Air Act (2019, 2020) and estimated litigation penalties (Note 18; Item 7); coal still
  supplies most of DTE Electric's own generation (Monroe alone 36% in 2025, Item 1) until 2032.
- **Integrity facts recorded at Q5** were judged there (the file reached Q5); no further integrity flag is added.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 721fe7b5); written question by question; committed after Step 0 and
      Q1, after Q2, after Q3 and Q4 together (one commit, not two: a deviation from write-early, stated), after Q5 and Q6
      together (the same), after Q7 with the buyback line written back into Q6, and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's (not touched); the
      run binds only once folded into the register by the dispatcher (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One directory listing of `Test Runs/`
      showed other run-file names (declared under contamination at the top, not used); commit subjects and the adopted
      utility case's list of names were seen and not used.
- [x] Every v5 id resolves (check script `check_run.py` in the research folder: every M/L/R id in `principle_ledger_v5.csv`,
      every quoted fragment beside an id found in that row, no E-ids); every id sits beside a quotation of its own row; every
      filing fact carries its document and accession; peer figures are XBRL transcription, flagged.
- [x] The order was kept; the first failing STOP (Q7) closed the run; nothing after it is a clearance. The Q7 arithmetic was
      computed during the Step 0 reading, before Q1 to Q4 closed, and its script and output are headed COMPUTATION, NOT A
      CLEARANCE (operator rule 3); it carried no entry language and was not used before Q7.
- [x] Owner cash after every real cost from the filed cash flow statements, never a net-income proxy (operator rule 5);
      maintenance guessed and stated; stock pay deducted; the sovereign from the US Treasury; the price from an aggregator,
      flagged.
- [x] Contrary evidence written down as found (foundations, Q3 to Q6); the facts for later questions are under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor rule arises.
- [x] `tools/run.py` produced no arithmetic line (UNRESEARCHED); nothing it prints was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (see the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Net or gross debt credit.** Q7, The regulated utility, credits "the long-term debt raised over the window"; it does not
say whether redemptions are netted. Gross issuance ($14,300M) would credit the refinancing of old debt against new
spending; this run netted ($7,667M) and said so. (2) **Which "business" supplies the debt share** when the filing states no
allowed structure: the consolidated parent (69.4%, inflated by parent-level debt carrying subsidiary equity) or the
regulated subsidiary (55.3%). Here neither binds, but on a utility with less borrowing over the window the choice would
decide the credit. (3) **The debt credit inside the maintenance-only case.** The rule says the credit is against "the capital
spending it funded" but not how it splits between the maintenance case and the growth spending; this run charged the
maintenance case in full to the equity and set all the credited debt against growth spending, since in a no-growth utility
the debt does not rise. A run that spreads the same $7,667M across maintenance and growth spending in proportion would raise
the no-growth figure and lower the growth case; the framework should say which. (4) **A spin-off inside the window** is not named in
specific (c), which covers acquisitions and mergers only; this run used the years after the separation as a CONVENTION of
its own. (5) **"Sales" in specific (f)** for a company with a gross-revenue trading arm: consolidated revenue fell over the
window on gas prices while the utility grew; this run used utility revenue, confessed. (6) The template's
`tools/run.py` step yields nothing for this filer (utility capital spending carries the filer's own tags), so every
arithmetic line was taken by hand; the tool's guard should say so rather than "UNRESEARCHED", which reads like a verdict.
(7) Q6's "candidate second STOP" for serial issuance is still unresolved, and a utility that plans to sell shares every
year to fund a regulated rate base is the case on which it would be decided.
