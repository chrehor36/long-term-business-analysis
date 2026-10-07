import re
out=[]
for y in [2014,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]:
    t=open(f'tenk_FY{y}.txt',encoding='utf-8').read()
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t)
    seg=re.findall(r'(Global market share of the ([A-Za-z,& ]{3,40}) segment (?:(increased|decreased) ([0-9.]+) points?|(was unchanged)))',t)
    out.append(f'== FY{y}: '+' ; '.join(f"{s[1]} {s[2] or s[4]} {s[3]}" for s in seg))
    # also all-outlet share
    ao=re.findall(r'[^.]{0,120}all-outlet[^.]{0,160}',t)
    for a in ao[:3]: out.append('   AO: '+a[:280])
open('shares_out.txt','w').write('\n'.join(out)); print('\n'.join(out))
