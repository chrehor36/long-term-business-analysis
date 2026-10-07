import json, os, re
from fetch import get, strip
cik='277135'
lines=[l.split() for l in open('tenk_list.txt')]
for l in lines:
    fd,form,acc=l[0],l[1],l[2]
    fy=l[-1][:4]
    if int(fy)>=2021: continue
    a=acc.replace('-','')
    try:
        items=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json'))['directory']['item']
    except SystemExit as e:
        print('FAIL',acc); continue
    names=[x['name'] for x in items]
    want=[]
    for n in names:
        nl=n.lower()
        if nl.startswith('r') and nl[1:2].isdigit(): continue
        if nl.endswith(('.htm','.html')) and ('10k' in nl or '10-k' in nl or 'ex13' in nl or 'ex-13' in nl or nl==l[3].lower() or 'exhibit13' in nl or 'annual' in nl or nl=='0001.htm' or re.match(r'000\d\.htm',nl)):
            want.append(n)
    if not want:
        want=[n for n in names if n.endswith('.txt') and n.startswith('0')]
    print(fy,acc,names if len(names)<15 else names[:15],'->',want)
    for n in want:
        out=f'cache/k{fy}_{n}.txt'
        if os.path.exists(out): continue
        b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{n}')
        open(out,'w',encoding='utf-8').write(strip(b))
