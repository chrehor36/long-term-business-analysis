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
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
GP=['GrossProfit']; COGS=['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold']
OI=['OperatingIncomeLoss']
EQ=['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','StockholdersEquity']
DEBT=['LongTermDebtNoncurrent','LongTermDebtCurrent','LongTermDebtAndCapitalLeaseObligations','LongTermDebtAndCapitalLeaseObligationsCurrent','ShortTermBorrowings','LoansPayableToBankCurrent','DebtCurrent','LineOfCredit','ShortTermBankLoansAndNotesPayable','LongTermDebt']
CASH=['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations']
STI=['ShortTermInvestments']
out={}
for t in sys.argv[1:]:
    j=load(t+'_facts.json')
    rev={};[rev.setdefault(k,v) for tg in REV for k,v in ser(j,[tg]).items()]
    # prefer the tag with the most coverage per period: take max value among revenue tags per period
    revm={}
    for tg in REV:
        for k,v in ser(j,[tg]).items():
            if k not in revm or v[0]>revm[k][0]: revm[k]=v
    gp=ser(j,GP); cogs={}
    for tg in COGS:
        for k,v in ser(j,[tg]).items(): cogs.setdefault(k,v)
    oi=ser(j,OI); eq={}
    for tg in EQ:
        for k,v in ser(j,[tg],True).items(): eq.setdefault(k,v)
    cash={}
    for tg in CASH:
        for k,v in ser(j,[tg],True).items(): cash.setdefault(k,v)
    sti=ser(j,STI,True)
    dt={}
    for tg in ['LongTermDebtNoncurrent','LongTermDebtCurrent','ShortTermBorrowings','LoansPayableToBankCurrent','ShortTermBankLoansAndNotesPayable','LineOfCredit','DebtCurrent']:
        for k,v in ser(j,[tg],True).items(): dt[k]=dt.get(k,0)+v[0]
    rows=[]
    for k in sorted(revm):
        r=revm[k][0]/1e6
        g=gp[k][0]/1e6 if k in gp else (r-cogs[k][0]/1e6 if k in cogs else None)
        o=oi[k][0]/1e6 if k in oi else None
        cap=None
        if k in eq:
            cap=eq[k][0]/1e6+dt.get(k,0)/1e6-(cash[k][0]/1e6 if k in cash else 0)-(sti[k][0]/1e6 if k in sti else 0)
        rows.append((k,r,g,o,cap))
    out[t]=rows
    print('==',t)
    prev=None
    for k,r,g,o,cap in rows:
        gr='' if prev is None else '%+.1f%%'%(100*(r/prev-1)); prev=r
        print(k,'rev %.1f'%r,gr,'GM %s'%('%.1f%%'%(100*g/r) if g else '-'),'OM %s'%('%.1f%%'%(100*o/r) if o is not None else '-'),'OI/netopcap %s'%('%.1f%%'%(100*o/cap) if (o is not None and cap and cap>0) else ('neg' if cap is not None and cap<=0 else '-')), 'netopcap %s'%('%.0f'%cap if cap is not None else '-'))
json.dump(out,open('row_all.json','w'),indent=0)
