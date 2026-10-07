import json, sys, time, urllib.request, gzip
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"gzip"}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    d=r.read()
    if r.headers.get("Content-Encoding")=="gzip": d=gzip.decompress(d)
    time.sleep(0.2); return d
if __name__=="__main__":
    url,out=sys.argv[1],sys.argv[2]
    open(out,"wb").write(get(url)); print("ok",out)
