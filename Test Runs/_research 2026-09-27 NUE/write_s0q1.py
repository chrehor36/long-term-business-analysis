import io
P='../2026-09-27 Run - NUE Nucor.md'
t=open(P,encoding='utf-8').read()
old_s0=t[t.index('**Sovereign, for the currency the business EARNS in**'):t.index('---\n## Q1')]
new_s0=open('s0.md',encoding='utf-8').read()
t=t.replace(old_s0,new_s0,1)
old_q1=t[t.index('- Unit economics in my own words, no management language: ____'):t.index('## Q2 — IS IT A FRANCHISE?')]
new_q1=open('q1.md',encoding='utf-8').read()
t=t.replace(old_q1,new_q1,1)
open(P,'w',encoding='utf-8').write(t)
print('ok')
