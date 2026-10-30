"""pg.py FILE.txt grep PATTERN  -> page:line hits ; pg.py FILE.txt page N [M] -> print pages N..M"""
import sys, re
sys.stdout.reconfigure(encoding="utf-8"); f=sys.argv[1]; mode=sys.argv[2]
pages=open(f,encoding='utf-8',errors='replace').read().split('\f')
if mode=='grep':
    pat=re.compile(sys.argv[3], re.I)
    for i,p in enumerate(pages,1):
        for ln in p.splitlines():
            if pat.search(ln): print(f"p{i}: {ln.strip()[:220]}")
else:
    a=int(sys.argv[3]); b=int(sys.argv[4]) if len(sys.argv)>4 else a
    for i in range(a,b+1):
        print(f"=================== PAGE {i}"); print(pages[i-1])
