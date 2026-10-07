P='../2026-09-27 Run - NUE Nucor.md'
q=open('q2.md',encoding='utf-8').read()
reps=[('NUE ahead in 10 of 17 years, STLD in 7','NUE ahead in 9 of 17 years, STLD in 8'),
('*"a remarkable textile company — but not a remarkable business"*','*"a remarkable textile company - but not a remarkable business"*'),
('**Answer:** the average is made by nine years; the other nineteen average less than 8.7%, the twenty non-boom years 8.7%.','**Answer:** the average is made by the supply-tight years; the twenty years outside the two booms (2004-2008, 2021-2023) average 8.7%.')]
for a,b in reps:
    assert q.count(a)==1,a
    q=q.replace(a,b)
open('q2.md','w',encoding='utf-8').write(q)
t=open(P,encoding='utf-8').read()
a=t.index('- Needed or desired [ ] · no close substitute [ ] · not price-regulated [ ]')
b=t.index('## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?')
t=t[:a]+q+t[b:]
open(P,'w',encoding='utf-8').write(t); print('ok')
