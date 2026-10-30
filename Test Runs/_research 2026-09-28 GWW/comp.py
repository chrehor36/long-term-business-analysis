import glob,re
files=sorted(glob.glob('cache/k19*_full.txt')+glob.glob('cache/k20*10k*.txt')+glob.glob('cache/k20*gww-20*.htm.txt'))
files=[f for f in files if 'xex' not in f]
out=open('competition_by_year.txt','w',encoding='utf-8')
for f in files:
    L=open(f,encoding='utf-8').read().split('\n')
    L=[l for l in L if l.strip()]
    hits=[i for i,l in enumerate(L) if re.match(r'^\s*COMPETITION\s*$',l,re.I)]
    out.write(f'\n===== {f} hits {hits}\n')
    for i in hits[-1:]:
        txt=' '.join(x.strip() for x in L[i+1:i+14])
        # stop at next all-caps heading-like line
        out.write(txt[:2500]+'\n')
out.close()
