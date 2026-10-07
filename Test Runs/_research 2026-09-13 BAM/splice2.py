RUN=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - BAM Brookfield Asset Management.md"
t=open(RUN,encoding='utf-8').read()
def rd(f): return open(f,encoding='utf-8').read()
s=t.index('## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?')
head=t[:s]
body = rd('q3_final.md')+'\n'+rd('q4_final.md')+'\n'
body += '---\n\u26d4 **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close\nthe file; neither is a pass. **Q2 returned OUT, so what follows is headed as a computation, per\noperator rule 3.**\n\n---\n'
body += rd('q5_final.md')+'\n'+rd('q6_final.md')+'\n'+rd('audit_final.md')
open(RUN,'w',encoding='utf-8').write(head+body)
n=(head+body).count(chr(10))+1
print('lines now',n)
for ph in ['__Q3HEADER__','__Q4HEADER__','__CLOSEQ__','__Q2SHORT__','__Q6Q2__','__Q3GATENOTE__','__Q4VERDICTLABEL__','__Q3VERDICTNOTE__','____']:
    c=(head+body).count(ph)
    print(ph, c, 'OK' if c==0 else 'LEFT')
