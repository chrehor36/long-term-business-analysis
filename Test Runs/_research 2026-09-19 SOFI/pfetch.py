import sys, os, re, json
sys.path.insert(0,'tools')
import sources as S
sys.path.insert(0,'Test Runs/_research 2026-09-19 SOFI')
from fetch import totext
R='Test Runs/_research 2026-09-19 SOFI/peers/'
for spec in sys.argv[1:]:
    tick,cik,acc,doc = spec.split('|')
    a=acc.replace('-','')
    url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}'
    try:
        h=S._get(url, headers=S.SEC_UA)
    except Exception as e:
        print(tick,'ERR',e, url); continue
    p=R+f'{tick}_tenk.txt'
    open(p,'w',encoding='utf-8').write(totext(h))
    print(tick, len(h), '->', os.path.getsize(p))
