# Company Run — Grand Canyon Education, Inc. (NASDAQ: LOPE) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md` (operator rule 10). The template was copied to this
file before any fetch; research folder `Test Runs/_research 2026-10-10 LOPE/` (raw filings under its `cache/`, ignored).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Contamination, declared and not used.** (1) The dispatching message says earlier Grand Canyon run files exist; none was
opened, listed or searched, and their dates, boxes and contents are unknown to me. (2) The session context showed, without my
asking, a git status listing other tickers' research folders (AYI, ARCB, BDC and others), five recent commit subjects about
other names (AME, ITW, JKHY, KEYS, KLAC and their boxes), and a memory index line saying that a count of gate-clearers exists
and "nothing buyable", that holding reviews are owed, and that wave 7 is paused. None of it names LOPE; none of it was used.
(3) `CLAUDE.md` (loaded automatically) points sessions to the register and the session-state file; I did not open them, by
the brief's blind rule, which governs.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $159.80 (close 2026-10-09; `tools/run.py`'s quote, an aggregator, **flagged** per operator rule 5: live quote
  only).
- **Shares by class** from the latest filing's cover: common stock, one class, **26,065,037** shares as of 2026-07-28
  (Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession `0001104659-26-088674`;
  `python Screens/cover_shares.py LOPE` returns the same count). Check against issued less treasury: the same 10-Q's
  balance sheet shows 54,265 thousand issued and 28,031 thousand in treasury at 2026-06-30, so 26,234 thousand
  outstanding; the cover count is 169 thousand lower, consistent with July repurchases (the program was active: 1,195,897
  shares bought in the first half, 10-Q note 10). No 8-K filed after the 10-Q reports a share issue; the 8-K of 2026-10-01
  (`0001104659-26-112835`) opens a $100.0 million revolver "primarily to fund repurchases", so the count may be lower again
  by the price date. No preferred, no options outstanding (proxy, `0001104659-26-047719`: "The Company does not have any
  outstanding stock options").
- **Market cap:** 26,065,037 × $159.80 = **$4,165.2M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-09 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): Form 10-K for FY2025 (filed 2026-02-18, `0001104659-26-017047`); Form 10-Q for
  Q2 2026 (filed 2026-07-30, `0001104659-26-088674`); proxy DEF 14A (filed 2026-04-23, `0001104659-26-047719`); 8-Ks of
  2025-10-30 (`0001104659-25-104492`, the summary of the government matters), 2025-12-15 (`0001104659-25-120898`, ED's
  recognition of GCU and the buyback increase), 2026-06-03 (`0001104659-26-069570`, the MSA letter of intent), 2026-06-25
  (`0001104659-26-077768`, a director's resignation), 2026-08-24 (`0001104659-26-100299`, the CFO's leave), 2026-10-01
  (`0001104659-26-112835`, the revolver), 2026-07-30 earnings release exhibit 99.1 (`0001104659-26-088669`), 2024-12-05
  (`0001558370-24-016051`, the cash pledged for GCU's loans); and for the span, the 10-Ks for FY2018
  (`0001558370-19-000782`), FY2021 (`0001558370-22-001269`), FY2023 (`0001558370-24-001060`) and FY2024
  (`0001558370-25-001150`), and the 10-Q for Q3 2024 (`0001558370-24-014620`, the end of the securities class action).
  **One figure cross-checked against the filed statement:** FY2025 net cash provided by operating activities, $273,491
  thousand in the filed consolidated statement of cash flows of the FY2025 10-K, against 273.5 (USD millions) in the XBRL
  series `tools/run.py` reads: they agree. Capital expenditures, $34,843 thousand filed, against 34.8: they agree.
- `python tools/run.py LOPE`, arithmetic lines only (its output is in the research folder, `run_py_output.txt`; nothing it
  prints as a rule, an id or a verdict is used, Part VII): OCF less stock pay less capital spending, USD millions:
  2023 185.9, 2024 238.5, 2025 225.0; three-year mean 216.5; five-year window mean 219.0. No securities inside operating
  cash, no other stock-pay line, no intangible or software payment beside capex. Stock pay 13.2 / 14.2 / 13.6. D&A
  (tagged) 23.1 / 27.8 / 31.2, plus amortization of purchased intangibles of 8.4 a year (Orbis, from 2019).
  **My recast for Q7** (research folder, `q7.py`, `q7_out.txt`): the run.py figure also removes the after-tax investment
  income, so that owner cash is before interest for the all-equity basis (Q7, On what the floor is earned):
  2021 234.1, 2022 171.0, 2023 177.8, 2024 226.3, 2025 214.3; mean **204.7**. (2021's investment income, 49.1 pre-tax,
  is mostly interest on the GCU secured note repaid that year; removing it is the point of the recast.)

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, and here the answer turns entirely on one customer, Grand Canyon University, and on the federal student-aid
rules its students borrow under; the quotation tells me nothing about either **[M2006-077]**. Who is paid to tell you: the
company's own releases lead with "Adjusted EBITDA" and per-share guidance, and its bonus plan pays on the same figure (Q4,
Q5); the seller's projection is not consulted **[M1995-050]**. No macro enters: the federal policy question is not a
macro forecast but a property of this business (who pays the tuition), and it is weighed at Q2 and Q7, not used to time
anything **[M2000-094]**. The analyst's habits: scuttlebutt last and "to possibly reject your original hypothesis"
**[M1998-144]**; the incentive in me (operator rule 9) is to close early, since a STOP saves the work of Q6 to Q10; I
record it so it can be checked.

**Contrary evidence, written down as found** **[M1997-127]**:
- (against the business) GCU, one customer, was 89.5% of 2025 service revenue (10-K FY2025, note 2).
- (against) The legal basis of the tuition-share fee is agency guidance, a 2011 Dear Colleague Letter, which the 10-K says
  "could be altered or removed without prior notice" (10-K FY2025, Item 1, Regulation).
- (against) The chief financial officer was placed on paid administrative leave on 2026-08-21 "in connection with an
  ongoing governmental investigation involving a non-employee third party's trades in Company stock" (8-K
  `0001104659-26-100299`).
- (against) A $35.0 million settlement of a False Claims Act suit over enrollment-counselor pay, recorded in 2025 (10-K
  FY2025, note 1; 8-K `0001104659-25-104492`).
- (for, against my first hypothesis that regulation makes it unforeseeable) GCU's enrollment rose from 90,297 (2017) to
  131,826 (2025) through six years in which ED refused its non-profit status, fined it, and the FTC sued; every government
  matter ended in 2025 without findings (8-K `0001104659-25-104492`).
- (for) The amended MSA of 2026-07-29 runs to 2041 and removes GCU's right to terminate for convenience (10-Q Q2 2026,
  note 11).
- (against) University partners other than GCU fell from 25 (end 2023, 10-K FY2023) to 20 (end 2025, 10-K FY2025).

## THE STANDING RULE
Owning a part-interest bought with cash, unlevered and sized below anything that could ruin the buyer, risks only what is
paid; the buyer's own financing and sizing are his to keep within "Never risk permanent loss of capital." **[L2023-005]**.
No borrowed money is contemplated **[L2014-005]**. Nothing in this name's own exposures reaches the buyer except through
the price paid.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**What the business is, from the filings.** GCE sells a bundle of services (counseling and admissions, marketing,
technology and academic support, back office) to universities for a share of their tuition. Its customer list is 20
universities (10-K FY2025, Item 1), but one customer is the business: Grand Canyon University, which GCE owned until
2018-07-01 and sold to an Arizona non-profit, took 89.5% of 2025 service revenue and 88.9% of 2024's (10-K FY2025, note 2,
Concentration of Credit Risk). The fee was 60% of GCU's tuition and fee revenue, ancillary revenue included (housing, food,
arena, hotel, golf course, apparel), under a Master Services Agreement of 2018-07-01 that ran to 2033-06-30 and that GCU
could end for convenience after 2025-07-01 on payment of a year's fees (8-K `0001104659-26-069570`). The amended MSA,
signed 2026-07-29 and effective 2026-07-01, runs to **2041-06-30**, renews automatically for up to three five-year terms,
removes the right to terminate for convenience, puts the fee at **60% of tuition and academic-related fees only**, ends a
reimbursement GCE had paid GCU, and replaces the non-renewal fee with eighteen months of continued service; GCE estimates
service revenue lower by about $20 million a year and operating income lower by "an immaterial amount" (10-Q Q2 2026,
note 11, `0001104659-26-088674`). The rest of revenue is healthcare programs run with other universities at 47
off-campus laboratory sites, the business bought as Orbis Education in January 2019 for $361.2 million in cash (XBRL
`PaymentsToAcquireBusinessesNetOfCashAcquired`, 10-K FY2019 `0001558370-20-001013`).

**The test as the draft states it.** "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years" **[M2012-065]**, asked first: "can I understand it?" **[M1995-051]**.
1. *The key variables and how predictable they are* **[M1998-044]**. Revenue is, near enough, 60% × GCU's tuition revenue
   (fixed by contract to 2041) plus a tenth from other partners. GCU's tuition revenue is enrollment × net tuition per
   student. Enrollment at GCU: 90,297 (2017), 97,369 (2018) (10-K FY2018); 108,139 (2021) (10-K FY2021); 117,279 (2023)
   (10-K FY2023); 123,149 (2024) (10-K FY2024); 131,826 (2025), of which online 107,148 and ground 24,678 (10-K FY2025);
   121,921 at 2026-06-30, online 113,011 (10-Q Q2 2026; mid-year counts are seasonally lower). Online is the engine:
   83,696 (2022) to 107,148 (2025); ground has been flat near 25,000 since 2022 (24,943 / 25,209 / 24,552 / 24,678). Net
   revenue per student has been flat (10-K FY2025, MD&A: "Revenue per student was flat between years"); GCU has frozen
   its campus tuition for years and the growth is volume. Costs are people and advertising (counseling 31% of 2026
   first-half revenue, marketing 22%, technology and academic 16%, 10-Q Q2 2026). These are few variables, each with a
   filed record of a decade.
2. *Do the past statements tell me the future ones?* **[M2008-033]**. Mostly yes: service revenue rose every year
   2019 to 2025 (778.6 to 1,106.1, USD millions), operating margin held between 24.0% and 26.7% from 2022 to 2025 after a
   higher 2019 to 2021 (the filer's own explanation of the drop is new sites and staff, MD&A of each year). The
   statements do not tell me the regulatory variable (below).
3. *Is it important and knowable?* **[M2006-076]**. The variable that could move everything is federal: GCU's students
   pay with Title IV loans and grants, GCU's eligibility rests on ED, and the tuition-share fee itself rests on a 2011
   Dear Colleague Letter that "could be altered or removed without prior notice" (10-K FY2025, Item 1). OBBBA's graduate
   loan caps and its program-level earnings test take effect July 2026, and the 10-K says "it is impossible to predict the
   outcome" of the rulemaking. Important, yes. Knowable over ten years, no, not in detail.
4. *Would the insiders write it down?* **[M2000-105]**. The insiders here write down one year (they publish an annual
   outlook, exhibit 99.1 of `0001104659-26-088669`) and refuse to write down the regulatory outcome. That cuts toward
   TOO HARD. But the record cuts the other way: between 2019 and 2025 ED refused GCU's non-profit status, fined it $37.7
   million, the FTC sued GCE and its chief executive, and a False Claims Act suit went to the eve of trial; through all of
   it GCU's enrollment grew from 97,369 to 131,826, and every government matter ended in 2025 without findings (8-K
   `0001104659-25-104492`). The rows say the speakers themselves erred in this direction: "we tended to overestimate the
   difficulties from regulation" **[M2004-058]**; of businesses "very much affected by the political process", "economics
   usually win out" **[M2012-074]**; and they put regulatory risk into the price, not into the circle: "If a thing is cheap
   enough, obviously you can afford a little more country risk, or regulatory risk, or whatever." **[M2004-083]**.
5. *Is the forecast about customers or technology?* **[M2017-019]**, **[M2023-030]**. About customers: working adults
   and nurses choosing a low-priced, Christian, online-heavy university with heavy counseling. Technology (an LMS,
   AI tools) is a cost line, not the product.
6. *How far off could I be?* **[M2011-084]**. Far, on one road: a hostile rewrite of the incentive-compensation guidance
   or of Title IV eligibility. The for-profit sector's own history (Mueller ran Apollo's University of Phoenix from 2006
   to 2008, proxy) shows enrollment can fall by most of itself in a few years when Washington turns. That range is weighed
   at Q2 (what could destroy it) and Q7 (how sure), as the rows weigh regulatory risk **[M2004-083]**.
7. *Do I doubt it is inside?* **[M2002-092]**. I doubt the regulatory forecast, not the economics: the mechanism (a
   fixed share of one university's tuition, costs that are people and advertising) is plain, and the doubt is about the
   size of the castle's threat, which is Q2's question.

**Routing.** Not a fast-changing technology business; not a financial institution; not a holding company (two parts,
handled at Q2 under the business-of-parts convention).

**VERDICT: IN**, narrowly. The economics are a fixed contractual share, to 2041, of one university's tuition, with a
decade's filed record of the two variables that drive it **[M2012-065]**, **[M1998-044]**; the federal risk is real and
unforecastable, and the rows send it to price and to the castle rather than to the circle **[M2004-058]**,
**[M2004-083]**. A reader who weighs test 4 the other way would close here TOO HARD (NATURE); I record that the call is
close.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now." **[M1995-038]**

**The parts table** (business of parts, CONVENTION of section B). GCE reports one segment and no operating profit by
partner, so the split is by revenue (10-K FY2025, note 2):

| part | share of 2025 service revenue | castle | decides? |
|---|---|---|---|
| Services to GCU (online and ground, including GCU's own ABSN sites) | 89.5% | read below | **yes** (more than half on any plausible margin split) |
| Services to the other 19 partners (healthcare programs at off-campus sites, from the Orbis purchase; one online partner) | 10.5% | contracts of 7 to 15 years with early-termination rights in some (note 1); partner count fell from 25 (end 2023) to 20 (end 2025) while site enrollment rose 16.6% in 2025 | no; carried to Q7 as an ordinary business at no growth if open |

**The castle tests, each with its filing fact (the deciding part).** The castle has two walls: the contract, and GCU's
own place among universities.
1. *The key factors and how permanent* **[M1995-038]**. The contract wall: 60% of GCU's tuition to 2041, no termination
   for convenience, eighteen months' tail after a notice of non-renewal (10-Q Q2 2026, note 11). Behind it, GCE employs
   the counselors, marketers, technologists and back office that GCU runs on (10-K FY2025, Item 1, Back-Office Services);
   GCU could not replace them quickly. The university wall: a low and long-frozen price, an online model at scale, a
   Christian identity, and heavy one-to-one counseling.
2. *Would it stand without the lord?* **[L2007-006]**. Partly no. The chief executive of GCE, Brian Mueller, is also the
   president of GCU (10-K FY2025, risk factors; proxy). The contract is now fixed to 2041 regardless of who runs either
   side, which is the strongest answer the filings give; the relationship beyond 2041 is a question about two boards,
   not a person.
3. *The money test* **[M2011-015]**. An attacker with money cannot take GCU's fee from GCE before 2041: the contract
   forbids it. An attacker with money can try to take GCU's students, and the largest attackers are already in the field
   and are not SEC filers (flagged): Southern New Hampshire University, Western Governors University, Liberty University,
   Arizona State University's online arm, Purdue Global. Through 2022 to 2025, against all of them, GCU's online
   enrollment rose from 83,696 to 107,148 (10-K FY2023, FY2025). The attackers have not taken it.
4. *Pricing power* **[M2005-020]**. None shown, and none sought: revenue per student "was flat between years" (10-K
   FY2025, MD&A), the growth is volume. This is the low-cost operator's choice, passing the advantage to the customer
   rather than banking it **[L1996-016]**, not a prayer session before a rise.
5. *Unit volume* **[M1999-054]**. Rising: GCU 108,139 (2021) to 131,826 (2025), 7.0% in 2025; online 8.7% in 2025 and
   7.8% in the year to 2026-06-30 (113,011 against 104,856, 10-Q Q2 2026).
6. *The low-cost position* **[L2004-007]**. GCE's filings claim it, and the volume is consistent with it; I have no
   cost-per-student figure for the non-filing rivals to test it, which is a limit of this run.
7. *Would the customer choose it over the low bid?* **[M2017-009]**. The low bid in online degrees is WGU's flat-rate
   term; students choose GCU in rising numbers anyway. The other part tells the opposite story: five partners left
   between 2023 and 2025, and some partners renegotiated "the revenue share percentage was reduced" (10-K FY2025, MD&A).
8. *Ask the competitors*: the competitor row below, from their own filings.
9. *Widening or narrowing* **[L2005-010]**. Widening on the contract (eight more years, no exit right, at a cost GCE
   puts at about $20 million of revenue a year and an immaterial amount of operating income); narrowing on margin (31.5%
   to 34.1% in 2019 to 2021, 24.0% to 26.7% in 2022 to 2025, the filer attributing it to added sites and staff) and on
   partner count in the other part.
10. *What could destroy, modify or reduce it* **[M2000-014]**. Washington. The fee is lawful because of a 2011 Dear
    Colleague Letter that "could be altered or removed without prior notice" (10-K FY2025, Item 1); GCU's students pay
    with Title IV money; OBBBA's graduate loan caps and program earnings test bite from July 2026, outcome "impossible to
    predict" (10-K FY2025, Item 1). The rows put the speakers' own error on this side of the ledger: "we tended to
    overestimate the difficulties from regulation" **[M2004-058]**; "economics usually win out" **[M2012-074]**. Would the
    business be started today against its substitutes **[L2006-008]**? GCU's growth against SNHU and WGU says yes.

**The competitor row** (operating income ÷ revenue, from each filer's own 10-K series in XBRL, `peers_out.txt` in the
research folder; the latest 10-K accession named; span 2015 to the latest year):

| filer | latest 10-K | operating margin, by year | reading |
|---|---|---|---|
| **LOPE** | `0001104659-26-017047` | 2015 27.0, 2016 27.2, 2017 29.0, 2018 30.5, 2019 34.1, 2020 32.9, 2021 31.5, 2022 26.1, 2023 25.9, 2024 26.7, 2025 24.0 | highest and steadiest in the field |
| STRA (Strategic Education) | `0001013934-26-000006` | 16.0, 13.0, 11.5, -3.6, 11.1, 10.6, 6.5, 6.6, 8.4, 12.8, 13.7 | ordinary, merger-scarred |
| ATGE, renamed Covista Inc. 2026-01-28 (June years) | `0001104659-26-092044` | FY2019 12.6, 13.5, 14.5, 5.8, 11.6, 13.7, 19.1, FY2026 19.6 | improving recently |
| PRDO (Perdoceo) | `0001193125-26-059331` | -10.9, -4.6, 5.7, 12.3, 13.8, 20.8, 21.5, 18.6, 21.2, 25.6, 23.2 | losses to high margins on shrinking-then-stable revenue |
| APEI (American Public Education) | `0001201792-26-000004` | 15.9, 12.2, 11.6, 10.9, 4.5, 7.7, 7.3, -22.7, -8.0, 5.3, 7.4 | poor |
| TWOU (2U, the pure revenue-share servicer) | `0001459417-24-000011` (FY2023, last) | -17.4, -10.2, -10.5, -11.3, -42.9, -23.1, -17.7, -26.8, -23.9 | losses every year; Chapter 11 (8-K of 2024-07-25, item 1.03), deregistered (Form 15, 2024-09-25) |

**The field's returns over the last full cycle, judged in words** (section C). The field does not earn one return: the
pure revenue-share servicer (2U) never earned one and failed; APEI and STRA earned ordinary-to-poor margins; PRDO and
Covista earn high margins only lately. GCE earned the highest margin of the six in every year of the span, and on a
small tangible base (Q3). So this is not a standing castle that protects only ordinary returns. Neither is it a field
with a record of durable returns: the one company in it that resembles GCE's model most failed, which is the strongest
evidence against GCE's castle, and the difference is the one customer GCE created and has now contracted to 2041.

**VERDICT: IN.** The castle is standing on the evidence: a contract to 2041 without an exit right **[M1995-038]**, a
customer whose enrollment has grown against well-funded non-profit attackers **[M2011-015]**, and returns at the top of
its field through the whole span. The threat that could destroy it is federal and cannot be forecast; the rows weigh such
a threat rather than refuse it **[M2004-058]**, **[M2012-074]**, and it is carried to Q7 (how sure) and Q9. The non-GCU
part does not decide; its narrowing partner count is carried to Q7.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- *Return on the capital actually needed* **[M2010-090]**, measured on tangible assets **[M2011-060]**. At 2025-12-31
  (10-K FY2025 balance sheet; the same figures as comparatives in the Q2 2026 10-Q): total assets 992.3, less cash 111.8
  and investments 188.3, less goodwill 160.8 and intangibles 151.5, leaves 379.9 of operating assets, of which 96.6 are
  lease right-of-use assets; less non-interest current liabilities other than leases (payables 24.3, accrued pay 35.2,
  accrued 32.3, tax 3.4) the net tangible operating capital is about 188 (USD millions). Pre-tax operating income was 265.9
  after the $35.0 million settlement. The return on the capital the business needs is well above 100% a year; read with
  the leases capitalised it is still far above any rival in the competitor row. The test asks what the business needs,
  not what a buyer pays **[M2010-090]**; goodwill and the Orbis intangibles are what GCE paid, and they belong to the
  capital-allocation reading (Q6).
- *Reinvestment to stand still and to grow* **[L1999-024]**, **[M2000-144]**. Capital spending 28.9 to 44.5 a year in
  2021 to 2025 against depreciation of 21.4 to 31.2; the filer intends "approximately $30.0 million to $40.0 million per
  year" (10-K FY2025, MD&A), mostly fit-out of new laboratory sites. Working capital is small and stable (receivables 84.3
  at 2025 year-end on 1,106.1 of revenue). Service revenue rose 209.5 from 2021 to 2025 on almost no added tangible
  capital: "the best business is one that gives you more and more money every year without putting up anything to get
  it, or very little" **[M1998-081]**.
- *Where capital did go in*: $870 million lent to GCU as the 2018 purchase price (the secured note, repaid in 2021,
  10-K FY2018 and FY2021); $361.2 million for Orbis in 2019, a part whose partner count is now falling (Q2); $200 million
  of GCE's cash pledged in October 2024 as collateral for GCU's bank loans, released in December 2024 (8-K
  `0001558370-24-016051`). The first two earned or are earning; the third shows that GCE's capital stands behind its
  customer's balance sheet when asked.
- *The growth arithmetic* **[M2001-019]**. Growth here is cheap in capital and dear in counseling and marketing expense,
  which runs through operating income: it is already charged in the owner cash used at Q7.

**WEIGHS FOR**: a business that has earned very high returns on the tangible capital it needs and grows with little
added capital **[M1998-081]**, **[M1995-047]**; against it, only the capital it has put behind its one customer (the note
and the pledge), carried to Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, 2016 to 2025** **[M2025-032]** (`tools/run.py` table from the first-filed XBRL;
read against the filed statements of the FY2018, FY2021, FY2023, FY2024 and FY2025 10-Ks):

| year-end | assets | liabilities | equity | cash | receivables | goodwill | intangibles | lt debt | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 1,092 | 319 | 774 | 46 | 10 | 3 | - | 67 | 651 |
| 2017 | 1,304 | 318 | 986 | 153 | 11 | 3 | - | 60 | 854 |
| 2018 | 1,324 | 110 | 1,214 | 120 | 47 | 3 | - | 23 | 1,082 |
| 2019 | 1,690 | 247 | 1,443 | 122 | 49 | 161 | 202 | 141 | 1,341 |
| 2020 | 1,845 | 270 | 1,574 | 246 | 62 | 161 | 194 | 108 | 1,595 |
| 2021 | 1,223 | 178 | 1,045 | 601 | 70 | 161 | 185 | - | 1,855 |
| 2022 | 833 | 195 | 638 | 120 | 77 | 161 | 177 | - | 2,040 |
| 2023 | 930 | 212 | 718 | 146 | 79 | 161 | 168 | - | 2,245 |
| 2024 | 1,018 | 235 | 784 | 325 | 83 | 161 | 160 | - | 2,471 |
| 2025 | 992 | 245 | 747 | 112 | 84 | 161 | 152 | - | 2,687 |

What moved and why. 2016 to 2017: the owned university, with campus property, and small debt. 2018: the sale of the
university's assets to GCU for a secured note (not a column above; it sat in the asset total until repaid). 2019: Orbis
bought for $361.2 million, giving the goodwill of 161 and intangibles of 202 and the debt of 141 that funded it. 2021:
the note was repaid ($1,159.9 million collected, XBRL `ProceedsFromCollectionOfNotesReceivable`), debt was paid off, and
$803.8 million of stock was bought in (2022: $604.2 million). Since then equity has stayed near 640 to 785 while retained
earnings rose by about 220 a year: every year's profit has gone out as buybacks. Receivables track revenue (about a
month's revenue at year-end; lower mid-year, 34.2 at 2026-06-30, against a deferred revenue line of 15.1 that appears only
mid-year). No debt since 2021 until the revolver of 2026-09-28 (undrawn at the 8-K). Nothing builds suspiciously:
no prepaid or deferred asset accounts growing, no inventories, no reserves that move **[M1995-064]**. "what the figures
are saying and what they don’t say" **[M2025-032]**: what they cannot say is GCU's own condition, which drives 89.5% of
revenue and is not in these statements (GCU files no 10-K; its bond disclosures were not read: a limit of this run).

**The real costs.** Stock pay is expensed (13.6 in 2025) and is deducted again from operating cash at Q7 **[L2015-003]**.
Depreciation runs a little below capital spending, and the gap is charged by using capital spending, not depreciation, in
owner cash **[L2015-004]**. The Orbis intangibles (university partner relationships) amortize 8.4 a year; with partners
leaving, they deplete, so the charge is kept **[L2012-003]**. The $35.0 million settlement is a real cost and is kept in
the central figure **[L2016-007]**: litigation and regulatory costs recur in this company's history, though the earnings
release excludes "litigation and regulatory costs" as "unusual" charges. Contributions to private
school tuition organizations ($5.0 million in 2025) are made "in lieu of" state income tax and are a real cost either way.

**EBITDA in the filer's own mouth, guidance, the featured adjusted figure.** The quarterly release leads its highlights
with GAAP net income and then gives "As adjusted" figures and "Adjusted EBITDA", which adds back stock pay and "unusual
charges", and publishes per-share guidance for the quarter and the year (exhibit 99.1 of `0001104659-26-088669`). The
annual bonus of the named executives pays 50% on revenue and 50% on Adjusted EBITDA (proxy `0001104659-26-047719`,
CD&A). The rows: "the number of times we’re going to buy into a company [...] where people are talking about EBITDA, is
going to be about zero" **[M2002-026]**; "the scourge of earnings "guidance"" **[L2019-006]**; a management that
"regularly attempts to wave away very real costs by highlighting "adjusted per-share earnings" makes us nervous"
**[L2016-006]**. Under the convention of 2026-10-06 these weigh against here and are judged at Q5 with the integrity
record. Against them: GAAP figures come first in the release and every adjustment is reconciled; a management that "does
explain to you in clear terms what’s going on" is "a plus" **[M1994-018]**.

**VERDICT on the accounts: IN** (no confusion, no suspicion the statements themselves raise **[M1995-063]**,
**[M1995-065]**); **WEIGHS AGAINST** on the EBITDA, adjusted-earnings and guidance habits, carried to Q5 **[M2002-026]**,
**[L2019-006]**, **[L2016-006]**. The recast owner cash (Step 0) feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
"do we really want to be in partnership with this person and count on them to behave in the future" **[M2015-005]**. For
a marketable stock the reading tests carry the weight **[M2007-081]**: the record, the proxy, the reports **[M1994-009]**,
**[M1998-036]**.

**The record for (written first, since the incentive in me is to close).**
- Ability: Brian Mueller has run GCE since 2008 and GCU since 2012 (proxy). Under him GCU grew to 131,826 students, and
  the 2018 sale was carried through ED's refusal, a fine, an FTC suit and a securities class action, all ended by 2025.
  The record read against "the hand they were dealt" **[M1994-008]** is strong.
- Pay and ownership: Mueller's total pay was $2,020,867 in 2025, about the same in 2023 and 2024; salary $321,000, halved
  in 2018 for the dual role; he owns 295,628 shares, 1.1% (proxy, beneficial ownership at 2026-03-31). No options exist.
  On this evidence he has "gotten rich with their shareholders and not off their shareholders" **[M2003-055]**.
- The government matters ended without findings: ED rescinded its $37.7 million fine with "no findings, fines,
  liabilities or penalties of any kind"; the FTC voted unanimously to dismiss and the case ended with prejudice; the
  Ninth Circuit held ED had applied the wrong legal standard; the IRS reaffirmed GCU's exemption; ED recognized GCU as a
  non-profit in December 2025 (8-Ks `0001104659-25-104492`, `0001104659-25-120898`). The securities class action was
  settled with the insurers paying "the entire settlement amount" (10-Q Q3 2024, `0001558370-24-014620`).
- When the CFO matter arose, the board acted at once: leave from 2026-08-21, an interim CFO named, outside counsel
  engaged; "a pound of cure, promptly applied" **[M2017-007]**.

**The record against.**
1. **An open government investigation touching a top officer.** On 2026-08-21 the board placed Daniel Bachus, the CFO
   and a named defendant in the securities action and in Ogdon, on paid leave "in connection with an ongoing governmental
   investigation involving a non-employee third party’s trades in Company stock"; the company says it "is not a focus of
   this investigation" and that the leave "is not the result of any issues with the Company’s financial statements" (8-K
   `0001104659-26-100299`). Unresolved at the price date. It concerns trading in this very stock by an outsider, in
   connection with the officer who sees the numbers first.
2. **Money paid on the conduct alleged.** $35.0 million to settle a False Claims Act suit alleging enrollment counselors
   were paid in breach of the incentive-compensation ban (8-K `0001104659-25-104492`; 10-K FY2025). No admission, and ED
   agreed the current plans are lawful; but the suit survived summary judgment (10-K FY2023) and the money was paid.
3. **Fraud claims that survive.** Three private actions allege false statements about the time and cost of GCU's
   doctoral programs: Smith and Wang (a RICO count survived dismissal; class certification sought), Ogdon (RICO and New
   York claims survived; the CEO, COO and CFO are defendants), Valerio (nearly 300 plaintiffs; dismissal denied) (10-Q Q2
   2026, note 8). The government's version of the same allegation was dropped after a change of administration, which the
   company itself credits in part to "the new approach to these matters taken by the federal government" (8-K
   `0001104659-25-104492`): the merits were not tried.
4. **One man on both sides of the only contract that matters.** The chief executive of the vendor is the president of
   the customer, employed by both (proxy: salary halved "reflecting his dual employment by GCE and GCU"); GCU's pay to him
   is not in GCE's filings. The structure is disclosed and ring-fenced (barred from GCU's board and from the MSA
   negotiations, 10-K risk factors), and the 2026 amendment was negotiated under it. In 2024 GCE pledged $200 million of
   its shareholders' cash to secure its customer's bank loans (8-K `0001558370-24-016051`). "There are also readings in
   corporate culture that have to be made." **[M1998-121]**: from GCE's filings I cannot read whose interest prevails
   when the two diverge, and the 10-K says they may.
5. **The habits carried from Q4**: Adjusted EBITDA featured and paid on, quarterly and annual EPS guidance
   **[M2002-026]**, **[L2019-006]**, **[L2016-006]**; "Managers that always promise to "make the numbers" will at some
   point be tempted to make up the numbers." **[L2002-041]**. I found no instance of the numbers themselves being made up.

**Reading them together.** No single item is proof of dishonesty, and items 2 and 3 are allegations in an industry where
allegations are common. But the rule is applied on doubt, not on proof: "If you’ve got doubts, forget it." **[M2013-088]**;
and the speakers look "for the obvious cases of people you can trust", accepting "we may be wrong about a fair number that
we’re ruling out" **[M2007-092]**. With a live investigation of trading in the company's stock tied to its chief financial
officer, money paid to end a claim about how recruiters were paid, consumer fraud claims still alive against the top
three officers, a chief executive on both sides of the one contract, and a management that pays itself on Adjusted EBITDA
and guides to the quarter, this is not an obvious case of people one can trust. "Sincerity and empathy can easily be
faked." **[L2023-003]**.

**VERDICT on integrity: OUT**, on doubt and not on a finding (no court or agency has found dishonesty). **Ability WEIGHS
FOR** **[M1994-008]**. The file closes here. Q6 to Q10 and Q12 are NOT REACHED; the Q7 figures below are COMPUTATION, NOT A
CLEARANCE, and the facts found for later questions are under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED (Q5 closed the file). Facts under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. **COMPUTATION, NOT A CLEARANCE** (the two reporting figures the brief asks for; Part VII, The owner's price;
no entry language; operator rule 3). Research folder, `q7.py` and `q7_out.txt`.
- **Owner cash** after every real cost, after GCE's own tax, before interest (all-equity basis): operating cash less stock
  pay less all capital spending less after-tax investment income, USD millions: 2021 234.1, 2022 171.0, 2023 177.8, 2024
  226.3, 2025 214.3; **five-year mean 204.7**. Equity-only beside it (investment income kept): 272.7, 173.0, 186.0, 238.6,
  225.1; mean 219.1. GCE's effective tax rate ran 21.1% to 23.1%, so no carryforward adjustment arises.
- **Growth shown** on aggregate owner cash, end years 2021 to 2025: **-2.19% a year** (all-equity); -4.68% equity-only
  (2021 carries the GCU note interest). By specific (b) a negative growth makes the bottom of the range and no growth the
  top. Neither end year is a cyclical peak or trough on the filer's description; the 2025 settlement is kept in, with
  the figure without it shown beside (Q4).
- **Rate:** 5.60% (Treasury 30-year, 2026-10-09). Ten years at the shown growth, then zero nominal growth.
- **Net debt** at 2026-06-30 (latest filed balance sheet): borrowings nil; cash 171.1 and investments 103.5; net debt
  **-274.5** (net cash). Operating leases (104.2) left out, said so. The 10-Q's own subsequent event (the amended MSA) moves
  no cash; the revolver of 2026-09-28 is a later 8-K, undrawn at its date.
- **(a) VALUE RANGE, central, all-equity:** **$128.50 to $150.76 a share** (width 1.19 to one; whole business plus net
  cash, over 26,065,037 shares). Equity-only beside it: **$103.83 to $150.09**. The price, **$159.80**, is above the top of
  both.
- **(b) FAIR PRICE** (reporting convention: the price at which the midpoint case of the range, growth at half the shown
  rate for ten years then none, earns the floor of about ten percent on owner cash after the company's own tax, no
  conversion): **$83.49 a share** on the all-equity basis (central); **$71.85** on the equity-only basis beside it.
- **Beside the literal window, not deciding:** measured between the halves of the window (2021-22 against 2024-25) the
  growth is +2.83% and the all-equity range $150.76 to $186.14, fair price $97.00; with the 2025 settlement added back the
  growth is +1.42%, range $155.34 to $172.59, fair price $95.62. Every variant puts the fair price between about $72 and
  $108, well below $159.80; the owner-cash yield at the price is 5.26% against a 5.60% bond.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts under AFTER THE STOP.

---
## THE BOX
**OUT at Q5 (integrity, on doubt), integrity facts recorded, not judged beyond Q5's doubt.** Q1 IN (narrowly), Q2 IN,
Q3 weighs FOR, Q4 IN on the accounts and weighs AGAINST on the habits. For the record only (COMPUTATION, NOT A
CLEARANCE): value range $128.50 to $150.76 a share (all-equity; $103.83 to $150.09 equity-only) against a price of
$159.80; fair price $83.49 (all-equity; $71.85 equity-only). Had Q5 passed, the price sits above the top of the range and
the file would have closed OUT at Q7 by the floor convention.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q5 (integrity, for any later run to answer first):** the CFO's leave and the government investigation of a third
  party's trades (8-K `0001104659-26-100299`); the $35.0 million False Claims Act settlement (8-K
  `0001104659-25-104492`); the three surviving consumer actions (10-Q Q2 2026, note 8); the CEO's dual role (proxy
  `0001104659-26-047719`); a director of 17 years, the audit committee chair, resigned on 2026-06-22 with no reason
  given (8-K `0001104659-26-077768`); the chief information officer resigned in October 2025 (8-K `0001104659-25-102147`).
- **Q6, the money:** buybacks of $2,200 million for 25,363,153 shares since the program began, an average near $86.75
  (10-K FY2025); by year, 2021 $797.8 million for 9.199 million shares (about $86.7), 2023 $130.8 million for 1.170
  million (about $111.8), 2024 $165.4 million for 1.142 million (about $144.8), 2025 $255.3 million for 1.479 million
  (about $172.6), first half 2026 $195.7 million for 1.197 million (about $163.5) (10-Ks; 10-Q Q2 2026). The program
  names no price; it is a standing authorization ($2,545.0 million in total, expiring 2027-03-01). The 2025 and 2026
  purchases were made above the top of the computed range ($150.76). A $100.0 million secured revolver was signed on
  2026-09-28 "primarily to fund repurchases" (8-K `0001104659-26-112835`). No dividend. The company "intends to continue
  using a significant portion of its cash flows from operations to repurchase its shares" (10-Q Q2 2026). Orbis, $361.2
  million in 2019, the only acquisition. Bonus metrics: revenue and Adjusted EBITDA, 50% each, no capital charge;
  restricted stock vesting over five years by time only (proxy). Directors own little: 1,102 to 14,168 shares each apart
  from the executives (proxy).
- **Q9, debt and exposures:** no borrowings at 2026-06-30; operating leases 104.2; the new revolver carries covenants
  (leverage at most 2.0 times, fixed-charge cover at least 1.10, capital spending capped at $50.0 million a year) and an
  event of default on an amendment of or default under the GCU MSA that would be a material adverse change (8-K
  `0001104659-26-112835`). Exposure to GCU's own balance sheet: GCU refinanced with $520.0 million of bonds in December
  2024, after GCE had pledged $200 million of cash for GCU's interim bank loans (8-K `0001558370-24-016051`). One customer,
  89.5% of revenue.
- **Q12:** the newspaper test would meet the doctoral-program cost allegations (unresolved private suits) and the
  recruiting-pay settlement; none of the businesses the rows name.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Commits:** step 0 committed
      (`0f8d7ed2`). From Q1 on, every commit attempt met `.git/index.lock` held by another process (file dated
      2026-10-10 10:35:25 and unchanged through the rest of the run); I retried and did not delete it, per the brief. The
      questions were therefore written in order but committed late; see the reply for the commit that finally landed.
- [x] Dispatched: the brief allowed per-question commits; the lock in `Screens/_daily/` is the dispatcher's. Not yet
      folded (the dispatcher's step).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under Contamination at the top.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by the check script in the research folder; every filing
      fact carries its accession or its named filing.
- [x] The order was kept; Q5's STOP closed the file; the Q7 figures are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (OCF less stock pay less all capital spending), never a net-income proxy; the
      sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written as found (Foundations); facts for later questions under AFTER THE STOP with the
      integrity flag in the box line.
- [x] Not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS (2026-10-10, output `cf_out.txt` in the research folder: v5 ledger
      4280/4280 verbatim, phantom ids in 0 run files); the run's own check (`check.py`): no E-ids, 63 v5 ids all in the
      CSV, every quoted fragment beside an id found in its row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q5's doubt has no edge.** "If you’ve got doubts, forget it." **[M2013-088]** is applied on doubt alone, but the
framework does not say whose doubt about what: an open investigation touching one officer, allegations not tried on the
merits, and a disclosed dual role are each doubts of a kind, and a stricter or looser reader can close or pass the same
record. I closed on the combination, and say so; a written rule on unresolved matters (for example, whether a pending
investigation of an officer is a doubt by itself) would make two analysts agree. (2) **Q1 against Q2 on regulation.** A
business whose revenue rests on one agency's guidance letter can be sent to Q1 TOO HARD (NATURE) by test 4 (insiders will
not write the regulatory outcome down) or passed to Q2 and Q7 by **[M2004-058]** and **[M2004-083]**; the framework routes
fast technology change explicitly but not regulatory change, and I chose the second reading. (3) **Owner cash on the
all-equity basis** says "owner cash before interest" but not whether interest *income* on surplus cash is removed when the
cash is added back as negative net debt; I removed it (otherwise the cash is counted twice) and say so. (4) **Specific (b)**
gives no test for when an end-to-end rate is "meaningless": here 2021 carries the last of a seller-note's interest and the
end-to-end rate is negative while the halves give a positive one; I kept the literal rate central and showed both. (5)
**The fair price** is defined as the price at which "the midpoint of the range earns the floor"; whether the midpoint is the
midpoint value or the midpoint growth case discounted at the floor is not said; I used the second and named it.
