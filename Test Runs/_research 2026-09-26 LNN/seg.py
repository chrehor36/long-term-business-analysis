import re
res={}
for fy in range(2010,2026):
    t=open(f'tenk_FY{fy}.txt',encoding='utf-8').read()
    t=re.sub(r'[\s|​\xa0]+',' ',t)
    for seg,pat in (('IRR',r'Irrigation (?:Equipment )?[Ss]egment'),('INF',r'Infrastructure (?:Products )?[Ss]egment')):
        m=re.search(pat+r'[^$]{0,40}?Operating revenues \$ ([\d,]+) \$ ([\d,]+).{0,260}?Operating income(?: \(\d\))? \$ (\(?[\d,]+ ?\)?) \$ (\(?[\d,]+ ?\)?)',t)
        if m:
            g=[x.replace(',','').replace(' ','') for x in m.groups()]
            g=[-float(x.strip('()')) if x.startswith('(') else float(x) for x in g]
            res.setdefault((seg,fy),(g[0],g[2])); res.setdefault((seg,fy-1),(g[1],g[3]))
            print(fy,seg,g)
        else: print(fy,seg,'nf')
    m=re.search(r'Return on invested capital[^%]{0,40}?((?:\(?-?[\d.]+ ?\)? ?%\s*){3,5})',t)
    if m: print(fy,'ROIC',m.group(1))
print()
for seg in ('IRR','INF'):
    for fy in range(2009,2026):
        if (seg,fy) in res:
            r,o=res[(seg,fy)]; print(seg,fy,f'{r/1e3:.1f} {o/1e3:.1f} {o/r*100:.1f}%')
