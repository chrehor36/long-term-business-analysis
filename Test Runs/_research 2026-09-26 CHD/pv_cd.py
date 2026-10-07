import re,glob,json
out={}
for f in sorted(glob.glob('tenk_20*.txt')):
    L=[re.sub(r'\s*\|\s*$','',x.strip()).strip() for x in open(f,encoding='utf-8').read().split('\n')]
    L=[x for x in L if x not in ('','|')]
    fy=f[5:9]
    for i,x in enumerate(L):
        if re.match(r'Net Sales\s*[-–—]\s*Consumer Domestic',x):
            yr=None; rows=[]; j=i+1; lab=None
            while j<len(L) and j<i+90:
                y=L[j]
                m=re.search(r'(20\d\d)$',y)
                if yr is None and (y.startswith('December 31') or re.match(r'^20\d\d$',y)):
                    if m: yr=m.group(1)
                    j+=1; continue
                if re.match(r'^\(?-?[\d.]+\)?$',y):
                    v=float(y.replace('(','-').replace(')',''))
                    if lab: rows.append((lab,v)); lab=None
                elif y in ('%','%)'): pass
                else: lab=y
                if rows and rows[-1][0].startswith('Net Sales'): break
                j+=1
            print(fy,yr,rows)
            out.setdefault(str(yr),{})[fy]=rows
json.dump(out,open('pv_cd.json','w'),indent=1)
