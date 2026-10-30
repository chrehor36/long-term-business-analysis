# BRIEF - ECL Ecolab Inc. - WAVE 7, dispatched 2026-09-28 by the 13:46 overnight cycle

You are running ONE company through the purchase framework, unattended. The operator is asleep; nobody
will answer a question. Work in the repository at C:\Users\chreh\OneDrive\Documents\BRK.

## 0. Read first, in order
1. `CLAUDE.md` (the map), `Framework/OPERATOR-PROTOCOL.md` (binding), `Framework/THE FRAMEWORK v4.md` (governing),
   `Framework/v4/THE MANAGER STANDARD - Q3.md` (for Q3 if reached).
2. `Test Runs/_TEMPLATE - Company Run.md` (the enforcement surface).
3. `Screens/WATCHLIST RUN QUEUE.md`: the WAVE 7 section (line ~259), THE WRITE-EARLY PROTOCOL, CLAIM THE NAME AT
   DISPATCH, THE FOLD (six steps, including the dated note on writing the register entry BY LINE), WRITING A BRIEF.
4. The most recent finished runs, for the standard and the fold mechanics:
   `Test Runs/2026-09-28 Run - OII Oceaneering International.md`, `Test Runs/2026-09-28 Run - SANM Sanmina.md`,
   `Test Runs/2026-09-28 Run - MSA MSA Safety.md` (MSA reached Q5; the others closed at Q2). Their research
   folders (`Test Runs/_research 2026-09-28 OII/` etc.) hold reusable scripts (fetch, companyfacts, oe, peers,
   qcheck, fold). Adapt them; do not trust them blind (the SANM fold script, adapted from WING, appended WING
   to the done file).
5. `Screens/SURVIVAL SHAPES - index.md` (name the shape from it by number; a new shape is added at fold).

## 1. Write early, claim now
- FIRST action after reading: copy the template to `Test Runs/2026-09-28 Run - ECL Ecolab.md` and commit it
  (the claim). Then write each question as it closes and commit after each gate.
- Research, scripts and outputs go to `Test Runs/_research 2026-09-28 ECL/` (this folder; this brief is in it).
- COMMIT WITH A PATHSPEC ONLY: `git commit -F <msgfile> -- <paths>`. Never `git add X && git commit`.
  Write commit messages to a file. Bash heredocs containing apostrophes fail here: write scripts to files.
- Commit trailer (the operator's own prompt line, which takes precedence over the environment's default;
  use it and do not log it as an error): `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`
- Do not touch `Screens/_daily/_overnight.lock`; the dispatching cycle holds it.
- No helper agents. One agent, this one.

## 2. The screen row, UNLABELLED (from `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 160)
```
ticker,name,cap_m,oe_bottom_m,oe_top_m,spread,spread_dollars,cap_flag,deal_note,name_change_note,wc_note,yield_bottom,vs_sovereign,growth_required,level_shift,level_note,best_year_dep,best_year_note,level_shift_oe,level_note_oe,best_year_dep_oe,flags_disagree,level_shift_full,years_filed,window_disagree,acq_note,da_note,spread_caveat,newest_filing,newest_periodic
ECL,ECOLAB INC.,80452,1373,1665,0.212,"$1,373M to $1,665M",,"1 8-K Item 1.01 filing(s) since 2026-02-23, none carrying a merger agreement (EX-2.1) - most likely a credit facility or offering; open them only if something else is odd.",,,0.0171,-0.0364,0.0829,1.31,no step,0.036,no single-year dependence (9-yr OCF series),1.44,no step,0.042,,1.75,19,,,,4-construction width only (3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25],2025-12-31,2026-06-30
```
Every field is a claim to reproduce or refute, not a fact. Recent runs found cap_m stale by 9-14%, the yield
fields struck on the stale cap and a 5.35% bond, and "no single-year dependence (9-yr OCF series)" wrong on
both halves more than once. Record each screen field you check, and whether it reproduced, in the self-audit.

## 3. Step 0 inputs - strike them yourself
- Sovereign: strike it fresh from the US Treasury daily par yield curve, 30-year, dated (`tools/sources.py`
  `sovereign('USD')`). Do not inherit a figure from this brief or from another run.
- Price: re-strike it and flag the aggregator. **The market is open while you run (Monday 2026-09-28)**:
  `tools/sources.price` and `tools/run.py` have returned an intraday print as the day's price with no warning
  in four consecutive runs. Use the last CLOSE, record any intraday print as recorded-not-used.
- Share count: `python Screens/cover_shares.py ECL` returned, at dispatch, 280,328,603 common ($1.00 par),
  10-Q period 2026-06-30, filed 2026-08-06, accession 0001628280-26-053886. Re-run it, read the cover yourself,
  confirm there is one class and read the charter before summing anything. Ecolab CIK is 0000031462 (verify).
- Split-invariant cap per the protocol (`close`, never `adjclose`).
- `deal_note`: OPEN the Item 1.01 8-K(s) and say what they are. Also search for any Item 2.01, EX-2.1 or
  announced transaction since the last 10-K, in either direction (Ecolab as buyer, seller or target). A live
  merger makes the quote a spread, not an owner-earnings price (ROKU).
- SBC: verify it RESOLVES and is COMPLETE (BE's did not resolve; Boeing's stock-settled 401(k) sat under a tag
  no SBC element contains).

## 4. The priors - hypotheses to refute, not conclusions
Every brief so far has contained at least one error. Assume this one does too, and check each prior.
- Perimeter. My understanding, to verify from filings: Ecolab merged with Nalco (2011); acquired Champion
  Technologies (2013); separated its Upstream Energy business into ChampionX (2020, an exchange offer and
  Reverse Morris Trust with Apergy); sold its surgical solutions business (2024). If so, the 19 filed years
  of the screen straddle more than one perimeter, and a window that mixes them measures a company that is
  not the one priced. Establish from the filings which years are the priced perimeter.
- Q1: a large-scale seller of water treatment, cleaning, sanitising and pest-control programs delivered through
  a field sales-and-service force. Check against the 10-K segment note whether that description is right and
  complete.
- Q2: the filer reports pricing contribution in its MD&A and releases; that is exactly the series [E3-43]'s
  demonstration asks for, and it must be read as a series across the down years (2009, 2015-16, 2020), not in
  the inflation years alone. [E3-03]'s three conditions, [E2-58]'s commodity class and its wide-and-sustainable
  cost exception, and [E4-04]'s competence limit are the tests. Build a filed competitor row (candidates to
  check: Veolia's water technologies, Kurita, Solenis/Diversey, Rentokil, Diversey's own filings while it filed,
  ChampionX while it filed) and name the unobtainable rows. Write the strongest evidence against your verdict
  FIRST [E4-26, E3-41].
- Q3, if reached: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s third flag;
  read the proxy for what pay vests on ([E4-27] is the incentives row; [E4-52] is the lollapalooza row, NOT pay).
  Check the adjusted-EPS headline and any multi-year margin target.
- Q4, if reached: name the death from the survival-shapes index by number; debt, pensions and the separation
  structures (any tax indemnity) are the places to look.
- Owner earnings: rebuild the width over EVERY window (1 year to the longest the priced perimeter allows) and
  BOTH (c) ends [E2-09, E3-44]; report dollars and a word wherever the bottom sits near or below zero.
  **Known tool traps:** `run.py` averages each year's low and high capex ends, mixing ends across years;
  `run.py` strikes "growth the price assumes" against the bond, not the floor; the `DepreciationAndAmortization`
  tag has included goodwill impairment for another filer; acquired-intangible amortisation and any
  discontinued-operations cash must be handled explicitly. Owner earnings never via a net-income proxy
  (PRIME RULE 3's clause).
- Hard sequence: STOP at the first question not IN. UNRESEARCHED and UNKNOWABLE close the file. Any valuation
  before Q1-Q4 close is headed `COMPUTATION — NOT A CLEARANCE` and carries no entry language; a closed gate
  is not reopened by material beneath it [E2-37, E3-39].

## 5. The fold - the run does it, all six steps
1. Register entry in `## COMPLETED FROM THE QUEUE` (line-exact heading match, assert unique, insert as the
   FIRST entry like OII's, count the entries back before and after, from the file: 241 were counted at 13:07 by
   the previous cycle; count it yourself). Price, share count with cover accession, cap, sovereign, and the
   PASS/FAIL line naming the question that closed the file.
2. Append `ECL` to `Screens/_daily/_wave7_done.txt` (it has 99 lines ending OII; after, 100 lines equal to the
   order file's first 100). Search the WHOLE queue file for an ECL roster line to strike; record if none.
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, ending
   "Next in the order file: <the 101st line of `Screens/_daily/_wave7_order.txt`>."
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row ONLY if Q1-Q4 all cleared. A Q2 or Q3 or Q4 failure
   arms nothing and records the reversal condition in words.
5. Survival-shapes index: dated note or new shape as the precedent runs did.
6. `python tools/check_framework.py` must PASS before the fold commit. Pathspec commit.

Nothing about the framework changes: no ledger row, no edit to `Framework/`, no question added or removed.
Never present the framework as proven to beat the market. No em dashes in your own prose (quoted text and
the required `COMPUTATION — NOT A CLEARANCE` heading excepted). No git push, rebase, reset --hard or force.

## 6. What to return to the dispatcher
The verdict line (e.g. Q1 IN / Q2 OUT, with the reason in one sentence), price with date and source, share
count and accession, cap, sovereign with date, PASS/FAIL, every commit hash in order, the register count
before and after, the done-file line count, the next name, the screen errors found, tooling defects reported
not patched, your own errors, and any file left uncommitted.
