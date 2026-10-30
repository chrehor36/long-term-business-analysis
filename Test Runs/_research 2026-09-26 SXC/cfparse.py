import re,json
txt=open('cf_statements.txt',encoding='utf-8').read()
blocks=re.split(r'^### ',txt,flags=re.M)[1:]
NUM=re.compile(r'^\(?\s*-?[\d,]+\.?\d*\s*\)?$|^—$|^-$')
def val(t):
    t=t.strip()
    if t in('—','-'): return 0.0
    neg=t.startswith('(')
    v=float(t.strip('()').replace(',','').strip())
    return -v if neg else v
res={}
for b in blocks:
    lines=b.split('\n'); fn=lines[0].split()[0]
    fy=2025 if 'tenk25' in fn else int(re.search(r'FY(\d{4})',fn).group(1))
    rows=[]; cur=None
    for l in lines[1:]:
        parts=[p.strip() for p in l.split('|')]
        parts=[p for p in parts if p not in('','$',')')]
        if not parts: continue
        if NUM.match(parts[0].replace(' ','')):
            if cur is not None:
                for p in parts:
                    if NUM.match(p.replace(' ','')): cur[1].append(val(p))
            continue
        # label line, maybe with numbers after
        cur=[parts[0],[]]; rows.append(cur)
        for p in parts[1:]:
            if NUM.match(p.replace(' ','')): cur[1].append(val(p))
    d={}
    for lab,v in rows:
        if len(v)>=3: d.setdefault(lab,v[:3])
    res[fy]=d
json.dump(res,open('cf_parsed.json','w'),indent=1)
pats={'OCF':r'(?i)^net cash provided by operating','DA':r'(?i)^depreciation','SBC':r'(?i)(stock|share).based compensation|^stock compensation','CAPEX':r'(?i)^capital expenditures','ACQ':r'(?i)acquisition|purchase of .*business','NCIDIST':r'(?i)distributions? to noncontrolling|distributions to unitholders.*public|to public unitholders','NI':r'(?i)^net (income|\(loss\)|loss)','IMP':r'(?i)impairment','BUYNCI':r'(?i)(purchase|acquisition) of .*(noncontrolling|interest|units)|repurchase of .*units|simplification'}
for fy in sorted(res):
    d=res[fy]; print('==',fy,'10-K (years',fy,fy-1,fy-2,')')
    for k,p in pats.items():
        for lab,v in d.items():
            if re.search(p,lab): print(f'  {k:8s} {lab[:70]:70s} {v}')
