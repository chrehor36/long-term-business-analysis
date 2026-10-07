# BRIEF - KEYS Keysight Technologies, Inc. - WAVE 7, dispatched 2026-09-28 by the 15:46 overnight cycle

You are running ONE company through the purchase framework, unattended. The operator is asleep; nobody
will answer a question. Work in the repository at C:\Users\chreh\OneDrive\Documents\BRK.

## 0. Read first, in order
1. `CLAUDE.md` (the map), `Framework/OPERATOR-PROTOCOL.md` (binding), `Framework/THE FRAMEWORK v4.md` (governing),
   `Framework/v4/THE MANAGER STANDARD - Q3.md` (for Q3 if reached).
2. `Test Runs/_TEMPLATE - Company Run.md` (the enforcement surface).
3. `Screens/WATCHLIST RUN QUEUE.md`: the WAVE 7 section (line ~259), THE WRITE-EARLY PROTOCOL, CLAIM THE NAME AT
   DISPATCH, THE FOLD (six steps, including the dated note on writing the register entry BY LINE), WRITING A BRIEF.
4. The most recent finished runs, for the standard and the fold mechanics:
   `Test Runs/2026-09-28 Run - ECL Ecolab.md` (reached Q5; bands armed), `Test Runs/2026-09-28 Run - CLB Core Laboratories.md`
   and `Test Runs/2026-09-28 Run - SANM Sanmina.md` (both closed at Q2). Their research folders
   (`Test Runs/_research 2026-09-28 ECL/`, `... CLB/`, `... SANM/`) hold reusable scripts (fetch, companyfacts,
   oe, peers, qcheck, fold). Adapt them; do not trust them blind (the SANM fold script, adapted from WING,
   appended WING to the done file; check every hard-coded ticker, count and "next" name in anything you copy).
5. `Screens/SURVIVAL SHAPES - index.md` (name the shape from it by number; a new shape is added at fold).

## 1. Write early, claim now
- FIRST action after reading: copy the template to `Test Runs/2026-09-28 Run - KEYS Keysight Technologies.md` and
  commit it (the claim). Then write each question as it closes and commit after each gate.
- Research, scripts and outputs go to `Test Runs/_research 2026-09-28 KEYS/` (this folder; this brief is in it).
- COMMIT WITH A PATHSPEC ONLY: `git commit -F <msgfile> -- <paths>`. Never `git add X && git commit`.
  Write commit messages to a file. Bash heredocs containing apostrophes fail here: write scripts to files.
  A new untracked file needs `git add -- <that path>` before a pathspec commit can carry it; never add an
  ignored path, and check `git diff --cached --name-only` is exactly your paths before committing.
- Commit trailer (the operator's own prompt line, which takes precedence over the environment's default;
  use it and do not log it as an error): `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`
- Do not touch `Screens/_daily/_overnight.lock`; the dispatching cycle holds it.
- No helper agents. One agent, this one.

## 2. The screen row, UNLABELLED (from `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 167)
```
ticker,name,cap_m,oe_bottom_m,oe_top_m,spread,spread_dollars,cap_flag,deal_note,name_change_note,wc_note,yield_bottom,vs_sovereign,growth_required,level_shift,level_note,best_year_dep,best_year_note,level_shift_oe,level_note_oe,best_year_dep_oe,flags_disagree,level_shift_full,years_filed,window_disagree,acq_note,da_note,spread_caveat,newest_filing,newest_periodic
KEYS,"Keysight Technologies, Inc.",54543,879,978,0.112,$879M to $978M,,,,"ONE LINE MADE THE CASH: ContractWithCustomerLiability moved 50% of 2024 OCF. Operating cash is not owner earnings when one balance-sheet line produced it (DELL, INOD). Read the 2024 cash-flow statement and liquidity note.",0.0161,-0.0374,0.0839,1.44,no step,0.047,no single-year dependence (9-yr OCF series),1.45,no step,0.053,,1.77,13,,"acquisitions are $2,999M, 5% of cap, inside the window.",,4-construction width only (3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25],2025-10-31,2026-04-30
```
Every field is a claim to reproduce or refute, not a fact. Recent runs found cap_m stale by 3-19%, the yield
fields struck on the stale cap and a 5.35% bond, the `wc_note` reading the sign of a working-capital line
backwards (SANM, CLB) or quoting a gross roll-forward line (OII), "9-yr OCF series" wrong more than once, and
acquisition notes that missed purchases made after the screen's data (ECL). Note `newest_periodic` is 2026-04-30:
a later 10-Q exists (below). Record each screen field you check, and whether it reproduced, in the self-audit.

## 3. Step 0 inputs - strike them yourself
- Sovereign: strike it fresh from the US Treasury daily par yield curve, 30-year, dated (`tools/sources.py`
  `sovereign('USD')`). Do not inherit a figure from this brief or from another run.
- Price: re-strike it and flag the aggregator. **The market is open while you run (Monday 2026-09-28)**:
  `tools/sources.price` and `tools/run.py` have returned an intraday print as the day's price with no warning
  in six consecutive runs. Use the last CLOSE, check `regularMarketTime`, record any intraday print as
  recorded-not-used.
- Share count: `python Screens/cover_shares.py KEYS` returned, at dispatch, 170,244,745 (Common Stock, par $0.01),
  10-Q period 2026-07-31, filed 2026-09-02, accession 0001601046-26-000036. Re-run it, read the cover yourself,
  confirm there is one class and read the charter (authorized preferred, any issued) before summing anything.
  `tools/sources.cik_for('KEYS')` returns CIK 0001601046, "Keysight Technologies, Inc." (verify).
- Split-invariant cap per the protocol (`close`, never `adjclose`).
- `deal_note` is blank in the row, and blank has been wrong before (SANM's ZT Systems, ECL's CoolIT, neither
  with an EX-2.1). Search the 8-Ks since the last 10-K for Items 1.01, 2.01, 8.01 and any EX-2.1, in either
  direction (buyer, seller or target), and say what each is. A live merger makes the quote a spread, not an
  owner-earnings price (ROKU). Run `sources.deal_note(cik)` by hand as well.
- SBC: verify it RESOLVES and is COMPLETE (BE's did not resolve; Boeing's stock-settled 401(k) sat under a tag
  no SBC element contains). Check for any stock-settled employee plan outside the SBC element.

## 4. The priors - hypotheses to refute, not conclusions
Every brief so far has contained at least one error. Assume this one does too, and check each prior.
- Perimeter and registrant. My understanding, to verify from filings: Keysight was separated from Agilent
  Technologies (the electronic measurement business) in a spin completed around November 2014, with a fiscal
  year ending October 31, so the registrant's own 10-Ks begin with FY2014 and the Form 10 carries carve-out
  history before that. Since then it has bought other businesses (Ixia in 2017 is one I believe was large;
  a 2025 purchase of Spirent Communications is another I believe closed; verify both, their dates, prices and
  what else was bought or sold). Establish which filed years measure the company that is priced; a window that
  mixes perimeters measures a company that is not the one priced. The row's `acq_note` says $2,999M: check what
  it counts and what it misses.
- Q1: an electronic design, emulation and test company (oscilloscopes, network and signal analyzers,
  network test, design software), selling to communications, aerospace and defense, automotive and
  semiconductor customers, with hardware, software and service revenue. Check against the 10-K segment note
  whether that description is right and complete, how revenue splits between segments and between products
  and services, and how much is recurring.
- Q2: test it with [E3-03]'s three conditions, [E2-58]'s commodity class and its wide-and-sustainable cost
  exception, [E3-43]'s pricing demonstration read as a series across the down years (the filings say which;
  FY2015-FY2016, FY2020 and FY2023-FY2024 are candidates), and [E4-04]'s competence limit, which bites hard in
  electronics where the product generation turns over. Build a filed competitor row from SEC filers where the
  business is comparable (and name the unobtainable rows: foreign filers and private firms that do not file with
  the SEC, and test lines buried inside larger conglomerates). Record the long-run return on tangible capital as
  the filings show it, with goodwill from the purchases shown both ways. Write the strongest evidence against
  your verdict FIRST [E4-26, E3-41].
- Q3, if reached: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s third flag;
  read the proxy for what pay vests on ([E4-27] is the incentives row; [E4-52] is the lollapalooza row, NOT pay).
  The capital-return record (buybacks and their prices against value, acquisitions and what they earned) is a
  Q3 read.
- Q4, if reached: name the death from the survival-shapes index by number; debt maturities, covenants and
  acquisition debt are places to look.
- Owner earnings: rebuild the width over EVERY window (1 year to the longest the priced perimeter allows)
  and BOTH (c) ends [E2-09, E3-44]; report dollars and a word wherever the bottom sits near or below zero. The
  row's `spread_caveat` cites [E4-25]: check the claim against the numbers.
  **Known tool traps:** `run.py` averages each year's low and high capex ends, mixing ends across years;
  `run.py` strikes "growth the price assumes" against the bond, not the floor; the D&A tag has included goodwill
  impairment for another filer (OII) and acquired-intangible amortisation for another (ECL), which matters here
  after Ixia and Spirent; capitalised software or development belongs in (c) (XPEL); any discontinued-operations
  cash must be handled explicitly (ECL); `run.py` reads one CIK only. Owner earnings never via a net-income proxy
  (PRIME RULE 3's clause).
- Hard sequence: STOP at the first question not IN. UNRESEARCHED and UNKNOWABLE close the file. Any valuation
  before Q1-Q4 close is headed `COMPUTATION — NOT A CLEARANCE` and carries no entry language; a closed gate
  is not reopened by material beneath it [E2-37, E3-39].

## 5. The fold - the run does it, all six steps
1. Register entry in `## COMPLETED FROM THE QUEUE` (line-exact heading match, assert unique, insert as the
   FIRST entry like ECL's, count the entries back before and after, from the file: 243 were counted at 15:46
   by this dispatcher, entries being the lines beginning `- **` inside the slice to `## THE WRITE-EARLY PROTOCOL`;
   count it yourself). Price, share count with cover accession, cap, sovereign, and the PASS/FAIL line naming
   the question that closed the file.
2. Append `KEYS` to `Screens/_daily/_wave7_done.txt` (it has 101 lines ending CLB; after, 102 lines equal to the
   order file's first 102, compared ignoring line endings). Search the WHOLE queue file for a KEYS roster line
   to strike; record if none.
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, ending
   "Next in the order file: <the 103rd line of `Screens/_daily/_wave7_order.txt`>." (read it yourself).
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
