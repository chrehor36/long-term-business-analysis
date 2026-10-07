import json
S=json.load(open('xbrl_series.json'))
# filed-statement values for FY2006-2009 (FY2008/FY2009 10-K, thousands->millions); 2007 continuing ops balance sheet
extra={'rev':{'2006-08-31':1841.039,'2007-08-31':1964.781,'2008-08-31':2026.644},
 'gp':{'2006-08-31':652.837,'2007-08-31':744.315,'2008-08-31':815.795},
 'oi':{'2006-08-31':152.119,'2007-08-31':222.423,'2008-08-31':261.060},
 'ar':{'2007-08-31':295.544,'2008-08-31':268.971,'2009-08-31':227.371},
 'inv':{'2007-08-31':146.536,'2008-08-31':145.725,'2009-08-31':140.797},
 'ppe':{'2007-08-31':162.011,'2008-08-31':161.506,'2009-08-31':145.829},
 'ap':{'2007-08-31':210.402,'2008-08-31':205.776,'2009-08-31':162.299},
 'gw':{'2007-08-31':352.945,'2008-08-31':342.306,'2009-08-31':510.563},
 'intang':{'2007-08-31':118.774,'2008-08-31':129.319,'2009-08-31':184.826},
 'eq':{'2007-08-31':671.966}}
for k,v in extra.items():
    for d,x in v.items(): S[k].setdefault(d,x)
amort={2006:3.2,2007:3.2,2008:3.7,2009:5.4,2010:7.1}
for d,v in json.load(open('companyfacts.json'))['facts']['us-gaap']['AmortizationOfIntangibleAssets']['units']['USD'] and []: pass
A={2011:10.2,2012:11.2,2013:10.9,2014:11.2,2015:11.0,2016:21.4,2017:28.0,2018:28.5,2019:30.8,2020:41.7,2021:40.7,2022:41.0,2023:42.1,2024:39.7,2025:76.5}
amort.update(A)
rows=[]
print('FY   rev    gm%   om%   ntoa  preRoNTOA  RoTotalOpCap  ROE')
for y in range(2006,2026):
    d=f'{y}-08-31'; p=f'{y-1}-08-31'
    rev=S['rev'].get(d); gp=S['gp'].get(d); oi=S['oi'].get(d)
    def ntoa(dd):
        try: return S['ppe'][dd]+S['ar'][dd]+S['inv'][dd]-S['ap'][dd]
        except KeyError: return None
    n1,n0=ntoa(d),ntoa(p)
    avg=(n1+n0)/2 if n1 and n0 else None
    op=oi+amort[y]
    r1=op/avg if avg else None
    tc=lambda dd:(ntoa(dd)+S['gw'][dd]+S['intang'][dd]) if ntoa(dd) and dd in S['gw'] and dd in S['intang'] else None
    t1,t0=tc(d),tc(p); rt=oi/((t1+t0)/2) if t1 and t0 else None
    e1,e0=S['eq'].get(d),S['eq'].get(p); ni=S['ni'].get(d)
    roe=ni/((e1+e0)/2) if (ni and e1 and e0) else None
    f=lambda x:f'{x*100:6.1f}' if x is not None else '     -'
    print(y,f'{rev:7.1f}',f(gp/rev),f(oi/rev),f'{n1:7.1f}' if n1 else '      -',f(r1),f(rt),f(roe))
    rows.append(dict(fy=y,rev=rev,gm=gp/rev,om=oi/rev,ntoa=n1,ro_ntoa=r1,ro_tc=rt,roe=roe))
json.dump(rows,open('roc_rows.json','w'),indent=1)
