import json
inp = json.load(open("value_inputs.json"))
r_gov = 0.056; SH = 913.248; P = 283.74
DEBT = 14052; CASH = 3660 + 3341; RECV = 2163
ND = DEBT - CASH; ND_r = ND - RECV
def pv(oc0, g, r, n=10):
    v = 0; oc = oc0
    for t in range(1, n+1):
        oc *= (1+g); v += oc/(1+r)**t
    return v + (oc/r)/(1+r)**n          # zero nominal growth after year ten
def irr(oc0, g, target):
    lo, hi = 0.001, 1.0
    for _ in range(200):
        m = (lo+hi)/2
        if pv(oc0, g, m) > target: lo = m
        else: hi = m
    return m
mc = SH*P; EV = mc + ND; EV_r = mc + ND_r
print(f"market cap {mc:,.0f}; net debt {ND:,.0f} (less CHIPS receivables {ND_r:,.0f}); EV {EV:,.0f} / {EV_r:,.0f}")
def show(label, oc0, g, eq_only=False):
    v = pv(oc0, g, r_gov); v10 = pv(oc0, g, 0.10)
    if eq_only:
        ps, ps10 = v/SH, v10/SH; tgt = mc
    else:
        ps, ps10 = (v-ND_r)/SH, (v10-ND_r)/SH; tgt = EV_r
    i = irr(oc0, g, tgt)
    print(f"{label:58s} OC0 {oc0:7.0f} g {g:6.2%}: value {v:9,.0f} -> ${ps:7.2f}/sh at 5.6%; ${ps10:7.2f}/sh at 10%; IRR at price {i:6.2%}")
    return ps, ps10, i
c = inp["maint_alleq"]; g_cap = 0.0388
print("CENTRAL: maintenance-only, all-equity, cycle base 2019-2023, growth capped to sales growth between cycles")
b = show("bottom: no growth", c["cyc"], 0.0)
t = show("top: sales growth between cycles (cap applied; shown OC 7.18%)", c["cyc"], g_cap)
t_uncap = show("beside: shown OC growth 7.18% uncapped", c["cyc"], c["g_cyc"])
print(f"  range ${b[0]:.2f} - ${t[0]:.2f}; width {t[0]/b[0]:.2f}x; FAIR (avg of ends at 10%) ${(b[1]+t[1])/2:.2f}")
ce = inp["maint_eq"]
print("EQUITY-ONLY (owner cash after interest, against market value)")
be = show("bottom", ce["cyc"], 0.0, True); te = show("top (3.88%)", ce["cyc"], g_cap, True)
print(f"  range ${be[0]:.2f} - ${te[0]:.2f}; FAIR ${(be[1]+te[1])/2:.2f}")
a = inp["allcapex_alleq"]
print("ALL-SPENDING case beside (cycle base)")
ba = show("bottom", a["cyc"], 0.0); ta = show("top growth between cycles", a["cyc"], a["g_cyc"])
print("LITERAL WINDOW 2021-2025 beside (all-equity, maintenance-only)")
lw = show("no growth on window avg (top under rule b)", c["win"], 0.0)
lb = show("literal CAGR -13.7% (bottom under rule b)", c["win"], c["g_lit"])
print("GENEROUS SENSITIVITY: TTM to 2026-06-30 maintenance OC as base")
# TTM: OCF 8667, SBC 2H25+1H26 = (419-245)+236=410, dep gross ~ 2*1088 + chips dep ~ 2*? use 2025 gross 2271*1.13, swam 82, ITC 433, net int (542-? )
ttm = 8667 - 410 - 82 - (2271*1.13) - 433 + (556-232)*0.79
show("TTM base no growth", ttm, 0.0); show("TTM base 3.88%", ttm, g_cap); show("TTM base 7.18%", ttm, 0.0718)
