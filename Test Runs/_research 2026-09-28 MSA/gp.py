import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
out=open('gp_by_year.txt','w',encoding='utf-8')
out2=open('competition_by_year.txt','w',encoding='utf-8')
for y in range(1993,2026):
    t=open(f'cache/k{y}.txt',encoding='utf-8',errors='ignore').read()
    t1=re.sub(r'\s+',' ',t)
    gps=re.findall(r'((?:Gross profit|gross margin|Cost of products sold)[^.]{0,40}(?:\.[^.]{3,400}){0,4}\.)',t1)
    pr=[m for m in re.findall(r'[^.]{0,300}(?:price increase|selling price|pricing|price realization|prices)[^.]{0,300}\.',t1) if 'option pricing' not in m and 'Black-Scholes' not in m and 'market price' not in m.lower() and 'quoted' not in m]
    out.write(f'\n===== FY{y}\n')
    for g in gps[:6]: out.write('GP: '+g[:900]+'\n')
    for p in pr[:12]: out.write('PR: '+p[:700]+'\n')
    comp=re.findall(r'[^.]{0,200}(?:compet)[^.]{0,500}\.',t1)
    out2.write(f'\n===== FY{y}\n')
    for c in comp[:8]: out2.write(c[:900]+'\n')
