import fetch,re
L=["0000060667-26-000113","0000060667-26-000119","0000060667-26-000020","0001193125-25-224995","0001193125-25-208264","0000060667-25-000161","0000060667-25-000162","0000060667-25-000199","0000060667-26-000091","0000060667-26-000062"]
for acc in L:
    try:
        b=fetch.get('https://www.sec.gov/Archives/edgar/data/60667/'+acc.replace('-','')+'/'+acc+'-index.htm','idx_'+acc+'.htm').decode('utf-8','replace')
        docs=re.findall(r'href="(/Archives/edgar/data/60667/[^"]+\.htm)"',b)
        items=re.findall(r'Items?</b>[^<]*<[^>]*>([^<]*)',b)
        print(acc, re.findall(r'<div class="info">([^<]*)</div>',b)[:3], flush=True)
        for d in docs:
            name=d.split('/')[-1]
            t=fetch.doc(60667,acc,name,'8K_'+acc+'_'+name.replace('.htm',''))
            print('  ',name,len(t),flush=True)
    except Exception as e: print(acc,'ERR',e,flush=True)
