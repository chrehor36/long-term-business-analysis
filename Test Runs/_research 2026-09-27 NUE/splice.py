P='../2026-09-27 Run - NUE Nucor.md'
t=open(P,encoding='utf-8').read()
a='The five answers above are what survived.'
assert t.count(a)==1; t=t.replace(a,'The six answers above are what survived.')
b=open('body_close.md',encoding='utf-8').read()
x='(five items, Q2)'; assert b.count(x)==1; b=b.replace(x,'(six items, Q2, including the one year, 2022, that runs against the reading)')
i=t.index('## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?')
t=t[:i]+b
open(P,'w',encoding='utf-8').write(t); print('ok', len(t.splitlines()))
