import os, time
from fetch import get
from tables import flat
cik='1001385'
rows=[l.split() for l in open('sub_list.txt') if ' 10-K ' in l or ' 10-K405 ' in l]
for r in rows:
    fd, form, acc, doc, rep = r[0], r[1], r[2], (r[3] if len(r)>4 else ''), r[-1]
    if not doc.endswith('.htm') and not doc.endswith('.txt'): 
        print('nodoc', r); continue
    out=f'cache/k{rep[:4]}.txt'
    if os.path.exists(out): continue
    try:
        b=get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}')
    except SystemExit as e:
        print('FAIL', rep, e); continue
    open(out,'w',encoding='utf-8').write(flat(b)); print(out, acc, len(b)); time.sleep(0.5)
