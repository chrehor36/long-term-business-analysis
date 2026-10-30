import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, strip
CIK='1944048'
for acc,doc,out in [('0001944048-26-000030','kvue-20251228.htm','tenk_2025.txt'),('0001944048-25-000033','kvue-20241229.htm','tenk_2024.txt'),('0001944048-24-000057','kvue-20231231.htm','tenk_2023.txt'),('0001628280-23-015837','kenvue424b4.htm','ipo424b4_2023.txt')]:
    if os.path.exists(out): continue
    b=get(f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}')
    open(out,'w',encoding='utf-8').write(strip(b)); print(out, os.path.getsize(out))
