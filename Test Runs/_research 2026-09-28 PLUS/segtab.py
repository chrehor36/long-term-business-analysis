import glob,re,sys
sys.stdout.reconfigure(encoding='utf-8')
yrs=sys.argv[1:]
for p in sorted(glob.glob('cache/k_20*.txt')):
    if yrs and p[8:12] not in yrs: continue
    s=open(p,encoding='utf-8').read()
    idx=[m.start() for m in re.finditer(r'SEGMENT REPORTING|Segment Reporting',s)]
    # take the last occurrence that is followed by a table w/ "Technology"
    best=None
    for i in idx:
        seg=s[i:i+9000]
        if 'Technology' in seg or 'technology' in seg: best=i
    if best is None: print(p,'none'); continue
    t=s[best:best+7000]
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t)
    print('#####',p[8:18]); print(t[:5000]); print()
