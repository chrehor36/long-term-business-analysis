# PREREGISTRATION 2026-10-06: four re-runs under sections A, D and H of the gaps case
*Written and committed before any re-run began (operator rule 9: pre-register before computing, frame to refute). The commit
that carries this file is the seal; the four test runs are written after it. The case is
`Framework/v5/CASE 2026-10-05 - gaps found by the small-cap runs, for the operator's approval.md`; its DECIDED blocks of
2026-10-06 adopted A, B, C, E and G outright and D and H subject to this test. No test analyst opens this file.*

## What is tested
Three rules, each on the name whose original run raised it:

| name | original run (binds as written) | original box | rule under test | what the rule is expected to change |
|---|---|---|---|---|
| ENSG, The Ensign Group | `Test Runs/2026-10-05 Run - ENSG Ensign Group.md` | OUT at Q4, suspicion under the two-tell convention | section A (adopted; in the framework) | Q4 no longer closes on the press-release habit alone; the habit is weighed at Q4 and judged at Q5 with the integrity record |
| RYZ, Ryerson | `Test Runs/2026-10-05 Run - RYZ Ryerson Holding.md` | OUT at Q2 | section D(a), cycles | the box is unchanged; the Q7 COMPUTATION is built on the last full cycle's average with the literal window beside it, and the range and fair price differ from the original's five-year window |
| EFOR, Everforth (formerly ASGN) | `Test Runs/2026-10-05 Run - EFOR Everforth.md` | TOO HARD (NATURE) at Q1 | section D(c), acquisitions | the box is unchanged; the Q7 COMPUTATION states which consistent pair it used (acquisitions deducted with total growth, the default) and shows the other beside it |
| PBH, Prestige Consumer Healthcare | `Test Runs/2026-10-05 Run - PBH Prestige Consumer Healthcare.md` | OUT at Q7, on the all-equity basis the analyst chose | section H, the all-equity basis as the central figure | a second analyst, given H as a written rule, lands on the same basis and the same box, with the equity-only figure beside |

*(The original file names above are as the register records them; if a file name differs in a word, the register's entry for
the ticker under `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md` is the authority.)*

## The hypothesis, framed to refute
**H0, to be refuted:** each rule under test is idle or confounded. A rule is **idle** if the re-run that applies it reaches the
same figures and the same box as the original by the same route, so the rule changed nothing. A rule is **confounded** if the
box moves for a reason the rule does not name. A rule **holds** if the analyst applied it from its text without confessing a
CONVENTION the text leaves open, and whatever it changed is a change the rule names.

## Pass rules, fixed now
1. **D holds** if, in the RYZ and EFOR re-runs, the analyst could identify the cycle (RYZ) and the acquisition pair (EFOR) from
   the filings alone, applied the specific as written, said "rule under test" where it bore, and the box did not move. If the
   analyst could not identify a full cycle from the filings, (a) is sent back to the case as inapplicable as written. If the
   box moved, D is confounded on that name and goes back to the case with the reason.
2. **H holds** if the PBH re-run builds its central Q7 figure on the all-equity basis, shows the equity-only figure beside it,
   and closes in the same box as the original (OUT at Q7) or in a different one for a reason the rule names (the floor earned
   or not earned on the whole-business price). If the re-run closes IN on the equity-only figure, H failed to govern and goes
   back to the case.
3. **A is already adopted** and is not withdrawn by this test. The ENSG re-run is recorded against it: if Q4 closes OUT again,
   the record states whether the suspicion came from the accounts themselves (the rule held: the STOP fell where reading four
   puts it) or from the press-release habit counted as a tell (the rule failed to govern, and the case is reopened). If Q4 is
   IN or a weighing and Q5 decides, the record states what Q5 found.
4. In every re-run: no row is cited beside words that are not the row's own; the acceptance test passes; the analyst's
   self-audit is honest. A re-run that fails this rule is a failed test run, not evidence on the rule.
5. The price is today's, not the original's. Price differences are recorded and the comparison is on the basis, the range and
   the box, never on the price alone.

## What the test runs are
Test records, like the fifteen runs of the v5 tests: written to `Framework/v5/tests/` as `T2 <TICKER> - rerun.md` with the
working folder `Framework/v5/tests/_work_T2_<TICKER>/`; they bind nothing, enter no register, and change no verdict of record.
The protocol for the analysts is `Framework/v5/tests/T2 PROTOCOL - the four re-runs of 2026-10-06.md`; the two rule texts are
`Framework/v5/tests/RULES UNDER TEST 2026-10-06 - sections D and H.md`. The analysts are blind to the originals, to every
`Test Runs/` file, to the case, and to this file; each sees the governing framework as amended today, the template, the ledger,
the protocol and the rule texts. Per-question pathspec commits are granted; the lock is written by the dispatching session
(operator rule 10).

## Hazards declared
- The four names were chosen because their originals raised the rules; a rule that holds on the name that raised it is not
  thereby shown to hold elsewhere. Four names is a small test.
- The ENSG re-run tests a rule already adopted; the finding can reopen the case but cannot, by itself, un-adopt it.
- RYZ and EFOR closed before Q7; their D test is on a COMPUTATION, NOT A CLEARANCE, not on a verdict.
- The PBH original already used the all-equity basis; the H test on it is a reproducibility test of the rule as written, not a
  test of whether the basis changes the box.
- The analysts know from the rule texts' title that the texts are "under test"; they do not know on which name or why.

## RESULTS
*(Appended after the four re-runs, before any adoption language.)*

### Written 2026-10-06, after the four re-runs closed, before any adoption language
The four test runs are `Framework/v5/tests/T2 ENSG - rerun.md`, `T2 RYZ - rerun.md`, `T2 EFOR - rerun.md` and `T2 PBH - rerun.md`,
each committed question by question by its analyst (the working folders are untracked: `.gitignore` already ignores
`Framework/v5/tests/_work_*/`, which the T2 protocol did not know). The main session's citation check found every id resolving
and no quoted fragment outside its row in any of the four; `tools/check_framework.py` PASS. Rule 4 is met by all four. All
four analysts declared what they saw by accident (file names in a listing, commit subjects naming the other re-runs); none
opened a blind-listed file. The four were run and resumed after one timed session limit; nothing committed was lost.

| name | original box | re-run box | the rule under test, as applied |
|---|---|---|---|
| ENSG | OUT at Q4 (two tells) | TOO HARD (NATURE) at Q2 | section A not reached: the file closed at Q2 before Q4 |
| RYZ | OUT at Q2 | OUT at Q2 | D(a) applied from the filings: the window opens on a year the filer calls a cyclical high, the base is the last full cycle FY2020 to FY2025, the literal window beside, growth between cycle averages; D(b), D(c), D(f) and H also bore and were marked |
| EFOR | TOO HARD (NATURE) at Q1 | OUT at Q2 | D(c) applied from the filings: net acquisitions deducted, total growth credited, the second pair not showable because the filer reports no organic growth; D(a), D(b), D(e), D(f) and H also bore and were marked |
| PBH | OUT at Q7, on the all-equity basis the analyst chose | OUT at Q7 | H applied as written: the central figure on unlevered owner cash against market value plus net debt, the equity-only figure beside and not deciding; D(b) and D(c) also bore |

**Pass rule 1, D.** On RYZ, D holds: the cycle was identified from the filings, the specific was applied as written, "rule
under test" was written where it bore, and the box did not move. On EFOR, the box moved (TOO HARD (NATURE) at Q1 to OUT at
Q2); by the letter of rule 1 that is a FAIL and D goes back to the case with the reason. The reason is identifiable and lies
outside D: the re-run closed under sections B (the Commercial segment, more than half of five-year operating profit, decides)
and C (a durable position earning ordinary returns over the cycle closes OUT), both adopted this morning and both absent
when the original ran; D bore only on the Q7 COMPUTATION, where the analyst could apply D(c) from the filings. The
pre-registration did not anticipate that the sections adopted outright would move the box of a name chosen to test a
section adopted subject to test; that is a defect of this design, stated here and not cured after the fact. Three findings go
back to the case with D in any event: (i) D(a) does not say which series defines the cycle (RYZ); (ii) D(c) does not cover a
deal closed after the window and before the price date (RYZ and PBH, who each valued it on its own filed record and added its
financing to net debt); (iii) D(e)'s "never charge all spending and also cap the growth" put the no-growth maintenance-only
case above the growth case for a serial acquirer whose purchases bought less growth than they cost (EFOR), which inverts the
range's ends. The inversion is not a defect of arithmetic: it is the finding the rows name, "growth can destroy value"
**[L2000-023]**; D(e) should say so, so that an analyst does not read it as an error.

**Pass rule 2, H.** H holds on PBH: the central figure was built on the all-equity basis, the equity-only figure shown beside,
and the box is the original's (OUT at Q7). H was also applied without confession in the other three re-runs. One refinement
goes back with it: H does not say which date's net debt (RYZ); PBH took the latest filed balance sheet plus the subsequent
events the filing itself states, which is the reading to write down.

**Pass rule 3, A.** The ENSG re-run closed at Q2, so it says nothing about section A either way. A stays adopted; the case is
not reopened by this test, and nothing here is counted as a pass for A.

**Pass rule 5.** Prices were today's; every comparison above is on the basis, the range and the box.

**What the figures say, outside the pass rules.** PBH's fair price moved from $47.74 (the original, the floor applied to
pre-tax cash on the whole business) to $9.14 (the re-run: section E's after-tax owner cash, D(c)'s acquisitions deducted,
D(b)'s negative growth carried, and the two debt-financed deals closed since the original added to net debt). The largest
single step is section E, which applies to every run from now on: the floor on owner cash after the company's tax, with no
conversion, makes every fair price lower than the pre-tax practice of the runs of 2026-10-05 and 2026-10-06, including the
fourteen large-cap fair prices armed as alerts today. Those alerts stand as the runs' own figures; a re-run under E would
lower each of them.

**Verdict, as pre-registered.** D: holds on RYZ, fails by the letter on EFOR for a reason outside D, and returns to the case
with the three findings above. H: holds, and returns to the case only for the net-debt date. Neither enters the governing
text on this test alone; the operator decides on the amended texts.
