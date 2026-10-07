import sys, json, urllib.request, os, time, gzip
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip'}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
    b=r.read()
    if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
    time.sleep(0.15)
    return b
if __name__=='__main__':
    url,out=sys.argv[1],sys.argv[2]
    open(out,'wb').write(get(url))
    print(out, os.path.getsize(out))
