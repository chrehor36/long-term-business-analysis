import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get
P={'PPG':'0000079879','SHW':'0000089800','RPM':'0000110621','AXTA':'0001616862'}
def ann(f,tags,unit='USD',duration=True):
    out={}
    for t in tags:
        if t not in f: continue
        for x in f[t]['units'].get(unit,[]):
            fr=x.get('frame','')
            if not x['form'].startswith('10-K'): continue
            if duration:
                if fr.startswith('CY') and 'Q' not in fr: out.setdefault(int(fr[2:6]),x['val'])
            else:
                if fr.startswith('CY') and fr.endswith('Q4I'): out.setdefault(int(fr[2:6]),x['val'])
    return out
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
PT=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']
IE=['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt']
EQ=['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','StockholdersEquity']
LTD=['LongTermDebtNoncurrent','LongTermDebtAndCapitalLeaseObligations']
STD=['LongTermDebtCurrent','DebtCurrent','ShortTermBorrowings','ShortTermDebtAndCurrentPortionOfLongTermDebt']
CASH=['CashAndCashEquivalentsAtCarryingValue']
GW=['Goodwill']; INT=['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet']
res={}
for k,c in P.items():
    fn=f'peers/facts_{k}.json'
    if not os.path.exists(fn):
        open(fn,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json')); time.sleep(0.5)
    d=json.load(open(fn)); f=d['facts']['us-gaap']
    r=ann(f,REV); pt=ann(f,PT); ie=ann(f,IE)
    eq=ann(f,EQ,duration=False); ltd=ann(f,LTD,duration=False); cash=ann(f,CASH,duration=False)
    std={}
    for t in STD:
        for y,v in ann(f,[t],duration=False).items(): std[y]=std.get(y,0)+v
    print('====',k,d['entityName'])
    for y in range(2014,2026):
        if y in r and y in pt:
            ebit=pt[y]+ie.get(y,0)
            cap=(eq.get(y,0)+ltd.get(y,0)+std.get(y,0)-cash.get(y,0))
            print(y, f'rev {r[y]/1e6:,.0f}', f'pretax {pt[y]/1e6:,.0f}', f'intexp {ie.get(y,0)/1e6:,.0f}', f'EBIT% {ebit/r[y]*100:.1f}', f'capital {cap/1e6:,.0f}', f'EBIT/cap {ebit/cap*100:.1f}%' if cap>0 else '-', 'miss:'+','.join(n for n,dct in (('ie',ie),('eq',eq),('ltd',ltd),('cash',cash)) if y not in dct))
