# -*- coding: utf-8 -*-
p=r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
t=open(p,encoding='utf-8').read()

a = """entry here** — the exact failure the FOLD rule of 2026-09-07 was written to stop, running in the
opposite direction this time (queue entry present, reading-list entry missing, instead of the
reverse). Its queue-fold edits were also still sitting **uncommitted** in the shared working tree
when the ROKU fold began; they were committed separately under their own title (`9abe450`) rather
than swept into a ROKU-titled commit. **The count below therefore advances by two, and BA's
narrative fold is still owed by whoever holds that session.**"""

b = """entry here** — the exact failure the FOLD rule of 2026-09-07 was written to stop, running in the
opposite direction this time (queue entry present, reading-list entry missing, instead of the
reverse). Its queue-fold edits were also still sitting **uncommitted** in the shared working tree
when the ROKU fold began; they were committed separately under their own title (`9abe450`) rather
than swept into a ROKU-titled commit. **The count below therefore advances by two, and BA's
narrative fold is still owed by whoever holds that session.**

> **ADDENDUM, same day, minutes later — the paragraph above is SUPERSEDED IN ITS SECOND HALF and
> is left standing per operator rule 6.** BA's narrative fold **did** land, concurrently, at commit
> `3a57500`, and it sits immediately above this ROKU entry. So "still owed" was true when written
> and false within the hour, and the honest reading is narrower than what I wrote: **the BA fold
> was not missing, it was IN FLIGHT, and I could not tell the difference from the file on disk.**
> That is worth more than the observation it replaces, because it is a *new* failure mode for the
> FOLD rule: **the rule assumes a fold is either done or not done, and gives a concurrent reader no
> way to distinguish "not folded" from "being folded right now."** The two facts that did hold up
> are the ones to keep: BA's queue edits were genuinely uncommitted in the shared tree when I
> reached it, and committing them separately at `9abe450` was the right call — it is exactly the
> wrongly-titled-commit collision the FOLD rule records as having happened three times. **The
> cheap guard is a convention, not code: a run that has finished its analysis and started its fold
> commits its queue edit FIRST and alone, so the tree never carries a half-finished fold that
> another session must guess about.** The counts are sequential and correct: BA 72/43 at line
> 8024, ROKU 73/44 below."""

assert a in t
t=t.replace(a,b)
open(p,'w',encoding='utf-8').write(t)
print('ok')
