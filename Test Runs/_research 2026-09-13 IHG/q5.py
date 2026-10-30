"""COMPUTATION - NOT A CLEARANCE. Arithmetic only: price implied by owner-earnings bases at the ~10% floor and at the sovereign."""
import json
SH = 146.997788; PX = 153.83; CAP = SH * PX
out = {"cap_$M": round(CAP, 1)}
def val(oe, g, r, yrs=10, g_term=0.0):
    v = 0.0; x = oe
    for t in range(1, yrs + 1):
        x *= (1 + g); v += x / (1 + r) ** t
    term = x * (1 + g_term) / (r - g_term) / (1 + r) ** yrs
    return v + term
bases = {"low 339 (2019-23 maint)": 339, "5y maint 468": 468, "5y central 555": 555, "5y growth 593": 593, "3y growth 673": 673}
for name, oe in bases.items():
    row = {"yield_%": round(100 * oe / CAP, 2)}
    for r in (0.10, 0.0535):
        for g in (0.0, 0.05, 0.08, 0.10):
            row[f"r{r}_g{g}_per_share"] = round(val(oe, g, r) / SH, 0)
        # perpetual growth needed at the quote (Gordon, next-year OE)
        lo, hi = -0.05, r - 1e-6
        for _ in range(200):
            m = (lo + hi) / 2
            if oe * (1 + m) / (r - m) > CAP: hi = m
            else: lo = m
        row[f"perp_g_needed_r{r}_%"] = round(100 * m, 2)
    out[name] = row
# what the business has done
out["fee_business_op_profit_cagr_2019_25_%"] = round(100 * ((1231 / 813) ** (1 / 6) - 1), 2)
out["sep_growth_end_cagr_2019_25_%"] = round(100 * ((783 / 425) ** (1 / 6) - 1), 2)
out["sep_growth_end_5y_mean_2017_21_vs_2021_25"] = None
json.dump(out, open("q5_out.json", "w"), indent=1)
print(json.dumps(out, indent=1))
