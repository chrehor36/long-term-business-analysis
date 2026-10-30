import json
def series(fn,tag,instant):
    g=json.load(open(fn))['facts']['us-gaap']; d={}
    if tag not in g: return d
    for v in g[tag]['units'].get('USD',[]):
        if not v.get('form','').startswith('10-K'): continue
        if instant:
            if v.get('end','').endswith('12-31'): d.setdefault(int(v['end'][:4]),v['val']/1e6)
        else:
            if v.get('end','').endswith('12-31') and v.get('start','')[5:]=='01-01' and v['start'][:4]==v['end'][:4]: d.setdefault(int(v['end'][:4]),v['val']/1e6)
    return d
for t,fn in [('WSC','facts.json'),('MINI','peers/MINI_facts.json'),('MGRC','peers/MGRC_facts.json'),('URI','peers/URI_facts.json'),('TH','peers/TH_facts.json')]:
    op=series(fn,'OperatingIncomeLoss',0); a=series(fn,'Assets',1); gw=series(fn,'Goodwill',1)
    it=series(fn,'IntangibleAssetsNetExcludingGoodwill',1)
    for k,v in series(fn,'FiniteLivedIntangibleAssetsNet',1).items(): it.setdefault(k,v)
    rev={}
    for tag in ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet']:
        for k,v in series(fn,tag,0).items(): rev.setdefault(k,v)
    row=[]
    for y in range(2012,2026):
        if y in op and a.get(y):
            ta=a[y]-gw.get(y,0)-it.get(y,0)
            row.append(f"{y}: op {op[y]:.0f} / TA {ta:.0f} = {100*op[y]/ta:.1f}% ; margin {100*op[y]/rev[y]:.1f}%" if rev.get(y) else f"{y}: op {op[y]:.0f} / TA {ta:.0f} = {100*op[y]/ta:.1f}%")
    print(t); print('\n'.join(row)); print()
