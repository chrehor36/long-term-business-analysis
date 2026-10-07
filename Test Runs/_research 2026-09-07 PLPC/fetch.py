import json, urllib.request, re, sys, time, os
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(u):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
        except Exception as e:
            print('retry',e); time.sleep(3)
    raise SystemExit('fail '+u)
def strip(h):
    h=h.decode('utf-8','ignore')
    h=re.sub(r'(?is)<script.*?</script>',' ',h)
    h=re.sub(r'(?is)<style.*?</style>',' ',h)
    h=re.sub(r'(?is)<td[^>]*>','\t',h)
    h=re.sub(r'(?is)</tr>','\n',h)
    h=re.sub(r'(?is)<br[^>]*>','\n',h)
    h=re.sub(r'(?is)</p>','\n',h)
    h=re.sub(r'(?s)<[^>]+>',' ',h)
    import html as H; h=H.unescape(h)
    h=re.sub(r'[ \xa0]+',' ',h)
    h=re.sub(r'\n[ \t]+','\n',h)
    h=re.sub(r'\n{3,}','\n\n',h)
    return h
def pull(cik,acc,doc,out):
    a=acc.replace('-','')
    u=f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}'
    b=get(u); open(out+'.htm','wb').write(b)
    open(out+'.txt','w',encoding='utf-8').write(strip(b))
    print(out, len(b), '->', os.path.getsize(out+'.txt'))
    time.sleep(0.4)
if __name__=='__main__':
    pull(*sys.argv[1:5])
