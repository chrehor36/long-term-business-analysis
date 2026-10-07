import json
P=json.load(open('raw/_cna_parsed.json'))
segs=['Specialty','Commercial','International']
def g(y,s,keys,col=0):
    r=P[f"{y}|{s}"]['rows']
    for k in keys:
        for lab,v in r.items():
            if lab.startswith(k): return v[col]
    return 0.0 if 'Dividend' in keys[0] else None
cat={2016:(18,116,31),2017:(49,267,64),2018:(26,193,33),2019:(15,154,10),2020:(125,358,67),2021:(12,358,27),2022:(2,222,23),2023:(0,207,29),2024:(0,318,40),2025:(0,217,23)}
cat_tot={2016:165,2017:380,2018:252,2019:179,2020:550,2021:397,2022:247,2023:236,2024:358,2025:240}
# Note E claim reserve development, three P&C segments, own-year 10-K (2017 from FY2017 10-K)
pyd={2016:(-287,55,-58),2017:(-202,-87,-9),2018:(-150,-25,-4),2019:(-92,-2,21),2020:(-61,43,-2),2021:(-45,-6,2),2022:(-40,-43,-13),2023:(-14,-22,13),2024:(-9,-16,-6),2025:(37,39,-25)}
und_rep={2019:(93.0,95.2,98.6)}  # from FY2020 10-K comparative column
uw={}
out={}
for y in range(2016,2026):
    nep=[g(y,s,['Net earned premiums']) for s in segs]
    cr=[g(y,s,['Combined ratio |','Combined ratio']) for s in segs]
    # combined ratio exact label
    cr=[P[f"{y}|{s}"]['rows']['Combined ratio'][0] for s in segs]
    er=[P[f"{y}|{s}"]['rows']['Expense ratio'][0] for s in segs]
    dr=[P[f"{y}|{s}"]['rows'].get('Dividend ratio',[0.0])[0] for s in segs]
    und=None
    for k in ('Underlying combined ratio','Combined ratio excluding catastrophes and development'):
        if k in P[f"{y}|Specialty"]['rows']:
            und=[P[f"{y}|{s}"]['rows'][k][0] for s in segs]
    if y in und_rep: und=list(und_rep[y])
    uwg=None
    for k in ('Underwriting gain','Underwriting gain (loss)','Underwriting (loss) gain'):
        pass
    uwl=[]
    for s in segs:
        r=P[f"{y}|{s}"]['rows']; v=[r[k][0] for k in r if k.startswith('Underwriting')]
        uwl.append(v[0] if v else None)
    N=sum(nep)
    w=lambda xs: sum(a*b for a,b in zip(xs,nep))/N
    crw=w(cr); erw=w(er); drw=w(dr)
    catpts=cat_tot[y]/N*100; pydpts=sum(pyd[y])/N*100
    o=dict(nep=nep,N=N,cr=cr,crw=round(crw,2),er=er,erw=round(erw,2),drw=round(drw,2),cat=cat[y],cat_tot=cat_tot[y],catpts=round(catpts,2),pyd=pyd[y],pydsum=sum(pyd[y]),pydpts=round(pydpts,2),
           und_seg=und,und_w=round(w(und),2) if und else None,und_calc=round(crw-catpts-pydpts,2),uw=uwl)
    if None not in uwl: o['uw_sum']=sum(uwl); o['cr_from_uw']=round(100-sum(uwl)/N*100,2)
    out[y]=o
    print(y,o)
json.dump(out,open('raw/_cna_calc.json','w'),indent=0)
# ROE
roe={2016:(859,11756,11969),2017:(899,11969,12244),2018:(813,12244,11217),2019:(1000,11217,12215),2020:(690,12215,12707),2021:(1202,12707,12809),2022:(894,12809,8825),2023:(1205,8548,9893),2024:(959,9893,10513),2025:(1278,10513,11621)}
for y,(ni,b,e) in roe.items(): print(y,ni,b,e,round(ni/((b+e)/2)*100,2))
print('2022 restated LDTI',round(682/((11105+8548)/2)*100,2))
