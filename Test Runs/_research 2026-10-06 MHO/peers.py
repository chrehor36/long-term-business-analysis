import json,sys,os
sys.path.insert(0,'.')
from fetch import get
from datetime import date
HERE=os.path.dirname(os.path.abspath(__file__))
PEERS={'MHO':799292,'NVR':906163,'DHI':882184,'LEN':920760,'MTH':833079,'CCS':1576940}
TAGS={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','HomeBuildingRevenue','RealEstateRevenueNet','SalesRevenueGoodsNet'],
      'ni':['NetIncomeLoss','ProfitLoss','NetIncomeLossAvailableToCommonStockholdersBasic'],
      'pti':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
      'eq':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
      'ocf':['NetCashProvidedByUsedInOperatingActivities'],
      'inv':['InventoryRealEstate','RealEstateInventory','InventoryNet','InventoryRealEstateWorkInProcess'],
      'dil':['WeightedAverageNumberOfDilutedSharesOutstanding'],
      'imp':['ImpairmentOfRealEstate','InventoryWriteDown','ImpairmentOfRealEstateAndOtherAssets'],
      'buy':['PaymentsForRepurchaseOfCommonStock'],
      'iss':['ProceedsFromIssuanceOfCommonStock'],
      'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense']}
def load(t,cik):
    p=os.path.join(HERE,'peers',f'{t}_facts.json')
    if not os.path.exists(p):
        open(p,'w',encoding='utf-8').write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{str(cik).zfill(10)}.json"))
    return json.load(open(p,encoding='utf-8'))
def series(j,tags,instant=False):
    out={}
    for t in tags:
        for ns in ('us-gaap',):
            if t not in j['facts'].get(ns,{}): continue
            for u,vals in j['facts'][ns][t]['units'].items():
                if u!='USD' and u!='shares': continue
                for v in sorted(vals,key=lambda v:v['filed']):
                    if v.get('form') not in ('10-K','10-K/A','10-KT'): continue
                    if 'start' in v:
                        if instant: continue
                        d=(date.fromisoformat(v['end'])-date.fromisoformat(v['start'])).days
                        if not 340<d<380: continue
                    elif not instant: continue
                    if 'segment' in v: continue
                    fy=int(v['end'][:4]) if v['end'][5:7]>'03' else int(v['end'][:4])-1
                    out.setdefault(fy,v['val'])
    return out
if __name__=='__main__':
    res={}
    for tk,cik in PEERS.items():
        j=load(tk,cik); r={}
        for k,tags in TAGS.items():
            r[k]=series(j,tags,instant=(k in ('eq','inv')))
        res[tk]=r
    json.dump(res,open(os.path.join(HERE,'peers','series.json'),'w'),indent=0)
    for tk in res:
        print('=====',tk)
        for k in res[tk]:
            s=res[tk][k]
            print(' ',k,' '.join(f"{y}:{s[y]/1e6:.0f}" for y in sorted(s) if y>=2005))
