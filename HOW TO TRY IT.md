# HOW TO TRY IT — running the frameworks yourself

*Written 2026-10-04 for the public copy of this repository. Everything here works from a clone; nothing needs an
account except the free SEC EDGAR access the tools use, which asks only for a contact string in the request header.*

## What you have in front of you

Three editions of one idea, each built from verbatim Buffett and Munger quotes and nothing else:

| Edition | Where | Standing |
|---|---|---|
| **v3.0 / v3.1** (July 2026): eight gates, two valuation books, a Graham companion | `Framework/ARCHIVE - v3.x (superseded 2026-08-26)/` and `Framework/ARCHIVE - RULINGS 1-14 (resolved into v4, 2026-08-26).md` | superseded; kept as the audit trail; never applied |
| **v4.1** (August 2026): six questions, four verdicts, one book; every rule a quote with its ledger id | `Framework/THE FRAMEWORK v4.md` and `Framework/THE HOLDINGS FRAMEWORK.md` | **in force**: every run and review in `Test Runs/` since 2026-08-28 is under it |
| **v5** (October 2026): a candidate built by a blind read of the 32 annual-meeting transcripts and the reports they discuss, into its own ledger | `Framework/v5/`: the case, the pre-registration, the reading register and notes, the theme maps, the section drafts | candidate; not in force until a written comparison against v4.1 and a ruling case the operator approves |

The map of the whole repository, with a status word for every file, is `CLAUDE.md`. The rules of work that bind a
run are `Framework/OPERATOR-PROTOCOL.md`. The honest record of what the frameworks have and have not been shown
to do is in `README.md` ("Does it actually work?"): the market-beating claim is **unproven**, and every backtest
that beat the market was withdrawn for a look-ahead bug.

## 1. Check the build

```
git clone https://github.com/chrehor36/long-term-business-analysis.git
cd long-term-business-analysis
python tools/check_framework.py
```

Python 3.10 or later, standard library only. The acceptance test runs six checks and should end in `PASS`: no
phantom citation in any governing document, no number without a ledger id or a CONVENTION label, a well-formed
ledger whose every row's source file is on disk, every ledger row matched verbatim against its source document,
no phantom citation in any of the run files, and every path named in a pointer document present. If it fails on
a fresh clone, open an issue with the output.

## 2. Verify a rule in under two minutes

Pick any rule in `Framework/THE FRAMEWORK v4.md`. It carries a bold id like **[E4-28]**. Find that id in
`principle_ledger.csv`: the row gives the exact quote, the year and the source file. Open the source file and find
the quote. That is the project's standard, and `python tools/ledger_verbatim.py` does it for all 311 rows at once.

## 3. Run a company through v4.1

1. Read `Framework/OPERATOR-PROTOCOL.md` (nine rules, six prime rules), then `Framework/THE FRAMEWORK v4.md`.
2. Copy `Test Runs/_TEMPLATE - Company Run.md` to a dated file, `Test Runs/<date> Run - <TICKER> <name>.md`,
   **before** fetching anything (operator rule 1: the template is the enforcement surface).
3. Pre-fill the arithmetic: `python tools/run.py TICKER` prints it; `python tools/run.py TICKER --write` fills the
   file. The tool fetches the filing facts from SEC EDGAR and the sovereign yield from the issuing authority. It
   leaves every judgment field blank; a tool may get the same number sooner, it may never add a number.
4. Read the filing. Record the document, date and accession number, and cross-check one figure against the filed
   statement (operator rule 4). Tagged data is screening, never a verdict.
5. Answer Q1 to Q6 in order and stop at the first that is not IN. Every judgment cites a ledger id. No valuation
   is reported unless Q1 to Q4 each show IN; arithmetic produced earlier is headed `COMPUTATION — NOT A CLEARANCE`.
6. Complete the self-audit at the end of the template. A run is incomplete until it is checked.
7. Run `python tools/check_framework.py` before committing; check 5 will catch a citation that does not resolve.

`Test Runs/` holds about 430 finished runs to read as examples; `Test Runs/README - which run files are in
force.md` says which bind. The register of every run is under `## COMPLETED FROM THE QUEUE` in
`Screens/WATCHLIST RUN QUEUE.md`.

## 4. Review a holding

Copy `Test Runs/_TEMPLATE - Holding Review.md` and answer H1 to H5 under `Framework/THE HOLDINGS FRAMEWORK.md`.
An add to a position is a purchase and runs the purchase framework.

## 5. Follow or extend the v5 candidate

`Framework/v5/PREREGISTRATION - v5 blind read and comparison.md` fixes the design, the blind rule, the pass rules
and the hazards, and its results section records the read as it went. `Framework/v5/synthesis/` holds the theme
maps, the operator's structure decision and the section drafts. The v5 ledger itself is withheld until v5 is
adopted or refused (see `NOTICE.md`); the drafts quote its rows by id. To run the read on another corpus, the
machinery is `Screens/_daily/_v5_read_prompt.md` (the protocol a reading session follows), `tools/v5_ledger.py`
(the only way rows enter the ledger; it refuses any quote that does not match its source) and
`Screens/_daily/_v5_order.txt` (the units).

## 6. Rebuild or extend the corpus

The source texts are included (see `NOTICE.md` for their provenance and standing). The scripts that fetched them
are `Annual Meetings/brk-meetings.ps1` and `Shareholder Letters/brk-reports.ps1`; the `_SOURCES.txt` file in each
folder says where its texts came from and how they were extracted. Adding a document means adding its file to the
right shelf folder and, if a rule is to rest on it, a ledger row first (PRIME RULE 6: the row before the rule).

## What is not here

`PORTFOLIO.md` (the owner's holdings; a stub stands in), `principle_ledger_v5.csv` (until adoption), the raw
filings behind each run (fetch them by the accession numbers the run files give), and the owner's coursework.
Details in `NOTICE.md`.
