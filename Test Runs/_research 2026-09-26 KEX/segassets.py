import re,glob
def norm(t):
    t=re.sub(r'[ \t]*\|[ \t]*',' | ',t); t=re.sub(r'(\|\s*)+','| ',t); return re.sub(r'\s+',' ',t)
for fn in sorted(glob.glob('tenk_*.txt')):
    t=norm(open(fn,encoding='utf-8').read())
    m=re.search(r'Total assets:? \| Marine transportation \| \$? ?\|? ?([\d,]+) \| \$? ?\|? ?([\d,]+)',t)
    g=re.search(r'Goodwill:? \| Marine transportation[^A-Za-z]{0,80}',t)
    tot=re.search(r'Total Kirby stockholders.{0,4}equity \| ([\d,]+) \| ([\d,]+)',t)
    print(fn, m.groups() if m else None, (g.group(0)[:120] if g else ''), tot.groups() if tot else None)
