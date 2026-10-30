import pickle
P=pickle.load(open('cache/peers.pkl','rb'))
def g(t,tag,fy):
    v=P[t].get((tag,str(fy))); return v[0]/1e6 if v else None
REV={'CLF':'Revenues','NUE':'RevenueFromContractWithCustomerExcludingAssessedTax','STLD':'RevenueFromContractWithCustomerExcludingAssessedTax','X':'Revenues'}
PT={'CLF':'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','NUE':'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','STLD':'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','X':'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'}
INT={'CLF':'InterestPaidNet','NUE':'InterestExpense','STLD':'InterestPaidNet','X':'InterestExpense'}
DEBT={'CLF':'LongTermDebtNoncurrent','NUE':None,'STLD':'LongTermDebt','X':'LongTermDebt'}
print("Pretax margin by year (pretax income / revenue), %")
for t in P:
    row=[]
    for fy in range(2015,2026):
        r=g(t,REV[t],fy) or g(t,'SalesRevenueNet',fy) or g(t,'Revenues',fy); p=g(t,PT[t],fy)
        if p is None: p=g(t,'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments',fy)
        row.append(f"{100*p/r:7.1f}" if (r and p is not None) else "      -")
    print(t, ' '.join(row))
print("years 2015..2025")
def span(t,a,b):
    R=P_=0
    for fy in range(a,b+1):
        r=g(t,REV[t],fy) or g(t,'SalesRevenueNet',fy) or g(t,'Revenues',fy); p=g(t,PT[t],fy)
        if p is None: p=g(t,'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments',fy)
        if r is None or p is None: return None
        R+=r;P_+=p
    return 100*P_/R, P_, R
for t in P:
    for a,b in [(2020,2025),(2020,2024),(2016,2025),(2021,2025)]:
        s=span(t,a,b)
        if s: print(t,a,b,"aggregate pretax margin %.1f%% (pretax %.0f on revenue %.0f)"%s)
# pretax+interest over equity+LTD, 2021-2025 average
print("Pretax income plus interest, over shareholders' equity plus long-term debt (year-end), %")
for t in P:
    row=[]
    for fy in range(2016,2026):
        p=g(t,PT[t],fy); i=g(t,INT[t],fy) or g(t,'InterestExpenseNonoperating',fy) or 0
        e=g(t,'StockholdersEquity',fy); d=g(t,DEBT[t],fy) if DEBT[t] else None
        if d is None: d=g(t,'LongTermDebtNoncurrent',fy) or g(t,'LongTermDebt',fy)
        if p is None or e is None or d is None: row.append("      -"); continue
        row.append(f"{100*(p+i)/(e+d):7.1f}")
    print(t,' '.join(row))
print("years 2016..2025")
for t in P:
    acc=sorted(set((v[2],k[1]) for k,v in P[t].items() if k[1] in ('2025','2024')))
    print(t,acc[-3:])
