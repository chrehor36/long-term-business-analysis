import sys, re
# flatten a table region: join cell lines into rows by label
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(f, encoding='utf-8').read().split('\n')[a-1:b]
out, cur = [], ''
for x in L:
    x = x.strip().replace('​','')
    if not x or x in ('|', '$ |', '$', '​'):
        continue
    if re.match(r'^[A-Za-z(]', x) and not re.match(r'^\(?\s*[\d,\.]+\s*\)?\s*\|?$', x):
        if cur: out.append(cur)
        cur = x
    else:
        cur += ' ' + x
out.append(cur)
print('\n'.join(re.sub(r'\s*\|\s*', ' | ', o) for o in out))
