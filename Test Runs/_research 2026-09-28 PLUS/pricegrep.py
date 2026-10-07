import glob,re,sys
sys.stdout.reconfigure(encoding='utf-8')
pats=[r'compete principally based on price',r'margins may not be maintainable',r'downward pressure on (?:product )?pricing',r'pricing pressure',r'competitive pricing',r'price competition',r'lower (?:selling )?prices',r'sell products as commodities',r'reduce(?:d)? (?:our )?prices',r'price reductions?',r'terminable by either party']
out=open('price_sentences.txt','w',encoding='utf-8')
for p in sorted(glob.glob('cache/k_20*.txt')):
    s=re.sub(r'\s+',' ',open(p,encoding='utf-8').read())
    sents=re.split(r'(?<=[.!?])\s+',s)
    seen=set()
    for x in sents:
        for pt in pats:
            if re.search(pt,x,re.I) and x not in seen:
                seen.add(x); out.write(p[8:18]+' | '+x[:600]+'\n')
out.close()
