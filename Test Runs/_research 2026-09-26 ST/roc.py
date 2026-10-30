import json
b=json.load(open('bs_is.json'))
opinc={2008:79.95,2009:58.5,2010:228.9,2011:294.1,2012:277.5,2013:363.5,2014:371.6,2015:393.6,2016:492.4,2017:555.8,2018:710.4,2019:556.9,2020:337.7,2021:633.2,2022:670.1,2023:181.7,2024:149.3,2025:237.5}
imp={2008:13.2,2009:19.9,2023:321.7,2024:150.1,2025:225.7}
restr={2008:24.1,2009:18.1,2010:-0.1,2011:15.0}
def g(fy,k,i):
    r=b[str(fy)]; v=r[k][i]; return v/1000 if r['scale']==1000 else v
bal={}
for fy in range(2010,2026):
    bal[fy]={k:g(fy,k,0) for k in ['ppe','ar','inv','ap','gw','intg','eq']}
bal[2009]={k:g(2010,k,1) for k in ['ppe','ar','inv','ap','gw','intg','eq']}
rev={};cor={};am={}
for fy in range(2010,2026):
    rev[fy]=g(fy,'rev',0); cor[fy]=g(fy,'cor',0); am[fy]=g(fy,'amort',0)
    if fy>=2012: restr.setdefault(fy,g(fy,'restr',0))
for fy,i in [(2009,1),(2008,2)]:
    rev[fy]=g(2010,'rev',i); cor[fy]=g(2010,'cor',i); am[fy]=g(2010,'amort',i)
print('FY | rev | GM | GAAP OM | OM pre-amort/imp/restr | pre-tax on avg NTOA | on avg total op capital | ROE(avg) ')
out=[]
ni={2010:130.1,2011:6.5,2012:177.5,2013:188.1,2014:283.7,2015:347.7,2016:262.4,2017:408.4,2018:599.0,2019:282.7,2020:164.3,2021:363.6,2022:310.7,2023:-3.9,2024:128.5,2025:31.3}
for fy in range(2008,2026):
    adj=opinc[fy]+am[fy]+imp.get(fy,0)+restr.get(fy,0)
    line=f'{fy} | {rev[fy]:.1f} | {(rev[fy]-cor[fy])/rev[fy]*100:.1f}% | {opinc[fy]/rev[fy]*100:.1f}% | {adj/rev[fy]*100:.1f}%'
    if fy>=2010:
        nt=lambda y: bal[y]['ppe']+bal[y]['ar']+bal[y]['inv']-bal[y]['ap']
        tc=lambda y: nt(y)+bal[y]['gw']+bal[y]['intg']
        a=(nt(fy)+nt(fy-1))/2; c=(tc(fy)+tc(fy-1))/2
        e=(bal[fy]['eq']+bal[fy-1]['eq'])/2
        line+=f' | {adj/a*100:.1f}% (NTOA {nt(fy):.0f}) | {(opinc[fy]+imp.get(fy,0)+restr.get(fy,0))/c*100:.1f}% | {ni[fy]/e*100:.1f}%'
    out.append(line)
print('\n'.join(out)); open('roc_out.txt','w').write('\n'.join(out))
