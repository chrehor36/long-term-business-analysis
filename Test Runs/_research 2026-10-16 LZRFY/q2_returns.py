"""Q2 field returns: pre-tax EBIT over average capital (equity + net debt), and the same after 34% (Brazil's statutory
IRPJ+CSLL), set beside the year-end yield of the longest Tesouro Prefixado com Juros Semestrais (Tesouro Nacional file)."""
import csv
sov = {2015:16.57,2016:11.51,2017:10.37,2018:9.32,2019:6.93,2020:7.01,2021:10.82,2022:12.81,2023:10.44,2024:15.28,2025:13.89}
rows = list(csv.DictReader(open('peer_returns.csv')))
by = {}
for r in rows: by.setdefault(r['company'],[]).append(r)
out=[]
for co, rs in by.items():
    vals=[]
    for r in rs:
        y=int(r['year']); a=r['EBIT_cap_avg']
        if not a: continue
        a=float(a); vals.append((y,a))
    if not vals: continue
    mean = sum(v for _,v in vals)/len(vals)
    ms = sum(sov[y] for y,_ in vals)/len(vals)
    out.append(f"{co}: years {vals[0][0]}-{vals[-1][0]}; pre-tax EBIT/avg capital by year: " + ', '.join(f'{y} {v:.1%}' for y,v in vals))
    out.append(f"   mean pre-tax {mean:.1%}; after 34% {mean*0.66:.1%}; mean year-end long NTN-F over the same years {ms:.1f}%")
# Localiza without goodwill in capital from 2022 (business view, M2011-060)
lz=[r for r in rows if r['company']=='Localiza']
prev=None; vals=[]
for r in lz:
    cap=float(r['capital_BRLm'])-float(r['intangibles_BRLm']); y=int(r['year'])
    if prev: vals.append((y,float(r['EBIT_BRLm'])/((cap+prev)/2)))
    prev=cap
mean=sum(v for _,v in vals)/len(vals)
out.append("Localiza, capital less intangibles and goodwill: "+', '.join(f'{y} {v:.1%}' for y,v in vals)+f"; mean {mean:.1%}, after 34% {mean*0.66:.1%}")
print('\n'.join(out)); open('q2_returns.txt','w').write('\n'.join(out)+'\n')
