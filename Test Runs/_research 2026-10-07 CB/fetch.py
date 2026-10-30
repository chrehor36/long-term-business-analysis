import sys, json, time, urllib.request, os, re, gzip
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"gzip"}
def get(url, out=None):
    if out and os.path.exists(out):
        return open(out,'rb').read()
    req=urllib.request.Request(url,headers=UA)
    for i in range(4):
        try:
            r=urllib.request.urlopen(req,timeout=60); d=r.read()
            if r.headers.get('Content-Encoding')=='gzip': d=gzip.decompress(d)
            break
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(2)
    time.sleep(0.2)
    if out: open(out,'wb').write(d)
    return d
if __name__=='__main__':
    url=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else None
    d=get(url,out)
    if not out: sys.stdout.buffer.write(d)
