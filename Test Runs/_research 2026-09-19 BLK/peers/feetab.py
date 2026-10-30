import re,io,html as H,sys
def flat(path):
    src=io.open(path,encoding="utf-8",errors="replace").read()
    src=re.sub(r"(?is)<(script|style).*?</\1>"," ",src)
    t=re.sub(r"(?s)<[^>]+>"," ",src); t=H.unescape(t); t=re.sub(r"[\s\xa0]+"," ",t)
    return t
if __name__=="__main__":
    t=flat(sys.argv[1]); pat=sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 900
    for m in re.finditer(pat,t):
        print("@%d"%m.start(), t[m.start():m.start()+w]); print("  ~~~~")
