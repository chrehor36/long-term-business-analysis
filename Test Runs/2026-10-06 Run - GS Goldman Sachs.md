# Company Run — The Goldman Sachs Group, Inc. (NYSE: GS) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
Blind analyst run of record, at the operator's request. Research folder: `Test Runs/_research 2026-10-06 GS/` (tool
output, the filing extracts with accessions, the peer XBRL script, the id check). The skeleton of this file was copied
from the template before any fetch.

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. I did not open
`PORTFOLIO.md`, any earlier run or research folder for GS, any holding review, the session-state files, the queue
register, the prepped reading list or `tools/alerts.json`. **Contamination, declared:** I read one other company's v5 run
of 2026-10-05 (CCB Coastal Financial, a bank) for form only, which showed me how a previous analyst applied the bank door
at Q1; that is a form contamination toward a Q1 close and is named here so it can be discounted. My training-memory of
Goldman Sachs (a dealer-bank whose earnings swing with markets) is a prior; it is replaced below by what the filings say.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $893.46 (quote of 2026-10-05 read through `python tools/run.py GS` on 2026-10-06; **aggregator, flagged** per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class of common stock, **291,171,408** shares (Form 10-Q for the
  period ended 2026-06-30, filed 2026-08-03, accession `0000886982-26-000297`; cover as of 2026-07-17;
  `python Screens/cover_shares.py GS`). The preferred series and depositary shares listed on the 8-K covers are not common
  equity and are not added. The 10-Q balance sheet shows 291,442,355 outstanding at 2026-06-30.
- **Market cap:** about $260,150M (291,171,408 × $893.46).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, dated 2026-10-05
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4), all from EDGAR, CIK 0000886982:
  - Form 10-K for FY2025, filed 2026-02-25, accession `0000886982-26-000091` (business, risk factors, MD&A including the
    deposit table, market risk and VaR, liquidity, the statistical disclosures; Notes 4, 5 and 7 on fair value and
    derivatives; the balance sheet and statement of changes in equity).
  - Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-03, accession `0000886982-26-000297` (balance sheet, Level 3
    table, derivative note totals).
  - DEF 14A, filed 2026-03-20, accession `0001193125-26-117433` (fetched; not read for Q5 or Q6, which were not reached).
  - Form 8-K, 2Q26 earnings, filed 2026-07-14, accession `0000886982-26-000294`, EX-99.1 (`a2q26gsearningsresults.htm`),
    the latest earnings release on 2026-10-06.
  - Form 8-K, Items 2.02 and 8.01, filed 2026-01-08, accession `0000886982-26-000004` (the Apple Card transition: a $2.48B
    reserve release against a $2.26B revenue reduction in Q4 2025; the segment change).
- **One figure cross-checked against the filed statement:** total assets at 2025-12-31, $1,809,320M on the Consolidated
  Balance Sheet of the 10-K, against $1,809,320M in `tools/run.py`'s XBRL transcription of the same accession. They agree;
  total shareholders' equity, $124,972M, agrees likewise.
- **`python tools/run.py GS`, arithmetic lines only** (output saved as `run_py_output.txt`). Price, shares, sovereign and
  the ten balance-sheet year-ends are used. Its "owner earnings" lines (operating cash flow of −$12,587M, −$13,212M and
  −$45,154M for 2023 to 2025, giving a negative "yield") are **meaningless for a dealer-bank**: its operating cash flow is
  dominated by changes in trading assets, trading liabilities and customer receivables and payables (the tool itself
  flags +$57,560M of trading-liability change inside 2025's figure) and says nothing about cash an owner can take out.
  They are not used. Nothing the tool prints as a rule, an id or a verdict was read (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what this firm's earning power and condition will be in ten years,
not where a stock that has run to 2.4 times book goes next. The market serves and does not instruct **[M2006-077]**: a
record quarter (2Q26 net earnings $6,628M, annualized ROE 23.5%, EX-99.1) and the price that follows it carry no
instruction about value. **Who is paid to tell you** bears with unusual force here, because the subject *is* the barber:
"you do not get impartial advice from Wall Street — (laughs) — when there’s (an) enormous amount of fees possible from one
action, and no fees applicable from another action." **[M2020-037]**; "don’t ask the barber whether you need a haircut"
**[M2011-083]**. Goldman's own descriptions of its risk are read as a seller's. The analyst's habits: the worst anchor
"is always your previous conclusion" **[M2016-054]**; my prior about the firm, and the form of the CCB run I read, are the
anchors to resist in either direction.

**Contrary evidence, written down as found** **[M1997-127]**, in the order the filings gave it (against my prior that the
firm's condition cannot be read, as well as for it):
1. *Against the prior:* Level 3 financial assets were only 1.1% of total assets at 2025-12-31 ($20,324M), and "the fair
   values for substantially all of our financial assets and liabilities are based on observable prices and inputs" (10-K,
   `0000886982-26-000091`). Most of the book is marked to observable prices.
2. *Against the prior:* average daily VaR was $90M in 2025 and $92M in 2024, small against equity of $124,972M; one-day
   regulatory VaR was exceeded on only three days in 2025 (10-K).
3. *Against the prior:* deposits are now $501,422M, the largest single funding source, of which $269.63B is FDIC-insured;
   consumer deposits are $207,902M (10-K deposit table). There is a retail deposit base that did not exist a decade ago.
4. *For the prior:* derivative notional of $43,530,881M at 2025-12-31, up from $37,127,322M, and $52,831,907M at
   2026-06-30 (10-Q, `0000886982-26-000297`); gross fair values of $360,080M (assets) and $391,214M (liabilities) are
   reduced to $52,953M and $84,405M only by netting agreements and collateral.
5. *For the prior:* those deposits cost 3.94% on average in 2025, against 2.68% at Morgan Stanley and 1.82% at JPMorgan
   (peer row below); the "consumer" deposits are Marcus and Apple Card balances, and Apple Card is being transitioned away
   over about 24 months (8-K, `0000886982-26-000004`).
6. *For the prior:* the 10-K's own words on its market risk measure: "Previous moves in market risk factors may not
   produce accurate predictions of all future market moves", and VaR "is most effective in estimating risk exposures in
   markets in which there are no sudden fundamental changes or shifts in market conditions."
7. *For the prior:* total assets rose 17.6% in six months, from $1,809,320M to $2,127,711M, with trading assets from
   $656,796M to $789,083M (10-Q); the balance sheet a reader studies at year-end is not the one at risk six months later.

## THE STANDING RULE
Owning a common share bought with cash puts the buyer at risk of losing what is paid and nothing more; no borrowing, no
collateral and no option given is involved **[M2012-081]**, **[L2023-005]**. The rule is not engaged by the purchase as
such; it would be engaged only by financing it with borrowed money **[L2014-005]** or by sizing it so that a total loss
mattered.
