import re,glob
for f in sorted(glob.glob('flat/*10-K*.txt')):
    s=re.sub(r'\s+',' ',open(f,encoding='utf-8',errors='ignore').read())
    sents=re.split(r'(?<=\.) ',s)
    hits=[x for x in sents if re.search(r'(?i)(product gross margin|total gross margin|gross margin percentage)',x) and re.search(r'(?i)pric',x)]
    neg=sum(1 for x in hits if re.search(r'(?i)(negative|unfavorable|adverse)[^.]{0,40}pric|pric[^.]{0,30}(declin|erosion|pressure)',x))
    pos=sum(1 for x in hits if re.search(r'(?i)favorable pricing|pricing benefit|price increases',x) and not re.search(r'(?i)unfavorable pricing',x))
    first=hits[0][:330] if hits else ''
    print(f[5:15], 'neg',neg,'pos',pos,'|',first)
