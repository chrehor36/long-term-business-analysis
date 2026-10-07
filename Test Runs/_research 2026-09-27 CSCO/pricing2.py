import re,glob,json
out={}
for f in sorted(glob.glob('flat/*10-K*.txt')):
    if f<'flat/2004' : continue
    s=re.sub(r'\s+',' ',open(f,encoding='utf-8',errors='ignore').read())
    sents=re.split(r'(?<=\.) ',s)
    hits=[x for x in sents if re.search(r'(?i)^(the )?(lower |higher )?product gross margin( percentage)? (increased|decreased|declined|was)|product gross margin (increased|decreased|declined) by',x) and re.search(r'(?i)pric',x)]
    if not hits:
        hits=[x for x in sents if re.search(r'(?i)(product pricing|pricing reductions|sales discounts)',x) and re.search(r'(?i)gross margin',x) and 'may' not in x]
    if hits:
        out[f[5:15]]=hits[0][:520]; print(f[5:15],'|',hits[0][:520])
json.dump(out,open('pricing_sentences.json','w'),indent=1)
