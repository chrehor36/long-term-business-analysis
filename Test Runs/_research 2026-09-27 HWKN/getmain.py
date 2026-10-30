import sys,os,time,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='46250'
rows=json.load(open('allfilings.json'))
L=[]
for d,f,acc,doc,it,rep in rows:
    if f in ('10-K','10-K/A') and d>='2004-01-01' and doc:
        L.append((acc,doc,'tenk_%s%s.txt'%(rep[:4] if f=='10-K' else rep[:4]+'A','')))
L+= [('0000046250-26-000034','hwkn-20260628.htm','tenq_2606.txt'),
('0000046250-26-000005','hwkn-20251228.htm','tenq_2512.txt'),
('0000046250-25-000057','hwkn-20250928.htm','tenq_2509.txt'),
('0000046250-26-000026','hwkn-20260616.htm','proxy_2026.txt'),
('0000046250-25-000031','hwkn-20250618.htm','proxy_2025.txt'),
('0000046250-24-000015','hwkn-20240619.htm','proxy_2024.txt'),
('0000046250-26-000009','filename1.htm','corresp_2026.txt'),
('0000046250-23-000011','filename1.htm','corresp_2023.txt'),
]
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache'))
for acc,doc,out in L:
    if os.path.exists(out): continue
    try:
        b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    except SystemExit as e:
        print('FAIL',out,e); continue
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, acc, os.path.getsize(out)); time.sleep(0.3)
