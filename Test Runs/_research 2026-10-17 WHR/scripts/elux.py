import sys, xlrd
b = xlrd.open_workbook(sys.argv[1])
pat = [p.lower() for p in sys.argv[2:]]
for s in b.sheets():
    for r in range(s.nrows):
        row = [str(c.value).strip() for c in s.row(r)]
        lab = " ".join(row[:2]).lower()
        if any(p in lab for p in pat) or (r < 8):
            print(s.name, r, " | ".join(x for x in row if x)[:400])
