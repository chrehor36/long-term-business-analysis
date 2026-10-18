import sys, os, json, urllib.request, time, gzip
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"gzip"}
def get(url, out):
    p=os.path.join(os.path.dirname(os.path.abspath(__file__)),"cache",out)
    if os.path.exists(p): return open(p,'rb').read()
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    b=r.read()
    if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
    open(p,'wb').write(b); time.sleep(0.3); return b
if __name__=="__main__":
    get(sys.argv[1], sys.argv[2]); print("ok", sys.argv[2])
