import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='200406'
L=[('0000200406-26-000016','jnj-20251228.htm','tenk_2025.txt'),
('0000200406-26-000153','jnj-20260628.htm','tenq_2606.txt'),
('0000200406-26-000063','jnj-20260309.htm','proxy_2026.txt'),
('0000200406-25-000038','jnj-20241229.htm','tenk_2024.txt'),
('0000200406-24-000013','jnj-20231231.htm','tenk_2023.txt'),
('0000200406-23-000016','jnj-20230101.htm','tenk_2022.txt'),
('0000200406-22-000022','jnj-20220102.htm','tenk_2021.txt'),
('0000200406-21-000008','jnj-20210103.htm','tenk_2020.txt'),
('0000200406-20-000010','form10-k20191229.htm','tenk_2019.txt'),
('0000200406-19-000009','form10-k20181230.htm','tenk_2018.txt'),
('0000200406-18-000005','form10-k20171231.htm','tenk_2017.txt'),
('0000200406-17-000006','form10-k20170101.htm','tenk_2016.txt'),
('0000200406-16-000071','form10-k20160103.htm','tenk_2015.txt'),
]
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache'))
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
