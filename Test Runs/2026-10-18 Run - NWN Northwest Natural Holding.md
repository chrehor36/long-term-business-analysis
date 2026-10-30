# Company Run — Northwest Natural Holding Company (NYSE: NWN) — 2026-10-18
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under the canonical brief `Screens/_daily/_dispatch_brief.md`, with the one stated departure: the lines of evidence were
derived by the analyst from the 10-K's Item 1, Item 1A and Item 7 (listed under STEP 0), not hand-written by the dispatcher.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (721bb27e): `PORTFOLIO.md` read for this one ticker; the operator does not hold NWN (no line names NWN, Northwest Natural or NW Natural).*

**CONTAMINATION, declared before any verdict.** (1) A directory listing of `Test Runs/` filtered on today's date, made to
check that this run's file did not yet exist, showed four other run file names of 2026-10-18 (HOKCY, MDU, NJR, XNGSY) and
their research folders. None was opened. (2) The session context supplied by the harness carried the recent commit
subjects of the repository, among them the fold of the NJR run of today (a gas utility in another state: its box, its
Q7 figures, and the phrases "Q2 IN on the gas franchise at a regulator-set 9.6% on equity" and "the State's proceeding on
the future of gas utilities the closest call"). (3) The memory index lines in the session context (queue state, counts of
gate-clearers). None of this is used: no figure, box or reading below comes from it, and where this run reaches a different
box from the NJR subject line the reasons are this file's own, from NWN's filings. It is declared because it is a
reading of the same kind of business on the same day, and the analyst cannot un-see it **[M1997-127]**.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $48.99 (close 2026-10-16; `tools/run.py` live quote; **aggregator, flagged**, operator rule 5).
- **Shares by class:** one class, common stock, no par. Cover of the 10-Q for the quarter to 2026-06-30 (filed 2026-08-05,
  accession `0001733998-26-000127`): **42,093,538** shares as of 2026-07-28 (`python Screens/cover_shares.py NWN`). Check
  against the same 10-Q's balance sheet: issued and outstanding 42,093,292 at 2026-06-30; no treasury shares (no par,
  "issued and outstanding" one figure). No 8-K or prospectus after the 10-Q reports an equity issue (the three 8-Ks since,
  of 2026-07-31, 2026-09-03 and 2026-09-23, are a rate order, first mortgage bonds and a rate settlement).
- **Market cap:** 42.094M x $48.99 = **$2,062M**.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`tools/run.py`, issuing authority).
- **Net debt, latest filed balance sheet (2026-06-30, 10-Q `0001733998-26-000127`):** short-term debt $121.3M + current
  maturities $125.7M + long-term debt $2,376.7M - cash $24.2M = **$2,599.4M**. Operating leases ($78.2M of liabilities)
  left out, as Q7 directs. Debt issued after the balance-sheet date (NW Holdings Series F and G notes, $70M, 8-K of
  2026-06-05, `0001733998-26-000114`; NW Natural first mortgage bonds $120M, 8-K of 2026-09-03, `0001733998-26-000137`)
  is stated for repayment of existing debt and general purposes; it is not added, since its cash is not on the balance
  sheet either and no filing states its net effect. EV at the price: **$4,662M**.
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-27, `0001733998-26-000012` (Items 1, 1A, 7, 8 read); 10-K
  FY2024 `0001733998-25-000020` and FY2023 `0001733998-24-000011` (segment tables, meters, 2021-2022 cash-flow lines);
  10-K FY2021 `0001733998-22-000005` (meter growth 2020-2021); 10-Q Q2 2026 `0001733998-26-000127` (balance sheet,
  environmental note, regulatory and policy updates, meters); proxy DEF 14A filed 2026-04-17 `0001193125-26-161075`
  (pay design, adjusted EPS, CEO pay); 8-Ks of 2026-06-05, 2026-07-31 `0001733998-26-000123` (Washington rate order),
  2026-09-03, 2026-09-23 `0001733998-26-000145` (Texas rate settlement).
- **One figure cross-checked against the filed statement:** cash provided by operating activities FY2025, **$269,124
  thousand** on the filed consolidated statement of cash flows (10-K FY2025, page 86), against `tools/run.py`'s 269.1. Agrees.
  Capital expenditures FY2025 $466,893 thousand on the same statement against run.py's 466.9: agrees.
- **`python tools/run.py NWN`, arithmetic lines only** (output kept at `Test Runs/_research 2026-10-18 NWN/runpy_out.txt`):
  OCF 279.9 / 200.3 / 269.1 (FY2023-25); capex 327.3 / 394.4 / 466.9; D&A 125.6 / 137.9 / 165.5; owner cash after all
  capital spending -47.4 / -194.1 / -197.8; five-year window mean on the capex basis -152.8, on the depreciation basis 79.6.
  Stock pay "n/f" in XBRL: **resolved from the filed statements of shareholders' equity**: $3.6M (2021), $3.2M (2022),
  $3.6M (2023), $3.2M (2024), $4.1M (2025), deducted below. Finance-lease principal $0.3-0.5M a year, immaterial, noted.
  Nothing run.py prints as a rule, an id or a verdict is used (Part VII).

**The lines of evidence this name needs, chosen by the analyst from the 10-K FY2025** (the brief's stated departure):
1. *From Item 1 (Business, segments):* which part decides (three reportable segments since Q1 2025: NWN Gas Utility,
   SiEnergy, NWN Water; "Other"); the gas utility's exclusive service territory "allocated" by the OPUC and WUTC and its
   statement that it "has no direct competition from other natural gas distributors" but "competes with other forms of
   energy"; customer growth's dependence on "regulations and building codes permitting the use of natural gas in new
   construction"; gas in about 64% of single-family homes in the territory.
2. *From Item 1A (Risks):* CUSTOMER GROWTH RISK (building codes; the OPUC's order of 2024-10-25 phasing out the line
   extension allowance by 2027-11-01); PUBLIC PERCEPTION AND POLICY RISK (Washington CCA, Oregon CPP's 50% cut by 2035 and
   90% by 2050, gas bans considered locally, two climate suits naming the company); REGULATORY RISK (HB 3179's limit on
   rate filings; disallowance); REGULATORY ACCOUNTING RISK; ENVIRONMENTAL LIABILITY RISK; INABILITY TO ACCESS CAPITAL.
3. *From Item 7 (MD&A):* volumes, meters and margin of the gas utility over the years; the authorized returns (Oregon 2025
   order, Washington order of 2026-07-29); capital spending against depreciation and the five-year capex plan; the
   financing of that spending (debt, ATM equity, dividends); the climate-policy section and the company's own words on what
   it cannot predict.

---
## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what a gas distributor in western Oregon and southwest Washington
will pay its owners over ten to twenty years, not what the next buyer pays. The market "is there to serve you and not to
instruct you" **[M2006-077]**; the stock's fall or rise is not evidence here. No macro forecast enters **[M2000-094]**: the
gas price and the federal administration's energy policy are not forecast; the *state* climate laws below are not macro
forecasts but enacted rules that bind this business's product, and are read as facts about the business. Who is paid to
tell you **[M2020-037]**: the 10-K's own advocacy ("natural gas has an important role in moving the Pacific Northwest to a
lower carbon future") is the seller's view of what it sells and is read as such. The analyst's habits: write contrary
evidence down at once **[M1997-127]**, look for "what’s wrong" and "what you’re missing" **[M2025-013]**. **Contrary
evidence, written down as found** **[M1997-127]**: (1) owner cash after all capital spending has been negative in four of
the last five years; (2) gas-utility meter growth has fallen from 1.5% (2020, 2021) to 0.3% (twelve months to 2026-06-30),
with commercial and industrial meters now falling; (3) the Oregon regulator itself ordered the line extension allowance
phased out and wrote $13.7M of undepreciated line extension costs out of rate base (2024); (4) the Gasco uplands
environmental estimate was raised in April 2026 to a recorded $284M at the low end of a $284M to $950M range; (5) the
shares outstanding rose from 28.8M (2018 diluted average) to 42.1M while the dividend rose about one cent a year.

## THE STANDING RULE
A part-interest bought for cash, unlevered, cannot put the buyer at risk of ruin; "We are never going to risk what we have
and need for what we don’t have and don’t need" **[M2012-081]**, and borrowed money "can destroy the decent returns that a
life-long owner of equities would otherwise enjoy" **[L2014-005]**. The rule is met if the purchase is made without
borrowing and sized so that a total loss is survivable; nothing in this run asks otherwise.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand the economic dynamics of the
  industry" **[M2011-014]**. The key variables, and how predictable each is **[M1998-044]**:
  1. *Rate base* (what the regulator lets the company earn on): Oregon average rate base $2.27B in the 2025 order, up
     $180.1M since the prior case; Washington $328.0M rising to $397.8M over the three-year plan of 2026-07-29; SiEnergy's
     combined rate base about $343M in the settlement of 2026-09-22. It grows with capital spending (plan: $2.6B to $2.9B
     over 2026-2030 for NW Holdings, 10-K FY2025 Item 7). Readable and, five years out, foreseeable from the filed plans.
  2. *Allowed return:* 9.5% on equity at 50% equity in Oregon (order of 2025-10-24) and Washington (order of 2026-07-29);
     9.8% at 59.75% equity in the Texas settlement. Readable.
  3. *Earned against allowed:* consolidated return on average equity 5.9% to 8.8% over 2018-2025 (XBRL, computed in
     `peers_roe.txt`), below the allowed 9.4-9.5%: regulatory lag and holding-company debt. Readable.
  4. *Share count:* equity is issued to fund the plan (ATM program, $400M authorized). Readable.
  5. *The volume and customer base the rate base is spread over, and the regulators' treatment of that rate base as the
     two States pursue their climate laws.* This is the variable on which the ten-to-twenty-year economics turn; whether it
     can be foreseen is Q2's castle question (what could "destroy, or modify, or reduce" the strengths **[M2000-014]**),
     not a matter of understanding how the business makes money.
- **Routing.** The business is not one whose industry changes fast in the sense of the Q1 routing (where "the future
  technology could hurt the business as it presently exists" **[M1998-008]**): distribution of gas through pipes under rate
  regulation has changed slowly; the pressure is political and slow, which the framework places under Q2, where "slow change
  can be much harder to perceive, and can lull you to sleep easier" **[M2014-038]**.
  The holding company is read by its parts (Q1's holding-company paragraph; CONVENTION, **[M2023-031]** OPEN against it):
  the deciding part is the NWN Gas Utility (see the parts table at Q2), and it is understood by the tests above; SiEnergy
  (Texas gas distribution) and NWN Water (regulated water) are smaller regulated utilities read the same way.
- **Doubt test.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.
  The doubt this analyst holds is not about how the business earns (rate base times allowed return, decoupled in Oregon,
  passing gas cost through) but about how long the castle stands, which is the next question.
- **VERDICT: IN.** The economics are those of a rate-regulated distributor, readable from the rate orders and the
  statements; the first question, "can I understand it?" **[M1995-051]**, is answered yes for how it earns. Whether its
  standing can be foreseen ten to twenty years out is put at Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now" **[M1995-038]**.

**The parts table** (business of parts, CONVENTION of the framework; income from operations from the filed segment tables,
10-K FY2023 `0001733998-24-000011` for 2021-2022 and 10-K FY2025 `0001733998-26-000012` for 2023-2025; $M):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| NWN Gas Utility (NGD until 2024) | 147.9 | 152.8 | 170.6 | 173.2 | 219.9 | 864.5 | 87.5% | exclusive territory, rate-regulated | **yes** |
| SiEnergy (Texas gas, acquired 2025-01-07) | - | - | - | - | 26.6 | 26.6 | 2.7% | no defined territories in Texas; competes with other gas utilities for developments | no |
| NWN Water, NW Natural other, NW Holdings other (residual) | 15.2 | 14.6 | 14.4 | 17.9 | 34.4 | 96.5 | 9.8% | regulated water; Mist interstate storage; RNG | no |
| consolidated income from operations | 163.1 | 167.5 | 184.9 | 191.1 | 280.9 | 987.6 | 100% | | |

The file closes on the NWN Gas Utility. "lumping them together [...] impedes analysis" **[L2008-005]**.

**The castle tests, on the NWN Gas Utility, each with its filing fact.**
1. *What keeps it standing.* The territory: "NW Natural has been allocated an exclusive service territory by the Oregon Public
   Utility Commission (OPUC) and Washington Utilities and Transportation Commission (WUTC)", and it "has no direct competition
   from other natural gas distributors. However, it competes with other forms of energy in each customer class" (10-K FY2025
   Item 1). The castle is a grant of the two States, earned at a return the States set. Its permanence therefore depends on
   the grantor, and the grantor is legislating against the product (test 8).
2. *The attacker with money* **[M2011-015]**: no one will build a second gas network in Portland; on this test the castle
   stands. The attack comes from another direction: electricity, aided by building codes and climate law, competing for
   the heating load on "price, efficiency, reliability, performance, preference, perceptions, market conditions, building
   codes, technology, federal, state, and local energy policy, and environmental impacts" (10-K Item 1).
3. *Pricing power and the agony before a rise* **[M2005-020]**: the price is set in rate cases, the prayer session in
   statute. Oregon's HB 3179 (2025) "authorizes the OPUC to consider broader economic indicators when evaluating rate
   proposals and limits the frequency and timing of rate increases", allows increases only from April 1 to October 31, and
   bars a new general rate case within 18 months of the last until 2027-01-02 or multi-year rules (10-Q Q2 2026). Against
   it, the regulators have just granted: Oregon 9.5% on equity at 50% equity (order of 2025-10-24, +$20.7M), Washington 9.5%
   at 50% equity over three years (order of 2026-07-29, +$20.1M, +$7.5M, +$7.4M, the line extension allowance preserved in
   Washington; 8-K `0001733998-26-000123`).
4. *Unit volume, and whether the moat widens or shrinks* **[M1999-108]**. Volumes delivered: 1,206.7M therms (2023),
   1,170.8M (2024), 1,111.4M (2025); the company attributes the falls partly to weather (8%, 17%, 20% warmer than average) and
   partly to "lower usage from residential and commercial sales customers, pulp and paper industrial sales and transportation
   customers". **Meter growth, total:** 1.5% (2020), 1.5% (2021), 1.1% (2022), 0.6% (2023), 0.8% (2024), 0.5% (2025), 0.3%
   (twelve months to 2026-06-30). Commercial meters -0.2% (2025) and -0.8% (to June 2026); industrial -0.4% and -1.2% (10-K
   FY2021 `0001733998-22-000005`, FY2023, FY2024 `0001733998-25-000020`, FY2025, 10-Q Q2 2026). Gas is in about 64% of
   single-family homes in the territory (10-K Item 1).
5. *Would the customer still choose it over the alternative* **[M2017-009]**: for a new home the choice is made once, at
   construction, and "Single-family new construction has consistently been our largest source of growth" (10-K Item 1). The
   Oregon regulator ordered the line extension allowance phased out by 2027-11-01 and wrote undepreciated line extension
   costs out of rate base ($13.7M charge in 2024); the company is appealing. Washington's building codes (WSEC-2021)
   "generally have the effect of restricting or eliminating the use of gas space and water heating in new commercial and
   residential construction"; Initiative I-2066, which would forbid that, was declared invalid by the King County Superior
   Court and is on appeal to the Washington Supreme Court (10-K Item 7; 10-Q Q2 2026).
6. *Cost against the substitute.* Compliance costs go into the gas bill: "CCA compliance costs represent a 4.6% increase on
   residential bills starting on January 1, 2025"; Oregon's CPP costs are deferred and sought in rates. The company's own
   reading: "We are not able to determine at this time whether these developments will make natural gas use more or less
   competitive on a relative basis" (10-K Item 7).
7. *Widening or narrowing* **[L2005-010]**: narrowing on every growth measure in the filings (test 4) and on two regulatory
   acts against the growth mechanism (the Oregon line extension order, the Washington codes). Not narrowing on the return:
   the authorized return was renewed in both States within the last twelve months.
8. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. Oregon's CPP limits greenhouse-gas
   emissions from covered entities, natural gas utilities among them, "by 50% by 2035 and 90% by 2050 from a 2017-2019
   baseline" (in force 2025-01-01, the second set of rules after the first was invalidated in 2023, now challenged again in
   the Oregon Court of Appeals by a coalition that includes NW Natural); Washington's CCA declines to "95% below 1990 levels by
   2050". Both laws act on the volume of the product the castle carries, and the regulators who set the return are agencies
   of the same States. The rows' test of whether the business would exist if its substitutes had come first **[L2006-008]**
   is answered for new buildings in Washington's codes. The 10-K adds local actions considered in the territory (gas bans in
   new construction, a gas supplier tax, carbon impact fees) and two climate suits naming the company.

**The competitor row.** The 10-K names no rival company; it names classes ("providers of electricity, fuel oil, and
propane"; for storage, "other storage facilities and pipelines"; for SiEnergy, "other local distribution companies").
**CONVENTION of this run:** the comparison set is Avista Corporation (gas and electric distribution in the same two States;
CIK 0000104918; FY2025 10-K `0001193125-26-067872`) and Portland General Electric (the electric utility serving much of the
same territory, named in NWN's 10-K as the sole North Mist storage customer; CIK 0000784977; FY2025 10-K `0001193125-26-052750`,
its net income taken from the XBRL comprehensive-income tag including non-controlling interest, the only annual income tag it
files, so other comprehensive income is inside it); rationale: the 10-K names no rival, and these are the nearest regulated
distributor of the same product and the regulated seller of the substitute. Not compared: propane and fuel-oil sellers
(unnamed). Metric: net income on average equity, from each company's own XBRL filings, computed in
`Test Runs/_research 2026-10-18 NWN/peers_roe.txt` (transcription):

| year | NWN | Avista | Portland General |
|---|---|---|---|
| 2018 | 8.6% | 7.8% | 8.7% |
| 2019 | 7.6% | 10.6% | 8.4% |
| 2020 | 8.8% | 6.5% | 5.9% |
| 2021 | 8.6% | 7.0% | 9.2% |
| 2022 | 8.2% | 6.9% | 8.7% |
| 2023 | 7.6% | 7.1% | 7.4% |
| 2024 | 5.9% | 7.1% | 8.8% |
| 2025 | 7.9% | 7.3% | 7.7% |

**The field's returns over the whole span, judged in words.** The regulated players of this field, gas and electric, earn
between six and nine percent on book equity year after year, below the allowed nine and a half and a little above the long
bond. That is an ordinary return; it is a return set by a regulator, which the framework carries to Q3 as a second best
rather than closing OUT here **[M2009-104]**, **[L2009-012]**. The ordinary-return ground does not decide Q2.

**What decides Q2.** The castle stands today: the territory is exclusive, both regulators renewed the allowed return within
the year, and earnings rose in 2025 on the new Oregon rates. What will keep it standing ten to twenty years out is the one
question the filings cannot answer: whether two States whose laws require the gas this company delivers to fall by half by
2035 (Oregon) and nearly to nothing by 2050 (Washington) will keep allowing a fair return on, and the recovery of, a rate base
the company plans to grow by about $1.6B to $1.8B at NW Natural alone over 2026-2030 while its customer growth falls toward
zero. The company says it cannot say: of the codes and I-2066, "We cannot currently predict the ultimate outcome of such
appeal"; of compliance, "The evolving guidance to implement the CCA and CPP, evolving carbon credit markets, decades-long
compliance timeframes, likely changes in law and policy, and technological advancements, all make it difficult to accurately
predict long-term tools for and costs of compliance" (10-K FY2025 Item 7; the same in the 10-Q). The rules themselves have
been made, struck down and made again within three years, and the decisive one is under appeal now. The speakers' own utility
mistake is this question: "In such jurisdictions, it is difficult to project both earnings and asset values in what was once
regarded as among the most stable industries in America. [...] I did not anticipate or even consider the adverse
developments in regulatory returns" **[L2023-011]** (a row about Berkshire's own utilities, weighed as evidence of the test,
never as a verdict on this industry, by the framework's convention on rows about one company).

Is the castle *shown on the evidence to be filling in* (OUT), or is its future one that *cannot be judged* (TOO HARD)? The
evidence shows the growth filling in and the regulatory mechanism under pressure; it does not show the earning power
filling in. The return was just renewed, rate base is rising, and Oregon's decoupling protects margin against falling use.
What would show it filling in is a regulator refusing the return or the recovery of rate base at scale, and that has not
happened beyond the $13.7M line extension write-down. So the moat is tenuous rather than shown open: "when we see a moat
that’s tenuous in any way [...] it’s just too risky. We don’t know how to valuate that, and therefore we leave it alone"
**[M2000-019]**; where the threat cannot be figured, "we don’t even think about it then" **[M2000-014]**; "If we can think of
very much that can go wrong with them, we just forget it" **[M2000-016]**.

**The cause.** The deciding question is a forecast of two legislatures, two commissions, an environmental agency and the
appellate courts of two States over fifteen years. No filing not yet read could answer it: the issuer's insiders say in its
filings that they cannot predict it, which is the test of a forecast they "would not want to put down on paper"
**[M2000-105]**; "If something’s important but unknowable, forget it" **[M2006-076]**; "We couldn't solve this problem,
moreover, even if we were to spend years intensely studying those industries" **[L1993-023]**. The company does file
integrated resource plans with twenty-year scenarios; they are scenarios because the policy path is not known, and the
OPUC's acknowledgment of a plan "does not constitute ratemaking approval of any specific resource acquisition strategy or
expenditure" (10-K Item 1). The cause is NATURE, not WORK.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**: the castle stands today; whether it stands ten to twenty years out turns on
  state climate policy that the company's own filings say cannot be predicted. A lower price does not reopen it
  **[M2000-038]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING. NOT REACHED (the file closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED as a question; the reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.
## Q8, Q9, Q10, Q12: NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q2**: the NWN Gas Utility (87.5% of five-year operating income) holds an exclusive,
rate-regulated territory whose return both States renewed within the year, but whether it stands ten to twenty years out
turns on Oregon's and Washington's climate laws and their regulators' treatment of a growing rate base over a shrinking
customer base, a forecast the company's own filings say cannot be made. No research pass (the cause is NATURE). Integrity
facts recorded, not judged (an adjusted EPS featured in the proxy that excludes a regulatory disallowance; see AFTER THE
STOP, Q5). For the operator's reporting figures, the COMPUTATION below finds no case of the range earning the floor at
$48.99: value range -$5.49 to $2.64 a share (all-equity, at the 5.43% Treasury rate); fair price -$37.16, not positive
(equity-only $17.65).

---
## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box is unchanged, operator rule 2.)*

**Bearing on Q3 (capital).** Capital spending against depreciation, NW Holdings ($M; 10-K cash-flow statements): 2021
293.9 / 113.5; 2022 338.6 / 116.7; 2023 327.3 / 125.6; 2024 394.4 / 137.9; 2025 466.9 / 165.5; spending ran 2.6 to 2.9
times depreciation. Plan 2026-2030: $2.6B to $2.9B (NW Natural $1.6B to $1.8B; SiEnergy $750M to $800M; NWN Water $250M
to $300M). The NW Natural spending is described as "continued investments to support the safety and reliability" of the gas
utility (10-K FY2025 Item 7) while its meters grew 0.5% in 2025: the spending above depreciation buys rate base, not volume.
What that rate base earns: authorized 9.5% on equity at 50% equity and 4.74% on debt in Oregon (overall 7.12%); earned,
consolidated, 5.9% to 8.8% on equity 2018-2025. Acquisitions, net of cash: $1.3M, $94.3M, $7.5M, $29.8M, $338.1M (2021-2025),
plus $156.1M of debt assumed in 2025 (SiEnergy and Pines, cash consideration $331.5M).

**Bearing on Q4 (the accounts).** *Balance sheets, 2017-2025* (`tools/run.py` ten-year table from first-filed XBRL,
checked against the filed FY2025 and FY2023 statements; $M): total assets 3,040 to 6,167; equity 743 to 1,475, of which
common stock 449 to 1,044 (issuance) and retained earnings 302 to 436 (only $134M kept in eight years); goodwill 0 to 371
(water purchases from 2019, SiEnergy 2025); debt on the face of the balance sheet 834 to 2,605 (2,623 at 2026-06-30); cash
3 to 38, never large. NW Holdings' consolidated capital at 2025 year-end: common equity 36.2%, long-term debt 55.7%,
short-term and current debt 8.1%, against 49.4% equity at NW Natural: the holding company carries its own debt above the
ring-fenced utility. Non-current regulatory assets 424 at 2025 year-end and 641 at 2026-06-30; other non-current liabilities
186 to 411 in the same six months, the jump being the Gasco uplands environmental estimate (below, Q9). Receivables and
inventory move with gas prices and weather, not ahead of sales. What the figures cannot say: whether the regulatory assets
(environmental, CPP deferrals, pension) will be recovered, which depends on the same regulators as Q2. *The real costs:*
stock pay $3.2M to $4.1M a year (shown in the equity statement, inside "Other" in operating cash flow); cloud-software
spending of $10.4M to $22.4M a year sits inside operating cash flow; the RNG facility prepayment of $51.4M (2024) sits inside
operating cash flow. *EBITDA:* not presented as an earnings measure; it appears (search "EBITDA") once in the 10-K FY2025, as a pay factor ("a
cumulative EPS or EBITDA factor" for performance shares), and once in the 10-Q, where the 2025-2027 and 2026-2028 LTIP
performance shares of certain participants are measured on "a 3-year cumulative EBITDA" (10-Q note on stock-based
compensation). The same 10-K note says that because "one of the performance factors" may "remain variable until the first
quarter of the third year", "no expense was recognized for the 2024-2026 performance share awards and the majority of the
2025-2027 performance share awards as of December 31, 2025": recorded stock pay in 2024 and 2025 omits most of those awards
(52,178 and 73,640 shares at target). *The featured adjusted figure:*
the 10-K and 10-Q feature "Segment EPS", a non-GAAP measure that divides each segment's GAAP net income by diluted shares
(it sums to GAAP EPS); the proxy features "adjusted EPS of $2.93" for 2025 and "$2.33" for 2024 against GAAP $2.77 and
$2.03, the 2024 adjustment excluding "the non-cash effects of a line extension regulatory disallowance" (DEF 14A
`0001193125-26-161075`, page 23).

**Bearing on Q5 (the people), integrity facts recorded, not judged.** (1) The adjusted EPS featured in the proxy excludes,
for 2024, a regulator's write-down of rate base, which is a real loss of invested capital; the framework records a featured
adjusted figure at Q4 as a weighing and judges it at Q5 with the rest of the record **[L2016-006]**, **[M2013-088]**; not
judged here. (2) The CEO since 2025-04-01, Justin B. Palfreyman (President from May 2023), was paid $3,695,467 in 2025
(summary compensation table), including a $333,594 bonus column entry. (3) The annual incentive plan includes "Achievement of
EPS, ROIC, net income, credit ratings, capital expenditure and investor relations goals" among individual goals; EPS targets
for the performance shares are set "on an annual basis in February of each year of the cycle", and the committee may adjust
for "unanticipated circumstances or significant non-recurring or unplanned events"; some performance shares of 2025 and 2026
are measured on cumulative EBITDA (Q4 above). No instance found of earnings guidance
in the 10-K or 10-Q text (search "guidance"); press releases were not read.

**Bearing on Q6 (the money and the owners).** *Retention:* from 2017 year-end to 2025 year-end the company kept $134M of
earnings and added $595M of common stock (issuance, stock pay, and shares for deals); market value went from $1,714M
(28.736M shares x $59.65) to $1,943M (41.564M x $46.74; year-end closes from the aggregator, flagged): $229M of market value
for $729M kept or raised. Dividends paid every year while shares were sold through the ATM program ($47.4M net in 2025;
$400M authorized; $103.4M remaining at 2025 year-end); the dividend has risen each year since 1956, by about one cent a
share a year lately ($1.9425, $1.9525, $1.9625 paid, 2023-2025). No buyback. *Pay:* performance shares pay only above a
three-year average ROIC threshold of 4.63% (2025 grants), 4.26% (2024) and 4.21% (2023), below the 5.43% Treasury rate;
then on three-year cumulative EPS against annually set targets, with a relative TSR modifier; 35% of long-term awards are
RSUs with a performance threshold (DEF 14A). *Deals:* SiEnergy and Pines paid in cash and assumed debt (acquisitions under
Q7's definition, not mergers); 2023 business combinations partly paid in shares ($12.9M of shares issued).

**Bearing on Q9 (could it ruin us).** Debt: $2,623.7M at 2026-06-30 against income from operations of $280.9M (2025) and
interest expense of $122.5M (2025); pre-tax earnings over interest 2025 = (154.7 + 122.5) / 122.5 = 2.3 times. NW Holdings'
covenants: consolidated indebtedness to capitalization at 70% or less; NW Natural's dividends to the holding company stop if
its equity ratio falls below 44% or its secured rating falls to BB+ or Ba1 (ring-fencing, 10-K Item 7). Debt maturing within
a year at 2026-06-30: $125.7M plus $121.3M short-term. Environmental: Gasco uplands recorded at $284M, "the low end" of
$284M to $950M (revised feasibility study, April 2026); Gasco sediments recorded at $53M against $53M to $350M; Portland
Harbor natural-resource damages at the low end with "the high end of the range cannot be reasonably estimated"; recovery
sought through the Oregon SRRM, "subject to an earnings test" (10-Q Q2 2026 note 16). Single interstate pipeline supplies the
system (Item 1A). Two climate suits name the company (Note 17).

### COMPUTATION, NOT A CLEARANCE (the operator's reporting figures; Q7's construction applied after a closing STOP)
Script and output: `Test Runs/_research 2026-10-18 NWN/q7_computation.py`, `q7_computation_out.txt`. USD millions.

**Owner cash, five-year window 2021-2025**, from the filed cash-flow statements (10-K FY2023, FY2025): operating cash flow,
plus interest paid after the company's own tax (effective rate each year, 25.2% to 28.3%) for the all-equity basis, less
stock pay, less capital spending (all-spending) or less depreciation (maintenance-only; the depreciation charge as the proxy
for required spending **[M1998-127]**, and no filing gives a lower maintenance figure; the filing's own description of the
spending as safety and reliability work suggests depreciation is a floor, not a ceiling, for staying in place, as the rows
warn of railroads **[M2016-092]**):

| year | all-equity, all spending | all-equity, maintenance-only | equity-only, maintenance-only | spending above depreciation |
|---|---|---|---|---|
| 2021 | -104.7 | 75.6 | 43.2 | 180.4 |
| 2022 | -156.2 | 65.7 | 27.7 | 221.9 |
| 2023 | 8.6 | 210.4 | 150.8 | 201.8 |
| 2024 | -146.2 | 110.3 | 59.2 | 256.5 |
| 2025 | -120.4 | 181.0 | 99.5 | 301.4 |
| mean | **-103.8** | **128.6** | **76.1** | **232.4** |

Working capital is inside operating cash flow throughout (specific (d)); 2023's high figure is a gas-cost collection year,
not removed. Net debt $2,599.4M (2026-06-30). EV at the price $4,661.6M. Maintenance-only owner cash on EV: **2.76%**;
equity-only maintenance-only owner cash on the market value: 3.69%.

**The specifics, applied.** (c) Acquisitions: $471.0M over the window against half of maintenance-only owner cash before
purchases, $321.5M: the serial-acquirer specific applies, and the central figure is the organic pair (purchases left out);
the default pair (purchases deducted, $94.2M a year) is shown beside. (b) The all-spending series changes sign: its growth is
meaningless, and on that basis the range is the no-growth case alone. (e) The filing allows the maintenance guess
(depreciation), so the central case is maintenance-only, with the spending above depreciation ($232.4M a year) charged
against the growth it buys. (f) The maintenance-only series shows 27.2% a year between its halves, which carried ten years
would need owner cash far above the highest share of sales the filings show (17.6%, 2023): absurd; the sales growth of the
window is 10.6%, above the discount rate, so the cap is 5.43%. **CONVENTION of this run:** (e) forbids charging the growth
spending while capping the growth it bought, and (f) cuts the shown rate; the two are reconciled by crediting the growth
spending with what the filed rate orders say it earns, the authorized return, taken unlevered after the company's tax:
50% x 9.5% + 50% x 4.74% x (1 - 26.7%) = **6.49%** a year in perpetuity on each year's spending (Oregon order of
2025-10-24); rationale: the regulator's order is the filing that states what the added capital earns, and it is more
generous than the 5.9% to 8.8% the company actually earned on equity. Purchases and growth spending stop after year ten.

**The range (all-equity basis, at the 5.43% Treasury rate), per share, net debt deducted:**
- No-growth case, maintenance-only: 128.6 / 0.0543 = 2,368 less 2,599.4 = **-$5.49**.
- Growth case, spending above depreciation charged and credited at 6.49%: **$2.64**. (At the Treasury rate the regulated
  return slightly exceeds the discount rate, so growth adds a little; at ten percent it destroys value, the inversion of (e).)
- Beside: the literal window, all spending, no growth: -$107.16; the default pair (purchases deducted), no growth: -$46.70;
  maintenance-only cash carried at 5.43% for ten years with no growth spending charged (not a case: it charges nothing for
  the growth): $25.07.
- **Value range: -$5.49 to $2.64 a share, against $48.99.**

**The floor, tested first** (CONVENTION of the framework): no case earns about ten percent at $48.99. The most generous stream
the analyst can write, maintenance-only owner cash growing 5.43% a year for ten years with nothing charged for the growth,
earns **4.33%** a year on the enterprise value at the price; on the equity alone, 5.67%. Both are below the floor **[M2003-149]**.
Had Q2 passed, Q7 would have closed OUT on the floor; the width test is not reached.

**Fair price** (Part VII: each end case valued at ten percent, the two averaged, after the company's own tax):
- **All-equity (central): -$37.16 a share, not positive** (no-growth end at 10%: -$31.20; growth end at 10%: -$43.12).
- Equity-only, beside: **$17.65 a share** (no-growth end $18.07; growth end, half the growth spending equity-financed at the
  9.5% authorized return on equity, $17.22). The two differ because the lenders take the first dollar of value; the all-equity
  figure governs **[L2017-004]**.
- No other price figure is reported.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `98520d0f`, before the first EDGAR call); written question by
      question; committed after Step 0 and Q1 (`46de7f08`) and after Q2 (`5a25d725`); the close committed with this section.
      **Defect declared:** the commit of Step 0 and Q1 carried two stripped filing excerpts (`_tmp_1a.txt`, `_tmp_mda.txt`,
      Item 1A and Item 7 of the 10-K, 116KB and 146KB) into the tracked tree; the Q2 commit removed them from the tree and they
      now sit in the ignored `cache/`. They remain in history at `46de7f08`; history is not rewritten.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock and the fold are the dispatching session's
      (operator rule ten). No git lock was met.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. Seen by accident and declared under
      CONTAMINATION above: four run file names of today in a directory listing, the NJR fold's commit subject in the session
      context, the memory index. Not used.
- [x] Every v5 id cited was checked against `principle_ledger_v5.csv` by the check script in the research folder
      (`idcheck.py`); every filing fact carries its document and accession; numbers not from a filing are labelled
      CONVENTION or come from the computation script.
- [x] The order was kept; Q2's STOP closed the file; nothing after it is a clearance; the Q7 figures are headed COMPUTATION,
      NOT A CLEARANCE and carry no entry language.
- [x] Owner cash after every real cost (stock pay deducted from the filed equity statement; all spending, or depreciation as
      the maintenance proxy, stated); never a net-income proxy. Sovereign from the US Treasury. Aggregator quotes flagged (the
      price; the year-end closes used in the retention fact).
- [x] Contrary evidence written down as found (THE FOUNDATIONS, five items) **[M1997-127]**; facts for later questions under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit; `idcheck.py` in the research folder: 41 ids, 22 quoted fragments beside ids checked against their rows, 0 problems, no E-ids.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for a slow, policy-driven threat.** Q1 defines understanding as "a reasonable fix on about what the
earning power and competitive position will look like in five or 10 years" **[M2012-065]**, and Q1's routing sends a business
whose ten-year economics cannot be foreseen "because its industry changes fast" to Q1 TOO HARD. NWN's ten-year economics
cannot be foreseen, but because state policy may change, slowly and by litigation, not because the industry changes fast.
This run read the policy threat as a castle question (Q2 test 11, slow change under Q2) and closed at Q2; another analyst
could close at Q1 with the same facts and the same box. The text does not say which question owns a political threat to a
regulated franchise. (2) **The regulated-return exception and the castle.** Q2 carries "a return set by a regulator" to Q3
as a second best, which settles the ordinary-return ground, but says nothing of a castle whose grantor is also the threat;
the framework's castle tests are written for competitors, and the attacker here is the State that grants the territory.
(3) **Q7 (e) against (f).** (e) forbids charging growth spending while capping the growth it bought; (f) cuts an absurd shown
rate to the sales growth, capped at the discount rate. For a utility whose spending buys rate base, both apply at once, and
the text gives no way to reconcile them; this run credited the growth spending at the authorized return as its own
CONVENTION, which is the filing that states what the spending earns. (4) **NATURE and the integrated resource plan.** The
test of NATURE is whether insiders "would not want to put down on paper" the forecast **[M2000-105]**; a utility does put a
twenty-year forecast on paper, as a set of scenarios required by its regulator. This run read scenarios plus the company's
"cannot predict" as a refusal to forecast; the text does not say whether a filed scenario set counts as a forecast written
down.
