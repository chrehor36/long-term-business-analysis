import urllib.request, re, html, os, sys
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
def totext(b):
    t=b.decode("utf-8","replace")
    t=re.sub(r"(?is)<(script|style).*?</\1>"," ",t)
    t=re.sub(r"(?i)</(p|div|tr|br|li|h\d|table)>","\n",t)
    t=re.sub(r"(?i)<br\s*/?>","\n",t)
    t=re.sub(r"(?i)</t[dh]>"," | ",t)
    t=re.sub(r"<[^>]+>"," ",t)
    t=html.unescape(t).replace("\xa0"," ")
    t=re.sub(r"[ \t]+"," ",t)
    t=re.sub(r"\n\s*\n+","\n",t)
    return t
jobs=[("0001001085-26-000006","bn-20251231.htm","40F_main.txt"),
("0001001085-26-000006","bn-20251231_d2.htm","40F_d2.txt"),
("0001001085-26-000006","a2025-40xfex991aif.htm","40F_AIF.txt"),
("0001001085-26-000021","bn-20260630.htm","6K_Q2_2026.txt"),
("0001001085-26-000021","a2026-q26xkcover.htm","6K_Q2_2026_cover.txt"),
("0001171843-26-005886","exh_991.htm","6K_20260904_ex991.txt"),
("0001171843-26-005886","f6k_090326.htm","6K_20260904_cover.txt"),
("0001001085-26-000011","a2025-q46xkacover.htm","6KA_AR2025_cover.txt"),
]
if __name__=='__main__':
 for acc,fn,out in jobs:
    if os.path.exists(out): continue
    a=acc.replace("-","")
    b=get(f"https://www.sec.gov/Archives/edgar/data/1001085/{a}/{fn}")
    open(out,"w",encoding="utf-8").write(totext(b))
    print(out, len(b))
