# put.py START_MARKER END_MARKER FILE_WITH_TEXT : replace the run file text from START (inclusive) to END (exclusive)
import sys
p = 'Test Runs/2026-10-13 Run - SIEGY Siemens AG.md'
t = open(p, encoding='utf-8').read()
s, e, f = sys.argv[1], sys.argv[2], sys.argv[3]
i = t.index(s); j = t.index(e, i + len(s))
t = t[:i] + open(f, encoding='utf-8').read().rstrip('\n') + '\n\n' + t[j:]
open(p, 'w', encoding='utf-8').write(t)
print('ok', i, j)
