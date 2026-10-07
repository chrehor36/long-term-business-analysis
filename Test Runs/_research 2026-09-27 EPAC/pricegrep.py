import re,glob
exec(open('seg2.py').read().split('if __name__')[0])
out=open('price_sentences.txt','w',encoding='utf-8')
for f in sorted(glob.glob('filings/*_10-K_*.txt'))+sorted(glob.glob('filings/*_10-Q_*.txt')):
    s=flat(f)
    a=s.find("Management's Discussion"); 
    m=[x.start() for x in re.finditer(r"(?i)Item 7\.? ?Management",s)]
    st=m[-1] if m else 0
    en=s.find('Item 8',st+100) if m else len(s)
    if en<0: en=len(s)
    body=s[st:en] if m else s
    sents=re.split(r'(?<=[.;])\s+',body)
    out.write('===== %s\n'%f)
    for x in sents:
        if re.search(r'(?i)pric(e|ing)',x) and re.search(r'(?i)industrial|IT&S|tool|segment|margin|sales|gross',x) and len(x)<900:
            out.write('  - '+x.strip()+'\n')
