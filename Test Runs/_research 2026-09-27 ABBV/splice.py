"""Replace the block of the run file from a start heading up to (not including) an end heading with a body file."""
import sys
run, start, end, body = sys.argv[1:5]
s = open(run, encoding='utf-8').read()
i = s.index(start)
j = s.index(end, i + len(start)) if end != 'EOF' else len(s)
b = open(body, encoding='utf-8').read()
if not b.endswith('\n'): b += '\n'
s = s[:i] + b + s[j:]
open(run, 'w', encoding='utf-8').write(s)
print('spliced', len(b), 'chars between', repr(start), 'and', repr(end))
