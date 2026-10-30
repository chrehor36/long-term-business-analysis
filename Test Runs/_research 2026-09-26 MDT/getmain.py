import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1613103'
L=[('0001628280-26-044354','mdt-20260424.htm','tenk_2026.txt'),
('0001613103-25-000091','mdt-20250425.htm','tenk_2025.txt'),
('0001613103-24-000072','mdt-20240426.htm','tenk_2024.txt'),
('0001613103-23-000040','mdt-20230428.htm','tenk_2023.txt'),
('0001613103-22-000023','mdt-20220429.htm','tenk_2022.txt'),
('0001613103-21-000027','mdt-20210430.htm','tenk_2021.txt'),
('0001613103-20-000021','mdt-20200424.htm','tenk_2020.txt'),
('0001613103-19-000028','mdt-2019426x10k.htm','tenk_2019.txt'),
('0001613103-18-000024','mdt-2018427x10k.htm','tenk_2018.txt'),
('0001613103-17-000018','mdt-2017428x10k.htm','tenk_2017.txt'),
('0001613103-16-000093','mdt-2016429x10k.htm','tenk_2016.txt'),
('0001613103-15-000028','mdt-2015424x10k.htm','tenk_2015.txt'),
('0001613103-26-000010','mdt-20260816.htm','proxy_2026.txt'),
]
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
