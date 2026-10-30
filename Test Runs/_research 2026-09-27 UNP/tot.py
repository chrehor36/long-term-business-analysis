import re,sys
for y in (2020,2021,2022):
    s=open(f'tenk_{y}.txt',encoding='utf-8').read()
    f=re.sub(r'\s*\|\s*',' | ',s.replace('\n',' '))
    f=re.sub(r'\s+',' ',f)
    for lab in ('Freight Revenues','Freight revenues','Revenue Carloads','Revenue carloads','Average Revenue per Car','Average revenue per car'):
        for m in re.finditer(lab,f):
            seg=f[m.start():m.start()+3000]
            t=re.search(r'(Total|Average) \|[ $|]*([\d,]+)[ $|]*([\d,]+)[ $|]*([\d,]+)',seg)
            if t and 'Millions' in seg[:80] or (t and 'Thousands' in seg[:60]) or (t and lab.startswith('Average')):
                print(y,lab,t.group(0)[:80]); break
