import re
for fy in ['FY2007','FY2010','FY2013','FY2016','FY2019','FY2022','FY2024','FY2025']:
    t=open(f'tenk_{fy}.txt',encoding='utf-8').read()
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t)
    print('==',fy)
    seen=0
    for m in re.finditer(r'(?i)(net (patient )?(revenue|rate) per (patient )?visit|total patient visits|patient visits)',t):
        s=t[max(0,m.start()-60):m.start()+260]
        if re.search(r'\d{3},\d{3}|\$ ?\d{2,3}\.\d\d',s):
            print('  ',s); seen+=1
        if seen>=5: break
