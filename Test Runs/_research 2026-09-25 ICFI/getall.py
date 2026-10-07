import json, re, os, time
from fetch import get, strip
B='https://www.sec.gov/Archives/edgar/data/1362004/'
docs=[('10K_FY2025','0001193125-26-082536','icfi-20251231.htm'),
('10K_FY2024','0000950170-25-029917','icfi-20241231.htm'),
('10K_FY2023','0000950170-24-021617','icfi-20231231.htm'),
('10K_FY2022','0000950170-23-005304','icfi-20221231.htm'),
('10K_FY2019','0001564590-20-007616','icfi-10k_20191231.htm'),
('10K_FY2016','0001437749-17-003385','icfi20161231_10k.htm'),
('10Q_2026Q2','0001193125-26-338422','icfi-20260630.htm'),
('DEF14A_2026','0001140361-26-016102','ny20066983x1_def14a.htm')]
for name,acc,doc in docs:
    out=name+'.txt'
    if os.path.exists(out): continue
    b=get(B+acc.replace('-','')+'/'+doc); open(out,'w',encoding='utf-8').write(strip(b)); print(out,os.path.getsize(out)); time.sleep(0.5)
# 8-K exhibits since 2025-10
eks=[('20260924','0001437749-26-031146'),('20260806','0001193125-26-337985'),('20260625','0001437749-26-021699'),('20260624','0001437749-26-021568'),('20260507','0001193125-26-211897'),('20260416','0001437749-26-012565'),('20260326','0001437749-26-009949'),('20260305','0001437749-26-007070'),('20260226','0001193125-26-076573'),('20260115','0001437749-26-001353'),('20251030a','0001437749-25-032425'),('20251030b','0001193125-25-258534'),('20250917','0001437749-25-029287'),('20250731','0000950170-25-100892'),('20250617','0001437749-25-020636'),('20250501','0000950170-25-061830'),('20250331','0001437749-25-010188'),('20250227','0000950170-25-029032')]
for d,acc in eks:
    ix=B+acc.replace('-','')+'/'+acc+'-index.htm'
    h=get(ix).decode('utf-8','ignore')
    links=re.findall(r'href="(/Archives/edgar/data/1362004/[^"]+\.htm)"',h)
    for L in links:
        fn=L.split('/')[-1]
        out='8K_'+d+'_'+fn.replace('.htm','.txt')
        if os.path.exists(out): continue
        b=get('https://www.sec.gov'+L); open(out,'w',encoding='utf-8').write(strip(b)); print(out,os.path.getsize(out)); time.sleep(0.3)
