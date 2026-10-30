import io
p = 'Test Runs/2026-09-19 Run - IBM International Business Machines.md'
s = io.open(p, encoding='utf-8').read()
i = s.index("## SELF-AUDIT")
new = """## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 OUT → Q3, Q4, the
      computation and Q6 all written under a standing **RECORDED, NOT GOVERNING** banner placed
      immediately after the Q2 verdict.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN and Q3 IN
      and Q4 IN carry none. **The word PROVISIONAL appears once, attached to the mainframe moat
      class inside a gate whose verdict is OUT** — where a provisional class cannot promote
      anything and does not sit under an IN.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** **There is no
      UNRESEARCHED verdict in this file**, and that was checked rather than assumed: every gate is
      IN or OUT. Two sub-questions inside Q2 are marked **UNKNOWABLE**, with what cannot be known
      stated (below).
- [x] **Every UNKNOWABLE states what specifically cannot be known.** Two, both inside Q2: (a)
      **Transaction Processing and IBM Z profitability and unit volume** — IBM has never disclosed
      profit below the reportable-segment level or any MIPS series, so **no document exists** that
      would resolve the franchise leg's own economics; (b) **the mainframe comparator set** — BMC is
      private (KKR, no SEC periodic reports), Broadcom folds its CA mainframe software into an
      undisclosed *Infrastructure Software* segment, and no one sells a competing mainframe, so the
      same-metric peer cell cannot be filled by any filing. Both are UNKNOWABLE rather than
      UNRESEARCHED because I can name no document, not because I did not look.
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** FY2025
      10-K `0000051143-26-000010`, filed 2026-02-24, **with the incorporated Annual Report exhibit
      `ibm-20251231_d2.htm` inside the same accession**, which is where the statements and MD&A
      live; Q2 2026 10-Q `0000051143-26-000078`; the furnished Q2 2026 release
      `0000051143-26-000077` EX-99.1 and the CEO's pre-announcement letter `0000051143-26-000070`
      EX-99.1; the FY2025, FY2024, FY2022 and FY2021 earnings releases; the 2026 proxy
      `0000051143-26-000025`; and the FY2022 and FY2021 Annual Report exhibits for the Kyndryl
      perimeter. **Two figures cross-checked** against the filed statements: total revenue
      $67,535M and operating cash flow $13,193M, both matching XBRL to the dollar. MD&A,
      cash-flow statement **including its detail lines** (the $(4,278)M receivables line is the
      whole Q4 financing question), and footnotes (segments, borrowings, retirement-related
      benefits, revenue recognition, commitments and contingencies, acquisitions) all read.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.**
      Four annual windows × two (c) ends × two financing constructions, plus a TTM; the four-year
      FY2022-FY2025 mean is the longest legitimate one and **the reason the five-year default
      [E2-42] could not be met is stated and quoted** (the cash-flow statement includes Kyndryl and
      IBM published no Kyndryl cash-flow statement). (c) is disclosed as a guess **[E2-23]** at
      $1,600M-$2,000M with the raw filed D&A end refused in writing and the size of the refusal
      given ($3.1bn a year).
- [x] **Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED.** Ten peers with
      their own stated windows, four metrics, filing-sourced. Unfillable cells named, not guessed
      (ORCL and HPE gross margin, AMZN R&D, SAP in EUR). **The mainframe sub-claim is marked
      PROVISIONAL with its comparator set shown to be empty, and it is classed UNKNOWABLE rather
      than UNRESEARCHED with the reason given** — the framework's default for an unfillable peer
      cell is UNRESEARCHED, and departing from it required naming why no document exists.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      2026-09-18, US Treasury daily par yield curve, **struck fresh this run** via
      `python tools/sources.py` and not inherited.
- [x] **Value stated as a round-number range, not a point estimate.** ~$110 to $160 a share.
- [x] **One bar chosen, not both; windage count stated.** Bar 2, the screamer test. **Windage
      ZERO** on the price test, with the proof that none was needed (the un-normalised top of the
      band still misses the floor by 4.34 points).
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $229.55, 2026-09-18
      close, Yahoo Finance, flagged at Step 0 and again at the computation.
- [x] **Run committed to git**, in six commits with a pathspec each (template, Step 0, Q1, Q2,
      Q3, Q4, then this close and the fold).

**THINGS I GOT WRONG OR COULD NOT DO, recorded rather than smoothed:**
1. **[E3-70]'s grant-value measure of stock pay was not obtained.** No undimensioned grant-date
   total resolves for IBM in companyfacts. At 13.0% of operating cash flow SBC is under the
   50%-of-OCF threshold this project set for reading the grant table by hand, so the charge is used
   as the measure and named as the **floor** of the subtraction, not the measure.
2. **The TTM industrial construction could not be built.** IBM publishes the change in Financing
   receivables annually, in the MD&A free-cash-flow table, and not in the 10-Q. Left blank rather
   than estimated.
3. **The Kyndryl residual was not rebuilt from Kyndryl's own 10-K.** It could be attempted; the
   result would still be my subtraction rather than IBM's filed statement, and four clean years
   produced a band that does not straddle the decision. **If the answer had been close, this would
   have been the work order.**
4. **Segment-level (c) does not exist.** (c) is judged for the consolidated company; IBM discloses
   *"Depreciation/amortization of non-acquired intangibles"* by segment ($532M Software, $78M
   Consulting, $1,130M Infrastructure, $3M Financing in 2025) but no segment capex, so a
   franchise-only owner-earnings figure cannot be built.
5. **The mainframe complex's size ($19bn-$22bn) is my arithmetic, not IBM's disclosure**, and the
   run says so at Q1, Q2 and Q4 each time it is used.

---
## REGISTER
- Verdict: **[x] OUT (about the business)** — [ ] IN [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** **Q1 IN, Q2 OUT** — a genuine, unsubstitutable mainframe franchise over 28-33% of
  revenue, and for the other two thirds IBM's own Competition section names *"hundreds of
  competitors"*, *"regularly exposed to new competitors"* and price among its own methods of
  competition; **[E4-04]** excludes it because the position there is held by businesses bought and
  sold (four out, six in, five years) rather than by a defended advantage; the franchise legs are
  flat to shrinking (Transaction Processing +2.3% then −8%, Infrastructure Support −0.1%, IBM Z
  +51.7% then −42%) while the bought legs grow at $1.81 of acquisition cash per $1 of added annual
  revenue. **Price US$229.55 (2026-09-18), cap US$216,267M, sovereign USD 5.34%. FAIL.**
- **Computation, not a clearance:** owner earnings **$9,486M-$12,234M** across every window, both
  (c) ends and both financing constructions; judged centre $10.5bn; yield **4.39%-5.66%** against a
  **5.34%** sovereign, **−0.95 to +0.32 points**; the **~10% floor [E4-28] is missed by 4.3-5.6
  points at every end**; value roughly **$110-$160 a share** against a price of **$229.55**.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable. **This file is not short of any document
  it could have obtained.**
- **If UNKNOWABLE:** not the file's verdict. Two sub-questions are UNKNOWABLE and are named in the
  self-audit: the franchise leg's own profit and units, and the mainframe comparator set.
- **Survival shape (recorded at Q4, not governing):** **#10 THE CAMOUFLAGE**, with a proposed
  **feature** — the company sells the service that erodes its own franchise — offered to the
  operator and changing no register. Shapes #1, #2, #3, #4, #5 and #6 refused with arithmetic.
"""
s = s[:i] + new
io.open(p, 'w', encoding='utf-8').write(s)
print('audit written')
