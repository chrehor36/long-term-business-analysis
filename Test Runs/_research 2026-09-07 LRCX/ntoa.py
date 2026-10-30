import json,datetime
d=json.load(open('companyfacts_LRCX.json'))
us=d['facts']['us-gaap']
def ann(tag,unit='USD',dur=True):
    out={}
    if tag not in us: return out
    for it in us[tag]['units'].get(unit,[]):
        if it.get('form') not in ('10-K',): continue
        if it.get('fp')!='FY': continue
        st=it.get('start'); en=it['end']
        if dur:
            if not st: continue
            s=datetime.date.fromisoformat(st); e=datetime.date.fromisoformat(en)
            if not (330<=(e-s).days<=400): continue
        else:
            if st: continue
        if en not in out or it['accn']>out[en][1]: out[en]=(it['val'],it['accn'])
    return {k:v[0]/1e6 for k,v in out.items()}
rev=dict(ann('SalesRevenueNet')); rev.update(ann('Revenues')); rev.update(ann('RevenueFromContractWithCustomerExcludingAssessedTax'))
gp=ann('GrossProfit'); rd=ann('ResearchAndDevelopmentExpense'); sga=ann('SellingGeneralAndAdministrativeExpense')
op=ann('OperatingIncomeLoss')
assets=ann('Assets',dur=False); cl=ann('LiabilitiesCurrent',dur=False)
cash=ann('CashAndCashEquivalentsAtCarryingValue',dur=False); sti=ann('ShortTermInvestments',dur=False)
gw=ann('Goodwill',dur=False); ia=ann('FiniteLivedIntangibleAssetsNet',dur=False)
gwi=ann('IntangibleAssetsNetIncludingGoodwill',dur=False)
curdebt=ann('LongTermDebtCurrent',dur=False)
ltinv=ann('LongTermInvestments',dur=False)
print('year rev GM% OP OPm% assets CL cash sti gw ia gwi curdebt ltinv')
for y in sorted(set(list(rev)+list(assets))):
    print(y, round(rev.get(y,0),1), round(gp.get(y,0)/rev[y]*100,1) if y in rev and y in gp and rev[y] else '', round(op.get(y,0),1),
          round(op.get(y,0)/rev[y]*100,1) if y in rev and y in op and rev[y] else '',
          round(assets.get(y,0),1), round(cl.get(y,0),1), round(cash.get(y,0),1), round(sti.get(y,0),1),
          round(gw.get(y,0),1), round(ia.get(y,0),1), round(gwi.get(y,0),1), round(curdebt.get(y,0),1), round(ltinv.get(y,0),1))
