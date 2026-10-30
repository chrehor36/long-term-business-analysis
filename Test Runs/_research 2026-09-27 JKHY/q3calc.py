import json,urllib.request,datetime,sys
sys.stdout.reconfigure(encoding='utf-8')
X=json.load(open('xb.json'))
f=json.load(open('companyfacts.json'))['facts']['us-gaap']
def ann(tag,flow=True):
    out={}
    for u,vals in f[tag]['units'].items():
      for v in vals:
        if not v['form'].startswith('10-K'): continue
        e=v['end']
        if e[5:7]!='06': continue
        if flow and ('start' not in v or v['start'][5:7]!='07'): continue
        if not flow and 'start' in v: continue
        y=int(e[:4])
        if y not in out or v['filed']>out[y][1]: out[y]=(v['val'],v['filed'])
    return {k:v[0] for k,v in out.items()}
ni=ann('NetIncomeLoss'); eq=ann('StockholdersEquity',False); tax=ann('IncomeTaxExpenseBenefit')
pt={**ann('IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'),**ann('IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest')}
paid={**ann('IncomeTaxesPaid'),**ann('IncomeTaxesPaidNet')}
sh=ann('WeightedAverageNumberOfSharesOutstandingBasic')
div=ann('PaymentsOfDividends'); buy=ann('PaymentsForRepurchaseOfCommonStock')
print('FY | NI | avg equity | ROE | pretax | tax provision % | cash taxes paid % pretax | basic wtd shares (M) | dividends | buybacks')
for y in range(2009,2027):
    ae=(eq[y]+eq[y-1])/2 if y in eq and y-1 in eq else None
    print(y, round(ni[y]/1e6,1), round(ae/1e6,1) if ae else '', f'{ni[y]/ae:.1%}' if ae else '', round(pt.get(y,0)/1e6,1), f'{tax[y]/pt[y]:.1%}' if y in pt else '', f'{paid[y]/pt[y]:.1%}' if y in paid and y in pt else '', round(sh.get(y,0)/1e6,2), round(div.get(y,0)/1e6,1), round(buy.get(y,0)/1e6,1))
# prices
UA={'User-Agent':'Mozilla/5.0'}
b=urllib.request.urlopen(urllib.request.Request('https://query1.finance.yahoo.com/v8/finance/chart/JKHY?range=15y&interval=1mo',headers=UA),timeout=60).read()
open('price_raw_JKHY_15y_monthly.json','wb').write(b)
r=json.loads(b)['chart']['result'][0]
pts=[(datetime.datetime.utcfromtimestamp(t).date(),c) for t,c in zip(r['timestamp'],r['indicators']['quote'][0]['close']) if c]
for d,c in pts:
    if d.month in (6,7) : print('monthly close', d, round(c,2))
