import sys,io
run,secfile,start,end=sys.argv[1:5]
t=io.open(run,encoding='utf-8').read()
new=io.open(secfile,encoding='utf-8').read()
a=[i for i,l in enumerate(t.split('\n')) if l.startswith(start)]
b=[i for i,l in enumerate(t.split('\n')) if l.startswith(end)]
assert len(a)==1 and len(b)==1 and a[0]<b[0], (a,b)
L=t.split('\n')
L=L[:a[0]]+new.rstrip('\n').split('\n')+['']+L[b[0]:]
io.open(run,'w',encoding='utf-8',newline='\n').write('\n'.join(L))
print('spliced',a[0],b[0])
