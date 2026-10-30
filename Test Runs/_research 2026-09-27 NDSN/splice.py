# usage: python splice.py <start_marker> <end_marker> <bodyfile>  -- replaces text from start_marker (inclusive) up to end_marker (exclusive)
import sys
p = "../2026-09-27 Run - NDSN Nordson.md"
s = open(p, encoding="utf-8").read()
a, b, body = sys.argv[1], sys.argv[2], open(sys.argv[3], encoding="utf-8").read()
i = s.index(a); j = s.index(b, i + len(a))
assert s.count(a) == 1, "start marker not unique"
s = s[:i] + body.rstrip("\n") + "\n\n" + s[j:]
open(p, "w", encoding="utf-8").write(s)
print("spliced", i, j)
