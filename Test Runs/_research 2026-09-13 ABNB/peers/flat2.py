import re, glob
pat = re.compile(r'^[\s|()\-—–0-9,.%)]*$')
for f in glob.glob("20F_TCOM_*.txt"):
    out=[]
    for line in open(f,encoding='utf-8'):
        s=line.rstrip("\n")
        if out and (s.strip().startswith("|") or pat.match(s)):
            out[-1]+=" "+s.strip()
        else:
            out.append(s)
    res=[]
    for s in out:
        s=re.sub(r"\s*\|\s*"," | ",s)
        s=re.sub(r"\((\s*[0-9,.]+)\s*\|\s*\)",r"(\1)",s)
        s=re.sub(r"(\|\s*)+","| ",s)
        s=re.sub(r"\s+"," ",s)
        res.append(s)
    open("flat_"+f,"w",encoding='utf-8').write("\n".join(res))
