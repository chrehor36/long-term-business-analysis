# replace a section of the run file: python w_section.py START_MARKER END_MARKER newtext_file
import sys
p = "Test Runs/2026-10-18 Run - AQN Algonquin Power & Utilities.md"
s = open(p, encoding='utf-8').read()
start, end, f = sys.argv[1], sys.argv[2], sys.argv[3]
a = s.index(start)
b = s.index(end, a + 1) if end != "EOF" else len(s)
new = open(f, encoding='utf-8').read()
s = s[:a] + new + s[b:]
open(p, 'w', encoding='utf-8').write(s)
print('replaced', start, '->', end)
