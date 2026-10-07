import json, urllib.request, time, re, html, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url):
    for k in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=90); time.sleep(0.15); return r.read()
        except Exception as e: print('retry',url,e); time.sleep(2)
    raise
def totext(b):
    s=b.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</(p|div|tr|li|h\d|table)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    return s
for name,cik in [('MBUU',1590976),('MCFT',1638290)]:
    d=json.load(open(f'raw/{name}_sub.json')); r=d['filings']['recent']
    for i in range(len(r['form'])):
        f,fd,acc,doc=r['form'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i]
        a=acc.replace('-','')
        if f=='10-K':
            fy=int(doc.split('20')[-1][:2]) if False else None
            yr=int(fd[:4]) if fd[5:7]>='07' else int(fd[:4])-1
            lo=2017 if name=='MBUU' else 2019
            if yr<lo: continue
            out=f'raw/{name}_10K_FY{yr}.txt'
            if os.path.exists(out): continue
            url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}'
            open(out,'w',encoding='utf-8').write(f'{url} | {f} filed {fd} | accession {acc}\n'+totext(get(url)))
            print(out)
        if name=='MBUU' and f=='8-K' and fd>='2024-07-01':
            idx=json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json'))
            for it in idx['directory']['item']:
                n=it['name']
                if re.search(r'ex99|ex-99|exhibit99|ex_99',n,re.I) and n.endswith(('.htm','.html','.txt')):
                    out=f'raw/MBUU_8K_{fd}_{n}.txt'
                    if os.path.exists(out): continue
                    url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{n}'
                    open(out,'w',encoding='utf-8').write(f'{url} | 8-K filed {fd} | accession {acc}\n'+totext(get(url)))
                    print(out)
                elif re.search(r'ex99',n,re.I): print('nontext exhibit',fd,n)
