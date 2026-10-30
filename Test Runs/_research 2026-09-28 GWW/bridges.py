import glob,re
out=open('bridges_out.txt','w',encoding='utf-8')
files=sorted(glob.glob('cache/k20*10k*.txt')+glob.glob('cache/k200[0-9]_*.txt')+glob.glob('cache/k20[12]*gww-20*.htm.txt')+glob.glob('cache/k199*_full.txt'))
seen=set()
for f in files:
    if f in seen or 'xex' in f: continue
    seen.add(f)
    L=[l.strip() for l in open(f,encoding='utf-8').read().split('\n') if l.strip()]
    out.write(f'\n##### {f}\n')
    for i,l in enumerate(L):
        if re.search(r'consisted of the following|comprised of the following|consisted of:',l):
            # gather next 30 lines compactly
            blk=' '.join(L[i:i+30])
            blk=re.sub(r'\s*\|\s*',' ',blk)
            out.write('>> '+L[i-0][:250]+'\n   '+blk[len(L[i]):len(L[i])+400]+'\n')
out.close()
