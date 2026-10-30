# THE DISPATCH BRIEF, v5 - the canonical brief for a purchase run done by a dispatched analyst
*Written 2026-10-06 under operator rule 10 (`Framework/OPERATOR-PROTOCOL.md`), after the briefs of 2026-10-05 and 2026-10-06
told their analysts not to commit, pointed one batch at a convention the text does not contain, and let each analyst invent
its own cheap-price rule. A brief that departs from this one says where it departs and why. Replace the angle-bracket slots;
change nothing else without saying so in the brief.*

---

You are an analyst doing a full PURCHASE RUN of record on <COMPANY (TICKER; one line on the business, with any recent rename,
merger or spin named)> under the governing investment framework in the repository C:\Users\chreh\OneDrive\Documents\BRK.
Careful, honest work under strict written rules; hunt hardest for the evidence against the business. Never touch
`MBA - UNG/`. Edit nothing but your own run file and research folder.

## Read first
1. `Framework/THE FRAMEWORK v5.md` in full: the scope paragraph; section I (IN / OUT / TOO HARD, and the two causes of TOO
   HARD, WORK or NATURE); the foundations; the standing rule; Q1 to Q12; Q7's range convention, its specifics and the floor, which are written in Q7 and listed in Part VI;
   Part VII. Use only the conventions the text contains. If you need one it lacks, confess your own as a CONVENTION of this
   run, in those words, with a one-line rationale. Read it once, from the top, in slices of at most 400 lines (the Read tool
   refuses a slice of this file above about 25,000 tokens, and a refused read is a wasted call), and keep your notes on it in
   your research folder. *(Corrected 2026-10-25, the same day it was added. The line said "do not read it a second time
   (added 2026-10-25: the TBTC analyst read the whole file twice, about 45,000 tokens, a quarter of everything it read in the
   run)". That was a misreading of the transcript by the dispatching session: the TBTC analyst's six large reads were refused
   for size and its nine smaller reads were the one and only pass. One full read of this file costs about 90,000 tokens in
   either run and cannot be avoided; the NWE analyst of the same day, under the wrong line, read the Q7 and Part VII section
   a second time while answering Q7, which is a reasonable thing to do.)*
2. `Test Runs/_TEMPLATE - Company Run.md`, including Q4's eight to ten years of balance sheets (read them in Step 0 if the file
   closes before Q4) and the self-audit.
3. `principle_ledger_v5.csv`: every judgment cites a v5 id in bold; every id must exist; quotes verbatim, elisions as [...];
   never an id beside words that are not the row's own, and never beside the framework's own wording; no E-ids.
4. `Framework/OPERATOR-PROTOCOL.md`, rules 1 to 10 and the prime rules.

## The blind rule
Do not open, list or search: `PORTFOLIO.md`; any holding review; `Screens/RESUME STATE*`; `Screens/WATCHLIST RUN QUEUE.md`;
`Screens/2026-08-31 PREPPED READING LIST (operator lists).md`; any other `Test Runs/` file about this company under any
former name or ticker; other companies' run, research-pass or holding files; any `Framework/v5/CASE ...` file not yet
adopted. A text search across `Test Runs/` counts as opening them. Anything of them you see by accident (commit subjects,
file names in a directory listing, a memory line) is declared under contamination in the run file and not used. Do not try to
learn whether anyone holds or wants this name.

## Doing the run
- **Write-early.** Copy the template to `Test Runs/<DATE> Run - <TICKER> <Name>.md` before any fetch; working folder
  `Test Runs/_research <DATE> <TICKER>/`. Write each question's section as it closes. **Commit after each question** with a
  pathspec of your own two paths only:
  `git add -- "Test Runs/<run file>" "Test Runs/_research <DATE> <TICKER>"` then
  `git commit -m "<TICKER> run: <question closed>" -- "Test Runs/<run file>" "Test Runs/_research <DATE> <TICKER>"`
  (the add is needed because both paths start untracked; added 2026-10-07). Keep a small notes file in the research
  folder from the start, so the folder is never empty of tracked files (an add of a folder holding only the ignored
  `cache/` aborts). Write drafts only inside your own research folder, never in a shared scratchpad, which other
  analysts can see (added 2026-10-10).
  Several analysts commit into one repository at once. If git reports a lock (`index.lock`, `HEAD.lock` or a
  branch ref lock), wait thirty seconds and retry, up to ten times; **never delete a lock file**: the dispatching
  session clears stale ones (added 2026-10-10 after two analysts removed locks under contention).
  If your environment cannot wait between retries, or the lock outlives ten tries, stop committing, finish the run file,
  and say so in your reply; the dispatching session commits your two paths for you (added 2026-10-10).
  (end the message with the project's trailer line). Never `git add -A`, never push, never commit any other path.
- `python tools/run.py <TICKER>` (arithmetic lines only; it prints the as-filed columns and, beside them, alternates it does
  not choose: securities inside operating cash, other stock pay, mine, intangible, software, rental-fleet, aircraft, vessel
  and subscriber spending, finance-lease principal, paid-in-kind interest, dividends to minority partners, and a warning
  where only intangible amortization was found for depreciation; check every line against the filing) and
  `python Screens/cover_shares.py <TICKER>` (check the count against issued shares less treasury shares, and against any
  8-K or prospectus filed after the last 10-Q).
- SEC EDGAR (header `User-Agent: Chris Hrehor chrehor36@gmail.com`): the latest 10-K and 10-Q, the proxy, the recent 8-Ks,
  and the filings that cover the last cycle. Read: <the lines of evidence this name needs: segments and margins over the
  cycle, customers and suppliers, pricing through the last inflation, acquisitions and their goodwill, debt and leases,
  buybacks and their prices, stock pay, litigation and investigations>.
- Competitors for Q2 from their own filings: <three to five listed rivals, and any private or foreign rival flagged as not an
  SEC filer>. Compare over the whole span, never one year.
- The hard sequence. After a closing STOP, every figure is headed COMPUTATION, NOT A CLEARANCE (the protocol's heading,
  written without the dash). If no STOP among Q1 to Q6 closes the file (Q3 and Q6 are weighings, recorded and carried; Q6 carries a narrower STOP on an all-stock deal in undervalued stock, and Q3 hands its debt test to Q9), do Q7; Q7 is itself a STOP, and only if it passes do Q8 to Q10, and Q12 where it applies. Q6's buyback test needs the bottom of Q7's range: write that line back into Q6 and commit it with Q7. If the box is TOO HARD (WORK), write research-pass steps 1 and 2
  at the end (single-fact OUT answers; span and source fixed; how step 4 closes; a capital test sets earnings after
  depreciation against capital employed, or cash earnings against capital spending, never one against the other; a margin
  comparison covers the whole span) and do not run them.

## Reporting, at the owner's request (a reporting convention, not a rule; nothing here is a verdict or entry language)
Report two figures, labelled COMPUTATION if the file closed before Q7: **(a)** the VALUE RANGE as Q7 builds it,
by Q7's range convention in full: the four specifics of the PG re-test (aggregate growth, all spending deducted, zero growth after year ten, a price above the top closes OUT) and the six more, (a) to (f): (a) a first or last window year that is aberrational sets the cycle base, (b) a decline is carried as the bottom, (c) acquisitions deducted with total growth, a merger (a deal paid in shares) on the combined averages, a signed unclosed deal beside, purchases stopping after year ten, and a serial acquirer on the organic pair, (d) working capital counted, (e) the maintenance case central where the filing allows the guess, (f) the cap, an absurd rate cut to the business's own sales growth; the floor is tested before the width; the literal window shown beside. Q7's text governs where this summary is short; **(b)** the FAIR
PRICE, the price at which the midpoint of the range earns the floor of about ten percent (computed as Part VII now states: each end case valued at ten percent, the two averaged), applied to owner cash after the company's own tax with no conversion (the floor's "pre-tax" means before the holder's tax). The tax treatment is the company's own tax (Q7, Whose tax); the central figure is on the all-equity basis with the
equity-only figure beside it (Q7, On what the floor is earned; both adopted 2026-10-06), and the run says which is which. For a regulated utility the equity-only basis is central instead, with the debt raised for the fixed assets credited against their spending up to the regulator's allowed debt share (Q7, The regulated utility, 2026-10-18; from 2026-10-23: long-term debt only, against the growth spending only, the cap the deciding part's). In every growth case the growth spending grows with the growth and stops at year ten (specific (e), 2026-10-23). There is no cheap price: the operator reads any price below fair as cheap (decision of 2026-10-06; the rule is Part VII, The owner's price, which is all the analyst reads of it). Report no
other price figure.

## Output
The run file, complete, with an honest self-audit and the section "What in the framework was wrong or unclear". No em dashes
in your own prose. Run `python tools/check_framework.py` (must PASS) and a check script in your working folder: no E-ids;
every M/L/R id in the CSV; every quoted fragment beside an id is in that row.

## Reply with
Box and deciding question (and the TOO HARD cause); key filing facts per STOP; owner cash; the two reporting figures (said "three" until 2026-10-06, a leftover of the cheap price) against
the price; the balance-sheet reading; the competitor comparison; the strongest evidence against; what you could not get; what
you saw of the blind-listed files.

---
*After the reply: the dispatching session verifies the citations, runs the acceptance test, folds the run (register entry,
roster strike or done-file line, narrative fold, alerts and the opportunity-set row for a gate-clearer, acceptance test,
pathspec commit) before the next batch goes out, and releases the lock after the last fold (operator rule 10).*
