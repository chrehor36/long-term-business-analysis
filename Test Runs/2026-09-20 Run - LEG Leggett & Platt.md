# Company Run — Leggett & Platt, Incorporated (LEG) — 2026-09-20
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

> **THIS RUN CLOSES AT STEP 0, BEFORE Q1 OPENS.** Leggett & Platt ceased to exist as a
> public security on **2026-08-26**. It was merged into Somnigroup International Inc.,
> delisted from the NYSE, and deregistered. **Q1 through Q6 are unwritten and unscored, and
> no verdict about the business is recorded.** The evidence is in STEP 0 below.
>
> WAVE 7, name 2. The register tally is not carried into this file as a fact; the session
> holding the fold recounts it.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

### 0.1 THE SOVEREIGN, struck today and not inherited from the brief

- rate **5.34%** · date **2026-09-18** · source **US Treasury daily par yield curve,
  30-year par yield**, from the issuing authority (`python tools/sources.py`, run
  2026-09-20; 2026-09-18 is the most recent published print, 2026-09-19 being a Saturday
  and today a Sunday). **FRED DGS30 was not used**; the Treasury is the issuing authority
  and FRED is the fallback.
- Adjacent sovereigns from the same fetch, recorded but not used: JPY 4.05% (2026-09-17,
  Japan MOF), EUR 3.75% (2026-09-17, ECB).
- FX / ADR: none. Leggett & Platt reported in USD.
- **The rate is recorded because STEP 0 asks for it. It is never used in this file: the
  sovereign is the second test at Q5, and Q5 does not open.**

### 0.2 THE DEAL. This is the finding, and it is not a live deal, it is a closed one.

The screen row carried a **LIVE DEAL FORM** flag pointing at a Form 425 of 2026-04-13. The
brief's instruction was to resolve it by reading, not by inference. Reading it resolves it
in the opposite direction from the flag: **the transaction is not live, it is completed, and
Leggett & Platt is gone.** The chain, every link taken from the filing index of CIK
`0000058492`:

| date | form | accession | what it says |
|---|---|---|---|
| 2026-04-13 | **8-K, Item 1.01** | `0001193125-26-151966` | Agreement and Plan of Merger with **Somnigroup International Inc.** (Parent, Delaware) and **Sparrow Unity Corporation** (Merger Sub, Missouri). Each LEG share converts into **0.1455 shares of Somnigroup common stock**, cash in lieu of fractions. *"It is expected that the Merger will qualify as a tax free reorganization for U.S. federal income tax purposes."* |
| 2026-04-13 → 2026-08-06 | **425** ×6 | incl. `0001193125-26-153129`, `0001206264-26-000101` | merger communications. `0001193125-26-153129` is the one the screen row names, and it is a 425, i.e. a merger communication, exactly as the flag's wording implied |
| 2026-07-09 | **DEFM14A** | `0000058492-26-000364` | definitive merger proxy. Somnigroup's Form **S-4 (File No. 333-296998)** was declared effective by the SEC the same day |
| 2026-08-06 | **10-Q** | `0000058492-26-000430` | **the last periodic filing Leggett & Platt will ever make** |
| 2026-08-21 | **8-K, Items 5.07, 7.01** | `0001193125-26-361156` | results of the special meeting |
| **2026-08-26** | **8-K, Items 1.02, 2.01, 3.01, 3.03, 5.01, 5.02, 5.03** | `0001193125-26-366694` | **the merger closed** |
| 2026-08-27 | **Form 25-NSE** | `0000876661-26-000712` | NYSE removes the common stock from listing and registration, Rule 12d2-2(a)(3) |
| 2026-08-27 / 08-28 | **S-8 POS, POS AM, POSASR**, 50+ of them | various | post-effective amendments deregistering all unsold securities |
| **2026-09-08** | **Form 15-12G** | `0001193125-26-384400`, `0001193125-26-384395` | **termination of registration**, Rules 12g-4(a)(1) and 12h-3(b)(1)(i) |

**The completion 8-K, verbatim** (`d152590d8k.htm`, 2026-08-26):

> "On August 26, 2026 (the "Closing Date"), Sparrow Unity Corporation, a Missouri
> corporation ("Merger Sub") and wholly owned indirect subsidiary of Somnigroup
> International Inc., a Delaware corporation ("Parent"), merged with and into Leggett &
> Platt, Incorporated, a Missouri corporation (the "Company"), with the Company continuing
> as the surviving corporation (the "Merger" and the time of consummation thereof, the
> "Effective Time") pursuant to the previously announced Agreement and Plan of Merger, dated
> as of April 13, 2026"

> "each share of Company common stock, par value $0.01 per share ("Company common stock"),
> issued and outstanding immediately prior to the Effective Time … was automatically
> converted into the right to receive 0.1455 shares (the "Exchange Ratio") of Parent's
> common stock"

> "the Company notified the New York Stock Exchange ("NYSE") that the Merger had been
> consummated and requested that the trading of Company common stock on NYSE be suspended
> and that the listing of Company common stock on NYSE be withdrawn."

*(PRIME RULE 1, an artifact caught and corrected inside this run rather than published.* My
first extraction stripped HTML tags by replacing each with a space, and because the filing
underlines its defined terms with an inline `<span>`, the output read `(the " Closing Date ")`
with spaces inside the quotation marks. Those spaces are **mine, not the filing's**, and the
first draft of this file recorded them as the source's own rendering, with a note asserting
the entities were `&#147;`/`&#148;`. Both were wrong: the raw document uses `&#8220;` and
`&#8221;` and has no interior spacing. The quotes above are re-extracted with block-level
tags mapped to newlines and inline tags removed without substitution, and verified against
the raw HTML byte for byte. **A tag-stripper that inserts spaces will fabricate whitespace
inside every defined term in an EDGAR document**, which is worth knowing before a run quotes
one.*)

**And the single line that settles it beyond argument.** The Form 15-12G of 2026-09-08 states
the holders of record of each class. For the common stock:

> "Common Stock, $0.01 par value – 1 holder"

**One holder of record.** Every public share was converted by operation of law. There is no
float, no quote, and no instrument to buy.

**What it does to the perimeter, stated plainly as the brief requires.** The form is
**all-stock, not cash**: a fixed exchange ratio of 0.1455, so LEG holders became Somnigroup
holders rather than being cashed out. The 10-Q of 2026-08-06 states the dilution:

> "Upon completion of the Somnigroup Merger, Leggett & Platt's shareholders are expected to
> own approximately 8.6% of the combined company, based on the number of shares of Leggett &
> Platt common stock and Somnigroup common stock outstanding as of the record date of the
> special meeting."

So the perimeter did not merely change, it was **absorbed**. Leggett & Platt survives as a
wholly owned indirect subsidiary. Its three reportable segments on the last filed basis
(**Bedding Products**, **Specialized Products**, **Furniture, Flooring & Textile Products**,
the Aerospace Products Group, which had sat inside Specialized Products, having been divested
on **2025-08-29**: MD&A, *"for a cash price, net of selling expenses and cash sold, of $280
million and recognized a pretax gain of $91 million after final adjustments for working
capital were completed in December 2025"*, and Note N of the same 10-Q gives the unrounded
figures, *"net cash proceeds of $280.3"* and *"a pretax gain of $90.9"*) are now segments of
somebody else's consolidation, reported on
somebody else's basis, against somebody else's capital structure. Its credit agreement was
repaid and terminated on the closing date and its commercial paper programme was shut. **An
owner-earnings series built from LEG's filings is a series for a company that has already
ended, and no Q5 can be computed against it, because the price term does not exist.**

### 0.3 THE QUOTE THE SCREEN CARRIED IS A DEAD QUOTE, AND IT RECONSTRUCTS EXACTLY

- **Last trade: $9.20, close of 2026-08-26**, the closing date itself, Yahoo Finance
  (*aggregator, flagged*). The aggregator **still serves this as `regularMarketPrice` today,
  2026-09-20, with exchange "NYSE"**, twenty-five days after the listing was withdrawn and
  twelve days after registration was terminated. It is a price for a cancelled security.
- Share count, from the cover of the newest periodic filing: **136,588,995**, from the
  **10-Q for the period ended 2026-06-30, filed 2026-08-06, accession
  `0000058492-26-000430`**, cover line: *"Common stock outstanding as of July 30, 2026:
  136,588,995"*.
- **136,588,995 × $9.20 = $1,256.6M**, against the screen row's `cap_m` of **1257**. The
  queue's market capitalisation is, to within rounding, **the suspended-trading close times
  the cover count**. Nothing was wrong with the arithmetic; the input had stopped existing.
- And the $9.20 is not a price for Leggett & Platt at all, it is a price for Somnigroup
  scaled by the exchange ratio. Somnigroup (NYSE: SGI, CIK `0001206264`) closed at **$63.36
  on 2026-09-18** (Yahoo, *aggregator, flagged*), and **0.1455 × $63.36 = $9.22**. The
  terminal LEG quote was the deal spread collapsed to zero, which is the ROKU lesson of
  2026-09-12 arriving one stage later than the flag anticipated.

### 0.4 THE FILING WAS READ, not tagged data **[E3-27, E4-14]**

- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes *(of the last 10-Q)*
- **primary document: Form 10-Q for the period ended 2026-06-30, filed 2026-08-06,
  accession `0000058492-26-000430`** (`leg-20260630.htm`). This is the **last** periodic
  filing; the FY2025 10-K is accession `0000058492-26-000107`, filed 2026-02-26.
- also read in full: the 8-K of 2026-04-13 (`0001193125-26-151966`), the 8-K of 2026-08-26
  (`0001193125-26-366694`), the Form 25-NSE (`0000876661-26-000712`), the Form 15-12G
  (`0001193125-26-384400`).
- **figure cross-checked against the filed statement** (operator rule 4): net cash from
  operating activities for the six months ended 2026-06-30. The Consolidated Condensed
  Statements of Cash Flows reads **"Operating Activities ( 10.3 )"**; XBRL
  `NetCashProvidedByUsedInOperatingActivities` for 2026-01-01→2026-06-30 returns
  **−10,300,000** under the same accession. They agree. The MD&A states the same figure in
  words: *"Cash from operations for the six months ended June 30, 2026 was $(10) million,
  down $101 million from the same period last year."*
- **Recorded, not scored:** operating cash flow for the final half-year was **negative**, a
  $101M year-on-year swing. That is a Q4 observation and **Q4 is not written in this file.**
  It is put on the record here only so a later reader does not mistake this closure for a
  file that was never opened.

### 0.5 WHY THE FILE CLOSES HERE, AND THE VERDICT FORM

`THE FRAMEWORK v4.md` answers one question: **"should I buy this?"** Here the question has no
object. There is no security, there will be no further filing, and there is no price term for
Q5. Writing Q1 through Q6 would produce a document that reads like a live analysis of a dead
perimeter, which is the precise failure the brief names.

**I hunted the disconfirming evidence for this conclusion hardest, because closing a file is
the cheap outcome and I have an incentive to reach it [E4-26, E3-41, operator rule 9].** Four
counter-arguments, each tested and each refuted from the filings:

1. *"Run the gates anyway, as preparation for a Somnigroup run."* **No.** Somnigroup is a
   different company: different management, different capital structure, different
   consolidation, different owner earnings. *"determining the competitive advantage of any
   given company and, above all, the durability of that advantage"* **[E4-08]** is asked of a
   company, and this file's company is not that company. If Somnigroup is to be run, it is
   run as **SGI, CIK 0001206264**, from its own filings, under its own file.
2. *"A stub may still trade over the counter."* **No.** Form 15-12G, 2026-09-08: *"Common
   Stock, $0.01 par value – 1 holder"*. There is one holder of record.
3. *"The notes still exist."* The Form 15 covers them too (3.50% 2027, 64 holders; 4.40%
   2029, 66 holders; 3.50% 2051, 35 holders) and suspends the reporting duty behind them. No
   filings will support a run, and this framework buys businesses, not bonds.
4. *"The closed file has a price"* **[E3-47]**: *"Typically, our most egregious mistakes fall
   in the omission, rather than the commission, category… their invisibility does not reduce
   their cost."* This is the strongest objection and it is answered rather than waved away.
   [E3-47] is about failing to buy something you understood **and could have bought**. LEG
   could not have been bought by this project at any price after 2026-08-26. Whatever
   omission exists here is a **screening** omission, not an investment one, and it is
   reported below as a tooling defect rather than buried.

**The verdict form.** The four verdicts attach to *questions about a business you could buy*.
None of them describes "the security has been cancelled":

- **OUT** would assert *"the evidence is here and the business fails"*. That is a false
  statement about Leggett & Platt and this run does not make it.
- **UNRESEARCHED** would be a work order. There is no artifact to fetch; every artifact was
  fetched, and they are what closed the file.
- **UNKNOWABLE** is where the separating test routes (*"Can I name the document that would
  resolve this?"*, and no document can, because the instrument no longer exists), and its
  *effect*, *"close without prejudice… No finding about the business"*, is exactly right.
  But its *definition*, *"evidence is in, the future is still indeterminate"*, is false here:
  the evidence is complete and the future is entirely determinate. Recording UNKNOWABLE would
  misreport the run.

**So this file records no framework verdict and closes as DEAD_OR_ACQUIRED**, which is this
project's own existing category and not an invention of this run: it is a bucket in the triage
table of `Screens/2026-08-31 PREPPED READING LIST (operator lists).md`, whose
*"Taken private / merged / renamed"* line already strikes twenty-nine names (MAXR, STOR,
KBAL, NCS, UFS, AIRC, ROIC, INFN, BERY, DRQ, CCT, ENLC, NSA, PLYM, GMRE, SKX, SEE, LANC,
CSGS, CSWI, HIBB, SCVL, MODG, RYI, USAP, KLX, COMM, CIVI, ALE) and whose stated rule is
*"A name failing that check is recorded and closed without a full run."* LEG is the
thirtieth, and the only one to reach a run file, because it died **after** the queue was
built.

**CONVENTION** *(confessed under PRIME RULE 3)*: using DEAD_OR_ACQUIRED as the outcome of a
*run* rather than of a *triage* is this run's small extension of an existing project
category. **Rationale:** the alternative was to force one of four verdicts that each say
something untrue, and PRIME RULE 5 forbids adding a fifth verdict without a written case
presented for approval first. **The gap is flagged to the operator in the register below
rather than patched here.** The label licenses nothing: no gate is passed, no name is
promoted, and no number in this file is used for anything.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY?
**UNWRITTEN AND UNSCORED.** The file closed at STEP 0. No verdict is recorded.

## Q2 — IS IT A FRANCHISE?
**UNWRITTEN AND UNSCORED.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
**UNWRITTEN AND UNSCORED.**

## Q4 — WILL IT SURVIVE?
**UNWRITTEN AND UNSCORED.**

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**DOES NOT OPEN.** Q1 through Q4 are unwritten, and independently there is no price term:
the security was cancelled on 2026-08-26 and the only quote an aggregator will serve is a
dead one.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**UNWRITTEN AND UNSCORED.**

---
## DEFECTS FOUND BY THIS RUN

**1. `tools/run.py LEG` gives a wrong answer, and it gives it in the form of a verdict.**
The whole output is:

> LEG: not an SEC filer. Use the evidence ladder: company IR site (English),
> exchange filings (TDnet / RNS / SEDAR+). This is UNRESEARCHED, not UNKNOWABLE.

Two separate faults.

*(a) The statement is false.* LEG **is** an SEC filer: CIK `0000058492`, 10-K filed
2026-02-26, 10-Q filed 2026-08-06. What actually happened is that `sources.cik_for('LEG')`
returns `(None, None)` because the SEC has removed LEG from the live
`https://www.sec.gov/files/company_tickers.json` following the Form 25 and Form 15. Verified
this session: LEG and CIK 58492 are both absent from that file, while `SGI` is present at CIK
`1206264`.

*(b) The tool concludes, which operator rule 8 forbids* — *"Tools fetch and compute and are
forbidden to conclude; every flag is a prompt to read, never a score."* It does not merely
fail to resolve a ticker; it names a verdict, **"This is UNRESEARCHED, not UNKNOWABLE"**, and
it names the wrong one. A run that obeyed it would have gone looking for RNS and SEDAR+
filings for a company in Carthage, Missouri.

*Constructive form of the fix, for the operator to rule on:* absence from
`company_tickers.json` for a ticker that the project's own queue carries with a recent 10-K
is a **delisting tell, not a foreign-filer tell**. `submissions.json` for the known CIK
answers it in one call, and **Form 25 and Form 15 are clean signals** in a way that
`Screens/RESUME STATE 2026-09-12` item 5 found **8-K Item 2.01 was not** (*"Incomplete and
unclean, so not built"*). Item 2.01 both misses disposals and false-positives on mistagged
earnings releases; a Form 15-12G does neither. This does not add a step, it replaces a wrong
sentence with a right one.

**2. The pricing path cannot see a delisting, and the queue therefore carried a cancelled
security with a live-looking cap.** `Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv`
(last written 2026-09-13) prices LEG at `cap_m 1257`, which this run reconstructs exactly as
136,588,995 cover shares × the $9.20 suspended close of 2026-08-26. The **deal flag fired
correctly** on the six Form 425s, and its wording is right as far as it goes, but it has no
state for *closed*, so it warned about a spread in a name that no longer had one. Two further
priced rows named in `Screens/RESUME STATE 2026-09-12` are in the same class and should be
re-read before they are run, not after: **ACLS** (*"party to a real merger so its band tracks
deal terms"*) and **CNR** (*"the CONSOL/Arch merger"*).

**3. `CLAUDE.md` and this brief both state the ledger at 267 rows. `principle_ledger.csv`
has 311.** Counted this session with `csv.DictReader` (note the file carries a UTF-8 BOM, so
the first column key is `﻿id`; read it with `encoding="utf-8-sig"` or every id lookup
returns a false phantom). The commit `63df593` of this project, *"Survival shapes index:
every ruled line names its ledger rows (**ledger 311**)"*, already records 311, so the KEY
FILES table in `CLAUDE.md` is the stale pointer, and it is stale against its **own**
instruction three words later: *"Count the file, never the pointer"*. The composition
sentence beside it (*"266 verbatim quotes plus one negative finding … carrying 262 distinct
passages"*) is arithmetic on the old count and has not been restated. Flagged and not edited:
`CLAUDE.md` is outside this run's permission.

**4. A brief defect, and it is the one that matters.** The brief's section 2 instructed:
*"The deal note is the first thing you resolve, and you resolve it by reading, not by
inference"*, and it named the right accession. That instruction worked, and it is why this
run found the closure in its first ten minutes. But every subsequent section of the brief
(3 through 8) was written on the assumption that the deal might be **live** and never on the
assumption that it might be **closed**: section 8 requires the final report to carry *"Price,
its date and source … share count … the computed cap"* as though a price must exist, and
section 4's Q1 through Q4 instructions presuppose a company that still files. **The brief has
no branch for a name that has already been acquired**, which is the same gap as defect 5.

**5. The framework itself has no verdict for "the security has been cancelled."** Set out at
0.5 above. Not patched: PRIME RULE 5 requires a written case presented for approval before a
structural change, and this run has no authority to make one. Recorded for the operator.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **The file closed at STEP 0, before
      Q1. Q1 through Q6 are marked UNWRITTEN AND UNSCORED and carry no verdict**, which is
      the PAGP form of 2026-09-20 applied one stage earlier.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** No question
      is marked IN at all.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives. **No UNRESEARCHED
      verdict is recorded**; every artifact this run needed was obtained from EDGAR.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known. **No UNKNOWABLE
      verdict is recorded**, and 0.5 states why the label was considered and refused rather
      than assuming it.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked.
      10-Q `0000058492-26-000430`; six-month operating cash flow **−$10.3M**, filed statement
      against XBRL, agreed.
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.
      **Not applicable, Q4 not written.** No owner-earnings figure appears anywhere in this
      file, and no net-income proxy was used or contemplated (operator rule 5, PRIME RULE 3
      as amended 2026-09-20).
- [x] Competitor row filled, or the moat marked PROVISIONAL and UNRESEARCHED. **Not
      applicable, Q2 not written.** No moat class is asserted.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated. USD 5.34%,
      2026-09-18, US Treasury daily par yield curve. **Struck this session, not inherited
      from the brief.** Not used, because Q5 does not open.
- [x] Value stated as a round-number range, not a point estimate. **Not applicable, no value
      is stated.**
- [x] One bar chosen, not both; windage count stated. **Neither bar is used. Windage count:
      zero.**
- [x] Prices dated; aggregator used for live quotes only and flagged. The $9.20 is dated
      2026-08-26 and flagged twice: as an aggregator quote **and as a dead one**.
- [x] Run committed to git.
- [x] **Ledger ids verified against `principle_ledger.csv` this session.** Nine cited in this
      file (E4-19, E4-18, E3-27, E4-14, E4-08, E4-26, E3-41, E3-47, E5-36); twenty-two were
      checked in total. All exist and each says what this file attributes to it. **Zero
      phantoms.**
- [x] **Operator rule 9 check.** The incentive here ran toward closing early, because closing
      is cheap. The four counter-arguments at 0.5 were written before the closure was, and
      each was tested against a filing rather than against my preference **[E4-26]**. No
      screen or flag decided anything in this file **[E5-36]**: the deal flag was a prompt to
      read, and the reading, not the flag, is what closed it.

## REGISTER
- Verdict: **none of the four.** Outcome: **DEAD_OR_ACQUIRED, closed at STEP 0, before Q1,
  no finding about the business.**
- One line: **Leggett & Platt was merged into Somnigroup International Inc. on 2026-08-26 at
  0.1455 SGI shares per LEG share, delisted from the NYSE on 2026-08-27 and deregistered on
  2026-09-08 with one holder of record; the queue's $1,257M cap is the suspended-trading
  close of a cancelled security times the last cover count, and no Q5 can exist.**
- **If UNRESEARCHED, THE WORK ORDER:** not applicable. No artifact is outstanding.
- **If UNKNOWABLE:** not applicable, and 0.5 states why the label was considered and refused.
- **Successor, for whoever decides whether to queue it:** **Somnigroup International Inc.,
  NYSE: SGI, CIK `0001206264`**, $63.36 at 2026-09-18 (aggregator, flagged). Former LEG
  holders own approximately **8.6%** of it. **It is a different company and it requires its
  own v4 run from its own filings.** Nothing in this file may be carried into that one.
- **To the operator, three things this run leaves behind:** (1) `tools/run.py` concludes, and
  concludes wrongly, on a delisted ticker, against operator rule 8; (2) the queue's pricing
  path cannot see a delisting, and ACLS and CNR sit in the same class; (3) the framework has
  no verdict for a cancelled security, and the run template's STEP 0 has no line that would
  catch one. Details in DEFECTS FOUND BY THIS RUN.

---
## NOTE ON THIS RUN'S OWN COMMIT TITLE, 2026-09-20

**Commit `e2c06dd` is titled "LEG fold: closed at STEP 0 …" and NO FOLD WAS PERFORMED.**
The word was copied from the shape of the previous day's PAGP commit, where it was accurate.
The body of `e2c06dd` says so in its last paragraph, and so does the register above, but the
title is the line a later session greps. **History is not edited** (operator rule 6, and the
`e9cc6a5`/ORLY precedent recorded in `Screens/RESUME STATE 2026-09-12` item 4E); the
correction is recorded here and in the message of the commit that carries this note.
`Screens/WATCHLIST RUN QUEUE.md`, `Screens/_daily/_wave7_done.txt`,
`Screens/_daily/OVERNIGHT LOG.md`, `PORTFOLIO.md`, `tools/alerts.json` and
`Screens/2026-08-31 PREPPED READING LIST (operator lists).md` are all untouched by this run.

---
## RESEARCH FILES
All raw material written to `Test Runs/_research 2026-09-20 LEG/` as it was gathered:
`submissions.json`, `8K_2026-04-13_mergeragreement.htm/.txt`,
`8K_2026-08-26_completion.htm/.txt`, `Form15_2026-09-08_a.htm/.txt`,
`Form25NSE_2026-08-27.xml`, `10Q_2026-06-30.htm/.txt`, `concept_ocf.json`,
`company_tickers.json`, `fetch.py`.
