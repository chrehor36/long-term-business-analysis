import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='310158'
L=[('0000310158-26-000063','mrk-20251231.htm','tenk_2025.txt'),
('0000310158-26-000212','mrk-20260630.htm','tenq_2606.txt'),
('0001193125-26-147704','d85708ddef14a.htm','proxy_2026.txt'),
('0001628280-25-007732','mrk-20241231.htm','tenk_2024.txt'),
('0001628280-24-006850','mrk-20231231.htm','tenk_2023.txt'),
('0001628280-23-005061','mrk-20221231.htm','tenk_2022.txt'),
('0000310158-22-000003','mrk-20211231.htm','tenk_2021.txt'),
('0000310158-21-000004','mrk-20201231.htm','tenk_2020.txt'),
('0000310158-20-000005','mrk1231201910k.htm','tenk_2019.txt'),
('0000310158-18-000005','mrk1231201710k.htm','tenk_2017.txt'),
('0000310158-16-000063','mrk1231201510k.htm','tenk_2015.txt'),
]
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
