import sys,os,re,html,time,urllib.request
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
CIK='835011'
def url(acc,doc):
    return f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/{doc}"
def get(u,dst):
    d=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=120).read()
    open(dst,'wb').write(d); time.sleep(0.3)
def totext(src,dst):
    raw=open(src,'rb').read().decode('utf-8','ignore')
    raw=re.sub(r'(?is)<(script|style).*?</\1>',' ',raw)
    raw=re.sub(r'(?is)<br[^>]*>','\n',raw)
    raw=re.sub(r'(?is)</(p|div|tr|h[1-6]|li)>','\n',raw)
    raw=re.sub(r'(?is)</t[dh]>',' | ',raw)
    raw=re.sub(r'(?s)<[^>]+>',' ',raw)
    raw=html.unescape(raw)
    raw=re.sub(r'[ \t\xa0]+',' ',raw)
    raw=re.sub(r'\n\s*\n+','\n',raw)
    open(dst,'w',encoding='utf-8').write(raw)
jobs=[]
for a in sys.argv[1:]:
    acc,doc,name=a.split('::')
    jobs.append((acc,doc,name))
for acc,doc,name in jobs:
    u=url(acc,doc)
    try:
        get(u,name+'.htm'); totext(name+'.htm',name+'.txt')
        print('OK',name,os.path.getsize(name+'.txt'))
    except Exception as e:
        print('FAIL',name,u,e)
