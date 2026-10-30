import sys, xlrd, collections
b = xlrd.open_workbook(sys.argv[1])
def annual(sheet, label):
    s = b.sheet_by_name(sheet)
    hdr = None
    for r in range(s.nrows):
        row = [c.value for c in s.row(r)]
        if str(row[1]).strip() in ("Quarter", "Year"): hdr = row[1:]
        if str(row[1]).strip() == label and hdr:
            row = row[1:]
            acc = collections.defaultdict(float); n = collections.Counter()
            for h, v in zip(hdr[2:], row[2:]):
                h = str(h)
                if v == "" or not h[:4].isdigit(): continue
                acc[h[:4]] += float(v); n[h[:4]] += 1
            return {y: acc[y] for y in acc if n[y] == 4}
    return {}
for sheet in ("Net_sales_and_income-Q", "Business_Area_NA-Q"):
    ns = annual(sheet, "Net sales")
    oi = annual(sheet, "Operating income")
    ox = annual(sheet, "Operating income excl. non-recurring items") or annual(sheet, "Operating income excl. non-recurring items 1)")
    print(sheet)
    for y in sorted(ns):
        print(f"  {y} sales {ns[y]:9.0f}  OI {oi.get(y,0):8.0f} ({100*oi.get(y,0)/ns[y]:5.1f}%)  OI exNRI {ox.get(y,0):8.0f} ({100*ox.get(y,0)/ns[y]:5.1f}%)")
