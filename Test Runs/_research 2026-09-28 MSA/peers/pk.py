import os,sys
sys.path.insert(0,'..')
from fetch import get,strip
L=[('66740','0000066740-26-000014','mmm-20251231.htm','MMM_k2025'),('66740','0000066740-23-000014','mmm-20221231.htm','MMM_k2022'),('66740','0001558370-20-000581','mmm-20191231x10k62bf35.htm','MMM_k2019'),
('773840','0000773840-23-000013','hon-20221231.htm','HON_k2022'),('773840','0000773840-21-000015','hon-20201231.htm','HON_k2020'),
('798081','0001193125-26-159176','lake-20260131.htm','LAKE_k2026')]
for c,a,d,o in L:
    out=f'{o}.txt'
    if os.path.exists(out): continue
    open(out,'w',encoding='utf-8').write(strip(get(f'https://www.sec.gov/Archives/edgar/data/{c}/{a.replace("-","")}/{d}')))
    print(out,os.path.getsize(out))
