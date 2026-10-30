# BRIEF - CLB Core Laboratories Inc. - WAVE 7, dispatched 2026-09-28 by the 14:46 overnight cycle

You are running ONE company through the purchase framework, unattended. The operator is asleep; nobody
will answer a question. Work in the repository at C:\Users\chreh\OneDrive\Documents\BRK.

## 0. Read first, in order
1. `CLAUDE.md` (the map), `Framework/OPERATOR-PROTOCOL.md` (binding), `Framework/THE FRAMEWORK v4.md` (governing),
   `Framework/v4/THE MANAGER STANDARD - Q3.md` (for Q3 if reached).
2. `Test Runs/_TEMPLATE - Company Run.md` (the enforcement surface).
3. `Screens/WATCHLIST RUN QUEUE.md`: the WAVE 7 section (line ~259), THE WRITE-EARLY PROTOCOL, CLAIM THE NAME AT
   DISPATCH, THE FOLD (six steps, including the dated note on writing the register entry BY LINE), WRITING A BRIEF.
4. The most recent finished runs, for the standard and the fold mechanics:
   `Test Runs/2026-09-28 Run - ECL Ecolab.md` (reached Q5; bands armed), `Test Runs/2026-09-28 Run - OII Oceaneering International.md`
   and `Test Runs/2026-09-28 Run - SANM Sanmina.md` (both closed at Q2). Their research folders
   (`Test Runs/_research 2026-09-28 ECL/`, `... OII/`, `... SANM/`) hold reusable scripts (fetch, companyfacts,
   oe, peers, qcheck, fold). Adapt them; do not trust them blind (the SANM fold script, adapted from WING,
   appended WING to the done file; check every hard-coded ticker, count and "next" name in anything you copy).
5. `Screens/SURVIVAL SHAPES - index.md` (name the shape from it by number; a new shape is added at fold).

## 1. Write early, claim now
- FIRST action after reading: copy the template to `Test Runs/2026-09-28 Run - CLB Core Laboratories.md` and
  commit it (the claim). Then write each question as it closes and commit after each gate.
- Research, scripts and outputs go to `Test Runs/_research 2026-09-28 CLB/` (this folder; this brief is in it).
- COMMIT WITH A PATHSPEC ONLY: `git commit -F <msgfile> -- <paths>`. Never `git add X && git commit`.
  Write commit messages to a file. Bash heredocs containing apostrophes fail here: write scripts to files.
  A new untracked file needs `git add -- <that path>` before a pathspec commit can carry it; never add an
  ignored path, and check `git diff --cached --name-only` is exactly your paths before committing.
- Commit trailer (the operator's own prompt line, which takes precedence over the environment's default;
  use it and do not log it as an error): `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`
- Do not touch `Screens/_daily/_overnight.lock`; the dispatching cycle holds it.
- No helper agents. One agent, this one.

## 2. The screen row, UNLABELLED (from `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 163)
```
ticker,name,cap_m,oe_bottom_m,oe_top_m,spread,spread_dollars,cap_flag,deal_note,name_change_note,wc_note,yield_bottom,vs_sovereign,growth_required,level_shift,level_note,best_year_dep,best_year_note,level_shift_oe,level_note_oe,best_year_dep_oe,flags_disagree,level_shift_full,years_filed,window_disagree,acq_note,da_note,spread_caveat,newest_filing,newest_periodic
CLB,Core Laboratories Inc. /DE/,567,9,20,1.117,$9M to $20M,,,,"ONE LINE MADE THE CASH: AccountsPayable moved 62% of 2022 OCF. Operating cash is not owner earnings when one balance-sheet line produced it (DELL, INOD). Read the 2022 cash-flow statement and liquidity note.",0.0166,-0.0369,0.0834,1.28,no step,0.142,one year is doing heavy lifting - check it (9-yr OCF series),3.64,STEP UP - normalize down [E4-41],0.471,,1.28,5,,,,4-construction width only (3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25],2025-12-31,2026-06-30
```
Every field is a claim to reproduce or refute, not a fact. Recent runs found cap_m stale by 3-14%, the yield
fields struck on the stale cap and a 5.35% bond, the `wc_note` reading the sign of a working-capital line
backwards (SANM) or quoting a gross roll-forward line (OII), and "9-yr OCF series" wrong more than once.
Note `years_filed` is 5 here: see the perimeter prior below before trusting any window length. Record each
screen field you check, and whether it reproduced, in the self-audit.

## 3. Step 0 inputs - strike them yourself
- Sovereign: strike it fresh from the US Treasury daily par yield curve, 30-year, dated (`tools/sources.py`
  `sovereign('USD')`). Do not inherit a figure from this brief or from another run.
- Price: re-strike it and flag the aggregator. **The market is open while you run (Monday 2026-09-28)**:
  `tools/sources.price` and `tools/run.py` have returned an intraday print as the day's price with no warning
  in five consecutive runs. Use the last CLOSE, check `regularMarketTime`, record any intraday print as
  recorded-not-used.
- Share count: `python Screens/cover_shares.py CLB` returned, at dispatch, 45,884,542 (single class /
  undimensioned), 10-Q period 2026-06-30, filed 2026-07-30, accession 0001193125-26-326345. Re-run it, read the
  cover yourself, confirm there is one class and read the charter (authorized preferred, any issued) before
  summing anything. `tools/sources.cik_for('CLB')` returns CIK 0001958086, "Core Laboratories Inc. /DE/" (verify).
- Split-invariant cap per the protocol (`close`, never `adjclose`).
- `deal_note` is blank in the row, and blank has been wrong before (SANM's ZT Systems, ECL's CoolIT, neither
  with an EX-2.1). Search the 8-Ks since the last 10-K for Items 1.01, 2.01, 8.01 and any EX-2.1, in either
  direction (buyer, seller or target), and say what each is. A live merger makes the quote a spread, not an
  owner-earnings price (ROKU). `sources.deal_note(cik)` printed nothing at dispatch: run it by hand.
- SBC: verify it RESOLVES and is COMPLETE (BE's did not resolve; Boeing's stock-settled 401(k) sat under a tag
  no SBC element contains).

## 4. The priors - hypotheses to refute, not conclusions
Every brief so far has contained at least one error. Assume this one does too, and check each prior.
- Perimeter and registrant. My understanding, to verify from filings: the "/DE/" registrant (CIK 0001958086)
  is the product of a 2023 redomestication of Core Laboratories N.V. (a Netherlands company, a separate
  earlier CIK; find it and verify) into a Delaware corporation. If so, the new CIK's companyfacts will carry
  only the years since, which may be why `years_filed` is 5, and the long record sits under the predecessor's
  CIK in its 10-Ks. Establish (a) whether the redomestication changed the business perimeter or only the
  domicile, (b) what businesses were sold, exited or bought across the record (I believe some were divested
  around 2019-2021; verify, do not assume), and (c) which filed years measure the company that is priced.
  A window that mixes perimeters measures a company that is not the one priced.
- Q1: an oilfield-services firm selling laboratory analysis of rock and reservoir fluid samples (reservoir
  description) and products and services that improve well completions (production enhancement). Check
  against the 10-K segment note whether that description is right and complete, and how revenue splits
  between services and products.
- Q2: test it with [E3-03]'s three conditions, [E2-58]'s commodity class and its wide-and-sustainable cost
  exception, [E3-43]'s pricing demonstration read as a series across the down years (2009, 2015-2016, 2020
  are candidates; the filings say which), and [E4-04]'s competence limit. Build a filed competitor row from
  SEC filers where the segment is comparable (and name the unobtainable rows: private labs, the laboratory
  lines inside the large service companies that do not report them separately). Record the long-run return on
  tangible capital as the filings show it, whatever it shows. Write the strongest evidence against your
  verdict FIRST [E4-26, E3-41].
- Q3, if reached: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s third flag;
  read the proxy for what pay vests on ([E4-27] is the incentives row; [E4-52] is the lollapalooza row, NOT pay).
  The capital-return record across the cycle (dividends, buybacks and their prices against value) is a Q3 read.
- Q4, if reached: name the death from the survival-shapes index by number; debt maturities, covenants and
  the tax consequences of the redomestication are places to look.
- Owner earnings: rebuild the width over EVERY window (1 year to the longest the priced perimeter allows,
  across both CIKs where the perimeter is the same) and BOTH (c) ends [E2-09, E3-44]; report dollars and a
  word wherever the bottom sits near or below zero. The row's `level_note_oe` cites [E4-41] and `spread_caveat`
  cites [E4-25]: check both claims against the numbers.
  **Known tool traps:** `run.py` averages each year's low and high capex ends, mixing ends across years;
  `run.py` strikes "growth the price assumes" against the bond, not the floor; the `DepreciationAndAmortization`
  tag has included goodwill impairment for another filer (OII); acquired-intangible amortisation and any
  discontinued-operations cash must be handled explicitly (ECL); `run.py` reads one CIK only. Owner earnings
  never via a net-income proxy (PRIME RULE 3's clause).
- Hard sequence: STOP at the first question not IN. UNRESEARCHED and UNKNOWABLE close the file. Any valuation
  before Q1-Q4 close is headed `COMPUTATION — NOT A CLEARANCE` and carries no entry language; a closed gate
  is not reopened by material beneath it [E2-37, E3-39].

## 5. The fold - the run does it, all six steps
1. Register entry in `## COMPLETED FROM THE QUEUE` (line-exact heading match, assert unique, insert as the
   FIRST entry like ECL's, count the entries back before and after, from the file: 242 were counted at 14:46
   by this dispatcher, entries being the lines beginning `- **` inside the slice to `## THE WRITE-EARLY PROTOCOL`;
   count it yourself). Price, share count with cover accession, cap, sovereign, and the PASS/FAIL line naming
   the question that closed the file.
2. Append `CLB` to `Screens/_daily/_wave7_done.txt` (it has 100 lines ending ECL; after, 101 lines equal to the
   order file's first 101, compared ignoring line endings). Search the WHOLE queue file for a CLB roster line
   to strike; record if none.
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, ending
   "Next in the order file: <the 102nd line of `Screens/_daily/_wave7_order.txt`>." (read it yourself).
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
