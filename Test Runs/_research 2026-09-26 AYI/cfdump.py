import re, sys, io, glob
def section(fn):
    t=open(fn,encoding='utf-8').read()
    best=None
    for m in re.finditer(r'CONSOLIDATED STATEMENTS OF CASH FLOWS',t):
        seg=t[m.start():m.start()+12000]
        if re.search(r'(?i)operating activities',seg[:1500]) and re.search(r'(?i)net (income|earnings)',seg[:3000]):
            best=seg; break
    if not best: return None
    e=best.find('accompanying')
    return best[:e if e>0 else 8000]
if __name__=='__main__':
  sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
  for fn in sys.argv[1:]:
    s=section(fn)
    print('=====',fn)
    if not s: print('NONE'); continue
    for line in s.split('\n'):
        l=re.sub(r'\s*\|\s*',' ',line); l=re.sub(r'\$ ?','',l); l=re.sub(r'\(\s*','(',l); l=re.sub(r'\s*\)',')',l); l=re.sub(r'\s+',' ',l).strip()
        if l: print('  ',l[:160])
