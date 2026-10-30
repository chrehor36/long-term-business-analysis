import urllib.request, json, sys
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read()
for acc in sys.argv[1:]:
    a=acc.replace("-","")
    u=f"https://www.sec.gov/Archives/edgar/data/1001085/{a}/index.json"
    try:
        j=json.loads(get(u))
        print("==",acc)
        for it in j["directory"]["item"]:
            print("  ",it["name"], it.get("size"))
    except Exception as e: print(acc,"ERR",e)
