import re,sys,glob
for f in sorted(glob.glob('cache/10K_FY20*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t).replace('�','"')
    print('#####',f)
    for kw in sys.argv[1:]:
        ms=list(re.finditer(kw,t,flags=re.I))
        for m in ms[:2]:
            print('  --',kw,':',t[max(0,m.start()-150):m.start()+450])
