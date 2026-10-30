import glob,re
out=open('cf_text.txt','w',encoding='utf-8')
for fn in sorted(glob.glob('tenk_*.txt'))+['tenqt_2021-12-31.txt']:
    t=open(fn,encoding='utf-8').read()
    flat=re.sub(r'\s*\|\s*',' ',t); flat=re.sub(r'\s+',' ',flat)
    # find statement: the occurrence of 'Operating activities' followed within 6000 chars by 'Net cash provided by' and 'Investing'
    best=None
    for m in re.finditer(r'(?i)(CONSOLIDATED STATE ?M ?ENTS OF CASH FLOWS|STATEMENTS? OF CONSOLIDATED CASH FLOWS)',flat):
        seg=flat[m.start():m.start()+9000]
        if re.search(r'(?i)operating activities',seg) and re.search(r'(?i)investing activities',seg) and re.search(r'\d{3}\.\d',seg):
            best=seg; break
    out.write('\n\n===== '+fn+'\n'+(best or 'NOT FOUND'))
    print(fn, 'found' if best else 'NOT FOUND')
