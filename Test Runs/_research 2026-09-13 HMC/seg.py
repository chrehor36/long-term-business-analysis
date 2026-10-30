import re, glob, json
files = {'FY2018': glob.glob('20F_FY2018_*d20f.txt')[0], 'FY2021': glob.glob('20F_FY2021_*d20f.txt')[0],
         'FY2023': glob.glob('20F_FY2023_*d20f.txt')[0], 'FY2026': glob.glob('20F_FY2026_*d20f.txt')[0]}
def num(s):
    s = s.strip()
    if s in ('—', '-', ''): return 0
    neg = s.startswith('(')
    v = int(s.strip('()').replace(',', ''))
    return -v if neg else v
seg = {}
for k, f in files.items():
    L = open(f, encoding='utf-8').read().split('\n')
    for i, l in enumerate(L):
        m = re.match(r'As of and for the year ended March 31, (\d{4})$', l)
        if not m: continue
        # segment table has 'Segment profit' within 12 lines
        blk = L[i:i+16]
        if not any(x.startswith('Segment profit') for x in blk): continue
        y = int(m.group(1)); d = {}
        for x in blk:
            parts = [p.strip() for p in x.split('|')]
            lab = parts[0]
            for key, pat in [('rev','Total'),('ext','External customers'),('profit','Segment profit'),('assets','Segment assets'),('da','Depreciation and amortization'),('capex','Capital expenditures'),('imp','Impairment losses on non-financial'),('eq','Share of profit')]:
                if lab.startswith(pat) and key not in d:
                    d[key] = [num(p) for p in parts[1:6]]
        seg[y] = d
json.dump(seg, open('seg.json','w'), indent=0)
names = ['Moto','Auto','FS','PP&O','Total']
print('year  ' + '  '.join(f'{n:>30}' for n in names[:4]))
for y in sorted(seg):
    d = seg[y]
    row = []
    for j in range(4):
        rev = d['rev'][j]; pr = d['profit'][j]; a = d['assets'][j]
        row.append(f"rev {rev/1e3:>7.0f} m {100*pr/rev:5.1f}% ROA {100*pr/a:5.1f}%")
    print(y, ' | '.join(row))
print()
for y in sorted(seg):
    d = seg[y]
    print(y, 'D&A', d['da'][:4], 'capex', d['capex'][:4], 'eq', d.get('eq', [None]*4)[:4], 'imp', d.get('imp',[None]*4)[:4])
