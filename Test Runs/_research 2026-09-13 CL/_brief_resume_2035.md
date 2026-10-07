BRIEF: RESUME THE COLGATE-PALMOLIVE (CL) RUN FROM Q2, FINISH EVERY SECTION, DO THE FULL FOLD
Written by the overnight cycle of 2026-09-13 20:35 EDT. The operator is asleep. Nobody will answer a question.
Repository: C:\Users\chreh\OneDrive\Documents\BRK (Windows; Bash tool is Git Bash; python on PATH).

## 0. WHAT IS ON DISK, AND WHAT IS NOT
- Run file: `Test Runs/2026-09-13 Run - CL Colgate-Palmolive.md`. **Step 0 (`d4398ab`) and Q1 IN (`0c3de6e`) are committed.**
  The file ends at the Q1 verdict. **Q2, Q3, Q4, Q5, Q6, the self-audit and the register are not in it.** The session that wrote
  it stopped writing at 17:09 on 2026-09-13 (session limit); nothing has touched it since. You own it now.
- Research folder: `Test Runs/_research 2026-09-13 CL/`. Every 10-K FY2014-FY2025 (and the FY2017 10-K/A), the 2025-2026 10-Qs,
  three DEF 14As, 8-Ks since 2021 with their EX-99 earnings releases, companyfacts and submissions are already fetched as text.
  Do not refetch what is there.
- **DRAFTS LEFT BY THE KILLED SESSION, written OUT OF ORDER, before Q2 was closed.** Treat every one as an unverified input, never as
  a finding, and hunt in each for any line that presupposes a Q2 verdict (the BAM resume this morning removed two such lines, one a
  thin-evidence Q4 IN):
  - `sec_q3_draft.md`: a Q3 draft with `@@BANNER@@` and `@@DAILY@@` placeholders. Its leverage paragraph already speaks of *"a
    franchise's earning power"*, which is a Q2 conclusion written into Q3 before Q2 existed. Re-read every quote in it against the
    filing before any of it enters the run file.
  - `q2_subject.py` / `q2_subject_out.md`: a volume / price / FX decomposition by segment 2016-2025, transcribed from the 10-Ks.
    Spot-check at least three cells per segment against the filed tables before relying on it.
  - `oe.py` / `oe_out.md`: owner-earnings arithmetic. `q5.py` / `q5_out.md`: a value computation. **These were produced before Q1-Q4
    closed. Do not read `q5_out.md` until Q1-Q4 are recorded; when you do, re-derive it rather than adopt it.**
  - `peers/`: filings for PG, CLX, CHD, KMB, UL, HLN, KVUE, GIS, SJM, FRPT, with a manifest (`manifest_list.txt`), a grep helper
    `g.py`, a quote checker `s9_check_quotes.py`, and transcription briefs (`_brief_section_agents.txt`). **Only `SECTION_PG.md`
    and `SECTION_GIS.md` were finished.** CHD, KMB, UL, CLX, KVUE, HLN, FRPT and SJM have scratch scripts but no section. Finish or
    replace the competitor row yourself from the filings on disk (you may use sub-agents for transcription only, under that brief's
    no-judgment rules; they may not conclude). Competitors that are not SEC registrants (for example Nestle Purina, Mars, Reckitt,
    Henkel, Beiersdorf, private label) are named as such with what cannot be measured; never filled from memory.

## 1. READ FIRST, IN THIS ORDER
1. `CLAUDE.md`; `Framework/THE FRAMEWORK v4.md` in full (Q2 through Q6, and the self-audit); `Framework/v4/THE MANAGER STANDARD - Q3.md`.
   CL is not in `PORTFOLIO.md`, so this is a v4 purchase run, not a holding review.
2. `Test Runs/_TEMPLATE - Company Run.md` from the Q2 heading down; this is the surface you fill.
3. The run file as it stands (Step 0 and Q1).
4. For what a finished run and a finished fold look like: `Test Runs/2026-09-13 Run - NVDA NVIDIA.md` (Q2 onward) and the NVDA and
   AMZN entries at the top of `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md`.
5. In `Screens/WATCHLIST RUN QUEUE.md`: `## THE WRITE-EARLY PROTOCOL`, `## THE FOLD`, `## WRITING A BRIEF`, the WAVE 5 table and the
   two dated notes beside it (AMZN, NVDA) about the "capex unresolved" label.
6. `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` sections 2, 4, 5 and 9 (source limits already tested: do not
   re-attempt them; the incentives row is [E4-27], not [E4-52]).
7. `Screens/SURVIVAL SHAPES - index.md`.

## 2. THE WORK, IN THE HARD SEQUENCE
**Q2 first, fully, before any other gate is written.** Then:
- If Q2 is IN, continue to Q3, Q4 in order; stop at the first gate not IN (operator protocol 2). Q5 output may be reported only if
  Q1-Q4 all show IN.
- If any gate is not IN, the file closes there. Following the practice of every run in this register, Q3-Q6 are still written
  beneath the close under explicit "RECORDED, NOT GOVERNING" banners, and any valuation arithmetic is headed
  **COMPUTATION - NOT A CLEARANCE** and carries no entry language.
- Q6 records reopening conditions in words. Price bands in `tools/alerts.json` and a `PORTFOLIO.md` row are only for a name that
  clears all four business gates (the QLYS ruling).

**Write-early (mandatory).** Write each question into the run file the moment it closes and commit it before starting the next.
Commit with a fresh message file and a pathspec, never a bare commit (other sessions share the index):
`git commit -F "<fresh msg file>" -- "<path>" "<path>"`. `git add` your files by name first if they are untracked. End every
message with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Leave `Test Runs/_research 2026-09-13 ERIC/peers/OTHERS_row.md`
and every other file you did not write alone.

**Every judgment cites a ledger id that you have opened in `principle_ledger.csv` and checked says what you use it for.** No quote
from memory. If a Buffett or Munger passage bears on branded consumer goods, retailer bargaining power or pricing, search the
citation shelf on disk for it and cite it verbatim with year and source file, or do not use it. Q2 requires the competitor row.

## 3. EVIDENCE ALREADY GATHERED, BRIEFED AS HYPOTHESES TO REFUTE, NOT AS VERDICTS
These are priors pulled from the files on disk. Each has a case in both directions. Build both before deciding, and hunt hardest
against whichever you start to favour [E4-26]. Verify every figure against the filing before it enters the run file.
- **Toward a franchise:** the company reports its own global share of toothpaste at 41.3% and manual toothbrushes at 32.4% for 2025
  (Nielsen-based, with stated gaps in eCommerce and discounters). The killed session's decomposition shows total-company price +38.0
  points summed 2016-2025 against volume +7.7. Hill's sells a therapeutic range through veterinarians. Q1 recorded pre-tax operating
  returns on net tangible operating assets of 76.0%-98.5% in nine of ten years.
- **Against:** the same decomposition shows FX -20.4 points, so price plus FX in dollars summed about +17.6; whether pricing is
  pricing power ([E3-43], [E2-44](1), the See's test in [E4-37]) or recovery of devaluation in Argentina, Turkiye and Nigeria is the
  question. North America volume summed -9.3 over 2021-2025 while price summed +12.9. The 10-K names *"strong local competitors
  (including private label competition)"*, retailers *"some of which exercise greater bargaining strength than we do"*, Walmart at
  about 11% of sales, and *"AI-aided category pricing pressures"*. Advertising rose from 9.4% to 13.3% of sales per the Q1 section;
  whether that is investment or the cost of holding position is to be read, not assumed. The skin-health acquisitions were written
  down $2,211M in three charges.
- **Segments differ and may grade differently** (Oral Care, Personal Care, Home Care, Hill's; the 10-K and the 2026-03-17 recast 8-K
  give the segment and category splits). Test [E3-03] criterion 2 on each against the competitor row, and weigh them by profit.
- **Q3 companion rule:** read the latest 8-K EX-99 earnings releases (Colgate files them as exhibit 99 named like
  `q22026pressreleasetables.htm`; they are on disk as `EX_*` files) before scoring [E4-29] and [E4-22]'s third flag. What the pay
  plans vest on is [E4-27]. The DEF 14As are on disk.
- **Q4:** the Step 0 test found the "capex unresolved" label a tooling artefact (the tag changed; the capex line never left the face
  of the statement). The WAVE 5 note also asks for a check for missing early-year capex facts in companyfacts. **[E5-20] is a
  separate question, asked on the filing.** Step 0 left four open items for Q4: the perimeter (Venezuela deconsolidated at the end
  of 2015, so no window starts before 2016 without saying so; the Red Collar and Nutriamo plant purchases; Prime100, Filorga, EltaMD
  and PCA SKIN, hello); the ESOP expense tags that no SBC list reads; recurring restructuring cash (three Item 2.05 8-Ks in 2025-26)
  against [E2-57]; and hyperinflationary remeasurement inside net income. Also read the supplier finance note and pensions.
  Owner earnings never via a net-income proxy; (c) is a disclosed judgment. Name the survival shape against the index, or say none fits.
- **Q5, only if reached or as a computation:** re-confirm the sovereign from the US Treasury curve and the close yourself; Step 0 has
  USD 5.35% (09/11/2026), US$86.80 (2026-09-11, aggregator, flagged), 797,172,829 shares (10-Q cover `0000021665-26-000042`),
  cap US$69,194.6M. The ~10% floor [E4-28] comes first.

## 4. CLOSE THE RUN, THEN FOLD IT (all six steps; the run is not closed until they are done)
1. Self-audit section filled and checked; register line in the run file.
2. `python tools/check_framework.py` must PASS before the closing commit. If it fails, fix the cause and rerun it.
3. Entry at the TOP of `## COMPLETED FROM THE QUEUE` (newest-first, above NVDA), in the NVDA entry's form: the verdict line naming
   the question that closed the file, the commits, the price, the share count and its accession, the cap, the sovereign, and the
   pass/fail line. **Count the register from the heading line `## COMPLETED FROM THE QUEUE` to `## THE WRITE-EARLY PROTOCOL` (entries
   start `- **`); it should read 97 after your entry. Report the number you counted, not this one.**
4. Strike CL in the WAVE 5 table (`~~CL~~`), and leave a dated note beside the table (never edit the row) saying which kind of gap the
   label was for CL and what [E5-20] answered on the filing.
5. Narrative fold appended to `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`: findings, refuted priors, tooling defects.
   Add CL to `Screens/SURVIVAL SHAPES - index.md` as an instance of an existing shape or a proposed new one.
6. Commit the fold with a pathspec naming exactly the files you changed.
Do NOT write the overnight log line; the cycle that launched you writes it after checking your work.

## 5. STANDING RULES
- No em dashes in anything you write. Restructure the sentence. (The template's existing headings may keep theirs.)
- Verbatim only; flag extraction artefacts, never smooth them. Anything unsourced is labelled CONVENTION with a one-line rationale.
- If this brief states a fact the filing contradicts, the filing wins: correct it on the record and list it in your report.
- If you run long, keep committing section by section; a killed run under this protocol loses one question.

## 6. REPORT BACK (short)
Verdict line; which gate closed the file and on which ledger ids; price, share count and accession, cap, sovereign; every commit
hash with one line each; check_framework result; the register count you took at the fold; errors you found in this brief or in the
killed session's drafts; new tooling defects; anything left for the operator.
