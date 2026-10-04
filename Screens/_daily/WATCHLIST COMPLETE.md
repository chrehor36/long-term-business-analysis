# WATCHLIST COMPLETE - 2026-09-19, WAVE 6 CLOSED

Written by the unattended overnight session of **2026-09-19 22:32 EDT** (branch C of the overnight
prompt). **Every name in WAVE 6 is done**: each of the fifteen has an entry under
`## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md` **and** is struck - the eleven
triage-dropped businesses in the wave 6 table, CCB/ACNB/SOFI in the dated note under
`#### EXCLUDED UNDER THE OPERATOR'S BANK DIRECTIVE`, OTTR in the `## PRE-RUN` list. **No run was
started this cycle.** Nothing on disk had been modified inside the 45-minute window, so no session
was interrupted.

This file supersedes the wave 5 version of the same name (2026-09-19, register 117) and repeats no
count from it; every number below was struck against the register this cycle.

## THE STANDING COUNT, FROM THE REGISTER
Counted from the register itself (every line-start `- **` entry between `## COMPLETED FROM THE QUEUE`
at line 472 and `## THE WRITE-EARLY PROTOCOL` at line 9772), **not carried forward from any earlier
tally** - the discipline the 2026-09-19 count corrections were written to enforce.

- **132 register entries, no duplicate ticker** (132 entries, 132 distinct tickers). Every one ends
  with a price and a pass/fail line.
- **All 15 wave 6 names present exactly once** (KO, DIS, IBM, GFF, USAR, BLK, CB, TRV, AIG, CCB,
  ACNB, SOFI, JPM, TFC, OTTR), and all 15 struck.
- **Struck and registered are the same set**: every `~~TICKER~~` anywhere in the queue file has a
  register entry, and every register entry is struck somewhere. Zero either way.

| where the run stopped | count | names |
|---|---|---|
| Q1 (UNKNOWABLE) | 5 | HHH, RGTI, DJT, BIRD, **USAR** |
| Q2 (OUT) | 92 | includes wave 6's **TFC, OTTR, SOFI, AIG, CCB, TRV, BLK, DIS, IBM** |
| Q4 (OUT) | 2 | ORCL, ARM |
| Q5 (all four business gates IN, below the ~10% floor [E4-28] on price) | 33 | ORLY, BRK-B, MCD, HAS, COKE, TSCO, SBUX, ACLS, BMI, EFX, CMG, CTAS, WMT, GRMN, MSFT, AAPL, GOOGL, AVGO, TXN, CRM, AMAT, KLAC, LRCX, SHOP, SNPS, PLTR, CL, SPGI, **KO, GFF, CB, ACNB, JPM** |
| **cleared Q5** | **0** | |

Against the 117 counted earlier on 2026-09-19 (4 at Q1, 83 at Q2, 2 at Q4, 28 at Q5), wave 6 added
15: **1 at Q1 (USAR), 9 at Q2, 5 at Q5 (KO, GFF, CB, ACNB, JPM)**. **No business on the operator's
watchlist has cleared Q5** - 132 runs, 33 of them with all four business gates IN, every one of the
33 quit on at the [E4-28] floor. Operator rule 7 stands: none of this bears on whether the method
beats the market, which remains **UNPROVEN**.

The gate for each entry was taken by regex on its opening four lines (`FAIL at Q<n>`), not by eye;
the five Q1 and 33 Q5 names are listed above so the classification can be checked name by name.

## WHAT CLOSED SINCE THE WAVE 5 NOTE
Both operator decisions that note left open are **closed**, and the closures are the operator's, not
a session's:
1. **The three banks (CCB, ACNB, SOFI) - RULED AND RUN.** The operator's ruling of 2026-09-19,
   recorded in the WAVE 6 section, is that the five banks are run. All five are: CCB, ACNB, SOFI,
   JPM, TFC. The bank directive of 2026-08-30 is superseded for the watchlist, not deleted.
2. **The ~17 unpriced watchlist names - IDENTIFIED.** The operator sent twenty screenshots on
   2026-09-19; the diff found 193 distinct tickers, 42 funds/indices/crypto, **151 businesses**,
   reconciling to the 151 the 2026-09-01 triage counted. Eleven were nowhere on disk; those eleven
   are wave 6.

## OPERATOR DECISIONS STILL OPEN
1. **TJX needs a fresh purchase run.** The `## PRE-RUN, EXCLUDED FROM THE QUEUE` audit of
   2026-09-19 found five of the fourteen rest on work predating the framework in force: **V
   (2026-07-14), HRB (2026-07-16), NHNKY (2026-07-15), TBTC (2026-07-17), TJX (2026-08-26)**. Four
   are the operator's own positions and are discharged under `Framework/THE HOLDINGS FRAMEWORK.md`,
   whose first reviews are already owed on them. **TJX is not held and is the one name of the five
   that needs a v4.1 purchase run for a current verdict.** Not started unattended: it is a full run,
   not a bounded cycle's work.
2. **Eight survival shapes are PROPOSED and unruled** - #23 THE CUSHION (CB), #25 THE INDEMNITY
   (CCB), #25 THE SLEEPING DEPOSITOR (ACNB), #26 THE MARKED BOOK (SOFI), #27 THE LICENCE (JPM),
   #28 THE CONVERTED WINDFALL (OTTR), #29 THE BOUGHT RATIO (TFC), plus #21 THE ROLL-UP (SOUN) from
   wave 5. None enters the index as accepted until the operator rules.
3. **A NUMBER COLLISION IN `Screens/SURVIVAL SHAPES - index.md`, found this cycle and NOT fixed.**
   **Two different proposed shapes are both numbered 25**: THE INDEMNITY (CCB) and THE SLEEPING
   DEPOSITOR (ACNB), rows 40 and 41 of that file, both dated 2026-09-19. Everything after them (26,
   27, 28, 29) is therefore one number short of the count of shapes. **Left as found**, because
   renumbering a register of shapes the operator has not yet ruled on is a structural change, and
   because the two folds that wrote them are history (operator rule 6). The fix is the operator's:
   either renumber one to 30, or rule that one of the two is a feature of the other.

## AN ARITHMETIC DISCREPANCY THE REPOSITORY CANNOT CLOSE
The WAVE 6 section states **"151 of 151 businesses are identified"**. Counted on disk this cycle,
the three lists that account for a business hold **150 distinct tickers**: 132 in the register, 14
in `## PRE-RUN`, 7 in `## NOT SEC REGISTRANTS`, with OTTR shared by the first two and MITSY/NHNKY by
the last two. **One name's worth of difference, and it cannot be resolved from the repository** -
the 151-name list was transcribed from screenshots and never saved to a file, which is the same
limit `#### WHAT CANNOT BE RECONCILED FROM DISK` already records. Stated rather than reconciled by
adjusting a count. It may be a classification difference in the screenshot diff (a ticker counted a
business there and a fund here, or a dual-class line) rather than a missing business; **only the
operator's screenshots can say**.

## ALSO FLAGGED TO THE OPERATOR IN THE REGISTER (pointers only, read the entries)
- **A brief-writing defect, three consecutive folds** (SOFI, CCB, OTTR, recorded 2026-09-19): a
  brief instructed the agent to "strike it in the WAVE 6 table" for a name that table does not
  contain. Recorded in the queue rather than resolved by editing, and the fold instructions are
  where the fix belongs.
- **Three consecutive banks' briefs mis-stated which bank the run was** (SOFI "second", JPM
  "fourth", TFC "fourth"), each corrected at the fold by counting the register. The rule that caught
  all three: **count from the register, never carry a tally forward.**
- `Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`
  still says BAM and BN "stay blocked"; both were run on 2026-09-13. That document was outside those
  runs' permission to edit, and remains so.
- `Backtests/scripts/bt17_microcap.py` `shares_asof()` has no staleness test; whether any backtest
  panel priced a spin-off, de-SPAC or pre-IPO registrant on a stale share fact has not been tested.
- Registrants that sell their business and keep the listing are priced on the sold business until
  the next 10-K recasts the years (BIRD dated note). A prompt, not a proposed rule.
- **The overnight lock defect of 2026-09-19 20:34** is addressed by commit `e176f12` (freshness, not
  a PID); this cycle honoured the lock and found no live session. The scheduler trace should be
  watched for one more night before the defect is called closed.

## NOT STARTED, BY INSTRUCTION
The three CSV lists, the TJX re-run, the shape-numbering fix, and any other new work were **not**
started unattended.

---

# ADDENDUM 2026-09-19 23:33 EDT - the 22:32 fold re-struck, and one of its claims is WRONG

Written by the next unattended cycle (branch C again: every WAVE 6 name was still done, nothing
under `Test Runs/` had been modified inside the 45-minute window, and no name was left to run). The
cycle's bounded unit was therefore **to audit the fold above rather than repeat it**, per operator
rule 6, which is why this is an addendum and **nothing above this line has been edited**.

## WHAT RE-STRUCK CLEAN
Counted again from the file, not carried forward from the section above:
- **132 register entries, 132 distinct tickers, zero duplicates.** CONFIRMED.
- **Gate tally CONFIRMED: Q1 5 · Q2 92 · Q4 2 · Q5 33 · cleared Q5 ZERO**, summing to 132. *(My
  first pass printed 91 and 32 with two entries unmatched. The defect was in MY regex, not the
  register: the PLTR and INOD entries wrap as `FAIL at   Q5` and `FAIL at   Q2` with the line break
  collapsed to multiple spaces. Recorded because a count that disagrees with the one above should
  say which of the two was wrong, and it was mine.)*
- **All 132 entries carry both a price token and a pass/fail token**, tested by regex on the entry
  body rather than by eye. Zero without either. The queue's two-part output contract holds across
  the whole register.

## WHAT DID NOT: "STRUCK AND REGISTERED ARE THE SAME SET" IS FALSE
The section above states: *"every `~~TICKER~~` anywhere in the queue file has a register entry, and
every register entry is struck somewhere. Zero either way."* **The second half is true; the first
half is not.** Taking every struck string in the file gives **134**, and two are not register
tickers:
1. **`~~TICKER~~` at line 9848** is prose, not a name: it is the fold instruction *"Strike the
   ticker in its tier roster (`~~TICKER~~`)"*. Harmless, and it is what an audit by regex must
   expect to find.
2. **`~~BRK-A~~` at line 201 IS a real ticker, struck, with NO register entry of its own.** The
   Mini Berk roster strikes it *"(covered by the BRK-B run; the A prices at 0.08% parity; struck
   2026-09-13)"*. **This is correct bookkeeping and no work is owed** - BRK-A is run, by BRK-B's
   run, because it is the same company in a different share class. **The false thing is the audit
   claim, not the strike.** Any future audit asserting struck-equals-registered has to except
   BRK-A, or it will keep re-finding it.

## AND BRK-A IS THE ONLY CANDIDATE ON DISK THAT FITS THE 150-VERSUS-151 GAP EXACTLY
The section above reports that the WAVE 6 diff claims **151 businesses identified** while the three
on-disk lists hold **150 distinct tickers**, and calls the last one unresolvable from the
repository. Recomputed here from the file: register **132** + PRE-RUN **14** + NOT-SEC **7**, less
OTTR (register and PRE-RUN) and MITSY/NHNKY (PRE-RUN and NOT-SEC), = **150**. CONFIRMED.

**BRK-A is in none of those three lists** (verified: not in the register, not in PRE-RUN, not in
NOT SEC REGISTRANTS), and it is a business ticker, not a fund. **150 + BRK-A = 151, exactly.**

It also matches the defect class that section itself guessed at: *"a ticker counted a business there
and a fund here, **or a dual-class line**"*. **BRK-A is the dual-class line**, and it is invisible to
a count of the three lists for one specific reason: **it is the only name in the queue whose run is
discharged by a DIFFERENT name's run**, so it is the only struck business with no register row.

**This is a CANDIDATE, not a closure, and it must not be written up as one.** The 151-name list was
transcribed from screenshots and never saved, so **nothing on disk can prove BRK-A is a line in
them** - Stocks lists commonly carry both share classes, but commonly is not evidence. The gap is
still open; what has changed is that it now has a named, checkable candidate instead of an
unidentified one. **The operator can settle it in seconds: is BRK-A a line in the twenty
screenshots of 2026-09-19?** If yes, the 151 reconciles and the discrepancy closes with no business
missing. If no, a genuinely unidentified business remains and only the screenshots can name it.

## ADDED TO OPERATOR DECISIONS STILL OPEN
4. **Confirm or refute BRK-A as the 151st line** (above). One look at the screenshots decides it.
   Until then the arithmetic discrepancy stands as recorded, not as reconciled.

**No run was started, no count above was edited, and the three CSV lists, the TJX re-run and the
shape-number collision were all left untouched, by instruction.**

# ADDENDUM 2026-09-20 00:32 EDT - the register was never checked against the files on disk; it is now

Branch C for the third consecutive cycle. State read first: all fifteen WAVE 6 names (KO, DIS, IBM,
GFF, USAR, BLK, CB, TRV, AIG, CCB, ACNB, SOFI, JPM, TFC, OTTR) still carry a `## COMPLETED FROM THE
QUEUE` entry **and** are struck, tested one by one; nothing under `Test Runs/` was modified inside
the 45-minute window; the lock at 00:31:56 is this cycle's own (PID 9252). No name to run, no file
to resume. **Nothing above this line has been edited** (operator rule 6).

The bounded unit this time was chosen because **the OTTR defect has never been tested against the
register itself.** OTTR was a list asserting a run that had no file on disk. The two folds above
audited the register against the strike marks and against its own output contract, both of which are
internal to one document. Neither asked the OTTR question: **does every register entry correspond to
a run file that actually exists?**

## RE-STRUCK FIRST, NOT CARRIED FORWARD
- **132 register entries, 132 distinct tickers, zero duplicates.** CONFIRMED for the third time,
  counted from the file.
- **Gate tally Q1 5 · Q2 92 · Q4 2 · Q5 33 · cleared Q5 ZERO**, summing to 132. CONFIRMED, with
  whitespace collapsed so the wrapped PLTR and INOD entries match (the 23:33 note's warning was
  read before the regex was written, and it worked).

## THE NEW CHECK: REGISTER AGAINST DISK. IT PASSES.
1. **All 132 register tickers have a run file on disk.** Every ticker was matched against the 296
   `Test Runs/*Run - <TICKER> *.md` files (277 distinct tickers, the surplus being runs that predate
   this queue). **Zero missing. No second OTTR.**
2. **One ticker's file is not named after it, and it is correct.** `BRK-B` is the single name whose
   run file carries a different ticker: `Test Runs/2026-09-02 Run - BRK Berkshire Hathaway.md`. Its
   register entry names that path explicitly, so nothing is lost, but **an audit matching ticker to
   filename must except BRK-B** or it will report a phantom miss. This is the same name the 23:33
   fold had to except for the strike audit, in its A class rather than its B.
3. **Every `Test Runs/….md` path cited inside a register entry resolves to a file that exists:
   129 citations across 128 entries, ZERO broken.** One entry cites two files (OXY: its run and the
   `ADDENDUM 2026-09-02 - the OXY run's SBC claim was a back-solve` beside it).
4. **No unfolded run.** Every run file dated 2026-09-13 or later has a register entry: zero orphans.
   Nothing was run and left out of the register during wave 5 or wave 6.

## THE ONE GAP FOUND, AND IT IS A CITATION GAP, NOT A MISSING RUN
**Four register entries name no run file at all: SOFI, ACNB, BLK and CB.** All four are WAVE 6 folds
of 2026-09-19. The other 128 entries point at their file; these four do not.

**All four runs exist and are substantive**, verified by opening each:

| ticker | file | lines |
|---|---|---|
| SOFI | `Test Runs/2026-09-19 Run - SOFI SoFi Technologies.md` | 2,110 |
| ACNB | `Test Runs/2026-09-19 Run - ACNB ACNB Corporation.md` | 1,642 |
| BLK | `Test Runs/2026-09-19 Run - BLK BlackRock.md` | 1,402 |
| CB | `Test Runs/2026-09-19 Run - CB Chubb.md` | 1,600 |

*(CB also has an older `2026-07-14 Run - CB (Chubb).md`, predating v4.1; the 2026-09-19 file is the
one the register entry describes.)*

**The entries are NOT edited to add the pointers**, on the same rule the 22:32 and 23:33 folds
followed when they left the shape-number collision as found: a register entry is the fold record,
and a later cycle records beside it rather than rewriting it. The paths are written out above, so
the pointer now exists on disk either way and a reader loses no time. **What the operator may want
to rule on is whether a fold should be allowed to repair a missing file pointer in its own entry
class, since this is bookkeeping rather than judgment.** Added as operator decision 5.

## MY OWN DEFECT, RECORDED
My first pass at check 3 reported **23 broken pointers**. All 23 were artifacts of my own handling:
a run-file path that wraps across a line break in the markdown becomes `Test Runs/2026-09-07 Run -
MRVL Marvell   Technology.md` when the newline is replaced by a space instead of collapsed. **This
is the identical regex class the 23:33 fold recorded against itself**, hit again one cycle later on
a different check. Two consecutive audits have now tripped on line wrapping in this file. **Any
future audit of `WATCHLIST RUN QUEUE.md` must normalise whitespace with `re.sub(r'\s+',' ')` before
matching anything that can wrap** - that is the durable lesson, and it belongs here rather than in a
third cycle's confession.

## ADDED TO OPERATOR DECISIONS STILL OPEN
5. **May a fold add a missing run-file pointer to its own register entry?** Four entries (SOFI,
   ACNB, BLK, CB) lack one; the files exist and are named above. This cycle left the entries
   untouched, reading operator rule 6 strictly. A one-line ruling either way settles the class.

**No run was started. The three CSV lists, the TJX re-run under v4.1, the eight unruled survival
shapes and the duplicate shape number 25 were all left untouched, by instruction.**

---

# ADDENDUM 2026-09-20 01:34 EDT - the register agrees with the run files, gate by gate; and the lock defect is closed

Written by the unattended overnight session of **2026-09-20 01:31 EDT** (branch C, the fourth
consecutive cycle with no name to run). **Nothing above this line was edited** (operator rule 6).

State read first, not carried forward: all fifteen WAVE 6 names still carry a
`## COMPLETED FROM THE QUEUE` entry **and** are struck; **no file under `Test Runs/` was modified
inside the 45-minute window** (checked by `LastWriteTime`, 296 run files, zero hits); the lock at
01:31:56 is this cycle's own and its PID **18084 is alive**. No name to run, no file to resume.

## RE-STRUCK FROM THE FILE, FOR THE FOURTH TIME
Parsed by line range (474 to 9773, the register section proper, after confirming that
`## THE WRITE-EARLY PROTOCOL` also occurs **inside** an entry as prose, which breaks a naive
`.index()` slice and cost this cycle one wrong count of 19):

- **132 register entries, 132 distinct tickers, zero duplicates** - CONFIRMED.
- **Gate tally Q1 5 | Q2 92 | Q4 2 | Q5 33, cleared Q5 ZERO, summing to 132** - CONFIRMED.

**A regex pitfall in the same class as the whitespace one, recorded so a fifth cycle does not meet
it fresh: nine of the 132 entries write `FAIL AT Q<n>` in capitals** (TFC, JPM, SOFI, AIG, CB, GFF,
KO, SPGI, CL). A case-sensitive pass classifies all nine as unknown and reports Q2 89 / Q5 27.
**Match the register case-insensitively, and normalise whitespace first.**

## THE NEW CHECK: THE REGISTER AGAINST THE RUN FILES' OWN VERDICTS. 132 OF 132 AGREE.
The three prior audits tested the register against the strike marks, against its own output
contract, and against the **existence** of the files on disk. None of them asked whether the
register's verdict is **the verdict the run file records**. That was the last untested layer, and it
now passes.

Method, independent of the register: each run file was parsed for its `## Q<n>` headings and the
first `VERDICT: [ ] IN [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE` checkbox inside each section; the
file's gate is **the first of Q1 to Q4 whose box is not IN**, and a file with Q1 to Q4 all IN is a
Q5 name. The register's gate was taken separately from its own text. **Zero mismatches across all
132**, and the file-side tally reproduces the register-side tally exactly: **Q1 5, Q2 92, Q4 2,
Q5 33**. BRK-B was mapped by hand, as every audit of this kind must (`2026-09-02 Run - BRK
Berkshire Hathaway.md`).

## BUT THE Q5 CHECKBOX CANNOT BE MACHINE-READ, AND THREE FILES PROVE IT
**Three run files tick `VERDICT: [x] IN` inside their Q5 section, and the register records all
three as FAIL at Q5 on price. The register is right in all three cases.** The tick means a
different thing in each:

| file | the line as written | what it means |
|---|---|---|
| AMAT (`2026-09-07`, L1461) | `VERDICT: [x] IN is NOT reached and UNKNOWABLE is NOT used - the name FAILS at Q5, on price` | the box is ticked to **negate** IN |
| AVGO (`2026-09-06`, L1348) | `VERDICT: [x] IN as an analysis, FAIL on price - the name is QUIT ON at the [E4-28] floor` | IN as an **analysis**, fail on price |
| ORLY (`2026-09-02`, L1363) | `VERDICT: [x] IN` *(the question is answered - the evidence is here and it produces a number)* | IN means **the question was answerable**; the fail is carried by "NOT RANKED - below the [E4-28] floor" and by the plain answer beneath it |

**A future audit that read the Q5 box would report three phantom clearances** against the one
standing claim this file makes about outcomes - that no name has ever cleared Q5. It would be
wrong. The Q1 to Q4 boxes are clean, unambiguous and machine-readable in all 132 files; **it is only
at Q5 that the template's four-verdict checkbox has been used as prose**, because Q5 returns two
things at once (is the question answerable, and does the price clear the floor) and the template
gives it one box. **Left exactly as found.** The template is the enforcement surface and changing it
is a structural change (CLAUDE.md prime rule 5); the three files are history (rule 6). Added as
operator decision 6.

**Read Q5 by prose, never by box.** That is the durable instruction until the operator rules.

## CLOSED THIS CYCLE: THE OVERNIGHT LOCK DEFECT
The 22:32 note said the scheduler trace "should be watched for one more night before the defect is
called closed." It was watched, and it is closed. Commit **`e176f12`** landed 2026-09-19 20:40
("an interactive lock is honoured by freshness, not by a PID it cannot name"). **Every cycle since
behaves correctly, on the trace's own words:**

- **21:31 SKIP** - "interactive session holds the lock, refreshed 52 min ago". The fix honouring a
  live lock it cannot name by PID, which is exactly what it was written to do.
- **22:31 takeover** - "stale lock (interactive=True, pid 0 alive=False, 112 min)". Taken over on
  **freshness**, not on the PID. Correct.
- **23:31, 00:31, 01:31** - three consecutive clean `START`s, **no stale-lock line at all**.
- The lock file now reads `18084 2026-09-20T01:31:56` and **PID 18084 is alive**.

Before the fix the trace took over the **same dead PID 21248** at 15:31, 19:31 and 20:31, three
hours apart, each time with a fresh mtime. That pattern has not recurred in five post-fix cycles.
**The defect is called closed.** The pointer in `## ALSO FLAGGED TO THE OPERATOR IN THE REGISTER`
above is left as written, per rule 6; this section is its closure.

## ADDED TO OPERATOR DECISIONS STILL OPEN
6. **Does Q5 need a machine-readable outcome field?** Q5 answers two questions with one checkbox
   and three files have resolved the collision three different ways. Either the template gains a
   separate one-line Q5 outcome (`CLEARED` / `QUIT ON AT THE FLOOR` / `UNKNOWABLE`), or it is ruled
   that Q5 is read by prose forever and no tool may score it. A template change needs the
   operator's approval in any case (prime rule 5).

**No run was started. The three CSV lists, the TJX re-run under v4.1, the eight unruled survival
shapes, the duplicate shape number 25 and the four missing entry pointers were all left untouched,
by instruction.**

---

# ADDENDUM - 2026-09-20 02:32 EDT, overnight cycle

**WAVE 6 IS STILL CLOSED. Branch C.** State re-struck from the files, never carried forward: all
fifteen WAVE 6 names (KO, DIS, IBM, GFF, USAR, BLK, CB, TRV, AIG, CCB, ACNB, SOFI, JPM, TFC, OTTR)
carry a `## COMPLETED FROM THE QUEUE` entry **and** are struck; **register 132 entries, 132 distinct
tickers, zero duplicates; gate tally Q1 5 | Q2 92 | Q4 2 | Q5 33, cleared Q5 ZERO, summing to 132**
- confirmed for the fifth time. No file under `Test Runs/` was modified inside the 45-minute window;
the lock at 02:31:56 is this cycle's own. No name to run, no file to resume.

## THE NEW CHECK: THE RUN FILES HAVE NEVER BEEN SWEPT FOR PHANTOM CITATIONS

The four prior audits tested the register against the strike marks, against its own output
contract, against the existence of the run files, and against each run file's own verdict. **Every
one of them tested the REGISTER. None tested the RUN FILES' EVIDENCE.**

And nothing else does either. `tools/check_framework.py` checks exactly **five** documents - the
framework, the holdings framework, the insurer sector method and the two templates. **The 132 run
files are outside its scope**, and always have been. Individual folds asserted "zero phantom" for
their own run (TFC's says "101 ledger ids cited, every one verified"); the corpus had never been
swept as a whole. This is the layer THE STANDARD rests on - *another analyst must be able to verify
any rule against its cited source in under two minutes* - so it is the one worth testing.

**Result, and it is clean:**

| sweep | files | citations | phantom |
|---|---|---|---|
| the 132 registered names | 140 run files | **20,004** | **0** |
| all markdown under `Test Runs/` | 786 of 1,043 files | **37,927** | **0** |

**Zero phantom ledger ids in 37,927 citations.** Zero wrap-broken ids (`E4-` / newline / `28`),
tested for because that is the exact defect class the last two cycles confessed. The 140-against-132
gap is not a discrepancy: several tickers carry a pre-queue run as well as the queue run.

## THE SECOND CHECK, AND IT COST ME THE CYCLE'S REAL LESSON

Phantom-freedom only proves the cited id **exists**. It does not prove the quote beside it is **that
id's quote**. So the second test: does every verbatim corpus quote in a run file sit beside the
ledger row it actually comes from?

**My first pass said 115 MIS-CITATIONS across 86 files, and every one of them was my own defect.**
It matched `"quote" [Exx-nn]` - quote first, id after. **That is not this corpus's convention.** The
run files cite **before** the quote at least as often as after:

> This is the behaviour **[E5-30]** calls a ratchet: *"once you start it, it's all over … And
> forecasting earnings, I can't imagine anything more destructive."*
> *(`2026-08-31 Run - HOG (Harley-Davidson) v4.1.md`, line 573 - correctly cited, and my pattern
> scored it as mis-cited to `[E3-48]`, which is the id that opens the NEXT bullet.)*

The tell was in the output and I nearly wrote it up before reading it: **84 of the 115 were
cross-era** (an E3 id "should have been" E4, and so on). A real mis-citation habit is not era-random;
an artifact that grabs whatever id opens the next bullet is. I also tested and **refuted** the
alternative that the ledger had been renumbered under the older runs - a renumber shifts by a
constant within one era, and the rate held flat at 13-30% straight through to the 2026-09-19 runs.

**Corrected test** - attribute a quote to the owning id if that id appears anywhere in the
surrounding context, before or after, and allow that quoting a **governing document** is legitimate
(the framework, the holdings framework and the insurer sector method quote the corpus themselves):

| quote >= 45 chars, context window | corpus quotes | owning id present | quoting a governing doc | **uncited residual** |
|---|---|---|---|---|
| 400 chars | 3,027 | 2,895 (95.6%) | 130 | **2** |
| 600 chars | 3,027 | 2,936 (97.0%) | 90 | **1** |

**The last residual is not a defect either.** It is HHH quoting *"For almost all other insurers, a
comparable degree of concentration…"* from `SECTOR METHOD - owner earnings for insurers…`, which is
a governing document I had left out of the allowed set. **The true residual is ZERO.**

**So: 3,027 verbatim corpus quotes across the run corpus, every one of them traceable to the ledger
row it came from, and 37,927 citations with no phantom among them.** The evidence layer holds.

## THE DURABLE LESSON, written down so a sixth cycle does not re-learn it

Three cycles running, the defect has been the reader, not the read: 00:32 broke paths on a newline,
01:34 broke a tally on capitalisation, and this one invented 115 mis-citations out of a bullet
boundary. The rule that covers all three: **when a finding accuses the corpus, first construct the
hypothesis in which the finding is an artifact of my own parse, and kill that one first.** For this
file specifically: **a ledger id may precede its quote. Never attribute a quote to the nearest id
that follows it.**

## ADDED TO OPERATOR DECISIONS STILL OPEN
7. **Should `tools/check_framework.py` sweep `Test Runs/` for phantom citations?** The sweep costs
   about a second, it covers 37,927 citations the acceptance test currently never sees, and it is
   pure arithmetic under operator rule 8 - it fetches and compares, it concludes nothing. It passes
   clean today, so adding it locks in a property rather than opening a backlog. **Not added
   unilaterally**: the tooling test is *"does it get the same number sooner, or does it add a
   number?"*, and widening the acceptance test's scope is the operator's call, not a session's.

**No run was started. The three CSV lists, the TJX re-run under v4.1, the eight unruled survival
shapes, the duplicate shape number 25 and the four missing entry pointers were all left untouched,
by instruction. Nothing above this addendum was edited (operator rule 6).**

---

# ADDENDUM - 2026-09-20 03:32 EDT, overnight cycle

**Branch C again: WAVE 6 is still closed.** State read before anything was touched. All fifteen
WAVE 6 names (KO, DIS, IBM, GFF, USAR, BLK, CB, TRV, AIG, CCB, ACNB, SOFI, JPM, TFC, OTTR) carry a
`## COMPLETED FROM THE QUEUE` entry; nothing under `Test Runs/` was modified inside the 45-minute
window; the lock at 03:31:56 is this cycle's own. No name to run, no file to resume.

## RE-STRUCK FROM THE FILE, FOR THE SIXTH TIME
Register **132 entries, 132 distinct tickers, zero duplicates**. Gate tally **Q1 5 | Q2 92 | Q4 2 |
Q5 33**, summing to 132, **cleared Q5 ZERO**. CONFIRMED, and it agrees with every prior cycle.

## THE NEW CHECK: THE OPERATOR'S OWN DELIVERABLE CONTRACT, WHICH NO AUDIT HAS EVER TESTED
The queue opens with a rule that is not in the framework and is not in `check_framework.py`, so
nothing has ever enforced it: ***"EVERY RUN IN THIS QUEUE MUST END WITH BOTH"* a price and a
pass/fail line.** Five cycles have audited the register, the register against disk, the register
against the run files' gate verdicts, and the run files' citations. **None tested whether the runs
deliver what the operator actually asked for.**

Swept both sides.

- **Register side: 132 of 132 clean.** Every entry carries a price-shaped figure in a named
  currency, the word "price", and a pass/fail word. No exceptions.
- **Run-file side: 132 of 132 carry a price. 129 of 132 carry the literal token PASS or FAIL.**
  The three that do not are **AEHR**, **DJT** and **BN**, and **all three satisfy the rule on
  substance**: each names the gate that closed the file and each reports a price under
  `COMPUTATION - NOT A CLEARANCE` (AEHR $93.49 x 32,620,450 = $3,049.7M, Q4 OUT; DJT $8.85 x
  277,941,274 = $2.46bn, Q2 and Q4 OUT; BN a $87.8bn cap against a $38.22 quote, Q2 OUT). The
  operator's rule asks for the pass/fail *"stated plainly: which question closed the file"*, and
  all three state it. **The gap is a token, not a deliverable.** Nothing is owed to the operator.

## THE SECOND CHECK: SOVEREIGN-SOURCE DISCIPLINE UNDER THE 2026-09-02 CORRECTION
`CLAUDE.md` was corrected on 2026-09-02 (commit `cf18a75`, 05:57 EDT) to make the **US Treasury
daily par yield curve the USD source and FRED the FALLBACK**, because operator rule 5 demands the
issuing authority and FRED is a St. Louis Fed redistribution of a Treasury series. **Whether the
runs actually obeyed it has never been checked.** Swept the 132 runs of record.

- **129 are dated 2026-09-02 or later. 128 of them name the Treasury daily par yield curve as the
  source of record.** Where FRED appears in those files it is named as the fallback and explicitly
  marked unused, or recorded as having failed (QCOM: *"`tools/sources.py` returned `USD FAILED: The
  read operation timed out` on its FRED path"*).
- **The three runs of record that predate the correction (GM, OXY, PLAB, all 2026-09-01) use FRED.
  That was the rule in force. Not violations**, and PLAB is the run that CAUSED the correction.
- **ONE file in 132 names a non-Treasury source of record: `2026-09-02 Run - F Ford Motor.md`.** It
  takes USD 30-year 5.25% at 2026-08-31 from the **Board of Governors, Statistical Release H.15,
  series `RIFLGFCY30_N.B`**, and argues it is *"the issuing authority itself, one rung above the
  project's standing FRED source"* after FRED was unreachable at three attempts. **The argument is
  one rung short.** H.15 is a Federal Reserve release of a constant-maturity yield that the
  **Treasury** computes and publishes, which is the same relation that demoted FRED; the Fed is the
  issuing authority for the release, not for the series.
- **It changes nothing downstream, and that is checked, not assumed.** AEO's run reads the Treasury
  CSV directly and records the adjacent observation **5.25% (2026-08-31)** - the identical figure
  to the basis point. Ford's number is right; only its named source is off by a rung.
- **And the rule was six minutes old.** `cf18a75` landed 05:57 EDT; the Ford file landed 06:03
  (`a329d07`). A run that takes hours was already in flight when the document changed under it.
  **Recorded, not corrected** (operator rule 6), and **not counted as a protocol violation**: the
  run named its rung and its obstacle, which is what the evidence ladder asks of it.
- One pointer slip found beside it, worth a line and no more: **AEO cites the rule as *"corrected
  2026-09-01"*** when the commit is 2026-09-02. AEO retrieved its rate on 2026-09-01 and used the
  Treasury, which is the practice `CLAUDE.md` itself says preceded the document (*"`daily_fetch.py`
  had already moved to the Treasury curve"*). **The run followed the corrected rule before the
  document carried it; only the date on the pointer is wrong.**

## MY OWN DEFECT, AND IT IS THE SAME ONE FOR THE FOURTH CYCLE RUNNING
The 02:32 addendum wrote down the durable lesson: *when a finding accuses the corpus, build the
hypothesis in which it is an artifact of my own parse and kill THAT first.* **It bit me twice in one
cycle, both times on a line wrap.**

1. My first sovereign sweep reported **six** files citing FRED with no Treasury mention (AEO, DG, F,
   NKE, QCOM, ULTA). **Five of the six were mine.** They write *"Daily Treasury\n  Par Yield Curve
   Rates"*, and the wrap falls between "Treasury" and "Par". Only Ford survived the correction.
2. My gate tally came back **Q1 5 | Q2 91 | Q4 2 | Q5 32 plus TWO unmatched**, against the standing
   92 / 33. **Both unmatched were mine too**: PLTR writes *"FAIL at\nQ5"* and INOD *"FAIL at\nQ2"*,
   wrapped between "at" and the gate number. Normalising whitespace returns 92 and 33 exactly.

**Three cycles blamed a newline, a capitalisation and a bullet boundary. This one blamed a line wrap
twice.** The instruction that would have saved both: **normalise whitespace before matching anything
in this corpus, always, and only then read the result.** These are hand-wrapped markdown files at
roughly 100 and 110 columns; **any token a check depends on can be split by the wrap**, and a
multi-word source name or a "FAIL at Q5" is exactly the length that gets split. Written here rather
than left for a seventh cycle.

## ADDED TO OPERATOR DECISIONS STILL OPEN
**Operator decision 8: should the queue's deliverable rule become part of the acceptance test?**
It passes 132 of 132 on substance today, so like decision 7 it would lock in a property rather than
open a backlog. Three files would need a token added to pass a literal check, which is an edit to
history under rule 6 and therefore not a session's call. **The standing instruction until it is
ruled: read the pass/fail by prose, never by token** - the same shape as decision 6's Q5 box.

**Operator decision 9: the Ford sovereign rung.** One run of 132 sources the USD sovereign from Fed
H.15 rather than the Treasury, with an identical figure, under a rule that was six minutes old. It
can be left as history, or an addendum can be attached to the Ford file. **Left as found.**

**Nothing above this addendum was edited. No run started.** The three CSV lists, the TJX re-run, the
eight unruled shapes, the duplicate shape number 25 and the four missing entry pointers are all
untouched, per the standing instruction not to start them unattended.

---
# ADDENDUM 2026-09-20 04:32 EDT - THE OPERATOR PROTOCOL'S OWN RULES 3, 4 AND 6, SWEPT FOR THE FIRST TIME

**Branch C again, and the state was re-struck from the file before anything else.** All fifteen
WAVE 6 names carry a `## COMPLETED FROM THE QUEUE` entry and all fifteen are struck (tested one by
one on whitespace-normalised text); no file under `Test Runs/` was modified inside the 45-minute
window; the lock at 04:31:56 is this cycle's own. **Register 132 entries, 132 distinct tickers, zero
duplicates; gate tally Q1 5 | Q2 92 | Q4 2 | Q5 33, summing to 132, cleared Q5 ZERO - CONFIRMED for
the seventh time.** No name to run, no file to resume.

## WHAT HAD NEVER BEEN TESTED
Six prior cycles audited the register against the strike marks, against its own output contract,
against the files on disk, against the run files' own gate verdicts, against the ledger, against the
queue's deliverable rule, and against the sovereign-source correction. **None of them tested the
OPERATOR PROTOCOL in `CLAUDE.md` - the eight-clause protocol that binds every run - and
`tools/check_framework.py` has never covered it.** Three of its clauses are machine-checkable.

**RULE 3 - COMPUTATION IS NOT CLEARANCE.** *"Any valuation math produced before Q1-Q4 close must be
headed **COMPUTATION - NOT A CLEARANCE** and may carry no entry language."* **99 of the 132 runs
closed at Q1, Q2 or Q4, and all 99 carry the heading. Zero missing.**

The second half of the rule - *no entry language* - was swept on a thirteen-phrase vocabulary
(`clears the floor`, `above the floor`, `RANKED`, `is a buy`, `entry price`, `passes Q5`, and so on).
**19 hits in 16 files, and every one of the 19 is either my own artifact or the rule being obeyed
out loud.** `is a buy` inside *"equity is a buyback artifact"* (DRI) and *"is a buyer with an
alternative"* (FLNC); `RANKED` inside **NOT RANKED** (AEO, BLK, CGNX, OTTR, OXY); `above the floor`
inside *"none clears the 10% floor"* (ORCL), *"above the floor range -> no"* (TM), and USAR's
offtake contracts, where the floor is a price floor in a supply agreement and not [E4-28]'s.
**Two were read by hand rather than pattern-matched, and both are clean:**
- **GM** - *"it clears the floor with negative required growth"* sits inside the **bias declaration
  under operator rule 9**, naming the analyst's own incentive to validate the screen [E4-27]. It
  quotes the screen's claim in order to hunt against it. The opposite of entry language.
- **TGT** - *"Re-entry price, pre-committed: ~$130/sh"* sits in **Q6**, which is the question that
  asks what would prove the verdict wrong, and the same sentence reads *"and only via the reopen
  tests above; Q2 OUT is otherwise permanent."* A disconfirmation trigger, not an entry.

**TRUE RESIDUAL ZERO. No run in the register carries entry language behind a closed gate.**

**RULE 4 - THE FILING GETS READ.** *"Record the document, date and accession number."*
**132 of 132 run files record at least one accession number in the filed `##########-##-######`
form.** (The clause's other half - *"cross-check one figure against the filed statement"* - is
prose and is not machine-checkable; it is not claimed here.)

**RULE 6 - THE AUDIT IS PART OF THE RUN.** *"A run is incomplete until its self-audit is checked."*
**132 of 132 carry a SELF-AUDIT section.** Across the 132 runs of record exactly **two unchecked
boxes** exist, and both are correct as written: FLNC's `- [ ] **Not done, named:** the Levitan
derivative complaint ... was not read`, which is an honest absence declaration and must stay
unticked, and MKL's `- [ ] Run committed to git - done at the commit following this write`, a box
that cannot be ticked before the commit that ticks it.

## A STRUCTURAL FACT NO COUNT HAS EVER CARRIED
**Eight registered tickers have TWO run files, not one: CCB, CB, SPGI, SPOT, TXN, MU, SBUX, TSCO.**
In every case the older file is a July run under the old `TICKER (Name)` filename convention and the
newer is the September run of record; **seven of the eight register entries cite the September file
by name, and the eighth is CB, one of the four entries the 00:32 cycle already recorded as carrying
no pointer at all.** So **no register entry is anchored to a superseded run** - the question that
had not been asked, now answered.

Counting outward from there: **270 distinct tickers have a single-name run file on disk, plus 12
multi-name files** (ten July sector packs, the `2026-08-26 v3.1 RE-RUN - All Names.md`, and the
NCLTY v4.1 rerun) **whose contents are not attributable to one ticker by filename.** The three
counted lists govern 150. **125 tickers therefore hold a run file and appear in NONE of the three
lists - 89 whose latest run predates v4.1 (2026-08-28) and 36 run under v4.1** (HON, UNH, VZ, LOW,
ITW, KMB, RPM, OTIS and 28 others). These are the pre-watchlist universe: the July v3.x screening
batch of Japanese ADRs, apartment REITs, homebuilders and E&P names, and the late-August v4.1 runs
that predate the 2026-09-01 triage. **Nothing is owed on any of them and no count above is wrong** -
they were never on the watchlist, so "151 of 151 identified" was never a claim about them. The fact
worth recording is narrower and is about a READER: someone who opens `Test Runs/` looking for this
project's verdict on UPS or Lennar finds a **v3.x** answer carrying no marker that it predates the
framework in force. That is **operator decision 10**, below.

**AND THE CROSS-CHECK THAT MATTERS: the PRE-RUN audit of 2026-09-19 stands.** Swept independently,
the names in a counted list whose latest run predates v4.1 are **V, HRB, NHNKY, TBTC and TJX** -
exactly the five that audit named, and **TJX is confirmed as the only one of the five not governed
by `Framework/THE HOLDINGS FRAMEWORK.md`.** Decision 1 is unchanged and still needs a full run.

## MY OWN DEFECTS THIS CYCLE - THE FIFTH CONSECUTIVE CYCLE IN WHICH THE DEFECT WAS THE READER
1. **A SIXTH name nearly went into the paragraph above: NCLTY, apparently last run 2026-07-15.** It
   was mine. The file `2026-08-28 RERUN - NCLTY (Nitori) under v4.1.md` says **RERUN**, not **Run**,
   and my filename pattern required `Run - `. The queue's own table lists NCLTY under *"run under
   v4.1"* and is right. **A finding that contradicts a careful prior audit by exactly one name is
   almost always the reader; I built that hypothesis first and it was correct.**
2. **The self-audit sweep first reported five files with unchecked boxes, and three were mine** -
   CCB, SBUX and TSCO, where I took the FIRST file per ticker alphabetically and so read the **July
   run** instead of the September run of record. That defect is what surfaced the eight-duplicates
   finding above, so it was worth having, but it was still a defect: **when a ticker has more than
   one run file, the run of record is the one the register cites, not the one the glob returns first.**
3. **The held-status flag in my first pass was worthless and is not reported.** I tested holdings by
   searching `PORTFOLIO.md` for a bare ticker, which returns True for `IT` and `UK` on ordinary
   English words. **`PORTFOLIO.md` is a ranked opportunity set with a standing-lines audit, not a
   holdings list**, and holdings cannot be read out of it by regex at all.

**The durable instruction, added to the whitespace rule the last cycle wrote:** *in this corpus a
filename is not a schema.* Run files use at least four conventions - `Run - TICKER Name`,
`Run - TICKER (Name)`, `RERUN - TICKER (Name)`, `Run - Sector N-pack (A B C)` - and one more for
BRK-B, whose file is named after neither ticker. **Any sweep keyed on filenames must print its own
unmatched list and read it**, which is how all three defects above were caught.

## ADDED TO OPERATOR DECISIONS STILL OPEN
**Operator decision 10: do the 125 uncounted run files need a staleness marker?** 89 of them are
v3.x verdicts on names that were never queued, sitting in the same folder as the 132 runs of record
with nothing on the face of the file to say which framework produced them. **Nothing is owed as
analysis** - these names are out of scope and re-running them is not this queue's work. The question
is only whether a one-line header belongs at the top of a superseded run, and that is an edit to
history under rule 6 and therefore the operator's call, not a session's. **Standing instruction
until it is ruled: a run file dated before 2026-08-28 states a verdict under a framework no longer
in force, and is history, not an answer.**

**Nothing above this addendum was edited. No run started.** The three CSV lists, the TJX re-run, the
eight unruled shapes, the duplicate shape number 25 and the four missing entry pointers are all
untouched, per the standing instruction not to start them unattended.

---

# ADDENDUM 2026-09-20 05:32 EDT - OPERATOR RULE 5, "STRICT INPUTS", SWEPT FOR THE FIRST TIME

*An unattended cycle. WAVE 6 is closed, so this is branch C: no name to run, no file to resume, one
bounded audit, written beside the record and not over it (operator rule 6).*

**STATE READ FIRST.** All fifteen WAVE 6 names (KO, DIS, IBM, GFF, USAR, BLK, CB, TRV, AIG, CCB,
ACNB, SOFI, JPM, TFC, OTTR) carry a `## COMPLETED FROM THE QUEUE` entry **and** are struck on
normalised text; **nothing under `Test Runs/` was modified inside the 45-minute window** (`find`
returned an empty set); the lock at `05:31:56` is this cycle's own PID. Nothing to dispatch.

## RE-STRUCK FROM THE FILE, FOR THE EIGHTH TIME
**Register 132 entries, 132 distinct tickers, zero duplicates.** Gate tally **Q1 5 | Q2 92 | Q4 2 |
Q5 33**, summing to 132, **cleared Q5 ZERO** - every one of the 33 that reached Q5 fails there.
Counted from the file, not carried forward.

## WHAT HAD NEVER BEEN TESTED
Seven prior cycles swept the register, the register against disk, against the run files' gate
verdicts, against the ledger, against the operator's deliverable rule, against the sovereign-source
correction, and against operator-protocol rules 3, 4 and 6. **None tested operator rule 5, which has
three clauses and is the only rule in the protocol that governs what goes INTO a number rather than
how it is reported.** The 03:32 cycle came closest and tested one rung of one clause: Treasury
versus FRED, **for USD only**. It never asked whether the currency was right.

### CLAUSE A - "Sovereign for the EARNINGS CURRENCY, from the issuing authority, dated." HOLDS, 132/132.
**Nine runs of record report in a currency that is not the dollar, and all nine paired the sovereign
to the currency the business EARNS in, never to the listing.** This is [E4-15, E3-32] applied where
it costs something:
- **JPY, Japan MOF `jgbcme.csv`:** TM (3.995%, about 4.00%, 30-year, 2026-09-10), HMC, SONY.
- **EUR, ECB:** SPOT (3.83%, 2026-09-10) and STLA - the latter stating in its own file that *"the
  ECB curve is a fitted AAA-sovereign curve published by the central bank, not a single issuer's
  bond"*, which is the limit named rather than smoothed.
- **TWD, a currency that exists in NONE of the three sources `CLAUDE.md` names:** TSM and UMC both
  went **up** the evidence ladder rather than substituting the dollar - the issuing authority's own
  auction (the central bank acting for the MOF, 30-year, 2026-05-26) **cross-checked to the official
  secondary curve** (Taipei Exchange, dated to the observation) because the auction print was three
  and a half months old. Both files state the case FOR the USD sovereign out loud (the chips are
  billed in dollars) and both refuse it, because owner earnings are computed in NT$ from the NT$
  cash-flow statement and the cap is priced in NT$ from the Taipei quote: *"setting a USD rate
  beside an NT$ yield is the ATLKY currency defect inverted."*
- **SEK, a fourth currency outside the three:** ERIC, Sveriges Riksbank SWEA series `SEGVB10YC`,
  3.227%, 2026-09-11, **fetched by hand with nothing added to `tools/sources.py`**, and **two limits
  stated rather than hidden**: the tenor is 10-year because that is the longest benchmark the
  authority publishes, and the Riksbank's series is compiled by a data vendor, **one rung short of
  the issuing authority - so it was cross-checked to the Debt Office's own 2026-09-09 auction.**
  That is the Ford-sovereign question of the 03:32 cycle, met and answered inside the run.
- **IHG** is the reverse case and is argued, not assumed: a UK-domiciled filer reporting in dollars,
  where *"the USD sovereign is the natural pairing, and no currency conversion enters any yield."*
- Every one of the nine also shows the USD sovereign **beside** its own, and every one states that
  the choice **moves nothing**: the [E4-28] floor *"does not move with the sovereign"*, so the
  currency decides the points-over-sovereign display and never the quit-on line.

**Dated: 132/132.** **Tenor: 131 of 132 name it** (30-year, or the stated-longest-available for SEK).
**The one exception is PEP** (2026-09-02), which records the rate (**5.27%**), the date
(**2026-09-02**), the source (**US Treasury daily par yield curve, issuing authority**) and the
currency argument (56% of FY2025 net revenue US; FX carried at Q4, not in the rate) **but never
writes the tenor.** **Cross-checked rather than assumed: eighteen sibling runs struck on the same
date record 5.27% AND name the 30-year** (AATC, AEO, ANF, BRK-B, DG, DKS, GHC, HHH, L, MKL, NKE,
ORLY, QCOM, UAL, ULTA, WTM among them). **PEP's rate IS the 30-year; the omission is a word, not a
number, and nothing downstream moves.** Recorded, not corrected - the file is history under rule 6.

### CLAUSE B - "Owner earnings never via a net-income proxy." HOLDS in all 132 runs of record.
Fourteen sentences in the corpus put "proxy" beside net income or owner earnings. **Twelve are the
rule being obeyed out loud**, and the best of them are the ones where net income was tempting:
AVGO's $5,973M year-on-year swing *"that does not touch owner earnings in either year - which is
precisely why [E2-23] refuses the net-income proxy"*; BA's FY2025 net income of +$2,235M of which
$9,566M is a disposal gain; AMZN's TTM net income containing **$80,425M** of "Other income", *"almost
all of it Anthropic marks and reclassifications"*; INTC and NVDA each naming rule 5 by number.
**The positive side of the same test:** 114 of 132 name maintenance capex directly; **the residual
18 is fully explained and the true residual is zero** - fifteen use the framework's two-end bracket
(the D&A end and the capex end) instead of the phrase, and **three are the SECTOR METHOD insurers**
(AIG, CB, TRV), for which the corpus *"does not compute an owner-earnings number"* at all. AIG is
the only file in the register with **no bracket and no (c)**, which is the sector method being
followed, not a gap.

**THE TWO SENTENCES THAT ARE NOT THE RULE BEING OBEYED ARE THE MOST USEFUL THING THIS CYCLE FOUND,
AND THEY ARE NOT ABOUT THE 132.** Two runs of record report that the **superseded v3.0 file for the
same company built owner earnings on a net-income proxy**, and name it:
- **SONY:** *"The 2026-07-14 v3.0 SONY pass in `Test Runs/2026-07-14 Test Run - SONY, TBTC,
  NTDOY.md` ran on a net-income proxy ('Owner earnings uses net income as first proxy') and is
  superseded, not inherited; its figures are not used anywhere below."*
- **AMZN:** `Test Runs/2026-07-15 Run - SPOT GOOGL MSFT SHW AMZN (5-pack).md` *"(v3.0; it passed
  Amazon's moat as 'WIDE, WIDENING' and built owner earnings on a net-income proxy, which v4.1
  forbids)"*.

**This converts operator decision 10 from a tidiness question into an evidence question.** The 04:32
cycle found 125 run files that sit in `Test Runs/` and belong to none of the three counted lists, and
asked whether a staleness marker belongs on them. **Here are two of them, named by the runs that
superseded them, and the defect in both is a rule-5 violation on the one number the framework calls
the one number.** Both were caught the right way - by the later run reading the earlier one and
refusing to inherit it, which is the write-early protocol's "prior art read for what it found,
binding nothing" working exactly as intended. **Nothing is owed as analysis** and no figure in the
register comes from either file. The question the operator still owns is whether a reader who opens
the July file FIRST can tell.

### CLAUSE C - "Primary filings over aggregators; aggregators for live quotes only, flagged." HOLDS, 132/132.
Every run of record names its quote source in the same sentence as the price, and every one flags
it: *"Price $319.97 (2026-09-04, aggregator - live quote only, flagged per operator rule 5)"* (AAPL)
is the standard form, and the non-USD runs flag the local exchange instead (the Taipei quote for TSM
and UMC, the Stockholm quote and the Riksbank USD/SEK fixing for ERIC, *"never the USD ADR"*).
**Residual zero.** AATC is worth reading beside the clause: it argues that *"a company-published PDF
is primary"* under rule 5 while recording that **"it is not, however, the same document"** as the
10-K - the rule applied to a case it does not name.

## MY OWN DEFECTS - THE SIXTH CONSECUTIVE CYCLE IN WHICH THE DEFECT WAS THE READER
**Four findings accused the corpus this cycle; all four were mine, and two were caught only because
the last two cycles wrote down how.**
1. **The register first came back as 135 entries, 133 distinct, with GHC and HHH as DUPLICATES.**
   I bounded `## COMPLETED FROM THE QUEUE` at end-of-file instead of at the next heading, so bullets
   from the sections below the register were read as entries. **Bounded at the next `## ` heading it
   is 132/132/zero, eight cycles running.** A duplicate-ticker finding against a register seven
   cycles have called clean is the reader, and I built that hypothesis first.
2. **The tenor sweep first reported 26 files with NO sovereign tenor. 25 of the 26 were mine.**
   This corpus writes the 30-year at least four ways - `30-year`, `30 Yr`, `30-yr`, `30Y` - and my
   pattern took only the first. PEP is the single survivor of a variant-tolerant match.
3. **The price-flag sweep first reported 23 files whose price line names no quote source. All 23
   were mine**, twice over: my first pass matched the first source-like word anywhere in the file
   (a competitor's exchange, a split feed, the Taipei sovereign curve), and my second required the
   word "close" beside the price, which the standard form does not use. Matched on the price
   sentence itself: **132 of 132, residual zero.**
4. The maintenance-capex sweep went 42 to 18 to 0 the same way.

**The durable instruction, added beside the whitespace rule (03:32) and the filename rule (04:32):**
***a token this corpus depends on has more than one spelling, so match a token CLASS and never a
token*** - and, the narrower half of the same lesson, ***bound a section at the next heading of its
own level or higher, never at end-of-file***, which is the single error that manufactured two
phantom duplicate register entries in a register that has none.

## ADDED TO OPERATOR DECISIONS STILL OPEN
**Operator decision 11: `tools/sources.py` knows three currencies and the queue has needed five.**
TWD and SEK were both struck by hand, from the issuing authority, with their limits stated - TSM and
UMC to the central bank's auction cross-checked against the Taipei Exchange curve, ERIC to the
Riksbank's SWEA API cross-checked against the Debt Office's auction - and **neither was added to the
tool.** That was right under the tooling rule (*"does it get the same number sooner, or does it add a
number?"*), and it is also why the next non-USD run will do the same work again. **The question is
the operator's**, because a fourth and fifth sovereign in `sources.py` is a tooling change, not a
session's call; the standing practice needs no ruling to continue. **Related and narrower: the ERIC
tenor.** That sovereign is a 10-year because Sweden publishes no longer benchmark, while every other
run in the register uses a 30-year; the file states this, and whether a tenor mismatch across
currencies needs a rule is the same call.

**Nothing above this addendum was edited. No run started.** The three CSV lists, the TJX re-run, the
eight unruled shapes, the duplicate shape number 25 and the four missing entry pointers are all
untouched, per the standing instruction not to start them unattended.

---

# ADDENDUM 2026-09-20 06:32 EDT - THE LEDGER ITSELF, CHECKED AGAINST THE SOURCE DOCUMENTS FOR THE FIRST TIME. 261 OF 267 VERIFY; SIX DO NOT

**WAVE 6 IS STILL CLOSED. Branch C.** State re-struck from the files, never carried forward: the
`## COMPLETED FROM THE QUEUE` register, bounded at the next heading of its own level, holds **132
entries, 132 distinct tickers, zero duplicates**; all fifteen WAVE 6 names (KO, DIS, IBM, GFF, USAR,
BLK, CB, TRV, AIG, CCB, ACNB, SOFI, JPM, TFC, OTTR) carry an entry **and** are struck on normalised
text. Nothing under `Test Runs/` was modified inside the 45-minute window; the lock at 06:31:56 is
this cycle's own. No name to run, no file to resume. **Ninth consecutive confirmation.**

## WHAT HAD NEVER BEEN TESTED

Seven prior audits worked outward from the register: strikes, output contract, files on disk, each
run's own verdict, phantom citations in the run files, the operator protocol's rules 3/4/6, and rule
5's inputs. The 02:32 cycle got closest to the evidence, proving **37,927 citations with zero
phantom ids** and **3,027 run-file quotes all traceable to the ledger row they came from.**

**But every one of those checks resolved a citation to a ROW IN `principle_ledger.csv` AND STOPPED
THERE.** Nothing in this repository has ever asked the next question: **does the row match the
document it cites?** `tools/check_framework.py` reads five documents and the ledger's id list; it
never opens a letter, a meeting transcript or a talk. **267 rows carry the whole evidence base, and
the 37,927 citations that rest on them are only as good as the rows.** PRIME RULE 1 is the rule
under test: *"VERBATIM ONLY. The ledger takes exact quotes with year and source file. Paraphrase is
never recorded as quotation. Flag OCR and transcript artifacts; never smooth them."*

Method: each row's `quote_verbatim` matched against its own `source_file` on a letters-and-digits
normalisation (kills smart quotes, dash class, line wrapping, double spaces), with elision markers
(`...`, `[...]`) split into fragments that must appear **in document order**. 289 shelf `.txt` files
were indexed so a failed fragment could be hunted corpus-wide before being called a defect.

## THE RESULT: 261 OF 267 VERIFY VERBATIM

| outcome | rows |
|---|---|
| quote found verbatim in the cited file | **217** |
| found verbatim as ordered fragments across an elision | **44** |
| **does not verify as written** | **5** |
| source cell names a folder, not a document | **1** |

**52 rows carry an elision marker; 50 of them elide honestly.** The six that fail are below, each
read in its source and classified. **Four of the six are cited nowhere but `Framework/CHANGELOG.md`
and one is cited nowhere at all, so five of the six carry no analytic load. The sixth is cited 167
times.**

### 1. E4-19 - THE MOST-CITED DEFECTIVE ROW, AND THE SMOOTHING REACHED THE FRAMEWORK'S OPENING PAGE

`Annual Meetings/2006 Annual Meeting.txt`, cited **167 times across 144 files**, including the
epigraph of **I. THE FOUR VERDICTS** in `Framework/THE FRAMEWORK v4.md`. Two defects:

- **A transcript artifact was smoothed away.** The transcript reads *"...in, out, and too hard."
  **(Laughter)** And a lot of things end up in the 'too hard' pile..."*. The ledger row deletes
  `(Laughter)` and closes the gap without a mark. **PRIME RULE 1 names this exact case: "Flag OCR
  and transcript artifacts; never smooth them."** The framework's epigraph reproduces the smoothed
  text, so the deletion is live in the governing document, not only in the ledger.
- **The two halves are spliced in REVERSE transcript order.** *"What I've learned is I know enough
  not - to know that I don't know enough to make an investment decision"* is Buffett answering an
  **earlier** question about IBM, Sun, Oracle, Dell, EMC and Intel; it stands at offset 49,771,
  while the "three boxes" passage stands at 51,226. The row joins them with `[...]`, which a reader
  takes as "text omitted between", and the order is backwards.

**The splice has never propagated.** Of the 144 files citing E4-19, **143 cite the id with no quoted
text at all** and the one that quotes (the framework) quotes only the "three boxes" clause. The
reverse-order defect is real and latent; the `(Laughter)` deletion is real and live.

### 2. E2-02 - THE ONE DEFECT THAT CHANGES A MEANING

`Shareholder Letters/1981 Letter.txt`. Both fragments are verbatim, and they are **inverted**. The
letter's order is: *"if all earnings are **paid out** and return on equity stays at 14% - the 7%
tax-exempt equivalent ... is just as frozen as is the coupon on a tax-exempt bond"* (offset 17,792),
**then** *"**If, on the other hand, all earnings ... are retained** ..., earnings will grow at 14%
per year"* (offset 18,062). The row prints the retention sentence first, then `[...]`, then the
paid-out conclusion with the words *"if all earnings are"* cut off the front. **Read as written, the
frozen-coupon conclusion attaches to the retention case, which is the opposite of the passage's
argument** - Buffett's whole point there is that the two cases differ. Cited only in the changelog.

### 3. E4-07 - AN UNMARKED CONDENSATION INSIDE A VERBATIM CELL

`Shareholder Letters/1999 Letter.txt`. Source: *"...but **the direction in which value is going to
go** is in no way ordained."* Ledger: *"...but **the direction of change** is in no way ordained."*
Nine words replaced by three, no bracket, no ellipsis. The sense is preserved and the row is
therefore easy to defend and still **not verbatim**, which is the only standard the column claims.

### 4. E1-09 - A BRACKETED SUBSTITUTION THAT DROPS THE NUMBER

`Partnership Letters/1966-01-20 Partnership Letter.txt`. Source: *"...of achieving **performance
surpassing the Dow by, say, fifteen percentage points per annum**."* Ledger: *"...of achieving
**[performance superior to the Dow]**."* The brackets are honest signalling, but **the substitution
removes the magnitude**, and magnitude is the interesting half of that sentence. **This is the only
row in all 267 that inserts editorial text of its own**; the one other bracketed insertion, E3-60's
`[Benjamin]`, is the transcriber's, present in `Annual Meetings/1997 Annual Meeting.txt` itself, and
carrying it through is correct.

### 5. E3-20 - HERE THE LEDGER IS RIGHT AND THE SHELF IS DAMAGED

`Munger Talks (PCA)/Talk 02 ... USC, 1994-04-14.txt` reads *"The model I like...is **the at the
racetrack**."* The file on disk has a hole where "pari-mutuel system" belongs; the ledger row
supplies the two words. Almost certainly the true text (Munger's next sentence in the same file is
*"a pari-mutuel system is a market"*) and **still a repair made silently inside a verbatim cell**,
and the defect it repairs is in the source file, which nobody has been told about. **Under THE
STANDARD this row cannot be verified against its source in two minutes; it can only be inferred.**

### 6. E5-07 - NOT A QUOTE, AND SAYS SO

`source_file` is `Wesco Letters (Munger)/`, a folder. The cell is a **negative finding**, opening
`NOTE:` and recording that the 1997-2009 Wesco letters yielded no quotable philosophy, with
`supports_gate_or_sheet` reading *"n/a - negative finding recorded per Prime Rule 1"*. Correct
behaviour, deliberately logged, cited **zero** times. It is flagged here only because **`CLAUDE.md`
describes the file as "267 verbatim rows - the evidence base"**, and the honest count is **266
quotes plus one mining record.**

## WHAT THIS DOES AND DOES NOT DISTURB

**It disturbs no verdict.** Five of the six rows are cited only in the changelog or not at all, and
the sixth is cited by id in 143 files that quote nothing. **No run's gate turns on a defective
row.** What it disturbs is the claim the acceptance test implies and has never tested: that a cited
id resolves to a verified quote. **260 of 267 rows now carry that guarantee for the first time**
(261 verify, less E3-20 whose source is damaged), and six are documented.

## MY OWN DEFECTS - THE SEVENTH CONSECUTIVE CYCLE IN WHICH THE READER WAS WRONG, AND THE FIRST IN WHICH THE RULE CAUGHT THEM BEFORE THE WRITE-UP

Three artifacts, all killed before anything was claimed, by the 02:32 rule *"construct the
hypothesis in which the finding is an artifact of my own parse, and kill that one first."*

1. **"25 rows cite a source file that does not exist."** They cite it with a line range attached:
   `Shareholder Letters/1983 Letter.txt (lines 136-146)`. **The `source_file` column has two
   spellings** - bare path in 242 rows, path plus parenthetical locator in 25 - which is the 05:32
   rule (*a token this corpus depends on has more than one spelling*) recurring in a new column.
2. **"E5-07's source file is unreadable."** It is a directory. A path column may hold a folder.
3. **`grep` returned nothing for strings I had just proved were present.** The shelf files are
   hard-wrapped, and `grep` is line-based. **Every text check against this shelf must collapse
   whitespace before matching**, exactly as the 03:32 cycle found for the run files.

**The durable instruction, written beside the whitespace rule (03:32), the filename rule (04:32) and
the token-class rule (05:32): A VERBATIM CHECK IS A CHECK ON TWO DOCUMENTS, AND EITHER CAN BE THE
DAMAGED ONE.** E3-20 is the case: the finding looked like a ledger defect and is a shelf defect.
When a quote does not match, search the whole shelf for the fragment before naming the ledger wrong.

## ADDED TO OPERATOR DECISIONS STILL OPEN

12. **The six rows above.** Four are one-line repairs against a source the repository already holds
    (E2-02 order, E4-07 condensation, E1-09 bracket, E4-19 `(Laughter)` plus order), **but a ledger
    row is evidence, and PRIME RULE 6 puts an edit to the evidence base above a session's pay
    grade**; E4-19's repair additionally means editing the epigraph of `THE FRAMEWORK v4.md`. **None
    was touched.** Recommended order if the operator wants them: E4-19 first (167 citations, and the
    smoothing is in the governing document), then E2-02 (the one that misreads).
13. **`Munger Talks (PCA)/Talk 02 ... .txt` has a hole in it** at *"is the at the racetrack"*. That
    is a source-shelf repair, not a ledger one, and it needs the operator's own copy of the
    Almanack. **Until it is repaired, E3-20 is the only row in the ledger that cannot be verified
    from disk.**
14. **Should the verbatim check become part of the acceptance test?** It runs in under two seconds
    over 267 rows and 289 shelf files, it concludes nothing and computes nothing new, and it is the
    only machine check that would enforce PRIME RULE 1 rather than assume it. **Same standing as
    decision 7** (the phantom sweep over `Test Runs/`): widening `check_framework.py` is the
    operator's call. **Both would pass today apart from the six rows above, so both lock in a
    property rather than open a backlog.** The script used this cycle is left at
    `tools/_tmp_ledger_audit.py` for the operator to read, adopt or delete; it is named `_tmp` and
    is wired to nothing.

**Nothing above this addendum was edited. No run started.** The three CSV lists, the TJX re-run, the
eight unruled shapes, the duplicate shape number 25 and the four missing entry pointers are all
untouched, per the standing instruction not to start them unattended.

---

# ADDENDUM 2026-09-20 07:32 EDT - PRIME RULES 3 AND 4, SWEPT FOR THE FIRST TIME. BOTH HOLD WHERE THEY GOVERN; SEVEN FILES SHOW THAT CONFESSION IS NOT AUTHORIZATION

**Overnight cycle. Branch C: no name to run.** State re-read before anything was done.

## RE-STRUCK FROM THE FILE, FOR THE TENTH TIME

Register bounded at the next heading of its own level (the 05:32 rule), entries matched on the
corpus's actual head pattern `- **TICKER (Name), date`:

- **132 entries, 132 distinct tickers, zero duplicates.**
- **Zero unmatched top-level bullets** - the sweep printed its own unmatched list and it was empty
  (the 04:32 rule).
- All fifteen WAVE 6 names carry a register entry **and** are struck on normalised text.
- Nothing under `Test Runs/` modified inside the 45-minute window. The lock at 07:31:56 is this
  cycle's own.

**My first pattern returned zero entries** and would have reported the register empty. The corpus
writes `- **TFC (Truist Financial Corporation), 2026-09-19 - ...`, not `- **TFC**`. Eighth
consecutive cycle in which the first finding was the reader's defect, and the unmatched-list rule
caught it before it reached a claim.

## WHAT HAD NEVER BEEN TESTED

Seven prior cycles audited the register (00:32, 01:34), the run files' citations (02:32), the
operator's deliverable contract and the sovereign rung (03:32), operator rules 3/4/6 (04:32),
operator rule 5 (05:32) and the ledger against the shelf (06:32). **Every one of them audited the
OPERATOR PROTOCOL or the evidence base. The PRIME RULES - the six rules in `CLAUDE.md` that govern
what may enter the corpus and from where - have never been swept.** PRIME RULE 1 was reached
sideways at 06:32. This cycle takes **PRIME RULE 3 (CONFESS INVENTIONS)** and **PRIME RULE 4 (THE
CITATION SHELF)**, the two that decide admissibility.

## PRIME RULE 4 HOLDS WHERE IT GOVERNS

**The governing documents are clean.** `THE FRAMEWORK v4.md`, `THE HOLDINGS FRAMEWORK.md` and both
run templates contain **zero** occurrences of Graham, Security Analysis, The Intelligent Investor,
Graham-Newman or Doddsville, on a whitespace-normalised whole-file read. The shelf amendment of
2026-07-13 is fully executed in the documents that decide verdicts.

**The ledger obeys the amendment exactly as written.** Graham is named in `principle_ledger.csv`
only **inside** verbatim Buffett/Munger sentences - E2-12 (*"Ben Graham, my friend and teacher"*),
E4-05 (*"Long ago, Ben Graham taught me that 'Price is what you pay; value is what you get.'"*),
E3-65 (Munger: *"a Ben Graham-style basis"*), the 1997 meeting row - plus `evolution_notes` cells
that record the amendment itself (*"cite this, not Graham directly (shelf amendment 2026-07-13)"*).
**Not one row cites Graham as a source.** This is the rule's own prescription performed.

**The one gap is in the rule's wording, not the practice.** PRIME RULE 4 names **seven** source
classes. The ledger draws on **eight** folders:

| folder | rows | named by PRIME RULE 4? |
|---|---|---|
| Shareholder Letters | 142 | yes - Berkshire letters |
| Annual Meetings | 57 | yes - meeting transcripts |
| Munger Talks (PCA) | 29 | yes - Poor Charlie's Almanack |
| Partnership Letters | 18 | yes |
| **Special Letters** | **8** | **NO** |
| Fortune Essays (Buffett) | 7 | yes |
| Wesco Letters (Munger) | 3 | yes |
| Owners Manual | 3 | yes - An Owner's Manual |

**"Special Letters" is the 2014 50th-anniversary pair**, `2014 Warren Buffett - Past Present
Future.txt` and `2014 Charlie Munger - Past Present Future.txt` - published inside the 2014
Berkshire annual report and therefore substantively Berkshire letters, but not named by the shelf as
written. **It is not an off-shelf source and nothing here is contaminated.** It matters only because
those 8 rows carry real load: **E5-11** is the three strengths of staying power, quoted in Q4 of the
governing framework, and **E5-19** is the row `CLAUDE.md`'s own operator rule 7 cites for the honest
record - *the man, the system, luck and devotion*. The most load-bearing attribution in the operator
protocol rests on a source class the citation shelf does not name.

## THE ONE RUN FILE THAT CITES GRAHAM AS A SOURCE - AND IT DECLARES ITSELF

All 1,043 `.md` files under `Test Runs/` were swept. **Ten non-company hits in four files.** Six are
*Golden Grahams*, the General Mills cereal, in a CL peer section - the token-class trap for the
third cycle running, now in breakfast form. Two are descriptive and compliant: UNTC's *"closer to a
Graham-style statistical bargain"* and the 5-pack's *"a Graham cigar butt, not a Munger business"*
cite nothing and use the phrase **exactly as Munger uses it verbatim in E3-65**.

**The remaining two are both in `2026-07-20 Run - HGRAF (HydroGraph Clean Power).md`, and they are
an independent Graham citation carrying load:**

> - Graham's ledger anchor [SA, book p.54, eye-verified]: *"An investment operation is one which,
>   upon thorough analysis, promises safety of principal and a satisfactory return. Operations not
>   meeting these requirements are speculative."*

and its **SELF-AUDIT certifies it**: *"[x] Classification grounded in both frameworks' own texts
(Gate 1 evaluability; Graham ledger anchor, eye-verified)"*. Dated **seven days after** the
2026-07-13 amendment.

**Read fairly, this is not a smuggled citation.** The file's header declares `Framework v3.0` and a
deliberate two-framework run, and `README.md` documents the companion Graham build from his own two
books as a separate parallel artifact. The corpus's own standard is stated **first and
independently**, and the verdict is FAIL at Gate 1 on the framework's own grounds; **the Graham
anchor is additive and no verdict turns on it.** What is missing is that the run never names the
amendment it is stepping outside of. **PRIME RULE 4 removed Graham from the shelf; it never said
whether a declared dual-framework run may draw on the companion build.** That question is open, and
it is the operator's.

## PRIME RULE 3 HOLDS, AND IS THE BEST-IMPLEMENTED RULE IN THE REPOSITORY

**Governing documents: 16 CONVENTION labels, 16 rationales. No exceptions.** `THE FRAMEWORK v4.md`
carries a dedicated register - **VI. THE CONFESSED CONVENTIONS**, seven rows, each with a "Why it
exists" cell, headed *"Everything invented that survives, in one place. Nothing else in this
document is ours."* `THE HOLDINGS FRAMEWORK.md` labels five, each with its reasoning and its ledger
id. The `SECTOR METHOD` goes furthest: a section titled **"WHAT IS CONVENTION HERE, AND WHY -
confessed, per PRIME RULE 3"**, conventions numbered 1 to 5, each with an italic *Rationale:*, and
CONVENTION 4 additionally carries the record of its own successful test (the WTM float recipe
reproducing Markel's first published float to within 1.1%).

**Run files: 390 labels across `Test Runs/`.** 243 carry an inline rationale; 55 resolve by pointer
to a numbered convention in a governing document (`CONVENTION 4`, `v4 section VI`, `SECTOR METHOD`)
- which is the correct pattern, not a gap. The residual 92 were sampled, not classified one by one,
and the sampled ones are self-audit checkboxes restating a label defined earlier in the same file,
or an inline metric definition that **is** the rationale (ULTA's net-tangible-operating-assets
line). **I found no unconfessed invention. I also did not prove there is none, and say so here
rather than report a clean sweep I did not run.**

**The other limb of the rule - "or it is deleted" - is discharged and then some.**
`Framework/INVENTIONS - deleted and why.md` records the v3.1 audit's classification (9
corpus-sourced, 14 derived, **43 invented, all deleted**) and its Section V, **VERIFICATION OWED**,
sets two non-optional tests plus a standing third. **All three were performed**: `Framework/v4/
VERIFICATION - the two cases that decide the deletions.md` (Citigroup 2007, Coca-Cola 1988), and the
six live names re-run **three times** - `REGRESSION - the six live names under v4.md`, `RERUN - the
six live names under the Q3 weight rule.md`, `RERUN 3 - the six names under the v4.1 floor.md`.

**One flag, and it is a flag and not a defect.** The file says *"This file records what each one
did"* of the 43, and `CLAUDE.md` points to it as *"the 43 deletions and what they cost"*. The file
itemises them in **21 entries** - 5 narrative sections plus a 16-row table - several of which bundle
several rules (entry 3 is the 4% floor **and** the +1% **and** the +2% premium; entry 5 is a
six-component ladder). **The 43 is a classification count the file states about itself; no
entry-by-entry mapping to it exists, so the claim is plausible and not individually checkable.** I
had this written as a defect - "the pointer says 43 and the file holds 21" - before expanding the
bundles. Under the 2026-09-19 rule *count the file, never the pointer*, the count here is honest and
the pointer is fine.

## THE CYCLE'S REAL FINDING: A CONVENTION LABEL WAS USED TO LICENSE WHAT A RULE FORBIDS

**Seven run files, all dated 2026-07-15, label a net-income proxy for owner earnings a FRAMEWORK
CONVENTION.** `MTSUY (Mitsubishi)` is the origin and states the case in full - *"FRAMEWORK
CONVENTION - not attributable to Buffett/Munger: for a sogo shosha, the standard OE formula (NI +
D&A - maintenance capex) does not map cleanly onto the business"* - and **six inherit it by pointing
at it**: `ITOCY`, `MARUY`, `MITSY`, `SSUMY` (*"as documented in the MTSUY run"*), `NPNYY` and
`FUJIY` (*"same convention as the sogo shosha runs, for the same reason"*).

**MTSUY's self-audit checks the box on it**: *"[x] OE convention (NI as proxy) documented explicitly
as a FRAMEWORK CONVENTION, not silently substituted for the full formula."*

**PRIME RULE 3 was obeyed to the letter. Operator rule 5 was broken by the thing it confessed.**
Rule 5 reads *"Owner earnings never via a net-income proxy"* - never, with no convention clause.
**A CONVENTION covers what the corpus does not supply; it cannot cover what a rule forbids.
Confession is not authorization, and the two rules have never been reconciled in writing.** The
seven files sit in that gap, and the self-audit checkbox is the proof they thought they were inside
it.

**Two things this does not disturb.** First, **v4 closed the hole from the other side**: section VI's
confessed convention is *"Owner earnings via operating cash flow less SBC, less the (c) guess"* -
the opposite construction - and the 05:32 cycle proved clause B holds in **all 132 runs of record**.
The 2026-09-18 runs show the discipline working out loud: SPGI writes *"Built by hand from the filed
cash-flow statements; never a net-income proxy."* Second, **none of the seven is in the register**,
so no counted verdict and no register figure rests on any of them.

**What it does do is enlarge the 04:32 cycle's operator decision 10 for the second night running.**
That decision asks what to do about the 125 run files that hold a verdict and are in none of the
counted lists. The 06:32 cycle named **two** of them as carrying a rule-5 violation on the one
number (SONY, AMZN). **This cycle names seven more, and the seven are worse in one specific way:
06:32's two were caught because the LATER run read the earlier one and refused to inherit it. Here
the inheritance succeeded - one file invented it and six adopted it by citation in a single day.**
Nine of the 125 are now named.

## MY OWN DEFECTS - THE EIGHTH CONSECUTIVE CYCLE IN WHICH THE READER WAS WRONG

1. **The register pattern returned 0 of 132** (`**TICKER**` against a corpus that writes
   `**TICKER (Name), date`). Caught by the unmatched-list rule before it became a claim.
2. **"The INVENTIONS file holds 21, not 43."** Wrong - the entries bundle. Caught by reading the
   file instead of counting its headings.
3. **"248 of 390 CONVENTION labels carry no rationale."** Wrong twice: the marker list was too
   narrow (it missed *"not attributable to Buffett/Munger"* and *"as documented in the MTSUY run"*),
   and it had no notion of a label resolving by **pointer** to a numbered convention. 248 to 147
   to 92, and the 92 are a wording pattern.
4. **Six of ten Graham hits in 1,043 run files were a breakfast cereal.**

**Durable instruction, added beside the whitespace rule (03:32), the filename rule (04:32), the
token-class rule (05:32) and the two-documents rule (06:32): A RULE CAN BE OBEYED AND BROKEN BY THE
SAME SENTENCE.** Auditing a rule means asking not only *was it followed* but *what did following it
authorize* - the seven sogo shosha files pass PRIME RULE 3 and fail operator rule 5 on one line of
text, and no check that reads one rule at a time can see it.

## ADDED TO OPERATOR DECISIONS STILL OPEN

15. **PRIME RULE 3 and operator rule 5 have never been reconciled.** Should PRIME RULE 3 carry an
    explicit limit - *a CONVENTION may cover what the corpus does not supply; it may never cover
    what a rule forbids*? The seven 2026-07-15 files are the worked case, and their self-audits show
    the gap is real rather than theoretical. **This is an amendment to a PRIME RULE, which PRIME
    RULE 5 puts above a session's pay grade. Not touched.**
16. **PRIME RULE 4's shelf names seven classes; the ledger draws on eight.** "Special Letters" - the
    2014 50th-anniversary essays, 8 rows - is substantively part of the 2014 Berkshire annual report
    and is **not** an off-shelf source, but the rule does not name it, and E5-19 from that class is
    what `CLAUDE.md`'s own operator rule 7 cites. **One clause in PRIME RULE 4 closes it. Amending a
    PRIME RULE is the operator's call. Not touched.**
17. **May a declared dual-framework run draw on the companion Graham build?** `2026-07-20 Run -
    HGRAF` does, seven days after the shelf amendment, with a verbatim Security Analysis quote and a
    self-audit checkbox certifying it - while stating the corpus's own standard first and
    independently, and reaching its FAIL on the framework's own grounds. **PRIME RULE 4 removed
    Graham from the shelf and is silent on the companion. Same standing as decision 10** (a
    pre-v4.1 file that holds a verdict); **the minimum repair is one sentence in the run naming the
    amendment it steps outside of, which is an edit to history under PRIME RULE 6. Not touched.**

**Nothing above this addendum was edited. No run started.** The three CSV lists, the TJX re-run, the
eight unruled shapes, the duplicate shape number 25 and the four missing entry pointers are all
untouched, per the standing instruction not to start them unattended.

---

# ADDENDUM 2026-09-20 08:32 EDT - OPERATOR RULES 1 AND 2, THE TEMPLATE AND THE HARD SEQUENCE, SWEPT FOR THE FIRST TIME. THE SEQUENCE HOLDS 132/132; THE Q5 VERDICT BOX CANNOT EXPRESS THE VERDICT THE REGISTER RECORDS 33 TIMES

**State read before anything was touched.** All fifteen WAVE 6 names carry a `## COMPLETED FROM THE
QUEUE` entry and are struck; nothing under `Test Runs/` was modified inside the 45-minute window;
the lock at 08:31:56 is this cycle's own. No name to run, no file to resume. Branch C.

## RE-STRUCK FROM THE FILE, FOR THE ELEVENTH TIME

Register **132 entries, 132 distinct tickers, zero duplicates**, the section bounded at the next
heading of its own level (`## THE WRITE-EARLY PROTOCOL`) rather than at end-of-file, per the 05:32
rule. Gate tally read per entry on normalised whitespace: **Q1 5 | Q2 92 | Q4 2 | Q5 33 = 132, zero
unmatched, cleared Q5 ZERO.** Eleventh consecutive confirmation.

## WHAT HAD NEVER BEEN TESTED

Ten prior cycles swept the register, the register against disk, the register against the run files'
gate verdicts, the ledger, the ledger against its own sources, the deliverable rule, the sovereign
correction, operator protocol rules 3, 4, 5 and 6, and PRIME RULES 3 and 4. **Operator rules 1 and
2 had never been touched, and they are the two that decide the SHAPE of a run:**

> **1. RUN FILE FIRST.** Copy `Test Runs/_TEMPLATE - Company Run.md` to a dated file and fill it top
> to bottom. **The template is the enforcement surface.**
> **2. HARD SEQUENCE.** No Q5 output may be reported unless Q1-Q4 each show IN. UNRESEARCHED and
> UNKNOWABLE both close the file; neither is a pass.

`check_framework.py` reads five documents and never opens a run file's gate structure. Rule 3's
half of this was checked at 04:32 (99 of 99 early-closing runs carry the `COMPUTATION - NOT A
CLEARANCE` heading). **Nothing had ever asked whether the gates themselves are declared in order.**

## THE HARD SEQUENCE HOLDS, 132 OF 132

Every run of record was resolved, its gate sections located, and the first verdict checkbox inside
each section read. Two tests, both directions:

- **Of the 33 runs the register calls FAIL AT Q5, all 33 declare Q1, Q2, Q3 and Q4 as `[x] IN`.**
  Not one reports a Q5 output on an unopened or non-IN gate.
- **Of the 99 runs that closed at Q1, Q2 or Q4, not one declares its closing gate IN**, and not one
  skips an earlier gate: every gate before the closing gate is `[x] IN` in every file.

**Zero violations.** The corroborating fact, which is the framework's own record rather than a
check: **no run in 132 has ever cleared Q5.** All 33 that reached it carry ranking language, all 33
cite the **[E4-28]** floor, and all 33 are explicitly **NOT RANKED** or **quit on**.

## THE CYCLE'S REAL FINDING: Q5 IS THE ONE GATE WHOSE VERDICT BOX HAS NO "OUT"

The template's verdict lines, read side by side:

| gate | template verdict line |
|---|---|
| Q1-Q4 | `VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED -> ____  [ ] UNKNOWABLE -> ____` |
| **Q5** | `VERDICT: [ ] IN  [ ] UNRESEARCHED -> ____  [ ] UNKNOWABLE -> ____ · ranking position ____` |
| Q6 | `Verdict: [ ] IN [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence)` |

**Q5 offers no OUT.** The design is coherent and deliberate: at Q5 "IN" means *the question is
answered and it produces a number*, and the rejection is carried by the **ranking position** field,
below the floor and therefore quit on rather than placed. **But the register records the outcome 33
times as "FAIL AT Q5", and that is a verdict the template's Q5 box cannot write.** The corpus
resolves the gap four different ways, and this had never been counted:

- **24 of 33 write no Q5 checkbox at all** and carry the outcome in prose (AAPL, KO, WMT, TXN,
  SPGI, BRK-B, CB, GFF and sixteen others). This is the template followed to the letter: the box is
  skipped, the ranking field does the work.
- **ORLY writes `[x] IN`** *(the question is answered, the evidence is here and it produces a
  number)* **· ranking position: NOT RANKED, below the [E4-28] floor**, then the plain answer:
  *"The answer is no, and it is a price answer, not a business answer."* **This is the template used
  exactly as designed, and it is the queue's first name ever to reach Q5.**
- **AVGO improvises a compound**: `VERDICT: [x] IN as an analysis, FAIL on price - the name is QUIT
  ON at the [E4-28] floor`. It wanted the word FAIL in a box that has no FAIL.
- **AMAT improvises a negation**: `VERDICT: [x] IN is NOT reached and UNKNOWABLE is NOT used - the
  name FAILS at Q5`. It ticked the box in order to say the box does not apply.

**All four are right and the register is right in all 33 cases. Nothing is owed as analysis.** What
the finding does is name a trap: **any automated check that reads the Q5 checkbox inverts ORLY.** It
would score `[x] IN` at Q5 as a clearance on the one name the queue calls its first to reach that
gate, and it would score AMAT as IN on a sentence that says IN is not reached. This is the 03:32
standing instruction arriving from a second direction: **read the pass/fail by prose, never by
token**, and now with the reason, which is that the token does not exist for this gate.

## OPERATOR RULE 1 - "FILL IT TOP TO BOTTOM" AGAINST RULE 2 - "STOP AT THE FIRST THAT IS NOT IN"

The two rules pull opposite ways and the corpus has always resolved it the same way, which is worth
writing down because no document says it. Swept on fourteen template sections: **122 of 132 runs
carry every section token; the 10 that do not are missing only Q4 subsections** (great/good/
gruesome, the three strengths, the named way it dies) **and every one of them closed at Q1 or Q2**,
declaring the remainder unopened in terms: DKS `## Q3 · Q4 · Q6 - NOT OPENED`, AATC `## Q3 · Q4 ·
Q5 · Q6 - NOT OPENED`, DELL `## Q3, Q4, Q5, Q6 - NOT OPENED`. The other 122 reach the Q4 vocabulary
because they record material past the closing gate under **RECORDED, NOT ADJUDICATED** or **NOT
GOVERNING**, which the framework permits and rule 2 keeps out of the verdict. **Rule 1 governs the
SURFACE, rule 2 governs the SEQUENCE; the file is filled down to the gate that closes it and the
remainder is marked unopened by name.** No file was found that quietly omits a section it reached.

**A cross-check that came free.** Twenty files carry an UNRESEARCHED or UNKNOWABLE gate somewhere.
In every one the non-IN gate is either **the closing gate itself** (BIRD, DJT, HHH, RGTI, USAR at
Q1; MBGL at Q2; GOOGL, GRMN, KLAC, MSFT at Q5) **or a gate AFTER the close**, recorded and not
governing (CCB and SOFI Q3/Q4 UNRESEARCHED behind a Q2 close; BE, DASH, META, PATH, PUBM Q4
UNKNOWABLE behind a Q2 close; OTTR Q3, Q4 and Q5 all UNKNOWABLE behind a Q2 close). **Not one file
treats an UNRESEARCHED or UNKNOWABLE gate as a pass, which is the second sentence of rule 2.**

## THE FOUR MISSING ENTRY POINTERS, NAMED FOR THE FIRST TIME

The standing untouched item has read "the four missing entry pointers" since 00:32 without naming
all four. They are **CB, ACNB, SOFI and BLK**. ACNB's register entry cites no `.md` file at all;
SOFI's and BLK's cite only `PORTFOLIO.md`; CB's cites the SECTOR METHOD and the MKL competitor row.
All four run files exist on disk and were read for this sweep (`2026-09-19 Run - ACNB ACNB
Corporation.md`, `2026-09-19 Run - SOFI SoFi Technologies.md`, `2026-09-19 Run - BLK BlackRock.md`,
`2026-09-19 Run - CB Chubb.md`) and all four pass the hard sequence. **The gap is a pointer, not a
run.** Adding one is an edit to history under PRIME RULE 6; left untouched, now named.

## MY OWN DEFECTS - THE NINTH CONSECUTIVE CYCLE IN WHICH THE READER WAS WRONG

Three findings accused the corpus this cycle and all three were mine.

1. **"CB is missing ten of fourteen template sections."** I resolved each entry to its run file by
   taking the **first** backticked `.md` in the entry, and CB's entry cites a competitor row from
   another company's research folder before it cites anything of its own. I was auditing a
   competitor table against a company-run template. **A register entry cites many files; only some
   of them are its own.** Resolution was rebuilt to prefer a cited file whose basename names the
   ticker, and CB then passed clean.
2. **"ACNB and JPM report a Q5 output with Q3 never declared"**, a hard-sequence violation on two
   of the five banks, which would have been the most serious finding any of these cycles produced.
   It was a **40,000-character window cap** in my own section reader. ACNB's Q3 section runs 43,035
   characters and JPM's runs 59,254; both declare `VERDICT: [x] IN - at GATE weight` at the very
   end of it. **Bank Q3 sections in this corpus are longer than a whole run file elsewhere.** Cap
   removed, both passed, and the flagged count went 2 to 0.
3. **"AMAT and AVGO declare Q5 IN against a register that says FAIL."** Both matched `[x] IN`
   inside sentences that say the opposite; AMAT's is literally *"[x] IN is NOT reached"*. This is
   the 03:32 lesson again and it is why the Q5 finding above is written as a trap rather than as a
   defect: **the checkbox and the sentence disagree, and the sentence is the verdict.**

**Durable instruction, added beside the whitespace rule (03:32), the filename rule (04:32), the
token-class rule (05:32), the two-documents rule (06:32) and the authorization rule (07:32): A
CHECKBOX IS NOT A VERDICT IN THIS CORPUS - READ THE SENTENCE IT SITS IN.** Every one of the three
defects above is a tick mark read without its clause, and the framework's own Q5 box is the reason
that habit is unsafe rather than merely sloppy. Second half, learned from the bank sections: **never
bound a section by a character budget; bound it by the next heading of its own level or higher.**

## ADDED TO OPERATOR DECISIONS STILL OPEN

18. **The Q5 verdict box has no OUT, and the register writes "FAIL AT Q5" 33 times.** The design is
    defensible: at Q5 the rejection is a ranking position, not a verdict about the business, which
    is exactly what ORLY's *"a price answer, not a business answer"* says. But two runs improvised
    wording to get the word FAIL into the box, 24 skipped the box, and one used it as designed in a
    way an automated reader would invert. **Should the template's Q5 line name the outcome
    explicitly** (`[ ] IN - ranked ____` / `[ ] IN - NOT RANKED, below the [E4-28] floor`)? That is
    a change to the enforcement surface, which operator rule 1 makes the governing artifact and
    PRIME RULE 5 puts above a session's pay grade. **Standing instruction until ruled: at Q5, read
    the ranking position and the prose, never the checkbox. Not touched.**
19. **The four register entries that do not point at their own run file are CB, ACNB, SOFI and
    BLK** (item named above). All four runs exist and all four are sound. **Adding the pointer edits
    history under PRIME RULE 6. Not touched.**

**Nothing above this addendum was edited. No run started.** The three CSV lists, the TJX re-run, the
eight unruled shapes and the duplicate shape number 25 are all untouched, per the standing
instruction not to start them unattended.

---

# ADDENDUM 2026-09-20 09:32 EDT - OPERATOR RULES 7, 8 AND 9, THE LAST THREE NEVER AUDITED. ALL THREE HOLD. BUT A LEDGER ID IS NOT A UNIQUE KEY TO A PASSAGE, AND FIVE PASSAGES ARE ENTERED TWICE

**State read before anything was touched.** All fifteen WAVE 6 names carry a `## COMPLETED FROM THE
QUEUE` entry and are struck; nothing under `Test Runs/` was modified inside the 45-minute window;
the lock at 09:31:56 (pid 9096) is this cycle's own. No name to run, no file to resume. Branch C.

## RE-STRUCK FROM THE FILE, FOR THE TWELFTH TIME

Register **132 entries, 132 distinct tickers, zero duplicates**, the section bounded at the next
heading of its own level (`## THE WRITE-EARLY PROTOCOL`, line 9774) rather than at end-of-file, per
the 05:32 rule. Gate tally read per entry on normalised whitespace: **Q1 5 | Q2 92 | Q4 2 | Q5 33 =
132, zero unmatched, cleared Q5 ZERO.** Twelfth consecutive confirmation.

## WHAT HAD NEVER BEEN TESTED

Eleven prior cycles swept the register, the register against disk, the register against the run
files' gate verdicts, the ledger, the ledger against its own sources, the deliverable rule, the
sovereign correction, **operator protocol rules 1, 2, 3, 4, 5 and 6**, and PRIME RULES 3 and 4.
**Rules 7, 8 and 9 are the three that were left, and they are the three that govern the ANALYST
rather than the filing:**

> **7. STATE THE HONEST RECORD WHEN ASKED.** The market-beating claim is **UNPROVEN** ... **Never
> present the framework as proven to beat the market.**
> **8. THE DIVISION OF LABOR.** Arithmetic is automated; judgment is made by the AI running the
> framework; **every judgment is justified from the corpus by ledger id, or it is not a judgment -
> it is an opinion.** Tools fetch and compute and are **forbidden to conclude**; every flag is a
> prompt to read, never a score.
> **9. THE ANALYST IS ALSO A SUBJECT OF THE PSYCHOLOGY.** ... the antidotes are the corpus's own:
> **[E4-26]**, **[E3-41]**, **[E4-27]**.

`check_framework.py` tests that a cited id EXISTS in `principle_ledger.csv`. **Nothing has ever
asked whether the gate that decided a run was justified by one at all.**

## RULE 8 HOLDS, 132 OF 132, AND NOT NARROWLY

Each register entry was resolved to its run file, each file split into gate sections bounded by the
next heading of its own level or higher (the 08:32 rule, adopted rather than re-learned), and every
GOVERNING gate - Q1 through the gate the register says closed the file - tested for a ledger id.

- **Zero files carry a governing gate with no ledger id.** Not one gate in 132 runs.
- **At the CLOSING gate specifically** - the section that actually carries the verdict - the
  distinct-id count runs **minimum 4, median 19, mean 22.9, maximum 87.** The thinnest closing
  gates are DJT and USAR at 4, and both closed at Q1 UNKNOWABLE, where the finding is that the
  document does not exist and there is less to cite.
- **Corpus-wide: 183 distinct ledger ids are in live use across the 132 runs**, median 69 distinct
  ids per run, minimum 39 (DKS, AATC), maximum 115 (JPM). **Zero phantom ids**, confirming 02:32
  from a second direction.
- **The second half of rule 8 holds too.** Every occurrence of `acquisition_flag`, `level_shift`,
  `run.py` and `check_framework` in the run files was read in a 400-character window for
  conclusion language. **Zero passages assert a tool output as a verdict.** The flag is a prompt to
  read everywhere it appears.

**The weakest governing gate in a file is almost always Q1**, and 18 runs rest Q1 on a single
ledger id. That is coherent rather than thin: Q1 asks whether the business can be understood, and
the answer is carried by the filing, with the corpus supplying the standard (**[E3-16]**, the
circle of competence) rather than the evidence. Q2, Q3 and Q4 run 13 to 29 ids apiece.

## RULE 7 HOLDS, AND THE ONE APPARENT VIOLATION IS GM'S OWN 10-K

Thirteen run files contain market-beating language. **Twelve are self-audit checkboxes DENYING the
claim** (*"[x] Never presented as proven to beat the market; nothing here claims it"*). **The
thirteenth is GM**, and the sentence is GM's own five-year stock performance graph: *"GM beat the
index over five years"* - a fact about General Motors, not a claim about the framework. **Zero
violations.** Worth recording that only 12 of 132 runs carry the denial explicitly; rule 7 says
*"when asked"*, and no run was asked, so this is coverage, not a gap.

## RULE 9: THE SELF-AUDIT IS UNIVERSAL, THE NAMED ANTIDOTES ARE NOT

**132 of 132 run files carry a self-audit**, which is rule 6 and rule 9's operative half. But the
three antidotes rule 9 names by id are cited very unevenly: **[E4-26]** (hunt disconfirming
evidence) in **86** of 132, **[E4-27]** (the incentives read the analyst) in **66**, and
**[E3-41]** (*"you must not fool yourself, and you're the easiest person to fool"*) in **6**. Four
runs cite all three; **fifteen cite none of the three** (ANF, BA, BMI, CMG, CRWD, EFX, GFF, GRMN,
PEP, PINS, PLTR, ROKU, TSCO, WMT, WTM). This is not a violation - rule 9 prescribes a practice, not
a citation, and all fifteen carry a self-audit and a "what this run got wrong" section. It is
recorded because **[E3-41] is quoted in the operator protocol itself and is almost absent from the
work the protocol governs.**

## THE CYCLE'S REAL FINDING: A LEDGER ID IS NOT A UNIQUE KEY TO A PASSAGE

The 06:32 cycle matched each of the 267 rows against its own source document. **It never asked
whether two rows carry the same passage.** They do, five times. Zero rows are exact duplicates, so
nothing flagged; but on a letters-and-digits normalisation, **five shorter quotes sit wholly inside
a longer quote from the same source file and the same year:**

| the longer row | contains | live use in the 132 runs |
|---|---|---|
| **[E2-08]** owner earnings, "the complete definition INCLUDING working capital", 1986 | **[E2-23]** owner earnings, full definition, 1986 | **E2-08 = 0**, E2-23 = 117 |
| **[E5-33]** serial restructuring belongs in owner earnings, 2016 | **[E5-10]** "normal earning power" is the operative quantity, 2016 | E5-33 = 58, **E5-10 = 0** |
| **[E5-08]** the two-condition buyback test, 2011 | **[E5-01]** the two buyback conditions, 2011 | E5-08 = 109, **E5-01 = 0** |
| **[E5-08]** the two-condition buyback test, 2011 | **[E5-24]** the first law of capital allocation, 2011 | E5-08 = 109, E5-24 = 49 |
| **[E4-11]** THE WINDAGE RULE, 2004 meeting | **[E4-48]** realistic at every level, one margin at the end, 2004 meeting | E4-11 = 46, E4-48 = 16 |

**The corpus resolved this two different ways on its own, and both are defensible.**

- **Three pairs resolved by abandonment.** E2-08, E5-10 and E5-01 are cited in **zero** of the 132
  runs of record. Each lost to its twin and the runs converged on one id per passage without anyone
  ruling on it.
- **Two pairs are used together on purpose, and correctly.** E5-08 and E5-24 appear together in 45
  runs; E4-11 and E4-48 in 10. Read in place, they carry **different propositions drawn from one
  continuous passage**. JPM is the clean example: **[E4-11]** names *which bar* the windage rule
  offers (*"WHICH BAR ARE YOU USING? never both on the same number"*) and **[E4-48]** names the
  discipline that bar enforces (*"realistic inputs, errors on the conservative side, conservatism
  spent once"*). **A long quote legitimately supports two rules.**

**Why it matters to rule 8, which is the rule under test.** Rule 8 makes a ledger id the thing that
separates a judgment from an opinion. **If one passage has two ids, an id is not a key to evidence -
it is a key to a row**, and a run can satisfy rule 8 with an id no other run uses for that passage,
against a reader who would look the passage up under the other one. **Nothing catches this**:
`check_framework.py` tests that an id resolves to a row, which all ten do; the 02:32 phantom sweep
tests the same thing; the 06:32 sweep tests the row against its source, which all ten pass.

**Two live consequences, both recorded and neither acted on.**
1. **The framework's ONE NUMBER is the sharpest case.** CLAUDE.md: *"Owner earnings is the one
   number."* Its defining 1986 passage carries two ids. The runs of record use **E2-23** 117 times
   and **E2-08 never** - but **E2-08 is still the id cited by `Curriculum/CHARTER.md` and
   `Framework/CHANGELOG.md`.** A reader coming from the charter looks up the id the work abandoned.
   `[coursework path withheld]` has the same problem with **E5-01**.
2. **The row count in CLAUDE.md is right and the passage count is smaller.** 267 rows, **262
   distinct passages**. The KEY FILES line says *"267 verbatim rows"*, which is accurate as
   written - it says rows, not passages. **Not edited.** The 2026-09-19 correction to that same
   line (117 -> 267) is the precedent for counting the file rather than the pointer, and this cycle
   counted the file.

**`python tools/check_framework.py` PASSES: 0 phantom citations, 0 unlabelled numbers.** Nothing
above is a broken build.

## WHAT THE 267 ROWS ACTUALLY CARRY, COUNTED FOR THE FIRST TIME

**183 of 267 rows are cited by at least one of the 132 runs. 84 are not.** The 84 are not a random
tail and they are not rot:

| the 84 uncited rows, by the vocabulary of their `supports_gate_or_sheet` cell | count |
|---|---|
| **v3's superseded EIGHT-GATE vocabulary only** ("Gate 6", "Gate 7", "Workbook Sheet 5", "OM-15") | **65** |
| v4's own Q-vocabulary | 14 |
| neither (prose only) | 5 |

Against **154 of the 183 CITED rows speaking v4's Q-vocabulary**. The uncited set is overwhelmingly
**the residue of the eight-gate framework the v3.x archive holds**, which CLAUDE.md already puts out
of force. Of the 19 uncited rows that do speak v4's vocabulary, **13 support Q5 ranking, Q6 exit or
position sizing** - E2-32 and E2-65 (the gin-rummy prohibition), E2-46 and E3-64 and E3-67 (the
switching penalty, the tax-deferral edge, the croupiers' take), E3-63 (sizing), E4-53 (the analyst's
own allocation). **These are the gates that only bind a name the corpus BUYS, and the corpus has
bought nothing: no run in 132 has cleared Q5.** The uncited tail is a direct measurement of that.

**Cross-checked against the governing documents so the word "uncited" is honest:** of the 84,
**16 are cited by `THE FRAMEWORK v4.md` (12), `THE HOLDINGS FRAMEWORK.md` (9) or
`_TEMPLATE - Holding Review.md` (2)** and are alive at framework level even though no purchase run
has needed them. **68 of 267 are cited by no run and no governing or template document.** Era 1 (the
partnership letters, concentration and position sizing) supplies 12 of those 68.

## MY OWN DEFECTS - THE TENTH CONSECUTIVE CYCLE IN WHICH THE READER WAS WRONG

1. **One of 132 register entries would not resolve to a run file: BRK-B.** The register writes the
   ticker **BRK-B**; the file on disk is `2026-09-02 Run - BRK Berkshire Hathaway.md`. My matcher
   required `Run - <TICKER>` and the B-share suffix is in the register, not the filename. **The
   04:32 filename rule arriving a second time**: the register's ticker and the file's ticker are
   different strings and neither is authoritative for the other.
2. **The rule 7 grep returned 13 files and the honest count is zero.** Twelve of the thirteen are
   self-audit lines whose sentence is a DENIAL of the very phrase matched, and the thirteenth is a
   sentence about GM's share price. **A token-level reader scores rule 7 at 13 violations against a
   corpus that violates it nowhere.** This is the 08:32 lesson - *a checkbox is not a verdict, read
   the sentence it sits in* - arriving a third time, now on a grep rather than a checkbox.
3. **"84 rows are uncited" was very nearly written as a defect.** It is a defect only if the rows
   should be in use. Testing it against the governing documents moved 16 of the 84 out of the set,
   and classifying the rest by vocabulary showed 65 belong to a framework that is not in force.
   **The disconfirming test was run because [E4-26] says to run it hardest on your own best
   finding**, which is rule 9 read against the rule-9 audit.

**Durable instruction, added beside the whitespace rule (03:32), the filename rule (04:32), the
token-class rule (05:32), the two-documents rule (06:32), the authorization rule (07:32) and the
checkbox rule (08:32): AN ID IS NOT A PASSAGE. Before calling a ledger row unused or a citation
unique, check whether another row carries the same words.** The ledger's own uniqueness is on the
id column, and nothing enforces uniqueness on the quote.

## ADDED TO OPERATOR DECISIONS STILL OPEN

20. **Five passages are entered in `principle_ledger.csv` under two ids each** (E2-08/E2-23,
    E5-33/E5-10, E5-08/E5-01, E5-08/E5-24, E4-11/E4-48). **Three of the ten ids are cited in zero
    of the 132 runs.** Two of the pairs are used together on purpose and should probably stay.
    **Should the abandoned ids (E2-08, E5-10, E5-01) be retired, or should the pairs be
    cross-referenced in the ledger so a reader arriving at either finds the other?** Either is a
    change to the evidence base, which PRIME RULE 6 and PRIME RULE 5 put above a session's pay
    grade. **Not touched.**
21. **Two charters cite ids the work abandoned**: `Curriculum/CHARTER.md` cites **E2-08** for owner
    earnings, where the 132 runs cite **E2-23** 117 times; `[coursework path withheld]` cites
    **E5-01**, where the runs cite **E5-08** 109 times. Both citations resolve to real rows with
    the right words, so `check_framework.py` passes and nothing is false. **Repointing them is an
    edit to documents outside this queue. Not touched, now named.**

**Nothing above this addendum was edited. No run started.** The three CSV lists, the TJX re-run, the
eight unruled shapes, the duplicate shape number 25 and the four missing entry pointers (CB, ACNB,
SOFI, BLK) are all untouched, per the standing instruction not to start them unattended.

---

# ADDENDUM 2026-09-20 10:32 EDT - PRIME RULES 5 AND 6, THE LAST TWO NEVER AUDITED. BOTH HOLD IN SUBSTANCE. BUT THE FRAMEWORK'S CONFESSED-CONVENTIONS HEADER BREAKS THE ABSENCE-CLAIM RULE PRINTED FOURTEEN LINES BELOW IT, AND `Framework/README.md` STILL ROUTES A READER TO v3.0

**Branch C. No name to run, no file to resume.** State read before anything was touched:
register **132 entries, 132 distinct tickers, zero duplicates** (counted from
`## COMPLETED FROM THE QUEUE` on the `- **TICKER (` entry pattern, not carried forward);
all fifteen WAVE 6 names registered and struck; `find "Test Runs" -mmin -60` returned
**nothing**, so no session is mid-write; the lock reads `10076 2026-09-20T10:31:56`, this
cycle's own. **Thirteenth consecutive confirmation.**

`python tools/check_framework.py` run first: **PASS.** 267 rows, 267 unique ids, 267/267
source files on disk; 0 phantom citations and 0 unlabelled numbers across all five checked
documents; 184 ids cited by `THE FRAMEWORK v4.md`.

## WHAT HAD NEVER BEEN TESTED

Twelve cycles have swept the OPERATOR PROTOCOL end to end (rules 1-9, all of them) and
PRIME RULES 3 and 4. **PRIME RULES 5 and 6 are the last two, and neither had ever been
looked at:**

- **PRIME RULE 5** - *"ASK BEFORE STRUCTURAL CHANGE. Adding, merging or deleting a question
  requires a written case with quotes, presented for approval first."*
- **PRIME RULE 6** - *"NOTHING IS WRITTEN UNTIL ITS EVIDENCE EXISTS. A rule enters the
  framework only after its ledger row does."*

**Neither is machine-checkable by the existing tool, and this is the gap that matters:**
`check_framework.py` verifies that every id a document **cites** resolves to a real row, and
that every number carries a label. **It has no way to ask whether a rule carries a citation
at all.** A rule stated with no id and no number is invisible to the acceptance test. That
is precisely the surface PRIME RULE 6 governs, and it has been unmeasured since v4 was
written.

## PRIME RULE 5 HOLDS - THE CASE EXISTS, THE CHANGE RECORD DOES NOT

The largest structural change this project ever made is **eight gates (v3.1) to six
questions (v4.0)**, on 2026-08-26. PRIME RULE 5 asks for a written case with quotes.

**It exists, and it is substantial.** `Framework/2026-08-26 AUDIT - What Actually Works, and
What To Cut.md` opens by naming its commission in the operator's own words - *"the framework
has done very well so far, run an audit and find what has worked so well about it. I want to
be able to simplify it"* - carries ten block quotes plus inline quotation, and states its own
verification contract: *"Every finding below carries a file and line reference so it can be
checked directly."* Its PART 0 corrects the premise of its own commission before answering it,
withdrawing the market-beating claim. `Framework/INVENTIONS - deleted and why.md` then records
all **43** deletions individually, classified **9 CORPUS-SOURCED / 14 DERIVED / 43 INVENTED**
against the ledger, and preserves what each deletion cost. **That is the written case PRIME
RULE 5 asks for, and it is better than the rule requires.**

**But `Framework/CHANGELOG.md` never recorded the change.** The file contains **zero**
occurrences of "v4" or "2026-08". It ends at v3.0, and its point 5 reads:

> "5. All 8 gates preserved — no renames, merges, additions, or deletions."

Its own contract, three lines from the top, is *"Every delta from the May edition... **No
silent edits.**"* **The eight-to-six rebuild is the one delta it does not carry.** The
substance is not missing - the audit and the INVENTIONS register hold it - but the document
whose single job is the change record stops one edition short, and tells a reader the eight
gates are intact.

## `Framework/README.md` IS THE FRAMEWORK FOLDER'S FRONT DOOR AND IT IS AN EDITION OUT OF DATE

Found while chasing the changelog. It is undated, present-tense, and wrong in five ways at
once:

| README.md says | Actually |
|---|---|
| **"Current edition: v3.0 (July 2026)."** | v4.1 has governed since 2026-08-26 |
| routes to three **v3.0 PDFs** by bare filename | all three are in `ARCHIVE - v3.x (superseded 2026-08-26)/`, which CLAUDE.md puts **out of force** |
| `principle_ledger.csv` (**76** verbatim quotes) | **267** |
| "all **8 gates** with corpus citations", "**47** principles", "Sheet 7-B", "Scream Test" | v3's vocabulary; the 09:32 sweep measured 65 ledger rows still speaking it |
| `scripts_v3/` — regenerate any PDF | also inside the archive folder, not at the path implied |

**The 76 is the same defect CLAUDE.md fixed on itself eleven days ago** - *"count corrected
2026-09-19: the line had said 117, and the USAR run caught it; **count the file, never the
pointer**"*. The correction was applied where it was caught and **nowhere else**. So I swept
every non-run markdown file for a claimed ledger size:

| file | claims | actual | verdict |
|---|---|---|---|
| `CLAUDE.md` | **267** | 267 | correct, fixed 2026-09-19 |
| `Framework/README.md` | **76** | 267 | **stale by 191** |
| `Framework/PLAIN ENGLISH...md` | **261** | 267 | stale by 6; dated 2026-08-28, present tense |
| `Framework/v4/TEST D - FINDINGS REGISTER.md` | 261, and nine incremental counts | — | **correct: dated history** ("Final state: ledger 261 rows"). Not a defect, and must not be edited - operator rule 6 |

One detail worth keeping: PLAIN ENGLISH says *"The framework cites **184** of them"*, and
`check_framework.py` reports **184** today. **The ledger grew by six rows since 2026-08-28
and the framework cites none of them** - which is the 09:32 cycle's 84-uncited-rows finding
arriving from the other direction.

## PRIME RULE 6: THE TEST, AND WHY ITS FIRST ANSWER WAS WRONG

I split `THE FRAMEWORK v4.md` into its 235 blocks and flagged every block that states a rule
(`must`, `never`, `require`, `forbidden`, `do not`, `may not`) while carrying **no ledger id
and no CONVENTION label**. **Fourteen blocks.**

**Then I ran the disconfirming test [E4-26] demands, and it killed most of the finding.**
Every one of the fourteen has at least one ledger id within ten lines. Reading each window,
**nine are a lead-in to the quote that evidences them** and are not violations at all:

- line 148 *"The competitor row is required."* is immediately followed by **[E3-28]** saying
  exactly that;
- line 867 *"Never as a forecast"* is immediately preceded by **[E3-32]**, *"I do not have to
  have a view on interest rates"*;
- line 52 *"A conclusion that required fighting for it is worth less"* sits directly under
  **[E4-18]**'s *"no degree of difficulty factor"*.

**This is the 08:32 checkbox lesson and the 09:32 grep lesson arriving a third time: the unit
of evidence is not the block.** A token-level reader scores PRIME RULE 6 at fourteen
violations against a document that mostly complies.

## WHAT SURVIVED: THREE RULES THAT ARE OURS AND SAY SO NOWHERE

Section VI of `THE FRAMEWORK v4.md` is headed **"THE CONFESSED CONVENTIONS"** and its second
line is:

> "Everything invented that survives, in one place. **Nothing else in this document is
> ours.**"

Seven rows are in that table. **Three rules are not in it, carry no ledger id, and are not
labelled CONVENTION anywhere in the document** (the document has exactly four inline
CONVENTION labels, at lines 33, 76, 654 and the section VI heading):

1. **Line 44 - "A thin-evidence gate is never IN."** The nearest cites are [E4-46]
   (UNRESEARCHED is for documents) and [E4-18] (no degree-of-difficulty factor); **neither
   says a thin gate cannot be IN.** The rule supplies its own warrant in its next sentence -
   *"This rule exists because runs that did otherwise put unverified names into a real
   portfolio"* - and that warrant is **operational history, not the corpus**. PRIME RULE 3
   requires such a rule be *"labelled **CONVENTION** with a one-line rationale, or it is
   deleted."* **It has the rationale and not the label.** This is the exact mirror of the
   07:32 finding, which was a label used to license what a rule forbids.
2. **Line 489 - "The flag binds position size, never the discount rate."** Load-bearing: it
   decides whether a Q3 capital-allocation flag is allowed to move a Q5 number. The two cites
   in its window, **[E4-13]** and **[E5-08]**, are about CEO optimism and say nothing about
   either mechanism. The *"never the discount rate"* half does have corpus support at
   **[E3-42]** (*"not try to have the whole panoply with all different kinds of risk rates"*)
   and **[E4-21]** (*"We don't formally have discount rates"*) - **neither is cited here.**
   The *"binds position size"* half is ours, and section VI's own position-sizing row says
   something different: sizing is *"left as a stated judgment"*, not something a Q3 flag binds.
3. **Line 1134 - "Keep them separate; never apply both to the same number."** *Conservatism
   spent once* is **[E4-11]**, cited nine lines below. **The rule that Bar 1 and Bar 2 may
   never touch the same number is the framework's own reconciliation of two passages**, and
   the corpus does not state it.

A fourth, different in kind: **line 70**, the read-the-filing rule (XBRL is screening; record
the accession number; cross-check one figure), is **OPERATOR PROTOCOL rule 4 restated inside
the governing document**. The operator is a legitimate authority and this is not a defect -
but it is a third thing the document contains that is neither corpus nor confessed
convention, and the header admits only two.

## THE CYCLE'S REAL FINDING: THE ABSENCE-CLAIM RULE IS BROKEN BY THE SENTENCE FOURTEEN LINES ABOVE IT

Section VI closes with **THE ABSENCE-CLAIM RULE**, added 2026-08-28 from Test D's verdict,
and it is the strictest rule in the document:

> "this document may assert that the corpus lacks something only if a recorded sweep looked
> for it, the assertion names that sweep, and the assertion is worded as **'no instance
> found,' never 'does not exist.'**"

**"Nothing else in this document is ours" is an absence claim of exactly that class.** It
asserts that no unconfessed invention exists in 1,278 lines. **It names no sweep, and it is
worded absolutely.** Test D's own diagnosis of why negative claims are dangerous applies to
it word for word: they *"cite nothing and... `tools/check_framework.py` therefore cannot
test"* them.

**This sweep is the first that has ever looked, and it found three.** Under the rule's own
wording the sentence should read: *"no further instance found - sweep of 2026-09-20 recorded
in WATCHLIST COMPLETE.md."* **Not edited.** Rewriting a governing document's confession is
above a session's pay grade under PRIME RULES 5 and 6, and the 07:32 lesson was that
confession is not authorization.

## MY OWN DEFECTS - THE ELEVENTH CONSECUTIVE CYCLE IN WHICH THE READER WAS WRONG

1. **The block test scored PRIME RULE 6 at fourteen violations and the honest count is
   three.** Nine of the fourteen are lead-ins to the quote that evidences them. I would have
   written all fourteen up had [E4-26] not been run against my own best finding. **Three
   consecutive cycles have now produced the same shape of error** - checkbox (08:32), grep
   (09:32), block (10:32) - and it is one error: **a match is not a reading.**
2. **I nearly logged the TEST D register's "261 rows" as a stale pointer.** It is dated
   history and says so - *"Final state: ledger 261 rows"* - and editing it would violate
   operator rule 6. **The test for a stale count is not whether it differs from today; it is
   whether the sentence is present-tense.** That separated README (defect) and TEST D
   (correct) from each other, and left PLAIN ENGLISH honestly in between.
3. **I went looking for a PRIME RULE 5 violation and found the rule over-satisfied.** The
   audit and the INVENTIONS register exceed what the rule asks. The defect was one document
   away, in the changelog nobody thought to open, and I only opened it because I was trying
   to prove the rule had been broken.

**Durable instruction, added beside the whitespace rule (03:32), the filename rule (04:32),
the token-class rule (05:32), the two-documents rule (06:32), the authorization rule (07:32),
the checkbox rule (08:32) and the id rule (09:32): A STALE POINTER HIDES IN THE DOCUMENT
NOBODY OPENS. When a count is corrected in one file, grep every other file for the same
count - and before calling any of them stale, check the tense: a dated record of what was
true is not a wrong claim about what is true.**

## ADDED TO OPERATOR DECISIONS STILL OPEN

22. **`Framework/README.md` announces "Current edition: v3.0 (July 2026)" and routes to three
    archived PDFs, a ledger count of 76 against an actual 267, 8 gates and 47 principles.**
    It is the Framework folder's front door and every pointer in it is superseded. **This is
    the most direct breach of THE STANDARD ("another analyst must be able to verify any rule
    against its cited source in under two minutes") in the repository: an analyst who starts
    here is sent to the out-of-force edition.** Rewriting it is a documentation decision, not
    a session's. **Not touched, now named.**
23. **`Framework/CHANGELOG.md` has no v4 entry at all** and still asserts "All 8 gates
    preserved," against its own promise of "No silent edits." The substance lives in the
    2026-08-26 audit and `INVENTIONS - deleted and why.md`. **Should the changelog be
    extended to v4, or formally closed at v3.0 with a pointer to those two documents?**
24. **Three rules in `THE FRAMEWORK v4.md` are the framework's own and are neither cited nor
    confessed** - line 44 (a thin-evidence gate is never IN), line 489 (the flag binds
    position size, never the discount rate), line 1134 (never apply both bars to the same
    number). **PRIME RULE 3 gives two options, a CONVENTION label or deletion, and all three
    should probably take the label** - line 489 could additionally cite [E3-42] and [E4-21]
    for its "never the discount rate" half. **Not touched: adding to section VI is a change
    to the governing document.**
25. **Section VI's "Nothing else in this document is ours" violates the ABSENCE-CLAIM RULE
    printed fourteen lines below it.** Under that rule's own wording it should name this
    sweep and read "no further instance found." **Not touched, for the same reason.**
26. **`Framework/PLAIN ENGLISH...md` says the ledger holds 261 quotes; it holds 267.** Off by
    six, present tense, in a document dated 2026-08-28. Minor, and the "cites 184 of them" in
    the same sentence is still exactly right.

**Nothing above this addendum was edited. No run started.** The three CSV lists, the TJX
re-run, the eight unruled shapes, the duplicate shape number 25 and the four missing entry
pointers (CB, ACNB, SOFI, BLK) are all untouched, per the standing instruction not to start
them unattended.

---

# ADDENDUM 2026-09-20 10:42 EDT - THE 07:32 SWEEP'S TWO FINDINGS, FIXED ON OPERATOR AUTHORITY

**Operator said "Fix" to decisions 15 and 16.** Both are now closed. Decision 17 is untouched.
Nothing above this block was edited, no run was started, and no run file was altered.

## FIX 1 - THE NET-INCOME PROXY SEVEN, CORRECTED BY ADDENDUM AND NOT BY EDIT

New file: `Test Runs/ADDENDUM 2026-09-20 - the net-income proxy seven, and why a CONVENTION
label cannot license operator rule 5.md`. **Operator rule 6 governs: not one character of the
seven run files was changed.**

**The seven, identified independently and then read one by one.** All seven 2026-07-15 files
carrying a `FRAMEWORK CONVENTION` label were found by grep (exactly seven of the 92 run files
of that date), and each label was read in place: **MTSUY** (the origin, plus a second
same-file convention taking g1 = 2% *"same spirit as the NI-as-OE-proxy convention"*),
**ITOCY**, **MARUY**, **MITSY**, **SSUMY** (all four *"as documented in the MTSUY run"*),
**NPNYY** and **FUJIY**. **Eight uses, seven files, one day.** Every label is quoted verbatim
in the addendum with the sentence it licenses.

**The general rule is carried by the corpus, not argued from the framework.** Per the
operator's instruction that the corpus is the law: **[E2-08]** makes reported earnings the (a)
input and requires the working-capital increment inside (c); **[E2-09]** chooses *"the owner
earnings figure, not the GAAP figure"* by name and says *"(c) must be a guess"*, so a missing
capex figure obliges a disclosed guess rather than an omission; **[E3-44]** and **[E2-41]**
supply the default guess, which is why *"not obtainable this pass"* never licensed anything;
**[E2-60]** names reported earnings as capable of being *"ersatz"*; **[E3-04]** supplies the
look-through construction for the equity-method income MTSUY gave as its reason; and
**[E4-25]** rules on what an unpinnable input licenses: *"Usually, the range must be so wide
that no useful conclusion can be reached."* **Abstention, not a substitute number.**

**The rule, one sentence: a CONVENTION label may confess an invention, and may never license
conduct a rule forbids.** Not lifted into PRIME RULE 3 - PRIME RULE 5 puts that with the
operator, so **decision 15 stays open** with the wording now sourced and ready.

**Register check, run not assumed: none of the seven is among the 132 entries** under
`## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md` (132 entries, 132 distinct
tickers). **But the 07:32 addendum's "no counted verdict rests on them" stopped one step
short, and the new addendum says so:** the MITSY file records `**Bought 8 shares at $586 =
$4,688, Roth IRA.**` on 2026-07-16 and itself notes the position *"rests on the NI-proxy OE
convention"*. Real money moved on the forbidden number. MITSY is the only one of the seven
already withdrawn (2026-08-26, Ruling 12) and re-run (`2026-08-28 Run - MITSY (Mitsui)
v4.1.md`, owner earnings look-through **[E2-23, E3-04]**, Q2 OUT, adds barred), so the held
position no longer rests on it.

**What the verdicts are worth, name by name, in the addendum's table.** The proxy is the
numerator of every Gate 6 yield and the base of every Gate 8 asymmetry in these files, so
**six of the seven still carry an unwithdrawn verdict computed from a number operator rule 5
forbids**: MTSUY (STATUTE-ONLY), ITOCY, MARUY, SSUMY (all BUY-ELIGIBLE / ENTER ELIGIBLE),
NPNYY (STATUTE-ONLY at most) and FUJIY (STATUTE-ONLY). **All six are void as valuations and
real as qualitative research.** Two further defects recorded: the four DCF files used a
**+2.5% NARROW spread** where Ruling 4-A (2026-08-01) sets **+4.5%**, so every IV is 200bp
under-discounted independently of the proxy; and NPNYY and FUJIY carry *"PASS (provisional)"*
gates, which under v4 were never passes at all.

**How v4 closed the hole from the other side, recorded from the v4 text:** section VI's
confessed convention is the opposite construction (*"operating cash flow less SBC, less the
(c) guess"*), so a net-income proxy is not reachable from the build; Q4 states *"D&A is the
default guess for (c)"*, which retires the stated reason; Q4 names the equity-method case and
requires the **[E3-04]** look-through increment; UNRESEARCHED now closes a file rather than
licensing a workaround; the *"unverified / general knowledge / provisional"* rule disqualifies
the label these files wore; and the ABSENCE-CLAIM RULE would now reject MTSUY's unswept *"not
attributable to Buffett/Munger"*, which was false on five ledger rows.

## FIX 2 - PRIME RULE 4 NOW NAMES THE EIGHTH SOURCE CLASS

**`CLAUDE.md` amended.** This is a rule made to match its own practice, which the operator
authorised; it is not an edit to history.

**Before:** *"Partnership letters, Berkshire letters, Wesco letters, meeting transcripts, Poor
Charlie's Almanack, An Owner's Manual, Buffett's Fortune essays."*

**After:** the same list, plus *"the `Special Letters`, the 2014 fiftieth-anniversary pair
published inside that year's Berkshire annual report"*, with a dated parenthetical recording
the 07:32 sweep, the eight-folders-versus-seven-classes finding, and that **[E5-19]** is from
this class and operator rule 7 cites it. **The Graham amendment of 2026-07-13 was not
touched, and nothing else in the rule changed.**

**The folder's real name on disk is `Special Letters`**, checked, holding
`2014 Warren Buffett - Past Present Future.txt` and `2014 Charlie Munger - Past Present
Future.txt`. **The dependency was verified by counting the ledger, not by trusting the
finding:** 267 rows draw on exactly **eight** folders, `Special Letters` supplying **8** rows
(E5-04, E5-11, E5-12, E5-15, E5-19, E5-21, E5-44, E5-45). **The row that proves the dependency
is [E5-19]**, the Munger essay's *"the man, the system, luck and devotion"* accounting, quoted
by operator rule 7 in the honesty record every session must state. **[E5-11]**, Q4's three
strengths of financial staying power, is from the same folder.

## MY OWN DEFECT

**I had MTSUY's label at lines 71 to 83 and its second convention at line 145.** Both off by
one, from a `sed` range read whose first printed line was the blank above the heading. Caught
by re-reading with line numbers printed before the addendum was committed. The label is lines
**72 to 82**, the heading line **71**, the g1 convention line **146**, the self-audit
checkbox line **171**.

## THE ACCEPTANCE TEST

**`python tools/check_framework.py` PASSES with both fixes in place**, and the record of when
matters, so it is written down rather than smoothed. It failed twice while I worked, both times
inside another agent's concurrent repair of `principle_ledger.csv` and `tools/check_framework.py`
(first 7 rows of the wrong column width, then that agent's new verbatim check reporting 5 rows
not matching their cited source). **Neither failure was mine and neither was worked around:**
this session read those two files and `THE FRAMEWORK v4.md` and wrote to none of them. The
commit message of `3752650` records the second failure as still open, because it was when the
commit was made; **the repair landed minutes later and the test now passes.** That commit
message is left as written, per operator rule 6.

## STILL OPEN

**Decision 15** stays open as an amendment to PRIME RULE 3, with the one-sentence rule now
written and sourced to **[E2-09]** and **[E4-25]**. **Decision 16 is closed.** **Decision 17**
(whether a declared dual-framework run may draw on the companion Graham build) was not mine and
was closed separately the same day in commit `6612129`.
**Six names now carry a recorded void verdict and no replacement**, which is a queue item and
not a repair: reopening any of them needs the annual securities report read, owner earnings
rebuilt on operating cash flow less SBC less the (c) guess with the look-through increment, a
current JPY 30-yr from the MOF, the Q2 competitor row, and the current NARROW spread. **Under
operator rule 5 that is a new run under v4, not a fix to these files.**

---

# ADDENDUM 2026-09-20 - THE SIX ROWS REPAIRED ON THE OPERATOR'S INSTRUCTION. FIVE CELLS RE-CUT FROM THE SOURCE, ONE LEFT ALONE BECAUSE THE SHELF IS THE DAMAGED DOCUMENT, FIVE DUPLICATE PASSAGES CROSS-REFERENCED, AND THE VERBATIM CHECK ADOPTED AS CHECK 4

**Authorised session, not an overnight cycle.** The operator read the 06:32 addendum (decisions
12, 13, 14) and the 09:32 addendum (decisions 20, 21) and said **"Fix"**, with the standing
instruction *"The corpus is the law. All answers are in the corpus"* and its consequence: **where
the ledger and the source disagree the source wins, and where the framework and the source
disagree the source wins there too**, which is PRIME RULE 2 in its own words. Every row below was
re-read in its own file on disk before a character was changed. **No verdict moved and no run file
was touched.** `python tools/check_framework.py` **PASSES** with the new check wired in.

## THE FIVE ROWS REPAIRED, EACH AGAINST ITS OWN SOURCE

### E4-19 - `Annual Meetings/2006 Annual Meeting.txt`, cited 167 times across 144 files

**What the row said.** *"There's just - there's just games that are too tough. Charlie says, you
know, "We've got three boxes at the company: in, out, and too hard." And a lot of things end up in
the "too hard" pile, and it doesn't bother us. [...] What I've learned is I know enough not - to
know that I don't know enough to make an investment decision."*

**What the transcript says.** Two things the row did not. At **line 213**: *"WARREN BUFFETT: I know
— what I've learned is I know enough not — to know that I don't know enough to make an investment
decision."* At **line 215**: *"There's just — there's just games that are too tough. Charlie says,
you know, "We've got three boxes at the company: in, out, and too hard." **(Laughter)** And a lot of
things end up in the "too hard" pile, and it doesn't bother us."*

**What it says now.** The know-enough clause first, then `[...]`, then the three-boxes passage, with
**`(Laughter)` restored** and the front of the first fragment restored to the transcript's own
*"I know - what I've learned is"*. The locator moved from `(line 215)` to `(lines 213-215)`.

**A CORRECTION TO THE 06:32 FINDING, and it matters.** That addendum called the know-enough clause
*"Buffett answering an **earlier question** about IBM, Sun, Oracle, Dell, EMC and Intel"* and gave
the offsets as 49,771 and 51,226. **Both fragments are in the SAME answer to the SAME question**:
section `### 12. Tech is still in the "too hard" pile` runs from offset 49,177 to 54,115, and the
two fragments stand at **49,900 and 51,333** inside it, two paragraphs apart. So the defect was
**order, not provenance**: `[...]` between them is an honest elision within one answer, which it
would not have been across two questions. The repair is therefore a re-ordering, not a split.

### E2-02 - `Shareholder Letters/1981 Letter.txt`. The one that misread its source

**What the row said.** The **retention** sentence first, then `[...]`, then *"paid out and return on
equity stays at 14% - the 7% tax-exempt equivalent ... is just as frozen as is the coupon on a
tax-exempt bond"* with the words *"if all earnings are"* cut off the front. Read as written, **the
frozen coupon attached to the retained case.**

**WHAT THE LETTER PLAINLY SAYS.** The paid-out case comes first and it is the frozen one: *"And, if
conditions persist - **if all earnings are paid out** and return on equity stays at 14% - the 7%
tax-exempt equivalent to the higher-bracket individual investor is just as frozen as is the coupon
on a tax-exempt bond. Such a perpetual 7% tax-exempt bond might be worth fifty cents on the dollar
as this is written."* Then, and only then: *"**If, on the other hand, all earnings** of our typical
American business **are retained** and return on equity again remains constant, **earnings will grow
at 14% per year.**"* The whole point of the passage is that the two cases differ: **retention grows
the coupon, payout freezes it.** The row had it exactly backwards.

**What it says now.** The paid-out fragment first with its front restored, then `[...]` (the
fifty-cents sentence is what sits between), then the retention sentence. Nothing else changed: the
concept cell, the year and the gate pointer were already right.

### E4-07 - `Shareholder Letters/1999 Letter.txt`

**What the row said.** *"...but **the direction of change** is in no way ordained."*
**What the letter says.** *"...but **the direction in which value is going to go** is in no way
ordained."*
**What it says now.** The letter's nine words, restored. No bracket and no ellipsis, because none is
needed: the whole quote is one continuous span of the letter.

### E1-09 - `Partnership Letters/1966-01-20 Partnership Letter.txt`

**What the row said.** *"...of achieving **[performance superior to the Dow]**."* The only row in
267 that inserted editorial text of its own.
**What the letter says.** *"...of achieving **performance surpassing the Dow by, say, fifteen
percentage points per annum.**"*
**What it says now.** The figure is back and the bracket is gone. The quote is a single unbroken
sentence of the letter, so the row now carries no elision at all.

### E5-07 - `Wesco Letters (Munger)/`, a folder, and not a quotation

**What the row said.** A cell opening `NOTE:` and counted among *"267 verbatim rows"*.
**What it is.** A deliberate negative finding from the Wesco survey, `supports_gate_or_sheet`
already reading *"n/a - negative finding recorded per Prime Rule 1"*, cited zero times.
**What it says now.** Its first words are **"NOT A QUOTATION - NEGATIVE FINDING, recorded per PRIME
RULE 1."** so that a reader and the acceptance test see the same thing in the same glance. Nothing
of the finding's own text was altered. `CLAUDE.md`'s KEY FILES line now reads **266 verbatim quotes
plus one negative finding**, carrying **262 distinct passages**.

## THE ROW I REFUSED TO TOUCH: E3-20

`Munger Talks (PCA)/Talk 02 - A Lesson on Elementary Worldly Wisdom (USC, 1994-04-14).txt` reads,
on disk: *"The model I like—to sort of simplify the notion of what goes on in a market for common
stocks—is the"*, then a paragraph break, then *"at the racetrack."* **Two words are missing where
the ledger reads "pari-mutuel system", and the ledger is the sound document.** The row is left
exactly as it stands, per the operator's instruction and per *"where you cannot verify from the
shelf, say so and stop rather than reasoning your way to a plausible text."*

**I could not establish the missing words from another file on the shelf, and I looked.** The only
other occurrences of *pari-mutuel* in the whole repository are Talk 02's own **next** sentence (*"If
you stop to think about it, a pari-mutuel system is a market"*) and a later sentence in Talk 09,
both of which are **inference, not the words**. **And Talk 09 carries the same hole**: *"as a
teenager I'd been to the racetrack in Omaha, where they had the"*, paragraph break, *"And it was
quite obvious to me that if the house take, the croupier's take, was 17 percent..."*. So **decision
13 covers two files, not one**, and the defect is the PCA extraction rather than any passage.
**It still needs the operator's own copy of the Almanack.** Until then E3-20 is the one row in the
ledger that can be inferred but not verified from disk, and the acceptance test now says so out
loud on every run rather than passing over it.

## THE FIVE DUPLICATE PASSAGES: CROSS-REFERENCED, NOTHING RETIRED

Decision 20 offered retirement or cross-reference. **Cross-reference, in the `evolution_notes`
column, which is the column the ledger already uses for provenance.** Nine rows now carry an
`ALIAS NOTE` naming the twin, which cut is longer, and how many of the 132 runs cite each. **Every
one of the ten ids still resolves**, because 183 rows are in live use and deleting an id would
break citations that are correct.

| passage | rows now marked | runs citing |
|---|---|---|
| owner earnings, 1986 | **E2-08** (longer) and **E2-23** | 0 and 117 |
| restructuring charges, 2016 | **E5-33** (longer) and **E5-10** | 58 and 0 |
| the 2011 buyback passage | **E5-08** (longest), **E5-01**, **E5-24** | 109, 0 and 49 |
| the 2004 windage answer | **E4-11** (longer) and **E4-48** | 46 and 16 |

**Two charters repointed** (decision 21): `Curriculum/CHARTER.md` from **[E2-08]** to **[E2-23]**,
and `[coursework path withheld]` from **[E5-01]** to **[E5-08]**. Both now cite the id the work
actually uses, and the alias notes mean a reader arriving at the abandoned id still finds the other.

## THE NEW CHECK: `tools/ledger_verbatim.py`, WIRED IN AS CHECK 4

Decision 14, adopted. The scratch script is gone; the permanent one is **`tools/ledger_verbatim.py`**,
runnable on its own for the row-by-row report and imported by `tools/check_framework.py`, whose
header now names four checks. **It opens each row's own cited file and looks for the row's own
words, in document order, on a letters-and-digits normalisation.** It concludes nothing, computes
nothing new, and deliberately does **not** hunt the shelf for a better home for a failed fragment:
that is diagnosis, and diagnosis belongs to the reader.

**Runtime: 1.07 seconds for the whole acceptance test**, against 1.11 before, which is measurement
noise. The check itself takes about a second including interpreter start.

**How it reports the damaged shelf file.** Two exceptions, both declared by a human, both printed on
every run, and neither able to rot:

- A cell whose first words are `NOT A QUOTATION` is not matched. **The declaration has to be written
  into the cell**, so it is the author's claim and a reader sees it where the tool does. One row:
  E5-07.
- A row listed in **`tools/shelf_damage.csv`** cites a file with a hole in it. One row: E3-20, whose
  entry names the missing span, the second instance in Talk 09, why the words cannot be recovered
  from the shelf, and decision 13. It reports as `SHELF_DAMAGE_DECLARED` and **does not fail the
  build**, because failing it would punish the ledger for a defect in the shelf and would block
  every unrelated commit until the Almanack arrives. **But a declared row that DOES verify fails**,
  so the exception dies the day its cause is repaired.

Output, every run: `verbatim against cited source: 265/267 OK`, then the two exceptions by name.

**Proved by negative test before it was trusted**, each perturbation restored: deleting `(Laughter)`
from E4-19 fails the build; reversing E2-02's fragments fails it and names which fragment broke the
order; and declaring a healthy row damaged fails as `STALE_DAMAGE_ENTRY`.

**Its honest limit.** It enforces *verbatim, in document order, elisions marked*. It cannot tell
that an elision mark is **hiding** a transcript artifact rather than omitting text: had E4-19 been
written with `[...]` where `(Laughter)` stands, the check would have passed it. That half of PRIME
RULE 1 is still the reader's.

## WHAT THIS DISTURBS

**No verdict.** Four of the five repaired rows are cited only in `Framework/CHANGELOG.md` or nowhere,
and E4-19 is cited by id in 143 files that quote no text; the one file that quotes it is the
framework, and it quotes the three-boxes clause, which is unchanged apart from the restored
`(Laughter)`. No run's reasoning rests on the order of E4-19's two fragments or on E2-02's
inversion, so nothing had to be stopped and reported.

**One governing document changed.** The epigraph of **I. THE FOUR VERDICTS** in
`Framework/THE FRAMEWORK v4.md` now carries `(Laughter)` exactly where the transcript has it. It is
the only edit to a governing document, and it makes the document match the corpus, not the reverse.

**Two history files still carry the smoothed wording and were deliberately left alone**, per
operator rule 6: `Framework/2026-08-26 THE FIVE PASSAGES - Synopsis and Rulings.md` (which prints
the two passages as two separate block quotes, more honestly than the ledger row did, but without
`(Laughter)`) and the superseded v3.1 template and archives. **They are history and not in force.**

## DEFECTS IN THE BRIEF I WAS GIVEN, AND IN THE FINDINGS IT RESTED ON

1. **"An earlier question" is wrong for E4-19** (06:32 addendum, repeated in the brief). One
   question, one answer, two paragraphs apart, offsets 49,900 and 51,333, not 49,771 and 51,226.
   The defect was order alone.
2. **"Mark the redundant ids as aliases" would have missed the id that actually needed it.** In two
   of the five pairs the row cited in **zero** runs is the **longer** one (E2-08, E5-33), so
   *redundant* and *abandoned* are different sets, and **E2-08, the id `Curriculum/CHARTER.md`
   cites, is the longer row.** Marking only the shorter twins would have left that charter pointing
   at an unmarked row. All nine rows were cross-referenced in both directions instead.
3. **"Ten ids" is nine rows.** E5-08 stands in two of the five pairs, so the ten citations name nine
   distinct rows. The count of **262 distinct passages** is unaffected: five containments collapse
   five rows.
4. **The brief asked me to write repairs into the ledger without saying the cells are CSV fields.**
   My first pass appended commas into unquoted `evolution_notes` cells and check 3 correctly failed
   with seven malformed rows. Redone through `csv.writer` at field level, so the 253 untouched rows
   are byte-identical and only 14 lines of the file changed.
5. **`CLAUDE.md` carried an uncommitted edit that is not mine**, adding `Special Letters` as an
   eighth citation-shelf class under PRIME RULE 4 (the 07:32 sweep's finding). It was in the working
   tree when I arrived. It is committed alongside my own KEY FILES and TOOLS lines because git
   commits whole files, and it is recorded here so the authorship is not lost.

## STILL OPEN AFTER THIS SESSION

- **Decision 13 remains open and is now larger**: `Munger Talks (PCA)/Talk 02` AND `Talk 09` both
  have extraction holes at the same phrase. Needs the operator's own Almanack. E3-20 stays as
  written until then.
- The three CSV lists, the TJX re-run, the eight unruled shapes, duplicate shape 25 and the four
  missing entry pointers (CB, ACNB, SOFI, BLK) were **not touched**, per the standing instruction
  not to start them unattended.

---

# 2026-09-20 -- NINETEEN LEDGER ROWS ADDED: THE [E4-04] EXCLUSION, AND BANKS

Rows only. **No rule, no framework document and no run file was touched.** PRIME RULE 6 puts the
evidence row before the rule, and these nineteen rows are evidence for **two rulings the operator
has not yet made**: what the fast-change exclusion [E4-04] actually excludes, and whether a bank
can clear Q2 at all. Nothing here decides either. Commit `b7e84ca`, one commit, pathspec
`principle_ledger.csv`.

**On the fast-change exclusion, ten rows.** E2-75 (1987 letter, acquisition criterion (5): 'simple
businesses (if there's lots of technology, we won't understand it)' -- and the phrase is in print
in ten consecutive letters, 1982-1991, and again in 2014); E3-72 and E3-73 (Talk 02, USC 1994,
the two passages that follow the surfing model already rowed at E3-51: Munger grounds the
exclusion in 'our personal inadequacies', then says it 'doesn't mean that it's irrational for you
to do it'); E3-74 (1995 meeting: 'smart once' vs 'stay smart', 'you cannot coast in retailing');
E3-75 (1991 letter: Xerox, Apple and Wal-Mart named as misses, 'We will never develop the
competence to spot such businesses early'); E4-57 and E4-58 (1999 letter: 'no insights into which
participants in the tech field possess a truly durable competitive advantage', and 'far beyond our
perimeter'); E5-51 (2010 meeting: Munger raises BYD himself as the breach of the rule, 'we have
always bragged about avoiding that', with Buffett's 'That's fair.' kept in place); E5-52 (2018
meeting: Apple underwritten on the ecosystem and 'the nature of consumer behavior', explicitly
'not because it was a tech stock in the least'); E5-53 (2023 meeting: TSMC sold on location with
the franchise verdict expressly intact -- 'nobody in the chip industry that's in their league').

**What the ten rows show without ruling on it:** the exclusion is stated in the corpus as a fact
about the analyst, not about the industry, and it was crossed twice in public with reasons given
both times. Whoever rules on [E4-04] now has the corpus's own counter-instances in front of them,
in the ledger, citable.

**On banks, nine rows.** E3-76 (1996 meeting, cut as ONE row with two marked elisions so the
numbers cannot be cited without the conditional that governs them: Bank of Granite at 2.58 percent
on assets and a 33 percent efficiency ratio on 400-500 million, 'There's no magic to it. You just
have to stay away from doing something foolish', and 'we like businesses like banking, **if** we've
got somebody in charge of them that is going to run them right'); E4-59 (2007: over 20 percent on
tangible equity 'dealing in what is basically a commodity -- money', and the objection left
standing, 'you still would think that would be self-neutralizing'); E4-60, E4-61, E4-62 (2002,
three rows from one answer: the two-sided test 'very little risk on the asset side and very cheap
money on the deposit side'; 'I would not characterize all banks as the same'; and Munger's
'Warren and I have failed to properly diagnose banking'); E5-54 (2011: the engine named --
cheap money, 'the implicit federal guarantee', and permitted leverage, all conditional on keeping
'out of trouble on the asset side'); E5-55 (2016: 'You can change the math of banking, and the
attractiveness of banking, totally, by capital requirements'); E5-56 (2012 letter: the Wells Fargo
'amortization of core deposits' charge, 'Yet core deposits regularly increase'); E4-63 (2008: the
buy decision needs 'the culture of the management and the institution, and that's hard to do for
99 percent of the banks').

**What the nine rows show without ruling on it:** the corpus supplies a positive bank
specification (two conditions, one per side of the balance sheet), a confessed error in the
underestimating direction, an owner-earnings add-back specific to the sector, a franchise that is
partly a regulator's decision and partly a public guarantee, and a stated base rate of one in a
hundred for how often the required knowledge is obtainable. That is a sector the corpus says it
got wrong, which is the one kind of sector no run may treat as settled by citation.

**Verification.** Every quote was cut from the file on disk, never from the brief; every row was
written through `csv.writer`, so all 267 pre-existing lines are byte-identical and the diff is 19
insertions. `python tools/check_framework.py` **PASSES**, with the verbatim count risen from
265/267 to **284/286** -- up by exactly the number of rows added, and the two non-verifying rows
are still only the two declared exceptions (E3-20 shelf damage, E5-07 declared not a quotation).

**Two citations in the brief were NOT added, because the ledger already carries the passage.** The
1999 Fortune sentence ('the durability of that advantage') is **E4-08**, added 2026-07-14; the 1982
letter administered-prices passage naming 'deposit costs for financial institutions' is **E2-59**,
lines 465-478. So the brief's claim that all of them are uncited is wrong in two places, and its
arithmetic is wrong as well: it lists nineteen numbered items, one of which is three rows, which is
twenty-one citations, not the 'nineteen across eighteen' it states. Nineteen rows were added. Every
line number the brief gave was correct, at every one of the nineteen.

---

# CLOSURE 2026-09-20 ~12:00 EDT - THE OPERATOR SAID "FIX". DISPOSITION OF EVERY DECISION ABOVE

*Interactive session, on the operator's instructions "Fix", "The corpus is the law. All answers are in the
corpus", and "Your job is to audit and fix." Every item below is committed; the hash is in the git log.*

| # | decision | disposition |
|---|---|---|
| 1 | TJX needs a fresh purchase run | **OPEN - a run, queued for the next phase** |
| 2 | eight (now ten) proposed survival shapes unruled | **OPERATOR** - a taxonomy choice, not a corpus question |
| 3 | shape-number collision (#25 twice) | **FIXED** - THE SLEEPING DEPOSITOR is #30; ACNB run carries a dated addendum |
| 4 | confirm BRK-A as the 151st line | **CONFIRMED** from the screenshots; covered by the BRK-B run, struck, no entry of its own |
| 5 | may a fold add a missing run-file pointer | **FIXED** as bookkeeping: pointers added under CB, ACNB, SOFI, BLK (see 19) |
| 6 | Q5 machine-readable outcome | **FIXED** with 18 |
| 7 | sweep Test Runs for phantom citations | **ADOPTED** - check 5 in `check_framework.py`: 1,046 files, 0.7 s, zero phantoms |
| 8 | deliverable rule in the acceptance test | **NOT ADOPTED** - passes 132/132 on prose; a token test would invert (the 03:32 finding) |
| 9 | the Ford sovereign rung | **RECORDED** - one run of 132 on the FRED fallback, immaterial, left as history |
| 10 | 125 unregistered run files, staleness marker | **FIXED** - `Test Runs/README - which run files are in force.md`: 141 in force, 158 superseded, generated from disk |
| 11 | `sources.py` knows three currencies, the queue needed five | **OPEN** - the foreign-filer tooling fix the operator queued on 2026-09-18 (items 11-13 of that list) |
| 12 | the six ledger rows | **FIXED** - E4-19, E2-02, E4-07, E1-09 re-cut from their sources; E5-07 relabelled NOT A QUOTATION; the v4 epigraph now carries `(Laughter)` |
| 13 | the hole in Talk 02 | **OPEN, and it is two files**: Talk 02 and Talk 09 both have holes; needs the operator's own Almanack |
| 14 | verbatim check in the acceptance test | **ADOPTED** - check 4, `tools/ledger_verbatim.py`, 284/286 with two declared exceptions |
| 15 | PRIME RULE 3 clause | **FIXED** - "may confess an invention; may never license conduct a rule forbids", sourced to [E2-09], [E3-44] |
| 16 | PRIME RULE 4's eighth class | **FIXED** - `Special Letters` named; [E5-19] is the dependency |
| 17 | HGRAF cites Security Analysis after the shelf amendment | **FIXED** by dated addendum in the run file |
| 18 | the Q5 box has no OUT | **FIXED** - the template box reads RANKED / NOT IN, QUIT ON below the floor [E4-28] / UNRESEARCHED / UNKNOWABLE |
| 19 | four register entries without run-file pointers | **FIXED** |
| 20 | five passages under two ids | **FIXED** - nine rows carry ALIAS NOTEs both ways; every id still resolves |
| 21 | two charters cite abandoned ids | **FIXED** - Curriculum E2-08 -> E2-23; MBA E5-01 -> E5-08 |
| 22 | README announces v3.0 | **FIXED** |
| 23 | CHANGELOG has no v4 entry | **FIXED** - frozen-at-v3.0 header |
| 24 | three uncited rules in v4 | **FIXED** - labelled CONVENTION; the discount-rate half cites [E3-42], [E4-21] |
| 25 | section VI's absence claim | **FIXED** - restated in the absence-claim rule's own form |
| 26 | PLAIN ENGLISH says 261 | **FIXED** |

**Also done, outside the numbered list:** the seven 2026-07-15 net-income-proxy runs carry one addendum
(`ADDENDUM 2026-09-20 - the net-income proxy seven ...`); the six of them in no current list are recorded
in the queue's SKIPPED section; the [E3-43] mis-sourcing in the CCB, SOFI and JPM runs is corrected by
addendum; nineteen corpus passages on [E4-04] and on banks are in the ledger (E2-75, E3-72..76, E4-57..63,
E5-51..56; 286 rows); and the two Q2 readings those passages decide are written as a PRIME RULE 5 case
in `Framework/v4/RULING CASE 2026-09-20 - two Q2 readings the corpus decides ...`, **for the operator's
approval. Only TSM's verdict of record would move under Case 1; nothing moves under Case 2.**

**Three defects of my own this session, recorded:** (1) I committed `CLAUDE.md` with a pathspec while the
ledger agent had uncommitted lines in it, and swept them into commit `f157417` - the crossing class the FOLD
rule names, from the other side; (2) my lock file carried a PID that was not alive, so three unattended cycles
walked through it (fixed in `_overnight.ps1`, honoured by freshness now); (3) four parallel agents each
spawning helpers exhausted the account limit at 10:45, which I should have foreseen.

**Update 2026-09-20 ~12:40, after the operator said the corpus answers all five:** Case 1 and Case 2 are APPLIED in `THE FRAMEWORK v4.md` Q2 (commit 2931a61); TSM re-read to Q2 UNKNOWABLE by addendum and register note; decision 13 is HALF FIXED - Talk 02 restored from two independent July captures that agree, Talk 09 has no copy on disk and stays as found; the ten proposed survival shapes are being put to the corpus; WAVE 7 (the three CSV lists) is opened, financials held out under the 2026-08-30 directive, and the hourly task is running it one name at a time.

## 2026-09-20, LATE: THE SURVIVAL-SHAPE PASSAGES ARE IN THE LEDGER (25 ROWS, 286 -> 311)

The read-only corpus search of this morning ruled on eighteen proposed survival shapes - the named
ways a business dies, asked at Q4 - and the passages grounding the kept shapes were not in the
ledger. PRIME RULE 6 wants the row before any rule or index cites one, so the rows go in first and
alone: **no rule, no index, no run file was touched, and no shape is written anywhere yet.** Commit
`0eaeadd`, pathspec `principle_ledger.csv`.

Every cell was cut from the file on disk by locating a phrase and slicing, never typed from this
brief or from memory, so the U+FFFD characters two shelf extractions leave where em dashes belong,
the smart quotes, the backtick before `earnings" in the 1998 letter and the transcript's "then you
do" all survive as found. **Line locators were computed from the match rather than copied**, which
is how five wrong ones in the ordering brief were caught.

| shape | ids | the passages |
|---|---|---|
| #23 reserves | **E4-64**, **E3-77** | 1999 letter: the reservoir of redundant reserves "has now largely dried up"; 1998 letter: the buyer boosting loss reserves at deal time so earnings flow into income later (E3-77 also grounds #24) |
| #17 price set by others | **E2-76**, **E2-77** | 1988 letter, cut in two at the paragraph boundary: Proposition 103 and the threat of the same in other states; then below-cost pricing ending in government provision, with the low-cost producer having the most economic goodwill to lose |
| #19 the channel takes the brand | **E4-65**, **E5-57** | 2001 meeting: "the retailer would like his name to be the brand", Munger on the muscle power of the Sam's Clubs and the Costcos; 2019 meeting: Kirkland at $39 billion against all of Kraft Heinz at $26 billion, and "we paid too much" |
| #21 the paper is the product | **E5-58**, **E5-59**, **E4-66** | 2014 letter: the accounting wizard as a selling point, "the clock struck twelve", share issuance as "one of the surest indicators"; 2014 meeting: continuous issuance names the species; 2001 meeting: a stock at 100 worth 10, and "you can run out of money before the promoter runs out of ideas" (E4-66 also grounds #24) |
| #25 the counterparty fails with you | **E4-67**, **E3-78** | 2001 letter: the daisy chain of retrocessionaires, the stress test of every participant, the tide going out; 1996 letter: never laying off risk because of "reservations about our ability to collect from others when disaster strikes" |
| #26 the income is front-ended | **E4-68**, **E4-69**, **E4-70**, **E4-71** | 2002 letter: mark-to-model degenerating into "mark-to-myth", and the energy and utility sectors reporting earnings "until the roof fell in"; 2003 letter: the "front-ending" of income dictated by GAAP, and Clayton retaining its loans; 2001 meeting, Munger: "The accounting is improper. It front-ends way too much income." |
| #14 the regulated return | **E5-60** | 2015 letter: the prescribed return on capital, the redecorating joke, and federally subsidised renewables that "may eventually erode the economics of the incumbent utility" |
| #18 the sale is financed to fail | **E4-72**, **E4-73** | 2003 letter, two rows: terrible loans unloaded on naive lenders; and the different model required, one that stops the seller pocketing money up front on loans "destined to default" |
| #13 the non-owned input | **E3-79** | 1990 letter: the See's landlord refusing to renew, at a rent that "would have wiped out the store's profit" - and the 263 customers who reversed it |
| #22 society withdraws it | **E3-80**, **E4-74** | 1994 meeting: "the economics of the business may be fine, but that doesn't mean it has a great future"; 1999 meeting, Munger: the legislative threat "is serious, and I haven't the faintest idea of how to predict it" |
| #27 the graded verdict | **E5-61** | 2016 meeting, continuing where E5-55 stops: returns on equity go down, "it hasn't turned it into a bad business, it's turned it into a less attractive business than earlier" |
| #24 dilution | **E2-78**, **E5-62** | 1982 letter: mergers non-dilutive in the reported sense that were "instantly value destroying", the calculation in intrinsic value "too seldom made"; 2013 meeting as the COUNTER-row - Singleton buying in stock "relentlessly and very logically, like a great chess player should" |
| #5 (absorbing #15) | **E2-79** | 1989 letter: "the time elapsing between folly and failure can be stretched out", and "A base business can not be transformed into a golden business by tricks of accounting or capital structure" |

**No duplicates.** All 25 passages were absent from the ledger on a phrase grep of every quote cell,
the naked-swimmer sentence and "mark-to-myth" included, so both were cut whole rather than trimmed.
E2-54 quotes the same 1989 section at lines 1368-1376 and does not overlap E2-79. E5-61 begins at the
sentence after E5-55's quote ends, so the two share line 409 and no words.

**Six line numbers in the ordering brief were wrong, each corrected against the disk:** the 1994
meeting's "great future" sentence is at line 431, not 427 (it is in Buffett's follow-up, so the row is
cut as two fragments, 427 and 431); the 2001 letter's daisy-chain passage ends at 559, not 558; the
2014 letter's at 1477, not 1474; the 1999 letter's begins at 323, not 322; and the 2003 letter's
Clayton passage and the 2002 letter's mark-to-myth passage each begin a line earlier than given, at
941 and 788. The 1988 letter's paragraphs break at 625, 634 and 647, not at the 635/636 the brief
proposed, so the two-row split follows the paragraphs.

**Judgment calls, stated:** the 1988 letter is TWO rows (a monitoring trigger and a survival verdict,
separately citable; one row would have run to 1,929 characters, longer than any quote the ledger
holds); the 2015 letter is ONE row on E3-76's precedent, because the prescribed return causes the
cost base the subsidy erodes and splitting it would let either half be cited without the other; and
E3-78 and E4-69 are cut a few lines wider than asked, because neither was self-contained without the
sentence naming its mechanism.

`python tools/check_framework.py` PASS: 311 rows, 311 unique ids, 311/311 source files on disk,
verbatim verified 310/311 (up exactly 25; the one non-quote is still E5-07), phantom citations 0 in
1,047 run files and in all five governing documents, unlabelled numbers 0.

**Update 2026-09-20 ~14:00:** the shapes are ruled from the corpus (13 kept, 3 merged, 2 dropped; 25 rows added, ledger 311); wave 7 first cycle started 13:46.

---

# ADDENDUM 2026-09-20 13:46 EDT - WAVE 7 OPENS: PAGP run, Q2 OUT; and two stale pointers the run caught on its way past

Written by the unattended overnight session of **2026-09-20 13:46 EDT** (branch B, the first cycle
since 2026-09-19 with a name to run). **Nothing above this line was edited** (operator rule 6).

State read first, not carried forward: register **132** entries before the run, `PAGP` absent from
`Screens/WATCHLIST RUN QUEUE.md` on a whole-file grep (0 hits), `Screens/_daily/_wave7_done.txt`
empty (0 lines), no `Test Runs/*Run - PAGP*.md` on disk, the lock at 13:46:18 (pid 14428) this
cycle's own. **PAGP is the first name in `_wave7_order.txt` and nothing was done, so branch B: run
from scratch.** One agent, `model: opus`, foreground, waited for.

**The run folded itself and all six steps were verified by this session, not taken on report:**
register **132 to 133**, counted with `^- \*\*` inside the slice from the `## COMPLETED FROM THE
QUEUE` heading to `## THE WRITE-EARLY PROTOCOL` only (the USAR fold trap); `PAGP` is the one line in
`_wave7_done.txt`; the narrative fold and `SURVIVAL SHAPES - index.md` went in the same commit;
**no band and no `alerts.json` row**, because the name failed on the BUSINESS and a price alert on
it is a category error (the QLYS ruling); `python tools/check_framework.py` **PASS**; both commits
carry a pathspec. `Test Runs/2026-09-20 Run - PAGP Plains GP Holdings.md`, 40,367 bytes.

## ADDED TO OPERATOR DECISIONS STILL OPEN

27. **Three present-tense documents say the ledger holds 267 rows; it holds 311.** The file grew by
    44 rows today, in `b7e84ca` (19 rows on the [E4-04] fast-change exclusion and on banks) and
    `0eaeadd` (25 rows for the survival shapes kept by the corpus ruling), and
    `check_framework.py` now prints 311 / 311 unique ids / 311 source files. Stale: **`CLAUDE.md`
    line 157**, **`Framework/PLAIN ENGLISH - what this is and how it works.md` line 15**, and
    **`Framework/README.md` line 26** - the same three files item 26 corrected from 261 and 76 this
    morning, stale again by the afternoon. **This is the 10:32 cycle's own durable instruction
    arriving on the cycle that wrote it**: *a stale pointer hides in the document nobody opens*, and
    the answer today is that it also hides in the document everybody opens, because a count is
    corrected on the day it is noticed and the ledger keeps growing after. **NOT EDITED, and the
    reason is not timidity:** CLAUDE.md's line carries a *composition* clause as well as a count -
    "266 verbatim quotes plus one negative finding", "262 distinct passages", "five passages entered
    under two ids each" - and none of those three sub-counts can be honestly updated without reading
    the 44 new rows against their sources. **Writing 311 while leaving a false composition beside it
    is worse than leaving both stale**, and PRIME RULE 6 says nothing is written until its evidence
    exists. The bounded unit for a later cycle: read the 44 rows, recount the composition, correct
    all three files together. *Found by the PAGP run agent, which ran `check_framework.py` before its
    commit as the FOLD requires and read the number it printed instead of the number its brief gave
    it - the brief said 267, on this session's authority, and the brief was wrong.*

28. **Every commit in this tree since 2026-07-13 carries a malformed author email:
    `chrehor36@gmail'.com`,** with a stray apostrophe almost certainly left by a PowerShell quoting
    accident. **1,543 of 1,543 commits, no clean ones.** The defect is not in this repository:
    `git config --show-origin user.email` resolves it to **`file:C:/Users/chreh/.gitconfig`**, the
    machine-wide global, so it is on every repository on this machine and it is the operator's own
    identity. **NOT EDITED** - a one-character fix, but it is outside the working folder and it is a
    person's name on their own work, which is not an unattended session's to change. History is not
    rebased either (operator rule 6); a fix would apply going forward only.

**One tooling defect found by the run and left standing, because the fix is a measurement, not an
edit:** `working_capital_flag()` **reads one balance-sheet line and never nets its counter-line.**
It fired on PAGP naming 2021, where `AccountsPayableAndAccruedLiabilities` released **$1,970M**
against $1,991M of operating cash - 99%, exactly as the screen said - while **receivables absorbed
$2,179M in the same year**, so net working capital was a **$227M drain**. The flag named the year
the cash was *drained* as the year it was *made*, because the two tags carry opposite cash-sign
conventions and the function reads neither against the other. **The flag was still right to fire**:
it sent a reader to the 2021 cash-flow statement, which is all a flag may do (operator rule 8 -
every flag is a prompt to read, never a score). It fires on 158 of 331 rows, so the size of the
false-direction class is unmeasured, and re-thresholding it blind would be adding a number rather
than getting the same number sooner. **Recorded, not fixed.**

**And a second, larger one, which the run's own last words called a class rather than a name: no
guard in this toolchain reads noncontrolling interests.** `owner_earnings()` takes the consolidated
operating-cash line whatever share of it belongs to the registrant's own shareholders. At PAGP that
overstated the numerator **roughly four times** against a denominator of one class of one tier, and
the screen's `growth_required` of **-13.81%** - the figure that sorted PAGP first in the whole
wave-7 order of 218 names - is a product of that mismatch and not a fact about the business. **Any
sponsor/MLP pair, multi-tier partnership or majority-owned-JV consolidator among the 217 names still
to run in `_wave7_order.txt` carries it**, and the three lines that detect it (the NCI line on the income statement,
on the balance sheet, and in partners' capital) are in every 10-K. **The wave-7 order is ranked on
an unadjusted yield for that whole class**, which is the same shape as the SBC-of-zero finding of
2026-09-12: not a wrong verdict, a wrong reading order.

**No name beyond PAGP was started.** The TJX re-run under v4.1, the duplicate shape number 25, the
four missing entry pointers and operator decisions 20-28 are all untouched.
