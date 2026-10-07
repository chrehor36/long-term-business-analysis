import io,sys
# usage: splice.py runfile bodyfile start_heading end_heading
rf,bf,a,b=sys.argv[1:5]
t=io.open(rf,encoding='utf-8').read(); body=io.open(bf,encoding='utf-8').read()
L=t.split('\n')
ia=[i for i,l in enumerate(L) if l.startswith(a)]; ib=[i for i,l in enumerate(L) if l.startswith(b)]
assert len(ia)==1 and len(ib)==1 and ia[0]<ib[0], (ia,ib)
new=L[:ia[0]]+body.rstrip('\n').split('\n')+['']+L[ib[0]:]
io.open(rf,'w',encoding='utf-8',newline='\n').write('\n'.join(new))
print('spliced',a,'->',b,len(L),'->',len(new))
