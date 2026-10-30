import re, io, sys, html as H
def txt(path, lo=0, hi=None):
    s=io.open(path,encoding="utf-8",errors="replace").read()
    s=re.sub(r"(?is)<(script|style).*?</\1>"," ",s)
    s=re.sub(r"(?is)</t[dh]>"," | ",s)
    s=re.sub(r"(?is)</tr>","\n",s)
    s=re.sub(r"(?s)<[^>]+>"," ",s)
    s=H.unescape(s); s=re.sub(r"[ \t\xa0]+"," ",s)
    s=re.sub(r"\n *","\n",s); s=re.sub(r"\n{2,}","\n",s)
    return s
if __name__=="__main__":
    path=sys.argv[1]; pat=sys.argv[2]; ctx=int(sys.argv[3]) if len(sys.argv)>3 else 400
    t=txt(path)
    io.open(path.replace(".htm",".txt"),"w",encoding="utf-8").write(t)
    for m in list(re.finditer(pat,t,re.I))[:6]:
        a=max(0,m.start()-120); b=min(len(t),m.end()+ctx)
        print("-----", m.start()); print(t[a:b].replace("\n"," | "))
