import sys,os,time
sys.argv=[sys.argv[0]]
exec(open('fetch.py').read().split("cik='1046311'")[0])
jobs=[('WH','1722684','0001722684-26-000007','wh-20251231.htm'),('WH19','1722684','0001722684-20-000007','wh-20191231x10k.htm'),
('HLT','1585689','0001585689-26-000007','hlt-20251231.htm'),('HLT19','1585689','0001585689-20-000013','hlt-20191231.htm'),
('MAR','1048286','0001048286-26-000007','mar-20251231.htm'),('MAR19','1048286','0001628280-20-002376','mar-q42019x10k.htm')]
for name,cik,acc,doc in jobs:
    out=f'cache/rival_{name}.txt'
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(name,len(b)); time.sleep(0.3)
