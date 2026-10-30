import re,glob,sys,json
sys.stdout.reconfigure(encoding='utf-8')
files=['cache/k_2025.txt','cache/q2606_cat-20260630.htm.txt','cache/proxy26_cat014496-def14a.htm.txt']+sorted(glob.glob('cache/r20*ex*99*1*.txt')+glob.glob('cache/r20*earning*.txt')+glob.glob('cache/r20*ex991*.txt'))
seen=set()
for f in files:
    if f in seen: continue
    seen.add(f)
    t=open(f,encoding='utf-8').read()
    print(f, 'EBITDA', len(re.findall(r'EBITDA',t,re.I)), 'adjusted', len(re.findall(r'adjusted',t,re.I)))
g=json.load(open('cache/facts.json'))['facts']['us-gaap']
def ann(tag):
    out={}
    for u,v in g[tag]['units'].items():
        for x in v:
            fr=x.get('frame','')
            if len(fr)==6 and x.get('fp')=='FY': out[int(fr[2:])]=x['val']/1e6
    return out
tax=ann('IncomeTaxesPaid'); pre=ann('IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'); pre[2024]=13373; pre[2025]=11541
print('cash tax / pretax:',{y:round(tax[y]/pre[y]*100,1) for y in sorted(tax) if y in pre and pre[y]>500})
r=ann('RestructuringCharges'); print('restructuring',{y:r[y] for y in sorted(r)},'sum 2011-2025',sum(r[y] for y in range(2011,2026)))
