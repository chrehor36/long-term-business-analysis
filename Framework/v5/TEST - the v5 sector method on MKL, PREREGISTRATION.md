# TEST — the v5 sector method on MKL (Markel Group) — PREREGISTRATION — 2026-10-05
**Committed before the run.** The operator chose, on 2026-10-05, to test
`Framework/v5/CASE 2026-10-05 - a v5 sector method for insurers and float companies, for the operator's approval.md` on
one insurer before adopting it. MKL is the case because its run of 2026-09-02 under v4.1
(`Test Runs/2026-09-02 Run - MKL Markel Group.md`) found the two defects any insurer method must survive: a double count
of underwriting profit, and a first component that gave two answers far apart depending on its construction.

## The run
A session that has not seen the 2026-09-02 MKL run file, its research folder, the register or reading-list entries for MKL,
or this project's earlier insurer runs, runs MKL under `Framework/THE FRAMEWORK v5.md` with the case's method applied where
the case says it applies. The questions are answered in order and the first STOP that closes the file closes it, as in any
v5 run; **the method's arithmetic is carried to its end in every case**, under COMPUTATION — NOT A CLEARANCE where a STOP
has already closed the file, because the test is of the method. The run is written to
`Framework/v5/tests/SM MKL - the v5 sector method.md`. It is not a run of record and binds nothing.

## Pass rules, fixed now
- **P1, executability.** Every step of the method's section 3 is carried out from MKL's own filings and gives its figure:
  float, the cost of float, component 1, component 2, and a value range. A step that cannot be carried out names the missing
  input and the document that would supply it; more than one such step fails P1.
- **P2, no double count.** Investment income is outside component 2, and underwriting profit or loss enters the value once,
  in one place the run names.
- **P3, one answer for component 1.** The method's conventions decide which construction of component 1 applies, so the run
  reports one figure, not two. If it still produces two constructions whose figures differ materially, P3 fails, and the
  case's convention that should decide it is named for amendment.
- **P4, scope.** Every judgment cites a v5 id or a CONVENTION of the case; no v4 id; check 7 of the acceptance test passes.
- **P5, comparison.** After the run, a comparison file sets its figures and its close beside the 2026-09-02 run and explains
  every difference as a difference of method, of data (eleven months more filings), or of judgment.

**Verdict.** The method passes if P1, P2, P3 and P4 hold. A failure on any of them is amended in the case before adoption,
and the amendment is written down before the run is repeated. P5 is reported, not scored.
