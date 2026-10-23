import sys,re
f=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
t=' '.join(open(f,encoding='utf-8').read().split('\n')[a-1:b])
t=re.sub(r'[\s|]+',' ',t).replace('￦','W').replace('—','-')
for k in ['Transmission and distribution','Electric power generation (Nuclear)','Electric power generation (Non-nuclear)','Electric power generation (Non- nuclear)','Plant maintenance','Others','Consolidation adjustments','Total ']:
    t=t.replace(k,'\n'+k)
for L in t.split('\n'):
    print(L[:400].encode('ascii','replace').decode())
