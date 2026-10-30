import re,sys
f=sys.argv[1]; pats=sys.argv[2:]
s=open(f,encoding="utf-8").read(); s=re.sub(r"[\s|]+"," ",s)
for p in pats:
    for m in re.finditer(p,s):
        print("~",f,":",s[m.start():m.start()+int(700)]); print()
