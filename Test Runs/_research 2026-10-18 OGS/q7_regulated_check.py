# A coherent regulated case, as a check on the floor test (not the convention's range): ten years in which pre-capex
# all-equity cash and all spending each grow at their own shown rates (2021-2025 window, WC at its average), then a
# terminal on the depreciation variant at year-ten levels (rate base flat, spending equal to depreciation). $ millions.
pre0, pre_g = 568.1, (683.9 + 37.4 - (-22.9)) / (477.3 + 37.4 - (-33.6))   # smoothed end years, see q7_out.txt
pre_g = pre_g ** 0.25 - 1
sp0, sp_g = 690.2, (759.5 / 544.3) ** 0.25 - 1
da0, da_g = 247.0, (285.1 / 207.2) ** 0.25 - 1
EV = 7898.5; ND = 3146.5; SH = 62.856270
def val(r):
    pv = 0
    for t in range(1, 11):
        pv += (pre0 * (1 + pre_g) ** t - sp0 * (1 + sp_g) ** t) / (1 + r) ** t
    term = pre0 * (1 + pre_g) ** 10 - da0 * (1 + da_g) ** 10
    return pv + term / r / (1 + r) ** 10, term
for r in (0.0543, 0.08, 0.10):
    v, term = val(r); print(f"r {r:.4f}: EV value {v:,.0f}  per share {(v-ND)/SH:7.2f}  terminal cash {term:,.0f}")
lo, hi = 0.01, 0.5
for _ in range(100):
    m = (lo + hi) / 2
    if val(m)[0] > EV: lo = m
    else: hi = m
print(f"growth rates: pre {pre_g*100:.2f}%  spending {sp_g*100:.2f}%  D&A {da_g*100:.2f}%   IRR at price {m*100:.2f}%")
