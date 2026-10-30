"""Print the operating and investing sections of each filed cash-flow statement, compacted. Transcription only."""
import re,sys
files=['tenk_FY2011_ex13.txt','tenk_FY2014.txt','tenk_FY2017.txt','tenk_FY2020.txt','tenk_FY2023.txt','tenk_FY2026.txt']
for f in files:
    L=open(f,encoding='utf-8').read().split('\n')
    idx=[i for i,l in enumerate(L) if 'TOTAL OPERATING ACTIVITIES' in l]
    if not idx: print(f,'NO CF'); continue
    n=idx[0]
    # start at the statement heading
    s=max(i for i in range(n) if re.search(r'(?i)OPERATING ACTIVITIES',L[i]) and 'TOTAL' not in L[i])
    s=max(i for i in range(s-15,s) if re.search(r'(?i)cash',L[i])) if any(re.search(r'(?i)cash',L[i]) for i in range(s-15,s)) else s
    e=[i for i in range(n,len(L)) if 'TOTAL INVESTING ACTIVITIES' in L[i]][0]
    txt=' '.join(x.strip() for x in L[s-3:e+1] if x.strip() not in ('','|'))
    txt=re.sub(r'\s*\|\s*',' ',txt); txt=re.sub(r'\(\s+',"(",txt); txt=re.sub(r'\s+\)',")",txt)
    print('=====',f,'line',s-2,'to',e+1); print(txt); print()
