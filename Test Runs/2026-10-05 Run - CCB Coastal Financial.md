# Company Run — Coastal Financial Corporation (NASDAQ: CCB) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Blind analyst run
of record. Research folder: `Test Runs/_research 2026-10-05 CCB/` (the filings as text, the peer XBRL extracts, the id
check). Written top to bottom, question by question; the skeleton of this file was written before any fetch.

**POSITION NOTE, declared before any verdict:** not checked; the brief forbids opening `PORTFOLIO.md`, and I did not.
**Contamination, declared:** the session context handed to me at start-up carried the repository's recent commit
subjects, and one reads "PORTFOLIO: CCB position recorded". I did not look for it; I have seen it. I therefore run this
name as one the operator may hold. That is the incentive operator rule 9 names: the analyst near a holder has a reason to
clear. The antidote I applied is the row's: "if you have doubts about something being into your circle of competence, it
isn’t." **[M2002-092]**. I opened none of the forbidden files (the two earlier CCB runs, their research folder, any
holding review, the resume-state files, the queue).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $39.88 (live quote 2026-10-05, read through `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, no par, **15,286,327** (Form 10-Q for the
  period ended 2026-06-30, filed 2026-08-07, accession `0001437958-26-000061`; `python Screens/cover_shares.py CCB`).
- **Market cap:** about $609.6M (15,286,327 × $39.88).
- **Sovereign for the earnings currency (USD):** 5.63%, the US Treasury daily par yield curve, 30-year, dated
  2026-10-02 (the latest curve date `tools/run.py` returned on 2026-10-05; issuing authority).
- **Filings read** (operator rule 4), all from EDGAR, CIK 0001437958:
  - Form 10-K for FY2025, filed 2026-02-27, accession `0001437958-26-000013` (business, risk factors, MD&A, segment
    tables, credit-enhancement tables, capital table, Item 9A, the auditor's reports).
  - Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-07, accession `0001437958-26-000061`.
  - DEF 14A, filed 2026-04-13, accession `0001437958-26-000023` (ownership tables only; Q5 not reached).
  - Form 8-K, Item 4.02 (non-reliance, restatement), filed 2025-03-17, accession `0001437958-25-000056`.
  - Form 8-K, Item 4.01 (auditor change, Moss Adams to Baker Tilly), filed 2025-06-04, accession `0001437958-25-000130`.
  - Form 8-K, Item 8.01 (Bluevine to be acquired by Valley National), filed 2026-09-28, accession `0001437958-26-000065`.
  - Forms 8-K, Item 5.02: CFO appointed (`0001437958-25-000157`, 2025-09-22); Chief Risk Officer resigned
    (`0001437958-25-000160`, 2025-10-02); CFO departure and interim CFO, accession `0001437958-26-000045` (2026-07-22); Executive Chair
    appointed and bylaws amended, accession `0001437958-26-000056` (2026-07-30); a director added, accession
    `0001437958-26-000017` (2026-03-12). The Q2 2026 earnings 8-K, accession `0001437958-26-000052`, was read for its
    item only; the figures are taken from the 10-Q.
  - **Regulatory enforcement:** no formal order, written agreement or consent order is disclosed in the 10-K or the
    10-Q. The 10-K speaks only conditionally ("If we were to become subject to a regulatory action") and of "any
    supervisory actions to which we are or become subject". Informal supervisory actions are confidential and would not
    appear; that is itself a fact about what can be read from the outside, and it is carried into Q1.
- **One figure cross-checked against the filed statement:** total deposits at 2025-12-31, $4,144,199 thousand on the
  consolidated balance sheet in the 10-K, against $4,144.2M in the XBRL facts of the same accession. They agree.
- **`tools/run.py CCB`, arithmetic lines only.** Price, shares, sovereign and the balance-sheet transcription are used.
  Its "owner earnings" line (operating cash flow less stock pay and capex, a printed "yield" of 36%) is **meaningless for
  a bank** and is not used: a bank's operating cash flow carries loan-sale and held-for-sale flows (CCB sold $6.64B of
  CCBX loans in 2025) and says nothing about the cash an owner can take out. Q1 closes before Q4 and Q7, so no
  substitute cash figure is built; nothing printed by the tool as a rule, an id or a verdict was read (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this bank will be in ten years, not where the quote goes
after a loss quarter. The market serves and does not instruct **[M2006-077]**: the price fall that a $42.1M quarterly
loss produces says nothing about value either way. Who is paid to tell you **[M2020-037]**: the 10-K's own words on the
partners' indemnities ("We believe that this alignment of interests ensures that CCBX partners are motivated to implement
robust risk management practices") are management's, and are read as such. The analyst's habits: the worst anchor "is
always your previous conclusion" **[M2016-054]**, and here the anchor I had to resist is not a conclusion of mine but the
knowledge that the name may be held.

**Contrary evidence, written down as found** **[M1997-127]**, in the order the filings gave it:
1. Item 4.02, 2025-03-17: FY2023 and three 2024 quarters could not be relied on; interest income and BaaS loan expense
   were misstated "due to differences between BaaS lending partner accounting" and the bank's; material weaknesses in
   ICFR at 2024-12-31 and 2023-12-31; the predecessor auditor's ICFR opinion for 2024 was adverse (Item 4.01 8-K).
2. CCBX deposits were 61.7% of total deposits at 2025-12-31; "two partners with deposits that together represent 45% of
   total deposits" (10-K, liquidity note).
3. CCBX net charge-offs $196.8M in 2025 on average CCBX loans of $1,730.0M, about 11.4%; carried by partner promises of
   reimbursement booked as a "credit enhancement asset" of $177.7M, 36% of year-end equity of $491.0M.
4. Q2 2026: a net loss of $42.1M, "primarily attributable to a $68.8 million credit expense related to a single, isolated
   CCBX partner relationship, which included a $46.0 million credit enhancement receivable valuation adjustment" and a
   $22.8M specific provision "for credit losses not expected to be fully collected under the partner's indemnification
   arrangement". Four months earlier the 10-K had called the alignment of interests a guarantee of partner discipline.
5. Uninsured deposits rose from 15.5% of deposits (2025-12-31) to 27.7% (2026-06-30).
6. 2026-09-28: Bluevine, a partner with about $447M of deposits on the balance sheet, agreed to be acquired by Valley
   National Bancorp, a bank. The 10-K's own risk factor: partners "may seek to reduce their reliance on third-party
   banking relationships by obtaining their own bank charters".
7. Turnover in the risk and finance chairs: the Executive Vice President and Chief Risk Officer resigned effective
   2025-10-01 (8-K, accession `0001437958-25-000160`); the CFO since 2012 handed over the same day to a successor
   (accession `0001437958-25-000157`), who left effective 2026-08-15 after about ten and a half months; the retired CFO
   returned as interim at $100,000 a month; a non-employee director since 2016 was made Executive Chair at $750,000 a
   year (accession `0001437958-26-000056`).
8. No repurchases and no authorized programme (10-Q, Part II Item 2); a $91.8M public offering of 1,380,000 shares in 2024.

## THE STANDING RULE
Owning a common share bought with cash puts the buyer at risk of losing what is paid and nothing more; no borrowing, no
collateral, no option given is involved **[M2012-081]**, **[L2023-005]**. The rule is not engaged by this purchase; it is
engaged only if the buyer were to finance or size it so that a total loss of the position mattered.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the framework states it for a bank.** "A bank is inside the circle when both sides of its balance sheet can
be read from its filings, the little-risk asset side and the cheap deposit side **[M2002-022]**, and outside it when the
asset side cannot **[M2005-068]**", and "the readable half does not make the unreadable half readable **[M2002-094]**"
(Q1, The door against the exclusion, settled). The row that opens the door: banks with "very little risk on the asset
side and very cheap money on the deposit side. And even Charlie and I can understand that." **[M2002-022]**; the danger
"It’s always on the asset side." **[M2011-022]**. CCB is two banks on one charter, and the filing reports them as two
segments, so each side is read for each segment.

**The balance sheet, by segment, 2025-12-31** (10-K segment table, accession `0001437958-26-000013`; dollars in millions):

| | Community bank | CCBX (BaaS) | Treasury & admin | Consolidated |
|---|---|---|---|---|
| Loans receivable | 1,942.0 | 1,807.6 | | 3,749.5 |
| Allowance for credit losses | (18.2) | (151.3) | | (169.5) |
| Deposits | 1,586.4 | 2,557.8 | | 4,144.2 |
| Cost of deposits, FY2025 | 1.71% | 3.84% | | 2.99% |
| Loan yield, FY2025 (CCBX before BaaS loan expense) | 6.52% | 15.87% | | 11.00% |
| Net charge-offs, FY2025 | $0.027M | $196.8M | | $196.8M (5.45% of average loans) |

At 2026-06-30 (10-Q, accession `0001437958-26-000061`): assets $5.46B, loans $4.21B, deposits $4.86B of which CCBX
$3.29B (67.7%), equity $463.4M; Tier 1 leverage 9.11% (company), down from 10.62% at year-end.

**1. The community bank, asset side: readable.** Commercial real estate and C&I loans in the Puget Sound region (81% of
community real-estate loans secured there), non-owner-occupied CRE at 170.9% of total risk-based capital, net
charge-offs of $27 thousand in 2025 and $540 thousand in 2024. A reader can say what this book is and roughly what it will
lose. Nothing here is beyond the filing.

**2. The community bank, deposit side: readable and fairly cheap.** $1.59B of deposits costing 1.71% in 2025, gathered
through 14 branches, 12 in Snohomish County "where we are the largest community bank by deposit market share", with
80.9% of community loan customers also holding deposits. That is money "from a natural customer base" **[M2012-012]**.
For contrast, Heritage Financial, a plain Washington commercial bank, paid 1.37% on its deposits in 2025 (below). On its
own this half would pass the door.

**3. CCBX, asset side: cannot be read from the filings.** This is the deciding finding.
- The book: $1.81B of loans originated by fintech partners, chiefly credit cards ($622.7M) and other consumer loans
  ($691.7M; average consumer balance about $500 to $800), plus $210.5M of capital-call lines to venture funds through one
  partner. Loans are underwritten on the partners' own "policies, scorecards, and/or lending models", submitted to the
  bank for approval. The bank also sold $6.64B of CCBX loans in 2025 and $7.84B in the first half of 2026, mostly
  revolving card balances sold back to partners at par: the loan book on the balance sheet is a slice of a flow many
  times its size.
- The losses: CCBX net charge-offs were $196.8M in 2025 on average CCBX loans of $1,730.0M, about 11.4%, and the CCBX
  provision was $190.0M in 2025 and $277.8M in 2024.
- What stands between those losses and the bank's equity is not collateral but a promise. "CCBX partner agreements
  provide for credit enhancements that cover $192.2 million, or 97.7%, of the charge-offs on CCBX loans" (10-K). The
  bank books a provision and, at the same moment, a matching "credit enhancement asset" through noninterest income: a
  receivable from the partner. It stood at $177.7M at 2025-12-31, **36% of equity**. Its value is the partners' ability
  to pay. The partners are, with one exception (Bluevine, named in an 8-K), not named; their finances are not in CCB's
  filings; the filings disclose 22 active relationships at 2026-06-30 against 28 "at varying stages" at year-end.
- The rows name this asset. Of a promise to pay when losses come: "you better be very sure that they can and will pay,
  because the terrible thing that’s happening to you may be presenting terrible things to them. [...] And that’s why
  reinsurance recoverables are a dangerous asset to have." **[M2003-084]**. And of a chain of such promises: "When a
  daisy chain of retrocessionaires exists, a single weak link can pose trouble for all." **[L2001-018]**.
- **What happened.** In February 2026 the 10-K said: "We believe that this alignment of interests ensures that CCBX
  partners are motivated to implement robust risk management practices and maintain the overall health of the
  portfolio." In the second quarter of 2026 one partner's promise failed: a $46.0M valuation adjustment on the credit
  enhancement receivable, the first ever recorded, plus a $22.8M specific provision for losses "not expected to be fully
  collected under the partner's indemnification arrangement", $68.8M in all, about 14% of year-end equity, and a $42.1M
  quarterly net loss. The rows say this is how it goes with lenders: "You spot troubles in financial institutions late.
  It’s just the nature of the beast." **[M2001-066]**; and "the only thing we understand is that we don't understand how
  much risk the institution is running." **[L2002-018]**.
- **The accounts themselves came from the partners.** The 2025 restatement arose from "differences between BaaS lending
  partner accounting" and the bank's, and the material weaknesses concerned "accounting and financial reporting for
  information provided by Banking-as-a-Service (“BaaS”) partners" (10-K Item 9A; remediated and reported effective at
  2025-12-31 by management and Baker Tilly). Test 3 asks whether the past statements tell me the future ones **[M2008-033]**;
  here the bank could not, for two years, state its own CCBX income lines correctly from what its partners sent it.
- Growth has hidden the test the rows ask for: "in all types of financial institutions, rapid growth sometimes masks major
  underlying problems (and occasionally fraud)." **[L2004-009]**. Assets went from $806M (2017) to $5.46B (June 2026);
  the CCBX book has never been seen in a no-growth year.
- So I can follow every transaction, and cannot say what the whole is worth: "even though I could understand every
  individual transaction they did, I don’t regard the whole enterprise, or the operation of it, necessarily as being
  within my circle of competence." **[M2002-094]**. That is the row's case exactly.

**4. CCBX, deposit side: not cheap, and not the bank's own customers.** CCBX deposits cost 3.84% in 2025 (4.70% in 2024),
against 1.71% for the community bank. The partner sets the rate to its customer and the bank pays the partner; the money
belongs to the partner's customers, sits where the partner places it, and moves with sweeps ($843.6M swept off the
balance sheet at year-end). Two partners held 45% of total deposits; one of the large ones (Bluevine, about $447M) has
agreed to be bought by a bank. Uninsured deposits went from 15.5% to 27.7% in six months. Test 12 asks whether funds come
"from a natural customer base" or "on a wholesale basis, and that money can run pretty fast" **[M2012-012]**; CCBX money
is neither the bank's natural base nor brokered wholesale, but it behaves like the second: a counterparty can take it in
one decision. The rows' question for a lender, "what can be demanded of them tomorrow morning" **[M2023-103]**, cannot be
answered for 45% of the deposits without knowing two unnamed partners' plans. Pathward, another BaaS bank, paid 0.09% on
its deposits (below), so cheap BaaS money exists; CCB's is not it. This half fails "very cheap money on the deposit side"
**[M2002-022]** on the evidence, and is not readable as to its permanence.

**5. The ten-year question and the winners.** Understanding means "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**. For CCBX that requires knowing which fintechs
will be partners in ten years, whether they stay solvent, and whether they keep needing a third-party bank: the 10-K warns
they may obtain "their own bank charters", and its largest-named partner is now being bought by one. "there’s industries
we know that may have a wonderful future, but we don’t have the faintest idea who the winners will be" **[M2012-067]**;
"We view change as more of a threat into the investment process than an opportunity." **[M1999-063]**. The bank's culture
cannot be read from outside either, and the row says so of most banks: "that’s hard to do for 99 percent of the banks."
**[M2008-090]**; a chief risk officer gone in October 2025, two changes of finance chief in ten months and a new
executive chair do not make it easier.

**The door, applied.** Community bank: both sides readable. CCBX: the asset side's protection is a receivable from
unnamed private counterparties, one of which has just failed to pay in full; the deposit side is dear and controlled by
two partners. CCBX is now the larger segment by deposits (67.7%) and the source of nearly all the risk. The settled
reading governs: a readable half does not make an unreadable half readable **[M2002-094]**, and the file closes in the
"too hard" box **[M2006-013]**. Doubt alone would close it **[M2002-092]**; this is more than doubt. It is no judgment that
the bank is bad: "It’s no judgment that there’s anything bad." **[M2007-052]**; "It doesn’t mean it isn’t a good buy."
**[M2000-038]**.

**Which cause: NATURE, not WORK.** The test between them is whether the insiders would write the forecast down (test 5,
**[M2000-105]**). The deciding question is the ten-year solvency and conduct of the fintech partners whose promises carry
the CCBX asset side. That is not knowable from primary public documents: the partners are mostly private and unnamed, and
their accounts are not filed. The one insider who could see everything, the bank's management, wrote a one-sentence
forecast of partner discipline in February 2026 and recorded the failure of that forecast in June 2026. The rows call
this the nature of the industry, not a gap in the reader: "in other cases the nature of the industry would be the
roadblock." **[L1993-023]**; "It’s just the nature of the beast." **[M2001-066]**. A research pass could name a few more
partners, but under the pass's own rule (c) a question unanswerable from primary documents is recorded and set aside, and
the remaining answers already show the unreadable half; a pass that ends unsure ends TOO HARD (NATURE) **[M2002-092]**.
No lower price reopens the box **[M2000-038]**. For the record, the questions a WORK reading would have listed are: the
names and audited condition of the partners behind the credit-enhancement asset; the loss history of each partner's
programme through a downturn; the contractual notice and exit terms on the two largest deposit relationships. The first
two are not on the public record for private fintechs; the third would not answer the ten-year question.

**VERDICT: TOO HARD (NATURE)** at Q1. The CCBX asset side cannot be read from the filings: 97.7% of its charge-offs are
carried by partner indemnities booked as a receivable equal to 36% of equity (2025-12-31), and in Q2 2026 one partner's
indemnity failed for $68.8M (10-Q, accession `0001437958-26-000061`).

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED.
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.
## Q7 — WHAT IS IT WORTH? NOT REACHED.
## Q8 — IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — IS IT THE FAT PITCH? NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## EVIDENCE GATHERED BEYOND THE CLOSING STOP: NOT A CLEARANCE
*The brief asked for the competitor row and the balance-sheet reading. They were gathered before Q1 closed, because the
bank door needs both sides of the balance sheet and a yardstick for "cheap money". They are recorded here as evidence, not
as answers to Q2 or Q4, which were not reached; nothing below carries entry language.*

**The competitor row** (FY2025 or nearest fiscal year; from each company's own 10-K XBRL facts; ratios mine: ROA on
average assets, cost of deposits as interest on deposits over average deposits, efficiency as noninterest expense over net
interest income plus noninterest income, net charge-offs over year-end net loans):

| Company | Accession | ROA | Cost of deposits | Efficiency | Net charge-offs / loans | Equity / assets |
|---|---|---|---|---|---|---|
| Coastal Financial (CCB) | `0001437958-26-000013` | 1.06% | 3.02% (filed: 2.99%) | 53.1% | 5.50% (filed: 5.45% of average) | 10.4% |
| The Bancorp (TBBK) | `0001295401-26-000002` | 2.52% | 2.05% | 31.7% | 2.23% | 7.4% |
| Pathward (CASH), FY to 2025-09-30 | `0000907471-25-000116` | 2.53% | 0.09% | 66.7% | 1.63% | 12.0% |
| Green Dot (GDOT) | `0001386278-26-000015` | -1.73% (net loss $98.9M) | not tagged | not computed | not meaningful (loans $55.7M) | 14.9% |
| Heritage Financial (HFWA), plain community bank | `0001628280-26-012703` | 0.96% | 1.37% | 67.3% | 0.03% | 13.2% |

Cross River Bank: no SEC filer found by an EDGAR company search for "cross river" with form 10-K (2026-10-05); not
compared. Caveats: CCB's efficiency ratio is flattered by the gross-up (credit-enhancement income in noninterest income
against BaaS loan and fraud expense in noninterest expense), so it is not comparable; Pathward's near-zero deposit cost
reflects prepaid and payment balances that are mostly noninterest bearing. What the row shows for the bank door: two other
BaaS banks earn more than twice CCB's return on assets with half or less of its loss rate, and one of them gets its money
almost free; CCB earns about what a plain community bank earns, with a hundred and eighty times its loss rate, carried by
partners' promises.

**The balance sheets, 2017 to June 2026** **[M2025-032]** (XBRL facts of CCB's 10-Ks, newest vintage; $M):

| Year-end | Assets | Deposits | Net loans | Allowance | Equity | Borrowings | Net income | Provision | Interest on deposits |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 806 | 703 | 649 | 8 | 66 | 10 | 5 | 1 | 2 |
| 2018 | 952 | 804 | 758 | 9 | 109 | 10 | 10 | 2 | 3 |
| 2019 | 1,129 | 968 | 928 | 11 | 124 | 10 | 13 | 3 | 6 |
| 2020 | 1,766 | 1,421 | 1,528 | 19 | 140 | 10 | 15 | 8 | 4 |
| 2021 | 2,636 | 2,364 | 1,714 | 29 | 201 | 24 | 27 | 10 | 2 |
| 2022 | 3,144 | 2,818 | 2,553 | 74 | 243 | 48 | 41 | 79 | 19 |
| 2023 | 3,750 | 3,360 | 2,904 | 117 | 295 | 48 | 45 | 184 | 89 |
| 2024 | 4,121 | 3,585 | 3,310 | 177 | 439 | 48 | 45 | 278 | 121 |
| 2025 | 4,741 | 4,144 | 3,580 | 170 | 491 | 48 | 47 | 193 | 117 |
| 2026-06-30 | 5,460 | 4,860 | 4,210 (gross) | | 463 | | (30) first half | | |

What the figures say: the bank is six to seven times its 2017 size; the allowance went from $8M to $177M as the CCBX
consumer book arrived in 2022; interest on deposits went from $2M (2021) to $117M (2025) as partner money replaced branch
money; equity grew from $66M to $491M, of which $91.8M was a 2024 share sale and the rest retained earnings, before
falling to $463M after the first-half 2026 loss. What they do not say: the credit-enhancement asset that offsets the
provisions is not a separate line in this table and its quality is not visible in it; the reported net income of $45M to
$47M a year (2023 to 2025) is the residue of provisions of $184M to $278M a year netted against partners' promises.
**What they cannot say:** whether those promises will be kept. That is the Q1 finding.

**COMPUTATION — NOT A CLEARANCE.** At $39.88 the market capitalisation of about $609.6M is about 1.32 times the equity of
$463.4M at 2026-06-30. Recorded as arithmetic only; Q7 was not reached and no value is stated.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**. The community bank half is readable on both sides; the CCBX half is not: its
asset side rests on indemnities from mostly unnamed private fintech partners (a receivable of $177.7M, 36% of equity, at
2025-12-31), one of which failed for $68.8M in Q2 2026, and its deposit side costs 3.84% with two partners holding 45%
of deposits. The deciding question, the partners' ten-year solvency and conduct, is not on the public record and was
mis-forecast by the insiders themselves; no further work is opened and no lower price reopens it **[M2000-038]**. Q7 not
reached; no range is stated.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. **Not committed after each:** the brief
      for this run forbade commits; the file was written early and filled in place.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, see below); every filing fact has its
      accession; no number without a filing or a stated computation.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance, and the evidence beyond the stop is headed
      as such.
- [x] Owner cash after every real cost, never a net-income proxy: not computed, because Q4 and Q7 were not reached; the
      tool's operating-cash figure was rejected as meaningless for a bank. The sovereign is from the Treasury, dated; the
      price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the eight items under the foundations).
- [x] No row dated after the anchor is cited in a point-in-time run: not a point-in-time run (anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS (run 2026-10-05 after writing: no phantom ids, no unlabelled numbers, every
      ledger row verbatim). A separate script found 30 distinct v5 ids cited, all present in `principle_ledger_v5.csv`,
      no v4 (E-) ids, and every quoted fragment placed before an id matching that row's text.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) **WORK or NATURE for a counterparty question.** Test 5 asks whether the insiders "would not want to put
down on paper" the forecast **[M2000-105]**. Here the insiders did put a forecast down (the alignment sentence) and were
wrong within four months. The framework does not say whether an insider forecast that fails counts as one they "would
write down"; I read the failure, with **[M2001-066]**, as evidence of the industry's nature and closed NATURE, but a
second analyst could call it WORK and open a research pass that would stall on private partners' accounts. (2) **The bank
door has no rule for third-party credit protection.** The door asks for "very little risk on the asset side"
**[M2002-022]**; it does not say whether a high-loss book made low-risk by a counterparty's indemnity counts as little
risk. The nearest rows (**[M2003-084]**, **[L2001-018]**) sit in the standing rule and Q9, not in Q1; I carried them into
Q1 because Q9's test 10 says the financial-institution question is owned by Q1. A sentence in the door naming
indemnities, recoverables and credit enhancements would settle it. (3) **Evidence asked for after the stop.** The hard
sequence closes the file at Q1, but the brief asked for the competitor row and the balance-sheet reading; the framework
is silent on recording evidence gathered beyond the stop. I recorded it under a NOT A CLEARANCE heading. (4) **The
template's write-early rule says commit after each question**, and this brief forbade commits; the self-audit says so
rather than ticking it plainly. (5) **`tools/run.py` prints an operating-cash "owner earnings" and a 36% "yield" for a
bank**, which is nonsense for a lender; the sector method covers insurers and float companies only, and there is no
stated cash-figure method for a bank at Q4 and Q7. Had the run reached Q4, I would have had to invent one and confess it.
