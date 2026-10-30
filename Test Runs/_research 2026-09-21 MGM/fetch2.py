import urllib.request, io, sys, time
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
def get(u):
    for i in range(4):
        try:
            r=urllib.request.Request(u,headers=UA)
            with urllib.request.urlopen(r,timeout=60) as f: return f.read().decode('utf-8','replace')
        except Exception as e:
            print('retry',e); time.sleep(2+3*i)
    raise RuntimeError(u)
if __name__=='__main__':
    u=sys.argv[1]; out=sys.argv[2]
    io.open(out,'w',encoding='utf-8').write(get(u)); print('wrote',out)
