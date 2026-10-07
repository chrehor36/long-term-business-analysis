import re,sys
out=open('bridges.txt','w',encoding='utf-8')
for fy in ['FY2014','FY2016','FY2017','FY2019','FY2020','FY2021','FY2022','FY2023','FY2024','FY2025']:
    t=open(f'tenk_{fy}.txt',encoding='utf-8').read()
    f=re.sub(r'\s+',' ',t)
    out.write(f'===== {fy}\n')
    for m in re.finditer(r'(?i)(net sales (increased|decreased)[^.]{0,120}(due to|primarily)[^●]{0,80}(● [^●]{0,160}){1,8})',f):
        out.write(m.group(1)[:900]+'\n--\n')
    for m in re.finditer(r'(?i)(selling prices?[^.]{0,200}\.)',f):
        s=m.group(1)
        if re.search(r'\d+\s*%|percent',s): out.write('  PRICE: '+s[:300]+'\n')
out.close()
