# Company Run — CMS Energy Corporation (NYSE: CMS) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run, written by the analyst under the brief of 2026-10-18 (which departs from the canonical brief only in
having the analyst derive the lines of evidence and the competitors from the filing). Template copied before any fetch
(commit 72164472).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. **Filled at the fold, 2026-10-18, after the run was committed (272cfa86):** not held; CMS Energy (CMS) does not appear in `PORTFOLIO.md` as a holding (the ticker string appears there only inside another company's row, as the abbreviation "CMS-only").

**Contamination, declared as found, not used.** (1) A directory listing of `Test Runs/` made to confirm this file's name
showed the names (only) of other run files and research folders dated 2026-10-18 (twenty-two other companies, many of them
utilities, and an ADDENDUM of the same date); none was opened. (2) The session context carried recent commit subjects of
another company's overnight run and a memory index line about the queue and the opportunity set; not used. (3) The
governing framework's own paragraph on the regulated utility records that sixteen utilities run on 2026-10-17 and
2026-10-18 showed a fair price that was not positive on the all-equity basis; that sentence is part of the governing text,
read as such, and no run file was opened. No file about CMS under any name was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $68.70 (close 2026-10-16, the last trading day before this run; printed by `tools/run.py`; **aggregator, live
  quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: **313,577,136 CMS Energy common shares** at 2026-07-13 (10-Q for the
  quarter to 2026-06-30, filed 2026-07-28, accession `0000811156-26-000028`; `python Screens/cover_shares.py CMS`). The
  script also printed 84,108,789 shares as a second "class": that is the common stock of Consumers Energy Company, the
  co-registrant, all of it held by CMS Energy ("There were no shares of Consumers common equity held by non-affiliates", 10-K
  cover, `0000811156-26-000004`); it is not added. Checked against the balance sheet: "outstanding 313.6 shares in 2026 and
  306.4 shares in 2025" (millions; 10-Q balance sheet). Issuance after the 10-Q: the 10-Q says of the $3 billion program of
  May 2026 "There have been no sales of securities under this program", and that the 2023 program is "fully utilized"
  (6.5 million shares issued in the half year at a weighted $75.80). No 8-K after 2026-07-28 reports an issuance; shares
  sold at the market after that date would not appear until the next 10-Q, so the count may be slightly low. The authorized
  common was raised from 350.0 to 700.0 million shares in 2026 (10-Q balance-sheet caption; 8-K of 2026-05-13, items 5.03
  and 5.07, `0001104659-26-060230`). The November 2025 convertible notes pay principal in cash, with only the excess
  settled in shares (10-Q, EPS note).
- **Market cap:** 313.577M x $68.70 = **$21,543M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16
  (issuing authority; printed by `tools/run.py` from `tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-02-10, `0000811156-26-000004` (Items 1, 1A, 3, 5, 7,
  8: the statements, Notes 3, 5, 12, 13, 17); 10-Q for the quarter to 2026-06-30, filed 2026-07-28,
  `0000811156-26-000028`; proxy (DEF 14A) filed 2026-03-26, `0000811156-26-000015`; 10-K for FY2022, filed 2023-02-09,
  `0000811156-23-000014` (cash flows 2020 to 2022, segments 2020 to 2022, MD&A on 2022 operating cash); 10-K for FY2020,
  filed 2021-02-11, `0000811156-21-000016` (cash flows 2018 to 2020); 10-K for FY2017, filed 2018-02-14,
  `0001104659-18-009493` (cover price); 8-Ks: 2026-02-05 earnings release and presentation (`0001104659-26-010603`,
  exhibits 99.1 and 99.2, slides read as images), 2026-07-28 earnings release (`0001104659-26-087288`, exhibit 99.1),
  2026-06-03 CFO succession (`0001104659-26-070037`), 2026-02-20 two directors elected (`0001104659-26-017913`).
  **One figure cross-checked against the filed statement:** net cash provided by operating activities, 2025, **$2,235M** on
  the filed Consolidated Statement of Cash Flows (10-K, `0000811156-26-000004`) equals the XBRL value `tools/run.py`
  read. Capital expenditures 2025 ($3,824M) are not in the XBRL element the tool reads after 2022; they were taken from the
  filed statement.
- `python tools/run.py CMS`, arithmetic lines only (Part VII): it printed the 2020 to 2022 window only, because capital
  spending is tagged under another element after 2022 ("the window ends at 2022-12-31"); every figure below for 2023 to
  2025 is from the filed statements. Stock pay "n/f" in XBRL; read from Note 12: compensation expense recognized $22M,
  $26M, $28M, $27M, $25M for 2021 to 2025 (`0000811156-23-000014`, `0000811156-26-000004`). The tool's ten-year balance-sheet
  table is used at Q4 and checked against the filed balance sheets for 2025 and 2024. Nothing it printed as a rule, id,
  floor or verdict was read. Raw output: `Test Runs/_research 2026-10-18 CMS/run_py_output.txt`.

**The lines of evidence this name needs, chosen from the 10-K's Items 1, 1A and 7, and why.** Item 7 names what drives the
business: "regulation and regulatory matters", "state and federal legislation", "economic conditions", "load growth",
"weather", "energy commodity prices", "interest rates", "their securities’ credit ratings" (`0000811156-26-000004`). From
that list and the risk factors the run reads: (1) **the regulator and the rate cases**: the Michigan Public Service
Commission sets "Consumers’ electric and gas retail rates" which "cannot be changed without regulatory authorization"
(Item 1A); allowed against requested returns and amounts, case by case; (2) **the capital plan against operating cash**:
$24.1B at Consumers and $25.8B in all for 2026 to 2030 (Item 7), against operating cash of about $2.2B a year; (3) **debt,
its growth and its covenants** (Item 7, the covenant table; Note 5); (4) **share issuance**, since the 8-Ks name equity
programs of $1B and $3B; (5) **securitization** of retired plant (Note 3, Note 5); (6) **competition the filing names**:
Retail Open Access capped at 10 percent, municipal utilities and franchises, distributed generation, large loads bought
at wholesale (Item 1, Item 1A); (7) **the J.H. Campbell emergency orders** and their cost recovery at FERC (Item 7, 10-Q);
(8) **the non-utility segment**, NorthStar Clean Energy (Item 1; the July 2026 release); (9) **long-term purchase
commitments**, $17.0B of capacity and energy payments through 2060 (Item 1). Data-centre load is read as part of (2) and
(6).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether the buyer would be content to own this "if the market closed for five
years" **[M1997-109]**, and for a regulated utility the business is the rate base and the return a commission allows on it,
so the reading is of the commission's record, not of the quotation. No macro forecast enters: interest rates are named by the
filer as a driver, and the run carries them only as a property of the business (the cost of the debt that funds the plant),
never as a forecast, since "macro conclusions are — just never enter into the discussion" **[M2000-094]**. Who is paid to
tell you: the earnings releases and the presentation are written for "analysts and investors" and feature an adjusted figure
and a growth target; the run reads the filed statements first and treats the presentation as the company's own advocacy,
"don’t ask the barber whether you need a haircut" **[M2011-083]**. Margin of safety is an attitude here: if the case needs a
pencil it is "too close to think about" **[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]**: (a) the
2025 electric rate order granted $277M of a request the company had put at $436M (later revised), at 9.90 percent against
10.25 percent asked (10-Q, `0000811156-26-000028`); (b) the plan needs outside money every year: "~$700" million of planned
equity in 2026 and "~$750/yr" over the long-term plan (presentation slide 12, `0001104659-26-010603`), and the authorized
shares were doubled; (c) the company's proxy boasts "23 years of meeting or exceeding our adjusted earnings guidance"
(DEF 14A, `0000811156-26-000015`) and a slide shows adjusted earnings rising "for over two decades, regardless of conditions"
(slide 15); (d) five-year total return to 2025 was 134 against 164 for the S&P 400 Utilities and 196 for the S&P 500 (10-K
Item 5); (e) operating cash fell to $855M in 2022 on "gas purchased at higher prices and underrecovery of power supply
costs" (FY2022 10-K, `0000811156-23-000014`); (f) the U.S. Secretary of Energy has kept the J.H. Campbell coal plant running
past its approved retirement under five 90-day orders, and "there is not currently a FERC-approved MISO Tariff for recovery
of compliance costs" (10-K Item 1A); (g) in July 2026 the company announced it is "exiting non-utility renewables
development" at NorthStar (`0001104659-26-087288`).

## THE STANDING RULE
The rule binds the buyer: "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**.
Owning a part-interest in CMS, bought with the buyer's own money and no borrowing, sized so that a
fall of half or more would cause no forced sale **[M2020-022]**, puts no ruin on the buyer; nothing in the purchase gives
anyone "the right to cash out" against the buyer **[L2014-024]**. The target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**. **The key variables** **[M1998-044]**, from the filing: (1) the rate base, which the
  filer expects to grow "more than 8 percent" a year in the 10-K and "more than 10 percent" in the 10-Q of July 2026, on a
  $24.1B five-year plan at Consumers; (2) the return the commission allows on the equity part of it: 9.90 percent in the
  2024 and 2025 electric orders, 9.80 percent in the 2024 gas order (10-K Item 7; 10-Q); (3) the share of each request the
  commission grants, and the lag; (4) the debt and equity that fund the plan, and so the number of shares; (5) volumes,
  which the filer expects to grow for electricity and stay "stable" for gas, with weather moving any one year. **Are they
  foreseeable?** The return on the regulated part is the most foreseeable kind the rows name: "when you get an allowed
  return in the electric utility you’re almost certain of earning it, I mean, if you behave yourself" **[M2010-037]**. The
  past statements tell the future ones in the sense the rows ask **[M2008-033]**: a decade of filings shows rate base,
  earnings and debt rising together, with the same commission and the same mechanisms (rate cases on forward test years,
  power-supply and gas-cost recovery clauses). What cannot be foreseen with the same confidence is the regulatory climate,
  which the rows themselves say can turn: "In such jurisdictions, it is difficult to project both earnings and asset
  values in what was once regarded as among the most stable industries in America." **[L2023-011]**; the 10-K's own risk
  factor says regulators "could face competitive or political pressures to avoid or limit rate increases" on
  "affordability concerns". The run finds no fact in the filings read that puts Michigan among the jurisdictions of
  L2023-011 (no wildfire liability, no denied recovery of a major plant, returns allowed near 9.9 percent in each case
  read); it carries the climate to Q2 and Q9 as the framework directs.
- **Routing.** Not a business of fast change in the sense of Q1: the product is the delivery of electricity and gas over
  a grid and pipes that Consumers "has served Michigan customers since 1886" (Item 1). The energy transition (coal exit,
  9,000 MW of solar and 4,000 MW of wind planned, storage) changes what Consumers builds, not how it is paid: new plant
  enters the rate base, and new clean PPAs earn "a return equal to its pre-tax weighted-average cost of capital" (Item 7).
  **A holding company read by its parts** (Q1, Q2's business of parts): electric utility 61 percent of five-year segment net
  income, gas utility 34 percent, NorthStar 5 percent (table at Q2). The deciding part, the electric utility, and the gas
  utility are understood by the tests above. NorthStar does not decide.
- **VERDICT: IN.** The ten-year economics of a Michigan rate-regulated electric and gas utility can be written down: a
  larger rate base earning near what the commission allows, financed by debt and new shares in proportions the filings
  state **[M2012-065]**, **[M2010-037]**. The regulatory climate is the open variable, carried forward, not hidden **[L2023-011]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table** (segment net income available to common stockholders, the measure the filer reports for every year of
the window; FY2022 10-K `0000811156-23-000014` for 2021 and 2022, FY2025 10-K `0000811156-26-000004` for 2023 to 2025;
USD millions):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| Electric utility (Consumers) | 565 | 567 | 550 | 681 | 719 | 3,082 | 61% | franchised distribution; generation protected by a statutory cap | **yes (more than half)** |
| Gas utility (Consumers) | 302 | 378 | 315 | 328 | 409 | 1,732 | 34% | franchised distribution, transmission and storage | no |
| NorthStar Clean Energy | 23 | 34 | 67 | 63 | 71 | 258 | 5% | none found: it "competes with other energy developers, energy retailers, and independent power producers" | no |

Corporate interest and other is a cost of the parent, not a part. Under the business of parts (Q2, CONVENTION adopted
2026-10-06), the electric utility decides, since it carries more than half of five-year segment profit; the file closes on
its castle. The gas utility's castle is the same kind and is read with it. NorthStar, which does not decide and shows no
castle, is carried to Q7 as an ordinary business at no growth; the filer announced on 2026-07-28 that it is "exiting
non-utility renewables development and retaining Michigan-based assets" (`0001104659-26-087288`).

**The castle tests, with the filing fact for each.**
- **The key factors and how permanent they are** **[M1995-038]**. Consumers serves "6.8 million of Michigan’s 10 million
  residents", has served Michigan "since 1886", and its distribution system is 82,854 miles of overhead lines, 10,027 miles
  underground and 28,433 miles of gas mains, mostly "below or adjacent to public roads" under easements and municipal
  franchises (Item 1). Its rates are set by the MPSC and "cannot be changed without regulatory authorization" (Item 1A).
  What keeps the castle standing is the franchise and the commission's compact; it depends on law and on the commission,
  not on the genius of the lord.
- **The attacker with money** **[M2011-015]**. A rival with any sum could not lay a second grid of that size through the
  same streets under the same franchises; this is the railroad's case, not the airline's: "You really couldn’t create
  another railroad" **[M2013-054]**. The attacks the filing names are of another kind: Retail Open Access, municipal
  utilities, customer self-generation, and large loads buying at wholesale (below).
- **Pricing power and the agony before a rise** **[M2005-020]**. The price is set by the commission in a formal case
  almost every year, and the commission cuts the asks: 2024 electric, $325M sought, $176M granted at 9.90 percent against
  10.25 percent asked; 2024 gas, $248M sought (revised to $217M), $157.5M granted at 9.80 percent; 2025 electric, $436M
  sought (later refined), $277M granted at 9.90 percent (10-K Item 7 and Note 3; 10-Q, `0000811156-26-000028`). The
  business has no pricing power of its own; it has the right to ask, and a record of being granted most of the return asked
  and roughly half to three-quarters of the money. The filer's own risk factor names the pressure: regulators could limit
  increases on "affordability concerns" (Item 1A).
- **Would the customer still choose it over the low bid** **[M2017-009]**. For delivery, the customer has no choice. For
  generation, the filing answers the question: Michigan law lets customers buy from alternative suppliers "in an aggregate
  amount capped at 10 percent of Consumers’ sales", deliveries under the program "were at the 10‑percent limit", and "The
  proportion of Consumers’ electric deliveries under the ROA program and on the ROA waiting list is over 10 percent"; the
  rivals "charge market-based rates, putting competitive pressure on Consumers’ electric supply" (Items 1 and 1A). Where the
  law lets the customer take the low bid, enough customers take it to fill the cap and form a queue. The generation half of
  the castle is a statute, not a preference.
- **Ask the competitors; the competitor row.** The 10-K names no rival company as a competitor. It names classes:
  "alternative electric suppliers", municipalities, "customer self-generation", data-centre relocation; for gas "GCC and
  transportation programs; system bypass" and "propane, oil, and electricity"; for NorthStar "other energy developers".
  Companies named in the 10-K in other roles (DTE Electric, co-owner of Ludington; Panhandle Eastern and Trunkline,
  pipelines; the MCV Partnership, a supplier; Wolverine Power and the Michigan Public Power Agency, joint owners) are not
  named as rivals. **CONVENTION of this run:** the comparators are three SEC filers that are rate-regulated combination
  electric and gas utilities in the MISO region: **DTE Energy** (the other large MPSC-regulated utility, so the closest test
  of the same commission), **Ameren** and **WEC Energy Group**. Rationale: the filer names no rival, its returns are set by a
  commission, and what comparators can show is what the same and neighbouring commissions let a utility earn over a span.
  Metric: net income available to common (or net income) over average stockholders' equity, from each filer's XBRL
  (transcription; the peers' filed statements were not read; latest vintages: DTE `0000936340-26-000054`, Ameren
  `0001002910-26-000009`, WEC `0000783325-26-000018`, CMS `0000811156-26-000004`):

| year | CMS | DTE | Ameren | WEC |
|---|---|---|---|---|
| 2016 | 13.5% | 9.7% | 9.3% | 10.6% |
| 2017 | 10.6% | 12.2% | 7.3% | 13.0% |
| 2018 | 14.3% | 11.3% | 11.0% | n/f |
| 2019 | 13.9% | 10.7% | 10.6% | n/f |
| 2020 | 14.4% | 11.3% | 10.2% | 11.5% |
| 2021 | 22.2% (EnerBank sale gain) | 8.6% (spin-off year) | 10.6% | 11.9% |
| 2022 | 12.1% | 11.3% | 10.6% | 12.4% |
| 2023 | 12.0% | 13.0% | 10.5% | 11.2% |
| 2024 | 12.6% | 12.3% | 10.1% | 12.3% |
| 2025 | 12.2% | 12.2% | 11.4% | 11.6% |

  (WEC 2020 to 2025 on equity including noncontrolling interests, its only tagged equity series after 2017; n/f = not found
  in the tag read.) CMS's consolidated return runs above the 9.80 to 9.90 percent its commission allows on Consumers' equity:
  part of the gap is the parent's own debt, whose covenant ratio is debt to capital "0.56 to 1.0" for CMS parent only against
  "0.51 to 1.0" for Consumers (10-K Item 7), and part is NorthStar and tax credits. The field earns about ten to thirteen
  percent on book equity in every year shown, with no year of collapse in the span.
- **Widening or narrowing** **[M1999-108]**. On the evidence read: allowed returns flat at 9.80 to 9.90 percent across the
  three orders of 2025 and 2026, below the 10.25 percent asked each time; the ROA queue standing above the cap; the 2023
  Energy Law adding obligations (50 percent renewable by 2030, 100 percent clean by 2040) that enlarge the rate base; a
  large-load tariff with "a minimum 15‑year contract" for data centres (Item 7). Neither a widening nor a narrowing is shown
  over the span read; the compact is stable in the orders and under pressure in the filer's own risk words.
- **What could destroy, modify or reduce it** **[M2000-014]**: (1) Michigan lifting the 10 percent cap, or a "ROA-like
  community solar program"; (2) municipalities creating utilities or impairing franchises; (3) distributed generation, its
  cap raised to 10 percent of peak load; (4) FERC asserting jurisdiction over large-load interconnections or letting large
  loads buy at wholesale; (5) a commission turning against the company on affordability; (6) federal orders that keep plant
  running without a tariff to recover the cost (J.H. Campbell: a net $42M cost of the first order sought at FERC, pending;
  10-Q). Each is a filed risk; none is shown under way at a scale that opens the castle in the span read. The rows' own
  warning about this class of castle is carried: "I did not anticipate or even consider the adverse developments in
  regulatory returns" **[L2023-011]**.

**The field's returns over the last full cycle, judged in words.** The span 2016 to 2025 includes the 2020 recession and
pandemic, the 2022 gas-price spike, and the warm or stormy years the filer itself marks; the regulated field's book returns
held at about ten to thirteen percent through all of it, set by commissions. That is a fair return, not a rich one, which
is what the rows say of the class: "You can't expect to earn outsized profits in regulated utilities, but the industry
offers owners the opportunity to deploy large sums at fair returns" **[L2005-005]**. Q2's list rules OUT the standing castle
that protects only ordinary returns and names, in the same item, the exception: a return set by a regulator is carried to
Q3 as a second best (the framework's item cites **[M2009-104]** and **[L2009-012]**). The deciding part's return is set by a
regulator, so the item does not close the file; the return goes to Q3.

**VERDICT: IN.** The deciding part's castle is standing on the evidence: a franchised grid that no attacker with money
could duplicate **[M2011-015]**, **[M2013-054]**, under a commission that allowed 9.80 to 9.90 percent in each order read;
the gas part is of the same kind. The castle protects a regulated, fair return, which Q2 carries to Q3 rather than closing on
**[L2005-005]**. The cracks are recorded and carried, not credited away: the generation half stands on a statute whose cap
customers have filled (the low-bid test fails where the law permits it **[M2017-009]**), the price is set by a commission
under affordability pressure **[M2005-020]**, and the rows' own utility mistake **[L2023-011]** goes to Q9. NorthStar (5
percent) shows no castle and goes to Q7 at no growth.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **What the capital needed earns** **[M2010-090]**. Total plant, property and equipment (net, with construction work in
  progress) was $21,039M at the end of 2020 (FY2020 10-K, `0000811156-21-000016`) and $30,680M at the end of 2025 (FY2025
  10-K): **+$9,641M, or 46 percent, in five years.** Operating income, which is after depreciation, was $1,230M in 2020 (as
  restated with EnerBank in discontinued operations, FY2022 10-K) and $1,727M in 2025: **+$497M, or 40 percent.** On the
  measure the rows give for a utility's added capital, "It’s measured by the operating earnings after depreciation"
  **[M2014-086]**, the added plant earned about **5.2 percent before tax** ($497M on $9,641M), and the whole plant about 5.8
  percent in 2020 and 5.6 percent in 2025 before tax. Part of the 2025 plant ($3,052M of construction work in progress) is
  not yet in rates, so the incremental figure understates what the plant will earn once it is; part of 2025's operating
  income came from "favorable weather" (Item 7), which overstates it. The equity slice earns more, because the commission
  allows 9.80 to 9.90 percent on Consumers' equity and the rest is funded with debt at 3.5 to 5.3 percent on the
  securitization bonds (Note 5) and the rates on the first mortgage bonds: the book return on CMS's equity of about twelve percent (Q2) is
  a regulated return levered at the parent as well as at the utility, which the rows tell the reader to strip out before
  crediting a high return: rule out "a cyclical peak in earnings, a monopolistic position, or leverage" **[L1994-009]**.
- **Reinvestment to stand still and to grow.** Depreciation and amortization ran $1,114M to $1,306M a year in 2021 to 2025;
  capital spending (excluding finance leases) $2,076M to $3,824M, plus $107M to $214M a year of cost to retire property and
  the $812M Covert plant bought in 2023 (filed statements). Operating cash, after interest, covered none of it with room to
  spare: operating cash less all capital spending was **negative in every year from 2022 to 2025** ($855M against $2,481M in
  2022; $2,235M against $4,038M in 2025). The plan ahead is larger: $4.4B in 2026 rising to $6.2B in 2028 (Item 7). The
  filer's maintenance spending is not stated as such; the depreciation charge is taken as the stated guess for it, the
  rows' own proxy, "not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**,
  with the reason for a utility: spending equal to depreciation leaves net plant, and so the rate base, about flat. Much of
  the rest is compulsory in the filer's own words, set by the 2023 Energy Law (renewable and clean standards, storage),
  reliability orders and pipe replacement; the rows' warning is "we have tried to avoid places where there was a lot of
  compulsory reinvestment just in order to stand still" **[M1997-016]**, and the utility case is named outright: "To earn
  more, their owners must invest more" **[L2011-019]**.
- **The growth arithmetic and its caps.** The filer expects rate-base growth of "more than 8 percent" a year (10-K) and
  "more than 10 percent" (10-Q, July 2026). Growth here is bought with capital at the regulated rate; it is the "good"
  savings account of the rows at best, one that "pays an attractive rate of interest that will be earned also on deposits
  that are added" **[L2007-010]**, and only if the rate allowed is attractive at the price paid for the deposit, which is a
  Q6 and Q7 matter (new shares are sold at more than twice book: common equity $9,550M against a market value of $21,543M).
  Rising earnings alone prove nothing where the capital rises with them: "we’re not earning a higher rate of return on
  capital than we were when we started. We just put way more capital into the business" **[M2023-081]**. The growth carried
  at Q7 is capped by what the business has shown, not by the plan.
- **WEIGHS AGAINST.** A capital-heavy second best in the rows' own terms **[M2018-055]**, **[M2009-104]**: a cash-consuming
  business **[M2012-057]** whose added plant earns about five percent before tax on the operating measure **[M2014-086]**,
  with the commission's 9.80 to 9.90 percent on the equity slice as the reasonable return that keeps it from the gruesome
  account, and with the reinvestment largely compulsory **[M1997-016]**, **[L2011-019]**. The "little or no debt" criterion
  is applied at Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL; 2024 and 2025 checked
  against the filed balance sheet, `0000811156-26-000004`; USD millions):

| year-end | total assets | stockholders' equity | cash | long-term debt (non-current) | retained earnings |
|---|---|---|---|---|---|
| 2016 | 21,622 | 4,253 | 235 | 8,640 | -616 |
| 2017 | 23,050 | 4,441 | 182 | 9,123 | -531 |
| 2018 | 24,529 | 4,755 | 153 | 10,615 | -271 |
| 2019 | 26,837 | 5,018 | 140 | 11,951 | -25 |
| 2020 | 29,666 | 5,496 | 168 | 13,634 | 214 |
| 2021 | 28,753 | 6,631 | 452 | 12,046 | 1,057 |
| 2022 | 31,353 | 7,015 | 164 | 13,122 | 1,350 |
| 2023 | 33,517 | 7,544 | 227 | 14,508 | 1,658 |
| 2024 | 35,920 | 8,230 | 103 | 15,194 | 2,035 |
| 2025 | 39,941 | 9,144 | 509 | 17,807 | 2,443 |
| 2026-06-30 (10-Q) | 40,905 | 9,774 | 241 | 18,172 | 2,546 |

  **What moved and why.** Assets nearly doubled, almost all of it plant. Long-term debt roughly doubled with them ($8.6B to
  $18.2B, plus a current portion of $870M at mid-2026; $585M of securitization bonds at the end of 2025 sit within the
  total). Equity doubled
  ($4.3B to $9.8B), but not from retained earnings alone: retained earnings were a deficit of $616M in 2016 (the residue of
  older losses) and reached $2.5B; the rest is paid-in capital from new shares, other paid-in capital rising to $7,036M at
  mid-2026, with shares outstanding up from 279.2 million (2016) to 313.6 million (mid-2026). Cash is kept low, a few hundred
  million against $1.0B of debt due within the year; the company relies on revolvers ($2.1B available at the end of 2025)
  and the markets (Item 7). Debt to equity has stayed near two to one throughout. Regulatory assets ran $2.5B (2019) to
  $3.8B (2024) and $3.5B (2025) against regulatory liabilities of $4.2B; they jumped in 2022 with the retirement and
  securitization of the Karn coal units and fell in 2025, so they are not "building up suspiciously high" **[M1995-064]**.
  No goodwill of consequence. EnerBank, a bank, was owned until its sale in 2021, which is why 2021's assets fell and
  equity jumped (the gain). **What the figures cannot say** **[M2025-032]**: what the commission will allow on the plant now
  being built; the balance sheet shows the capital, the commission sets its return.
- **The real costs.** Depreciation is charged and is a real cost **[R1996-023]**; for a utility the commission sets the
  rates and includes removal costs in them (Note 3, AROs; a depreciation case filed December 2025 asks for $34M more a
  year). Stock pay is small and expensed: $22M to $28M a year (Note 12). Pensions: the plan is overfunded (postretirement
  benefit asset $1,957M at the end of 2025), and the commission defers pension expense above or below rates for ten-year
  recovery (Note 11), so pension income ($186M of "non-operating retirement benefits, net" in 2025) is real only as far as
  the commission lets it stay with the owners. Deferred taxes: the company pays almost no cash income tax ("Income taxes
  paid (proceeds from sale of renewable energy tax credits), net" of $15M, minus $69M and minus $20M in 2023 to 2025),
  because of accelerated tax depreciation and transferred credits; for a utility this is not owner's money, "that helps our
  customer and it doesn’t help us, basically" **[M2015-030]**, and the run counts taxes as paid with that note. Tax-loss and
  credit carryforwards are small ($139M, credits expiring 2038 to 2045; Note 13), so the carryforward convention does not
  bite. No EBITDA in the filer's mouth in the documents read.
- **The habits, recorded here and carried to Q5.** (1) **Guidance, and making it**: the proxy states "marking 23 years of
  meeting or exceeding our adjusted earnings guidance" (DEF 14A, `0000811156-26-000015`); the February release is headed
  "CMS Energy Exceeds Earnings Guidance in 2025, Raises 2026 Adjusted EPS Guidance" and reaffirms "long-term adjusted EPS
  growth of 6 to 8 percent, with continued confidence toward the high end" (`0001104659-26-010603`); the presentation's
  slide 15, "Industry-Leading Financial Performance", draws adjusted earnings per share as a straight rising line from 2003
  through recessions, a pandemic, five chief executives, governors and commissions of both parties, and every weather year,
  captioned "for over two decades, regardless of conditions". (2) **An adjusted figure featured**: the release's first
  figure after reported EPS is "adjusted earnings per share for 2025 were $3.61", against reported $3.53; the exclusions
  ($0.08) are small and reconciled, and include "major enterprise resource planning software implementations", a real and
  recurring kind of cost, and a "State tax policy change". (3) **Pay on the same figure**: 70 percent of the annual bonus
  rests on "Annual Incentive EPS (CMS Adjusted (non-GAAP) EPS)", target $3.54, achieved $3.61, paid at 150 percent (DEF 14A).
  These are a WEIGHING against at Q4 **[M1994-018]** and are carried to Q5 as evidence on the people, under the framework's
  make-the-numbers paragraph.
- **The tells that live in the accounts.** None found that rises to confusion or suspicion: regulatory assets are
  commission-approved and not building; receivables and inventories move with gas prices and the recovery clauses, as the
  filer explains (2022's draw "due primarily to gas purchased at higher prices and underrecovery of power supply costs",
  FY2022 10-K, reversed in 2023 and 2024); reserves are not seen moving with a stock sale; the accounts can be followed.
  The levers that smooth a utility's reported year are visible in the 2025 MD&A and are regulatory, not hidden: "2025
  deferred storm expense", "gain amortization in lieu of rate relief" on the gas side ($30M of ASP gain amortized), and
  deferred accounting for vegetation-management and ERP costs granted in the 2025 order (10-Q). They are named here because
  they are the means by which a regulated utility's year can be brought to a target; they are not, on what was read,
  misstatements.
- **VERDICT on the accounts: IN (not confused, no suspicion from the statements themselves); WEIGHS AGAINST** on the habits
  of guidance, a featured adjusted figure, and pay on it, carried to Q5 **[M1994-018]**, **[L2016-006]**. Recast earnings for
  Q7: owner cash from operating cash after interest and the company's own tax as paid, less stock pay, less preferred
  dividends and distributions to minority partners, less depreciation as the maintenance guess, with all spending beside
  (COMPUTATION below).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* the hand is a franchise under one
  commission; the play has been to grow the rate base and win most of each ask (Q2), keep the plant running, and keep credit
  "solid investment grade" (presentation slide 12). The rate orders read granted 9.80 to 9.90 percent against 10.25 percent
  asked, about what DTE, under the same commission, has earned on its book over the span (Q2 table). *How they treat the
  owners:* the proxy (read below), the issuance (carried to Q6, after the stop), the reports.
- **The record read for integrity, both ways.** For the people: the accounts can be followed and the adjustments to them are
  small and reconciled (Q4); bad news is reported plainly in the releases (second-quarter 2026 adjusted EPS "$0.37, compared
  to $0.71", first half "$1.50 per share in 2026 compared to $1.73", `0001104659-26-087288`) and in the 10-K (the shortfalls
  in every rate order, the Campbell costs not yet recovered); the chairman is independent and separate from the chief
  executive (DEF 14A); directors and officers may not pledge or hedge the stock; related-party transactions need audit
  committee approval; no restatement, enforcement action or related-party dealing was found in the filings read; the chief
  executive holds 644,070 shares including restricted stock (DEF 14A) against total 2025 pay of $10,534,039. Against the
  people, the habits carried from Q4, read with the rest:
  1. **The declared target, made every year, and featured.** "23 years of meeting or exceeding our adjusted earnings
     guidance" is in the first sentence of the proxy's executive summary of 2025 ("2025 Successes"); the year's release leads with exceeding guidance and
     raising the next; the slide draws the line "for over two decades, regardless of conditions", across five chief
     executives. The rows' words for exactly this: "we become downright incredulous if they consistently reach their
     declared targets. Managers that always promise to "make the numbers" will at some point be tempted to make up the
     numbers." **[L2002-041]**; and of the habit handed from one chief executive to the next: "it’s a terrible problem the new
     CEO has coming in after a previous CEO has said the important thing to do is to hit your earnings targets" and "it’s a
     totally destructive policy" **[M2022-054]**.
  2. **The means to make it are in the filings.** A regulated utility's year can be shaped by what is deferred and when, and
     the 2025 and 2026 filings show the instruments in use: a "2025 deferred storm expense", a "gain amortization in lieu of
     rate relief", deferred vegetation-management and ERP costs, a return to normal weather that the company itself sizes at
     minus 22 cents a share for 2026 (slide 11), against a guidance range 7 cents wide. Each is commission-approved and disclosed; none is a misstatement
     on what was read. But the rows' warning is about the behaviour that targets breed, not only the accounting: "they
     corrode CEO behavior" and "CEOs engaged in uneconomic operating maneuvers so that they could meet earnings targets they
     had announced" **[L2000-039]**; the offence "has been encouraged by the scourge of earnings "guidance" and the desire of
     CEOs to "hit the number."" **[L2019-006]**.
  3. **An adjusted figure in the headline, and the bonus paid on it.** The adjusted figure leads the release, and 70 percent
     of the annual bonus is paid on it, at 150 percent for 2025, against a target the company sets inside its own guidance
     range. "a management that regularly attempts to wave away very real costs by highlighting "adjusted per-share
     earnings" makes us nervous" **[L2016-006]**; the excluded costs here are small, which lightens this count, not the first.
  4. **Emphasis on the stock's market.** "Industry-Leading Financial Performance", "premium growth" (slide 11), and a
     long-term growth promise "with continued confidence toward the high end": things "they do in public in relation to their
     investors and the promises they make" **[M2004-067]**.
- **The judgment.** Integrity is the STOP, and it is applied on doubt, not on proof: "If you’ve got doubts, forget it."
  **[M2013-088]**; "we rule out 90 percent of the times. And we may be wrong about a fair number that we’re ruling out. The
  important thing is whether the ones we’re ruling in we’re right about." **[M2007-092]**. On the record read, nothing shows
  the figures to be false, and the rest of the record is creditable. But this is not a borderline instance of the habit the
  rows distrust; it is the habit at its fullest, kept for twenty-three years through five chief executives, chosen by the
  company as its leading boast in the proxy and the annual presentation, paid for in the bonus, and served by instruments
  (deferrals, amortizations, regulatory timing) whose use in any one year a reader cannot see from outside. The rows do not
  say such a management is dishonest; they say it makes them "downright incredulous" **[L2002-041]**, that it will "at some
  point be tempted" **[L2002-041]**, and that the doubt is enough. Read honestly, that is doubt, and it is not cured by the
  clean accounts, because the rows place the danger in the behaviour the target breeds **[L2000-039]**, **[L2019-006]** and
  because "everybody mouths the integrity, even when it’s lacking" **[M2010-069]**. Ability, by contrast, WEIGHS FOR: rate
  cases run on a regular clock, constructive orders, credit kept, costs held ("Achieved >$100M of waste elimination
  savings", slide 3), though a business of this castle "doesn’t require good management" in the rows' sense **[M1996-037]**.
- **VERDICT on integrity: OUT, on doubt** **[M2013-088]**, **[L2002-041]**, **[M2022-054]**; ability WEIGHS FOR. The file
  closes here. No misstatement was found; the doubt is the one the rows name for a management that always makes its declared
  number and features doing so. Everything below this line is NOT REACHED as a judgment; the figures the brief asks for are
  computed beneath the STOP under the heading the protocol requires.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED (closed at Q5). The buyback line and the facts found are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a clearance (closed at Q5). The range and the fair price the owner asked for are computed below under
COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (closed at Q5).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED (closed at Q5). Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (closed at Q5).

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (closed at Q5). No business the rows name for Q12 (casinos, tobacco, loading schemes, gambling dressed as
investing) is among CMS's businesses.

---
## COMPUTATION, NOT A CLEARANCE
*(Operator rule 3. The file closed at Q5. What follows is the arithmetic the owner asked for, built as Q7 would build it,
with no entry language and no verdict. The script is `Test Runs/_research 2026-10-18 CMS/valuation.py`.)*

**Basis.** The deciding part earns a return a regulator allows, so under Q7's paragraph on the regulated utility
(2026-10-18) the central figure is the **equity-only basis**: owner cash after interest and after the company's own tax as
paid, against the market value of the shares ($21,543M); the all-equity figure is beside it and never decides.

**The window, 2021 to 2025** (USD millions; filed cash-flow statements, FY2022 10-K `0000811156-23-000014` and FY2025 10-K
`0000811156-26-000004`):

| line | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| operating cash (as filed, after interest and tax paid) | 1,819 | 855 | 2,309 | 2,370 | 2,235 | 1,918 |
| less stock pay (Note 12) | 22 | 26 | 28 | 27 | 25 | 26 |
| less preferred dividends and distributions to minority partners | 0 | 14 | 22 | 22 | 24 | 16 |
| less depreciation and amortization (the maintenance guess, Q3) | 1,114 | 1,126 | 1,180 | 1,240 | 1,306 | 1,193 |
| **owner cash, maintenance only (equity-only)** | **683** | **-311** | **1,079** | **1,081** | **880** | **682** |
| changes in working capital and other assets and liabilities (in operating cash) | -46 | -1,113 | 416 | 262 | -61 | -108 |
| owner cash, maintenance only, before working capital | 729 | 802 | 663 | 819 | 941 | 791 |
| capital spending (excl. finance leases) | 2,076 | 2,374 | 2,407 | 3,018 | 3,824 | 2,740 |
| cost to retire property and other investing | 133 | 107 | 167 | 160 | 214 | 156 |
| businesses bought less sold (Covert 2023; EnerBank 2021 and 2022; ASP 2024) | -898 | -5 | 812 | -124 | 0 | -43 |
| long-term debt issued less retired, plus change in notes payable | 100 | 1,813 | 1,492 | 982 | 2,394 | 1,356 |

- **Working capital is counted** (specific (d)): the five-year average includes 2022's draw of $1,113M, which the filer ties to
  one event, "gas purchased at higher prices and underrecovery of power supply costs" (FY2022 10-K); it reversed in 2023 and
  2024. Interest is inside operating cash (interest paid $489M to $741M).
- **The debt credit** (Q7, the regulated utility): long-term debt raised over the window, net of retirements, $6,781M,
  credited against the fixed-asset spending it funded, up to the debt share of capital. The regulator's allowed debt share
  is not stated in the filings read; the business's own debt share at the latest filed date is 65 percent (debt and finance
  leases $19,301M against total equity $10,399M at 2026-06-30, 10-Q), and Consumers' covenant ratio is 0.51 (10-K). The cap
  is $9,940M at 65 percent, $7,799M at 51 percent; neither binds, so the credit is the $6,781M actually raised, $1,356M a
  year. It applies to the growth spending only: spending equal to depreciation leaves the rate base flat and needs no new
  debt, so the maintenance case takes no credit.
- **Owner cash.** Maintenance only (central, specific (e)): **$682M a year**. After all spending and the debt credit:
  $682M less the equity share of growth spending ($2,740M + $156M - $43M - $1,193M - $1,356M = $304M) = **$379M a year**
  (literal per-year figures 586, 152, 365, 249, 542). With the EnerBank sale proceeds left out of businesses sold, the
  equity share of growth spending is $484M and all-spending owner cash $198M a year.
- **Growth.** The maintenance-only series changes sign (2022), so specific (b) measures growth between the halves of the
  window: 2021 and 2022 average $186M, 2024 and 2025 average $981M, a rate of about 74 percent a year, which is meaningless;
  by (b) **the central range is the no-growth case alone, said so.** Beside it, with the one-event working-capital draw taken
  out of the growth measure only (specific (d)'s instruction to show the range at the business's working-capital intensity
  before the event, applied here to a middle year; see the framework notes), the series before working capital grew from
  $729M to $941M, **6.6 percent a year** (2.9 percent if 2021's $111M of EnerBank discontinued operations is removed from
  its base). Sales grew 3.9 percent a year ($7,329M to $8,539M); 6.6 percent for ten years would put owner cash at about 14
  percent of sales, against a highest share of 14.5 percent (2023) in the filings read, so the cap of specific (f) does not
  bite. Growth is charged with its spending: the growth case deducts the equity share of growth spending ($304M a year,
  growing with the business) for ten years, then no growth and no growth spending, at zero nominal growth after year ten.
- **NorthStar** is inside the consolidated figures; in the central no-growth case it is carried at no growth, as Q2
  directs for a part that does not decide.

**VALUE RANGE (equity-only, central), at the sovereign 5.43%:** no-growth case **$40.08 a share** ($682M / 0.0543 =
$12,567M, over 313.577M shares); the central range is that case alone. **Beside it** (working-capital event out of the growth
measure): **$40.08 to $57.55** (growth case $18,045M; $41.95 at 2.9 percent growth). Against **$68.70**. Width beside:
1.44 to 1. Also beside: all-spending owner cash at no growth, $22.25 ($11.64 with EnerBank left out); with deferred taxes
deducted as if paid ($168M a year average added back in operating cash), the no-growth case falls to $30.22.

**The floor, tested first.** Expected return at $68.70: **3.2 percent** a year on the no-growth case ($682M on $21,543M);
**4.7 percent** on the growth case beside (internal rate at which its stream is worth the price); 3.6 percent at 2.9 percent
growth. No case earns about ten percent at the price; every case is below the 5.43 percent bond as well. Q7, had it been
reached, would close **OUT** on the floor, the price standing above the top of every case.

**FAIR PRICE (a reporting figure, never a verdict; Part VII), equity-only basis, central: $21.76 a share** (the no-growth
case valued at ten percent, $682M / 0.10, over the shares; the central range has one case, so the average is that case).
Beside it, with the growth case: **$23.92**. **All-equity basis, beside:** owner cash before interest after the company's
tax, $682M + $601M average interest paid x (1 - 0.21) = $1,157M (21 percent is the federal rate the filer's own sensitivity
slide uses); at ten percent, $11,572M, less net debt $18,956M (debt and finance leases $19,301M less cash and restricted cash
$345M, 2026-06-30), preferred $224M and minority interests $625M: **-$26.26 a share**, not positive (-$38.01 with the growth
case, whose growth spending carries no debt credit on this basis). Tax treatment: the company's own tax as paid, near zero
in cash, with deferred taxes not treated as owner money **[M2015-030]**; no conversion. No cheap price is reported.

---
## THE BOX
**OUT at Q5** (integrity, on doubt: the make-the-numbers habit at its fullest, twenty-three years of meeting or exceeding
adjusted EPS guidance featured in the proxy and the presentation, the bonus paid on the same figure; no misstatement found).
COMPUTATION beside, not a clearance: equity-only value $40.08 a share (no-growth case alone; $40.08 to $57.55 with the 2022
working-capital event out of the growth measure) against $68.70; no case earns the floor at the price; fair price $21.76
equity-only ($23.92 beside), all-equity -$26.26.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; not weighed; the box is unchanged.)*
- **Q6, issuance.** Common shares 279.2M (2016), 294.4M (2023), 306.4M (2025), 313.6M (mid-2026); stock issued for
  $26M, $69M, $192M, $286M, $525M in 2021 to 2025 and $495M net in the first half of 2026 at a weighted $75.80; the 2023
  $1B program "fully utilized"; a $3B program from May 2026; "Planned equity issuance" of "~$700" million in 2026 and
  "~$750/yr" over the long-term plan (slide 12); authorized shares raised from 350.0M to 700.0M. New shares were sold at
  prices above the computed range above, which by the rows' own test does not harm continuing owners **[M1996-013]**; the
  rows' candidate second STOP on serial issuance **[L2014-015]** is carried, unresolved, in the framework's section VI.
- **Q6, buybacks (the line Q6's buyback test asks for, recorded back from the computation).** No buyback programme: "CMS
  Energy has no other publicly announced plans or programs that permit the repurchase of equity securities"; the only
  repurchases are shares withheld for tax on vested restricted stock (452 shares in the fourth quarter of 2025 at an average
  $71.05; 10-K Item 5). The bottom of the computed range is $40.08; those purchases sit above it.
- **Q6, retention.** Diluted EPS less dividends declared, 2020 to 2024: $1.01, $2.92 (EnerBank gain year), $1.01, $1.06,
  $1.27, a total of $7.27 a share retained; the share price on the cover dates moved from $58.42 (June 2020) to $69.28 (June
  2025), +$10.86 (10-K covers `0000811156-21-000016`, `0000811156-26-000004`). Five-year total return to 2025: 134 against
  164 for the S&P 400 Utilities and 196 for the S&P 500 (10-K Item 5). Dividend payout target "~60%" in 2026, "~55% over
  time" (slide 12); dividends declared rose every year, $1.24 (2016) to $2.17 (2025).
- **Q6, Part B.** Chief executive's 2025 total pay $10,534,039; 70 percent of the annual bonus on adjusted EPS, paid at 150
  percent; the long-term award on relative TSR and relative EPS growth against a peer group; pay benchmarked to a
  compensation peer group's median (DEF 14A). Chairman independent and separate. New CFO from inside (8-K of 2026-06-03).
- **Q8.** The 30-year Treasury yields 5.43 percent; the computed expected return at the price is 3.2 to 4.7 percent.
- **Q9.** Pre-tax earnings over interest **[L2012-002]** in 2025: ($1,248M + $789M) / $789M = 2.6 times. Long-term debt due
  in 2026 $1.0B, interest $0.8B, purchase obligations $2.4B, capital spending $4.4B, against operating cash of $2.2B: the plan
  needs the markets every year, which the filer states: "CMS Energy and Consumers rely on the capital markets to fund their
  robust capital plan" (Item 7). The parent "depends on dividends from its subsidiaries to meet its debt service" (Item 1A);
  parent debt to capital 0.56 against a covenant limit of 0.70. Purchase obligations total $20.6B, mostly long-term PPAs;
  capacity payments of $17.0B through 2060. One state, one commission: the rows' diversity point, "A catastrophic event can
  render a single utility insolvent" **[L2005-019]**. J.H. Campbell kept running under federal orders with cost recovery at
  FERC pending. The "little or no debt" criterion **[R1997-001]** is stated for whole businesses; debt is about twice equity.
- **Q12.** Coal generation continues at J.H. Campbell under federal emergency orders; none of the businesses the rows name.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 72164472); written question by question; committed after each,
      except that Step 0 with Q1, and Q3 with Q4, went in one commit each (37494bda, b92b4647).
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (not checked by the
      analyst); the fold is the dispatcher's.
- [ ] **Blind rule, breached in the letter once, declared:** before creating this file the analyst ran a directory listing of
      `Test Runs/` filtered to "2026-10-18" to confirm the name was free; it printed the names of other companies' run files
      and research folders of the same date (declared under contamination at the top). No other run file, holding review,
      `PORTFOLIO.md`, register, reading list or resume-state file was opened or searched. Nothing seen was used.
- [x] Every v5 id resolves (`check_cites.py`: ids found in `principle_ledger_v5.csv`, no E-ids, every quoted fragment beside
      an id found in that row); every filing fact carries its accession; numbers carry a filing or a CONVENTION.
- [x] The order was kept; the first STOP that failed (Q5) closed the run; nothing after it is a clearance; Q7's figures are
      under COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash from operating cash after every real cost (stock pay, preferred and minority distributions, depreciation
      as the stated maintenance guess, all spending beside), never a net-income proxy; the sovereign from the US Treasury;
      the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (foundations, Q2, Q4); the facts found for later questions are under AFTER THE
      STOP.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run before the final commit (result recorded in the commit message).
- Peers' figures are XBRL transcription only; their filed statements were not read (a limit, stated at Q2).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7 (b) against (d) for a middle year.** The maintenance series changes sign only because of 2022's gas-price
working-capital draw, which (d) calls an aberrational year; (a) speaks only of first and last years, (b) then sends a
sign-changing series to the halves and, when they are meaningless, to the no-growth case alone, while (d) asks for the range
at the pre-event intensity "beside". The run kept the literal reading central (no-growth alone) and put the event-removed
growth case beside; the text should say which governs when the aberrational year is in the middle. (2) **The regulated
utility's debt credit.** The paragraph does not say whether "the long-term debt raised over the window" is gross issuance or
net of retirements, nor whether the maintenance-only case (specific (e)) also takes the credit; the run used net debt raised
and gave the credit to growth spending only, on the reasoning that a flat rate base needs no new debt. Both readings change
the all-spending figure materially. (3) **"The debt share the regulator allows as the filing states it":** the 10-K does not
state it; the fallback (the business's own share at the latest date) gives 65 percent consolidated, whereas the regulated
subsidiary's own covenant ratio is 0.51; the paragraph does not say whose debt share (parent consolidated or the regulated
subsidiary). Here neither cap binds. (4) **Q5 and the regulated utility.** The make-the-numbers convention routes the habit to
Q5, where doubt closes, but a rate-regulated utility's earnings are steady partly by design (allowed returns, recovery
clauses, commission-approved deferrals), so the same record can be read as structure or as the habit the rows distrust. The
run found doubt because the company chose the streak as its leading boast and pays on it; a reader who weighs the structure
more could pass Q5 and close at Q7 instead. The box is OUT either way here, but the deciding question is a judgment the text
does not pin down; a stated test (for example, whether the company features the streak, and whether pay rests on the same
guided figure) would make it reproducible. (5) **Competitors for a franchise monopoly.** The brief's rule (take the rivals
the 10-K names) yields none for a regulated utility; comparators chosen by the analyst measure commissions, not rivals, and
were confessed as a CONVENTION of this run. (6) `tools/run.py` printed a window ending 2022 because the capital-spending
element changed after 2022; the 2023 to 2025 lines were read from the filed statements. (7) The template's section headings
carry em dashes, against the project's no-em-dash rule; left as the template's own text.
