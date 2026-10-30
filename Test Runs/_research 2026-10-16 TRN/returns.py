# Field returns from each company's own XBRL (first-filed 10-K values), USD millions. Transcription + arithmetic only.
import json
import os,sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facts import annual
def g(c,t,dur=True):
    f=json.load(open(f'cache/facts_{c}.json')); return {k[:4]:v[0]/1e6 for k,v in annual(f,t,duration=dur).items()}
def fyk(c,t,dur=True):
    f=json.load(open(f'cache/facts_{c}.json')); return {k:v[0]/1e6 for k,v in annual(f,t,duration=dur).items()}
T=0.79
rows=[]
# TRN: interest from InterestExpense tag 2016-2020; 10-K 'Interest expense, net' 2021-2025 (accessions 0000099780-23-000013, -24-000017, -26-000014)
trn_int=g('0000099780','InterestExpense'); trn_int.update({'2021':191.4,'2022':207.6,'2023':265.5,'2024':273.5,'2025':274.2})
co={'TRN':('0000099780',trn_int),'GATX':('0000040211',g('0000040211','InterestExpense')),
    'GBX':('0000923120',{k[:4]:v for k,v in fyk('0000923120','InterestPaidNet').items()}),
    'RAIL':('0001320854',{k[:4]:v for k,v in fyk('0001320854','InterestPaidNet').items()})}
out=[]
for name,(c,intr) in co.items():
    ni={k[:4]:v for k,v in fyk(c,'NetIncomeLoss').items()}
    a={k[:4]:v for k,v in fyk(c,'Assets',False).items()}
    e={k[:4]:v for k,v in fyk(c,'StockholdersEquity',False).items()}
    if name=='RAIL':
        e={k[:4]:v for k,v in fyk(c,'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest',False).items()}
        ni.update({k[:4]:v for k,v in fyk(c,'NetIncomeLossAvailableToCommonStockholdersBasic').items() if k[:4] not in ni})
    print(f'== {name}  year  NI  int  assets  equity  ROE(avg)  ROA_unlev_after-tax(avg)')
    roes=[];roas=[]
    for y in range(2016,2026):
        Y=str(y);P=str(y-1)
        if Y in ni and Y in a and P in a and Y in intr:
            avgA=(a[Y]+a[P])/2; 
            roa=(ni[Y]+intr[Y]*T)/avgA
            roe=ni[Y]/((e[Y]+e[P])/2) if Y in e and P in e and (e[Y]+e[P])>0 else float('nan')
            roes.append(roe); roas.append(roa)
            print(f'   {Y} {ni[Y]:8.1f} {intr[Y]:7.1f} {a[Y]:8.1f} {e.get(Y,float("nan")):8.1f}  {roe*100:6.1f}%  {roa*100:5.1f}%')
    import math
    r=[x for x in roes if not math.isnan(x)]
    print(f'   mean ROE {sum(r)/len(r)*100:.1f}%  mean unlevered after-tax ROA {sum(roas)/len(roas)*100:.1f}%  n={len(roas)}')
