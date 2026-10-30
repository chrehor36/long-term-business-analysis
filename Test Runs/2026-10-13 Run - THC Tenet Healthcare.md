# Company Run — Tenet Healthcare Corporation (NYSE: THC) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
e604df1a).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold, 2026-10-13, by the dispatching session after the run was committed: not held (`PORTFOLIO.md` carries no line for THC or Tenet).*

**Dispatched run.** Written by a dispatched analyst under the canonical brief (`Screens/_daily/_dispatch_brief.md`) with
the brief's one stated departure: the lines of evidence were derived by the analyst from the 10-K (listed below), not
listed by the dispatcher.

**Contamination, declared and not used.** (1) The session's opening git status showed recent commit subjects for a CYH
run (Community Health Systems, a rival named in this file's competitor row): "Fold CYH v5 re-run ... TOO HARD (NATURE) at
Q1" and "CYH run: Q1 TOO HARD (NATURE), the box". I did not open that run file or its research folder. Because the subject
line names a box for a hospital company, it is an anchor for this run: I wrote the Q1 case for IN first (below) and decided
on Tenet's own filings; the reader should still weigh the risk that the anchor leaked. (2) A directory listing of
`Test Runs/` filtered for "THC|tenet" matched "healthcare" in other file names and showed five names: an HCA run of
2026-07-15, an ACHC run of 2026-10-13, an AMN run and a PBH run of 2026-10-05, a GEHC run of 2026-07-15. None was opened;
no file about Tenet under any name was listed. (3) The git status also listed research folders of AYI and ARCB, and the
memory index carries a queue-state line; neither bears on Tenet. Nothing of these is used.

**Lines of evidence, derived from the 10-K for 2025 (the brief's departure).** From Item 1: the two segments and their
parts (50 hospitals, Conifer, USPI's 533 ASCs and 26 surgical hospitals); competition (the 10-K names no rival company,
only kinds of rival); healthcare policy (the Affordable Care Act, the OBBBA of July 2025); the anti-fraud laws and the
company's record under them. From Item 1A: managed-care contracts and payer concentration; government programs and
Medicaid supplemental payments; physicians and labor; joint ventures and their partners; the debt. From Item 7: payer mix,
DSH and supplemental revenue, segment Adjusted EBITDA, noncontrolling interests by segment, the 2024 divestitures, the CHI
agreement on Conifer, cash flow and capital spending. These are the lines read below.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $269.14 (2026-10-13, aggregator quote via `tools/run.py`; aggregator, live quote only, flagged per operator
  rule 5). For scale only: the company's own repurchases in 2026 were at average prices of $236.30 (March), $190.26 (May)
  and $167.20 (June) (10-Q for Q2 2026, accession 0000070318-26-000037).
- **Shares by class** from the latest filing's cover: 80,519,000 common, one class (10-Q for the quarter ended 2026-06-30,
  filed 2026-07-29, accession 0000070318-26-000037, cover as of 2026-07-24; `python Screens/cover_shares.py THC`).
  **Check:** the 10-Q balance sheet shows 159,187 thousand issued less 78,680 thousand in treasury = 80,507 thousand at
  2026-06-30, against 80,519 thousand on the cover three weeks later (share-plan issuance; no repurchase is reported in that
  gap). The 8-Ks since (2026-09-08, accession 0000070318-26-000040; 2026-09-22, accession 0001193125-26-397901) are a note
  offering and its indenture and state no share issuance or buyback.
- **Market cap:** 80.519M × $269.14 = **$21,671M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for 2025 (filed 2026-02-17, accession 0000070318-26-000012), Items 1, 1A, 7,
  the cash-flow statement, the segment note and the subsequent-event note; 10-Ks for 2022 (0000070318-23-000010), 2023
  (0000070318-24-000016) and 2024 (0000070318-25-000009) for the 2021 and 2022 cash flows, the segment tables and the
  COVID repayments; the 10-K for 2020 (0000070318-21-000008) for the 2018 to 2020 segment table; the 10-Q for Q2 2026
  (0000070318-26-000037); the proxy of 2026-04-16 (DEF 14A, accession 0001193125-26-159118), summary compensation table and
  incentive design; the 8-Ks of 2026-09-08 and 2026-09-22 (the $2.0 billion of 6.250% notes due 2034, proceeds and cash
  on hand to redeem all $1.5 billion of 5.125% first-lien notes due 2027 and $0.5 billion of the 6.125% notes due 2028, so
  net debt is unchanged by them apart from costs).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025, $3,540M in
  `tools/run.py` (XBRL) = $3,540M on the filed consolidated statement of cash flows (10-K, accession 0000070318-26-000012).
  Agrees.
- `python tools/run.py THC`, arithmetic lines only (`Test Runs/_research 2026-10-13 THC/runpy_THC.txt`): operating cash
  2023 to 2025 $2,374M, $2,047M, $3,540M; stock pay $66M, $67M, $104M; capital spending $751M, $931M, $1,010M; D&A $870M,
  $818M, $863M. The tool lists beside them, unchosen, distributions to minority partners ($594M, $681M, $809M) and
  finance-lease principal ($107M, $87M, $62M). Both are real cash out of the common owner's reach and are taken into owner
  cash in the COMPUTATION below; the tool's own three-year "owner earnings" line leaves them out and is not used.

### The balance sheets, eight to ten years, read in Step 0 because the file closes before Q4 **[M2025-032]**
Ten year-ends 2016 to 2025 from `tools/run.py` (first-filed XBRL, transcription) and the noncontrolling-interest lines from
the same filings, USD millions; the 2025 and mid-2026 figures checked against the filed balance sheets (10-K 0000070318-26-000012;
10-Q 0000070318-26-000037).

| year-end | total assets | shareholders' equity | goodwill | other intangibles | cash | receivables | debt (incl. finance leases) | retained earnings | redeemable NCI | other NCI |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 24,701 | 417 | 7,425 | 1,845 | 716 | 2,897 | 15,255 | -1,742 | 2,393 | 665 |
| 2017 | 23,385 | -147 | 7,018 | 1,766 | 611 | 2,616 | 14,937 | -2,390 | 1,866 | 686 |
| 2018 | 22,409 | -119 | 7,281 | 1,731 | 411 | 2,595 | 14,826 | -2,236 | 1,420 | 806 |
| 2019 | 23,351 | -371 | 7,252 | 1,602 | 262 | 2,743 | 14,751 | -2,467 | 1,506 | 854 |
| 2020 | 27,106 | 28 | 8,808 | 1,600 | 2,446 | 2,690 | 15,719 | -2,128 | 1,952 | 909 |
| 2021 | 27,579 | 1,028 | 9,261 | 1,497 | 2,364 | 2,770 | 15,646 | -1,214 | 2,203 | 1,026 |
| 2022 | 27,156 | 1,142 | 10,123 | 1,424 | 858 | 2,943 | 15,079 | -803 | 2,149 | 1,317 |
| 2023 | 28,312 | 1,608 | 10,307 | 1,368 | 1,228 | 2,914 | 15,002 | -192 | 2,391 | 1,509 |
| 2024 | 28,936 | 4,171 | 10,691 | 1,397 | 3,019 | 2,536 | 13,173 | 3,008 | 2,727 | 1,649 |
| 2025 | 29,677 | 4,220 | 11,198 | 1,348 | 2,883 | 2,565 | 13,171 | 4,415 | 2,956 | 1,797 |
| 2026-06-30 | 30,676 | 4,658 | 11,437 | 1,281 | 2,170 | 2,608 | 13,248 | 5,943 | 2,143 | 1,899 |

What the figures say. (1) **The common owner's book is goodwill and more.** Shareholders' equity was below zero from 2017
to 2019 and is $4,220M at 2025 against goodwill of $11,198M and other intangibles of $1,348M: tangible common equity is
about -$8.3 billion. Goodwill rose from $7.4 billion to $11.2 billion over the decade, almost all of it USPI's purchases.
(2) **Debt did not fall for eight years** (about $15 billion 2016 to 2023) and fell to $13.2 billion only when fourteen
hospitals were sold in 2024 for $4,981M of proceeds (10-K 2025, cash-flow statement); it has stayed there since while
cash was spent on repurchases ($1,386M in 2025; $1,360M in the first half of 2026). (3) **Receivables are not building**:
$2,897M on revenue of $21,070M in 2016, $2,565M on $21,310M in 2025, a falling share of sales; inventories steady near
$300M to $400M. No tell of the kind **[M2025-032]** asks for was found in the working-capital lines. (4) **The minority
partners' claims grew while the common's was near zero**: redeemable and other noncontrolling interests together were
$3,058M in 2016 and $4,753M in 2025 (the CHI redemption of January 2026 cut the redeemable line by $846M). (5) **Retained
earnings** turned positive only in 2024, on the $2,916M pre-tax gain from the hospital sales (10-K 2025, segment note
reconciliation). What they cannot say: what the goodwill's ASCs will earn, and what government programs will pay the
hospitals; those are the questions below.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the first: a share is a business, bought for the cash the business will produce and
judged as if "the market closed for five years" **[M1997-109]**, which here means judging what a hospital company earns
when its prices are partly set in Washington and in eight state capitals. The no-macro foundation is noted so that it is
not misapplied: the federal payment and coverage question below is not a forecast of the economy but the key variable of
this business, which the company's own filings name. The analyst's habits govern the order of work: the worst anchor "is
always your previous conclusion" **[M2016-054]** (and contamination item (1) above is such an anchor), and the run looks
for "what’s wrong in things" **[M2025-013]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) owner cash to the common, after capital spending and
distributions to minority partners, was about nothing for the four years before COVID: 2016 -$603M, 2017 $176M, 2018 $98M,
2019 $63M (XBRL of the filed 10-Ks; 2016 to 2018 before finance-lease principal, which is not tagged for those years);
(b) DSH and other Medicaid supplemental revenue was $1,338M in 2025, $1,161M in 2024 and $929M in 2023 (10-K 2025, Item 7),
against Hospital Operations' segment profit after depreciation of $1,829M in 2025, and the OBBBA caps state-directed
payments and provider taxes from 2027; (c) the company says, in the 10-K and again in the July 2026 10-Q, "At this time,
we cannot estimate the OBBBA’s impact, nor can we predict the timing of that impact"; (d) minority partners took 26.8% of
earnings before interest and tax over 2016 to 2025 (computation below); (e) tangible common equity is negative; (f) "We
have paid significant amounts to resolve government investigations and qui tam matters brought against us in the past"
(10-K 2025, Item 1). Evidence the other way, written down as found: receivables falling against sales; debt down $2
billion since 2023; owner cash rising 2023 to 2025; USPI's revenue up from $2,072M (2020) to $5,172M (2025).

## THE STANDING RULE
The rule binds the buyer's conduct, not Tenet's: a purchase of this common would be paid in cash, since "borrowed money
has no place in the investor's tool kit" **[L2014-005]**, and sized so that its total loss is survivable: "never going to
risk what we have and need for what we don’t have and don’t need" **[M2012-081]**.
Nothing in this name forces a breach of it; Tenet's own debt is the target's and is weighed at Q9, which this run does not
reach.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
The test: "can I understand it?" **[M1995-051]**, where understanding means "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" **[M2012-065]**, "where the business will be in 10
years" **[M2000-037]**.

**Which part must be understood.** Q1's holding-company paragraph, extended to operating segments (section B of the gaps
case), asks that each part that matters be understood, a part mattering when it carries more than half of five-year
operating profit or else is the largest. The filer reports no segment operating income; its segment measure is Adjusted
EBITDA, and it reports segment depreciation. **CONVENTION of this run:** segment operating profit is the filer's segment
Adjusted EBITDA less the segment's depreciation and amortization; rationale: it is the nearest filed figure to operating
profit, and it charges depreciation, which the rows call a real cost **[R1996-023]**. Conifer was its own segment until
2022 and is now inside Hospital Operations; it is counted there, as the filer now reports it.

| year | Hospital Operations (incl. Conifer) | Ambulatory Care (USPI) | source |
|---|---|---|---|
| 2021 | 1,931-722 + 355-38 = 1,526 | 1,197-95 = 1,102 | 10-K 2022 segment note (0000070318-23-000010) |
| 2022 | 1,777-692 + 365-37 = 1,413 | 1,327-112 = 1,215 | same |
| 2023 | 1,997-750 = 1,247 | 1,544-120 = 1,424 | 10-K 2025 segment note (0000070318-26-000012) |
| 2024 | 2,185-684 = 1,501 | 1,810-134 = 1,676 | same |
| 2025 | 2,540-711 = 1,829 | 2,026-152 = 1,874 | same |
| **five-year total** | **7,516 (50.8%)** | **7,291 (49.2%)** | |

Hospital Operations carries just over half and **decides**. The margin is thin, so the owner's view is shown beside it:
net income to noncontrolling interests in 2025 was $155M in Hospital Operations and $805M in Ambulatory Care (10-K 2025,
Item 7), so of the 2025 segment profits the common owner's share is roughly $1,674M from the hospitals and $1,069M from
USPI. On either reading the hospitals are the part that matters, and a part that matters and cannot be understood keeps the
whole outside: "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**.

**The key variables of the hospitals, and how predictable they are** **[M1998-044]**. From the 10-K for 2025:
1. **What government programs pay, and whom they cover.** Medicare 15.2% and Medicaid 10.9% of the hospitals' net
   patient revenue in 2025, before the Medicare and Medicaid managed-care plans inside the 69.5% "managed care" line
   (Item 7). Medicaid DSH and supplemental revenue: $929M (2023), $1,161M (2024), $1,338M (2025), the fastest-growing
   source named in each year's revenue explanation ("growth in Medicaid supplemental revenue", Item 7). The OBBBA of July
   2025 brings, "beginning in 2027", "caps on state-directed payments, limits on provider taxes, stricter eligibility
   checks" and work requirements; the enhanced marketplace tax credits expired at the end of 2025 (Item 1).
2. **What commercial payers pay.** 69.5% of hospital patient revenue is managed care; the top ten payers are 69% of it;
   "The ongoing trend toward consolidation among non‑government payers tends to increase their bargaining power"; denials
   are rising (Item 1A).
3. **What labor costs.** Nurse shortages, 20% of hospital employees unionized at 27 hospitals, California's mandated
   healthcare minimum wage rising "through 2028", California's nurse ratios (Items 1 and 1A).
4. **Where care is given.** "patient volumes are shifting from inpatient to outpatient settings" (Item 7); site-neutral
   payment is named as a risk (Item 1A).

**The tests, applied.**
- *Test 3, do the past statements tell me the future ones* **[M2008-033]**? They do not, on the filings' own record: owner
  cash to the common was about nothing from 2016 to 2019 (Foundations, contrary evidence (a)) and $1,235M in 2025, the
  change made by COVID grants and advances, the 2024 sale of fourteen hospitals, payer mix, and supplemental payments that
  rose $409M in two years. A history that moves that far on government programs and portfolio sales fails the test of
  whether "the financial statements will tell me the information" **[M2008-033]** needed for the next ten years.
- *Test 4, is it important and knowable* **[M2006-076]**? Important: supplemental revenue alone equals 73% of the
  hospitals' 2025 segment profit after depreciation ($1,338M against $1,829M; revenue against profit, so a scale, not a
  share of profit). Knowable: the company says not. "At this time, we cannot estimate the OBBBA’s impact, nor can we
  predict the timing of that impact, on our future business" (10-K 2025, Items 1, 1A and 7), repeated word for word in
  the 10-Q of July 2026 (0000070318-26-000037); and of the states' supplemental programs, "we are unable to assess the
  effect that any such legislation or regulatory action might have on our business" (10-K 2025, Item 1A). "If something’s
  important but unknowable, forget it." **[M2006-076]**
- *Test 5, would the insiders write it down* **[M2000-105]**? This is the test the filing answers directly: the people
  who run the business, with every state's program in front of them, decline in a filed document to estimate the effect of
  a law already enacted, eighteen months before its main provisions bite. They "would not want to put down on paper their
  predictions" **[M2000-105]** and they have said so.
- *Test 8, how far off could I be* **[M2011-084]**? The range of the hospitals' earning power runs from the 2016 to 2019
  level, when the whole company produced next to nothing for its common owner, to the 2025 level; the filings give no
  ground for placing the next ten years inside that range rather than below it.
- *Test 7, customers or technology* **[M2017-019]**, **[M2023-030]**? Neither: the forecast that decides is of legislators
  and state agencies, which is not "consumer behavior" **[M2023-030]** and not a technology. The rows give no separate
  test for it; the nearest narrated case is the speakers' own utility error, where a regulatory climate made it "difficult
  to project both earnings and asset values" **[L2023-011]**, and their view of the industry after trying to change it,
  "the political power that the industry will have" **[M2025-056]**, **[M2021-053]**. These are weighed as evidence of how
  the speakers read regulated economics, not as a verdict on hospitals (Q2's convention on rows about one case applies by
  analogy).

**The case for IN, written first because of the anchor declared above.** Hospitals are an old service, not a fast-moving
technology; acute, emergency and surgical care will be needed in ten years in the Sun Belt markets where most of the
licensed beds sit; 69.5% of hospital revenue is negotiated with private payers, not set by government; the company has run
through the Affordable Care Act, sequestration and COVID and is still standing; and the speakers record that they once
"tended to overestimate the difficulties from regulation" **[M2004-058]**. All of this is true and is why the demand side
can be pictured. It does not answer the deciding variable: the demand is foreseeable, the price the hospitals are paid for
a quarter of their revenue, and the supplemental layer that has carried the recent profit growth, are not, and the company
says so. The definition asks for a fix on "what the earning power and competitive position will look like in five or 10
years" **[M2012-065]**, not on the service.

**Cause.** The deciding question is a forecast the industry's own insiders would not write down **[M2000-105]**: the
company's statement is not that the work is undone but that the outcome depends on what "states will implement" and what
Congress and agencies "might further" do (Item 7; Item 1). No reading of further filings by this analyst cures that; it is
the case where "the nature of the industry would be the roadblock" **[L1993-023]**. The part of it that is knowable (the
statute's own phase-down schedule) is not the deciding part; the states' responses and later legislation are. So the cause
is NATURE, not WORK. A lower price does not reopen it: "It doesn’t mean it isn’t selling for a fraction of its worth"
**[M2000-038]**.

**VERDICT: TOO HARD (NATURE)** **[M2006-013]**, **[M2006-076]**, **[M2000-105]**, **[M2002-092]**; the filing fact: the
company "cannot estimate the OBBBA’s impact, nor can we predict the timing of that impact" (10-K 2025, accession
0000070318-26-000012; 10-Q Q2 2026, accession 0000070318-26-000037), on a payment layer of $1,338M against the deciding
segment's $1,829M profit. The file closes here.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (facts found are under AFTER THE STOP).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read in Step 0).
## Q5 — WHO RUNS IT? NOT REACHED (integrity facts recorded under AFTER THE STOP, not judged).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED (COMPUTATION, NOT A CLEARANCE under AFTER THE STOP).
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the deciding part (Hospital Operations, 50.8% of five-year segment profit) turns
on government payment and coverage over ten years, which the company states it cannot estimate; integrity facts recorded,
not judged. No range is set beside the price as a verdict; the COMPUTATION below puts the price ($269.14) above the top of
its computed range ($170.82 to $259.53 a share, all-equity), with no case earning the floor.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2); each with its source **[M1997-127]**.)*

### Bearing on Q2 (the castle)
- **The competitor row.** The 10-K names no rival company. It names rivals by kind only: "tax‑supported government
  agencies", "not‑for‑profit organizations", "large teaching hospitals", physician-owned facilities, and "system‑affiliated
  hospitals and healthcare companies, as well as health insurers and private equity companies" (10-K 2025, Items 1 and
  1A). None of these is a company that files with the SEC by name; most are not-for-profit or municipal and do not file.
  **CONVENTION of this run:** the three rivals are HCA Healthcare, Universal Health Services and Community Health Systems,
  the investor-owned acute-care hospital operators that file with the SEC; rationale: the deciding part is the hospitals,
  and these are the filers whose hospitals compete for the same patients, physicians and payer contracts. (UHS is about
  half behavioral health; an ambulatory rival such as Surgery Partners was not chosen because USPI does not decide.)
  Metric: earnings before interest and tax (pre-tax income plus interest expense) on revenue and on total assets, 2016 to
  2025, first-filed XBRL of each 10-K (transcription; HCA FY2025 10-K 0001193125-26-044769, UHS 0001193125-26-071676, CYH
  0001193125-26-059509, Tenet 0000070318-26-000012; earlier years from each year's own 10-K). Tenet's 2021 and 2024
  facility-sale gains ($445M, $2,916M) are taken out; the rivals' figures are as filed (CYH's 2016 to 2019 include large
  impairments).

| | EBIT/revenue, 2016 → 2025 (%) | mean | EBIT/total assets, mean | minority partners' share of EBIT, 10 yrs |
|---|---|---|---|---|
| Tenet | 5.8, 4.5, 9.0, 6.9, 9.5, 12.1, 11.6, 12.1, 15.3, 17.0 | 10.4 | 7.7% | 26.8% |
| HCA | 15.7, 13.9, 15.2, 13.8, 13.6, 19.4, 17.1, 14.8, 15.0, 16.0 | 15.5 | 18.1% | 8.7% |
| UHS | 13.1, 12.3, 11.0, 10.8, 11.7, 10.9, 7.4, 8.0, 10.6, 12.3 | 10.8 | 10.7% | 0.9% |
| CYH | -4.1, -12.4, 1.8, 4.6, 12.3, 11.2, 9.9, 8.3, 4.6, 12.8 | 4.9 | 4.1% | 21.3% |

  (`Test Runs/_research 2026-10-13 THC/comp.py`.) Over the whole span Tenet's return on total assets before tax and before
  its partners' share is about two fifths of HCA's, near UHS's, above CYH's; Tenet's margin converged on HCA's only in 2024
  and 2025, after the hospital sales and as USPI grew; and more than a quarter of Tenet's earnings before interest belong to
  its partners, three times HCA's share.
- **The field's returns over the cycle.** On these four filers, the hospital field earned mean pre-tax returns on total
  assets from about 4% to about 18% over 2016 to 2025, with one filer (HCA) well above the others in every year.
- **USPI, the non-deciding part.** Grew by acquisition and joint venture with physicians: 27 ASCs and one surgical hospital
  bought in 2025 alone (10-K 2025, Item 7); its partners took $805M of 2025 net income (Item 7); "physicians ... are free to
  terminate their association with our facilities or admit their patients to competing facilities at any time" (Item 1A).

### Bearing on Q3 (capital)
- Capital spending $1,010M against D&A $863M in 2025; $931M against $818M in 2024; $751M against $870M in 2023 (cash-flow
  statement, 10-K 2025). The filing does not split maintenance from growth spending (a new 54-bed hospital opened in 2025,
  de novo ASCs; no cost stated in the parts read).
- Purchases of businesses and minority interests, net of sales of facilities and minority interests: 2021 -$26M,
  2022 $97M, 2023 $277M, 2024 -$4,233M (the $4,981M hospital sales; $748M without them), 2025 $320M.

### Bearing on Q4 (the accounts)
- "Litigation and investigation costs" every year: $116M (2021), $70M (2022), $47M (2023), $35M (2024), $64M (2025);
  "Impairment and restructuring charges, and acquisition-related costs" every year: $85M, $226M, $137M, $102M, $130M
  (cash-flow statements). The recurring "one-time".
- Adjusted EBITDA is the measure the chief operating decision makers use (10-K 2025, segment note); the proxy's opening
  summary features "a 21.4% adjusted EBITDA margin" and "free cash flow after NCI distributions" (DEF 14A 2026).
- 2026 carries $826M of "Revenue from contract termination" in its first half (10-Q Q2 2026), the CHI payments for ending
  Conifer's CHI contract on 2026-12-31 (a $1,360M note, payable January 2027 to 2029).

### Bearing on Q5 (integrity facts recorded, not judged)
- "We have paid significant amounts to resolve government investigations and qui tam matters brought against us in the
  past" (10-K 2025, Item 1). The specific matters were not read in this run (the 10-K's litigation note was not opened
  beyond this sentence and the cost lines above).
- "certain of our current arrangements, including joint venture arrangements, do not qualify for safe harbor protection"
  under the Anti-kickback Statute (10-K 2025, Item 1A).
- The chief executive is also chairman. His 2025 total pay was $43,108,969, of which $31,677,365 in stock awards and
  $9,000,000 non-equity incentive (DEF 14A 2026, summary compensation table); 2025 annual incentive paid at 200% of target
  corporate performance and 250% to 300% of target for named officers after individual multipliers; the 2023 performance
  stock earned at 225% of target, on Adjusted EPS and "Adjusted Free Cash Flow ... minus cash distributions paid to
  noncontrolling interests" (DEF 14A 2026).

### Bearing on Q6 (the money)
- Repurchases: $200M (2023), $672M (2024), $1,386M (2025), $1,360M in the first half of 2026; the programme "has no
  expiration date" and names no price (10-K 2025, Item 7; 10-Q Q2 2026). Average prices paid: $236.30 (March 2026),
  $190.26 (May), $167.20 (June). Against the COMPUTATION range below ($170.82 bottom, all-equity), the March and May
  purchases sit above the bottom and the June purchases just below it.
- January 2026: CHI's 23.8% of Conifer redeemed for $540M, settled against CHI's payment (10-K 2025, Note 25).

### Bearing on Q9 (debt)
- Total long-term debt $13,248M at 2026-06-30, fixed-rate notes maturing 2027 to 2034 after the September 2026
  refinancing; interest expense $821M in 2025, "23% of our $3.508 billion of operating income" (10-K 2025, Item 1A); the
  revolving credit is secured by receivables "including receivables for Medicaid supplemental payments" (Item 1A).

### Q7: COMPUTATION, NOT A CLEARANCE
*(The file closed at Q1; nothing below is a verdict or a clearance, and it carries no entry language (operator rule 3).
Built by Q7's range convention in full, for the reporting figures the brief asks for. Scripts: `oc.py`, `val.py` in the
research folder.)*

**Owner cash, 2021 to 2025, USD millions.** Operating cash as filed, plus the aberrational items the filer itself
describes: the COVID Medicare advances repaid inside operating cash ($512M in 2021, $880M in 2022) and the deferred payroll
taxes paid ($128M each year) (10-K 2022, Note on COVID; specific (a)); and in 2024 the tax on the hospital-sale gains,
taken as the $821M by which the filer says 2025 tax payments fell short of 2024's (10-K 2025, Item 7; **CONVENTION of this
run**, a disclosed guess: the filer states the drop, not the tax on the gains). Less stock pay, all capital spending,
distributions to minority partners and finance-lease principal; less purchases of businesses and minority interests net of
sales (specific (c), acquisitions deducted; the 2024 sale of fourteen hospitals, $4,981M, is a shrinking of the business,
treated as aberrational under (a), with the literal window shown beside).

| year | operating cash, adjusted | owner cash before purchases | net purchases | **equity-only owner cash** | after-tax interest added back (24%) | **all-equity owner cash** |
|---|---|---|---|---|---|---|
| 2021 | 2,208 | 931 | -26 | 957 | 712 | 1,669 |
| 2022 | 2,091 | 595 | 97 | 498 | 644 | 1,142 |
| 2023 | 2,374 | 856 | 277 | 579 | 670 | 1,249 |
| 2024 | 2,868 | 1,102 | 748 | 354 | 647 | 1,001 |
| 2025 | 3,540 | 1,555 | 320 | 1,235 | 657 | 1,892 |
| mean | | 1,008 | | **725** | | **1,391** |

**CONVENTION of this run:** interest is added back at 24% tax (21% federal plus about 3% state, the 2025 rate
reconciliation's state line being 2.9%); rationale: the all-equity basis needs owner cash before interest after the
company's tax, and the reconciliation gives no single marginal rate. Depreciation variant beside: owner cash before
purchases on D&A instead of capital spending, mean $981M against $1,008M. The filing does not allow the maintenance guess
(specific (e)), so all spending is charged. Serial-acquirer test: net purchases over the window, without the 2024 sale,
$1,416M, against half of owner cash before purchases, $2,520M: not a serial acquirer; the default pair stands. The divested
hospitals' earnings are inside 2021 to 2023, so the base is if anything high for the business as it now stands.

**Growth.** All-equity owner cash, 2021 to 2025 end years: **3.18%** a year (aggregate, not per share); between the halves
of the window (2021-22 against 2024-25): 0.96%, shown beside. Equity-only, end years: 6.58%. Cap (f): carried ten years,
3.18% puts owner cash at about 7.1% of sales growing at the company's own 2.3% (2021 to 2025, $19,485M to $21,310M), below
the highest share earned in the window (8.9%, 2025); no cut. Zero nominal growth after year ten; discounted at 5.60%.

**Net debt** (latest filed date, 2026-06-30): total long-term debt including finance leases $13,248M less cash $2,170M =
**$11,078M**; the September 2026 notes refinance existing notes and change it only by costs (8-Ks 2026-09-08 and
2026-09-22); operating leases left out. The CHI note receivable ($1,242M carrying amount, 10-Q Q2 2026) is shown beside,
not in the central figure, because the window's owner cash still carries the CHI contract it pays for ending.

| case | value range a share | fair price a share | width | expected return at $269.14 |
|---|---|---|---|---|
| **All-equity, central** (base $1,391M; 0% and 3.18%) | **$170.82 to $259.53** | **$56.10** | 1.52 to 1 | 4.25% (no growth), 5.47% (growth) |
| Equity-only, beside (base $725M; 0% and 6.58%) | $160.70 to $271.03 | $115.80 | 1.69 to 1 | 3.34%, 5.64% |
| All-equity, CHI note counted (beside) | $186.24 to $274.95 | $71.52 | 1.48 to 1 | 4.41%, 5.68% |
| All-equity, halves growth 0.96% (beside) | $170.82 to $195.29 | $40.95 | 1.14 to 1 | 4.25%, 4.60% |
| All-equity, literal window with the 2024 sale proceeds as owner cash (beside) | $355.34 to $497.12 | $171.97 | 1.40 to 1 | 6.79%, 8.53% |

Read as the convention reads it, with no verdict: the floor is tested first, and no case, the literal window included,
earns about ten percent **[M2003-149]** at $269.14; the price sits above the top of the central range.

**The two reporting figures (a reporting convention; not a verdict, not entry language).**
- **(a) VALUE RANGE (COMPUTATION):** **$170.82 to $259.53 a share**, all-equity basis, owner cash after the company's own
  tax, against a price of $269.14.
- **(b) FAIR PRICE (COMPUTATION):** **$56.10 a share** on the all-equity basis (each end case valued at ten percent, the two
  averaged, less net debt of $11,078M, over 80.519M shares); **$115.80 a share** on the equity-only basis, beside it. The
  all-equity figure is the central one.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit e604df1a, before the first EDGAR request); written question by
      question; committed after Step 0, after Q1, and at the close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatcher's; this run binds nothing
      until it is folded into the register (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. A directory listing filtered for "THC|tenet" showed
      five other runs' file names, and the opening git status showed CYH commit subjects; both declared under
      contamination at the top, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check
      script `Test Runs/_research 2026-10-13 THC/check_ids.py`, PASS); every filing fact carries its accession; numbers of
      ours carry a CONVENTION label.
- [x] The order was kept; the first STOP (Q1) closed the run; everything after it is facts or COMPUTATION, not a
      clearance.
- [x] Owner cash after every real cost, including the minority partners' distributions and finance-lease principal,
      never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price quote flagged as an
      aggregator's.
- [x] Contrary evidence written down as found (Foundations); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no anchor-date bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its "owner earnings" means, its yields and its "growth the
      price assumes" were not used.
- [x] `python tools/check_framework.py` PASS before the closing commit.
- Weak points, said plainly: the 2024 tax on the sale gains is a guess from the filer's stated year-on-year drop; the
  parts test turns on 50.8% against 49.2%, and on a measure (segment Adjusted EBITDA less segment depreciation) that is
  this run's convention; the rivals' EBIT is as filed and unadjusted for their impairments and gains; the litigation note
  of the 10-K was not read beyond Item 1's sentence.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Government as the key variable has no test of its own at Q1.** Test 7 asks whether the forecast is about
customers or about technology; the deciding forecast here is about legislators and state agencies, which is neither. I
reached the box through tests 3, 4 and 5 and the company's own filed statement that it cannot estimate the effect; the
rows nearest the case ([L2023-011], the utility error; [M2004-058], the speakers overestimating regulation) point opposite
ways, and the framework says nothing about which governs a business paid in part by government. A rule that says whether a
regulated or government-paid revenue stream is a Q1 matter (understanding) or a Q2 matter (a castle that can be filled in
by statute), as the commodity paragraph of 2026-10-12 did for commodity prices, would stop two runs placing it in
different questions. (2) **The parts threshold is knife-edge here and its measure is unstated.** "Five-year operating
profit" is not defined for a filer that reports only segment Adjusted EBITDA; I confessed a measure, and on it the hospitals
carry 50.8%. On the common owner's share (after the minority partners, who take far more of USPI's profit than of the
hospitals'), the hospitals carry clearly more; the text does not say whether the threshold is read before or after
noncontrolling interests, which for a joint-venture business like USPI is a large difference. (3) **Specific (c) on a
large divestiture.** "Net of businesses sold" read literally turns the sale of fourteen hospitals into $4.2 billion of owner
cash in one year; I treated it as aberrational under (a) and showed the literal window beside, but the text does not say
that a shrinking sale is outside (c), nor what to do with the sold hospitals' earnings still inside the window's early
years.
