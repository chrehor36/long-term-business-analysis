# Company Run: Covista Inc., formerly Adtalem Global Education, formerly DeVry (NYSE: CVSA), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Filled top to
bottom from `Test Runs/_TEMPLATE - Company Run.md`; every judgment cites a v5 ledger id in bold; every filing fact carries
its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED. Working
folder: `Test Runs/_research 2026-10-06 CVSA/` (filings as fetched and as text, `value.py` and `peers.py`, tool outputs).

**IDENTITY.** SEC ticker list: CVSA, "Covista Inc.", CIK 730464, SIC "Services-Educational Services", fiscal year ends
June 30. Former names on EDGAR: DEVRY INC (1995 to 2013), DEVRY EDUCATION GROUP (2013 to 2017), Adtalem Global Education
Inc. (2017 to 2026). The rename to Covista Inc. was filed with Delaware on 2026-02-05 (8-K, accession
0001104659-26-011611); the ticker moved from ATGE to CVSA. No spin-off or merger in the rename. The business today is
five institutions bought between 2003 and 2021: Chamberlain University (nursing, bought 2005), Walden University (online,
mostly graduate, bought from Laureate on 2021-08-12 for about $1.49 billion, cash flow statement FY2022, accession
0001558370-22-013289), and AUC, RUSM and RUSVM (Caribbean medical and veterinary schools, bought 2003 and 2011). DeVry
University was sold to Cogswell on 2018-12-11 (10-K FY2019, 0001558370-19-008351), with the company indemnifying the
buyer for certain losses up to $340.0 million (10-K FY2026, Note 18); Adtalem Brazil and the
financial-services group (ACAMS, Becker, OCL, EduPristine) were sold by FY2022. The run is on the company as it now stands.

**POSITION NOTE, declared before any verdict:** not checked. The blind rule of this run forbids opening `PORTFOLIO.md`;
the run is written as if the name is not held.

**CONTAMINATION DECLARED.** (1) The session's git-status snapshot showed untracked run files dated 2026-10-06 for EMN,
LRN (Stride, an education company) and WWW, and the subjects of recent commits (INSW, NX and MTCH v5 runs with their
boxes and prices, a run.py change for vessel purchases, "Session state: S&P 600 ranks 41-50"). None was opened. LRN is
in the same industry; its run file was not read and it is not used as a competitor. (2) The auto-loaded memory index
carries one line on the queue ("57 gate-clearers, nothing buyable") and nothing about this name. (3) `tools/run.py`
prints v4 material; only its arithmetic lines were read (Part VII). No prior run file under CVSA, ATGE, Adtalem or DeVry
exists in `Test Runs/` (directory listing searched for all four names; none found). (4) While checking how other run
files spell the computation heading, a text search over `Test Runs/2026-10-05*.md` printed the names of three holding
reviews dated 2026-10-05 (BRK.B, CCB, HRB) and up to 25 characters after each "COMPUTATION" in those files; no verdict,
price or company fact was shown, and no file was opened. A breach of the letter of the blind rule, declared.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $125.39, close 2026-10-05, from `tools/run.py` (aggregator, live quote only, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: 34,038,820, single class, as of 2026-07-31 (10-K FY2026, filed
  2026-08-06, accession 0001104659-26-092044; `python Screens/cover_shares.py CVSA`). The proxy (DEF 14A filed 2026-10-02,
  accession 0001104659-26-113316) gives 33,860,208 outstanding on 2026-09-21; the cover count is used.
- **Market cap:** $4,268M (34.04M shares at $125.39).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05 (issuing
  authority, via `tools/run.py`).
- **Filings read** (operator rule 4): 10-K FY2026 (period 2026-06-30, filed 2026-08-06, accession 0001104659-26-092044):
  Item 1, Item 1A, Item 5, MD&A, the four statements, Notes 9, 12, 18 and 19. 10-Q for the quarter to 2026-03-31 (filed
  2026-05-07, accession 0001104659-26-057163, fetched; used only for the March 2026 debt amendment, which the 10-K repeats).
  Proxy DEF 14A (accession 0001104659-26-113316): CEO letter, pay design, ownership. 8-Ks: 2026-02-05 (rename,
  0001104659-26-011611), 2026-03-02 (Term Loan B, 0000730464-26-000010), 2026-07-28 (two directors,
  0001104659-26-087540), 2026-08-06 (results, Exhibit 99.1, 0000730464-26-000037), 2026-09-18 (term loan repricing,
  0000730464-26-000055). Prior 10-Ks for the ten-year record: FY2025 (0001558370-25-010780), FY2023 (0001558370-23-014509),
  FY2021 (0001558370-21-011957), FY2019 (0001558370-19-008351), FY2017 (0001144204-17-044976).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, continuing
  operations, FY2026: $470,796 thousand on the filed Consolidated Statement of Cash Flows (10-K page 56); the XBRL tag
  `NetCashProvidedByUsedInOperatingActivitiesContinuingOperations` gives 470.8M. Match. Revenue $1,954,085 thousand on the
  filed income statement matches the XBRL $1,954.1M.
- **`tools/run.py` arithmetic lines, checked against the filing.** OCF (total, including discontinued) 295.8 / 337.9 /
  470.4 for FY2024 to FY2026; SBC 25.9 / 41.6 / 41.2; capex 48.9 / 50.3 / 77.7: all match the filed cash-flow statement.
  Two corrections to what the tool prints: (a) its five-year window (FY2022 to FY2026, "OE capex 185.4") uses total OCF,
  in which FY2022 is $10.4M because of the cash taxes and costs of the businesses sold that year; continuing operations
  OCF in FY2022 was $163.8M (FY2022 10-K as restated in the FY2024 filing). The run uses continuing operations, because the
  sold businesses are gone; their legacy costs (DeVry indemnity, divestiture litigation) are noted as a contrary item.
  (b) The tool's "D&A" for FY2024 (75.3) includes $35.6M of amortization of Walden's acquired student relationships, a
  purchase-accounting charge now finished; depreciation alone was $39.7M. The tool's ten-year balance-sheet table starts
  in FY2021 because of a filer-number vintage gap; the table below is rebuilt from the first-filed XBRL back to FY2016.

**The balance sheets, eleven year-ends, before the income account** **[M2025-032]** (USD millions, June 30, first-filed
XBRL vintage of each year's 10-K, read against the FY2026 and FY2025 filed statements; FY2016 and FY2017 still include
DeVry University and Brazil, sold later).

| June 30 | assets | liabilities | equity | cash | receivables, net | goodwill | intangibles | long-term debt | retained earnings | shares on cover (M) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 2,097.0 | 509.8 | 1,582.1 | 308.2 | 162.4 | 588.0 | 342.9 | none tagged | 1,771.1 | 62.35 |
| 2017 | 2,314.0 | 638.7 | 1,669.0 | 242.0 | 173.4 | 851.3 | 413.8 | 125.0 | 1,881.4 | 62.08 |
| 2018 | 2,345.0 | 816.6 | 1,519.3 | 430.7 | 146.7 | 813.9 | 362.9 | 290.1 | 1,917.4 | 59.93 |
| 2019 | 2,242.7 | 841.6 | 1,391.5 | 299.4 | 157.8 | 874.5 | 418.1 | 398.1 | 2,012.9 | 54.92 |
| 2020 | 2,228.7 | 915.4 | 1,310.4 | 500.5 | 87.0 | 686.2 | 287.5 | 286.1 | 1,927.6 | 51.88 |
| 2021 | 3,053.8 | 1,751.0 | 1,301.1 | 494.6 | 65.9 | 686.4 | 276.2 | 1,067.7 | 2,005.1 | 49.62 |
| 2022 | 3,029.2 | 1,524.1 | 1,505.1 | 347.0 | 79.0 | 961.3 | 873.6 | 838.9 | 2,322.8 | 45.20 |
| 2023 | 2,810.5 | 1,353.2 | 1,457.3 | 273.7 | 100.1 | 961.3 | 812.3 | 695.1 | 2,403.8 | 41.54 |
| 2024 | 2,741.4 | 1,372.3 | 1,369.1 | 219.3 | 124.1 | 961.3 | 776.7 | 648.7 | 2,540.5 | 37.69 |
| 2025 | 2,752.4 | 1,318.7 | 1,433.6 | 199.6 | 143.4 | 961.3 | 765.5 | 552.7 | 2,777.6 | 35.96 |
| 2026 | 3,012.7 | 1,566.5 | 1,446.2 | 406.3 | 166.9 | 961.3 | 754.3 | 657.8 | 3,029.1 | 34.04 |

Accessions, in year order: 0001144204-16-121173, 0001144204-17-044976, 0001144204-18-046216, 0001558370-19-008351,
0001558370-20-010728, 0001558370-21-011957, 0001558370-22-013289, 0001558370-23-014509, 0001558370-24-011099,
0001558370-25-010780, 0001104659-26-092044.

**What the balance sheets say.**
- *Equity is flat while retained earnings rose $1.26 billion.* The difference went out in buybacks: $1,633M repurchased
  FY2017 to FY2026 (cash-flow statements, the sum of the ten years' "repurchases of common stock" lines), and the cover
  share count fell from 62.35M to 34.04M. Treasury stock at cost is $2,288M at 2026-06-30.
- *Tangible equity is negative.* Goodwill $961.3M plus intangibles $754.3M is $1,715.6M against equity of $1,446.2M.
  Of the intangibles, **$611.1M is "Title IV eligibility and accreditations"** and $141.8M is trade names (Note 12): the
  largest single asset the company has paid for is the government's permission to take federal student aid. Walden's
  goodwill is $651.1M of the $961.3M.
- *Debt arrived with Walden.* Long-term debt went from $125M (2017) to $1,068M (2021, the Walden financing raised before
  the August 2021 close), and has been paid down to $657.8M plus $5.1M current; the $163.0M revolver drawn at year-end
  was repaid on 2026-07-01 (MD&A, Material Cash Requirements), leaving a $510.0M term loan due 2033. Net of the $406.3M
  cash (after the revolver repayment, $243.3M), net debt is about $267M. Leases add $242.6M of lease liabilities (Note 11).
- *Receivables run ahead of revenue, and so do the write-offs.* Net receivables rose from $79.0M (2022) to $166.9M
  (2026), 2.1 times, while revenue rose 1.41 times ($1,381.8M restated to $1,954.1M). Gross current accounts receivable
  are $225.9M against an allowance of $59.0M, a quarter of the gross (Note 9). The provision for credit losses on the
  filed cash-flow statement was $53.2M, $63.2M and $68.8M in FY2024 to FY2026 (10-K FY2026); the XBRL tag
  `ProvisionForDoubtfulAccounts` gives $6.3M for FY2021 (before Walden) and $23.8M for FY2022.
  The company also lends to its own students ("credit extension programs", gross $34.0M, interest 3.0% to 12.0%, Note 9).
- *Deferred revenue grows* ($149.8M in 2022 to $259.1M in 2026): students pay ahead of the term, a working-capital
  source that rises with enrollment and would reverse if enrollment fell.
- *What the figures cannot say:* whether the $611.1M of Title IV permission keeps its value; every one of the five
  institutions is on a provisional Program Participation Agreement because the consolidated composite score fell to 0.2
  for FY2022 (Item 1, Financial Responsibility), and the company keeps $202.6M of surety-backed letters of credit for ED.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety as an attitude: if the decision needs pencil and paper,
"it’s too close to think about" **[M1996-084]**. The second is the habit of looking for "what’s wrong in things because
that’s part of investing" **[M2025-013]**, because the reported record of the last three years is very good: revenue up
$503M since FY2023, adjusted EPS up 23.7% in FY2026, twelve straight quarters of enrollment growth (Exhibit 99.1, 8-K
2026-08-06). The test of a share as a business, "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, turns on whether the federal lending terms of 2031 can be guessed, which is the Q1 question.
**Contrary evidence, written down as found** **[M1997-127]**:
1. Item 1: about 78% of FY2025 cash revenue came from federal student aid (consolidated 90/10 rate 78%; Walden 82%, AUC
   86%, RUSM 86%, RUSVM 77%, Chamberlain 70%).
2. Item 1: ED rated the FY2022 composite score at 0.2 (1.5 is "financially responsible"); all five institutions are on
   provisional certification; RUSM's agreement expired 2025-03-31 and runs on a pending application.
3. Item 1A: from 2026-07-01 the One Big Beautiful Bill Act (OBBBA) eliminates Grad PLUS for new borrowers, imposes
   annual, aggregate and lifetime loan limits and limits aid for part-time students. The filer: "We cannot predict the
   extent to which reduced federal loan availability may influence prospective student demand."
4. Item 1: "Do No Harm" earnings tests take effect 2027-07-01: a graduate program loses Title IV if its completers earn
   no more than holders of a bachelor's degree, two years in three.
5. Note 18: 16,623 borrower-defense claims received (AUC 390, Chamberlain 3,224, RUSM 1,958, RUSVM 2,020, Walden 9,031);
   none approved or recouped yet.
6. FY2025 Note 18: Walden paid $28.5M in November 2024 to settle a class action alleging it understated the capstone
   credits needed for its DBA degree; the FY2023 10-K records DeVry-era settlements of $44.95M (McCormick) and $19.9M
   (Stoltmann) over graduate employment statistics, and the FY2019 10-K a $49.4M FTC payment (FY2017).
7. Medical and veterinary enrollment fell from 6,546 (September 2015, FY2017 10-K) to 5,297 (September 2025, FY2026 10-K).
8. FY2026 operating cash flow was flattered by taxes: $68.4M of deferred tax (OBBBA accelerated deductions) against
   $13.6M of cash taxes paid on a $77.7M provision (cash-flow statement and supplemental lines).
9. The FY2026 results release is headed "Exceeds Financial Guidance" and leads with adjusted EPS and adjusted EBITDA;
   "strategic advisory costs" were excluded from adjusted results two years running ($12.0M, $18.6M) and restructuring
   in each of the last four years (Note 19 reconciliations, FY2025 and FY2026).
10. The strongest case on the other side, stated as its holder would state it **[M2016-055]**: Chamberlain has the
    largest pre-licensure nursing program in the United States (AACN data cited in Item 1) in a market where
    "capacity limitations and restricted new student enrollment are common" at traditional schools; the nursing shortage
    is durable; the cohort default rates are 0.0% for every institution (Item 1); the company has cut debt, bought back
    45% of its shares in ten years, and grown aggregate owner cash every year since FY2022.

## THE STANDING RULE
Owning a share bought for cash, unlevered and sized so a halving does not force a sale, puts the buyer at no risk of
ruin: "Never risk permanent loss of capital." **[L2023-005]**; "borrowed money has no place in the investor's tool kit"
**[L2014-005]**. Nothing in the target changes the buyer's own conduct. Satisfied, on that conduct.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The question: "can I understand it? And unless it’s going to be in a business that I think I can understand, there’s no
sense looking at it." **[M1995-051]**; understanding means "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**.

**What the business is.** It sells degrees in nursing, medicine, veterinary medicine and graduate social, health and
education fields, to about 100,000 students (Item 1). FY2026 revenue $1,954.1M: Chamberlain $750.2M (adjusted operating
margin 19.1%), Walden $804.9M (29.8%), Medical and Veterinary $398.9M (20.0%) (MD&A and Note 19). The product is easy to
understand. The question the rows ask is not the product but the earning power ten years out **[M2012-065]**.

**The key variables and how predictable each is** **[M1998-044]** ("If something is not very predictable, forget it.").
1. *Demand for the degrees.* Predictable in direction for nursing: a shortage of nurses and capacity-limited traditional
   programs (Item 1). Less so elsewhere: Chamberlain's post-licensure enrollment "has declined" in FY2026 (MD&A);
   Caribbean medical enrollment has fallen about a fifth in ten years (contrary item 7) as U.S. capacity expanded (Item 1:
   "recent expansion in the U.S. medical education and veterinary education enrollment capacities").
2. *Who pays, and on what terms.* About 78% of cash revenue is federal aid (contrary item 1). The price the company can
   charge is bounded by what the federal lender will lend each student, and those bounds were cut on 2026-07-01 for new
   graduate and professional borrowers (contrary item 3). This variable is set by Congress and the Department of
   Education, not by the market or the company.
3. *Permission to take the federal money at all.* Provisional certification for all five schools, a 0.2 composite score,
   letters of credit that ED may raise "regardless of the merits" (Item 1A), a cross-default under which "an enforcement
   action against one of our institutions could also have a material adverse effect on" the others (Item 1), and an
   earnings test from 2027 (contrary item 4). The balance sheet prices this permission at $611.1M (Step 0).
4. *The accountability rules themselves.* Within the four years the FY2026 10-K describes, the rules were rewritten four
   times: borrower-defense rules of 2022 scheduled for 2023, then delayed by statute to 2035; Gainful Employment and
   Financial Value Transparency rules of October 2023 effective July 2024; OBBBA in July 2025; "Do No Harm" regulations
   published 2026-07-01 that "substantially revise the FVT/GE framework" (Item 1). Each changed what the business may
   charge, lend against or sell.

**The tests as the draft states them.**
- *Where will it be in ten years?* "You’re trying to print the next 10 years of Value Line in your head. And there’s some
  companies that you can do a reasonable job with, and there’s others that are just too tough." **[M1999-132]**. Here
  variables 2 to 4 decide the ten-year earning power, and they are political.
- *Do the past statements tell me the future ones?* **[M2008-033]**. The ten-year record is of a different company each
  few years: DeVry University (the namesake, sold in 2018 after the FTC and state settlements of contrary item 6), Brazil
  and the financial-services group sold, Walden bought with debt in 2021. The FY2016 statements say little about the
  FY2026 ones, and the current five-school company has five fiscal years of history, the first of them a partial year.
- *Is it important and knowable?* **[M2006-076]**: "If something’s important but unknowable, forget it." The terms of
  federal student finance for proprietary schools over the next ten years are important (78% of revenue) and, on the
  filer's own words, not knowable: "Covista cannot predict what additional changes, if any, the U.S. Congress may
  ultimately make"; "We cannot predict the extent to which reduced federal loan availability may influence prospective
  student demand"; "These factors outside our control limit our ability to assess our future enrollment effectively."
  (Item 1A.)
- *Would the insiders write it down?* **[M2000-105]**: "They would say, “That’s too hard.”" The insiders here are the
  filer, and the sentences above are their answer. They write down one year (FY2027 guidance: revenue $2,050M to
  $2,090M, Exhibit 99.1); they decline in the 10-K to write down what the new loan limits will do to demand.
- *How far off could I be?* **[M2011-084]**. Far. The company has already lived the far case once: DeVry University,
  after the FTC and class settlements, was sold in 2018 with the seller still indemnifying the buyer for up to $340.0M
  (Note 18). One school's enforcement action can reach the others' Title IV eligibility (Item 1).
- *Do I doubt it is inside?* **[M2002-092]**: "if you have doubts about something being into your circle of
  competence, it isn’t."

**The rows on the political variable.** Buffett, of a business that "historically earned good returns", declined to
judge it because "much of it is in the political realm. And my judgment about [...] what politicians will do is probably
not better than yours." **[M2005-098]**. Of currencies: "a bet on how government now, and in the future, will behave"
**[M2011-025]**. Of his own regulated utilities: "it is difficult to project both earnings and asset values in what was
once regarded as among the most stable industries in America. [...] I did not anticipate or even consider the adverse
developments in regulatory returns" **[L2023-011]**.

**The strongest case against this reading**, stated as well as its holder would state it **[M2016-055]**. Its row
of 2012: "railroads, utilities, insurance companies, are all very
much affected by the political process. Fortunately, I think, in the railroad industry, you know, we’ve got economics on
our side. And economics usually win out." **[M2012-074]**. Chamberlain has economics on its side (the nursing shortage,
the largest pre-licensure program, constrained public capacity). The answer, which is the analyst's reading and not a
row: at a railroad the customer pays the freight; here the main payer is the same political process that writes the
rules, so the economics cannot win out around the politics, they run through it. And Chamberlain is 38% of revenue;
Walden (82% federal) and the Caribbean schools (86% at AUC and RUSM) are the rest; the analyst's reading, not a filing
statement, is that the medical schools, with the longest and dearest programs, are the most exposed to the new
professional loan limits, and the filer gives no figure for how many of its students borrow above them. A holding company is understood by its parts, and a part that matters and cannot be understood keeps
the whole outside **[M2002-092]** (the by-parts reading is the framework's CONVENTION, Q1, "A holding company").

**Which cause** (section I). Not WORK. Part of the near-term question is knowable with work and time: FY2027 enrollment
will show what the July 2026 loan limits do. But the deciding question is the ten-year one, the terms on which a
future Congress and Department of Education will finance and police proprietary schools, and the filer itself will not
write that forecast down **[M2000-105]**. "We couldn't solve this problem, moreover, even if we were to spend years
intensely studying those industries." **[L1993-023]**; "we’re not going to learn enough in the followings five months
to make up for the fact that we went in deficient in the first place." **[M2008-086]**. A lower price does not reopen it:
"It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that
we don’t know how to evaluate it." **[M2000-038]**. And the circle is not widened to find something: "we will not
enlarge the circle. You know, we’ll wait." **[M1995-018]**.

**VERDICT: TOO HARD (NATURE).** The ten-year earning power depends on a forecast of federal student-aid policy toward
proprietary institutions, which carries about 78% of cash revenue, which was rewritten four times in four years, and
which the filer states it cannot predict **[M2006-076]**, **[M2000-105]**, **[M2005-098]**. "a lot of things end up in
the “too hard” pile, and it doesn’t bother us." **[M2006-013]**. The file closes here.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED. The competitor figures gathered for it are in the computation annex below; they are not a clearance.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0. Recorded for any later reading, not judged: the results release
features adjusted EPS and adjusted EBITDA and is headed "Exceeds Financial Guidance" (contrary item 9); receivables and
credit losses outgrow revenue (Step 0). Whether these are one tell or two under Q4's make-the-numbers line was not
decided, because Q4 was not reached.

## Q5: WHO RUNS IT? STOP on integrity.
NOT REACHED. Facts gathered, not judged: Stephen W. Beard has been CEO since 2021 and is also Chairman (proxy); he owns
477,464 shares counting units vesting within 60 days, 1.41%; directors and officers together 2.70% (proxy, ownership
table). Lisa W. Wardell remains a director (proxy); she was a director from 2008, chaired the audit and finance
committee, and was CEO from May 2016 (10-K FY2017 and FY2019, executive officers), the years of the FTC payment and the
DeVry employment-statistics settlements. The FY2026 bonus paid at 145% of
target for the CEO; the PSUs pay on revenue growth and adjusted EBITDA margin, and the FY2024 to FY2026 revenue PSUs
paid at 200% (proxy, CD&A).

## Q6 to Q10, Q12
NOT REACHED.

---
## COMPUTATION - NOT A CLEARANCE
*Everything in this section is arithmetic made after the file closed at Q1. It carries no entry language and clears
nothing (operator rule 3). It is reported at the owner's request, which is not a rule change.*

**Owner cash after every real cost** (USD millions; continuing-operations OCF less stock pay less all capital spending,
from the filed cash-flow statements; never a net-income proxy, operator rule 5):

| FY (June) | OCF, continuing | stock pay | capex | owner cash (A) | deferred tax in OCF | A, tax at provision (B) | depreciation | A with depreciation for capex (D) |
|---|---|---|---|---|---|---|---|---|
| 2022 | 163.8 | 22.6 | 31.1 | 110.1 | -13.7 | 123.8 | 44.6 | 96.6 |
| 2023 | 205.7 | 14.3 | 37.0 | 154.4 | -4.9 | 159.3 | 41.6 | 149.8 |
| 2024 | 288.4 | 25.9 | 48.9 | 213.6 | 11.1 | 202.5 | 39.7 | 222.8 |
| 2025 | 333.7 | 41.6 | 50.3 | 241.8 | 18.4 | 223.4 | 40.7 | 251.4 |
| 2026 | 470.8 | 41.2 | 77.7 | 351.9 | 68.4 | 283.5 | 43.9 | 385.7 |
| five-year mean | | | | **214.4** | | **198.5** | | **221.3** |
| four-year mean, FY2022 left out | | | | 240.4 | | 217.2 | | 252.4 |

Sources: FY2024 to FY2026 from the FY2026 10-K (0001104659-26-092044); FY2022 and FY2023 continuing-operations OCF as
restated in the FY2024 and FY2025 filings (0001558370-24-011099, 0001558370-25-010780). Cloud-computing implementation
payments ($27.2M, $32.8M, $14.0M in FY2024 to FY2026) sit inside OCF and are therefore already deducted. Interest is
inside OCF, so these figures are owner cash to equity. Variant B charges tax at the book provision, removing the FY2026
OBBBA timing benefit (contrary item 8). FY2022 is an abnormal year (Walden owned from 2021-08-12 only, $129.3M of
interest, integration costs), so the four-year mean is shown beside it **[L2005-003]**.

**The value range (the Q7 CONVENTION construction, as a computation).** Five-year mean owner cash (A) $214.4M; growth
shown on aggregate owner cash 33.7% a year FY2022 to FY2026 and 31.6% FY2023 to FY2026, both from depressed base years
and above the 5.66% discount rate, so the shown-growth end is capped at the discount rate (the convention's cap; the cap
at exactly 5.66% is a CONVENTION of this run: the convention says "capped", gives no lower figure, and the shown rate
cannot be carried). Ten years, then zero nominal growth, discounted at 5.66%.

| base | no-growth end | capped-growth end | top over bottom |
|---|---|---|---|
| A, five-year, $214.4M | $3,787M, **$111.26 a share** | $5,931M, **$174.24 a share** | 1.57 |
| A, four-year (FY2022 left out), $240.4M | $4,248M, $124.79 | $6,652M, $195.43 | 1.57 |
| B, five-year, tax at provision, $198.5M | $3,507M, $103.03 | $5,492M, $161.35 | 1.57 |

Against the price of $125.39: inside the five-year range, near its bottom; at the bottom of the whole-cycle (four-year)
variant. The range is narrower than three to one, so if Q1 to Q6 had passed, Q7 would have closed OUT (price inside the
range, not a screamer) **[M2009-005]**, not TOO HARD. The arithmetic says nothing about the political variable that
closed Q1, and the next five years may not resemble FY2022 to FY2026, the first years under the July 2026 loan limits.

**FAIR PRICE: about $99 a share** ($3,355M). Rule: the price at which the central case returns 10% a year pre-tax.
Central case: five-year mean owner cash A, grossed up for tax at the FY2026 effective rate of 22.5% (MD&A) to $276.6M
pre-tax, growing at half the capped rate (2.83%) for ten years then flat, discounted at 10%. The floor is applied on
equity: owner cash is after interest, so net debt (about $267M after the July revolver repayment) is not added again.
On variant B the fair price is about $91; on the four-year variant about $111. At $125.39 the central case's pre-tax
expected return is about 8.0%, below the floor's about 10% (CONVENTION, Q7, **[M2003-149]**); even the capped-growth
case gives about 9.6%.

**CHEAP PRICE: about $50 a share** ($1,708M). Rule, a CONVENTION of this run: the price at which the no-growth case on
the lowest defensible base (variant B, five-year, $198.5M after tax, $256.1M pre-tax) yields 15% pre-tax, half again the
floor, so that the margin would "scream" without the political variable being guessed **[M1996-084]**. Below it no
pencil is needed on the cash; the file would still be TOO HARD at Q1, because a lower price does not reopen a
NATURE closure **[M2000-038]**.

**Competitor comparison, gathered for Q2, not judged** (USD millions, each company's own 10-K XBRL, latest-filed value per
year; operating margin = operating income over revenue). Chosen as the closest listed rivals, each named from its own
latest 10-K: American Public Education (segments Rasmussen University and Hondros College of Nursing, nursing schools
against Chamberlain; 0001201792-26-000004), Strategic Education (Capella University and Strayer University, online
graduate and adult degrees against Walden; 0001013934-26-000006), Grand Canyon Education ("a publicly traded education
services company" serving Grand Canyon University, a non-profit, with healthcare programs at off-campus sites; its
margin is a services margin, not a school's; 0001104659-26-017047), Perdoceo (Colorado Technical University, the AIU
System and the University of St. Augustine for Health Sciences; 0001193125-26-059331). No listed company found owns a
Caribbean medical school.

| fiscal year | CVSA op. margin | LOPE | STRA | APEI | PRDO |
|---|---|---|---|---|---|
| 2016 | n/a (restated segments) | 27.2% | 13.0% | 12.2% | -4.6% |
| 2017 | n/a | 29.0% | 11.5% | 11.6% | 5.7% |
| 2018 | n/a | 30.5% | -3.6% | 10.9% | 12.3% |
| 2019 | 15.4% | 34.1% | 11.1% | 4.5% | 13.8% |
| 2020 | 12.7% | 32.9% | 10.6% | 7.7% | 20.8% |
| 2021 | 12.3% | 31.5% | 6.5% | 7.3% | 21.5% |
| 2022 | 5.6% | 26.1% | 6.6% | -22.7% | 18.6% |
| 2023 | 11.6% | 25.9% | 8.4% | -8.0% | 21.2% |
| 2024 | 13.7% | 26.7% | 12.8% | 5.3% | 25.6% |
| 2025 | 19.1% | 24.0% | 13.7% | 7.4% | 23.2% |
| 2026 | 19.6% | | | | |

CVSA years end June 30; the others December 31. Accessions of the latest-filed values: LOPE 0001104659-26-017047
(2023 to 2025) and earlier 10-Ks; STRA 0001013934-26-000006; APEI 0001201792-26-000004; PRDO 0001193125-26-059331. CVSA
values are as restated for continuing operations in each later 10-K. Owner cash as a share of revenue over the
comparable recent years: CVSA 13.9% (FY2024), 13.8% (FY2025), 18.0% (FY2026); LOPE 19.3% to 23.1% (2023 to 2025); STRA
5.3% to 10.3%; APEI 3.2% to 5.8%; PRDO not computed (its capital-spending tag is absent from its XBRL after 2016). What
the span shows, without a verdict: every listed peer has had at least one year of collapse or loss in the decade (STRA
2018, APEI 2022 and 2023, PRDO 2015 and 2016), and CVSA's own margin halved in FY2022; the industry's margins move with
regulation and acquisitions more than with any one company's steady advantage. CVSA's present margin is at the top of
its own decade and below LOPE's in every year.

---
## THE BOX
**TOO HARD (NATURE)** at **Q1**. The ten-year earning power turns on federal student-aid policy for proprietary schools
(about 78% of cash revenue; all five schools provisionally certified; new loan limits from 2026-07-01 and an earnings
test from 2027-07-01), a forecast the filer says it cannot make **[M2000-105]**, **[M2005-098]**. No research pass is
opened (NATURE is the closed box). Computation only, not a clearance: value range $111 to $174 a share (whole-cycle
variant $125 to $195) against $125.39; fair price about $99; cheap price about $50.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before the first EDGAR call); written question
      by question. **Not committed after each question**: the instruction for this run forbids commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, and every quoted fragment beside an id
      found in that row); every filing fact has its accession; no v4 id is cited.
- [x] The order was kept; Q1 closed the run; everything after it is NOT REACHED or headed COMPUTATION - NOT A CLEARANCE.
- [x] Owner cash after every real cost from the cash-flow statement, never a net-income proxy (operator rule 5); the
      sovereign from the Treasury; the aggregator quote flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (ten items in the foundations).
- [x] No row dated after the anchor is cited in a point-in-time run (not a point-in-time run; today's date is the anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII), and two of them were corrected against the filing.
- [x] `python tools/check_framework.py` PASS, 2026-10-06, after the last edit; a separate script
      (`_research 2026-10-06 CVSA/check_ids.py`) found no E-id, all 29 v5 ids in the ledger, and every quoted fragment
      beside an id inside that row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **Q1's routing names fast technology as the cause that closes the file at Q1, and says nothing of
government as the cause.** Here the unforeseeable variable is political, and the rows that fit it best (M2005-098,
M2011-025, L2023-011, against M2012-074) sit nowhere in Q1's text; Q2's "a regulated moat that broke" names utilities as
a mistake but not as a routing. I routed it through Q1's tests 4 and 5 (important and knowable; would the insiders write
it down), which fit, but a second analyst could pass Q1 on the nursing demand and close at Q2 TOO HARD instead. Q1 would
be clearer with one sentence saying whether a business whose main payer is the rule-maker is judged at Q1 or Q2.
(2) **The insider test has no rule for one-year guidance.** The filer writes a twelve-month forecast and refuses a
longer one in the same filing season; I read the refusal as the answer to test 5, but the framework does not say how
far out "would write it down" reaches. (3) **The Q7 growth cap.** The convention says the shown growth is "capped by
the growth arithmetic of Q3: no rate that runs past the discount rate", but gives no rule when the shown rate is far
above the discount rate because the base year is depressed; I capped at the discount rate exactly and confessed it as a
CONVENTION of this run. A ten-year carry at a rate above the discount rate is finite, so "runs past" is ambiguous for
the ten-year leg. (4) **A rename and a portfolio that changed three times** make "the ten-year record" and "the
five-year average" refer to different companies; the framework has no line on how many years of the present company are
needed before Q7's five-year mean is meaningful. I used continuing operations and showed the four-year variant beside
the five-year one.
