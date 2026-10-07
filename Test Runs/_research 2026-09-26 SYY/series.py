import json,sys
f=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'companyfacts.json'))['facts']['us-gaap']
def ann(tags, inst=False):
    out={}
    for t in tags:
        d=f.get(t)
        if not d: continue
        for u,v in d['units'].items():
            if u!='USD': continue
            for x in v:
                if x.get('form') not in ('10-K','10-K/A'): continue
                if not inst:
                    if 'start' not in x: continue
                    from datetime import date
                    s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                    if not 350<=(e-s).days<=380: continue
                fy=int(x['end'][:4]) if x['end'][5:7]>'03' else int(x['end'][:4])-1
                key=x['end']
                # newest vintage: later filed wins
                if key not in out or x['filed']>out[key][1]: 
                    if key in out and out[key][2]!=t and tags.index(out[key][2])<tags.index(t): continue
                    out[key]=(x['val'],x['filed'],t)
    return out
rows={
 'sales':ann(['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet']),
 'gp':ann(['GrossProfit']),
 'oi':ann(['OperatingIncomeLoss']),
 'eq':ann(['StockholdersEquity'],True),
 'cash':ann(['CashAndCashEquivalentsAtCarryingValue'],True),
 'gw':ann(['Goodwill'],True),
 'intg':ann(['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],True),
 'ltd':ann(['LongTermDebtNoncurrent','LongTermDebtAndCapitalLeaseObligations'],True),
 'std':ann(['LongTermDebtCurrent','DebtCurrent','ShortTermBorrowings','LongTermDebtAndCapitalLeaseObligationsCurrent'],True),
}
ends=sorted(rows['oi'].keys())
print('end        sales    gp    gm%   oi   om%   eq   cash  gw  intg  ltd  std')
for e in ends:
    g=lambda k:(rows[k].get(e,(None,))[0] or 0)/1e6
    s=g('sales'); 
    print(e, f"{s:8.0f} {g('gp'):7.0f} {100*g('gp')/s if s else 0:5.2f} {g('oi'):6.0f} {100*g('oi')/s if s else 0:5.2f} {g('eq'):7.0f} {g('cash'):6.0f} {g('gw'):6.0f} {g('intg'):6.0f} {g('ltd'):7.0f} {g('std'):6.0f}")
