import json,sys
sys.stdout.reconfigure(encoding='utf-8')
f=json.load(open('cache/facts.json'))['facts']['us-gaap']
def ann(tag):
    out={}
    for u,v in f.get(tag,{}).get('units',{}).items():
        for x in v:
            if x.get('form','').startswith('10-K') and x.get('start','')[5:]=='01-01' and x['end'][5:]=='12-31' and x['start'][:4]==x['end'][:4]:
                y=x['end'][:4]
                if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'])
    return {k:v[0] for k,v in out.items()}
rev={**ann('SalesRevenueNet'),**ann('RevenueFromContractWithCustomerExcludingAssessedTax')}
gp=ann('GrossProfit'); oi=ann('OperatingIncomeLoss'); sm=ann('SellingAndMarketingExpense'); ga=ann('GeneralAndAdministrativeExpense')
for y in sorted(rev):
    r=rev[y]; print(y, f"rev {r/1e6:6.1f} GM {100*gp[y]/r:5.1f}% OM {100*oi[y]/r:5.1f}% S&M {100*sm[y]/r:4.1f}% RG&A {100*ga[y]/r:4.1f}%")
