import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1383312'
L=[('0001628280-26-052243','br-20260630.htm','tenk_2026.txt'),
('0001383312-26-000022','br-20260803.htm','8k_2608.txt'),
('0001140361-26-019332','ef20072392_8k.htm','8k_2605a.txt'),
('0001140361-26-021675','ef20073635_8k.htm','8k_2605b.txt'),
('0001383312-26-000017','br-20260521.htm','8k_2605c.txt'),
('0001383312-26-000009','br-20260306.htm','8k_2603.txt'),
('0001383312-25-000034','br-20251113.htm','8k_2511.txt'),
('0001383312-26-000019','br-20260609.htm','8k_2606.txt'),
('0001383312-26-000003','br-20260202.htm','8k_2602.txt'),
('0001140361-25-037069','ny20050521x1_def14a.htm','proxy_2025.txt'),
('0001628280-25-037656','br-20250630.htm','tenk_2025.txt'),
]
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
