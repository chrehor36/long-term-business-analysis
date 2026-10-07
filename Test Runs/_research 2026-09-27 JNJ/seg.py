import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in range(2015,2026):
    t=open(f'cache/tenk_{y}.txt',encoding='utf-8').read()
    i=t.lower().find('income before tax by segment of business was as follows')
    if i<0: i=t.lower().find('income before tax by segment')
    seg=t[i:i+1400]
    seg=re.sub(r'[|\n]+',' ',seg); seg=re.sub(r'\s+',' ',seg)
    print(y, seg[:900]); print()
