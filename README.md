# A Framework for Long-Term Business Analysis

> **Just want the results?** [Passed Companies](Passed%20Companies/README.md): every business that passed, in plain
> English, sorted by how close its price is to our fair price.

## Where things stand (2026-10-29)

| | |
|---|---|
| **Framework in force** | v5 (`Framework/THE FRAMEWORK v5.md`), since 2026-10-05: twelve questions in the speakers' own order, three boxes (IN, OUT, TOO HARD) |
| **Companies analysed under v5** | 424, in 432 runs (one run file each in `Test Runs/`) |
| **Passed every business question** | 114, each with a plain-English page in `Passed Companies/` |
| **Bought (IN)** | none: every business that passed was priced above its value |
| **Price alerts** | 113, one per passer at its fair price, checked once a day; reaching one starts a fresh analysis, never a purchase. The older v4.1 price bands are all retired |
| **Still to run** | about 394 names in `Screens/_daily/_v5_rerun_order.txt` |
| **How runs happen** | an automated session on weekdays, 8:00 to 16:00 US Eastern, at most ten a day, each one audited the same evening |

Without the regulated utilities (whose returns a regulator caps, so most pass the business questions and few are ever
cheap), about one business in four passed. The lists that fed the queue were already chosen for quality, so that rate
is higher than a random sample of listed companies would give.

*This file described the v3.0 framework (eight gates, two valuation books, a Graham companion, a
10:1 leverage ceiling) from 2026-07-25 until 2026-09-25, two editions after those rules were deleted.
Rewritten on 2026-09-25 to match the documents in force. The section "Does it actually work?" is a
record and is kept word for word, with a dated addendum after it. The map of the repository for a
working session is `CLAUDE.md`.*

A rules-based method for deciding whether a business is worth owning, and whether one already owned
is worth keeping, built only from primary sources: the Berkshire Hathaway shareholder letters
(1965 to 2025), the Buffett Partnership letters (1957 to 1970), the Wesco letters, the annual meeting
transcripts (1994 to 2025), An Owner's Manual, Poor Charlie's Almanack, Buffett's Fortune essays and the
2014 fiftieth-anniversary pair.

**The standard the whole project is held to**: every rule either traces to a verbatim quote in that
corpus, cited by ledger id, or is labelled `CONVENTION` with a one-line rationale, or it is deleted.
Another analyst should be able to verify any rule against its cited source in under two minutes.
`tools/check_framework.py` enforces the machine-checkable half of that on every run.

## Why this exists

Most "value investing" writing repeats a small set of secondhand slogans, margin of safety, moats,
circle of competence, without ever pointing at the sentence they came from. This project started from
the opposite question: **if we throw out everything that cannot be traced to a primary source, what is
actually left?**

The first pass found the answer uncomfortable: a claims audit of the prior edition
(`Framework/ARCHIVE - May 2026 (superseded)/claims_audit.csv`)
turned up misattributed quotes, claims that existed nowhere in the corpus, and inventions passed off as
Buffett's or Munger's own words, including a famous "30-year Treasury... that's my yardstick" quote that,
verbatim, does not exist. The v3.0 rebuild corrected every one of them. The v4 audit of 2026-08-26 then
found that the rulings layered on top of v3.0 had added 43 numeric rules with no quote behind them, and
deleted all 43 (`Framework/INVENTIONS - deleted and why.md`). **The text wins.** Where the framework and
the primary sources disagreed, the framework was the thing that changed.

## The two questions

*(Rewritten 2026-10-29 to describe v5, the edition in force. Until then this section led with v4.1 under a dated
note; that text is kept word for word below, under "The v4.1 edition".)*

v5 was built by a blind read of the 32 Berkshire annual-meeting transcripts (1994 to 2025) and the letters and
annual-report sections they discuss, into `principle_ledger_v5.csv`, and adopted on 2026-10-05 under
`Framework/v5/RULING CASE 2026-10-05 - adopt v5, for the operator's approval.md`. Every rule in it rests on rows of
that ledger only.

**Should I buy this?** is answered by `Framework/THE FRAMEWORK v5.md`: a preamble of foundations (a share is a
business; the market serves, it does not instruct; no macro forecast enters), a standing rule on how a purchase is
financed and held, then twelve questions in the speakers' own order. A STOP question that fails closes the file; a
WEIGHING question is recorded and weighed with the others. Every file ends in one of three boxes, from Munger's
"in, out, and too hard" **[M2006-013]**: **IN**, **OUT** or **TOO HARD**.

| | Question | Kind |
|---|---|---|
| Q1 | Can I understand it, and where its economics will be in ten or twenty years? | STOP |
| Q2 | Why is the castle still standing, and what keeps it standing? | STOP |
| Q3 | How much capital must go in to get the earnings out? | WEIGHING |
| Q4 | Do the numbers show what it earns after every real cost? | STOP on confusion |
| Q5 | Who runs it? Able, honest, and the same once paid | STOP on integrity |
| Q6 | What will they do with the money and with the owners? | WEIGHING |
| Q7 | What is it worth, held as a range, and is the price far enough below it? | STOP |
| Q8 | Is it better than the alternatives: the bond, more of what is owned, buying in its own stock? | STOP |
| Q9 | Could it ruin us? The target's debt and exposures | WEIGHING |
| Q10 | Is it the fat pitch, and is the size right? | WEIGHING |
| Q11 | Having bought: has the business changed, or only its price? | WEIGHING |
| Q12 | (optional) Would we be proud of how the money is made? | STOP for named businesses |

A business "passes" when it is IN at every business question (Q1 to Q6). Q7 then values it: a range of what it is
worth, and a **fair price**, the price at which the middle of that range earns about 10% a year for an owner. A
passer priced above its fair price closes OUT at Q7 and gets a price alert at the fair price; reaching it starts a
fresh analysis, never a purchase by itself. The passers are listed in plain English in `Passed Companies/`.

**Should I keep what I own?** is answered by `Framework/THE HOLDINGS FRAMEWORK v5.md`: the default is to keep, a
price move alone is not a reason to sell, and six questions ask what has changed (the business or only its price,
the castle, the management, what retained money earns, a plainly better use for the money, and whether the purchase
was a mistake). An add to a position is a purchase and runs the purchase framework in full.

### The v4.1 edition (2026-08-28 to 2026-10-05), kept as written

**Should I buy this?** was answered, from 2026-08-28 to 2026-10-05, by `Framework/ARCHIVE - v4.x (superseded 2026-10-05)/THE FRAMEWORK v4.md`. Six questions in order, and the
analysis stops at the first that is not IN. Every question ends in one of four verdicts: IN, OUT,
UNRESEARCHED (the document exists and has not been read) or UNKNOWABLE (the evidence is in and the
future is still indeterminate).

| | Question |
|---|---|
| Q1 | Can I understand how this makes money? |
| Q2 | Is it a franchise? A moat is a relative claim, so the competitor row is required. |
| Q3 | Are they honest, and are they rational? |
| Q4 | Will it survive? Owner earnings, not net income; the named way this business dies. |
| Q5 | What is it worth, against a government bond? The floor first; what clears it ranks. |
| Q6 | What would prove me wrong, and when do I sell? |

**Should I keep what I own?** was answered, over the same period, by `Framework/ARCHIVE - v4.x (superseded 2026-10-05)/THE HOLDINGS FRAMEWORK.md`: five hold questions
and four outcomes for a position already held. An add to a position is a purchase and runs the purchase
framework.

Owner earnings is the one number: a multi-year mean, maintenance capex rather than total capex, the
working-capital increment included, and the maintenance figure a disclosed judgment, because Buffett says
it "must be a guess." A discounted-cash-flow model may run as an engine to convert growth into a rate; it
casts no vote.

## How a run works

*(Rewritten 2026-10-29 for v5. It said, from 2026-09-25, "No valuation is reported unless the four business
questions each show IN", a v4.1 rule.)*

Every company gets a dated run file copied from `Test Runs/_TEMPLATE - Company Run.md` and filled top to
bottom; the template's self-audit is the enforcement surface. The questions are answered in order and the first
failing STOP closes the file. Facts already found that bear on a later question are written down after the stop,
not weighed, and Q7's arithmetic is still computed beneath the stop, headed "COMPUTATION, NOT A CLEARANCE", so every
file carries a value range where one can be built. Tagged XBRL data is transcription and screening; the filing
itself gets read, and one figure is cross-checked against the filed statement. The sovereign yield comes from the
issuing authority for the earnings currency. Arithmetic is automated (`tools/run.py`); judgment is made by the
analyst and justified by a v5 ledger id, or labelled as opinion. The binding rules are in
`Framework/OPERATOR-PROTOCOL.md`.

Runs are folded into the register (`Screens/WATCHLIST RUN QUEUE.md`); a passer is added to
`Screens/V5 PASSERS - the alert list.md`, its fair price is armed in `tools/alerts.json`, and its plain-English page
is written. `tools/price_alerts.py`, run with `--v5-only`, checks the armed fair prices once a day at 10:00 US Eastern, and
`tools/daily_fetch.py` writes a daily digest of the bond rate, new filings and the distance of every passer to its
fair price.

## Does it actually work? Honest answer: we don't know yet — and we found a bug that explains why we thought we did.

This section previously reported that the full eight gates beat the market at
three of four tested dates. **Those results have been withdrawn.** On
2026-07-25 the screen that produced them was found to contain a look-ahead
bug, and the correction is documented in full in `Backtests/` (dated
CORRECTION sections appended to BT-9, BT-10, and BT-14).

**The bug.** Market cap was computed as `price × shares_at_anchor`. Both
Yahoo price fields are back-adjusted to *today's* share basis, while the
share count is the true point-in-time figure — so market cap was understated,
and owner-earnings yield overstated, by the cumulative split factor occurring
*after* the anchor date. AAPL at 2013-06-30 computed to $11.7B against a real
~$372B.

**Why it mattered so much.** Companies that split are overwhelmingly companies
whose stock rose. The bug inflated the measured yield of future winners
specifically — and since candidates were picked as the top-N by yield, it fed
look-ahead bias straight into selection. The screen was finding future winners
*because* they were future winners. Re-tested against the corrected screen,
only 5 of BT-10's 18 survivors still clear Book One; NVDA, the largest single
contributor to the headline result, misses the 4% hurdle at **0.31%**.

**What still stands.**
- **The mechanical layer is a coin flip — and this survived the correction.**
  Recomputed on the fixed engine across 944 one-year holdings at 13 anchors
  (2013-2025), the bare Book One screen wins **49.6%** of the time against SPY,
  with the median pass trailing by 1.45 points. The pre-correction figures were
  49.3% and −1.4 points, on a far smaller and dirtier sample. The reason the
  number barely moved is itself the point: the bug biased selection toward
  *long-run* winners, which says little about the *next twelve months*, so a
  one-year test was nearly immune to it while the multi-year full-gate tests
  were destroyed by it. Details: `Backtests/` BT-16.
- **The loss-avoidance evidence.** Gate 3 caught the same companies for the
  same real, filed reasons at independent dates (Fifth Third at three separate
  anchors; KLA and Franklin Resources at two each). Those rest on litigation
  and filings, not prices.
- **The corrected mechanical screen itself**, now validated against
  `dei:EntityPublicFloat` — the filed 10-K cover-page market value, available
  for 553/558 companies. The project had *no* independent market-cap check
  before, which is precisely how this survived four backtests. Corrected
  passes by anchor date: 79 (2013), 69 (2014), 99 (2015), 109 (2016), 79
  (2017), 80 (2018), 85 (2019), 96 (2020) — against 141-181 before.
- **BT-11**, the one full-gate test that used manual 10-K price extraction and
  never touched this screen. It *underperformed* SPY over 32 years.

**Where that leaves the thesis.** Every test that beat the market ran through
the buggy screen; the only uncontaminated one lost. So the framework's
market-beating claim is **unproven**, not disproven — the corrected candidate
lists are different companies and the qualitative gates have not yet been
re-run against them. The loss-avoidance half is unaffected. Rebuilding the
full-gate tests on corrected data is the current work.

We are leaving this failure written down rather than quietly re-running until
the numbers look good again. **The text wins** applies to our own results too.

**Addendum, 2026-09-25.** The section above was written on 2026-07-25 and is kept as written. What was
tested afterwards, with the write-ups in `Framework/v4/`: BT-15 re-ran the corrected basket at eight
anchors and it beat the index at two of them (`Framework/v4/PROOF - tests A, B and C, and what they
found.md`). Test E, pre-registered, tested the loss leg alone and passed thinly; BT-17 replicated it on
2026-08-28 in a thirteen-anchor S&P panel and a two-anchor micro-cap panel, thin and survivorship-conditioned,
with the return leg still trailing (`Framework/v4/TEST E - PREREGISTRATION - the loss leg.md`,
`Framework/v4/BT-17 - PREREGISTRATION - SP500 replication and the microcap panel.md`). Test D, also
pre-registered, read the corpus against v4 and failed it, which produced v4.1. The market-beating claim
remains unproven, and the corpus itself attributes Berkshire's record to the man, the system, luck and
devotion, not to a selection method alone. The "eight gates" and "Book One" named above were the v3.0
structure; v4.1 has six questions and one book. The 4% hurdle named above was also v3.0: v4.1 tests a price first
against a floor of about 10% [E4-28], and only what clears the floor is ranked against the government bond.

**Addendum, 2026-10-29.** Under v5, in force since 2026-10-05, the market-beating claim stays **unproven**, as
`Framework/THE FRAMEWORK v5.md` records in its second paragraph; no backtest has been run under v5.

## Opening this project in a new Claude Code session

*Added 2026-10-02.* A new session understands this project **only if it is opened in this folder**
(C:\Projects\BRK since the move of 2026-10-25; C:\Users\chreh\OneDrive\Documents\BRK before it). Opened anywhere else, including the parent Documents folder,
none of the three items below loads.

What a new session picks up on its own:

| What | Where it lives | What it gives the session |
|---|---|---|
| The map | `CLAUDE.md` | loaded automatically; what every folder is, which files govern, the order to read them in |
| The rules | `Framework/OPERATOR-PROTOCOL.md` | imported by `CLAUDE.md`, so the binding rules load too (tested in a fresh session on 2026-09-25) |
| Memory notes | outside the project, under the user's .claude folder, tied to this folder's path on this computer | standing preferences (no em dashes, run locally, commit with a pathspec) and where the queue stands |

What it does not get: the previous conversation word for word. Everything that matters is written down
instead. The last dated section of `Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md` says
where every queue stands (running or paused), the results so far, the open items and how to resume.

What breaks it:
- **Opening a different folder.** `CLAUDE.md` and the memory notes do not load.
- **Using a different computer.** The memory notes and the Windows scheduled tasks (`BRK-overnight`,
  `BRK-audit`, `BRK daily fetch`, `BRK price alerts`) exist only on the machine that created them
  *(until 2026-10-29 this line said the files sync through OneDrive and listed `BRK resume queue`; the project
  left OneDrive on 2026-10-25 and that task was not recreated)*.

A good first message in a new session:

```
Read the last section of the RESUME STATE file in Screens/ and tell me where things stand.
```

## Repository structure

| Folder or file | What it holds |
|---|---|
| `CLAUDE.md` | the map of the repository: every folder, its entry point and its status; what a session reads first |
| `Framework/` | the two governing documents, the operator protocol, the sector method, the proofs and tests in `Framework/v4/`, and the archives of every earlier edition |
| `principle_ledger_v5.csv` | the evidence base of v5: one verbatim passage per row with year and source, from the meeting transcripts and the letters they discuss; every citation in the v5 documents resolves to a row here |
| `principle_ledger.csv` | the evidence base of v4.1 and earlier editions, kept as their record |
| `Passed Companies/` | one plain-English page per business that passed, and an index sorted by price against fair price; built by `tools/passed_pages.py` |
| `Test Runs/` | one run file per business, its research folder, the addenda that correct runs after the fact, and the two templates |
| `Screens/` | the register of every run, the v5 passers list, the survival-shapes index (v4.1 record), the session-state file, the operator's lists and the overnight automation in `Screens/_daily/` |
| `tools/` | the acceptance test, the fetch-and-arithmetic library, the run pre-filler, the daily digest and the price alerts |
| `Backtests/` | the point-in-time tests of the mechanical layer, including the withdrawn ones and their corrections |
| `Shareholder Letters/`, `Partnership Letters/`, `Wesco Letters (Munger)/`, `Annual Meetings/`, `Munger Talks (PCA)/`, `Owners Manual/`, `Fortune Essays (Buffett)/`, `Special Letters/` | the citation shelf, one text file per document |
| `Annual Reports/`, `Quarterly Reports/`, `Buffett Pledge Letters/` | Berkshire's own reports and the pledge material, context only, not on the shelf |
| `Ben Graham/` | a separate Graham side project; Graham is off the shelf and is cited only as Buffett and Munger cite him |
| PORTFOLIO.md | holdings, standing lines, the ranked opportunity set and the reviews owed |
| MBA - UNG/, `Curriculum/` | **ignore both.** University coursework and a class charter that share the repository; nothing in the framework depends on them, and neither is read, searched, cited or edited in framework work |

## The public repository

*Added 2026-10-04.* This project is published at github.com/chrehor36/long-term-business-analysis as an export of
the working repository's tracked files, made by `tools/publish_public.py`. `HOW TO TRY IT.md` says how to check
the build, verify a rule, run a company through the framework in force, review a holding and read the record of how v5
was built and tested. `NOTICE.md` gives the provenance and copyright standing of every source folder and lists what the
public copy withholds: the owner's holdings file (a stub stands in), the holding reviews, the raw filings behind each run, and the
coursework. The v5 ledger was withheld until adoption and is published from 2026-10-05. From 2026-10-06 the research
folders behind the purchase runs are published too (the scripts, outputs and notes, so a reader can reproduce each run's
arithmetic); the raw filings and XBRL pulls stay out because they are the SEC's own documents and run to many gigabytes,
and `NOTICE.md` gives the EDGAR address form by which any accession number a run records reaches its document. Code is under the MIT licence (`LICENSE`); the project's documents are under CC BY 4.0
(`LICENSE-DOCS.md`); the quoted words of Buffett and Munger and the source texts are their authors' and publishers'.

## The one rule everything else follows from

**Verbatim or confessed, never invented and unlabelled.** If a claim cannot be traced to a quoted primary
source it is labelled `CONVENTION` with its rationale, or it does not go in the framework at all. And a
label may confess an invention; it may never license what a rule forbids.

---
*This is a personal research project, not investment advice. Nothing here
constitutes a recommendation to buy or sell any security.*
