import sys,re
# print a region of a stripped filing with table cells joined per row
f, start_pat, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
occ = int(sys.argv[4]) if len(sys.argv)>4 else 1
lines = open(f, encoding="utf-8").read().split("\n")
idx = [i for i,l in enumerate(lines) if re.search(start_pat, l)]
i0 = idx[occ-1]
buf=[]; row=[]
for l in lines[i0:i0+n]:
    s=l.strip().strip("|").strip().replace("​","")
    if not s or s in ("$",): continue
    row.append(s)
    if not re.fullmatch(r"[\(\)\d,.\-—%$ ]+", s) and len(row)>1:
        # new label starts: flush previous
        buf.append(" ".join(row[:-1])); row=[row[-1]]
buf.append(" ".join(row))
print("\n".join(buf))
