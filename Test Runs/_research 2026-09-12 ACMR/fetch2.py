import urllib.request, os, time, re, html as H
UA={"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
OUT="Test Runs/_research 2026-09-12 ACMR"
CIK="1680062"
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read()
        except Exception as e: time.sleep(3)
    return b""
def txt(s):
    s=re.sub(r"(?is)<(script|style).*?</\1>"," ",s)
    s=re.sub(r"(?is)</t[dh]>"," | ",s); s=re.sub(r"(?is)</tr>","\n",s)
    s=re.sub(r"(?is)<(p|div|br|li|h[1-6])[^>]*>","\n",s); s=re.sub(r"(?is)<[^>]+>"," ",s)
    s=H.unescape(s).replace("\u00a0"," ").replace("\u2019","'")
    s=re.sub(r"[ \t]+"," "); return s
jobs=[("0001140361-26-020717","ef20073127_8k.htm","8K_20260512_body.htm"),
 ("0001140361-26-020717","ef20073127_ex10-1.htm","8K_20260512_ex10-1.htm"),
 ("0001140361-26-021661","ef20073887_8k.htm","8K_20260515_body.htm"),
 ("0001140361-26-023310","ef20075131_8k.htm","8K_20260529_body.htm"),
 ("0001140361-26-023310","ef20075131_ex99-1.htm","8K_20260529_ex99-1.htm"),
 ("0001628280-26-054581","acmr-q22026xearningsreleas.htm","EX991_2026Q2.htm"),
 ("0001628280-26-031688","acmr-q12026xearningsreleas.htm","EX991_2026Q1.htm"),
 ("0001628280-26-011998","acmr-q42025xearningsreleas.htm","EX991_2025Q4.htm"),
 ("0001680062-26-000020","a25_acmshxresultsofshareho.htm","8K_20260206_ACMSH_results.htm"),
 ("0001680062-26-000012","a22release_acmsh-pricingof.htm","8K_20260202_ACMSH_pricing.htm"),
 ("0001680062-26-000009","acmsh-shareholderinquiryxb.htm","8K_20260130_ACMSH_inquiry.htm"),
 ("0001628280-26-020846","acmsh2025proposedprofitdis.htm","8K_20260324_ACMSH_profitdist.htm"),
 ("0001628280-26-025599","a417_indicativexannounceme.htm","8K_20260417_indicative.htm"),
 ("0001628280-26-027353","a427_acmrprelimq12026reven.htm","8K_20260427_prelimQ1.htm"),
 ("0001628280-26-019811","acmr-20260313.htm","8K_20260313_body.htm"),
 ("0001628280-26-042833","acmr-20260610.htm","8K_20260610_body.htm"),
 ("0001628280-26-059251","acmr-20260817.htm","8K_20260817_body.htm"),
]
for a,n,o in jobs:
    b=get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a.replace('-','')}/{n}")
    open(os.path.join(OUT,o),"wb").write(b); print(o,len(b)); time.sleep(0.3)
