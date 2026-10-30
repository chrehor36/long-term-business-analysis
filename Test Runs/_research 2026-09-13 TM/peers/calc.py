import sys
# (label, numerator, denominator) -> percent to 2dp. Arithmetic only.
rows = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip() and not l.startswith("#")]
for r in rows:
    lab, n, d = [x.strip() for x in r.split(";")]
    n = float(n.replace(",", "").replace("(", "-").replace(")", ""))
    d = float(d.replace(",", "").replace("(", "-").replace(")", ""))
    print("%-45s %10.2f%%" % (lab, 100.0 * n / d))
