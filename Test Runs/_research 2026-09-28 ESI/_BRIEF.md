# BRIEF - ESI Element Solutions Inc - WAVE 7, dispatched 2026-09-28 by the 16:46 overnight cycle

You are running ONE company through the purchase framework, unattended. The operator is asleep; nobody
will answer a question. Work in the repository at C:\Users\chreh\OneDrive\Documents\BRK.

## 0. Read first, in order
1. `CLAUDE.md` (the map), `Framework/OPERATOR-PROTOCOL.md` (binding), `Framework/THE FRAMEWORK v4.md` (governing),
   `Framework/v4/THE MANAGER STANDARD - Q3.md` (for Q3 if reached).
2. `Test Runs/_TEMPLATE - Company Run.md` (the enforcement surface).
3. `Screens/WATCHLIST RUN QUEUE.md`: the WAVE 7 section, THE WRITE-EARLY PROTOCOL, CLAIM THE NAME AT
   DISPATCH, THE FOLD (six steps, including the dated note on writing the register entry BY LINE), WRITING A BRIEF.
4. The most recent finished runs, for the standard and the fold mechanics:
   `Test Runs/2026-09-28 Run - KEYS Keysight Technologies.md` and `Test Runs/2026-09-28 Run - ECL Ecolab.md`
   (both reached Q5; bands armed), `Test Runs/2026-09-28 Run - CLB Core Laboratories.md` (closed at Q2).
   Their research folders (`Test Runs/_research 2026-09-28 KEYS/`, `... ECL/`, `... CLB/`) hold reusable
   scripts (fetch, companyfacts, oe, peers, qcheck, fold, fold_rest). Adapt them; do not trust them blind
   (the SANM fold script, adapted from WING, appended WING to the done file; the KEYS fold script stopped at
   step 5 on a format error; check every hard-coded ticker, count and "next" name in anything you copy).
5. `Screens/SURVIVAL SHAPES - index.md` (name the shape from it by number; a new shape is added at fold; count
   a shape's instances row before writing to it, KEYS found #10 at its maximum).
6. For a ROKU-style live deal: `Test Runs/2026-09-12 Run - ROKU Roku.md` is the precedent for "the quote is a spread".

## 1. Write early, claim now
- FIRST action after reading: copy the template to `Test Runs/2026-09-28 Run - ESI Element Solutions.md` and
  commit it (the claim). Then write each question as it closes and commit after each gate.
- Research, scripts and outputs go to `Test Runs/_research 2026-09-28 ESI/` (this folder; this brief is in it).
- COMMIT WITH A PATHSPEC ONLY: `git commit -F <msgfile> -- <paths>`. Never `git add X && git commit`.
  Write commit messages to a file. Bash heredocs containing apostrophes fail here: write scripts to files.
  A new untracked file needs `git add -- <that path>` before a pathspec commit can carry it; never add an
  ignored path, and check `git diff --cached --name-only` is exactly your paths before committing.
  Raw peer 10-K text files are NOT caught by .gitignore (MSA committed six); keep raw filings in `cache/`.
- Commit trailer (the operator's own prompt line, which takes precedence over the environment's default;
  use it and do not log it as an error): `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`
- Do not touch `Screens/_daily/_overnight.lock`; the dispatching cycle holds it.
- Do not touch the pre-existing modified `Test Runs/_research 2026-09-27 ARCB/_logmsg_dispatch.txt` or any
  other session's untracked files.
- No helper agents. One agent, this one.

## 2. The screen row, UNLABELLED (from `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 168)
```
ticker,name,cap_m,oe_bottom_m,oe_top_m,spread,spread_dollars,cap_flag,deal_note,name_change_note,wc_note,yield_bottom,vs_sovereign,growth_required,level_shift,level_note,best_year_dep,best_year_note,level_shift_oe,level_note_oe,best_year_dep_oe,flags_disagree,level_shift_full,years_filed,window_disagree,acq_note,da_note,spread_caveat,newest_filing,newest_periodic
ESI,Element Solutions Inc,8331,133,238,0.798,$133M to $238M,,"LIVE DEAL FORM: 22 filing(s) since the annual report of 2026-02-18, first 425 on 2026-07-06 (0001104659-26-080826). IF A DEAL IS LIVE THE QUOTE IS A SPREAD, NOT AN OWNER-EARNINGS PRICE - read it before pricing anything [ROKU, 2026-09-12].","NAME CHANGE inside the data window: was 'Platform Specialty Products Corp' until 2019-01-28. Possibly a reverse merger, de-SPAC, spin or merger whose predecessor's figures sit under this CIK - or a rebrand (~60% of these are real perimeter events). CHECK THAT MULTI-YEAR FIGURES ARE ONE COMPANY [NEGG, 2026-09-13].",,0.0159,-0.0376,0.0841,n/a,EARLY HALF STRADDLES ZERO - the pre-window years run from $-,0.057,no single-year dependence (9-yr OCF series),n/a,EARLY HALF STRADDLES ZERO - the pre-window years run from $-45.8M to $,0.073,,n/a,12,,"acquisitions are $778M, 9% of cap, inside the window.",,4-construction width only (3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25],2025-12-31,2026-03-31
```
Every field is a claim to reproduce or refute, not a fact. Recent runs found cap_m stale by 3-19%, the yield
fields struck on the stale cap and a 5.35% bond, the `wc_note` reading the sign of a working-capital line
backwards (SANM, CLB) or quoting a gross roll-forward line (OII, KEYS), "9-yr OCF series" wrong more than once,
text fields truncated (OII), and acquisition notes that missed purchases made after the screen's data (ECL, KEYS).
Note `newest_periodic` is 2026-03-31: a later 10-Q exists (below). Record each screen field you check, and
whether it reproduced, in the self-audit.

## 3. Step 0 inputs - strike them yourself
- Sovereign: strike it fresh from the US Treasury daily par yield curve, 30-year, dated (`tools/sources.py`
  `sovereign('USD')`). Do not inherit a figure from this brief or from another run.
- Price: re-strike it and flag the aggregator. This brief was written at 16:47 EDT Monday 2026-09-28, after the
  close; `tools/sources.price` and `tools/run.py` have returned an intraday print as the day's price with no
  warning in seven consecutive runs. Use the last CLOSE, check `regularMarketTime`, and record which session's
  close it is and any intraday print as recorded-not-used.
- Share count: `python Screens/cover_shares.py ESI` returned, at dispatch, 243,690,914 (Common Stock, par $0.01),
  10-Q period 2026-06-30, filed 2026-07-28, accession 0001590714-26-000065. Re-run it, read the cover yourself,
  confirm there is one class and read the charter (authorized preferred, any issued; the predecessor had
  Series A and Series B preferred at some point: check) before summing anything.
  `tools/sources.cik_for('ESI')` returns ('0001590714', 'Element Solutions Inc') (verify).
- Split-invariant cap per the protocol (`close`, never `adjclose`).
- **DEAL: THE ROW SAYS A DEAL FORM IS LIVE AND IT IS.** `sources.deal_filings(1590714)` at dispatch returned
  twenty-two Form 425 filings from 2026-07-06 to 2026-08-11 (filer agents 0001104659 and 0001213900, so more than
  one party is filing) and two 8-Ks, 2026-07-06 (0001104659-26-080825) and 2026-08-28 (0001104659-26-102559).
  I have NOT read them and do not know who is buying whom, in what consideration, or whether ESI is buyer,
  target or merger-of-equals party. READ THE 2026-07-06 8-K (Item 1.01 and any EX-2.1) AND THE 2026-08-28 8-K
  FIRST, then any S-4 or proxy. Establish: the parties and the direction; cash, stock or mixed consideration;
  whether an ESI shareholder receives a fixed amount (then the quote is a spread, not an owner-earnings price,
  ROKU) or keeps a share of a combined company (then the priced perimeter is the combined company, which no
  filed year measures); the vote and regulatory timetable, termination fees, and whether the deal is still live
  at the latest filing. Decide what the quote is BEFORE pricing anything, and say which run precedent applies.
  The gates on the business still run under the hard sequence; the deal decides what Q5 may do with the price.
- **Tooling note, report not patch:** `sources.deal_note(cik)` returned "deal check FAILED (TypeError)" when
  given the tuple from `cik_for`, and "FAILED (ValueError)" when given the ticker; it ran only with the integer
  CIK. Record it in the self-audit's tooling reports.
- SBC: verify it RESOLVES and is COMPLETE (BE's did not resolve; Boeing's stock-settled 401(k) sat under a tag
  no SBC element contains). Check for any stock-settled employee plan, founder or advisory award, or
  preferred-linked award outside the SBC element.

## 4. The priors - hypotheses to refute, not conclusions
Every brief so far has contained at least one error. Assume this one does too, and check each prior.
- Perimeter and registrant. My understanding, to verify from filings: the registrant began as Platform
  Acquisition Holdings, a listed acquisition vehicle, which bought MacDermid (specialty chemicals for plating,
  electronics and printing) in 2013, then bought agricultural-chemical businesses (Chemtura AgroSolutions and
  Arysta LifeScience, around 2015), sold the agricultural business to UPL around January 2019 and renamed itself
  Element Solutions. If that is right, filed years before FY2019 measure a different company (the agricultural
  segment would be in discontinued operations in restated years, or not), and the MacDermid predecessor's own
  history sits in other filings. Since then it has bought businesses (the row counts $778M; I believe Coventya,
  HKW, Kester, EFC and a Micromax purchase from Celanese are among them: verify every one, with dates and prices,
  and any sales). Establish which filed years measure the company that is priced; a window that mixes perimeters
  measures a company that is not the one priced. The row's `name_change_note` asks exactly this.
- Q1: a supplier of specialty chemicals and materials, in two segments (electronics: circuit-board and
  semiconductor plating chemistry and assembly solder and fluxes; industrial and specialty: surface finishing,
  graphics and offshore fluids), selling consumables priced into customers' production. Check against the 10-K
  segment note whether that description is right and complete, how revenue splits, how much is pass-through
  metal (tin, silver, gold, palladium) that moves revenue without moving profit, and how much is recurring.
- Q2: test it with [E3-03]'s three conditions, [E2-58]'s commodity class and its wide-and-sustainable cost
  exception, [E3-43]'s pricing demonstration read as a series across the down years (the filings say which; FY2019,
  FY2020 and FY2023 are candidates), and [E4-04]'s competence limit. Metal pass-through is a trap in both
  directions: strip it before reading margins and read the price the filer says it takes on its own chemistry.
  Build a filed competitor row from SEC filers where the business is comparable (and name the unobtainable
  rows: foreign filers and private firms that do not file with the SEC, and chemistry lines buried inside larger
  conglomerates). Record the long-run return on tangible capital as the filings show it, with goodwill from the
  purchases shown both ways (a vehicle that bought everything it owns may have almost no tangible base: say so).
  Write the strongest evidence against your verdict FIRST [E4-26, E3-41].
- Q3, if reached: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s third flag;
  read the proxy for what pay vests on ([E4-27] is the incentives row; [E4-52] is the lollapalooza row, NOT pay).
  The capital-return record (buybacks and their prices against value, acquisitions and what they earned, and
  the deal itself) is a Q3 read.
- Q4, if reached: name the death from the survival-shapes index by number; debt maturities, covenants and
  acquisition debt are places to look (the vehicle was built on term loans).
- Owner earnings: rebuild the width over EVERY window (1 year to the longest the priced perimeter allows)
  and BOTH (c) ends [E2-09, E3-44]; report dollars and a word wherever the bottom sits near or below zero (the
  row says the early half straddles zero: check whether those years are even the same company). The row's
  `spread_caveat` cites [E4-25]: check the claim against the numbers.
  **Known tool traps:** `run.py` averages each year's low and high capex ends, mixing ends across years;
  `run.py` strikes "growth the price assumes" against the bond, not the floor; the D&A tag has included goodwill
  impairment (OII) and acquired-intangible amortisation (ECL, KEYS), which matters a great deal for a company
  built by purchase; `run.py` has taken the larger SBC expense tag over the cash-flow add-back (KEYS);
  capitalised software or development belongs in (c) (XPEL); discontinued-operations cash must be handled
  explicitly (ECL; the agricultural sale makes this likely here); `run.py` reads one CIK only (CLB). Owner
  earnings never via a net-income proxy (PRIME RULE 3's clause).
- Hard sequence: STOP at the first question not IN. UNRESEARCHED and UNKNOWABLE close the file. Any valuation
  before Q1-Q4 close is headed `COMPUTATION — NOT A CLEARANCE` and carries no entry language; a closed gate
  is not reopened by material beneath it [E2-37, E3-39].

## 5. The fold - the run does it, all six steps
1. Register entry in `## COMPLETED FROM THE QUEUE` (line-exact heading match, assert unique, insert as the
   FIRST entry like KEYS's, count the entries back before and after, from the file: 244 were counted at 16:47
   by this dispatcher, entries being the lines beginning `- **` inside the slice to `## THE WRITE-EARLY PROTOCOL`;
   count it yourself). Price, share count with cover accession, cap, sovereign, and the PASS/FAIL line naming
   the question that closed the file.
2. Append `ESI` to `Screens/_daily/_wave7_done.txt` (it has 102 lines ending KEYS; after, 103 lines equal to the
   order file's first 103, compared ignoring line endings). Search the WHOLE queue file for an ESI roster line
   to strike; record if none (beware "ESI Group" in the KEYS entry, a different company).
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, ending
   "Next in the order file: <the 104th line of `Screens/_daily/_wave7_order.txt`>." (read it yourself).
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row ONLY if Q1-Q4 all cleared. A Q2 or Q3 or Q4 failure
   arms nothing and records the reversal condition in words. If a live deal makes the quote a spread, say what
   that does to any band.
5. Survival-shapes index: dated note or new shape as the precedent runs did.
6. `python tools/check_framework.py` must PASS before the fold commit. Pathspec commit.

Nothing about the framework changes: no ledger row, no edit to `Framework/`, no question added or removed.
Never present the framework as proven to beat the market. No em dashes in your own prose (quoted text and
the required `COMPUTATION — NOT A CLEARANCE` heading excepted). No git push, rebase, reset --hard or force.

## 6. What to return to the dispatcher
The verdict line (e.g. Q1 IN / Q2 OUT, with the reason in one sentence), what the deal is and what it made the
quote, price with date and source, share count and accession, cap, sovereign with date, PASS/FAIL, every commit
hash in order, the register count before and after, the done-file line count, the next name, the screen errors
found, tooling defects reported not patched, your own errors, and any file left uncommitted.
