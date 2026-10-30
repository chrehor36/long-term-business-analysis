# print windows around regex matches in a cached text file: grab.py FILE PATTERN [before] [after] [max]
import sys, re, os
f, pat = sys.argv[1], sys.argv[2]
b = int(sys.argv[3]) if len(sys.argv) > 3 else 300
a = int(sys.argv[4]) if len(sys.argv) > 4 else 600
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 5
p = f if os.path.exists(f) else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache', 'f', f)
t = open(p, encoding='utf-8').read().replace('\n', ' ')
out = []
for i, m in enumerate(re.finditer(pat, t, re.I)):
    if i >= mx: break
    out.append('[%d] ...%s...' % (m.start(), t[max(0, m.start()-b):m.end()+a]))
sys.stdout.buffer.write(('\n\n'.join(out) + '\n').encode('utf-8'))
