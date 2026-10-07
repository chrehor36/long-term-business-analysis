import re,glob
for fn in sorted(glob.glob('tenk_*.txt'))+['q2606_kex-20260630.htm.txt']:
    t=re.sub(r'\s+',' ',open(fn,encoding='utf-8').read())
    print('=====',fn)
    seen=set()
    for m in re.finditer(r'[^.]{0,250}(marine transportation|inland|coastal)[^.]{0,120}operating margin[^.]{0,250}\.',t,re.I):
        s=m.group(0).strip()
        if s[:80] in seen or len(s)>700: continue
        seen.add(s[:80]); print(' -',s)
