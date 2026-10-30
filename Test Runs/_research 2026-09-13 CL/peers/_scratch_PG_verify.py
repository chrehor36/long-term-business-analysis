import re,sys
sys.stdout.reconfigure(encoding='utf-8')
L=open('SECTION_PG.md',encoding='utf-8').read().split('\n')
norm=lambda s:re.sub(r'\s+',' ',s).strip()
cache={}
bad=0;n=0
for i,l in enumerate(L):
    if l.startswith('> '):
        m=re.match(r'Source: (\S+) line (\d+)',L[i+1]) if i+1<len(L) else None
        if not m: print('NO SOURCE',i,l[:80]); bad+=1; continue
        f=m.group(1)
        if f not in cache: cache[f]=norm(open(f,encoding='utf-8').read())
        n+=1
        if norm(l[2:]) not in cache[f]: print('MISS',i,l[:100]); bad+=1
    elif '—' in l or '–' in l:
        print('DASH in prose',i,l[:150])
print('quotes',n,'bad',bad)
