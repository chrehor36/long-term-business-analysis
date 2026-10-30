import csv
rows={r[0]:r[1:] for r in csv.reader(l for l in open("figures.csv") if not l.startswith("#")) }
yrs=rows.pop("item")
f=lambda k,i: float(rows[k][i]) if rows[k][i] else 0.0
for i,y in enumerate(yrs):
    oc=f("cfo_after_tax_and_net_interest",i)-f("capex_ppe",i)-f("capex_intangibles",i)+f("proceeds_ppe_intang_rou",i)-f("lease_principal_paid",i)+f("jv_dividends",i)-f("share_based_pay_expense",i)
    print(y, round(oc,1), "share of sales %.2f%%"%(oc/f("revenue",i)*100), "pre-interest(after 25%% tax) %.1f"%(oc+0.75*f("net_interest_paid",i)))
