import sys, os, time, urllib.request
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
cik=sys.argv[1]
for arg in sys.argv[2:]:
    accn,doc,name=arg.split("|")
    p=f"cache/peers/{name}.htm"
    if not os.path.exists(p):
        u=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn.replace('-','')}/{doc}"
        open(p,"wb").write(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90).read()); time.sleep(0.3)
    print(name)
