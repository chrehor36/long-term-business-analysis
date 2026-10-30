## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** Q7 closed the file OUT (operator rule 2). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** (Not asked by the operator for this run; no named business of Q12's list is involved.)

---
## THE BOX
**OUT at Q7**: no case of the range earns the floor at $5.25; the central range is **$(8.85) to $(6.85) a share** (the
organic pair; default pair $(10.04) to $(6.85); every case computed below zero) against $5.25 (close 2026-10-16, aggregator
flagged). Q1 IN; Q2 IN narrowly (the franchise stands; standing with regulators narrowed); Q3, Q4 and Q6 weigh against;
Q5 integrity IN, ability weighs against. Fair price (reporting figure, Part VII): $(8.95) all-equity, $(3.70)
equity-only; not positive. Re-look condition, as for any OUT: an alert at the top of the computed range, which is below
zero, so no price alert can be armed on this computation.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q8 (the bond).** The long Treasury yields 5.43% (Step 0). The most generous case at Q7 gives an expected return of
  3.28% at the price; FY2025's after-tax operating profit alone is 3.3% of the enterprise value (`q7_output.txt`).
- **Q9 (debt and exposures).** Net debt $6,580.7M at 2026-06-30 against shareholders' equity of $4,620.9M (Q2 2026 6-K).
  FY2025 operating profit before tax, Atlantica income out, $497.2M against interest expense of $282.5M: about 1.8
  times (Q7 table; FY2025 statement of operations). Principal due within twelve months of 2025-12-31: $1,577.9M,
  including the $1.15bn 5.365% notes due 2026-06-15 (AIF 2.1.2; XBRL maturity facts of the FY2025 40-F); in Q2 2026 the
  company raised $1,174.1M of long-term debt and repaid $1,164.1M (Q2 2026 cash-flow statement), so that maturity was
  refinanced. Ratings: issuer BBB at S&P, DBRS and Fitch; subordinated notes BB+ (AIF 3.10). The revolving facility at
  the parent was cut from $1.0bn to $750M in November 2025 (AIF 2.1.3). Cash is held near zero ($55.0M); the company
  depends on revolvers and a $1.0bn commercial paper program at Liberty Utilities (AIF 2.1.3). Exposures without an upper
  estimate: the Mountain View fire ($178.4M accrued; "cannot estimate the upper end", note 20(a)(i)); the Lexington gas
  explosion ($152.2M accrued against $149.0M insurance; "cannot currently estimate the upper end", note 20(a)(iii)); the
  Apple Valley condemnation (note 20(a)(ii)). The Q2 2026 release records a $17.2M write-off on the California proposed
  decision on wildfire cost recovery (6-K `0001174169-26-000031`, Exhibit 99.5). Seventeen regulators in diverse
  jurisdictions (MD&A risk) bear on L2005-019's point about diversity.
- **Q12.** Nothing found bearing on the named businesses.
- **Integrity facts (Q5 was answered IN; recorded here for any later run):** the regulators' motions to dismiss three
  rate cases and the NHPUC's order of an independent audit of the accounting information in a rate filing (MD&A FY2025);
  the 2023 performance units vesting at 107.4% of grant value with bottom-quartile shareholder return and a target
  rewritten after the sale (circular p. 67); the absence of any rate base or earned-ROE level in the filed documents read
  while the circular credits an increase in earned ROE (circular p. 52).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `d66c5c34`, before any EDGAR request); written question by
      question; committed after each (Step 0 to Q1 `dc148275`, Q2 `05b18056`, Q3 `7bdc5687`, Q4 `33da6e03`, Q5
      `68edfaad`, Q6 with Q7 `05f32a69`, as the brief directs for the buyback line).
- [x] Dispatched run: the brief allowed per-question pathspec commits; the lock and the fold are the dispatching
      session's (operator rule ten). This run is not in the register until the dispatcher folds it.
- [ ] **No other run file was opened, listed or searched: not clean.** Before the template was copied, one listing of
      `Test Runs/` filtered on today's date showed other runs' file names (AES, HOKCY, MDU, NJR, NWN, OGS, SR, SWX, UGI,
      XNGSY); no file was opened; declared at the top under CONTAMINATION and not used. The session's opening context
      also showed the AES run's commit subjects; declared, not used. No `PORTFOLIO.md`, holding review, resume-state
      file, queue file or reading list was opened. (Spire, whose run of today appeared in that listing, was not used as a
      comparable; Atmos was chosen instead.)
- [x] Every v5 id resolves (checked by `Test Runs/_research 2026-10-18 AQN/check_ids.py`, below); every filing fact
      carries its document or accession; numbers carry a filing or are labelled CONVENTION.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): built from segment operating
      results, the company's own tax, depreciation, the filer's sustaining spending, all spending beside, and working
      capital; the sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations, six items; Q2 tests 9 to 11); facts for
      later questions are under AFTER THE STOP.
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] `tools/run.py` printed only a failure line; nothing of it was used.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A divestiture inside the window.** Q7's specifics cover purchases (c) but not the sale of half the business: the
consolidated cash flows of FY2021 to FY2024 include the sold renewables business, and the framework says nothing on
whether the five-year base should be the whole company as it was or the continuing parts as they are. This run built the
base from the segment notes of the continuing parts and confessed two conventions to do it (hydro years, consolidated
working capital); a sentence in (c), "net of businesses sold", reads as if sale proceeds were negative capital spending,
which would credit $3bn of proceeds as owner cash and is absurd here. (2) **The maintenance guess when the filer
changes its definition.** The filer's "maintenance" was depreciation by definition until FY2024 and became a larger
"sustaining" figure in FY2025; (e) says "where the filing allows the guess" without saying what to do for the window's
earlier years. This run scaled depreciation by the two filed years' ratio, confessed. (3) **The regulated-return
exception at Q2 has no test of its own.** Q2 sends "a return set by a regulator" to Q3 as a second best, but does not say
how to judge a utility whose regulatory standing is narrowing (motions to dismiss, performance-conditioned increases)
while its franchise stands; this run closed Q2 IN narrowly and weighed the narrowing at Q3, Q5 and Q6, and a reader could
argue for TOO HARD. (4) **Preferred shares and minority interests in the all-equity basis.** The framework's all-equity
figure subtracts net debt only; here $184.3M of preferred and $356.3M of non-controlling interests also stand ahead of
the common, and the run deducted them, confessed in the Q7 claims line. (5) **Serial issuance** is still an unresolved
candidate STOP (Q6, section VI); this company is the case the row describes, and the run could only weigh it.

**CONVENTIONS of this run, collected:** the competitor choice (Q2); the hydro years and the consolidated working capital
in the Q7 base; the sustaining estimate for 2021 to 2023; total sales growth as the upper bound of organic growth;
preferred shares and non-controlling interests deducted as claims ahead of the common.
