import io,sys,re; sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
f=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
L=open(f,encoding='utf-8').read().split('\n')[a:b]
txt='\n'.join(L)
# tokenise
toks=re.findall(r'\(\s*[\d,\.]+\s*\)?|[\d][\d,\.]*|—|[A-Za-z][^|\n\$\d\(—]*',txt)
rows=[];cur=None
for t in toks:
    t=t.strip()
    if not t: continue
    if re.match(r'[A-Za-z]',t):
        if cur and not cur[1] : cur[0]+=' '+t
        else:
            cur=[t,[]]; rows.append(cur)
    else:
        if cur is None: continue
        v=t.replace(',','').replace(' ','')
        if v=='—': cur[1].append(0.0); continue
        neg=v.startswith('(')
        v=v.strip('()')
        try: x=float(v)
        except: continue
        cur[1].append(-x if neg else x)
for r in rows:
    if r[1]: print('%-90s %s'%(r[0][:90], r[1]))
