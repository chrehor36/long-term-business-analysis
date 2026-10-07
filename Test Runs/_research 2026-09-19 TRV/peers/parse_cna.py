import re,json
def num(s):
    s=s.strip().replace(',','').replace('$','').replace('%','').strip()
    if s in('—','-','–'): return 0.0
    neg=s.startswith('(')
    s=s.strip('()').strip()
    try: v=float(s)
    except: return None
    return -v if neg else v
def rows(lines):
    d={}
    for l in lines:
        parts=[p.strip() for p in l.split('|')]
        if len(parts)<2: continue
        lab=parts[0]; vals=[num(p) for p in parts[1:] if p.strip() not in (')',')%','%')]
        vals=[v for v in vals if v is not None]
        if lab and vals and lab not in d: d[lab]=vals
    return d
out={}
for y in range(2016,2026):
    L=open(f'raw/CNA_10K_FY{y}.txt',encoding='utf-8').read().split('\n')
    src=L[0]
    for i,l in enumerate(L):
        m=re.search(r'The following table (?:details|summarizes) the results of operations for (Specialty|Commercial|International)\.',l)
        if m:
            seg=m.group(1)
            if (y,seg) in out: continue
            blk=L[i+1:i+40]
            # stop at narrative
            cut=next((k for k,b in enumerate(blk) if 'Compared with' in b or 'Compared to' in b),len(blk))
            hdr=[b for b in blk[:cut] if re.search(r'\| 20\d\d',b)]
            out[(y,seg)]={'hdr':hdr[0] if hdr else '', 'rows':rows(blk[:cut])}
for k,v in out.items():
    print(k, v['hdr'])
    for lab,vals in v['rows'].items(): print('   ',lab,vals)
json.dump({f"{k[0]}|{k[1]}":v for k,v in out.items()},open('raw/_cna_parsed.json','w'),indent=0)
