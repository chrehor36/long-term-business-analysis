import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1547459'
L=[('0001437749-23-033880','ngvc20230930_10k.htm','tenk_2023.txt'),
('0001437749-22-028744','ngvc20220930_10k.htm','tenk_2022.txt'),
('0001437749-21-028226','ngvc20210930_10k.htm','tenk_2021.txt'),
('0001437749-20-025108','ngvc20200930_10k.htm','tenk_2020.txt'),
('0001437749-19-023923','ngvc20190930_10k.htm','tenk_2019.txt'),
('0001437749-18-021661','ngvc20180930_10k.htm','tenk_2018.txt'),
('0001437749-17-020347','ngvc20170930_10k.htm','tenk_2017.txt'),
('0001437749-16-043133','ngvc20160817_10k.htm','tenk_2016.txt'),
('0001437749-15-021984','ngvc20150930_10k.htm','tenk_2015.txt'),
('0001437749-14-021985','ngvc20140930_10k.htm','tenk_2014.txt'),
('0001104659-13-089909','a13-21538_110k.htm','tenk_2013.txt'),
('0001104659-12-083954','a12-26396_110k.htm','tenk_2012.txt'),
('0001047469-12-007416','a2210362z424b4.htm','prosp_2012.txt'),
]
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
