import sys,os,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='73309'
L=[('0001193125-26-071575','nue-20251231.htm','tenk_2025.txt'),
('0001193125-26-345891','nue-20260704.htm','q2606.txt'),
('0001193125-26-318190','d468854d8k.htm','8k_2607.txt'),
('0001193125-26-127739','d21430ddef14a.htm','proxy_2026.txt'),
('0001193125-26-060448','d116401d8k.htm','8k_2602.txt'),
('0001193125-25-307550','d85411d8k.htm','8k_2512.txt'),
('0001193125-26-086912','d94870d8k.htm','8k_2603.txt'),
]
for acc,doc,out in L:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out)); time.sleep(0.3)
