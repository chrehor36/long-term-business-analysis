# Owner cash for MPTI from the filed cash-flow statements (USD thousands).
# Sources: Form 10 info statement ex99.1 (0001564590-22-029832) for 2020-2021;
# 10-K FY2022 (0001564590-23-004848), FY2023 (0001437749-24-009243),
# FY2024 (0001437749-25-009645), FY2025 (0001437749-26-009844); 10-Q Q2 2026 (0001437749-26-027371).
rows = {
 # year: (OCF, SBC, capex, dep, amort, deferred_tax_in_OCF, interest_net_pretax, pretax, tax, revenue, op_income)
 2020: (3906, 145, 407, 435, 54, 491, -86, 2893, 583, 29984, 3030),
 2021: (2960, 292, 1099, 488, 54, 507, -12, 2113, 531, 26694, 2114),
 2022: (2042, 458, 936, 671, 54, 1136, -11, 2595, 797, 31845, 2875),
 2023: (4405, 2421, 1281, 797, 53, -784, 7, 4400, 911, 41168, 4299),
 2024: (7521, 636, 1898, 968, 5, 212, 243, 9775, 2139, 49012, 9394),
 2025: (10659, 1081, 2551, 1086, 0, 1480, 539, 10954, 2507, 54417, 10291),
}
print("year  rev    opinc  OCF   SBC   capex dep   defTx  OC_all  OC_maint  OC_all_taxN  OC_maint_taxN  int_at  OCall_eq  OCmaint_eq  OCall/rev")
out = {}
for y,(ocf,sbc,cap,dep,am,dt,intr,pt,tx,rev,oi) in rows.items():
    etr = tx/pt
    oc_all = ocf - sbc - cap
    oc_m = ocf - sbc - dep - am
    # tax-normalized: take out the deferred tax add-back so each year bears its own provision
    oc_all_t = oc_all - dt
    oc_m_t = oc_m - dt
    int_at = intr*(1-etr)
    # all-equity basis: owner cash before interest (remove after-tax interest income / add back after-tax interest expense)
    oc_all_eq = oc_all_t - int_at
    oc_m_eq = oc_m_t - int_at
    out[y] = dict(oc_all=oc_all, oc_m=oc_m, oc_all_t=oc_all_t, oc_m_t=oc_m_t, oc_all_eq=oc_all_eq, oc_m_eq=oc_m_eq, rev=rev, int_at=int_at)
    print(f"{y} {rev:6d} {oi:6d} {ocf:5d} {sbc:5d} {cap:5d} {dep+am:5d} {dt:6d} {oc_all:7d} {oc_m:8d} {oc_all_t:11d} {oc_m_t:13d} {int_at:7.0f} {oc_all_eq:8.0f} {oc_m_eq:10.0f}  {oc_all_eq/rev:6.1%}")
win = [2021,2022,2023,2024,2025]
for k in ("oc_all","oc_m","oc_all_t","oc_m_t","oc_all_eq","oc_m_eq"):
    avg = sum(out[y][k] for y in win)/5
    print(f"5-yr avg 2021-2025 {k}: {avg:,.0f}")
r0, r1 = rows[2021][9], rows[2025][9]
print("sales CAGR 2021-2025:", (r1/r0)**0.25-1)
for k in ("oc_all_eq","oc_m_eq"):
    a0,a1 = out[2021][k], out[2025][k]
    print(f"owner cash CAGR 2021-2025 {k}:", (a1/a0)**0.25-1 if a0>0 else None)
    h1 = (out[2021][k]+out[2022][k])/2; h2=(out[2024][k]+out[2025][k])/2
    print(f"  halves (21-22 vs 24-25) {k}: {h1:,.0f} -> {h2:,.0f}, rate over 3 yrs {(h2/h1)**(1/3)-1:.1%}")
print("max owner cash / sales in window (all-equity, maint):", max(out[y]['oc_m_eq']/out[y]['rev'] for y in rows))
print("max owner cash / sales in window (all-equity, all spend):", max(out[y]['oc_all_eq']/out[y]['rev'] for y in rows))
