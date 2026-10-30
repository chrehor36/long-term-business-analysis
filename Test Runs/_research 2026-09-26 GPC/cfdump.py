import re
out=open('cf_blocks.txt','w',encoding='utf-8')
for y in range(2006,2026):
    s=open(f'tenk_{y}-12-31.txt',encoding='utf-8').read()
    s=re.sub(r'[\s|$]+',' ',s)
    ms=[m.start() for m in re.finditer(r'Net cash provided by operating activities',s)]
    # statement = the occurrence followed within 3000 chars by 'Investing activities' and preceded by 'Operating activities'
    pick=None
    for p in ms:
        if re.search(r'(?i)investing activities',s[p:p+600]) and re.search(r'(?i)operating activities:?',s[max(0,p-5000):p]):
            pick=p
    if pick is None and ms: pick=ms[-1]
    if pick is None: out.write(f'== {y} NONE\n'); continue
    a=s.rfind('perating activities',0,pick-200)
    a=max(a-400,pick-5000)
    b=s.find('Cash paid',pick); b=pick+4500 if b<0 or b-pick>6000 else b+400
    out.write(f'== {y}\n'+s[a:b]+'\n\n')
out.close()
