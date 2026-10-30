import os
p=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-20 Run - EMBC Embecta.md"
d=r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-20 EMBC"
s=open(p,encoding='utf-8').read()
a=s.index("## Q3 \u2014 ARE THEY HONEST, AND ARE THEY RATIONAL?")
new=open(os.path.join(d,"_tail.md"),encoding='utf-8').read()
s=s[:a]+new
open(p,'w',encoding='utf-8').write(s)
print("ok",len(s))
