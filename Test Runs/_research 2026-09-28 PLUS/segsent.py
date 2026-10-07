import glob,re,sys
sys.stdout.reconfigure(encoding='utf-8')
for p in sorted(glob.glob('cache/k_20*.txt')):
    s=open(p,encoding='utf-8').read()
    m=re.search(r'[Tt]echnology segment accounted for[^.]*\.[^.]*\.',s)
    print(p[8:18], m.group(0)[:400] if m else '-')
