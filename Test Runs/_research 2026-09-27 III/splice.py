import sys
# usage: python splice.py body.md "START MARKER" "END MARKER"
# replaces run-file text from START (inclusive) to END (exclusive) with body
p = '../2026-09-27 Run - III Information Services Group.md'
body, a_m, b_m = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(p, encoding='utf-8').read()
assert s.count(a_m) == 1, ('start not unique', s.count(a_m))
assert s.count(b_m) == 1, ('end not unique', s.count(b_m))
a = s.index(a_m); b = s.index(b_m)
assert a < b
s = s[:a] + open(body, encoding='utf-8').read().rstrip() + '\n\n' + s[b:]
open(p, 'w', encoding='utf-8').write(s)
print('ok', len(s.splitlines()), 'lines')
