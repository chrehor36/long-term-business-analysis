import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='81362'
L=[('0001628280-26-010694','kwr-20251231.htm','tenk_2025.txt'),
('0001628280-26-051107','kwr-20260630.htm','tenq_2606.txt'),
('0001628280-26-028949','kwr-20260331.htm','tenq_2603.txt'),
('0001628280-26-022236','kwr-20260331.htm','proxy_2026.txt'),
('0000081362-25-000014','kwr-20241231.htm','tenk_2024.txt'),
('0000081362-24-000020','kwr-20231231.htm','tenk_2023.txt'),
('0000081362-24-000024','kwr-20231231.htm','tenka_2023.txt'),
('0000081362-23-000014','kwr-20221231.htm','tenk_2022.txt'),
('0000081362-22-000003','kwr-20211231.htm','tenk_2021.txt'),
('0000081362-21-000004','kwr-20201231.htm','tenk_2020.txt'),
('0000081362-20-000002','kwr-20191231.htm','tenk_2019.txt'),
('0000081362-19-000002','maindocument001.htm','tenk_2018.txt'),
('0000081362-18-000003','maindocument001.htm','tenk_2017.txt'),
('0000081362-17-000006','form10k.htm','tenk_2016.txt'),
('0000081362-16-000025','form10k.htm','tenk_2015.txt'),
('0000081362-15-000004','form10k.htm','tenk_2014.txt'),
]
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache'))
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
