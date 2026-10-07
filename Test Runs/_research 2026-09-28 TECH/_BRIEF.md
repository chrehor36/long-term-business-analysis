# BRIEF - TECH Bio-Techne Corporation - WAVE 7, dispatched 2026-09-28 by the 20:46 overnight cycle

You are running ONE company through the purchase framework, unattended. The operator is asleep; nobody
will answer a question. Work in the repository at C:\Users\chreh\OneDrive\Documents\BRK.

## 0. Read first, in order
1. `CLAUDE.md` (the map), `Framework/OPERATOR-PROTOCOL.md` (binding), `Framework/THE FRAMEWORK v4.md` (governing),
   `Framework/v4/THE MANAGER STANDARD - Q3.md` (for Q3 if reached).
2. `Test Runs/_TEMPLATE - Company Run.md` (the enforcement surface).
3. `Screens/WATCHLIST RUN QUEUE.md`: the WAVE 7 section, THE WRITE-EARLY PROTOCOL, CLAIM THE NAME AT
   DISPATCH, THE FOLD (six steps, including the dated note on writing the register entry BY LINE), WRITING A BRIEF.
4. The most recent finished runs, for the standard and the fold mechanics:
   `Test Runs/2026-09-28 Run - MA Mastercard.md`, `Test Runs/2026-09-28 Run - ESI Element Solutions.md` and
   `Test Runs/2026-09-28 Run - KEYS Keysight Technologies.md` (reached Q5; bands armed),
   `Test Runs/2026-09-28 Run - EGAN eGain.md` and `Test Runs/2026-09-28 Run - CW Curtiss-Wright.md` (closed at Q2).
   Their research folders (`Test Runs/_research 2026-09-28 EGAN/`, `... CW/`, `... MA/`, `... ESI/`) hold
   reusable scripts (fetch, getk, getsub, series, peers, px, sov, quotecheck, fold). Adapt them; do not trust
   them blind (the SANM fold script, adapted from WING, appended WING to the done file; the KEYS fold script
   stopped at step 5 on a format error; check every hard-coded ticker, CIK, count and "next" name in
   anything you copy).
5. `Screens/SURVIVAL SHAPES - index.md` (name the shape from it by number; a new shape is added at fold; count
   a shape's instances row before writing to it, KEYS found #10 at its maximum).

## 1. Write early, claim now
- FIRST action after reading: copy the template to `Test Runs/2026-09-28 Run - TECH Bio-Techne.md` and
  commit it (the claim). Then write each question as it closes and commit after each gate.
- Research, scripts and outputs go to `Test Runs/_research 2026-09-28 TECH/` (this folder; this brief is in it).
- COMMIT WITH A PATHSPEC ONLY: `git commit -F <msgfile> -- <paths>`. Never `git add X && git commit`.
  Write commit messages to a file. Bash heredocs containing apostrophes fail here: write scripts to files.
  A new untracked file needs `git add -- <that path>` before a pathspec commit can carry it; never add an
  ignored path, and check `git diff --cached --name-only` is exactly your paths before committing.
  Raw filing text is NOT caught by .gitignore except under a `cache/` subfolder (MSA committed six); keep
  raw filings in `Test Runs/_research 2026-09-28 TECH/cache/`.
- Commit trailer (the operator's own prompt line, which takes precedence over the environment's default;
  use it and do not log it as an error): `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`
- Do not touch `Screens/_daily/_overnight.lock`; the dispatching cycle holds it.
- Do not touch the pre-existing modified `Test Runs/_research 2026-09-27 ARCB/_logmsg_dispatch.txt` or any
  other session's untracked files.
- No helper agents. One agent, this one.

## 2. The screen row, UNLABELLED (from `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`, line 177)
```
ticker,name,cap_m,oe_bottom_m,oe_top_m,spread,spread_dollars,cap_flag,deal_note,name_change_note,wc_note,yield_bottom,vs_sovereign,growth_required,level_shift,level_note,best_year_dep,best_year_note,level_shift_oe,level_note_oe,best_year_dep_oe,flags_disagree,level_shift_full,years_filed,window_disagree,acq_note,da_note,spread_caveat,newest_filing,newest_periodic
TECH,BIO-TECHNE Corp,11322,144,211,0.467,$144M to $211M,,,,,0.0127,-0.0408,0.0873,1.18,no step,0.042,no single-year dependence (9-yr OCF series),1.23,no step,0.048,,1.66,18,,,,4-construction width only (3y/5y x two capex ends): CANNOT see variation older than the 5-year window; rebuild it [E4-25],2026-06-30,2026-06-30
```
Every field is a claim to reproduce or refute, not a fact. Recent runs found cap_m stale by 3-47% (MA's was a
2010 cover count times a 2014 split), the yield fields struck on the stale cap and a 5.35% bond, `wc_note`
misreading working-capital lines, "9-yr OCF series" wrong more than once, text fields truncated, and
acquisition and D&A notes blank beside material purchases and acquired amortization (MA, CW). Here `acq_note`,
`da_note` and `deal_note` are all blank: treat blank as unverified, not as "none". Record each screen field you
check, and whether it reproduced, in the self-audit.

## 3. Step 0 inputs - strike them yourself
- Sovereign: strike it fresh from the US Treasury daily par yield curve, 30-year, dated. CW found
  `tools/sources.py` `sovereign('USD')` serving a cached row after the Treasury had published; EGAN found
  it right. Fetch the Treasury directly (see `Test Runs/_research 2026-09-28 CW/sov.py` or `... EGAN/sov.py`)
  and record the date of the row you use. Do not inherit a figure from this brief or another run.
- Price: re-strike it and flag the aggregator. This brief was written at about 20:50 EDT Monday 2026-09-28,
  after the close; `tools/sources.price` and `tools/run.py` have returned an intraday print as the day's price
  in seven runs. Use the last CLOSE, check `regularMarketTime`, and record which session's close it is and any
  intraday print as recorded-not-used. `chartPreviousClose` has been meaningless in every recent run.
- Share count: `python Screens/cover_shares.py TECH` returned, at dispatch, 156,818,238 (Common Stock, $0.01
  par), 10-K period 2026-06-30, filed 2026-08-24, accession 0001104659-26-100322. Re-run it, read the cover
  yourself, confirm there is one class and read the charter (authorized preferred, any issued) before
  summing anything. `tools/sources.cik_for('TECH')` returned ('0000842023', 'BIO-TECHNE Corp') (verify). The
  fiscal year ends 30 June; the FY2026 10-K appears to be the newest periodic filing (check for any later
  10-Q or 8-K).
- Split-invariant cap per the protocol (`close`, never `adjclose`). My understanding (verify) is that the
  company did a four-for-one split in 2022; check the split history before using any older count or
  per-share figure, including prior-year buyback prices.
- Deal: `sources.deal_filings(842023)` at dispatch returned no deal forms and a latest annual report date of
  2026-08-24. That is a tool's reading of form types, not a reading of the filings: scan the 8-Ks since the
  FY2025 10-K yourself for Item 1.01, Item 2.01 (acquisitions and disposals), strategic-review language and
  any bid, before pricing (ESI's brief called a dead deal live; EGAN's found none; this one might miss a
  live one either way). The known tooling note stands: `sources.deal_note` has failed with TypeError on the
  `cik_for` tuple and ValueError on the ticker; it runs only with the integer CIK. Report, do not patch.
- SBC: verify it RESOLVES and is COMPLETE (BE's did not resolve; Boeing's stock-settled 401(k) sat under a tag
  no SBC element contains). Take it from the cash-flow add-back, not the larger of two tags (KEYS), and state
  it against owner earnings.

## 4. The priors - hypotheses to refute, not conclusions
Every brief so far has contained at least one error. Assume this one does too, and check each prior.
- Registrant and perimeter. My understanding, to verify from filings: Bio-Techne is a Minneapolis company,
  formerly Techne Corporation (renamed around 2014; check `name_change_note`, which is blank), whose oldest
  business is R&D Systems, a maker of research reagents (proteins, antibodies, assay kits) sold to academic,
  biotech and pharmaceutical laboratories. It reports, I believe, two segments: Protein Sciences, and a
  diagnostics and spatial-biology segment assembled largely by acquisition over the last decade (names I
  believe are in it, all to verify: Advanced Cell Diagnostics, Exosome Diagnostics, Asuragen, Lunaphore,
  ProteinSimple in Protein Sciences). My understanding is also that it sold or agreed to sell part of the
  diagnostics business (Exosome Diagnostics) in 2025, and that it held an equity stake in ChemoCentryx that
  produced large gains and losses in net income before Amgen bought that company: verify both from the
  filings, and establish which filed years measure the business being priced. A decade of purchases means
  the long operating-margin and return record is a record of a changing perimeter; say which years are
  comparable, and keep equity-investment gains and losses out of owner earnings.
- Customers. I believe the customer base is academic and government-funded laboratories, biopharma, and
  diagnostics customers, with a material share of sales outside the US including China; I do not know the
  proportions or any concentration. The 10-K says; the earnings releases of the last two years will say
  what the filer attributes changes in demand to.
- Q1: can you understand how this makes money, from the 10-K: who pays, for what, how revenue splits
  between consumables and instruments and between segments, and what the filer says it competes against.
- Q2: test it with [E3-03]'s three conditions, [E2-58]'s commodity class and its wide-and-sustainable cost
  exception, [E3-43]'s pricing demonstration read as a series across years (look for any filed price and
  volume attribution in the MD&A), [E2-44]'s two characteristics, and [E4-04]'s competence limit. Build a
  filed competitor row from SEC filers where the business is comparable (segment disclosures of larger
  life-science tool companies, and any standalone reagent makers that file), and name the unobtainable rows
  (private companies and product lines buried inside larger filers). Record the long-run return on tangible
  capital and the operating-margin record as the filings show it across the whole history, in dollars.
  Write the strongest evidence against your verdict FIRST [E4-26, E3-41].
- Q3, if reached: pull the latest 8-K EX-99.1 earnings releases before scoring [E4-29] and [E4-22]'s third
  flag, and read the adjusted-to-GAAP reconciliation (what is excluded, and whether acquired amortization and
  stock compensation are among the exclusions); read the proxy for what pay vests on ([E4-27] is the
  incentives row; [E4-52] is the lollapalooza row, NOT pay). The acquisition record (prices paid, impairments
  taken, businesses later sold) and the buyback record (prices against value, split-adjusted) are Q3 reads.
  I believe there was a CEO succession in 2024: verify and read what it changed.
- Q4, if reached: name the death from the survival-shapes index by number.
- Owner earnings: rebuild the width over EVERY window (1 year to the longest the priced perimeter allows)
  and BOTH (c) ends [E2-09, E3-44]; report dollars and a word wherever the bottom sits near or below zero.
  The row's `spread_caveat` cites [E4-25]: check the claim against the numbers.
  **Known tool traps:** `run.py` averages each year's low and high capex ends, mixing ends across years;
  `run.py` strikes "growth the price assumes" against the bond, not the floor; the D&A tag has included
  goodwill impairment (OII) and acquired-intangible amortization (ECL, KEYS, CW, ESI, MA): an acquirer's D&A
  will carry it here, so separate it; `run.py` has taken the larger SBC expense tag over the cash-flow
  add-back (KEYS), a weighted diluted count over the cover (MA), a stale quarter's cover (ESI) and a
  three-year window years out of date (EGAN); capitalized software or development belongs in (c) (XPEL);
  `run.py` reads one CIK only (CLB). Owner earnings never via a net-income proxy (PRIME RULE 3's clause).
- Hard sequence: STOP at the first question not IN. UNRESEARCHED and UNKNOWABLE close the file. Any valuation
  before Q1-Q4 close is headed `COMPUTATION — NOT A CLEARANCE` and carries no entry language; a closed gate
  is not reopened by material beneath it [E2-37, E3-39].

## 5. The fold - the run does it, all six steps
1. Register entry in `## COMPLETED FROM THE QUEUE` (line-exact heading match, assert unique, insert as the
   FIRST entry like EGAN's, count the entries back before and after, from the file: 248 were counted at 20:48
   by this dispatcher, entries being the lines beginning `- **` inside the slice to `## THE WRITE-EARLY PROTOCOL`;
   count it yourself). Price, share count with cover accession, cap, sovereign, and the PASS/FAIL line naming
   the question that closed the file.
2. Append `TECH` to `Screens/_daily/_wave7_done.txt` (it has 106 lines ending EGAN; after, 107 lines equal to
   the order file's first 107, compared ignoring line endings). Search the WHOLE queue file for a TECH roster
   line to strike; record if none.
3. Narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, ending
   "Next in the order file: <the 108th line of `Screens/_daily/_wave7_order.txt`>." (read it yourself).
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row ONLY if Q1-Q4 all cleared. A Q2, Q3 or Q4 failure
   arms nothing and records the reversal condition in words.
5. Survival-shapes index: dated note or new shape as the precedent runs did.
6. `python tools/check_framework.py` must PASS before the fold commit. Pathspec commit.

Nothing about the framework changes: no ledger row, no edit to `Framework/`, no question added or removed.
Never present the framework as proven to beat the market. No em dashes in your own prose (quoted text and
the required `COMPUTATION — NOT A CLEARANCE` heading excepted). No git push, rebase, reset --hard or force.

## 6. What to return to the dispatcher
The verdict line (e.g. Q1 IN / Q2 OUT, with the reason in one sentence), what the deal check found, price
with date and source, share count and accession, cap, sovereign with date, PASS/FAIL, every commit hash in
order, the register count before and after, the done-file line count, the next name, the screen errors
found, tooling defects reported not patched, your own errors, and any file left uncommitted.
