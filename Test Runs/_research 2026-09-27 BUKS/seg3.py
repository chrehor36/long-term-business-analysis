import re
for y in (2021,2022,2023,2024):
    L=open(f'tenk_{y}.txt',encoding='utf-8').read().split('\n')
    i=[k for k,l in enumerate(L) if re.search(r'Revenues from customers',l)][0]
    s=' '.join(x.strip() for x in L[i:i+400] if x.strip() not in ('','|','$','%'))
    s=re.sub(r'[\s|]+',' ',s)
    for m in re.finditer(r'(Year Ended April 30, 20\d\d).{0,80}?Revenues|Operating income \(loss\)[ \d,()\-]{0,80}|Income \(loss\) before[ \d,()\-a-z]{0,90}|Segment[^.]{0,40}income[ \d,()\-]{0,80}',s):
        print(y, m.group(0)[:160])
