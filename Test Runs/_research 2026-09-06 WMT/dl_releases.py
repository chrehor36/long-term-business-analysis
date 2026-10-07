import json, os, re, time, urllib.request, html as ht

UA="BRK-research chrehor36@gmail.com"
D=os.path.dirname(os.path.abspath(__file__))
man=json.load(open(os.path.join(D,'manifest.json')))

def qname(date):
    y,m,_=date.split('-'); y=int(y); m=int(m)
    # WMT FY ends Jan 31. Feb release = Q4 of FY(y); May = Q1 FY(y+1); Aug = Q2 FY(y+1); Nov = Q3 FY(y+1)
    if m<=3:  return f"q4fy{str(y)[2:]}"
    if m<=6:  return f"q1fy{str(y+1)[2:]}"
    if m<=9:  return f"q2fy{str(y+1)[2:]}"
    return f"q3fy{str(y+1)[2:]}"

def totext(h):
    h=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'(?i)</tr>','\n',h)
    h=re.sub(r'(?i)<br[^>]*>','\n',h)
    h=re.sub(r'(?i)</(p|div|table|h[1-6]|li)>','\n',h)
    h=re.sub(r'<[^>]+>',' ',h)
    h=ht.unescape(h)
    h=h.replace('\u00a0',' ').replace('\u200b','')
    lines=[re.sub(r'[ \t]+',' ',l).strip() for l in h.split('\n')]
    return '\n'.join(l for l in lines if l and l!='|')

for date,info in sorted(man.items(), reverse=True):
    if not info.get('pick'): print("NOPICK",date); continue
    q=qname(date)
    href=info['pick'][2]
    url = href if href.startswith('http') else "https://www.sec.gov"+href
    hp=os.path.join(D,f"8k-{q}-ex991.htm"); tp=os.path.join(D,f"8k-{q}-ex991.txt")
    if not os.path.exists(hp):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept-Encoding":"identity"})
            data=urllib.request.urlopen(req,timeout=90).read()
            open(hp,'wb').write(data); time.sleep(0.3)
        except Exception as e:
            print("DLFAIL",date,q,e); continue
    raw=open(hp,encoding='utf-8',errors='replace').read()
    open(tp,'w',encoding='utf-8').write(totext(raw))
    print("ok",date,q,os.path.getsize(hp),os.path.getsize(tp))
