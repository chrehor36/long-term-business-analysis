import sys, os, re, html
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fetch import get, D
def totext(raw):
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',raw)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|tr|h[1-6]|li)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=s.replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
if __name__=="__main__":
    url, name = sys.argv[1], sys.argv[2]
    raw=get(url, name+".htm")
    open(os.path.join(D,name+".txt"),"w",encoding="utf-8").write(totext(raw))
    print(name, "ok", len(raw))
