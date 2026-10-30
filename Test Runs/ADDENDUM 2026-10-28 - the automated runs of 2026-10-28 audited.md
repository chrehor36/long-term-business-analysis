# ADDENDUM 2026-10-28: the automated runs of 2026-10-28 audited

**Operator rule 6.** No run file is edited. This records the end-of-day audit of the runs folded today by the
unattended work-hours cycles (`BRK-audit`, written 2026-10-26 at the operator's word "Why don't we limit it to 10 runs a
day and have you audit them to verify them"). It follows the method of
`Test Runs/ADDENDUM 2026-10-23 - the overnight runs of 2026-10-18 to 2026-10-23 audited, six marked bad.md` and the
readings of `Test Runs/ADDENDUM 2026-10-27 - the automated runs of 2026-10-27 audited.md`.

**What was audited.** The eight names folded today by a cycle, each with a line in `Screens/_daily/OVERNIGHT LOG.md` and
a register entry under a `### v5 RE-RUN BATCH overnight 2026-10-28` heading: AQN (order key AQN-U, the run file
`Test Runs/2026-10-27 Run - AQN Algonquin Power & Utilities.md`, left at its template by the rate-limited cycle of
2026-10-27 and resumed and finished today), AWK, AWR, CWT, WTRG, CWCO, SBS, GWRS.

**Not audited here.** CTAS and INOD have run files dated today but were run and folded by an interactive session at the
operator's request ("Run innodata and cintas"), not by a cycle. No cycle died mid-run today: the 11:01 CWCO line is a
skip on a fresh run file, and the 11:41 cycle resumed CWCO after Q4 from its own file.

## How they were checked
- **Mechanical, all eight:** every run file committed and clean; every commit touching a run file or its research
  folder touched only those two paths, except the fold commit, which touches the Screens bookkeeping files and
  `tools/alerts.json` as the FOLD requires (AQN's fold, no alert, leaves the alert file alone); `python
  tools/check_framework.py` PASS; every ledger id in each run file resolves in `principle_ledger_v5.csv` (AQN 66 ids,
  AWK 81, AWR 102, CWT 68, WTRG 83, CWCO 91, SBS 69, GWRS 71, none missing); every quoted fragment adjacent to an id was
  matched to the row by script, and the eighteen the script did not pair were read by hand: each is a shelf quote
  carrying its right id on the other side (the runs write the id after the quote), or a quotation of a filing (AQN's
  "Adjusted Net Earnings per common share"). No citation slip. The alert follows the box: seven OUT at Q7 armed at the
  run's central fair price (six equity-only under Q7, The regulated utility; CWCO all-equity, the paragraph judged not
  to apply); AQN OUT at Q7 with no positive fair price on either basis and no alert, as BEP on 2026-10-18 and VST on
  2026-10-27. Register entry, done-file line, narrative line and passers list agree with each run file's box (all eight
  OUT at Q7, all eight on the passers list); each position note was filled at the fold ("not held"), and none of the
  eight is in `PORTFOLIO.md`; no tracked research file over 200 KB. Untracked `_fold_msg.txt` files are left in the CWT
  and SBS research folders (the cycle's commit messages, as SWX on 2026-10-27); they are not committed and change
  nothing.
- **By reading, three independent read-only auditors** (AQN, AWK, WTRG; AWR, CWT, GWRS; CWCO, SBS): the hard sequence;
  the deciding part; Q7's basis and specifics (a) to (f), with the utility readings of 2026-10-23; every fair price
  recomputed from the run's own inputs and own script, reproduced first; accession numbers on EDGAR; the price against
  the close; the sovereign at the issuing authority; the Q5 facts against the filings; the self-audit.
- **What every run got right:** every run's script reproduces its stated figures exactly; every accession checked
  exists for that company and form (twenty-six across the eight); every price is the close of 2026-10-27 to the cent
  (AQN $5.42, AWK $141.10, AWR $85.48, CWT $47.82, SBSP3 R$25.53 with the ADS at US$4.75) or a live print of 2026-10-28
  inside that day's range (WTRG $42.45, CWCO $27.12, GWRS $7.74); the sovereign is the Treasury 30-year par yield of
  5.30% on 2026-10-27 in every dollar run (the 2026-10-28 curve was not yet published when the runs were made), and
  SBS's 14.93% is the Tesouro Nacional buying rate on the NTN-F 2037-01-01 for 2026-10-27; the Q5 facts each run's
  integrity and ability findings rest on are in the filings (proxies, 10-Ks, the AQN circular and MD&A, the SBS 20-F).

**No box changes in any run. No run is BAD.** On each run's own inputs the text of Q7, with the readings of 2026-10-23,
gives the run's own fair price, AQN excepted, where the text gives a different figure that is also not positive and on
which no alert depends. Every armed alert rests on at least one reading the text does not fix that moves it by more
than 2%, and all seven are labelled FLAGGED.

## The verdicts
| run | box | verdict | the finding |
|---|---|---|---|
| AQN | OUT at Q7, on the floor | GOOD, with slips | Regulated Services decides; equity-only central, correctly. -$1.65 equity-only reproduced. Q7 measures growth on owner cash; the run measured it on segment operating income, and on its own two-year base owner cash changes sign (-$267.2M FY2024 continuing, +$78.1M FY2025), so by (b) the range is the no-growth case alone: fair **-$1.23**, not -$1.65. Both are not positive and no alert depends on the difference, so it is recorded as VST was on 2026-10-27. Unarmed, correctly. Cap at the business's own share (57.1%, no rate base by utility in the filing; 55.0% with commercial paper out, immaterial). Slips: `q7.py` and its output ("floor cleared at price: False") committed with Q1 (a113d4bb) headed "(COMPUTATION)", not the operator rule 3 heading, confessed; Step 0 to Q7 in seven commits inside seven minutes; the debt window five years against a two-year base (the cap binds, immaterial) |
| AWK | OUT at Q7, on the floor | GOOD, ruling owed | $39.41 reproduced and equal to the text on the run's inputs (debt credit $919.6M a year, below both caps; the (f) cut to sales growth of 6.94%). Readings the text does not fix: the sale of Homeowner Services and New York inside the window, taken literally under (c) with the gain tax left in, **$40.40** (+2.5%, gap 3 of 2026-10-23); the span of "the filings read" in (f), on which the cut turns (27.9% against 27.0%), **$43.85** uncut (+11.3%, confessed); deferred tax charged, about **$28.78** (-27%, gap 2 of 2026-10-27). Alert FLAGGED. Slips: `value.py` with the fair price committed with Q1 (1d41c6a3) without the operator rule 3 heading, confessed and the box left unticked; Q2 to Q4 within 67 seconds |
| AWR | OUT at Q7, on the floor | GOOD, ruling owed | $23.67 reproduced and equal to the text (long-term debt credit $70.01M a year, the 43% cap binding at $64.50M; growth cut under (f) to 7.17% and capped at 5.30%). Readings the text does not fix: developer advances and contributions added to owner cash (left out **$21.76**, -8.1%; netted from growth spending as CWT did, **$22.11**, -6.6%); cash tax used, deferred tax charged gives **$22.64** (-4.4%). The alert can only fire early. Alert FLAGGED. Slips: `q7.py` committed with Q5 and Q6 (bfa34136), after Q1 to Q4 closed, without a heading; Q2 with Q3 and Q5 with Q6 in combined commits while the self-audit ticks "committed after each" (line 517); ASUS (contracted, about 15%) kept on the equity-only basis (gap 5 of 2026-10-23, minor) |
| CWT | OUT at Q7, on the floor | GOOD, ruling owed | $9.43 reproduced; cap 46.6% is Cal Water's stated share on the deciding part, credit $119.6M; 6.34% growth passes (f). Readings the text does not fix: deferred tax charged centrally (on cash tax **$17.01**, +80%; gap 2 of 2026-10-27, which AWR read the other way today); developer funds netted from growth spending (AWR's reading **$13.20**, +40%). On cash tax with developer funds in the base the growth case at the sovereign exceeds the price, so "above the top of the range on every basis" (line 349) holds only on the run's readings; the box stands, the floor being failed on every reading ($23.10 and $18.90 at ten percent). The alert can only fire late. Alert FLAGGED. Slips: commit 2628f9d6 ("Q2 IN") also committed `owner_cash.py` with the whole range and fair price and a `part2.md` holding Q2 to Q7 and the box, before Q3 and Q4 were in the run file, without the operator rule 3 heading; Q2 to Q6 in five commits in one second (09:43:24); the self-audit's "order was kept" (lines 405-413) overstates this, partly confessed |
| WTRG | OUT at Q7, on the floor | GOOD, ruling owed | $13.00 reproduced; credit $396.7M a year under the 53.67% own-share cap, correctly (the 10-K states no allowed capital structure). The $385M revolver at 2020 (due 2023) counted as long-term debt while the 2025 commercial paper is out; read literally that stands, and with the revolver treated as short-term bank borrowing, as AQN treated its revolver today, **$13.95** (+7.3%), shown beside by the run. The alert can only fire late. Alert FLAGGED. Slips: **unconfessed**, `value.py` and its output, already carrying the $13.00 fair price and the floor returns, committed with Q3 and Q4 (2131e8d0), before Q5 and Q6, without the operator rule 3 heading; Q7, the box and the self-audit in one commit where the self-audit says "the next commit"; a declared `Test Runs/` listing showing the AWK run's name |
| CWCO | OUT at Q7, on price, inside the range | GOOD, with slips | The regulated-utility paragraph correctly judged not to apply: the licence gives "a fair and reasonable profit margin on its sales" under a rate cap, no allowed return on invested capital, and the company has no long-term debt. $24.85 all-equity reproduced; (f)'s "inside the ten years the shown rate is the cap" gives 14.8%, and the share-of-sales test does not cut it. Readings the text does not fix: growth measured on owner cash after purchases (17.1%), **$27.03** (+8.8%); the general sentence "no rate that runs past the discount rate" read inside the ten years, **$18.77** (-24.5%). Alert FLAGGED. The Q3 citation corrected in place by the resuming cycle (f18938ac edits a line committed in a7e8fb89: [M1998-081] to the right [M1994-081]) is dated in the file, declared in the self-audit and in the log, and right against the ledger; no verdict moved. Slips: `value.py` computing the range and fair price committed with Q1 (2ebc5d2c) without the operator rule 3 heading, not confessed; `value2.py` (with Q5 and Q6) made $18.77 central and `value3.py` reversed it, the choice changed after both figures were seen; Q2 to Q4 within 2.5 minutes from drafts, the self-audit still ticking "committed after each"; Q5 says the adverse controls opinion reached owners "through an 8-K" where it was first in the FY2024 10-K |
| SBS | OUT at Q7, on price, above the range | GOOD, ruling owed | R$8.67 reproduced and equal to the text (credit R$2,292M at the business's own 54.8% share, the 20-F stating no allowed debt share; growth spending grown and stopped at year ten). The fair price lies **above** the value range (R$4.94 to R$5.21) because the range is discounted at the 14.93% sovereign and the fair price, by its definition, at ten percent: mechanically consistent, but a firing at R$8.67 would find a price Q7 closes OUT again. At the higher of the floor and the sovereign, about **R$5.07** (-41.5%). A window across the 2024 privatization is a further unruled reading (post-privatization bases about R$18.54 and R$19.88). The box line "on price" would be more exact as "on the floor" (no case earns the floor); same box. Alert FLAGGED. Slips: Q1 and Q2 in one commit, Q3 to Q7 with the box and self-audit in one (the run took sixteen minutes); `owner_cash.py` run before Q4 was written, without the heading, confessed; the first self-audit's "committed after each" corrected seven seconds later (643c3a8a) |
| GWRS | OUT at Q7, on the floor | GOOD, ruling owed | $1.07 reproduced; credit is the debt increase, $3,975K, the 45% cap not binding. Readings the text does not fix: the Buckeye premiums valued apart as a nine-year stream (a confessed convention); left inside owner cash and the growth series, **$0.86** (-19.6%); (e) at a negative growth rate (growth spending held flat gives a figure not positive); the regulated paragraph where the allowed return is not earned (about 4% earned against 9.6% allowed, as KEP); the placement shares counted without their cash, **$1.11** on the cover count (+3.9%). The alert can only fire early. Alert FLAGGED. Slips: `q7_calc.py` committed with Q1 (976b9645) without the heading, confessed; Q2 to Q4 within 77 seconds; the self-audit says the acceptance-test result is "recorded in the reply", which is in neither the file nor the commit; finance leases in the 2025 debt figure but not the 2020 base (under 1%) |

## What was done
- **`tools/alerts.json`:** the AWK, AWR, CWT, WTRG, CWCO, SBS and GWRS alerts left at the run's figures and labelled
  `FLAGGED 2026-10-28` with the reading and the figure the other reading gives. No alert restated. AQN has no alert.
- **Bookkeeping:** none needed. The register and narrative headings carry the order key AQN-U as the re-run order
  names it; the entry names the ticker.
- Nothing about the framework, the template, the briefs or the prompts was changed.

## Gaps and recurring slips, for the operator
1. **The computation script committed before the questions that precede Q7 close, without the operator rule 3
   heading,** in seven of the eight runs today (WTRG and CWCO unconfessed; CWT's commit also carried a draft of every
   question to the box). Gap 1 of 2026-10-27, now in every cycle run of three days.
2. **Which tax a regulated utility's owner cash carries** (gap 2 of 2026-10-27): AWR took cash tax and CWT charged
   deferred tax on the same day; it moves CWT by 80% and AWK by about 27%.
3. **Developer advances and contributions at a water utility:** AWR added them to owner cash, CWT netted them from
   growth spending, GWRS left them out of both. It moves AWR by up to 8% and CWT by 40%.
4. **The fair price when the sovereign is above the ten percent floor** (SBS): the fair price is discounted at ten
   percent and lands above the value range; whether it should use the higher of the two (about 41% lower).
5. **A window across a sale of a part or a change of regime** (gap 3 of 2026-10-23): AWK's divestitures, AQN's
   renewables sale, SBS's privatization.
6. **The maintenance guess where the filer states "sustaining" capital** (AQN used it, AWK and WTRG depreciation; for AQN
   it turns a negative fair price positive), and depreciation as maintenance under IFRIC 12 (SBS).
7. **Revolver drawings in the debt credit** (WTRG, +7.3%): long-term by maturity, or bank borrowing left out with
   commercial paper.
8. **The span of "the filings read" in (f)** (AWK, +11.3%), and the general sentence on the discount rate against (f)'s
   "inside the ten years the shown rate is the cap" (CWCO, -24.5%).
9. **(e) at a negative growth rate; the regulated paragraph where the allowed return is not earned; non-utility income
   that ends inside ten years; shares issued after the cover counted without their cash** (GWRS).
10. **No alert rule for a utility whose central fair price is not positive** (AQN), as for BEP and VST.
11. **Questions committed in quick succession** in every run (CWT five in one second; SBS Q3 to the self-audit in one
    commit): write-early kept in form, not in substance, as on 2026-10-27.
