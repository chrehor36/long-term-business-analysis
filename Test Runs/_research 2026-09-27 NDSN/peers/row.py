import json, datetime, sys
def load(fn): return json.load(open(fn))['facts']['us-gaap']
def ser(j, tags, inst=False):
    out={}
    for tag in tags:
        if tag not in j: continue
        for u,fs in j[tag]['units'].items():
            if u!='USD': continue
            for f in fs:
                if f.get('form') not in ('10-K','10-K/A','10-KT'): continue
                e=f['end']
                if not inst:
                    if 'start' not in f: continue
                    d=(datetime.date.fromisoformat(e)-datetime.date.fromisoformat(f['start'])).days
                    if d<350 or d>380: continue
                y=e[:7]
                if y not in out or f['filed']>out[y][1]: out[y]=(f['val'],f['filed'],tag)
    return out
def first(j,tags,inst=False):
    d={}
    for tg in tags:
        for k,v in ser(j,[tg],inst).items(): d.setdefault(k,v)
    return d
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
COGS=['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold']
EQ=['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','StockholdersEquity']
CASH=['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations']
INT=['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet']
out={}
for t in sys.argv[1:]:
    j=load(t+'_facts.json')
    revm={}
    for tg in REV:
        for k,v in ser(j,[tg]).items():
            if k not in revm or v[0]>revm[k][0]: revm[k]=v
    gp=ser(j,['GrossProfit']); cogs=first(j,COGS); oi=ser(j,['OperatingIncomeLoss'])
    eq=first(j,EQ,True); cash=first(j,CASH,True); sti=ser(j,['ShortTermInvestments','MarketableSecuritiesCurrent'],True)
    gw=ser(j,['Goodwill'],True); it=first(j,INT,True)
    ltd=ser(j,['LongTermDebt'],True)
    dt={}
    for tg in ['LongTermDebtNoncurrent','LongTermDebtCurrent','ShortTermBorrowings','LoansPayableToBankCurrent','ShortTermBankLoansAndNotesPayable','CommercialPaper','DebtCurrent','LongTermDebtAndCapitalLeaseObligations','LongTermDebtAndCapitalLeaseObligationsCurrent']:
        for k,v in ser(j,[tg],True).items(): dt.setdefault(k,{})[tg]=v[0]
    def debt(k):
        d=dt.get(k,{})
        a=d.get('LongTermDebtNoncurrent',d.get('LongTermDebtAndCapitalLeaseObligations',0))
        b=d.get('LongTermDebtCurrent',d.get('LongTermDebtAndCapitalLeaseObligationsCurrent',0))
        c=d.get('ShortTermBorrowings',0)+d.get('LoansPayableToBankCurrent',0)+d.get('CommercialPaper',0)+d.get('ShortTermBankLoansAndNotesPayable',0)
        if k in ltd and a+b==0: a=ltd[k][0]
        return a+b+c
    rows=[]
    for k in sorted(revm):
        r=revm[k][0]/1e6
        g=gp[k][0]/1e6 if k in gp else (r-cogs[k][0]/1e6 if k in cogs else None)
        o=oi[k][0]/1e6 if k in oi else None
        cap=tcap=None
        if k in eq:
            cap=eq[k][0]/1e6+debt(k)/1e6-(cash[k][0]/1e6 if k in cash else 0)-(sti[k][0]/1e6 if k in sti else 0)
            tcap=cap-(gw[k][0]/1e6 if k in gw else 0)-(it[k][0]/1e6 if k in it else 0)
        rows.append((k,r,g,o,cap,tcap))
    out[t]=rows
    print('==',t, json.load(open(t+'_facts.json'))['entityName'])
    prev=None
    for k,r,g,o,cap,tcap in rows:
        gr='' if prev is None else '%+.1f%%'%(100*(r/prev-1)); prev=r
        f=lambda x,c:('%.1f%%'%(100*x/c) if (x is not None and c and c>0) else ('neg' if c is not None and c<=0 else '-'))
        print(k,'rev %.1f'%r,gr,'GM %s'%('%.1f%%'%(100*g/r) if g else '-'),'OM %s'%('%.1f%%'%(100*o/r) if o is not None else '-'),'OI/opcap %s'%f(o,cap),'OI/tangcap %s'%f(o,tcap),'opcap %s'%('%.0f'%cap if cap is not None else '-'),'tang %s'%('%.0f'%tcap if tcap is not None else '-'))
json.dump(out,open('row_all.json','w'),indent=0)
