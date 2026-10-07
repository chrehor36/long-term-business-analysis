import urllib.request, json, os, sys, time, re
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
D=os.path.dirname(os.path.abspath(__file__))
def get(url, fn=None, binary=False):
    p=os.path.join(D,fn) if fn else None
    if p and os.path.exists(p) and os.path.getsize(p)>0:
        return open(p,'rb').read() if binary else open(p,encoding='utf-8',errors='replace').read()
    for a in range(4):
        try:
            b=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120).read()
            break
        except Exception as e:
            print("retry",a,e); time.sleep(3)
    else:
        raise SystemExit("FAIL "+url)
    if p:
        open(p,'wb').write(b)
    time.sleep(0.3)
    return b if binary else b.decode('utf-8',errors='replace')

def idx(acc):
    a=acc.replace('-','')
    j=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/832988/{a}/index.json", f"idx_{acc}.json"))
    return [(i['name'], f"https://www.sec.gov/Archives/edgar/data/832988/{a}/{i['name']}") for i in j['directory']['item']]

if __name__=="__main__":
    for acc in sys.argv[1:]:
        for n,u in idx(acc):
            print(acc, n)
