import glob,re,io
out=io.open('price_sentences.txt','w',encoding='utf-8')
for f in sorted(glob.glob('filings/*10-K*.txt')):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\s+',' ',s)
    sents=re.split(r'(?<=[.;])\s+',s)
    hits=[x for x in sents if re.search(r'(selling price|price increase|pricing|price realization|prices? (were|was|increased|decreased|reduc)|lower prices|higher prices|pricing pressure|price competition|competitors?\b.{0,40}(include|such as|are ))',x,re.I) and len(x)<900 and 'XBRL' not in x and 'us-gaap' not in x]
    out.write('\n===== %s (%d)\n'%(f,len(hits)))
    seen=set()
    for h in hits:
        k=h[:120]
        if k in seen: continue
        seen.add(k); out.write('- '+h.strip()+'\n')
print(open('price_sentences.txt',encoding='utf-8').read()[:100])
