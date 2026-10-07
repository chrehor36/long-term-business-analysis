import re,glob
for fn in sorted(glob.glob('tenk_*.txt')):
    t=open(fn,encoding='utf-8').read()
    t=re.sub(r'\s+',' ',t)
    sents=re.split(r'(?<=[.;]) ',t)
    seen=set()
    print('=====',fn)
    for s in sents:
        if len(s)>900: continue
        if re.search(r'(term contract[^.]{0,120}(renew|pric)|spot contract rates|pricing on (inland )?term|rates on (inland )?term|average of approximately [0-9]+% ?(to|and)? ?[0-9]*%? (lower|higher)|contract rates? (on|for) )',s,re.I):
            k=s[:120]
            if k in seen: continue
            seen.add(k); print(' -',s.strip()[:700])
