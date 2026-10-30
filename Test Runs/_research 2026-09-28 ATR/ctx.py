import re, sys
sys.stdout.reconfigure(encoding='utf-8')
# usage: ctx.py FILE "needle" before after
p, k = sys.argv[1], sys.argv[2]
b = int(sys.argv[3]) if len(sys.argv) > 3 else 1200
a = int(sys.argv[4]) if len(sys.argv) > 4 else 400
s = re.sub(r'\s*\|\s*', ' ', open(p, encoding='utf-8').read()); s = re.sub(r'\s+', ' ', s)
i = s.find(k)
print('==', p, i)
if i >= 0: print(s[max(0, i - b):i + a])
