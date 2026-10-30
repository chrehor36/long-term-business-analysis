import sys, json, statistics
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources, run as R

RES = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 SWK"
facts = sources.sec_facts("0000093556")


def A(tags, vintage="newest"):
    d, t, u = sources.annual(facts, tags, vintage=vintage)
    return d


ocf = A(R.OCF)
cap = A(R.CAP)
soft = A(R.SOFTWARE_CAP)
print("SOFTWARE_CAP resolves:", soft)
sbc = {}
for t in R.SBC:
    for e, v in A([t]).items():
        if e not in sbc or abs(v) > abs(sbc[e]):
            sbc[e] = v
da = {}
for t in R.DA_TOTAL:
    for e, v in A([t]).items():
        if e not in da or abs(v) > abs(da[e]):
            da[e] = v
parts = {}
for t in R.DA_COMPONENT:
    s = A([t])
    print(f"  DA_COMPONENT {t}: {len(s)} yrs")
    for e, v in s.items():
        parts[e] = parts.get(e, 0.0) + abs(v)
for e, v in parts.items():
    if e not in da or v > abs(da[e]):
        da[e] = v
dep_ppe = A(["DepreciationDepletionAndAmortization"])
amort_int = A(["AmortizationOfIntangibleAssets"])
ap = A(["IncreaseDecreaseInAccountsPayable"])

ys = sorted(set(ocf) & set(da) & set(cap))
print("\nyears:", len(ys), ys[0], "->", ys[-1])
print()
hdr = f"{'FY':>11} {'OCF':>9} {'SBC':>7} {'cash':>9} {'capex':>8} {'D&A used':>9} {'depPPE':>8} {'amortInt':>9} {'oe_lo':>9} {'oe_hi':>9} {'dAP':>9}"
print(hdr)
rows = {}
for y in ys:
    cash = ocf[y] - sbc.get(y, 0.0)
    lo = cash - max(da[y], cap[y])
    hi = cash - min(da[y], cap[y])
    rows[y] = dict(ocf=ocf[y], sbc=sbc.get(y), cash=cash, capex=cap[y], da=da[y], lo=lo, hi=hi)
    print(f"{y:>11} {ocf[y]:>9,.1f} {sbc.get(y,0):>7,.1f} {cash:>9,.1f} {cap[y]:>8,.1f} "
          f"{da[y]:>9,.1f} {dep_ppe.get(y,float('nan')):>8,.1f} {amort_int.get(y,float('nan')):>9,.1f} "
          f"{lo:>9,.1f} {hi:>9,.1f} {ap.get(y,float('nan')):>9,.1f}")

print("\n--- WINDOW MATRIX: mean(oe_lo) / mean(oe_hi), trailing N years ---")
print(f"{'N':>4} {'window':>25} {'mean_lo':>10} {'mean_hi':>10}")
for n in range(2, len(ys) + 1):
    sel = ys[-n:]
    ml = statistics.fmean(rows[y]["lo"] for y in sel)
    mh = statistics.fmean(rows[y]["hi"] for y in sel)
    print(f"{n:>4} {sel[0]+'..'+sel[-1]:>25} {ml:>10,.1f} {mh:>10,.1f}")

json.dump(rows, open(rf"{RES}\rows.json", "w"), indent=1)
