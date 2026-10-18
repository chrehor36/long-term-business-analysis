
You are an analyst doing a full PURCHASE RUN of record on Horiba, Ltd. (HRIBF; HRIBF is the US over-the-counter symbol of its ordinary shares and HRBAY of its unsponsored American depositary shares; incorporated in Japan; not an SEC registrant: its only EDGAR filings are two depositaries' F-6EF registrations, The Bank of New York Mellon on 2025-09-29, accession 0001019155-25-000400, and Citibank on 2025-11-19, accession 0001193805-25-001622. The dispatcher has read no filing describing the business; write the one-line description of the business, and name any rename, merger, spin-off or split, from the company's own latest annual report) under the governing investment framework in the repository C:\Users\chreh\OneDrive\Documents\BRK.
Careful, honest work under strict written rules; hunt hardest for the evidence against the business. Never touch
`MBA - UNG/`. Edit nothing but your own run file and research folder.

## Read first
1. `Framework/THE FRAMEWORK v5.md` in full: the scope paragraph; section I (IN / OUT / TOO HARD, and the two causes of TOO
   HARD, WORK or NATURE); the foundations; the standing rule; Q1 to Q12; Q7's range convention, its specifics and the floor, which are written in Q7 and listed in Part VI;
   Part VII. Use only the conventions the text contains. If you need one it lacks, confess your own as a CONVENTION of this
   run, in those words, with a one-line rationale.
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
- **Write-early.** Copy the template to `Test Runs/2026-10-13 Run - HRIBF Horiba.md` before any fetch; working folder
  `Test Runs/_research 2026-10-13 HRIBF/`. Write each question's section as it closes. **Commit after each question** with a
  pathspec of your own two paths only:
  `git add -- "Test Runs/2026-10-13 Run - HRIBF Horiba.md" "Test Runs/_research 2026-10-13 HRIBF"` then
  `git commit -m "HRIBF run: <question closed>" -- "Test Runs/2026-10-13 Run - HRIBF Horiba.md" "Test Runs/_research 2026-10-13 HRIBF"`
  (the add is needed because both paths start untracked; added 2026-10-07). Keep a small notes file in the research
  folder from the start, so the folder is never empty of tracked files (an add of a folder holding only the ignored
  `cache/` aborts). Write drafts only inside your own research folder, never in a shared scratchpad, which other
  analysts can see (added 2026-10-10).
  Several analysts commit into one repository at once. If git reports a lock (`index.lock`, `HEAD.lock` or a
  branch ref lock), wait thirty seconds and retry, up to ten times; **never delete a lock file**: the dispatching
  session clears stale ones (added 2026-10-10 after two analysts removed locks under contention).
  If your environment cannot wait between retries, or the lock outlives ten tries, stop committing, finish the run file,
  and say so in your reply; the dispatching session commits your two paths for you (added 2026-10-10).
  (end the message with the project's trailer line, `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`). Never `git add -A`, never push, never commit any other path.
- `python tools/run.py HRIBF` (arithmetic lines only; it prints the as-filed columns and, beside them, alternates it does
  not choose: securities inside operating cash, other stock pay, mine, intangible, software, rental-fleet, aircraft, vessel
  and subscriber spending, finance-lease principal, paid-in-kind interest, dividends to minority partners, and a warning
  where only intangible amortization was found for depreciation; check every line against the filing) and
  `python Screens/cover_shares.py HRIBF` (check the count against issued shares less treasury shares, and against any
  8-K or prospectus filed after the last 10-Q).
- **The primary document (departure from the canonical brief: Horiba files nothing with the SEC beyond the depositaries' F-6s).** Read the company's own latest annual report from its investor-relations site (the Japanese Annual Securities Report, yukashoken hokokusho, filed on EDINET, and the integrated or annual report in English), its latest quarterly or half-year report, its notice of the general meeting, and its recent timely disclosures on the Tokyo Stock Exchange; and the earlier annual reports that cover the last cycle (operator rule 5: primary filings over aggregators). Record each document and its date in place of an accession number, and cross-check one figure against the filed statement. Where `tools/run.py` and `Screens/cover_shares.py` find no SEC data, take the arithmetic and the share count (issued shares less treasury shares) from the filed statements by hand, and say so. Price: the Tokyo close, dated, with the OTC quote only as a flagged aggregator figure; state the ADS ratio from the depositary's own document if you use it. Sovereign for the earnings currency: JPY, from the Japan Ministry of Finance, jgbcme.csv, the 30-year, dated (`python tools/sources.py`).
- **The lines of evidence (the brief's second departure, stated here: an unattended cycle cannot check a hand-written list, and five hand-written lists of 2026-10-07 and 2026-10-10 carried factual errors).** Derive them yourself from the annual report's sections on the business and segments, the business risks, and management's analysis of results (the counterparts of a 10-K's Item 1, Item 1A and Item 7), and say in the run file which you chose. Cover at least the segments and their margins over the cycle, customers and suppliers, pricing through the last inflation, acquisitions and their goodwill, debt and leases, buybacks and their prices, stock pay, and litigation and investigations.
- Competitors for Q2: take the rivals the company's own annual report names, up to three that file with the SEC, read from their own filings, and flag the named rivals that do not file with the SEC (a rival with its own primary annual report may be read from that, said so). Compare over the whole span, never one year.
- The hard sequence. After a closing STOP, every figure is headed COMPUTATION, NOT A CLEARANCE (the protocol's heading,
  written without the dash). If no STOP among Q1 to Q6 closes the file (Q3 and Q6 are weighings, recorded and carried; Q6 carries a narrower STOP on an all-stock deal in undervalued stock, and Q3 hands its debt test to Q9), do Q7; Q7 is itself a STOP, and only if it passes do Q8 to Q10, and Q12 where it applies. Q6's buyback test needs the bottom of Q7's range: write that line back into Q6 and commit it with Q7. If the box is TOO HARD (WORK), write research-pass steps 1 and 2
  at the end (single-fact OUT answers; span and source fixed; how step 4 closes; a capital test sets earnings after
  depreciation against capital employed, or cash earnings against capital spending, never one against the other; a margin
  comparison covers the whole span) and do not run them.

## Reporting, at the owner's request (a reporting convention, not a rule; nothing here is a verdict or entry language)
Report two figures, labelled COMPUTATION if the file closed before Q7: **(a)** the VALUE RANGE as Q7 builds it,
by Q7's range convention in full: the four specifics of the PG re-test (aggregate growth, all spending deducted, zero growth after year ten, a price above the top closes OUT) and the six more, (a) to (f): (a) a first or last window year that is aberrational sets the cycle base, (b) a decline is carried as the bottom, (c) acquisitions deducted with total growth, a merger (a deal paid in shares) on the combined averages, a signed unclosed deal beside, purchases stopping after year ten, and a serial acquirer on the organic pair, (d) working capital counted, (e) the maintenance case central where the filing allows the guess, (f) the cap, an absurd rate cut to the business's own sales growth; the floor is tested before the width; the literal window shown beside. Q7's text governs where this summary is short; **(b)** the FAIR
PRICE, the price at which the midpoint of the range earns the floor of about ten percent (computed as Part VII now states: each end case valued at ten percent, the two averaged), applied to owner cash after the company's own tax with no conversion (the floor's "pre-tax" means before the holder's tax). The tax treatment is the company's own tax (Q7, Whose tax); the central figure is on the all-equity basis with the
equity-only figure beside it (Q7, On what the floor is earned; both adopted 2026-10-06), and the run says which is which. There is no cheap price: the operator reads any price below fair as cheap (decision of 2026-10-06; the rule is Part VII, The owner's price, which is all the analyst reads of it). Report no
other price figure.

## Output
The run file, complete, with an honest self-audit and the section "What in the framework was wrong or unclear". No em dashes
in your own prose. Run `python tools/check_framework.py` (must PASS) and a check script in your working folder: no E-ids;
every M/L/R id in the CSV; every quoted fragment beside an id is in that row.

## Reply with
Box and deciding question (and the TOO HARD cause); key filing facts per STOP; owner cash; the two reporting figures (said "three" until 2026-10-06, a leftover of the cheap price) against
the price; the balance-sheet reading; the competitor comparison; the strongest evidence against; what you could not get; what
you saw of the blind-listed files.
