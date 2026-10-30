import sys
p, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(p, encoding='utf-8').read().split('\n')[a-1:b]
out = []
for l in L:
    s = l.strip().strip('|').strip()
    if not s: continue
    out.append(s)
t = ' '.join(out)
import re
t = re.sub(r'\$ ', '$', t); t = re.sub(r'\( ', '(', t); t = re.sub(r' \)', ')', t)
print(t)
