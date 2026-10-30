# Sensitivity (CONVENTION of this run): project AY2021-2025 to the development the same table showed, on average, for AY2016-2019 at their current age (9-6 yrs).
import re
txt=open('tri_2025.txt',encoding='cp1252').read().split('## ')[1:]
tot=0
for blk in txt:
    lines=blk.strip().split('\n'); name=lines[0]
    rows={}
    for l in lines[1:]:
        m=re.match(r'(\d{4}) initial\s+(\d+) latest\s+(\d+)',l)
        if m: rows[int(m.group(1))]=(int(m.group(2)),int(m.group(3)))
    mat=[ (rows[y][1]-rows[y][0])/rows[y][0] for y in range(2016,2020)]
    mp=sum(mat)/len(mat)
    add=0
    for y in range(2021,2026):
        i,l=rows[y]; cur=(l-i)/i
        add+= (mp-cur)*i
    tot+=add
    print(f"{name[:70]:70s} mature AY16-19 avg dev {mp:+.1%}; further dev implied for AY21-25 {add:+,.0f}")
print(f"TOTAL implied further development AY2021-2025 {tot:+,.0f}; per year {tot/5:+,.0f}")
open('immaturity_load.txt','w').write(str(round(tot/5)))
