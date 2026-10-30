import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
bs=json.load(open('bs_parsed.json')); x=json.load(open('xbrl_series.json'))
cfacts=json.load(open('companyfacts.json'))['facts']['us-gaap']
def inst(tag):
    s={}
    for u,v in cfacts[tag]['units'].items():
        for f in sorted(v,key=lambda f:f['filed']):
            if f['form']=='10-K' and f['end'][5:]=='12-31' and 'start' not in f: s[int(f['end'][:4])]=f['val']/1e6
    return s
inv=inst('InventoryNetOfAllowancesCustomerAdvancesAndProgressBillings'); bix=inst('BillingsInExcessOfCostCurrent')
B={}
files={2011:'tenk_FY2011.txt'}
for y in range(2011,2026):
    fn='tenk25_hii-20251231.htm.txt' if y==2025 else f'tenk_FY{y}.txt'
    B[y]={k:v[0] for k,v in bs[fn].items()}
    if y-1>=2010 and y-1 not in B: B[y-1]={k:v[1] for k,v in bs[fn].items()}
rev={2011:6575,2012:6708,2013:6820,2014:6957,2015:7020,2016:7068,2017:7441,2018:8176,2019:8899,2020:9361,2021:9524,2022:10676,2023:11454,2024:11535,2025:12484}
soi={2011:122,2012:457,2013:567,2014:585,2015:667,2016:715,2017:688,2018:663,2019:631,2020:555,2021:683,2022:712,2023:842,2024:573,2025:717}
oi={y:v[1] for y,v in ((int(k),v) for k,v in x['OperatingIncomeLoss'].items())}
ni={y:v[1] for y,v in ((int(k),v) for k,v in x['NetIncomeLoss'].items())}
pti={y:v[1] for y,v in ((int(k),v) for k,v in x['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'].items())}
def g(y,k): return B.get(y,{}).get(k,0.0)
def ntoa(y):
    # net tangible operating assets: PP&E + receivables + contract assets + inventories - trade payables - contract liabilities/billings in excess
    cl=g(y,'contract_liab') or bix.get(y,0)
    return g(y,'ppe')+g(y,'ar')+g(y,'contract_assets')+inv.get(y,0)-g(y,'tap')-cl
def netcap(y): return g(y,'equity')+g(y,'ltd')+g(y,'cur_ltd')-g(y,'cash')
print('FY rev soi soi% oi ni ntoa avg_ntoa soi/ntoa  netcap roc(pti+int?) roe')
rows=[]
for y in range(2012,2026):
    a=(ntoa(y)+ntoa(y-1))/2; e=(g(y,'equity')+g(y,'equity') if False else (g(y,'equity')+g(y-1,'equity'))/2); nc=(netcap(y)+netcap(y-1))/2
    r=dict(y=y,rev=rev[y],soi=soi[y],m=soi[y]/rev[y],oi=oi[y],ni=ni[y],ntoa=ntoa(y),r_ntoa=soi[y]/a,nc=netcap(y),r_nc=oi[y]/nc,roe=ni[y]/e,eq=g(y,'equity'))
    rows.append(r)
    print(f"{y} {rev[y]:6.0f} {soi[y]:4.0f} {100*r['m']:4.1f}% oi {oi[y]:4.0f} ni {ni[y]:4.0f} ntoa {r['ntoa']:6.0f} soi/avgNTOA {100*r['r_ntoa']:5.1f}% netcap {r['nc']:6.0f} oi/avgnetcap {100*r['r_nc']:5.1f}% roe {100*r['roe']:5.1f}% eq {r['eq']:.0f}")
S=lambda k,ys: sum(r[k] for r in rows if r['y'] in ys)
ys=range(2012,2026)
print('2012-25 soi/rev', S('soi',ys)/S('rev',ys))
ys2=range(2021,2026); print('2021-25 soi/rev', S('soi',ys2)/S('rev',ys2))
ys3=range(2012,2021); print('2012-20 soi/rev', S('soi',ys3)/S('rev',ys3))
print('ntoa by year', {y:round(ntoa(y)) for y in range(2011,2026)})
print('inv',inv); print('bix',bix)
json.dump(rows,open('roc_rows.json','w'))
