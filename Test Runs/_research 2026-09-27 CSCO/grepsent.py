import re,sys
pat=re.compile(sys.argv[1],re.I)
for f in sys.argv[2:]:
    s=re.sub(r'\s+',' ',open(f,encoding='utf-8',errors='ignore').read())
    sents=re.split(r'(?<=[.;]) ',s)
    hits=[x for x in sents if pat.search(x)]
    print('===',f[:60],len(hits))
    for h in hits[:int(__import__('os').environ.get('N','6'))]: print('  -',h[:600])
