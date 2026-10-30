import re,sys,glob
for f in sys.argv[1:]:
    s=re.sub(r'\s+',' ',open(f,encoding='utf-8').read())
    sents=re.split(r'(?<=\.) ',s)
    hits=[x for x in sents if 'Cisco' in x]
    print('===',f,len(hits))
    for h in hits[:6]: print('  ',h[:500])
