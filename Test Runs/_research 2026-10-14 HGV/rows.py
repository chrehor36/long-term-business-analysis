import re, html, sys
def rows(name):
    s=open("cache/"+name+".htm",encoding="utf-8",errors="replace").read()
    out=[]
    for tr in re.findall(r"(?is)<tr.*?</tr>", s):
        cells=[re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",c))).replace("\xa0"," ").strip() for c in re.findall(r"(?is)<t[dh].*?</t[dh]>", tr)]
        cells=[c for c in cells if c not in ("","$",")","%")]
        if cells: out.append(" | ".join(cells))
    return out
if __name__=="__main__":
    name=sys.argv[1]; open("cache/"+name+"_rows.txt","w",encoding="utf-8").write("\n".join(rows(name)))
