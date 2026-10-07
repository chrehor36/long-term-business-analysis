import re,sys,glob
for f in sorted(glob.glob('10K_filed*.txt'))+['10K_FY2025.txt']:
    L=[l.strip() for l in open(f,encoding='utf-8') if l.strip()]
    txt='\n'.join(L)
    txt=re.sub(r'\n(?=[-0-9(),.\$%—� ]+(\n|$))',' ',txt)
    print('=====',f)
    seen=set()
    for m in re.finditer(r'\n([A-Z][A-Za-z,&\s]{3,60}) Segment\n', txt):
        name=m.group(1).strip()
        seg=txt[m.end():m.end()+1500]
        sm=re.search(r'\nSales \$[^\n]*',seg)
        if not sm or sm.start()>500 or name in seen: continue
        seen.add(name)
        hdr=re.search(r'\n[^\n]*20\d\d 20\d\d[^\n]*',seg[:sm.start()+1])
        em=[l for l in seg.split('\n') if l.startswith(('Operating earnings','Earnings before interest','Earnings (loss)','Operating loss','Operating earnings (loss)'))]
        print(name,'|',(hdr.group(0).strip() if hdr else ''),'|',sm.group(0).strip(),'|',' || '.join(e[:170] for e in em[:3]))
