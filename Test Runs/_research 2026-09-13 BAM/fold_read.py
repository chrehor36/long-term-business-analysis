R=r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
t=open(R,encoding='utf-8').read()
n=open('fold_narrative.md',encoding='utf-8').read()
if not t.endswith('\n'): t+='\n'
t=t+n
open(R,'w',encoding='utf-8').write(t)
print('lines',t.count(chr(10))+1)
