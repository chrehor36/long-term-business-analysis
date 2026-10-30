# ADDENDUM 2026-10-26: the automated runs of 2026-10-26 audited

**Operator rule 6.** No run file is edited. This records the end-of-day audit of the runs folded today by the
unattended work-hours cycles (`BRK-audit`, written 2026-10-26 at the operator's word "Why don't we limit it to 10 runs a
day and have you audit them to verify them"). It follows the method of
`Test Runs/ADDENDUM 2026-10-23 - the overnight runs of 2026-10-18 to 2026-10-23 audited, six marked bad.md`.

**What was audited.** The seven names folded today by a cycle, each with a line in `Screens/_daily/OVERNIGHT LOG.md`
and a register entry under a `### v5 RE-RUN BATCH overnight 2026-10-26` heading: PPL, PEG, RWEOY, SO, TAC, UTL, VGNT.
The eight other run files dated today (ASML, PLTR, SNPS, and NRG, OGE, PAM, PCG, PNW) were run and folded by
interactive sessions this morning under their own batch headings, not by a cycle, and are outside this audit. No cycle
died mid-run today: every run file dated today has its register entry.

## How they were checked
- **Mechanical, all seven:** every run file committed and clean; every commit touching a run file or its research
  folder touched only those two paths, except the fold commit, which touches the Screens bookkeeping files and
  `tools/alerts.json` as the FOLD requires; `python tools/check_framework.py` PASS; every ledger id in each run file
  resolves in `principle_ledger_v5.csv` (PPL 73 ids, PEG 54, RWEOY 37, SO 74, TAC 36, UTL 72, VGNT 49, none missing);
  every quoted fragment beside an id was matched to its row by script, and every fragment the script did not match was
  read by hand and is a quotation of the filing or of the framework's own text, not of the ledger (no citation slip);
  the alert follows the box (PPL, SO and UTL armed at the run's equity-only central fair price under Q7, The regulated
  utility; PEG, RWEOY, TAC and VGNT not armed, their boxes not being OUT at Q7 or IN); register entry, done-file line,
  narrative line and passers list agree with each run file's box (the three OUT at Q7 are on the passers list, the four
  others are not); each position note was filled at the fold ("not held"), and none of the seven is in `PORTFOLIO.md`;
  no tracked research file over 200 KB.
- **By reading, three independent read-only auditors** (PPL, SO, UTL; PEG, TAC; RWEOY, VGNT): the hard sequence; the
  deciding part; Q7's basis and specifics (a) to (f), with the utility readings of 2026-10-23 as approved that day
  (long-term debt only, the credit against the growth spending only, the deciding part's cap, the company's own debt
  share where the filing states none); every fair price and every computation beneath a stop recomputed from the run's
  own inputs and script; accession numbers on EDGAR; the price against the close; the sovereign at the issuing
  authority; the Q5 facts against the filings; the self-audit.
- **What every run got right:** every run's arithmetic reproduces exactly from its own script; every accession checked
  exists for that company and form (over thirty across the six SEC filers); RWE's annual reports for 2024 and 2025 are on
  rwe.com and the figures the run used match them; every sovereign matches its issuing authority (Treasury 30-year par
  5.33% on 2026-10-23, Bank of Canada long benchmark 4.12% on 2026-10-23, ECB 30-year AAA 3.62% on 2026-10-23); every
  price matches the close or a labelled live quote within 0.2%; the Q5 facts behind PEG's integrity stop (the $6.6M FERC
  civil penalty in Note 12 of the FY2025 10-K, the "21st consecutive year" guidance release) and the Q5 facts cited by
  PPL, SO and UTL are in the filings.

**No box changes in any run. No run is BAD.**

## The verdicts
| run | box | verdict | the finding |
|---|---|---|---|
| PPL | OUT at Q7 | GOOD, ruling owed | $8.39 equity-only reproduced. The run began the debt-increase window at end-2021 because of the U.K. sale (gap 3 of the 2026-10-23 audit, still unruled) and confessed it; but the 2021 10-K restates end-2020 debt at $14,689M without the U.K. debt, so the confessed reason is loose, and on the literal five-year window the same inputs give about **$6.92** (-17.5%), the debt credit then below the cap. The run's figure is above, so the alert can only fire early. Alert left at $8.39 and labelled FLAGGED |
| PEG | OUT at Q5 | GOOD, with slips | Integrity doubt on the FERC penalty read with the guidance record is what Q5's text gives ("doubt closes the file"); the correction from Q5 IN to OUT (6f37af05 to 1bc49585) followed a new fact and came before Q6 (2641c3cc). Slips: `calc.py` committed with Step 0 and Q1 without the operator rule 3 heading; the violation's description rests on secondary sources, flagged by the run; holding-company debt share in the computation (gap 2, confessed, no alert) |
| RWEOY | OUT at Q2 | GOOD, with slips | Flexible Generation decides (38%). The price-taker ground alone would sit against Q2's commodity paragraph, but the low-bid and ordinary-returns OUT items carry the box, and the run states the conflict. Slips: ordinary returns measured on the whole company; the growth window includes the 2021 year the run calls aberrational; Q2 and Q7 committed 96 seconds apart |
| SO | OUT at Q7 | GOOD, with slips | $26.47 equity-only reproduced and the text gives the same (five-year window, Georgia Power's 44% allowed debt share, confessed for the whole part). Slips: the price $92.69 is labelled a close but was an intraday print (close $92.57, 0.13%); no template commit before the first fetch, Step 0 to Q2 in one commit (both confessed); `q7.py` committed with Q2, before Q3 and Q4 closed, without the operator rule 3 heading, not confessed |
| TAC | OUT at Q2 | GOOD, with slips | Gas decides and is a price-taker whose returns over the full Alberta cycle were ordinary (TAC 3.2%, Vistra 3.7%, NRG 5.7%): on Q2's OUT list. Slips: the deciding part is a near tie (Gas 36%, Hydro 35%) resting on a depreciation estimate labelled a CONVENTION, though the filer's own segment figures support Gas; `q7_computation.py` was committed with Step 0 and Q1 (eb2c9508) carrying the header "the file closed at Q2" two minutes before Q2 was committed (510ec446); a declared `Test Runs/` listing, nothing used. Bookkeeping: the register and narrative headings lacked the ticker (corrected, below) |
| UTL | OUT at Q7 | GOOD, with slips | $15.46 equity-only reproduced; gas decides (66.5%); cap 48%, not binding; the decline case under (b) and the post-window water deal handled as written. The maintenance guess is the plant depreciation provision, not full D&A (full D&A would give $9.91; gap 4, a defensible guess shown beside). Slips: no template commit, the first commit is Step 0 (the self-audit ticks "copied before any fetch" while listing the commits honestly); `q7.py` committed with Q3, before Q4 closed, without the operator rule 3 heading, not confessed |
| VGNT | OUT at Q2 | GOOD, with slips | Contractual price step-downs, termination for convenience, competition on price and excess capacity are Q2 OUT items, and the run argues why it is not TOO HARD. Every Versigent accession (the Form 10, both 10-Qs, five 8-Ks) and the Aptiv and Lear accessions confirmed. Slip: "no integrity fact found", while the run records adjusted operating income and adjusted EBITDA featured in place of GAAP, adding back restructuring that recurs every year, which Q5's text treats as integrity-bearing; recorded after the stop, the box does not turn on it |

## What was done
- **`tools/alerts.json`:** the PPL alert left at the run's $8.39 and labelled `FLAGGED 2026-10-26` with the gap and the
  literal-window figure of about $6.92. No alert restated; SO and UTL unchanged.
- **Bookkeeping corrected:** the TAC register heading in `Screens/WATCHLIST RUN QUEUE.md` read
  "### v5 RE-RUN BATCH overnight 2026-10-26, 2026-10-26" and the TAC narrative heading in
  `Screens/2026-08-31 PREPPED READING LIST (operator lists).md` read
  "## UPDATE 2026-10-26 - v5 RE-RUN BATCH overnight 2026-10-26 (v4.1 names run again under v5)"; the ticker was added to
  both, with a dated note on each line saying what it said before.
- Nothing about the framework, the template, the briefs or the prompts was changed.

## Gaps and recurring slips, for the operator
1. **Gap 3, the window after a sale of a part, now decides an armed alert by more than 2%** (PPL, about 17.5%), as it
   did for D and DTE. Where the filer restates the start of the window without the part sold, whether the literal
   five-year window then applies is the question to rule.
2. **The serial-acquirer rule asks for organic growth "as the filer reports it", and utilities report none.** PPL and
   UTL each built a figure of their own, confessed.
3. **The computation script committed before the questions that precede Q7 close, without the operator rule 3
   heading,** recurs (PEG, SO, TAC, UTL today; ED and DUK on 2026-10-23). The arithmetic is not presented as a clearance
   in any run file, but the committed script is. The cycle prompt or the canonical brief may want a line on it; that is
   the operator's to decide.
4. **The template commit before the first fetch** was skipped by SO and UTL (operator rules 1 and 10(a)).
5. **The fold left a heading without its ticker** (TAC), in both the register and the narrative; the batch file's label
   is the likely source, `tools/v5_rerun_fold.py` taking the heading from it.
