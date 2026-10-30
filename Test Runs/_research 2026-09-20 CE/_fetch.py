import json,sys,os,time,urllib.request,gzip,io
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
def get(url,dest=None,binary=False):
    req=urllib.request.Request(url,headers=UA)
    for a in range(4):
        try:
            r=urllib.request.urlopen(req,timeout=60); data=r.read()
            if r.headers.get('Content-Encoding')=='gzip': data=gzip.decompress(data)
            if dest:
                open(dest,'wb').write(data)
            return data
        except Exception as e:
            print('retry',a,e); time.sleep(3)
    raise SystemExit('failed '+url)
if __name__=='__main__':
    get(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None)
    print('ok', sys.argv[1])
