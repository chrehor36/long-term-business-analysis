import sys, json, urllib.request, os, time, gzip
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=60) as r:
        d=r.read()
        if r.headers.get('Content-Encoding')=='gzip': d=gzip.decompress(d)
    time.sleep(0.2)
    return d
if __name__=='__main__':
    url,out=sys.argv[1],sys.argv[2]
    d=get(url); open(out,'wb').write(d); print(out,len(d))
