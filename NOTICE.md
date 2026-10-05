# NOTICE — provenance, copyright and what the public copy withholds

*Written 2026-10-04 for the public copy of this repository. The working copy is private; the public copy is an
export of its tracked files made by `tools/publish_public.py`, which this file describes.*

## Whose words these are

The framework documents, the ledger, the run files and the tools are this project's own work (Chris Hrehor, with
Claude). **The quoted words are not.** Every rule in the framework rests on a short verbatim passage by Warren
Buffett or Charlie Munger, cited by year and source file, reproduced here for commentary, criticism and
verification: another analyst must be able to check any rule against its source in under two minutes. The
passages are the sentences that carry a lesson, never whole letters or answers.

## The source texts, folder by folder

| Folder | What it holds | Where it came from | Standing |
|---|---|---|---|
| `Shareholder Letters/` | Berkshire Hathaway chairman's letters 1965 to 2025 | 1977 to 2025 from berkshirehathaway.com; 1965 to 1976 and `Corporate Genealogy.txt` from a third-party archive (berkshire.memorex.ai). See `Shareholder Letters/_SOURCES.txt` | Berkshire Hathaway's copyright. The 1977 to 2025 letters are published free by Berkshire on its own site |
| `Annual Reports/`, `Quarterly Reports/` | Berkshire's printed annual reports FY1995 to FY2025 and 10-Qs 1996 to 2026, as text | berkshirehathaway.com | Berkshire Hathaway's copyright; published free on its site. Context for the letters; only the chairman's signed sections are on the citation shelf |
| `Annual Meetings/` | transcripts of the Berkshire annual meetings 1994 to 2025 | personal-study copies from berkshire.memorex.ai, fetched by `Annual Meetings/brk-meetings.ps1` | **The archive's notice prohibits reproduction and distribution of its copies.** The words are Buffett's and Munger's, spoken in public; the transcription is the archive's. These files are included at the repository owner's decision and will be removed on request from the archive or from Berkshire; open an issue |
| `Partnership Letters/` | Buffett Partnership letters 1957 to 1970 | a compiled PDF from the Ivey Business School archive, split into one file per letter. See `Partnership Letters/_SOURCES.txt` | historical letters widely republished; the compilation is Ivey's |
| `Wesco Letters (Munger)/` | Charlie Munger's Wesco Financial letters 1997 to 2009 | Wesco's published letters | historical letters, widely republished |
| `Munger Talks (PCA)/` | the eleven talks of *Poor Charlie's Almanack*, with front and end matter | Stripe Press's official free web edition (stripe.press/poor-charlies-almanack). See `Munger Talks (PCA)/_SOURCES.txt` | **Copyright Stripe Press / the Munger estate.** Published free online by the publisher; this is a text extraction of that edition, included at the repository owner's decision and removable on request |
| `Owners Manual/` | *An Owner's Manual* | berkshirehathaway.com | Berkshire's; published free |
| `Fortune Essays (Buffett)/` | Buffett's Fortune essays of 1977, 1999 and 2001 | the 1999 and 2001 PDFs are Berkshire's own copies hosted at berkshirehathaway.com; the 1977 text from a mirror. See `Fortune Essays (Buffett)/_SOURCES.txt` | **Fortune's copyright** on the articles; two are redistributed by Berkshire itself |
| `Special Letters/` | the 2014 fiftieth-anniversary pair, Buffett's and Munger's | inside Berkshire's 2014 annual report | Berkshire's; published free |
| `Buffett Pledge Letters/` | the giving-pledge material | public letters | off the citation shelf; context only |
| `Ben Graham/` | a separate side project; Graham is off the shelf | this project's own files | this project's |

Transcript and OCR artifacts are kept as found and never smoothed (PRIME RULE 1 in `Framework/OPERATOR-PROTOCOL.md`).

## What the public copy withholds

- **`PORTFOLIO.md`**, the repository owner's own holdings, cost bases and standing orders. A stub stands in its
  place so the acceptance test's pointer check passes. Every verdict the framework reached on a business is in
  `Test Runs/` and in the register in `Screens/WATCHLIST RUN QUEUE.md`; only the owner's positions are withheld.
- *(Until 2026-10-05, when v5 was adopted and the file was published:)* **`principle_ledger_v5.csv`**, the 4,279-row ledger of the v5 blind read, until v5 is adopted or refused (its
  pre-registration, `Framework/v5/PREREGISTRATION - v5 blind read and comparison.md`, said it would not be published
  during the read). The v5 case, pre-registration, reading register, notes, theme maps and drafts are all here, and
  quote the rows by id. The acceptance test resolves the v5 id class only when that ledger is on disk.
- *(From 2026-10-05, at the owner's instruction:)* **the holding files in `Test Runs/`**: holding reviews, notes on
  holdings, hold reads and research passes. They carry the owner's share counts, cost bases, accounts and keep-or-sell
  words. The purchase runs, written blind and carrying no position, stay public.
- **`Test Runs/_research*/`**, the raw filings, data pulls and scratch files behind each run (about 2.4 GB). Every
  run file names its filings by accession number so they can be fetched from SEC EDGAR.
- **`MBA - UNG/`** and **`Curriculum/`**, coursework and a class charter that share the working repository and have
  nothing to do with the framework.
- Caches (`tools/_cache/`, `Backtests/bt17_cache/`), logs and the lock file, which are gitignored in both copies.

In the five pointer documents the acceptance test reads (`CLAUDE.md`, `README.md`, `Framework/README.md`,
`Framework/OPERATOR-PROTOCOL.md`, `PORTFOLIO.md`), the export writes the two withheld file names without backticks
so that check 6 does not look for them; that is the only text the export changes.

## Licences

Code (`tools/`, `Screens/*.py`, `Backtests/scripts/`, the cycle scripts) is under the MIT licence (`LICENSE`). The
project's own documents (the frameworks, the ledger's structure and notes, the run files, the registers, this file)
are under Creative Commons Attribution 4.0 (`LICENSE-DOCS.md`). **Neither licence covers the quoted words of Buffett
and Munger or the source texts in the folders above**, which remain their authors' and publishers'.

## Not advice

This is a personal research project. Nothing in it is a recommendation to buy or sell any security. The
framework's market-beating claim is **unproven**, and `README.md` says so in full (operator rule 7).
