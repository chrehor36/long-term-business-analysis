import re
out=open('comps_out.txt','w',encoding='utf-8')
for y in range(2012,2026):
    t=open(f'tenk_{y}.txt',encoding='utf-8').read()
    t=re.sub(r'\s+',' ',t)
    for m in re.finditer(r'[Dd]aily average comparable store sales (increased|decreased)[^|]{0,700}?transaction[^|]{0,400}?\.(?= [A-Z])', t):
        s=m.group(0)
        if f'September 30, {y}' in s[:160]:
            print(y, s[:900], file=out); print(file=out); break
    else:
        m=re.search(r'omparable store sales[^|]{0,300}?fiscal year '+str(y)+r'[^|]{0,500}', t)
        print(y,'NOMATCH', m.group(0)[:600] if m else '', file=out); print(file=out)
