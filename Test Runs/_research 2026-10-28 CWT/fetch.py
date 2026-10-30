import sys, json, urllib.request, os, time
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
def get(url, path):
    if os.path.exists(path): return open(path,'rb').read()
    r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
    open(path,'wb').write(r); time.sleep(0.3); return r
if __name__=='__main__':
    get(sys.argv[1], sys.argv[2]); print('ok', sys.argv[2], os.path.getsize(sys.argv[2]))
