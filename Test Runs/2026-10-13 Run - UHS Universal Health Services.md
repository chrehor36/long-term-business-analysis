# Company Run: Universal Health Services, Inc. (NYSE: UHS), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template to this dated name before any
fetch. Dispatched blind run; working folder `Test Runs/_research 2026-10-13 UHS/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold, 2026-10-13, by the dispatching session after the run was committed: not held (`PORTFOLIO.md` carries no line for UHS or Universal Health).*

**Contamination, declared at the start (seen by accident, not used).** (1) A directory listing of `Test Runs/` that I
filtered for the ticker showed one file name, `2026-07-15 Run - UHS (Universal Health Services).md`. I did not open it;
the filter itself was a listing the blind rule forbids, and I declare it here. Its date places it before v4.1. (2) The
session's opening git snapshot showed the subjects of the last commits, which describe a THC (Tenet) v5 run closed TOO HARD
(NATURE) at Q1, with figures and a phrase about hospitals, the parts test and the OBBBA's supplemental layer. Tenet is a
hospital operator and a natural rival. I took none of its figures, I did not use Tenet as a competitor in Q2 (partly for
this reason; see Q2's convention), and I wrote Q1 below from UHS's own filings. A reader should still weigh the
possibility that the THC subject line anchored me toward the same question; I state the counter-case at Q1 for that reason.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $178.90 a Class B share (2026-10-13 quote printed by `python tools/run.py UHS`; aggregator, live quote only,
  flagged under operator rule 5).
- **Shares by class**, cover of the 10-Q for the quarter to 2026-06-30 (filed 2026-08-07, accession
  `0001193125-26-340278`), as of 2026-07-31: Class A 6,574,600; Class B 51,687,770; Class C 661,688; Class D 12,457;
  **58,936,515 in all** (`python Screens/cover_shares.py UHS`). The charter note: Class A, C and D "are not traded in any
  public market, but are each convertible into shares of our Class B Common Stock on a share-for-share basis" (10-K FY2025,
  Item 5, accession `0001193125-26-071676`), and the company's own basic share count for earnings per share is all classes
  together (63,581 thousand weighted for 2025 against a January 31, 2026 cover total of 61,086,640), so every class is
  counted; the classes share alike in dividends (the 10-Q, Note on earnings per share: "$11.8 million, or $.20 per share, during
  the second quarter of 2026", which at $0.20 is about 59 million shares, every class) and differ only in votes.
  Votes: Class A one, Class B one tenth, Class C one hundred, Class D ten; Class A and C, 11.9% of the shares, carry 91.3%
  of the general voting power and elect five of the seven directors (proxy, `0001193125-26-148814`); Alan B. Miller holds
  77.8% of Class A and all of Class C, 88.9% of the general voting power (proxy ownership table). See Q6 facts. The company holds no treasury stock line on its balance sheet: repurchased shares are retired (the 10-K, Item 5,
  table of shares "cancelled"). Check against later filings: the two 424B5 prospectus supplements of August 2026
  (`0001193125-26-341420`, `0001193125-26-348053`) are debt offerings and carry no newer share count; the 8-K of
  2026-08-17 (`0001193125-26-354078`) converts unvested Talkspace awards into Class B awards, a small number not stated;
  buybacks after July 31 are not yet filed. The July 31 cover count is used.
- **Market cap:** 58,936,515 × $178.90 = **$10,544M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 10/09/2026, the
  latest print (`python tools/sources.py`, run 2026-10-13; 10/12 was a bond-market holiday). The earnings currency is USD;
  the U.K. business is about 6% of revenue (10-K FY2025, Item 1: U.K. net revenues "approximately $1.001 billion in 2025").
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-25, `0001193125-26-071676`): Items 1, 1A, 5, 7 (overview,
  forward-looking factors, segment results, sources of revenue, the supplemental payment programs, the OBBBA section,
  liquidity), 8 (income statement, balance sheet, cash flows, Notes 8, 9, 10 and 12). 10-Q for the quarter to 2026-06-30
  (filed 2026-08-07, `0001193125-26-340278`): cover, balance sheet, liquidity, the supplemental and OBBBA update, the
  Talkspace and Ireland deals. Proxy DEF 14A filed 2026-04-09 (`0001193125-26-148814`). 8-Ks: 2026-08-13
  (`0001193125-26-348057`, underwriting agreement), 2026-08-17 (`0001193125-26-354078`, Talkspace closed), 2026-08-21
  (`0001193125-26-359953`, notes issued). For the span: 10-Ks FY2024 (`0000950170-25-027785`), FY2023
  (`0000950170-24-021175`), FY2021 (`0001564590-22-006717`), FY2019 (`0001564590-20-006793`) and FY2016
  (`0001564590-17-002860`), each read for the segment note, the supplemental payment table and, where named, the cash flow
  statement.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025,
  $1,864,397 thousand on the filed consolidated statement of cash flows (10-K FY2025), equal to the 1,864 that
  `tools/run.py` transcribed from the tagged data; capital spending 2025, "Property and equipment additions (1,015,152)",
  equal to its 1,015.
- **`python tools/run.py UHS`, arithmetic lines only** (Part VII: nothing it prints as a rule, an id or a verdict is used).
  Owner cash as filed, operating cash less stock pay less capital spending, USD millions: 2023 437, 2024 1,024, 2025 754.
  Stock pay 88, 99, 96. Capital spending 743, 944, 1,015. Depreciation and amortization 568, 585, 619. Other capital
  payments it found: dividends to minority partners 7, 7, 12 and finance-lease principal 4, 4, 2. Its ten-year balance
  sheet table and debt lines are read at Q4's facts below. Its share basis is a stale weighted average and is not used; the
  cover count above is. The full ten-year owner-cash series, with the CARES Act timing corrected on the filer's own
  description, is built in the COMPUTATION below.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, bought for what the business will produce, and
the test is "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. For a hospital
operator that question becomes a question about who pays the hospital, and that is where this run spends its time. The
second bears as well: the market's price of $178.90 "just tells us prices" **[M2006-077]**, and the stock's fall from the
$228.30 average the company paid in the fourth quarter of 2025 (10-K FY2025, Item 5) is no evidence either way. No macro
view enters **[M2000-094]**: the federal law and the state programs below enter only because the filings name them as the
largest single source of this company's earnings, not as a forecast of the economy. **Contrary evidence, written down as
found [M1997-127]:** (1) the Medicaid supplemental payment layer is about two thirds of 2025 pretax income (Q1 below);
(2) pretax income excluding that layer was lower in 2025 than in 2016 on revenue 78% higher (Q1, Q2 facts); (3) two
behavioral-health jury verdicts with large punitive or trebled damages, and an insurance programme that from March 2025
excludes sexual abuse incidents (Q9 facts); (4) a 2020 False Claims Act settlement of the behavioral division with a
corporate integrity agreement (Q5 facts).

## THE STANDING RULE
The buyer's own conduct: a purchase paid in cash, never on borrowed money, and sized so that its total loss could not
touch what the buyer has and needs, "We are never going to risk what we have and need for what we don’t have and don’t
need" **[M2012-081]**; "Never risk permanent loss of capital" **[L2023-005]**; borrowing is "the one thing that ends — or
can prevent you from playing out your hand" **[M2004-065]**. Nothing about UHS changes this; its own debt is the target's
and is weighed at Q9, not here. Clear on the buyer's conduct as written.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the text states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in
that particular business, and evaluating how predictable they were first", and "If something is not very predictable,
forget it." **[M1998-044]**; the question is whether "the financial statements will tell me the information that’s useful
to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**; and
"If something’s important but unknowable, forget it." **[M2006-076]**. Precision asked is low; the product is not the
question, the economics are.

**Lines of evidence, chosen from the 10-K and why** (the brief's departure from the canonical brief, stated here): from
Item 1, the two segments and their facilities, and the commercial health insurer inside them; from Item 1A, the first two
risk factors (state concentration in Texas, Nevada and California; payments from government and third-party payers) and
the regulatory risks (Medicare and Medicaid funding, the OBBBA, litigation and accreditation); from Item 7, the
forward-looking factors list, the segment results, Sources of Revenue and its "Summary of Various State Medicaid
Supplemental Payment Programs" table, and the OBBBA section, because the 10-K itself presents the supplemental payment
programs as the single item most sensitive to "regulatory, economic, environmental and competitive changes in those
states". Labor (salaries 47% of 2025 revenue), professional liability (Note 8) and the U.K. are the other lines; labor and
liability are read at Q2 to Q9 facts, the U.K. at Q2.

**The parts.** The filer reports two segments with different economics (Note 12). Segment pretax income, USD millions, on
the filer's bases (2021 to 2023 "before allocation of corporate overhead", 10-K FY2023; 2024 and 2025 "reportable segment
income before income taxes" under ASU 2023-07, 10-K FY2025; the two bases are close but not identical, said so):

| year | Acute care | Behavioral health |
|---|---|---|
| 2021 | 735 | 1,026 |
| 2022 | 430 | 980 |
| 2023 | 540 | 1,084 |
| 2024 | 840 | 1,356 |
| 2025 | 1,047 | 1,460 |
| five-year sum | 3,592 | 5,906 |

Behavioral health carries 62% of five-year segment pretax income and **decides** under Q2's business-of-parts convention,
which Q1's holding-company paragraph extends to operating segments. The file stands or falls on whether behavioral
health, and the company it decides, can be foreseen.

**Key variable one: who pays, and at what rate.** Behavioral health revenue 2025 by payer (Note 10, 10-K FY2025): Medicaid
18%, managed Medicaid 24%, managed care (commercial) 22%, U.K. revenue 13%, managed Medicare 6%, Medicare 4%, other 12%.
Forty-two percent of the deciding part's revenue is Medicaid. Company-wide, Medicare, Medicaid and their managed forms
are 52% of 2025 net revenue (11%, 12%, 15%, 14%). The rates are set by Congress, CMS and fifty state programs.

**Key variable two: the supplemental layer, and what it has done to the statements.** The 10-K's table of state Medicaid
supplemental programs (net of the provider taxes that fund them), against pretax income (consolidated statements of
income, same 10-Ks), USD millions:

| year | net benefit, provider-tax programs | pretax income | pretax less the layer | source of the layer figure |
|---|---|---|---|---|
| 2016 | 161 | 1,156 | 995 | 10-K FY2016 |
| 2019 | 225 | 1,066 | 841 | 10-K FY2019 (76 + 23 + 126) |
| 2021 | 430 | 1,293 | 863 | 10-K FY2021 |
| 2023 | 556 | 940 | 384 | 10-K FY2023 (165 + 9 + 382) |
| 2024 | 963 | 1,498 | 535 | 10-K FY2025 |
| 2025 | 1,283 | 1,972 | 689 | 10-K FY2025 |

With the DSH and plan-amendment programs added, the 2025 layer is $1,339M, 68% of pretax income. The layer grew about
eightfold in nine years; pretax income without it was lower in 2025 than in 2016 on net revenue of $17,365M against
$9,766M. The past statements therefore show a business whose earnings growth came from a payment layer created year by
year by state programs and CMS approvals, not from the hospitals' own pricing or volume; on **[M2008-033]**'s test, the
past statements do not tell me what the future ones will look like, because the layer that made them is now scheduled
by law to shrink.

**What the insiders write down, and what they refuse to.** The test is whether the insiders "would not want to put down on
paper their predictions" **[M2000-105]**. The company's own words, read in full:
- On the OBBBA's provider-tax and directed-payment limits it does write a number: in the 10-K, "approximately $432 million
  to $480 million by 2032"; in the 10-Q six months later, "approximately $500 million by 2032", on a 2026 net benefit now
  estimated at "approximately $1.520 billion" (it was $1,362M in the 10-K's "Estimated 2026" column). It adds: "We cannot
  predict, among other things, if this legislation will ultimately be implemented as enacted, or if certain states may
  attempt to modify their respective SDP program [...] our forecasted estimates are subject to change, potentially by
  material amounts" (10-K FY2025, OBBBA section).
- On CMS's January 2026 provider tax rule: "We are unable to determine the financial impact on our future Medicaid
  supplemental payments." (10-K and 10-Q).
- On the Medicaid eligibility rules (work requirements, six-monthly redeterminations): "we cannot predict the potential
  unfavorable impact on our future results of operations" (10-K and 10-Q).
- On the 2024 Managed Care Rule: "we are unable to estimate the impact" (10-K). On California's change to inpatient
  psychiatric Medi-Cal rates, a behavioral-health item: "We are unable to predict with certainty the impact [...] under
  some scenarios, the adverse financial impact could be material." (10-K).
- On the programs themselves: "Most of these programs are approved on a year-to-year basis and there is no assurance that
  these revenues will continue at their current rates or at all." (10-K, Item 1A and Item 7).
The insiders wrote one partial forecast to 2032, moved it within six months, called it subject to material change, and
declined to forecast the rest. Nobody in the filing writes down where the payment layer, or the Medicaid base beneath
it, will stand in 2036.

**Does the deciding part escape it?** No, on the filing. The 10-K does not split the supplemental benefit by segment, but
the behavioral segment carries part of it: its Medicaid revenue rose from $1,139M to $1,349M in 2025, and the filer
attributes $36M of its 2025 revenue increase to provider tax assessments, which exist only to fund these programs (10-K
FY2025, behavioral segment results). Its pretax income on the before-overhead basis stood between $901M and $1,084M in
every year from 2015 to 2023 while its revenue rose from $4,400M to $6,191M (10-Ks FY2016, FY2019, FY2021, FY2023), then
rose to $1,356M and $1,460M in the two years the layer jumped. I cannot separate the part's own earning power from the
layer, and 42% of its revenue is Medicaid, the program whose eligibility the company "cannot predict".

**The verdict.** The key variable of the deciding part and of the whole is the level of government payment, and above all
a supplemental layer equal to about two thirds of pretax income, approved year to year and now cut by a law whose full
effect the company says it cannot estimate. It is important and it is not knowable **[M2006-076]**; it is "not very
predictable" **[M1998-044]**; and "if you have doubts about something being into your circle of competence, it isn’t"
**[M2002-092]**. **TOO HARD.** The cause is **NATURE**, not WORK: the forecast is of future legislation, CMS approvals and
fifty state financing decisions, which the company itself, the insider best placed to write it, declines to write
**[M2000-105]**; no filing not yet read would answer it, and "the nature of the industry would be the roadblock"
**[L1993-023]**. The box is not a judgment of quality or price: "It doesn’t mean it isn’t a good buy. [...] It just means
that we don’t know how to evaluate it." **[M2000-038]**, and the rows' three boxes put it in "too hard" **[M2006-013]**.

**The counter-case, stated as strongly as I can** (written because the THC subject line I saw could have anchored me).
Hospitals and psychiatric beds are not a fast-changing technology; demand for both is durable; UHS has run them since
1979; behavioral margins held near 17% to 23% before overhead for a decade; and the company has written its own estimate
of the main cut, so an analyst could value the business with the layer reduced by $500M and call that conservative. I
reject it for three reasons from the filings: the estimate covers one provision and the company calls it subject to
material change; the company declines to estimate the eligibility rules, the January 2026 rule and the Managed Care Rule,
any of which reaches the deciding part's Medicaid base; and after a $500M cut the remaining layer would still be about half
of 2025 pretax income and still approved year to year. A conservative number for a variable the insiders will not forecast
is not a fix on it. **[M2011-084]** asks also "how far off we can be"; here I cannot bound it.

**VERDICT: TOO HARD (NATURE).** The file closes at Q1. Q2 to Q12 are NOT REACHED; facts already found are written below
under AFTER THE STOP, not weighed.

## Q2 TO Q12: NOT REACHED (closed at Q1 by a STOP; operator rule 2)

---
## THE BOX
**TOO HARD (NATURE), decided at Q1**: the deciding part's and the whole company's ten-year earning power rests on
government payment levels, above all a state Medicaid supplemental layer equal to 68% of 2025 pretax income, approved
year to year and cut by a law whose full effect the company itself declines to estimate. No further work is done and a
lower price does not reopen it (section I). **Integrity facts recorded, not judged** (Q5 below). For the operator's
reporting figures (COMPUTATION, NOT A CLEARANCE, below): value range $122.54 to $188.49 a share against $178.90; no case
earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; no verdict; the box is unchanged.*

**Bearing on Q2 (the castle).**
- *Competitors.* The 10-K names rivals only by kind ("other facilities", hospitals "owned by tax-supported governmental
  agencies or by nonprofit corporations", physician-owned hospitals and surgery centers; Item 1, Competition); no rival is
  named, so none is flagged as a non-filer. **CONVENTION of this run:** three SEC filers chosen by me, HCA Healthcare (the
  largest acute operator), Community Health Systems (acute hospitals, mostly outside large cities) and Acadia Healthcare
  (the largest listed behavioral operator), so that both of UHS's segments have a rival; rationale: the brief allows up to
  three chosen filers when the 10-K names kinds only, and Tenet, the other obvious choice, was left out because a Tenet
  run's commit subjects were in front of me (contamination, above).
- *The competitor row*, from each company's own tagged 10-K figures (pre-interest pretax margin = pretax income plus
  interest paid, over revenue; owner-cash margin = operating cash less stock pay less capital spending, over revenue;
  averages of the years shown; HCA 10-K FY2025 `0001193125-26-044769`, CYH 10-K FY2025 `0001193125-26-059509`, ACHC 10-K
  FY2025 `0001193125-26-078266`, and the earlier 10-Ks those facts were first filed in):

| company | pre-interest pretax margin 2016-2025 | same, 2021-2025 | owner-cash margin 2016-2025 | same, 2021-2025 | capital spending / revenue 2016-2025 |
|---|---|---|---|---|---|
| UHS | 10.8% | 9.8% | 5.3% | 3.0% (CARES repayment in 2021 not corrected here) | 5.8% |
| HCA | 15.4% | 16.4% | 7.4% | 7.7% | 6.9% |
| CYH | 4.5% | 8.8% | 0.9% | -1.2% | 3.5% |
| ACHC | 6.1% | 4.1% | 0.0% | -5.4% | 12.7% |

  Read in the filings behind them: CYH's equity has been negative since 2017 and its revenue fell from $18,438M (2016) to
  $12,485M (2025) through divestitures; ACHC recorded goodwill impairment of $996M in 2025 and sold its U.K. business
  (its 2020 revenue drop); HCA's equity is negative ($-6,027M at 2025 year-end) from buybacks on debt. UHS's pre-interest
  pretax margin is second of four over the span, below HCA throughout.
- *The field's returns over the last full cycle, in the filer's own figures:* UHS pre-interest pretax income on its
  capital (equity plus debt less cash) was about 14.6% in 2016 (1,263 on 8,635) and 17.9% in 2025 (2,128 on 11,891); on
  tangible capital (goodwill and intangibles removed) about 27% in both years. With the supplemental layer removed, 2025
  is (689 + 156) on 11,891, about 7.1%, or about 10.8% on tangible capital (845 on 7,825) (10-K FY2025 and FY2016, balance sheets and
  statements of income).
- *Pricing power and the low bid:* the 10-K says hospitals compete for payer contracts "on the basis of price, market
  reputation, geographic location, quality and range of services" and that managed care plans "demand that we accept lower
  rates of payment" (Item 1, Competition). Net revenue per adjusted admission rose 5.4% (acute, same facility) and 7.5%
  (behavioral, same facility) in 2025 (Item 7). Salaries were 54.0% of same-facility behavioral revenue in 2025 against
  53.6% in 2024; behavioral pretax margin before overhead fell from 23.2% (2015) to 17.1% (2022) and recovered to 19.7%
  (2025, segment basis) (segment notes as above).
- *Attackers:* the 10-K names outpatient centers, addiction treatment centers offering medically assisted treatment,
  physician-owned hospitals and surgery centers; California psychiatric staffing standards from June 1, 2026 (Item 7,
  forward-looking factors). UHS bought Talkspace, a virtual behavioral care company, for about $835M on 2026-08-17
  (8-K `0001193125-26-354078`).
- *U.K.:* 161 inpatient behavioral facilities, revenue $1,001M (2025) against $880M (2024); U.K. assets $1,531M
  (Item 1).

**Bearing on Q3 (capital).** Capital spending rose from $520M (2016) to $1,015M (2025), against depreciation of $417M and
$619M; capital spending exceeded depreciation in every year 2016 to 2025 (tagged cash-flow figures, cross-checked for
2023 to 2025 on the filed statements). 2026 guidance: $950M to $1.1B (10-Q). New hospitals named: Alan B. Miller Medical
Center, Palm Beach Gardens, opening second quarter 2026; the Washington, D.C. and Las Vegas hospitals "relatively recently
opened" (10-K, Items 1 and 7). The filing gives no split of capital spending between maintenance and growth. Acquisitions
net of disposals were small in the window ($80M, $8M, $-20M, $-20M, $32M for 2021 to 2025), then $188M (Ireland, July
2026) and about $835M (Talkspace, August 2026), the second paid for a company whose own 10-K for 2025
(`0001193125-26-105146`) shows operating cash of $9M against stock pay of $8M on revenue of $229M.

**Bearing on Q4 (the accounts).**
- *The balance sheets, ten year-ends* (`tools/run.py` transcription, first-filed tagged values, USD millions, read against
  the filed balance sheets for 2023 to 2025): equity 4,533 (2016) to 7,276 (2025); goodwill 3,784 to 3,990, nearly flat,
  since acquisitions were small after 2016; intangibles 228 to 76; receivables 1,440 to 2,602, against revenue 9,766 to
  17,365, so receivables held near 15% of revenue (14.7% to 15.0%), with 2025's rise partly "a $145 million increase in net
  receivables recorded in connection with various Medicaid supplemental payment programs" (10-K, cash flow discussion);
  debt on the face 4,136 to 4,753; cash small every year except 2020 (1,224, the CARES advances); retained earnings 4,891 to
  7,993. Weighted basic shares fell from 97M (2016) to 64M (2025) through buybacks. What the figures say: the balance sheet
  grew with revenue, without a goodwill build-up and without a receivables build-up beyond the supplemental receivable
  named. What they do not say: how much of the receivable and of the earnings rests on programs approved year to year;
  the self-insured professional and general liability accrual was $449M and workers' compensation $152M at 2025 year-end
  (Note 8), and the company itself says "it is reasonably likely that our future financial results may include material
  adjustments to prior period reserves" (Note 8). Reserve increases "as a result of unfavorable trends": $45M (2025), $79M (2024), $25M (2023).
- *Real costs:* stock pay $96M (2025) is expensed. 2025 pretax income includes an unrealized gain on non-marketable
  securities of $93M (cash flow statement), the main cause of "Other (income) expense, net" of $(134)M. The company
  features an "adjusted net income attributable to UHS per diluted share", which for 2025 was $21.74 against GAAP $23.10,
  lower than GAAP; the adjustments it lists include "the impact of changes in the market value of shares of certain non-marketable and marketable securities" (proxy, Annex A reference). The company gives annual earnings guidance and
  raised it twice during 2025 (proxy, Compensation Discussion: "we publicly disclosed increases to our previously disclosed
  estimated range"). The make-the-numbers habit and guidance are recorded here and carried to Q5 under the v5 text; not
  weighed.

**Bearing on Q5 (who runs it): integrity facts, recorded, not judged.**
- 2019 to 2020: the behavioral division was the subject of DOJ criminal and civil investigations; the criminal
  investigation was closed; the civil False Claims Act investigation, focused on "medical necessity issues and billing for
  services not eligible for payment due to non-compliance with regulatory requirements relating to, among other things,
  admission eligibility, discharge decisions, length of stay and patient care issues", was resolved for $127M with a
  corporate integrity agreement with HHS OIG; "UHS denies any fraudulent billings were submitted to government payers"
  (10-K FY2019, `0001564590-20-006793`, Legal Proceedings; corporate integrity agreement filed with the 8-K of July 10, 2020,
  per the FY2021 10-K exhibit list).
- 2024: a jury found Cumberland Hospital for Children and Adolescents (a UHS subsidiary) liable to three plaintiffs for
  sexual misconduct by its former medical director, awarding $60M compensatory, $180M trebled under the Virginia Consumer
  Protection Act and $120M punitive (reduced by the court to $1.05M); about 40 more plaintiffs are pending, next trial
  tentatively August 2026; insurance remaining for the 2020 policy year about $143M (Note 8).
- 2025: a Nevada jury awarded $500M punitive damages against UHS of Delaware (the management subsidiary) for intentional
  interference with a rival medical group's physicians; the company expects reduction to about $14M under Nevada law and
  reserved $18M (Note 8).
- Lawsuits "on behalf of numerous former patients spanning decades claiming to be the victims of sexual assaults while
  patients at our facilities" (Note 8).
- The founder, Alan B. Miller (88), is Executive Chairman with 88.9% of the general voting power; his son Marc D. Miller is
  Chief Executive Officer; the CFO has been CFO since 2003 (10-K, Executive Officers; proxy). Pay 2025: Marc D. Miller
  $16.1M (salary $1.43M, stock $10.0M, cash incentive $4.29M); Alan B. Miller $8.1M including a discretionary bonus of
  $1.07M (proxy, Summary Compensation Table).
- The annual cash incentive for the CEO and CFO is 100% on corporate criteria tied to adjusted earnings per diluted share
  against the guidance range announced each February (proxy, 2025 Annual Cash Incentive Formula); the CEO's cash incentive
  was 300% of salary for 2025 and for 2024 and 225% for 2023 (non-equity incentive over salary, Summary Compensation
  Table).

**Bearing on Q6 (the money and the owners).**
- Buybacks: $1,221M (2021), $833M (2022), $547M (2023), $671M (2024), $968M (2025) (cash flow statements, including tax
  withholding repurchases); in 2025 "approximately 4.65 million shares at an aggregate cost of approximately $899.3 million
  (average price of $193.38 per share)", fourth quarter average $228.30; second quarter of 2026 average "approximately
  $169.43 per share"; the programme has "no expiration date" and names no price (10-K, Item 5; 10-Q). **The buyback test's
  line, written back from the COMPUTATION below:** the bottom of the computed range is $122.54 a share; every average price
  paid that the filings state ($193.38, $228.30, $169.43) sits above it. Not weighed.
- Dividends $0.20 a quarter; dividends paid $51M (2025).
- Control: Class A and C carry 91.3% of the general voting power and elect five of seven directors (proxy).
- Related parties: UHS advises Universal Health Realty Income Trust, chaired by Alan B. Miller, and leases hospitals from it
  (rent about $21.7M in 2025 for four hospitals; Note 9 and Item 1).
- Talkspace (about $835M cash, August 2026) and Ireland ($188M, July 2026): acquisitions for cash, not mergers; no shares
  issued except converted Talkspace awards (8-K `0001193125-26-354078`).

**Bearing on Q9 (could it ruin us).** Debt at 2026-06-30: $771.9M current and $4,079.9M long-term; cash $138.8M (10-Q
balance sheet). Then borrowed $400M under a delayed-draw term loan plus revolver draws for Talkspace (8-K
`0001193125-26-354078`), and issued $1,100M of senior secured notes due 2031 and 2036 at 5.5% and 6.0% (8-K
`0001193125-26-359953`), against the $700M 1.65% notes due 2026-09-01 that the 10-K expected to refinance "at significantly
higher interest rates". The credit facility and every senior note share a first lien (8-K `0001193125-26-359953`). Pretax income over interest 2025: (1,972 + 156) / 156,
about 13.6 times; with the supplemental layer removed, (689 + 156) / 156, about 5.4 times. Professional liability: self
insured to $20M per occurrence, excess cover about $110M in 2025 (from $250M in 2014 to 2020), and from March 2025
"coverage exclusions for incidents involving sexual molestation or abuse" and, from March 1, 2025, "the single self-insured
retention no longer applies in connection with claims made by multiple plaintiffs against our behavioral health care
facilities" (Note 8). Concentration: Texas, Nevada and California facilities; Texas 16% of 2025 revenue (Item 1A).

**Bearing on Q12.** No business named in Q12 is carried on; not asked.

---
## COMPUTATION, NOT A CLEARANCE: the owner's two reporting figures (Part VII), after a closing STOP at Q1
*Arithmetic only, by Q7's range convention, carried out because the operator asks for the two figures; it carries no
entry language and does not reopen the box (TOO HARD (NATURE) is not reopened by price). Script:
`Test Runs/_research 2026-10-13 UHS/q7.py`.*

- **Owner cash after every real cost** (operating cash, less stock pay, less capital spending, less ERP application
  spending, less dividends to minority partners, less finance-lease principal where found), after interest and after the
  company's own tax, USD millions: 2021 726, 2022 266, 2023 426, 2024 1,013, 2025 715. **Cycle base, specific (a):** the
  literal window's first year is aberrational on the filer's own description, operating cash in 2021 carrying the "early
  repayment of $695 million" of 2020 Medicare accelerated payments and an $84M installment of deferred payroll tax, with the
  second installment of $94M in 2022 (10-K FY2021); those repayments are added back to the year they were paid. The literal
  window is beside: 2021 -53, 2022 172.
- **All-equity basis (central, Q7 "On what the floor is earned"):** after-tax interest added back at each year's effective
  tax rate (interest paid 76, 120, 200, 168, 156); acquisitions net of disposals deducted (default pair, specific (c); not a
  serial acquirer in the window: net purchases $80M over five years against owner cash of about $3.1B). Series: 704, 349,
  599, 1,163, 802; **five-year average $724M**.
- **Growth shown:** aggregate, end year to end year, 704 to 802, **3.31% a year**; under the cap (sales grew 8.3% a year
  2021 to 2025; no share-of-sales absurdity). Specific (e): the filing gives no maintenance split, so the all-spending case
  is central and the depreciation variant is shown beside.
- **Net debt:** $4,851.8M debt less $138.8M cash at 2026-06-30 = $4,713.0M; plus the subsequent events the filings
  themselves state: Talkspace financing $835M less Talkspace's own year-end cash of $37M (its 10-K), and the Ireland
  purchase of $188M (10-Q) = **$5,699M**. Operating leases ($410M) left out, as the convention says. Talkspace is credited
  at nothing (its filed owner cash after stock pay is about $1M) and Ireland at nothing (no filed earnings).
- **Value range, all-equity basis:** no-growth case $12,921M, growth case $16,808M for the whole business, less net debt,
  over 58,936,515 shares: **$122.54 to $188.49 a share against $178.90.** Width 1.30 to one. Expected return at the price:
  4.45% (no growth), 5.78% (growth). **The floor is tested first: no case earns about ten percent at the price**, so on
  this arithmetic Q7 would close OUT, had Q1 passed.
- **Fair price (Part VII: each end valued at ten percent, the two averaged, all-equity, less net debt): $41.66 a share.**
  Equity-only beside: owner cash after interest and acquisitions, less $43M a year of after-tax interest on the debt added
  for Talkspace and Ireland, average $570M, growth 1.48%: range $172.63 to $194.18; **fair price $101.80**. The central
  figure is the all-equity one; the equity-only figure never decides alone.
- Beside, not central: literal window (no CARES correction; the series changes sign and the halves give a meaningless rate,
  so the no-growth case alone, specific (b)): $69.64, fair $-3.55. Depreciation variant: $209.18 to $339.67, fair $105.32.
  Organic pair (acquisitions left out): $127.40 to $156.88, fair $35.80. Sensitivity of my own, labelled as such and not
  part of the convention: the company's own estimate of the OBBBA cut (about $500M pretax by 2032, phased from 2028, after
  tax at 23.4%) deducted from the central case: $23.70 to $89.66, fair $-7.61.
- **Reporting figures for the operator (a reporting convention, not a rule; COMPUTATION): (a) value range $122.54 to
  $188.49 a share (all-equity basis); (b) fair price $41.66 a share all-equity, $101.80 equity-only; price $178.90.**

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Q1 (the file closed there)
      and again at close (write-early).
- [x] Dispatched: the brief allowed per-question pathspec commits and states that the dispatching session holds the lock;
      the fold into the register is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Not fully kept:** I listed
      `Test Runs/` filtered for the ticker before I had read the brief's blind rule closely, and saw one file name; it is
      declared under contamination and was not opened or used. The THC commit subjects came with the session and are
      declared too.
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-13 UHS/check_ids.py`: no E-ids, every M, L or R id in
      the CSV, every quoted fragment beside an id inside that row); every filing fact has its accession; no number without
      a row or a filing.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance; the arithmetic
      after it is headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the US Treasury;
      the price quote flagged as an aggregator's.
- [x] Contrary evidence written down as found **[M1997-127]** (foundations line and the facts above); the facts found
      for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited (the run is dated today; no point-in-time anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before the final commit (see the close).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The parts test cannot be run cleanly when the decisive variable is reported only for the whole.** Q1's
holding-company paragraph, extended to segments, asks whether the deciding part can be foreseen, but UHS reports its
supplemental Medicaid layer only on a consolidated basis; I could show the deciding part shares the layer but not how much.
The text does not say whether an unsplittable consolidated variable is judged at the whole or at the part; I judged it at
both and found the same answer, but a different company could split the other way. (2) **Q1's test 5 ("Would the
insiders write it down?") has no rule for a partial forecast.** Here management did write one number (the OBBBA cut to
2032), revised it within six months, called it subject to material change, and declined the rest. I read a partial,
caveated forecast as not writing the forecast down; another analyst could read the written number as enough to build a
conservative case and pass Q1, which is the counter-case I stated. A line on partial insider forecasts would make this
reproducible. (3) **Q7's growth specifics meet a known, legislated decline.** The convention carries the growth shown, but
here the filing itself states a scheduled cut of about a quarter of pretax income; the convention gives no place for a cut
the filer quantifies, so I showed it as my own labelled sensitivity beside the central figure and did not let it touch the
reporting figures. (4) **Subsequent-event acquisitions and the target's cash.** The convention says to add a deal's
financing to net debt; it does not say whether the acquired company's own cash is netted. I netted Talkspace's filed
year-end cash and said so. Also noted, not a framework defect: the template's headings carry em dashes, which I replaced
with colons under the brief's prose rule.
