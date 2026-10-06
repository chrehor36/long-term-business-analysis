# Branch: experimental

**What this branch is for.** Testing the rules that earlier editions of the framework used without a source, to see
which of them actually worked, and building on the ones that did. The record of what was cut and why is in
`Framework/INVENTIONS - deleted and why.md`; the archived editions are under `Framework/ARCHIVE - */`; v5's own confessed
conventions are in Part VI of `Framework/THE FRAMEWORK v5.md`.

**Two rules for this branch.**

1. **Its rules stay off master.** The governing v5 framework on master takes its rules only from v5-scope passages
   (the annual meetings, the shareholder letters and the signed sections of the annual reports, through
   `principle_ledger_v5.csv`). Nothing tested here is merged into master's governing documents. A finding from this
   branch can reach master only the normal way: a written case with quotes from the v5 corpus, approved by the
   operator (PRIME RULE 5), with its ledger row first (PRIME RULE 6).
2. **It has its own working folder.** The public export, `tools/publish_public.py`, rewrites the master working copy
   from the private working repository. This branch is worked in its own folder (a git worktree,
   `C:\Users\chreh\BRK-experimental` on the operator's machine), never through the export, so an export can never
   overwrite it.

Branched 2026-10-05 from master at `be0a764` by the operator.
