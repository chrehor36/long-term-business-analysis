import json, sys, time, urllib.request, os, re
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
CIK="0000835011"
def get(url, binary=False):
    req=urllib.request.Request(url, headers=UA)
    d=urllib.request.urlopen(req, timeout=60).read()
    time.sleep(0.3)
    return d if binary else d.decode('utf-8','replace')
def idx(acc):
    a=acc.replace('-','')
    return json.loads(get(f"https://www.sec.gov/Archives/edgar/data/835011/{a}/index.json"))
def files(acc):
    j=idx(acc)
    return [(i['name'], i['size']) for i in j['directory']['item']]
if __name__=="__main__":
    for acc in sys.argv[1:]:
        print("==",acc)
        for n,s in files(acc): print("   ",n,s)
