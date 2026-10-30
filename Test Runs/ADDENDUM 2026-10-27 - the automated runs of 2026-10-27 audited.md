# ADDENDUM 2026-10-27: the automated runs of 2026-10-27 audited

**Operator rule 6.** No run file is edited. This records the end-of-day audit of the runs folded today by the
unattended work-hours cycles (`BRK-audit`, written 2026-10-26 at the operator's word "Why don't we limit it to 10 runs a
day and have you audit them to verify them"). It follows the method of
`Test Runs/ADDENDUM 2026-10-23 - the overnight runs of 2026-10-18 to 2026-10-23 audited, six marked bad.md`.

**What was audited.** The six names folded today by a cycle, each with a line in `Screens/_daily/OVERNIGHT LOG.md` and a
register entry under a `### v5 RE-RUN BATCH overnight 2026-10-27` heading: VST, WEC, XEL, OGS (order key OGS-U), SWX
(SWX-U), SR (SR-U).

**Recorded, not audited: AQN.** `Test Runs/2026-10-27 Run - AQN Algonquin Power & Utilities.md` has only its template
commit (999f4088, 11:01). The 11:00 cycle ended at 11:04 "RATE LIMITED (exit 1)" (the session limit, which reset at
1pm), and the 11:30, 12:00 and 12:30 cycles ended the same way within seconds. Those four cycles counted toward the
daily cap of ten, so every cycle from 13:00 was skipped and AQN was not resumed today. The research folder has an
uncommitted `notes.md` and three untracked scripts; they are the dead cycle's and are left for the next cycle's rule A.
AQN is not in the register and binds nothing (`Test Runs/README - which run files are in force.md`).

## How they were checked
- **Mechanical, all six:** every run file committed and clean; every commit touching a run file or its research
  folder touched only those two paths, except the fold commit, which touches the Screens bookkeeping files and
  `tools/alerts.json` as the FOLD requires (XEL's fold, no alert, leaves the alert file and passers list alone);
  `python tools/check_framework.py` PASS; every ledger id in each run file resolves in `principle_ledger_v5.csv` (VST
  62 ids, WEC 130, XEL 91, OGS 90, SWX 101, SR 98, none missing); every quoted fragment beside an id was matched to the
  row by script (the id before or after the quote), and every fragment the script did not match was read by hand: each
  is a quotation of a filing, of the framework's own text, or a shelf quote with the right id placed before it, with one
  exception named under WEC; the alert follows the box (WEC, OGS, SWX and SR armed at the run's equity-only central
  fair price under Q7, The regulated utility; VST OUT at Q7 with no positive fair price on the all-equity basis and
  no alert, as BEP on 2026-10-18; XEL OUT at Q5, no alert); register entry, done-file line, narrative line and passers
  list agree with each run file's box (the five OUT at Q7 are on the passers list, XEL is not); each position note was
  filled at the fold ("not held"), and none of the six is in `PORTFOLIO.md`; no tracked research file over 200 KB.
- **By reading, three independent read-only auditors** (VST, XEL; WEC, OGS; SWX, SR): the hard sequence; the deciding
  part; Q7's basis and specifics (a) to (f), with the utility readings of 2026-10-23; every fair price and every
  computation beneath a stop recomputed from the run's own inputs and script, reproduced first; accession numbers on
  EDGAR; the price against the close; the sovereign at the issuing authority; the Q5 facts against the filings; the
  self-audit.
- **What every run got right:** every run's script reproduces its stated figures exactly; every accession checked
  exists for that company and form (twenty across the six); every price matches the close of 2026-10-26 to the cent
  (VST $141.73, WEC $111.12, XEL $77.86, OGS $78.36) or is a live print of 2026-10-27 inside that morning's trading
  (SWX $92.02 in the 10:00 bar, close $92.84; SR $85.37 in the 10:20 to 10:25 bars, close $86.05); the sovereign is the
  Treasury 30-year par yield of 5.31% on 2026-10-26 in every run; every template was committed before the first fetch;
  the Q5 facts behind XEL's integrity stop (the pre-tax gains of about $162M in 2025 on debt repurchases inside ongoing
  EPS, the 2025 guidance of $3.75 to $3.85 naming no such gain, ongoing EPS $3.80, the proxy's "When ongoing EPS is
  below guidance, awards will not be paid" and the 143.76% payout) are in the filings and concern the current chief
  executive; the Q5 and Q6 facts cited by the other five are in the filings.

**No box changes in any run. No run is BAD.** Four armed alerts rest on a reading the text does not fix and are
labelled FLAGGED.

## The verdicts
| run | box | verdict | the finding |
|---|---|---|---|
| VST | OUT at Q7 | GOOD, with slips | Retail decides and is not a regulated return, so the all-equity basis is central, as the text says for market-priced businesses; fair -$15.65, not positive, no alert. The central growth case uses 2023 growth spending from the FY2024 10-K ($698M) where the run's own rule takes the latest filing (FY2025 Note 21, $205M): central value $20.49, not $26.02, fair still not positive (-$18.59); no alert depends on it. Slips: `scripts/q7.py` and its output committed with Q1 (9e160df8) headed "COMPUTATION, Q7", not the operator rule 3 heading, not confessed; the box line "Re-look under an alert at the top of the computed range" with no alert armed; parts measured on segment net income; Q6 and Q7 in one commit (confessed) |
| WEC | OUT at Q7 | GOOD, ruling owed | $33.14 reproduced. The run took the WECI acquisitions (unregulated renewables) out of the growth spending the debt credit is set against, reading "unregulated renewables ... stay on the all-equity basis"; with the credit against all growth spending, as the fixed method of 2026-10-23 has it, the same inputs give **$35.85** (+8.2%), shown beside by the run and confessed. This is gap 5 of the 2026-10-23 audit (a mixed company), still unruled. Alert left at $33.14 and labelled FLAGGED. Slips: `q7.py` committed with Step 0 and Q1 (013659c5) without the operator rule 3 heading; the self-audit ticks "no other run file listed" while lines 15-16 declare a `Test Runs/` listing; the WECI capital spending left in while its acquisitions came out; a shelf quote of [L2000-035] ("we spend [...] simply to stay in the same economic place", line 258) carried without its id, next to [M2000-144]; Q2 to Q7 committed within six minutes |
| XEL | OUT at Q5 | GOOD, with slips | "Doubt closes the file" on filed facts about the current management, the same footing as PEG on 2026-10-26. The computation beneath the stop ($11.91 equity-only) reproduces and the amended utility paragraph gives the same figure. Slips: `q7_calc.py` committed with Q1 (7a099560) with a docstring reading "(file closed at Q5)" three minutes before Q5 was written, as TAC on 2026-10-26; the self-audit says the output was headed COMPUTATION, NOT A CLEARANCE, a heading added only in the Q2 commit; owner cash not recomputed at the statutory rate under "Whose tax" (confessed as a CONVENTION, the filing saying the utilities collect tax through rates) |
| OGS | OUT at Q7 | GOOD, ruling owed | $27.59 reproduced and equal to the fixed method of 2026-10-23 on the run's inputs (long-term debt credit $160.1M a year binding; cap 40.57%, Oklahoma and Texas weighted, not binding). Two readings the text does not fix move it: owner cash on book tax where WEC today added back deferred tax (about **$35.80**, +29.8%), and working capital set to zero across the Uri draw and recovery under (d) (about $17.34 with the residual charged; both together about $25.55). Alert left at $27.59 and labelled FLAGGED. Slips: `scripts/q7.py` committed with Step 0 and Q1 (8c985586) without the operator rule 3 heading, not confessed; Q3 and Q4 in one commit (confessed); a declared blind-rule listing, the box left unticked |
| SWX | OUT at Q7 | GOOD, ruling owed | Owner cash changes sign, so by (b) the range is the no-growth case alone, as CNP. The restatement (Item 4.02, 8-K 2026-01-09) and the material weakness, remediated by 2026-06-30, read at Q4 as weak accounting where visible and not a STOP: Q4 stops on confusion or suspicion the statements raise, and the run gives its reasons. $35.19 reproduced; it adds $211.6M of holding-company cash to the equity-only value, where the paragraph reads owner cash "against the market value of the shares" and names no cash: without it **$32.27** (-8.3%), confessed by the run as its gap 5. The auditor notes that on a strict reading of the 2% test this would be BAD; it is recorded as a reading the text does not address, as PPL on 2026-10-26, and the alert, labelled FLAGGED, can only fire early. Slips: `calc.py` committed with Q1 (fbfcb750) computing a fair figure, without the operator rule 3 heading; a declared `ls "Test Runs" \| grep SWX` listing; Q5 and Q6 in one commit (declared); an untracked `_fold_msg.txt` left in the research folder by the fold |
| SR | OUT at Q7 | GOOD, ruling owed | Sign change, so (b)'s no-growth case alone. $20.95 reproduced. Tennessee (bought 2026-03-31) and the Marketing and Storage sales (2026) adjusted on the equity-only basis by a stated convention; specific (c)'s "financing added to today's net debt" is an all-equity term and sales after the window are not addressed (the run's gaps 1 and 2). The literal window with no adjustment gives **$28.32** (+35%); Tennessee on its full financing $25.43; a six-year storm-cycle base under (a) $23.24. Cap at the business's own share (62.6%), correct where an allowed share is stated for under half the rate base. Alert left at $20.95 and labelled FLAGGED; it can only fire late. Slips: `q7.py` committed with Q1 (29cea66a) without the operator rule 3 heading; Q5, Q6 and a Q6 fix committed within eleven seconds, the Q5 commit sweeping in `draft_q6.md`, while the self-audit says each question was committed as it closed; the price called a live quote with no time. The register gives the Marketing sale as $215.0M (the 8-K/A agreed price), the 10-Q about $212M received |

## What was done
- **`tools/alerts.json`:** the WEC, OGS, SWX and SR alerts left at the run's figures and labelled `FLAGGED 2026-10-27`
  with the gap and the figure the other reading gives. No alert restated. VST and XEL have no alert.
- **Bookkeeping:** none needed. The register and narrative headings carry the order keys (OGS-U, SWX-U, SR-U) as the
  re-run order names them, and each entry names the ticker.
- Nothing about the framework, the template, the briefs or the prompts was changed.

## Gaps and recurring slips, for the operator
1. **The computation script committed with Step 0 or Q1, before the questions that precede Q7 close, without the
   operator rule 3 heading,** in all six runs today (and PEG, SO, TAC, UTL on 2026-10-26). XEL's script named the closing
   question before it was written. Gap 3 of the 2026-10-26 audit; the cycle prompt or the canonical brief may want a
   line on it, the operator's to decide.
2. **Which tax a regulated utility's owner cash carries** (book tax, deferred tax added back, or the statutory rate
   under "Whose tax"): WEC and OGS read it differently on the same day, and it moves OGS's fair price by about 30%.
3. **Gap 5 of 2026-10-23, the mixed company,** now decides an armed alert by more than 2% (WEC, +8.2%).
4. **Cash on the equity-only basis** (SWX, -8.3%): the paragraph does not say whether cash held is added to the value.
5. **Deals and sales after the window on the equity-only basis** (SR, up to +35%), beside gap 3 of 2026-10-23.
6. **Specific (a) for a business with no cycle, and (d) where an event's draw and recovery span several years** (XEL,
   OGS, SR); **preferred stock** and junior subordinated notes, which neither basis names (SR).
7. **The daily cap counts rate-limited cycles.** Four cycles ended within seconds on the session limit and used four
   of the ten starts, so no cycle ran after 13:00 and AQN was left at its template. Whether a rate-limited start should
   count is the operator's to decide (`Screens/_daily/_overnight.ps1`).
8. **Questions committed in quick succession** (WEC Q2 to Q7 in six minutes; SR Q5, Q6 and its fix in eleven seconds)
   suggest the file is written ahead of its commits; write-early is kept in form, not always in substance.
