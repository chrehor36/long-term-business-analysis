import json
x=json.load(open('xbrl_series.json'))
def g(t,k):
    v=x.get(t,{}).get(k); return v[0]/1e6 if v else None
ends=sorted(set(x['GrossProfit'])|set(x['StockholdersEquity']))
print('end        rev     GP    GM%   OI    OM%   NI    OCF   SBC   D&A   capex  equity  buyback div  taxpaid')
for k in ends:
    rev=g('RevenueFromContractWithCustomerExcludingAssessedTax',k) or g('SalesRevenueNet',k)
    gp=g('GrossProfit',k); oi=g('OperatingIncomeLoss',k)
    div=g('PaymentsOfDividendsCommonStock',k) or g('PaymentsOfDividends',k)
    f=lambda v:('%7.1f'%v) if v is not None else '   -   '
    print(k, f(rev), f(gp), ('%5.1f'%(100*gp/rev) if gp and rev else '  -  '), f(oi), ('%5.1f'%(100*oi/rev) if oi and rev else '  -  '), f(g('NetIncomeLoss',k)), f(g('NetCashProvidedByUsedInOperatingActivities',k)), f(g('ShareBasedCompensation',k)), f(g('DepreciationDepletionAndAmortization',k)), f(g('PaymentsToAcquirePropertyPlantAndEquipment',k)), f(g('StockholdersEquity',k)), f(g('PaymentsForRepurchaseOfCommonStock',k)), f(div), f(g('IncomeTaxesPaidNet',k)))
