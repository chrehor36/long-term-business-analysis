import urllib.request, json, re, html
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read().decode("utf-8","replace")
for acc in ["0001171843-26-002125","0001171843-26-002336","0001171843-26-001924"]:
    a=acc.replace("-","")
    j=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/1837429/{a}/index.json"))
    for it in j["directory"]["item"]:
        if it["name"].startswith("exh"):
            t=re.sub(r"<[^>]+>"," ",get(f"https://www.sec.gov/Archives/edgar/data/1837429/{a}/{it['name']}"))
            t=html.unescape(re.sub(r"\s+"," ",t))
            print(acc, t[:700]); print()
