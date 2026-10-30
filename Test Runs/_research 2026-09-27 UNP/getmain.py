import sys,os,time
from fetch import get, strip
CIK='100885'
L=[('0000100885-26-000037','unp-20251231.htm','tenk_2025.txt'),
('0000100885-26-000250','unp-20260630.htm','q2606.txt'),
('0000100885-26-000155','unp-20260331.htm','q2603.txt'),
('0000100885-26-000249','unp-20260723.htm','8k_2607.txt'),
('0000100885-26-000098','unp-20260324.htm','proxy_2026.txt'),
('0001193125-25-168150','d51641d8k.htm','8k_250729_101.txt'),
('0001193125-25-167154','d64537d8k.htm','8k_250729_801.txt'),
('0000100885-25-000332','unp-20251114.htm','8k_251117.txt'),
('0000100885-25-000345','unp-20251212.htm','8k_251212.txt'),
('0000100885-25-000347','unp-20251219.htm','8k_251219.txt'),
('0001193125-25-270046','d84472d8k.htm','8k_251106.txt'),
('0000100885-26-000174','unp-20260514.htm','8k_260518.txt'),
]
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
