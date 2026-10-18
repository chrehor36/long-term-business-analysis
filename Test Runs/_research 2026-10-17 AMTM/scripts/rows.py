import sys, re, html
src=sys.argv[1]; out=sys.argv[2]
t=open(src,"rb").read().decode("utf-8","replace")
t=re.sub(r"(?is)<(script|style).*?</\1>"," ",t)
out_lines=[]
# split into tables and non-table text
parts=re.split(r"(?is)(<table.*?</table>)",t)
def clean(x):
    x=re.sub(r"(?i)<br\s*/?>"," ",x)
    x=re.sub(r"<[^>]+>"," ",x); x=html.unescape(x)
    return re.sub(r"[\s\xa0]+"," ",x).strip()
for p in parts:
    if p.lower().startswith("<table"):
        for tr in re.findall(r"(?is)<tr.*?</tr>",p):
            cells=[clean(c) for c in re.findall(r"(?is)<t[dh].*?</t[dh]>",tr)]
            cells=[c for c in cells if c not in ("","$",")","%",")%")]
            if cells: out_lines.append(" | ".join(cells))
        out_lines.append("")
    else:
        p=re.sub(r"(?i)</(p|div|li|h\d)>","\n",p)
        for l in clean_lines if False else p.split("\n"):
            c=clean(l)
            if c: out_lines.append(c)
open(out,"w",encoding="utf-8").write("\n".join(out_lines))
print(out,len(out_lines))
