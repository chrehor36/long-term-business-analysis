p=r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-09-26 Run - MLI Mueller Industries.md'
L=open(p,encoding='utf-8').read().split('\n')
s=[i for i,l in enumerate(L) if l.startswith('## Q3 — ARE THEY HONEST')]
e=[i for i,l in enumerate(L) if l.startswith('- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**')]
assert len(s)==1, s
e=[i for i in e if i>s[0]]
print(s,e)
end=e[-1]  # the Q6 verdict line
assert L[end+2]=='---' and L[end+3]=='## SELF-AUDIT', L[end:end+4]
new=open('_beneath.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:s[0]]+new+L[end+1:]
open(p,'w',encoding='utf-8',newline='\n').write('\n'.join(L))
print('spliced', len(L))
