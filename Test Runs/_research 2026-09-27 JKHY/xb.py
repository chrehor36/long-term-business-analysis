import json,sys
sys.stdout.reconfigure(encoding='utf-8')
f=json.load(open('companyfacts.json'))['facts']['us-gaap']
def ann(tag, flow=True):
    out={}
    if tag not in f: return out
    for v in f[tag]['units'].get('USD',[]):
        if not v.get('form','').startswith('10-K'): continue
        e=v['end']
        if e[5:7]!='06': continue
        if flow:
            s=v.get('start')
            if not s: continue
            m=(int(e[:4])*12+int(e[5:7]))-(int(s[:4])*12+int(s[5:7]))
            if m<11 or m>12: continue
        fy=int(e[:4])
        if fy not in out or v['filed']>out[fy][1]: out[fy]=(v['val'],v['filed'],v['accn'])
    return {k:v[0] for k,v in out.items()}, {k:v for k,v in out.items()}
T=dict(ocf='NetCashProvidedByUsedInOperatingActivities',capex='PaymentsToAcquirePropertyPlantAndEquipment',dev='PaymentsToDevelopSoftware',
 sw1='PaymentsForSoftware',sw2='PaymentsToAcquireSoftware',intang='PaymentsToAcquireIntangibleAssets',acq='PaymentsToAcquireBusinessesNetOfCashAcquired',
 sbc='ShareBasedCompensation',dep='Depreciation',amort='AdjustmentForAmortization',swam='CapitalizedComputerSoftwareAmortization',ccam='CapitalizedContractCostAmortization',
 rev1='Revenues',rev2='RevenueFromContractWithCustomerExcludingAssessedTax',opi='OperatingIncomeLoss',ni='NetIncomeLoss',tax='IncomeTaxExpenseBenefit',taxpaid='IncomeTaxesPaid',taxpaid2='IncomeTaxesPaidNet',
 div='PaymentsOfDividends',buy='PaymentsForRepurchaseOfCommonStock',dtax='DeferredFederalIncomeTaxExpenseBenefit',procsale='ProceedsFromSaleOfPropertyPlantAndEquipment')
B=dict(eq='StockholdersEquity',gw='Goodwill',oint='OtherIntangibleAssetsNet',sw='CapitalizedComputerSoftwareNet',ppe='PropertyPlantAndEquipmentNet',ta='LiabilitiesAndStockholdersEquity',debt='LongTermDebt',debt2='LongTermDebtAndCapitalLeaseObligations',debtc='LongTermDebtCurrent')
D={}
for k,t in T.items(): D[k]=ann(t)[0] if ann(t) else {}
for k,t in B.items(): D[k]=ann(t,False)[0] if ann(t,False) else {}
json.dump({k:{str(y):v for y,v in d.items()} for k,d in D.items()},open('xb.json','w'),indent=0)
yrs=range(2007,2027)
keys=list(T)+list(B)
print('FY   '+' '.join(f'{k[:7]:>8}' for k in keys))
for y in yrs:
    print(y, ' '.join(f'{(D[k].get(y,0) or 0)/1e6:8.1f}' if y in D[k] else '       -' for k in keys))
