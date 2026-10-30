# Parse Note 13 incurred-loss triangles from the FY2025 10-K (0000005272-26-000023) and compute
# first estimate -> 2025 estimate development by accident year. Undiscounted, net of reinsurance
# (tables state: "with separate presentation of the adverse development cover where applicable").
import re, sys
L = open('tenk_FY2025.txt', encoding='utf-8').read().split('\n')
out = []
i = 0
while i < len(L):
    if L[i].startswith('Incurred Losses and Allocated Loss Adjustment Expenses, Undiscounted and Net of Reinsurance'):
        # title = the nearest non-empty line above that is a line-of-business name
        j = i - 1
        while j > 0 and (not L[j].strip() or len(L[j]) > 200): j -= 1
        # walk back further to find the heading preceding description paragraph
        title = L[j].strip()
        k = i - 1; heads = []
        while k > i - 12:
            s = L[k].strip()
            if s and len(s) < 60 and not s.startswith('|'): heads.append(s)
            k -= 1
        name = heads[-1] if heads else title
        name = heads[0] if heads else title
        rows = {}
        for m in range(i, i + 40):
            s = L[m]
            mm = re.match(r'^(20\d\d) \| (.*)$', s)
            if mm:
                ay = int(mm.group(1))
                nums = [float(x.replace(',', '').replace('(', '-').replace(')', '')) for x in re.findall(r'\(?[\d,]+\)?', mm.group(2).replace('$', ''))]
                rows[ay] = nums
            if s.startswith('Total |'): break
        out.append((name, i + 1, rows))
        i += 40
    i += 1
for name, ln, rows in out:
    print('\n== %s (line %d)' % (name, ln))
    tot_first = tot_last = 0
    for ay in sorted(rows):
        v = rows[ay]
        nyrs = 2025 - ay + 1
        tri = v[:nyrs]
        if not tri: continue
        first, last = tri[0], tri[-1]
        ibnr = v[nyrs] if len(v) > nyrs else None
        chg = (last / first - 1) * 100 if first else 0
        tot_first += first; tot_last += last
        one = (tri[-1] / tri[-2] - 1) * 100 if len(tri) > 1 and tri[-2] else 0
        print('AY%d first %8.0f  2025 %8.0f  %+6.1f%%  (last yr %+5.1f%%)  IBNR %s  %s' % (ay, first, last, chg, one, ibnr, ' '.join('%.0f' % x for x in tri)))
    print('  sum AY first %.0f -> 2025 %.0f  %+.1f%%' % (tot_first, tot_last, (tot_last / tot_first - 1) * 100 if tot_first else 0))
