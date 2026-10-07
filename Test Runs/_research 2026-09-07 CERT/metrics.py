import json,sys
from datetime import date
TAGS_D=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax',
 'CostOfRevenue','CostOfGoodsAndServicesSold','GrossProfit','OperatingIncomeLoss','NetIncomeLoss',
 'NetCashProvidedByUsedInOperatingActivities','ShareBasedCompensation','ResearchAndDevelopmentExpense',
 'PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToDevelopSoftware','PaymentsForCapitalImprovements',
 'PaymentsToAcquireIntangibleAssets','GoodwillImpairmentLoss','ImpairmentOfIntangibleAssetsExcludingGoodwill',
 'AssetImpairmentCharges','ImpairmentOfIntangibleAssetsIncludingGoodwill','GoodwillAndIntangibleAssetImpairment']
TAGS_I=['Goodwill','IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet','Assets',
 'CashAndCashEquivalentsAtCarryingValue','ShortTermInvestments','MarketableSecuritiesCurrent',
 'LongTermDebtNoncurrent','LongTermDebt','LongTermDebtCurrent','DebtCurrent','OperatingLeaseLiabilityNoncurrent']
def load(t): return json.load(open(f'companyfacts_{t}.json'))
def dur(f,tag,minday=330,maxday=400):
    node=f['facts'].get('us-gaap',{}).get(tag)
    if not node: return {}
    out={}
    for unit,pts in node['units'].items():
        for p in pts:
            if 'start' not in p: continue
            s=date.fromisoformat(p['start']); e=date.fromisoformat(p['end'])
            if not (minday<=(e-s).days<=maxday): continue
            if p.get('form') not in ('10-K','10-K/A'): continue
            k=p['end']
            # prefer latest-filed
            if k not in out or p.get('filed','')>=out[k][2]:
                out[k]=(p['val'],p.get('accn'),p.get('filed'),p.get('fy'),p.get('fp'))
    return out
def inst(f,tag):
    node=f['facts'].get('us-gaap',{}).get(tag)
    if not node: return {}
    out={}
    for unit,pts in node['units'].items():
        for p in pts:
            if 'start' in p: continue
            if p.get('form') not in ('10-K','10-K/A'): continue
            k=p['end']
            if k not in out or p.get('filed','')>=out[k][2]:
                out[k]=(p['val'],p.get('accn'),p.get('filed'))
    return out
for tic in sys.argv[1:]:
    f=load(tic)
    print('#'*20,tic)
    print('--- DURATION (FY) ---')
    for t in TAGS_D:
        d=dur(f,t)
        if not d: continue
        ks=sorted(d)[-6:]
        print(f'{t}:')
        for k in ks: print('   ',k,f'{d[k][0]:,.0f}',d[k][1],'filed',d[k][2])
    print('--- INSTANT ---')
    for t in TAGS_I:
        d=inst(f,t)
        if not d: continue
        ks=sorted(d)[-4:]
        print(f'{t}:')
        for k in ks: print('   ',k,f'{d[k][0]:,.0f}',d[k][1])
