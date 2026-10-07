import glob,re,io
pat=re.compile(r'(price increase|pricing|promotion|discount|markdown|comparable net sales|comparable showroom|average order|price point|raise price|higher prices|lower prices)',re.I)
out=io.open('price_sentences.txt','w',encoding='utf-8')
for f in sorted(glob.glob('filings/*_10-K*.txt')):
    t=io.open(f,encoding='utf-8').read()
    # MD&A slice
    m=[x.start() for x in re.finditer(r"Management.s Discussion and Analysis of Financial Condition",t)]
    s=m[1] if len(m)>1 else (m[0] if m else 0)
    e=t.find('Quantitative and Qualitative Disclosures',s+100)
    seg=t[s:e if e>0 else s+80000]
    out.write('\n########## %s (MD&A chars %d)\n'%(f,len(seg)))
    seen=set()
    for sent in re.split(r'(?<=[.!?])\s+',seg):
        if pat.search(sent) and len(sent)<1500:
            k=sent.strip()[:200]
            if k in seen: continue
            seen.add(k); out.write('- '+sent.strip().replace('\n',' ')+'\n')
out.close()
