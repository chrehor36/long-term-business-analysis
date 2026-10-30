# record the fold's own error in the run file's own-errors line (history of committed text not rewritten)
p = 'Test Runs/2026-09-28 Run - KEYS Keysight Technologies.md'
s = open(p, encoding='utf-8').read()
a = "(10) the Q4 draft said the filer describes its capex by site, which no filing read says; removed before commit."
assert s.count(a) == 1
b = a + (" (11) **the fold script (`fold.py`, adapted from ECL's by `adapt_fold.py`) stopped at step 5**: the survival-shapes note "
         "carried \"44%\", which Python's %-formatting read as a directive; steps 1-4 (register entry, done file, reading list, "
         "bands and `PORTFOLIO.md` row) had completed and printed their verified counts, and the shapes file had not been written; "
         "the note was escaped and `fold_rest.py` ran steps 5-6 after recomputing the counts from the files as written; no file "
         "was written twice.")
s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
