import glob, re, json
tot_sh = 0; tot_v = 0; rows = []
for f in sorted(glob.glob('6k/*.txt')):
    t = open(f, encoding='utf-8').read()
    if 'Share buybacks in Ericsson during' not in t: continue
    m = re.search(r'\nTotal \| ([\d,\.]+) \| ([\d\.]+) \|(?: \d+ \|)? ([\d,\.]+)', t)
    tr = re.search(r'treasury stock amounts to ([\d,]+)', t)
    per = re.search(r'during the period ([^\n]+?20\d\d)', t)
    if not m:
        print('NO TOTAL', f); continue
    sh = float(m.group(1).replace(',', '')); v = float(m.group(3).replace(',', ''))
    tot_sh += sh; tot_v += v
    rows.append((f[3:13], per.group(1) if per else '', int(sh), round(v/1e6,1), tr.group(1) if tr else None))
for r in rows: print(r)
print('total shares', int(tot_sh), 'SEK m', round(tot_v/1e6,1), 'avg', round(tot_v/tot_sh,2))
json.dump({'rows': rows, 'shares': tot_sh, 'sek': tot_v}, open('bb_out.json','w'), indent=1)
