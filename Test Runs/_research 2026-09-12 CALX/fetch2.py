import urllib.request, time, re, html, os
H={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
docs=[("10K_FY2022","0001406666-23-000026","calx-20221231.htm"),
      ("10K_FY2021","0001628280-22-003338","calx-20211231.htm"),
      ("10K_FY2020","0001406666-21-000029","calx-20201231.htm"),
      ("10K_FY2018","0001406666-19-000029","a2018form10-k.htm"),
      ("10K_FY2015","0001406666-16-000041","calx-20151231x10k.htm"),
      ("10K_FY2012","0001406666-13-000010","calx-20121231x10k.htm"),
      ("10K_FY2010","0001193125-11-045511","d10k.htm")]
def strip(h):
    h=re.sub(r"(?is)<(script|style).*?</\1>"," ",h)
    h=re.sub(r"(?is)</t[dh]>",r" | ",h)
    h=re.sub(r"(?is)</(tr|p|div|br|li|h[1-6])>","\n",h)
    h=re.sub(r"(?s)<[^>]+>"," ",h)
    h=html.unescape(h)
    h=re.sub(r"[ \t\xa0]+"," ",h)
    h=re.sub(r"\n\s*\n+","\n",h)
    return h
for name,acc,doc in docs:
    out=f"{name}__{doc.replace('.htm','')}.txt"
    if os.path.exists(out): print("have",out); continue
    a=acc.replace("-","")
    u=f"https://www.sec.gov/Archives/edgar/data/1406666/{a}/{doc}"
    ok=False
    for i in range(6):
        try:
            r=urllib.request.Request(u,headers=H)
            b=urllib.request.urlopen(r,timeout=90).read()
            open(out,"w",encoding="utf-8").write(strip(b.decode("utf-8","replace")))
            print("OK",name,len(b)); ok=True; break
        except Exception as e:
            print("  retry",i,name,e); time.sleep(4)
    if not ok: print("FAILED",name,u)
    time.sleep(1)
