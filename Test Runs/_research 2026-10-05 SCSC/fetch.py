import sys, json, urllib.request, gzip, os, time
H={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url, out):
    if os.path.exists(out) and os.path.getsize(out)>0: return out
    r=urllib.request.urlopen(urllib.request.Request(url,headers=H),timeout=60)
    d=r.read()
    if r.headers.get('Content-Encoding')=='gzip': d=gzip.decompress(d)
    open(out,'wb').write(d); time.sleep(0.2); return out
if __name__=='__main__':
    get(sys.argv[1], sys.argv[2]); print('ok', sys.argv[2])
