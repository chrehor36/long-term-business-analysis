import sys, os, urllib.request, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"}
for spec in sys.argv[2:]:
    name, cik, acc, doc = spec.split("|")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    p = os.path.join(sys.argv[1], name + ".htm")
    if not os.path.exists(p):
        open(p, "wb").write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()); time.sleep(0.3)
    print(name, os.path.getsize(p))
