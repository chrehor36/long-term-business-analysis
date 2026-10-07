# adapt the ECL fold script to KEYS: every hard-coded ticker, count and next name replaced and asserted
p = 'fold.py'
s = open(p, encoding='utf-8').read()
R = [
    ("assert ents[1].startswith('- **OII ')", "assert ents[1].startswith('- **CLB ')"),
    ("open(DONE, 'a', encoding='utf-8', newline='').write(T + '\\n')",
     "dnl = '\\r\\n' if '\\r\\n' in open(DONE, encoding='utf-8', newline='').read() else '\\n'\nopen(DONE, 'a', encoding='utf-8', newline='').write(T + dnl)"),
    ("assert dl == ol[:len(dl)] and len(dl) == 100 and ol[len(dl)] == NEXT",
     "assert dl == ol[:len(dl)] and len(dl) == 102 and ol[len(dl)] == NEXT"),
    ("assert 'ECL-rerun-band' not in ids and 'ECL-floor-band' not in ids",
     "assert 'KEYS-rerun-band' not in ids and 'KEYS-floor-band' not in ids"),
    ("# 4b PORTFOLIO row after MSA", "# 4b PORTFOLIO row after ECL"),
    ("ci = [i for i, l in enumerate(P) if l.startswith('| - | MSA |')]",
     "ci = [i for i, l in enumerate(P) if l.startswith('| - | ECL |')]"),
    ("assert not any(l.startswith('| - | ECL |') for l in P)",
     "assert not any(l.startswith('| - | KEYS |') for l in P)"),
    ("then enter ECL in #10's instances", "then enter KEYS in #10's instances"),
]
for a, b in R:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
i = s.index("fold_line = (")
j = s.index("s = s.replace(a0, fold_line + a0)")
new = ("fold_line = ('- [x] Fold: register entry %d (%d before, heading unique at line %d, KEYS first and once, CLB second), "
       "done file %d lines ending KEYS and equal to the order file\\'s first %d, next %s; bands `KEYS-rerun-band` $154.81 and "
       "`KEYS-floor-band` $110.11 armed and a `PORTFOLIO.md` row added after ECL (a gate-clearer); survival-shapes index: KEYS "
       "entered in #10\\'s instances with a dated note (%d rows, maximum %d, counted before writing); KEYS in no tier roster "
       "(the whole queue file searched)\\n'\n"
       "             % (after, before, H2[0] + 1, len(dl), len(dl), NEXT, len(rows), mx))\n")
s = s[:i] + new + s[j:]
open(p, 'w', encoding='utf-8').write(s)
print('adapted')
