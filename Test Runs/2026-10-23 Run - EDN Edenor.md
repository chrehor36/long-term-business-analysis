# Company Run — Empresa Distribuidora y Comercializadora Norte S.A., Edenor (NYSE: EDN) — 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-23, after the run was committed (13e7f9ca): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Dispatch.** Run by a dispatched analyst under the brief of 2026-10-23 (operator rule ten), which departs from
`Screens/_daily/_dispatch_brief.md` in one place it names: the lines of evidence are derived by the analyst from the 20-F's
Items 4, 3.D and 5 (below, "The lines of evidence"). Working folder `Test Runs/_research 2026-10-23 EDN/`.

**Contamination, declared.** (1) The session context showed the subjects of the five most recent repository commits, which
name another company's v5 run (a US utility, boxed at Q2); seen, not opened, not used. (2) The session's memory index lines
were shown (queue counts, a list of owed reviews); none names this company; not used. (3) Before the template was copied,
one directory listing of `Test Runs/` was filtered for "2026-10-23" or "EDN" to confirm the run file did not yet exist; it
returned no line. That is a listing of the blind-listed folder, declared here; nothing was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $18.57 per ADS (close 2026-10-22; Yahoo Finance through `tools/sources.py`, an aggregator, live quote only,
  flagged per operator rule 5). No dividend and no split in the aggregator's ten-year record; the 20-F states "Edenor has
  not declared or paid any dividends since August 14, 2001" (Item 8, 0001292814-26-002270).
- **Shares by class** from the 20-F cover (`python Screens/cover_shares.py EDN`: 20-F filed 2026-04-15, period 2025-12-31,
  accession 0001292814-26-002270): Class A 462,292,111; Class B 442,566,330; Class C 1,596,659; issued 906,455,100. The
  charter note: all three are "Common, book-entry shares, face value 1 and 1 vote per share" (Q2 2026 interim, Note 21,
  0001292814-26-004179); Class A is the 51% control block held by Edelcos and pledged to the Argentine Government under
  the concession; Class C is the employee programme. I treat the classes as equal per share for the arithmetic, since the
  filing gives them the same face value, vote and capital share; the control block's pledge and sale rule are weighed
  as risks, not as a different claim on cash. Treasury: 30,772,779 Class B (20-F Item 4 shareholder table; the same
  count "as of June 30, 2026" in the interim, Note 21). **Outstanding: 875,682,321 shares = 43,784,116 ADS equivalents**
  at 20 Class B per ADS. Checked against issued less treasury (above) and against the 6-Ks after the interim
  (2026-08-11 and 2026-10-09): none reports an issue, buyback or split. The 20-F Item 16E reads "Not applicable".
- **Market cap:** 43,784,116 x $18.57 = **$813.1M**.
- **Sovereign for the earnings currency (the Argentine peso): NOT OBTAINED.** The issuing authority is the Argentine
  Treasury (Ministerio de Economía, Secretaría de Finanzas); `tools/sources.py` covers USD, JPY and EUR only, and in
  this run I found no long-rate series published by the issuing authority itself and did not take a market quote in its
  place. The US 30-year par yield, 5.29% (US Treasury daily par yield curve, 2026-10-22), is recorded for reference and
  is **not** used as the peso rate. Why this does not change any figure reported: the computation below the stop finds
  owner cash negative on average on every basis, so its value is not positive at any positive discount rate, and the
  fair price is computed at ten percent by Part VII's definition, which needs no sovereign.
- **Currency and inflation, stated plainly.** Argentina is hyperinflationary for IAS 29 since July 1, 2018; every 20-F
  from FY2018 is in constant pesos of its own year end (20-F 2025, Presentation of Financial Information and Note 3). I
  carry every figure in **constant pesos of December 31, 2025** (real pesos), chaining earlier filings by the filer's own
  annual inflation rates (Note 3: 2021 50.9%, 2022 94.8%, 2023 211.4%, 2024 117.8%, 2025 31.5%; Dec-2022 to Dec-2025
  factor 8.919, Dec-2024 to Dec-2025 1.315). Peso to dollar: the interim restates December 2025 equity of Ps 2,222,906M as
  Ps 2,597,380M of June 30, 2026 (factor 1.1685), and states the June 30, 2026 Banco Nación selling rate it uses for
  dollar liabilities, Ps 1,482 per US$ (interim, foreign-currency note). A December 2025 peso figure is carried to June 2026
  pesos by 1.1685 and to dollars at 1,482, the measuring unit and the rate of the same date. The peso has moved since June
  30; this is said, not corrected for.
- **Filings read** (operator rule 4): 20-F FY2025 (filed 2026-04-15, 0001292814-26-002270), Items 3.D, 4, 5, 7, 8, 15,
  16E and the audited statements; 20-F FY2024 (2025-04-22, 0001292814-25-001581), the restatement note and Item 15;
  20-F FY2022 (2023-04-19, 0001292814-23-001639), FY2020 (2021-04-26, 0001292814-21-001740) and FY2018 (2019-04-30,
  0001292814-19-001619), the primary statements; the Q2 2026 interim statements on 6-K (2026-08-11, 0001292814-26-004179);
  the 6-Ks of 2026-08-11 (press release 0001292814-26-004183; BYMA results letter 0001292814-26-004180; board minutes
  0001292814-26-004184) and of 2026-10-09 (call of an ordinary meeting for 2026-11-12, 0001292814-26-004882). A foreign
  private issuer files no proxy; the meeting materials for 2026-11-12 were not found beyond the call. **Cross-checks against
  the filed statements:** revenue FY2025 Ps 2,990,891M (consolidated statement of comprehensive income); FY2024 operating
  cash flow Ps 245,917M in the FY2024 20-F x 1.315 = Ps 323,381M against Ps 323,500M as restated in the FY2025 20-F; the
  FY2020 loss Ps 17,698M (FY2020 20-F) x 1.509 x 1.948 = Ps 52,023M against Ps 52,017M as restated in the FY2022 20-F.
- `python tools/run.py EDN` printed one line, "EDN: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." It returned
  no arithmetic for this 20-F filer; every figure in this file is taken from the filed statements.

### The lines of evidence (this brief's departure, chosen from Items 4, 3.D and 5 of the FY2025 20-F)
Chosen because the 20-F's own risk factors and operating review put them first and because the framework's questions need
them: (1) the concession and the tariff regime over the cycle, 2002 to 2026 (Item 4, Tariffs; Item 3.D, "The Argentine
Government has intervened in the electricity sector"); (2) the debt to CAMMESA, the state-run wholesale market, and its
regularizations, because they carried the business through the freezes (Item 3.D; Note 2.c); (3) energy losses against the
10% loss factor the tariff recognizes, and collections and subsidies (Item 3.D); (4) the debt and its currency (Item 3.D;
Item 5, Debt; interim Note 25); (5) capital spending and its compulsion through quality standards and fines (Item 5,
Capital Expenditures; Item 3.D, fines); (6) dividends, buybacks and their prices, and stock pay (Item 8; statements of
changes in equity); (7) the controlling shareholder's fee and the new acquisitions (Item 7; interim Notes 19, 33);
(8) litigation, the restatement and the control weakness (Item 8; FY2024 20-F Item 15).

### Owner cash after every real cost (constant pesos of December 2025, billions; working in `notes.md`)
Operating cash flow as filed (it contains the working-capital changes and, on this filer, excludes interest paid on
borrowings, which sits in financing), less payments for property, plant and equipment, less lease principal, less interest
paid. Stock pay is negligible (the share-based plan reserve was Ps 79M in 2024 and Ps 120M in 2023, statements of changes in
equity) and is inside the expenses.

| year | operating cash | capex | lease principal | interest paid | owner cash before interest (all-equity) | after interest (equity-only) | PP&E depreciation |
|---|---|---|---|---|---|---|---|
| 2021 | 370.9 | 255.8 | 9.1 | 15.5 | 105.9 | 90.4 | 158.1 |
| 2022 | 315.9 | 282.9 | 10.4 | 8.0 | 22.6 | 14.6 | 162.2 |
| 2023 | 204.7 | 343.1 | 18.5 | 5.3 | -156.9 | -162.2 | 237.1 |
| 2024 | 323.5 | 473.5 | 16.0 | 40.4 | -166.0 | -206.4 | 203.3 |
| 2025 | 192.0 | 368.5 | 12.3 | 92.1 | -188.8 | -280.8 | 203.3 |
| **five-year average** | 281.4 | 344.8 | 13.3 | 32.3 | **-76.6** | **-108.9** | 192.8 |

Sources: 2021 from the FY2022 20-F (x 8.919); 2022 from the FY2024 20-F, as restated (x 1.315); 2023 to 2025 from the FY2025
20-F. The operating cash of 2021 to 2024 is swollen by energy bought from CAMMESA and not paid for (increase in trade
payables Ps 35,524M and 61,843M in 2021 and 2022, Dec-2022 pesos; Ps 316,180M and 414,336M in 2023 and 2024, Dec-2025
pesos), and 2025's by the conversion of that debt into a payment plan (trade payables down Ps 551,021M, other payables up
Ps 387,716M). The government's write-downs of the same debt were booked as gains of Ps 566,432M (2023) and Ps 218,114M
(2025) under "Agreement on the Regularization of Obligations", non-cash, outside operating cash.

### The balance sheets, nine year ends, before the income account **[M2025-032]**
Read in Step 0 because the file closes before Q4 (template, Q4). Ratios are free of the measuring unit; each year-end is
taken from the filing in which it is a primary column (Dec-2017 and Dec-2018 from the FY2018 20-F, Dec-2019 and Dec-2020
from the FY2020 20-F, Dec-2021 from the FY2022 20-F as first filed, Dec-2022 and Dec-2023 from the FY2024 20-F as restated,
Dec-2024 and Dec-2025 from the FY2025 20-F). Cash and securities are cash plus financial assets at fair value and at
amortized cost; trade payables are current and non-current; the ratio to revenue uses that year's revenue.

| year end | equity / assets | borrowings / equity | net debt / equity | trade payables / revenue | trade receivables / revenue | PP&E / assets |
|---|---|---|---|---|---|---|
| 2017 | 0.39 | 0.23 | +0.07 | 0.35 | 0.21 | 0.80 |
| 2018 | 0.40 | 0.27 | +0.16 | 0.27 | 0.14 | 0.81 |
| 2019 | 0.50 | 0.17 | +0.11 | 0.15 | 0.14 | 0.85 |
| 2020 | 0.42 | 0.13 | +0.02 | 0.37 | 0.15 | 0.84 |
| 2021 | 0.31 | 0.14 | -0.12 | 0.68 | 0.15 | 0.82 |
| 2022 | 0.32 | 0.10 | -0.10 | 0.88 | 0.14 | 0.82 |
| 2023 | 0.38 | 0.17 | +0.01 | 0.35 | 0.09 | 0.84 |
| 2024 | 0.38 | 0.31 | +0.05 | 0.37 | 0.19 | 0.75 |
| 2025 | 0.39 | 0.53 | +0.17 | 0.18 | 0.17 | 0.72 |
| Jun 2026 | 0.39 | 0.62 | +0.16 | | | |

What moved and why, "what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**: (1) the
assets are wires and substations (PP&E 72% to 85% of assets every year; no goodwill); (2) the financing of the freeze is
written in the payables: from 15% of revenue in 2019 to 68% in 2021 and 88% in 2022, the unpaid energy bill to CAMMESA,
cleared in 2023 and 2025 by government agreements that wrote part of it off and rescheduled the rest over 72 to 96 months
(Item 3.D; Ps 240,755M outstanding under the 2025 plan as of 2026-04-14); (3) from 2024 that supplier financing is
replaced by dollar bonds: borrowings rise from 0.17 of equity at Dec-2023 to 0.53 at Dec-2025 and 0.62 at June 2026 (the
interim states US$977M of borrowings, Class 10 notes of US$550M issued April 2026 and Class 11 of US$213.5M in July 2026,
interim Note 25); (4) receivables against revenue are steady, so collection has not visibly broken; (5) equity is flat to
up in real terms only through the government's write-offs and the monetary gain on liabilities (RECPAM), not through
operating profit; (6) what the figures cannot say: the deferred tax liability, the largest liability after borrowings, was
misstated for 2018 to 2024 and restated in the FY2024 20-F (below, AFTER THE STOP, Q4).

## THE FOUNDATIONS (not a gate)
Two foundations bear on this name. **A share is a business**: the test is whether I would be content to own it if the
market closed for years, "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**; for
this business the answer turns on what the Argentine Government will let the tariff earn, which is the subject of Q1.
**No macro forecast enters** **[M2000-094]**: the variable that decides here is not a forecast of the economy but the price
of the business's own product, set by a government body, which is a property of the business, as the speakers treat the
average profitability of a business over time **[M2015-016]**; I record the line between the two because it is close. The
ADS is also a claim on peso earnings carrying dollar debt, and "Any currency-related investment is a bet on how government
now, and in the future, will behave." **[M2011-025]**. **Contrary evidence, written down as found** **[M1997-127]**:
(a) in April 2025 the regulator approved a five-year tariff review for 2025 to 2030 with monthly indexation to consumer and
wholesale prices and "a rate of return on assets in real terms and after taxes of 6.50%" (ENRE Resolutions 237/2025 and
304/2025, 20-F Item 4); (b) the new regulator, ENReGE, had its board appointed on May 4, 2026, ending the intervention, and
applied monthly tariff updates of 4.75%, 2.95% and 1.78% for June, July and August 2026 (interim Note 2.a); (c) the
operating result turned positive in 2024 (Ps 55,346M) and 2025 (Ps 143,139M) and was Ps 190,654M in the first half of 2026
against Ps 45,649M a year earlier (interim); (d) the 2019 settlement with the Federal Government, which a later ministry
declared "harmful to the general interest", was kept in force when the Government's nullity action was dismissed for lack
of prosecution on December 13, 2024 (20-F Item 4); (e) the concession runs to August 31, 2087 with exclusivity, and the
filer reports capacity investment ahead of demand and improving quality indicators in 2025 (Item 3.D); (f) bond buyers bid
US$1,151M for US$550M of seven-year dollar notes at 9.5% in April 2026 (interim Note 25). Each is weighed at Q1.

## THE STANDING RULE
A part-interest bought outright, without borrowed money and at a size the buyer can lose entirely, does not put the buyer at
risk of ruin; the rule binds the buyer's financing and sizing, which this run cannot see: "never going to risk what we have
and need for what we don’t have and don’t need" **[M2012-081]**; "borrowed money has no place in the investor's tool kit"
**[L2014-005]**. Recorded as a condition on any purchase, not as a finding about the company.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.

**The engine is simple, and I understand it.** Edenor buys energy from the wholesale market run by CAMMESA, passes its cost
through to about 3.4 million users in an exclusive area, and keeps a distribution margin (the VAD, or CPD in the filings)
set by the regulator; the margin pays for the network, its losses up to the 10% the tariff recognizes, the staff, the fines
and the debt (20-F Items 3.D and 4). No technology risk of weight: the filer knows of "no current projects to introduce new
technologies" that would end the natural monopoly (Item 3.D). The competitive position is not in doubt: exclusivity to 2087.

**The key variables and how predictable they are** **[M1998-044]**. (1) The real distribution margin the Government allows;
(2) energy losses, 4,305 GWh in 2025, up 5%, above the 10% recognized, which the filer does "not expect" to fall "in the near
term" (Item 3.D); (3) collections and the subsidies paid by three governments for poor neighbourhoods (Item 3.D); (4) the
peso against dollar debt. Variable (1) decides the earning power, and the filings give its record over the cycle:
- **2002 to 2016:** the Public Emergency Law revoked the concession's dollar and inflation indexation; the margin was fixed
  in pesos from January 2002 to January 2007; of the cost adjustments requested from 2007 to 2016 "Only two adjustments were
  recognized in a timely manner" (Item 4, Tariffs). Operating result 2016: minus 23% of revenue before the Government's
  "provisional remedies" (FY2018 20-F).
- **February 2017:** the integral tariff review (RTI) set a regulated margin; operating margins of 6.0%, 7.0% and 5.3% in
  2017, 2018 and 2019 (FY2018 and FY2020 20-Fs).
- **2020 to 2023:** the company was instructed "to refrain from applying, as from January 1, 2020" the rate-maintenance
  agreement signed with the Government in September 2019, and new tariffs sufficient to cover cost were not approved, so
  it "partially postponed" its payments to CAMMESA (Item 3.D). Operating result negative in all four years: minus 21.8% of
  revenue in 2020 (impairment of Ps 17,396M inside, Dec-2020 pesos), minus 3.9% in 2021, minus 15.2% in 2022, minus 17.1%
  in 2023. In September 2021 the Ministry of Economy declared the 2019 settlement "harmful to the general interest" and the
  Government sued to nullify it (Item 4; the action was dismissed for lack of prosecution in December 2024).
- **2024 to 2026:** a CPD increase of 319.2% in February 2024; the five-year review of April 2025 with monthly indexation
  and a 6.50% real after-tax return on assets; operating margins of 2.1% (2024), 4.8% (2025) and 10.5% (first half 2026).
  The energy emergency declared in December 2023 was extended to July 9, 2026 and the regulator stayed under intervention
  until a new body was appointed in May 2026 (Item 4; interim Note 2.a). The company holds an unresolved "Regulatory Asset"
  claim for the breaches of the 2017 review, which "The SE is already reviewing" (Item 3.D).
So the sign of the operating result in each of the last ten years followed the tariff regime in force, and the business's
two largest cash events of the window, the write-offs of Ps 566,432M (2023) and Ps 218,114M (2025) of its unpaid energy
bill, were government decisions too.

**The tests, each with its filing fact.**
- *Do the past statements tell me the future ones?* "the financial statements will tell me the information that’s useful
  to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**. They do
  not here: the statements of 2016 to 2025 record three regimes chosen by successive governments, and a reader of any five
  of those years would have forecast the next five wrongly.
- *Is it important and knowable?* The tariff path from 2027 to 2036 is the most important variable and is a political
  decision not yet taken by governments not yet elected; "If something’s important but unknowable, forget it."
  **[M2006-076]**.
- *Would the insiders write it down?* "they would not want to put down on paper their predictions" **[M2000-105]**. The
  nearest insider, the filer, does not: "there is uncertainty as to what measures the Argentine Government may adopt in
  connection with tariffs" and "the Company has still not been able to resolve the income deficit or recover its credits
  against the Federal Government resulting from the freeze on electricity rates" (Item 3.D); its notes carry expropriation
  events of default (Item 3.D).
- *How far off could I be?* "some model in our mind of how far off we can be" **[M2011-084]**: across the filings read the
  same network has earned from minus 23% to plus 7% of revenue at the operating line in full years; the ten-year cash runs
  from the regulator's allowed real return to years of operating losses financed by not paying the supplier.
- *Abroad: do I understand the governance?* "where we think we understand the nuances of the corporate governance system
  and taxation" **[M2000-141]**. The governance that sets this business's price is the Argentine state's: an emergency
  regime, an intervened regulator, a settlement repudiated by a later ministry, and a pledge over the control block that
  the Government may foreclose (Item 3.D).
- *The speakers' own premise for owning a utility.* "the bet we are making is that regulatory authorities will treat us
  fairly in the future" **[M2014-087]**; "look to our utilities' regulators (acting on behalf of our customers) to allow us
  an appropriate return" **[L2009-011]**; "when you get an allowed return in the electric utility you’re almost certain of
  earning it, I mean, if you behave yourself" **[M2010-037]**. The filings show the margin set by the 2017 review not
  earned in 2020 to 2023 while the network was run. And where the regulatory climate turns, "it is difficult to project
  both earnings and asset values in what was once regarded as among the most stable industries in America" **[L2023-011]**.

**The contrary evidence, weighed** **[M1997-127]**. The 2025 review, the new regulator, the indexation now applied monthly
and the profits of 2024 to 2026 (Foundations, (a) to (c)) are real, and they are the same kind of evidence the 2017 review
gave in 2017 to 2019, which was reversed from January 2020. They show the present regime, not the ten-year one. A row about
an understood business abroad asks a lower price, not a pass, "We wanted to get paid more for going into China, and we did,
because we don’t know the game as well there." **[M2006-021]**; it applies to a business whose economics are understood,
and the earning power here is not. Set against "what’s likely to be the average profitability of the business over time"
**[M2015-016]**: the ten-year average in the filings is an operating loss, and that average is itself a record of policy.

**Routing.** The fixed routing of Q1 names the industry that changes fast; this one changes by decree, and the tests that fail
are Q1's own (tests 3, 4, 5, 8 and 11). The castle, the exclusive concession, is not what is in doubt; what is in doubt is
the earning power the castle is allowed, the first half of the definition **[M2012-065]**. I close here rather than at Q2
for that reason and record the choice under "What in the framework was wrong or unclear". "if you have doubts about
something being into your circle of competence, it isn’t" **[M2002-092]**.

**The cause: NATURE.** The deciding question is a forecast of a government's tariff decisions over ten years and at least two
national elections; no filing not yet read could answer it, and the filer itself does not write it down. "in other cases
the nature of the industry would be the roadblock" and "We couldn't solve this problem, moreover, even if we were to spend
years intensely studying those industries." **[L1993-023]**; "if we can’t make a decision in five minutes, we can’t make it
in five months" **[M2008-086]**. A lower price does not reopen it: "It just means that we don’t know how to evaluate it."
**[M2000-038]**.

**VERDICT: TOO HARD (NATURE)**, the third of "in, out, and too hard" **[M2006-013]**. The ten-year earning power of the
business is set by Argentine tariff policy, which the filings show changing course in 2002, 2017, 2020 and 2024, and which
neither the filer nor any document read forecasts. The file closes here.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1). Facts found are under AFTER THE STOP.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0, as the template asks when the file closes before Q4.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts found are recorded under AFTER THE STOP, not judged.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. (The buyback test against the bottom of the Q7 range is not run; the computation below has no positive range.)

## Q7: WHAT IS IT WORTH? STOP.
NOT REACHED as a clearance. The figures the owner asked for are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8, Q9, Q10, Q12
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE) at Q1**: the ten-year earning power of an exclusive distribution network is set by Argentine tariff
policy, which the filings show changing course in 2002, 2017, 2020 and 2024, and which the filer itself does not forecast.
Q2 to Q12 not reached. COMPUTATION, NOT A CLEARANCE: the value range is not positive on the central basis (five-year
average owner cash negative on every basis), so no fair price is positive, against $18.57 per ADS. **Integrity facts
recorded, not judged** (Part VII): the controlling shareholder's fee of 1.75% of gross billing, and the unpaid supplier
during the freeze (AFTER THE STOP, Q5). Cause NATURE: no research pass is opened; a lower price does not reopen the box
**[M2000-038]**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict on any of them; the box is unchanged (operator rule 2).

**Bearing on Q2 (the castle and the field).**
- The rivals the 20-F names are Edesur S.A. (the other federal concession in greater Buenos Aires, co-owner of SACME) and
  Edelap S.A. (Item 4). An EDGAR company search for "Edesur", "Edelap" and "Distribuidora Sur" on 2026-10-23 returned no
  registrant: neither files with the SEC. The 20-F names no SEC-filing rival. No competitor row was built, since Q2 was
  not reached, and no rival was chosen by convention.
- The field's returns over the cycle, from the filer's own statements: operating result as a share of revenue minus 23.3%
  (2016, before government remedies), 6.0%, 7.0%, 5.3% (2017 to 2019), minus 21.8%, minus 3.9%, minus 15.2%, minus 17.1%
  (2020 to 2023), 2.1%, 4.8% (2024, 2025). The allowed return for 2025 to 2030 is 6.50% real after tax on assets (ENRE
  Resolution 237/2025, Item 4).
- Exclusivity may be revoked if technology makes distribution competitive, without indemnity (Item 3.D); Decree 450/2025
  opens wholesale contracting between private parties over a two-year transition (Item 4).

**Bearing on Q3 (capital).**
- Capital spending 2021 to 2025 averaged Ps 344.8bn a year against PP&E depreciation of Ps 192.8bn (Dec-2025 pesos), 1.8
  times. The concession sets no mandatory capital spending but "specific quality standards that become progressively more
  stringent over time" enforced by fines (Item 5, Edenor's Capital Expenditures); accrued fines and penalties Ps 67,666M at
  December 31, 2025, 2.26% of net energy sales (Item 3.D). Of 2025's Ps 394,892M of investments, "the majority" went to
  capacity, remote control, new connections and self-administered meters (Item 5); no maintenance split is given.

**Bearing on Q4 (the accounts).**
- The FY2024 20-F restated 2022 and 2023 for an error in the deferred tax on PP&E (the tax base was taken at historical
  values, overstating the liability for 2018 to 2024; equity at December 31, 2022 rose by Ps 190,979M of Dec-2024 pesos),
  and management concluded that internal control over financial reporting was not effective at December 31, 2024
  (0001292814-25-001581, Item 15). The FY2025 20-F describes the remediation and an audited ICFR opinion for 2025
  (0001292814-26-002270, Item 15). The cover of the FY2024 20-F ticks the boxes for an error correction and a recovery
  analysis; the Executive Committee "determined that it is not necessary to implement said clawback procedure".
- Net income is not the business's earnings: 2025 income before tax of Ps 291,332M is an operating result of Ps 143,139M
  plus a government write-off of Ps 218,114M plus a monetary gain (RECPAM) of Ps 307,317M less net financial costs of Ps
  377,238M; 2023's Ps 521,881M rests on a write-off of Ps 566,432M and RECPAM of Ps 1,302,235M against an operating loss.
- The press release on the first half of 2026 is headed "EDENOR REPORTS EBITDA OF ARS 313,747 MILLION" and gives the change
  in EBITDA "Excluding this extraordinary effect" (6-K 2026-08-11, 0001292814-26-004183).

**Bearing on Q5 (the people). Integrity facts, recorded, not judged.**
- The controlling shareholder, Edelcos (owned by South American Energy LLP, UK; it bought the 51% Class A block from Pampa
  Energía with ENRE approval on June 24, 2021), is paid under a technical assistance agreement "either an annual amount of
  Ps.1,766 million or the amount equivalent to 1.75% of the annual gross billing, whichever results in the higher amount,
  plus the associated value added tax"; the charge for 2025 was Ps 63,425M in Dec-2025 pesos (Item 7), against an operating
  result of Ps 143,139M, while no dividend has been paid to any shareholder since 2001. The agreement expires December 2026
  and may be extended; either party may end it on 60 days' notice (Item 7). The ultimate owners of the LLP are not named in
  the passages read.
- During the freeze the company "partially postponed" payment for the energy it bought from CAMMESA (Item 3.D); trade
  payables reached 88% of revenue at December 2022; the debt was later reduced by government agreements and rescheduled.
- A Class A director, Eduardo Marcelo Vila, is described as having been for 20 years the director of legal affairs of Grupo
  América, a multimedia group (Item 6). Recorded as a biographical fact only.

**Bearing on Q6 (the money and the owners).**
- No dividend declared or paid since August 14, 2001 (Item 8); the 2025 profit was allocated wholly to the statutory and
  discretionary reserves (meeting of April 29, 2026, interim Note 32).
- Buybacks under two programmes with stated caps (up to US$55 per ADR, then up to US$30 per ADR), "with the purpose of
  contribute to the reduction of the gap between the Company's fair value based on its assets value and the quoted price"
  (FY2018 20-F, Item 16E): average prices paid per ADS US$45.43 (May 2018), 41.88 (June), 25.94 (December), 27.28 (January
  2019), 27.81 (February), 21.26 (March), 17.44 (April); the ADS closed near US$5 to US$7 from September 2019 (aggregator,
  flagged). None since (FY2025 20-F, Item 16E "Not applicable"); 30,772,779 shares held in treasury.
- New uses of the money: minority stakes of 15% and 40% (political rights 11.8% in the latter) in two companies exploring
  for lithium and copper at an "early-stage or pre-exploration phase" in Catamarca, Ps 33,145M paid in 2025, fair value Ps
  54,689M at June 30, 2026 on a Level 3 per-hectare method (interim Note 19); a binding offer of April 14, 2026 for 50% of
  Citelec S.A., which controls 52.65% of Transener, minimum price US$206.2M (20-F, note on the Citelec tender); an
  irrevocable offer of July 23, 2026, jointly with Andina Energies PLC, for 70% of Metrogas S.A. (interim Note 33); and the
  stated evaluation of further acquisitions in transmission, hydrocarbons and gas (20-F, same note). The ordinary meeting
  of July 27, 2026 raised the corporate notes programme to up to US$1,700M (interim Note 32). Neither offer was reported
  accepted at the interim date.

**Bearing on Q9 (could it ruin us).**
- Borrowings of Ps 1,698,203M at June 30, 2026, of which US$977M in dollars (interim, foreign-currency note); after the
  date, Class 11 notes of US$213.5M issued July 3, 2026 and Class 9 peso notes repaid (interim Notes 25, 34). Revenues
  "are collected in Pesos pursuant to tariffs that are not indexed to the U.S. Dollar" and the currency risk cannot be
  hedged in full (Item 3.D). All debt carries bankruptcy, reorganization and expropriation events of default with cross
  default (Item 3.D). Incurrence covenant: debt ratio not above 3.75 (interim Note 25). CAMMESA payment plans: Ps 240,755M
  outstanding under the 2025 plan as of April 14, 2026 (Item 3.D).
- The Government may foreclose its pledge on the Class A shares if fines in a year exceed 20% of energy sales, among other
  events (Item 3.D). Physical assets insured up to US$2,833M; no cover for losses caused by the network or for business
  interruption (Item 3.D).

**Bearing on Q12.** No fact found that bears on a named business.

### Q7: COMPUTATION, NOT A CLEARANCE
Built by Q7's range convention as the owner asked; not a verdict and carrying no entry language (operator rule 3).
- **Basis.** A regulated utility: equity-only central, with the long-term debt raised over the window credited against the
  capital spending it funded, up to the regulator's allowed debt share (Q7, The regulated utility). No allowed debt share
  was found in the 20-F (a search for "WACC", "rate of return", "capital base" and "regulatory asset base" found only the
  6.50% return on assets); the business's own debt share of capital at the latest filed date is used, 38.1% (borrowings
  Ps 1,698,203M against borrowings plus equity Ps 4,452,715M, June 30, 2026). The credit is net new borrowing each year,
  capped at 38.1% of that year's capital spending: 0, 0, 47.0, 180.4 and 140.4 (Ps bn, 2021 to 2025). The use of the
  proceeds was not traced beyond the filer's general statement that investment was given priority (Item 5).
- **Owner cash, central, equity-only with the credit:** 90.4, 14.6, minus 115.3, minus 26.0, minus 140.4; five-year average
  **minus Ps 35.3bn** a year (Dec-2025 pesos). Equity-only without the credit: average minus Ps 108.9bn. All-equity (before
  interest): average minus Ps 76.6bn.
- **The specifics.** Growth (aggregate, specific (b)): the series changes sign, the halves are meaningless, so the range is
  the no-growth case alone, said so. Cycle (a): the window spans a freeze (2021 to 2023, which the filer describes as a
  deterioration of its "economic and financial equation") and a new regime (2024, 2025); no earlier full cycle under one
  regime exists in the filings read, so no cycle base is substituted and the literal window is the figure shown.
  Acquisitions (c): the Ps 33,145M paid in 2025 for the mining stakes is left out of the table above; counting it lowers
  the average by a further Ps 6.6bn a year; the Citelec and Metrogas offers are neither signed nor closed and no target
  record was read, so they are left out. Working capital (d): counted, inside operating cash. Maintenance (e): the filing
  gives no maintenance split, so the all-spending case is central. Cap (f): not reached, there is no positive growth to cap.
- **Value range: not positive** on the central basis, a single no-growth case with negative cash; not positive at any
  positive discount rate, which is why the missing peso sovereign changes nothing here. "if we don’t have the faintest
  idea what the future stream is going to look like, we don’t have the faintest idea what it’s worth, now" **[M1994-077]**.
- **Fair price (Part VII, each end at ten percent, averaged): not positive** on the central basis; not positive on the
  equity-only basis without the credit; not positive on the all-equity basis (negative cash, less net debt of Ps 427,957M of
  June 2026: borrowings Ps 1,698,203M less cash Ps 548,118M, current financial assets at fair value Ps 667,695M and at
  amortized cost Ps 54,433M; the Level 3 mining stakes are not counted as cash; operating leases left out).
- **The depreciation variant, shown beside as the four specifics require (not the fair price):** owner cash with PP&E
  depreciation in place of capital spending, after lease principal and interest, averages plus Ps 43.1bn a year (188.2,
  135.3, minus 56.2, 63.8, minus 115.7). At ten percent and no growth that is Ps 431bn, Ps 492 a share in Dec-2025 pesos,
  Ps 575 in June-2026 pesos (x 1.1685), Ps 11,503 per ADS (x 20), **US$7.76 per ADS** at Ps 1,482 per US$. It assumes that
  spending at depreciation would keep the network in place, which the quality standards and fines above put in doubt.
- **The owner's two figures:** (a) VALUE RANGE: not positive, against $18.57 per ADS; (b) FAIR PRICE: not positive on the
  central (equity-only, regulated-utility) basis and on the all-equity basis beside it. Conversion: Dec-2025 pesos to
  June-2026 pesos by the interim's own restatement factor 1.1685, then to dollars at the Ps 1,482 Banco Nación selling rate
  the interim states for June 30, 2026, 20 Class B shares per ADS.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 227306fa); written question by question; committed after each
      section (write-early).
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is held by the dispatching session, which
      folds the run (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, with the one listing declared
      under Contamination (a filtered listing of `Test Runs/` before the copy, which returned nothing); the commit subjects
      and memory lines seen are declared there and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is that row's own (check
      script `Test Runs/_research 2026-10-23 EDN/check_ids.py`); no E-id; every filing fact has its accession or filing;
      no number without a filing or a stated computation.
- [x] The order was kept; Q1, a STOP, failed and closed the run; nothing after it is a clearance; the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, from the filed cash flow statements, never a net-income proxy (operator rule 5).
      **The sovereign was not obtained from the issuing authority** (Step 0): a failure of operator rule 5's sovereign
      requirement, confessed; no figure reported depends on it, since no case is positive.
- [x] Aggregator quotes flagged (the price; the 2019 ADS range).
- [x] Contrary evidence written down as found (Foundations (a) to (f)) and weighed at Q1; the facts for later questions are
      under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` returned no arithmetic; nothing it printed was used.
- [x] `python tools/check_framework.py` PASS (2026-10-23, before the closing commit). The check script reports 33 id
      citations, 27 distinct, 0 problems; a wider pass over every quotation between consecutive ids flagged only 20-F
      quotations, search words and a section title, none of them set beside an id as its words.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Where a regulated price set by a government with a record of reversals closes.** Q1's fixed routing sends to TOO HARD
the business whose ten-year economics cannot be foreseen because its industry changes fast; Q2 owns rapid change, carries
the utilities letter of 2023 among its narrated mistakes as a regulated moat that broke, and excepts a regulator's return
from its OUT for ordinary returns. A distribution monopoly whose margin is set by decree fits neither routing sentence: the
castle stands, the earning power does not. I closed at Q1 because the tests that fail are Q1's (3, 4, 5, 8, 11) and the
definition of understanding names earning power first; another analyst could close the same name at Q2, test 11, with the
same box. A sentence saying which question owns a regulator's reversals would settle it. (2) **The peso sovereign.**
Operator rule 5 and Q7 need the long government rate of the earnings currency from its issuing authority; the protocol's
table and `tools/sources.py` cover USD, JPY and EUR only, and for a currency whose Treasury publishes no long par curve
(or none I found) the framework gives no instruction. Here it did not matter, because no case was positive; for an
Argentine name with positive owner cash it would decide the range. (3) **Constant-currency statements.** Q7's fourth
specific computes "no real growth" as zero nominal growth "the discount rate being nominal"; under IAS 29 the cash is
already real, so a nominal rate applied to real cash is the wrong pair. The framework does not say which rate to pair with
restated cash. (4) **The regulated-utility credit.** "the debt raised for the fixed assets" is not separable on this filer,
whose dollar notes refinance, fund working capital that once sat with the supplier, and now fund acquisition bids; I capped
net new borrowing at the debt share, and the rule does not say whether refinancing or a supplier's debt converted to a
payment plan counts. (5) **Government write-offs of a supplier's debt.** Owner cash as defined counts the cash kept by not
paying CAMMESA as operating cash, and the later write-off never appears in cash; the framework's real-cost list has no line
for a recurring government transfer booked as a "one-time" gain, which is the shape of this business's whole record.
