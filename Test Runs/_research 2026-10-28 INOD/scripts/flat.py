import re,sys
def flat(path):
    s=open(path,encoding="utf-8").read()
    s=re.sub(r"[ \t]*\|[ \t]*"," | ",s)
    s=re.sub(r"\n\s*(\||​|\$)\s*"," ",s)
    s=re.sub(r"[ ​]+"," ",s)
    s=re.sub(r"(\| )+","| ",s)
    return s
if __name__=="__main__":
    s=flat(sys.argv[1]); key=sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 4000
    occ=int(sys.argv[4]) if len(sys.argv)>4 else 0
    idx=[m.start() for m in re.finditer(re.escape(key),s)]
    print(len(idx),"hits")
    if idx: i=idx[occ]; print(s[i:i+n])
