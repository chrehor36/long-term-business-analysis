import re,glob
out=open('cf_blocks.txt','w',encoding='utf-8')
for fn in sorted(glob.glob('tenk_*.txt')):
    s=open(fn,encoding='utf-8').read()
    s=re.sub(r'[\s|$]+',' ',s)
    ms=[m.start() for m in re.finditer(r'(?i)Net cash provided by (\(used in\) )?operating activities',s)]
    pick=None
    for p in ms:
        if re.search(r'(?i)investing activities',s[p:p+400]) and re.search(r'(?i)Cash flows from operating activities',s[max(0,p-6000):p]):
            pick=p
    if pick is None: out.write(f'== {fn} NONE\n'); continue
    a=s.rfind('ash flows from operating activities',0,pick)
    b=s.find('Supplemental',pick); b=pick+4000 if b<0 or b-pick>6000 else b+600
    out.write(f'== {fn}\n'+s[a-300:b]+'\n\n')
out.close()
