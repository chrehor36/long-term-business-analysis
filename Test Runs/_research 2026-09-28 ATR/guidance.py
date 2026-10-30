import re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
# [E3-48]: the company's own quarterly guidance against its own reported outturn, from each EX-99.1.
rows = []
for p in sorted(glob.glob('cache/r2*x8kexx991.htm.txt')):
    s = re.sub(r'\s+', ' ', re.sub(r'\s*\|\s*', ' ', open(p, encoding='utf-8').read())).replace('​', '')
    g = re.search(r'expects (?:adjusted )?earnings per share for the (\w+) quarter of (\d{4})[^$]{0,200}?range of \$\s?([\d.]+) to \$\s?([\d.]+)', s)
    a = re.search(r'[Aa]djusted earnings per share[^$.]{0,80}?(?:were|was|of|to) \$\s?([\d.]+)', s)
    rows.append((p[6:13], g.group(1, 2, 3, 4) if g else None, a.group(1) if a else None))
qn = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
print('release | guidance given for next quarter | adjusted EPS reported this release')
for r in rows: print(r[0], '|', r[1], '|', r[2])
print()
print('quarter | guided low-high | reported | against range')
for i in range(len(rows) - 1):
    g = rows[i][1]; nxt = rows[i + 1][2]
    if not g or not nxt: continue
    lo, hi, act = float(g[2]), float(g[3].rstrip('.')), float(nxt)
    pos = 'ABOVE' if act > hi else ('BELOW' if act < lo else 'inside')
    print('Q%d %s | %.2f-%.2f | %.2f | %s' % (qn[g[0]], g[1], lo, hi, act, pos))
