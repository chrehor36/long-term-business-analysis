import re,glob,os,sys
sys.stdout.reconfigure(encoding='utf-8')
pats=[r'competitors periodically reduce their prices',r'competitive pricing',r'pricing environment[^.]{0,80}(competitive|aggressive|difficult|challeng)',r'(tight|tighter|tightening) capacity',r'excess capacity',r'nonunion[^.]{0,60}(lower|cost)',r'highest benefit contribution',r'price (reduction|decrease|concession)',r'rational']
files=['cache/ex03_d13042exv13.txt.txt','cache/ex05_d33393exv13.htm.txt']+sorted(glob.glob('cache/tenk_20*.txt'))
out=open('price_sentences.txt','w',encoding='utf-8')
for f in files:
    s=open(f,encoding='utf-8').read().replace('​',' ')
    s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\s+',' ',s)
    sents=re.split(r'(?<=[.])\s+(?=[A-Z])',s)
    cnt={p:0 for p in pats}
    out.write('===== %s\n'%os.path.basename(f))
    seen=set()
    for x in sents:
        for p in pats:
            if re.search(p,x,re.I):
                cnt[p]+=1
                if x not in seen and len(x)<900: out.write(' - '+x+'\n'); seen.add(x)
                break
    print(os.path.basename(f),[cnt[p] for p in pats])
