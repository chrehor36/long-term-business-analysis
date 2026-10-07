p='Test Runs/2026-09-27 Run - ARCB ArcBest.md'
s=open(p,encoding='utf-8').read()
b=open('Test Runs/_research 2026-09-27 ARCB/body_rest.md',encoding='utf-8').read()
assert 'RECORDED BENEATH THE CLOSE' not in s
s=s.rstrip('\n')+'\n'+b
open(p,'w',encoding='utf-8').write(s)
print(len(s.splitlines()))
