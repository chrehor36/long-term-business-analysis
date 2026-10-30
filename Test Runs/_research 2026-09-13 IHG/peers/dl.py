import sys, json, os
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 IHG')
import edgar
P = {'MAR':1048286,'HLT':1585689,'H':1468174,'WH':1722684,'CHH':1046311}
L = json.load(open('tenk_list.json'))
L['H'] += [['10-K','2020-12-31','2021-02-18','0001468174-21-000011','h-20201231.htm'],['10-K','2019-12-31','2020-02-20','0001468174-20-000015','h10-k123119.htm']]
meta = {}
for t,c in P.items():
    for form, rd, fd, acc, doc in L[t]:
        if form != '10-K': continue
        fy = rd[:4]
        if fy not in ('2019','2020','2021','2024','2025'): continue
        url = f"https://www.sec.gov/Archives/edgar/data/{c}/{acc.replace('-','')}/{doc}"
        fn = f'{t}_10K_FY{fy}.txt'
        try:
            txt = edgar.strip_html(edgar.get(url))
        except Exception as e:
            print('ERROR', t, fy, url, e); continue
        open(fn,'w',encoding='utf-8').write(txt)
        meta[fn] = {'accession':acc,'filed':fd,'url':url}
        print(fn, len(txt), acc, fd)
json.dump(meta, open('tenk_meta.json','w'), indent=1)
