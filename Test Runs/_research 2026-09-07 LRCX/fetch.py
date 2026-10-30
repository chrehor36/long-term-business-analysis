import json,urllib.request,sys,os,io
H={'User-Agent':'BRK Research chrehor36@gmail.com'}
def get(u):
    r=urllib.request.Request(u,headers=H)
    return urllib.request.urlopen(r,timeout=60).read()
if __name__=='__main__':
    u=sys.argv[1]; out=sys.argv[2]
    d=get(u); open(out,'wb').write(d); print(out, len(d))
