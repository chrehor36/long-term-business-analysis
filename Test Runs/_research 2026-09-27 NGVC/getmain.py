import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1547459'
L=[('0001437749-26-030470','ngvc20260911_pre14c.htm','pre14c_2609.txt'),
('0001437749-26-030469','ngvc20260911_8k.htm','8k_2609.txt'),
('0001437749-25-037556','ngvc20250930_10k.htm','tenk_2025.txt'),
('0001437749-26-026255','ngvc20260630_10q.htm','tenq_2606.txt'),
('0001437749-26-026263','ngvc20260805_8k.htm','8k_2608.txt'),
('0001437749-26-001768','ngvc20260116_def14a.htm','proxy_2026.txt'),
('0001437749-24-037351','ngvc20240930_10k.htm','tenk_2024.txt'),
]
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
