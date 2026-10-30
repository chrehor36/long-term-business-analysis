import sys, re, html
raw=open(sys.argv[1],encoding="utf-8",errors="replace").read()
raw=re.sub(r"(?is)<(script|style).*?</\1>"," ",raw)
def row(m):
    cells=re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>",m.group(0))
    out=[]
    for c in cells:
        c=re.sub(r"<[^>]+>"," ",c); c=html.unescape(c).replace("\xa0"," "); c=re.sub(r"\s+"," ",c).strip()
        if c: out.append(c)
    return "\n@@ "+" | ".join(out)+"\n" if out else "\n"
raw=re.sub(r"(?is)<tr[^>]*>.*?</tr>",row,raw)
raw=re.sub(r"(?i)<br\s*/?>","\n",raw)
raw=re.sub(r"(?i)</(p|div|h\d|li|table)>","\n",raw)
raw=re.sub(r"<[^>]+>"," ",raw)
t=html.unescape(raw).replace("\xa0"," ")
t=re.sub(r"[ \t]+"," ",t)
t=re.sub(r"\n\s*\n+","\n",t)
open(sys.argv[2],"w",encoding="utf-8").write(t)
print(len(t))
