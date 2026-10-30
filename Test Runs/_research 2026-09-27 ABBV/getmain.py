import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1551152'
L=[('0001551152-26-000008','abbv-20251231.htm','tenk_2025.txt'),
('0001551152-26-000026','abbv-20260630.htm','tenq_2606.txt'),
('0001104659-26-033387','abbv-20260508xdef14a.htm','proxy_2026.txt'),
('0001551152-25-000020','abbv-20241231.htm','tenk_2024.txt'),
('0001551152-24-000011','abbv-20231231.htm','tenk_2023.txt'),
('0001551152-23-000011','abbv-20221231.htm','tenk_2022.txt'),
('0001551152-22-000007','abbv-20211231.htm','tenk_2021.txt'),
('0001551152-21-000008','abbv-20201231.htm','tenk_2020.txt'),
('0001551152-20-000007','abbv-20191231x10k.htm','tenk_2019.txt'),
('0001551152-19-000008','abbv-20181231x10k.htm','tenk_2018.txt'),
('0001551152-18-000014','abbv-20171231x10k.htm','tenk_2017.txt'),
('0001551152-17-000004','abbv-12312016x10k.htm','tenk_2016.txt'),
('0001047469-16-010239','a2227341z10-k.htm','tenk_2015.txt'),
('0001047469-15-000995','a2223058z10-k.htm','tenk_2014.txt'),
('0001047469-14-001154','a2217723z10-k.htm','tenk_2013.txt'),
('0001047469-13-002827','a2213529z10-k.htm','tenk_2012.txt'),
]
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
