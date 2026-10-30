from fetch import get, strip
import os
B='https://www.sec.gov/Archives/edgar/data/918646/'
docs={
 'tenk_fy2026.txt':'000119312526230979/exp-20260331.htm',
 'tenq_q1_fy2027.txt':'000119312526323823/exp-20260630.htm',
 'tenk_fy2024.txt':'000095017024063523/exp-20240331.htm',
 'tenk_fy2022.txt':'000095017022010413/exp-20220331.htm',
 'tenk_fy2020.txt':'000156459020026773/exp-10k_20200331.htm',
 'tenk_fy2018.txt':'000156459018014244/exp-10k_20180331.htm',
 'def14a_2026.txt':'000119312526271073/exp-20260615.htm',
}
for k,v in docs.items():
    if os.path.exists(k): continue
    open(k,'w',encoding='utf-8').write(strip(get(B+v))); print(k,os.path.getsize(k))
