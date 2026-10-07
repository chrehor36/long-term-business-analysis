import re,html,os
from fetch import get
docs=[("FY2025","000070754925000075","lrcx-20250629.htm"),
("FY2024","000070754924000106","lrcx-20240630.htm"),
("FY2023","000070754923000102","lrcx-20230625.htm"),
("FY2022","000070754922000107","lrcx-20220626.htm"),
("FY2021","000070754921000136","lrcx-20210627.htm"),
("FY2020","000070754920000138","lrcx10k2020document.htm"),
("FY2019","000070754919000124","lrcx10k2019document.htm"),
("FY2018","000070754918000115","lrcx_10kx2018xdocument.htm"),
("FY2016","000070754916000050","lrcx_10kx2016xdocument.htm")]
for fy,acc,doc in docs:
    out=f"10K_{fy}.txt"
    if os.path.exists(out): print('skip',out); continue
    u=f"https://www.sec.gov/Archives/edgar/data/707549/{acc}/{doc}"
    try:
        d=get(u).decode('utf-8',errors='replace')
    except Exception as e:
        print('FAIL',fy,e); continue
    txt=re.sub(r'<[^>]+>',' ',d); txt=html.unescape(txt); txt=re.sub(r'[ \t\xa0]+',' ',txt)
    open(out,'w',encoding='utf-8').write(txt)
    print(out,len(txt))
