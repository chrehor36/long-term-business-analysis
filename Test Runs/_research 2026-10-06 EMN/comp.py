import json,requests,os,sys
from datetime import date
H={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def load(cik):
    fn=f'facts_{cik}.json'
    if not os.path.exists(fn):
        open(fn,'w').write(requests.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json',headers=H).text)
    return json.load(open(fn))
def annual(j,tags):
    out={}
    for tag in tags:
        for ns in ('us-gaap',):
            if tag not in j['facts'].get(ns,{}): continue
            for unit,vals in j['facts'][ns][tag]['units'].items():
                for v in vals:
                    if v.get('form') not in ('10-K','10-K/A') or 'start' not in v: continue
                    s=date.fromisoformat(v['start']);e=date.fromisoformat(v['end'])
                    if not 350<(e-s).days<380: continue
                    y=e.year
                    if y in out and out[y][2]==tag and out[y][1]<=v['filed']: continue
                    if y in out and out[y][2]!=tag: continue
                    out[y]=(v['val'],v['filed'],tag,v['accn'])
    return out
cos={k:v for k,v in [a.split('=') for a in sys.argv[1:]]}
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
PT=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments','IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic']
INT=['InterestExpense','InterestIncomeExpenseNet','InterestIncomeExpenseNonoperatingNet','InterestExpenseNet','InterestExpenseNonoperating','InterestExpenseDebt','InterestAndDebtExpense']
GP=['GrossProfit']
for k,c in cos.items():
    j=load(c)
    r=annual(j,REV);p=annual(j,PT);i=annual(j,INT);g=annual(j,GP)
    print(k, j.get('entityName'))
    for y in sorted(r):
        if y<2008 or r[y][0]==0: continue
        rv=r[y][0]
        s=f"  {y} rev {rv/1e6:8.0f}"
        if y in g: s+=f" GM {g[y][0]/rv*100:5.1f}%"
        if y in p:
            iv=(i[y][0] if y in i else 0); iv=-iv if i.get(y,(0,0,''))[2]=='InterestIncomeExpenseNet' else iv; ebit=p[y][0]+iv
            s+=f" pretax {p[y][0]/1e6:7.0f} int {(i[y][0]/1e6 if y in i else float('nan')):5.0f} EBITm {ebit/rv*100:5.1f}%"
        s+=f"  [{r[y][3]}]"
        print(s)
