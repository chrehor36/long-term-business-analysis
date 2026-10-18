import sys, urllib.request, gzip, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
def get(url, out):
    if os.path.exists(out) and os.path.getsize(out)>0: return
    req=urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        d=r.read()
        if r.headers.get('Content-Encoding')=='gzip': d=gzip.decompress(d)
    open(out,'wb').write(d); time.sleep(0.3)
if __name__=='__main__':
    get(sys.argv[1], sys.argv[2]); print('ok', sys.argv[2], os.path.getsize(sys.argv[2]))
