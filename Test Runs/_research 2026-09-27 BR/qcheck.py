import re,glob,sys,csv
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"').replace('�',"'")).strip()
corpus=' '.join(norm(open(f,encoding='utf-8',errors='replace').read()) for f in glob.glob('*.txt'))
led=' '.join(norm(r['quote_verbatim']) for r in csv.DictReader(open('../../principle_ledger.csv',encoding='utf-8')))
fw=norm(open('../../Framework/THE FRAMEWORK v4.md',encoding='utf-8').read())
for b in sys.argv[1:]:
    t=open(b,encoding='utf-8').read()
    for q in re.findall(r'\*"(.+?)"\*',t):
        parts=[norm(p).strip(' .') for p in re.split(r'\.\.\.|…|\[\.\.\.\]',q) if len(p.strip())>8]
        miss=[p for p in parts if p not in corpus and p not in led and p not in fw]
        if miss: print('MISSING in',b,'::',q[:150],'|| part:',miss[0][:120])
print('done')
