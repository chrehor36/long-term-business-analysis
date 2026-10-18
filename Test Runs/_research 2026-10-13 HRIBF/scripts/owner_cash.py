# Owner cash by hand from the filed consolidated cash-flow statements (yuho), JPY millions.
# OCF, PP&E purchases, intangible purchases, finance-lease principal, acquisitions (subsidiary shares / business transfer).
rows = {
 # year: (OCF, ppe, intang, lease, acq, D&A, goodwill_amort, sales, op_income, restricted_stock_pay)
 2016: (15871, 13001, 373, 195, 0, 6676, 139, 170093, 18499, 0),
 2017: (28287, 11664, 354, 163, 0, 7387, 146, 195399, 26834, 0),
 2018: (19536, 9667, 611, 181, 0, 7120, 120, 210570, 28838, 0),
 2019: (26638, 11762, 1172, 831, 0, 8485, 309, 200241, 20916, 0),
 2020: (32253, 14616, 429, 1254, 0, 9296, 322, 187080, 19694, 0),
 2021: (35268, 12195, 377, 1252, 0, 10063, 377, 224314, 32046, 0),
 2022: (33966, 11639, 444, 1482, 0, 10911, 437, 270133, 45843, 0),
 2023: (16652, 8849, 322, 1762, 2421, 12097, 505, 290558, 47296, 0),
 2024: (40335, 18152, 1295, 1875, 0, 12653, 406, 317369, 48340, 169),
 2025: (54383, 25275, 867, 1859, 2497, 13180, 625, 333081, 53040, 271),
}
print("year  OCF   capex  lease  owner_cash  acq  oc_after_acq  D&A  capex/D&A  oc/sales")
oc = {}
for y,(ocf,ppe,itg,ls,acq,da,gw,s,op,sp) in rows.items():
    c = ppe+itg
    o = ocf - c - ls - sp
    oc[y] = o
    print(f"{y} {ocf:6d} {c:6d} {ls:5d} {o:9d} {acq:5d} {o-acq:9d} {da:6d} {c/da:5.2f} {o/s:6.3f}")
for a,b in [(2016,2020),(2021,2025)]:
    v=[oc[y] for y in range(a,b+1)]; acq=[rows[y][4] for y in range(a,b+1)]
    print(a,b,"avg owner cash",sum(v)/5,"less acq",(sum(v)-sum(acq))/5)
