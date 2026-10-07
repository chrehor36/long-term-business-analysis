import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1800'
L=[('0001628280-26-010185','abt-20251231.htm','tenk_2025.txt'),
('0001628280-26-050134','abt-20260630.htm','tenq_2606.txt'),
('0001628280-26-028357','abt-20260331.htm','tenq_2603.txt'),
('0001308179-26-000064','abt-20260311.htm','proxy_2026.txt'),
('0001628280-25-007110','abt-20241231.htm','tenk_2024.txt'),
('0001628280-24-005348','abt-20231231.htm','tenk_2023.txt'),
('0001628280-23-004026','abt-20221231.htm','tenk_2022.txt'),
('0001104659-22-025141','abt-20211231x10k.htm','tenk_2021.txt'),
('0001104659-21-025751','abt-20201231x10k.htm','tenk_2020.txt'),
('0001104659-20-023904','abt-20191231x10k59d41b.htm','tenk_2019.txt'),
('0001047469-19-000624','a2237733z10-k.htm','tenk_2018.txt'),
('0001047469-18-000856','a2234264z10-k.htm','tenk_2017.txt'),
('0001047469-17-000744','a2230875z10-k.htm','tenk_2016.txt'),
('0001047469-16-010246','a2227279z10-k.htm','tenk_2015.txt'),
('0001047469-15-001377','a2222655z10-k.htm','tenk_2014.txt'),
('0001047469-14-001176','a2218043z10-k.htm','tenk_2013.txt'),
('0001047469-13-001180','a2212523z10-k.htm','tenk_2012.txt'),
]
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache'))
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
