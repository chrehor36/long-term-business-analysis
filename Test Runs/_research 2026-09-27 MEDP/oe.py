import json
x=json.load(open('xb_rows.json')); g=lambda k,y: x[k].get(str(y),0)/1e6
CAP=17273.965; SOV=5.49
# pre-XBRL years from the 424B4 (thousands): 2013 predecessor; 2014 = predecessor Q1 + successor 9M
rows={}
rows[2013]=dict(ocf=98.142,sbc=1.958,cx=4.561,dep=6.665,dadv=None,dtax=None,note='424B4 predecessor')
rows[2014]=dict(ocf=12.807+62.539,sbc=7.340+3.057,cx=1.090+4.225,dep=1.832+4.610,dadv=6.330+10.651,dtax=None,note='424B4 Q1 predecessor + 9M successor')
for y in range(2015,2026):
    ocf=g('OCF',y) or g('OCFc',y)
    dadv=g('dCWCL',y) if str(y) in x['dCWCL'] else g('dDefRev',y)
    rows[y]=dict(ocf=ocf,sbc=g('SBC',y),cx=g('Capex',y),dep=g('Dep',y),dadv=dadv,dtax=None,note='companyfacts/10-K')
dtax={2015:-12.7,2016:-9.0,2017:3.2,2018:3.9,2019:10.1,2020:0.5,2021:-37.1,2022:-23.0,2023:-25.0,2024:-26.6,2025:80.9}
for y,v in dtax.items(): rows[y]['dtax']=v
# TTM to 2026-06-30
rows['TTM']=dict(ocf=713.223-274.362+313.799,sbc=34.786-22.843+9.266,cx=31.356-16.107+30.725,dep=27.178-13.471+13.306,dadv=143.805-98.198+50.332,dtax=80.773-34.9+22.8,note='10-K FY2025 + 10-Q H1 2026 - 10-Q H1 2025')
out=[]
print('FY | OCF | SBC | capex | depreciation | chg advanced billings | deferred tax | OE capex end | OE D&A end | OE capex end, advances change removed | SBC/OCF')
for y in list(range(2013,2026))+['TTM']:
    r=rows[y]; a=r['ocf']-r['sbc']-r['cx']; b=r['ocf']-r['sbc']-r['dep']
    c=a-(r['dadv'] or 0) if r['dadv'] is not None else None
    r.update(oe_cx=a,oe_da=b,oe_noadv=c)
    print(f"{y} | {r['ocf']:.1f} | {r['sbc']:.1f} | {r['cx']:.1f} | {r['dep']:.1f} | {r['dadv'] if r['dadv'] is None else round(r['dadv'],1)} | {r['dtax']} | {a:.1f} | {b:.1f} | {'' if c is None else round(c,1)} | {100*r['sbc']/r['ocf']:.1f}%")
json.dump({str(k):v for k,v in rows.items()},open('oe_rows.json','w'),indent=1)
print()
ys=list(range(2013,2026))
def win(n,end=2025,key='oe_cx',adj=None):
    yy=[y for y in ys if end-n<y<=end]
    vals=[rows[y][key]-(adj(y) if adj else 0) for y in yy]
    return sum(vals)/len(vals)
print('window | capex end | D&A end | yield | advances change removed (capex end) | tax-normalized capex end | D&A end')
taxadj=lambda y: (rows[y]['dtax'] or 0) if y==2025 else 0
for n in range(1,14):
    a=win(n); b=win(n,key='oe_da'); c=win(n,key='oe_noadv') if n<=12 else None
    t1=win(n,adj=taxadj); t2=win(n,key='oe_da',adj=taxadj)
    print(f"{n}y ({2026-n}-2025) | {a:.1f} | {b:.1f} | {100*a/CAP:.2f}-{100*b/CAP:.2f}% | {'' if c is None else round(c,1)} | {t1:.1f} | {t2:.1f} | {100*t1/CAP:.2f}-{100*t2/CAP:.2f}%")
# tax-neutral: 2021-2025 sum of deferred tax
for (s,e) in [(2021,2025),(2022,2025),(2023,2025)]:
    yy=range(s,e+1); print('deferred tax sum',s,e,round(sum(rows[y]['dtax'] for y in yy),1))
# rolling 5y
print('\nrolling five-year means, capex end / D&A end / advances removed')
for e in range(2017,2026):
    print(e-4,e, round(win(5,e),1), round(win(5,e,'oe_da'),1), round(win(5,e,'oe_noadv'),1) if e-4>=2014 else '')
print('\nall trailing windows min/max, both ends, as filed:')
vals=[win(n,key=k) for n in range(1,14) for k in ('oe_cx','oe_da')]
print(round(min(vals),1), round(max(vals),1), '%.2f-%.2f%%'%(100*min(vals)/CAP,100*max(vals)/CAP))
t=rows['TTM']; print('TTM', round(t['oe_cx'],1), round(t['oe_da'],1), 'tax-adj', round(t['oe_cx']-t['dtax'],1), round(t['oe_da']-t['dtax'],1))
