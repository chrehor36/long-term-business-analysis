import csv
rows = list(csv.DictReader(open('data_filed.csv')))
f = lambda r,k: float(r[k])
print("year  rev    OCasfiled  OC_taxcharge  acq  OC/sales%  leasecash  rentless_note")
oc = {}
for r in rows:
    y = int(r['year'])
    a = f(r,'cfo') - f(r,'capex') + f(r,'disposals') - f(r,'lease_principal') - f(r,'interest_paid') - f(r,'sbc')
    b = a + f(r,'tax_paid') - f(r,'tax_cy_basis')
    oc[y] = (a, b, f(r,'acq'), f(r,'revenue'))
    print(f"{y} {f(r,'revenue'):7.1f} {a:8.1f} {b:10.1f} {f(r,'acq'):6.1f} {100*b/f(r,'revenue'):6.1f} {f(r,'lease_principal')+f(r,'interest_paid'):7.1f}")
def avg(ys, i): return sum(oc[y][i] for y in ys)/len(ys)
W = range(2021, 2026)
for i,lab in [(0,'as filed'),(1,'tax-charge basis')]:
    print(lab, 'window 2021-25 avg', round(avg(W,i),1), 'less acq', round(avg(W,i)-sum(oc[y][2] for y in W)/5,1),
          '| 2016-20 avg', round(avg(range(2016,2021),i),1), '| 2020-24 avg', round(avg(range(2020,2025),i),1))
