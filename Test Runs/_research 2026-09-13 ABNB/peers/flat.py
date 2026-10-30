import sys, glob, re
for f in glob.glob("1*_*.txt")+glob.glob("20F_*.txt"):
    if f.startswith("flat_"): continue
    out=[]
    for line in open(f,encoding='utf-8'):
        s=line.rstrip("\n")
        if s.strip().startswith("|") and out:
            out[-1]+= " "+s.strip()
        else:
            out.append(s)
    res=[]
    for s in out:
        s=re.sub(r"(\s*\|\s*)+"," | ",s)
        s=re.sub(r"\$ \| ","$",s); s=re.sub(r"\( \| ","(",s); s=re.sub(r" \| \)",")",s); s=re.sub(r" \| %","%",s)
        res.append(s)
    open("flat_"+f,"w",encoding='utf-8').write("\n".join(res))
