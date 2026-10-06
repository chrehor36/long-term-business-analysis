# Branch: ben-graham

**What this branch is for.** The Benjamin Graham side project: a framework built from Graham's own methods (net
current assets, earnings and asset tests, margin of safety by the numbers), its own board and ledger, and its own runs.
It starts from the material already in `Ben Graham/`: `Ben Graham/GRAHAM BOARD.md`,
`Ben Graham/A Framework for Graham Operations v0.1.md`, `Ben Graham/graham_ledger.csv` and the 2026-07-17 screen.

**Two rules for this branch.**

1. **Graham stays off master.** On master, Graham is off the citation shelf (PRIME RULE 4 of
   `Framework/OPERATOR-PROTOCOL.md`): the governing v5 framework may name him only as Buffett and Munger name him, and
   takes its rules only from the v5 corpus. Nothing built here is merged into master's governing documents, and
   Graham's own texts are cited here, not there.
2. **It has its own working folder.** The public export, `tools/publish_public.py`, rewrites the master working copy
   from the private working repository. This branch is worked in its own folder (a git worktree,
   `C:\Users\chreh\BRK-ben-graham` on the operator's machine), never through the export, so an export can never
   overwrite it.

Branched 2026-10-06 from master at `be0a764`, at the operator's request.
