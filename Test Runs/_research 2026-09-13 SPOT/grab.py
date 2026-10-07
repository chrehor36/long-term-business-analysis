# usage: python grab.py REGEX N  -> for every 20F_*.txt, print N chars after the LAST match (compressed)
import sys, io, re, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
pat=sys.argv[1]; n=int(sys.argv[2]); which=sys.argv[3] if len(sys.argv)>3 else 'last'
for fn in sorted(glob.glob('20F_FY20[12][0-9].txt'))+['20F_FY2025__ck0001639920-20251231.txt']:
    t=open(fn,encoding='utf-8').read()
    ms=list(re.finditer(pat,t))
    if not ms: print('##',fn,'none'); continue
    m = ms[-1] if which=='last' else ms[0]
    s=t[m.start():m.start()+n]
    s=re.sub(r'[\s|/]*\n[\s|/]*',' ',s); s=re.sub(r'(\s*\|\s*)+',' | ',s); s=re.sub(r'\(\s*(\d[\d,]*)\s*\|?\s*\)',r'(\1)',s)
    print('##',fn,len(ms)); print(s)
