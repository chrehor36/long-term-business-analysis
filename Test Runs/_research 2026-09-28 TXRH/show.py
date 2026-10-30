import sys, re
# show.py FILE START END : print a line range with whitespace collapsed (table cells kept on one line)
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(f, encoding='utf-8').read().split('\n')[a-1:b]
out = []
for x in L:
    x = re.sub(r'\s+', ' ', x).strip()
    if x in ('', '|'):
        continue
    out.append(x)
txt = '\n'.join(out)
sys.stdout.reconfigure(encoding='utf-8')
print(txt)
