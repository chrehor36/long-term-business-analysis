import urllib.request, os
H = {"User-Agent": "Mozilla/5.0"}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sov")
u = "https://www.tpex.org.tw/storage/bond_zone/tradeinfo/govbond/2026/202609/Curve.20260911-E.xls"
b = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60).read()
open(os.path.join(out, "Curve.20260911-E.xls"), "wb").write(b)
print(len(b), b[:8])
try:
    import xlrd
    wb = xlrd.open_workbook(file_contents=b)
    for sh in wb.sheets():
        print("== sheet", sh.name, sh.nrows, sh.ncols)
        for r in range(sh.nrows):
            row = [str(c.value) for c in sh.row(r)]
            if any(x.strip() for x in row):
                print(" | ".join(row))
except Exception as e:
    print("xlrd", e)
