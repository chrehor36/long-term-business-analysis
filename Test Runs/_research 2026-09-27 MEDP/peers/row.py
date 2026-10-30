import json, datetime, sys
def load(t): return json.load(open(t+'_facts.json'))['facts']
def ser(j, tags, inst=False, forms=('10-K','20-F','10-K/A','10-KT')):
    merged={}; used=set()
    for tag in tags:
        out={}
        for ns in j:
            if tag not in j[ns]: continue
            for u,fs in j[ns][tag]['units'].items():
                if u!='USD' and not u.startswith('USD'): continue
                for f in fs:
                    if f.get('form') not in forms: continue
                    e=f['end']
                    if not inst:
                        if 'start' not in f: continue
                        d=(datetime.date.fromisoformat(e)-datetime.date.fromisoformat(f['start'])).days
                        if d<350 or d>380: continue
                    y=int(e[:4]) if e[5:7]>='06' else int(e[:4])-1
                    if y not in out or f['filed']>out[y][1]: out[y]=(f['val'],f['filed'])
        for y,v in out.items():
            if y not in merged: merged[y]=v[0]; used.add(tag)
    return merged, ','.join(sorted(used)) or None
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueServicesNet','SalesRevenueNet']
OP=['OperatingIncomeLoss']
AM=['AmortizationOfIntangibleAssets','AmortizationOfAcquiredIntangibleAssets']
OCF=['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']
CX=['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets']
SBC=['ShareBasedCompensation','AllocatedShareBasedCompensationExpense']
TA=['Assets']; CASH=['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents']
LIAB=['Liabilities']; GW=['Goodwill']; INT=['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet']
DEBTS=['LongTermDebtNoncurrent','LongTermDebt','LongTermDebtAndCapitalLeaseObligations','LongTermDebtAndCapitalLeaseObligationsCurrent','LongTermDebtCurrent','DebtCurrent','ShortTermBorrowings','LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities','DebtInstrumentCarryingAmount']
ADV=['ContractWithCustomerLiabilityCurrent','ContractWithCustomerLiability','DeferredRevenueCurrent']
AR=['AccountsReceivableNetCurrent','ReceivablesNetCurrent']
UNB=['ContractWithCustomerAssetNetCurrent','UnbilledContractsReceivable','UnbilledReceivablesCurrent']
def debt(j,y):
    # total debt: prefer LongTermDebt (incl current) else noncurrent+current
    a,_=ser(j,['LongTermDebt'],True)
    if y in a: return a[y]
    n,_=ser(j,['LongTermDebtNoncurrent','LongTermDebtAndCapitalLeaseObligations'],True); c,_=ser(j,['LongTermDebtCurrent','LongTermDebtAndCapitalLeaseObligationsCurrent','DebtCurrent'],True)
    return n.get(y,0)+c.get(y,0)
t=sys.argv[1]; j=load(t)
S={}
for k,tags,inst in [('rev',REV,0),('op',OP,0),('am',AM,0),('ocf',OCF,0),('cx',CX,0),('sbc',SBC,0),('ta',TA,1),('cash',CASH,1),('liab',LIAB,1),('gw',GW,1),('int',INT,1),('adv',ADV,1),('ar',AR,1),('unb',UNB,1)]:
    S[k],tg=ser(j,tags,bool(inst)); print('#',k,tg)
ys=sorted(S['rev'])
print('yr   rev   growth  op   am  EBITA%  op%  adv/rev  (ar+unb-adv)/rev*365  NTOA  preTaxRet_exGWint  ret_inclGW  OCF  capex SBC')
prev=None
out={}
for y in ys:
    r=S['rev'][y]; op=S['op'].get(y); am=S['am'].get(y,0) or 0
    if op is None: continue
    ta=S['ta'].get(y); cash=S['cash'].get(y,0); li=S['liab'].get(y); gw=S['gw'].get(y,0); it=S['int'].get(y,0)
    d=debt(j,y)
    ntoa=None; cap=None
    if ta is not None and li is not None:
        cap=ta-cash-(li-d)    # operating capital incl goodwill/intangibles
        ntoa=cap-gw-it
    adv=S['adv'].get(y); ar=S['ar'].get(y); un=S['unb'].get(y,0)
    g=(r/S['rev'][y-1]-1) if (y-1) in S['rev'] else None
    f=lambda x:('%7.1f'%(x/1e6)) if x is not None else '      -'
    p=lambda x:('%6.1f%%'%(100*x)) if x is not None else '     -'
    print(y,f(r),p(g),f(op),f(am),p((op+am)/r),p(op/r),p(adv/r if adv else None),('%6.0f'%(((ar or 0)+un-adv)/r*365)) if adv and ar else '    -',f(ntoa),p((op+am)/ntoa if ntoa and ntoa>0 else None),p(op/cap if cap and cap>0 else None),f(S['ocf'].get(y)),f(S['cx'].get(y)),f(S['sbc'].get(y)))
    out[y]=dict(rev=r,op=op,am=am,ntoa=ntoa,cap=cap,adv=adv,ar=ar,unb=un,ocf=S['ocf'].get(y),cx=S['cx'].get(y),sbc=S['sbc'].get(y))
json.dump(out,open(t+'_row.json','w'))
