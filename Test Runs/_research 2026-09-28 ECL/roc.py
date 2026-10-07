import json, sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')
f=json.load(open('cache/facts.json'))['facts']['us-gaap']
def inst(t):
    o={}
    for u,arr in f.get(t,{}).get('units',{}).items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and 'start' not in x: o[x['end'][:4]]=x['val']/1e6
    return o
def dur(t):
    o={}
    for u,arr in f.get(t,{}).get('units',{}).items():
        for x in arr:
            if x.get('form') in ('10-K','10-K/A') and 'start' in x:
                d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                if 350<=d<=380: o[x['end'][:4]]=x['val']/1e6
    return o
eq=inst('StockholdersEquity'); gw=inst('Goodwill'); cash=inst('CashAndCashEquivalentsAtCarryingValue')
ia=inst('IntangibleAssetsNetExcludingGoodwill'); fl=inst('FiniteLivedIntangibleAssetsNet')
ltd=inst('LongTermDebtAndCapitalLeaseObligations'); ltd2=inst('LongTermDebtNoncurrent'); dc=inst('DebtCurrent')
oi=dur('OperatingIncomeLoss'); rev={**dur('SalesRevenueNet'),**dur('RevenueFromContractWithCustomerExcludingAssessedTax')}
print('FY  OI  rev  OM%  equity debt cash goodwill intang  net_tangible  pretax_ROntc%  net_capital_incl_gw  pretax_ROnc%  ROE_book(OI)')
rows={}
for y in sorted(oi):
    if y<'2008': continue
    debt=ltd.get(y,ltd2.get(y,0))+dc.get(y,0)
    intang=ia.get(y, fl.get(y,0)+ (0))
    ntc=eq[y]+debt-cash[y]-gw[y]-intang
    nc=eq[y]+debt-cash[y]
    rows[y]=(oi[y],rev[y],ntc,nc)
    print(y, f"{oi[y]:.1f} {rev[y]:.1f} {100*oi[y]/rev[y]:.1f} | {eq[y]:.1f} {debt:.1f} {cash[y]:.1f} {gw[y]:.1f} {intang:.1f} | {ntc:.1f} {100*oi[y]/ntc:.1f} | {nc:.1f} {100*oi[y]/nc:.1f}")
