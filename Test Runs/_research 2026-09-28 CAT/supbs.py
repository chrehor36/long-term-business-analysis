import re,sys,json
sys.stdout.reconfigure(encoding='utf-8')
def doc(y):
    f=f'cache/x13_{y}.txt' if y<=2014 else f'cache/k_{y}.txt'
    return open(f,encoding='utf-8').read()
def nums(s,n=8):
    s=s.replace('( ','(').replace(' )',')')
    toks=re.findall(r'\(?[\d,]+\)?|—',s)
    out=[]
    for t in toks[:n]:
        if t=='—': out.append(0.0)
        else:
            v=float(t.strip('()').replace(',',''))
            out.append(-v if t.startswith('(') else v)
    return out
L={'sales':r'Sales of Machinery[^0-9(—]{0,60}','oprof':r'Operating profit','cash':r'Cash and (?:short-term investments|cash equivalents)','stb':r'Short-term borrowings','ltd1':r'Long-term debt due within one year','ltd2':r'Long-term debt due after one year','inv':r'Investment in Financial Products subsidiaries','eq':r"Total (?:shareholders|stockholders)['’] equity",'ta':r'Total assets','gw':r'Goodwill'}
res={}
for y in range(2005,2026):
    t=re.sub(r'[\s|$]+',' ',doc(y))
    out={}
    i=[m.start() for m in re.finditer(r'Supplemental [Dd]ata for (?:Consolidated )?Results of Operations',t)]
    j=[m.start() for m in re.finditer(r'Supplemental [Dd]ata for (?:Consolidated )?(?:Statement of )?Financial Position',t)]
    if i:
        blk=t[i[0]:i[0]+12000]
        hdr=re.search(r'\(Millions of dollars\)((?: \d{4}){4,12})',blk)
        out['ro_hdr']=hdr.group(1) if hdr else ''
        for k in ['sales','oprof']:
            m=re.search(L[k],blk)
            if m: out[k]=nums(re.sub(r'^[^\d(—]*','',blk[m.end():m.end()+220]),12)
    if j:
        blk=t[j[0]:j[0]+15000]
        hdr=re.search(r'((?: \d{4}){4,12})',blk[:600])
        out['bs_hdr']=hdr.group(1) if hdr else ''
        for k in ['cash','stb','ltd1','ltd2','inv','eq','ta','gw']:
            m=re.search(L[k],blk)
            if m: out[k]=nums(re.sub(r'^[^\d(—]*','',blk[m.end():m.end()+200]),8)
    res[y]=out
    print(y,out)
json.dump(res,open('supbs.json','w'))
