"""Owner-earnings arithmetic for the MBGL run. Arithmetic only; every judgment is named in the run file.
Inputs are hand-transcribed from the filed combined cash-flow statements (Form 10/A 0001104659-26-066592,
F-23) and the 10-Q (0002090312-26-000014)."""
import json

# $M, filed carve-out cash-flow statements
ocf   = {"2023": 393, "2024": 427, "2025": 485, "H1_25": 233, "H1_26": 189}
sbc   = {"2023": 20,  "2024": 28,  "2025": 22,  "H1_25": 9,   "H1_26": 9}
dep   = {"2023": 12,  "2024": 13,  "2025": 14,  "H1_25": 7,   "H1_26": 7}   # "Depreciation" line; acquired amortization excluded
capex = {"2023": 18,  "2024": 15,  "2025": 24,  "H1_25": 8,   "H1_26": 12}
# related-party working-capital lines (due from + due to), intercompany artefacts of the carve-out
rp    = {"2023": -7 + 24, "2024": 11 - 16, "2025": -5 + 19, "H1_25": 2 + 12, "H1_26": -8 - 19}
int_paid = {"2023": 18, "2024": 17, "2025": 14, "H1_25": 0, "H1_26": 0}  # H1 cash interest not filed; TTM set to FY2025 (14) -- approximation, stated

def ttm(d):
    return d["2025"] - d["H1_25"] + d["H1_26"]

for d in (ocf, sbc, dep, capex, rp, int_paid):
    d["TTM"] = ttm(d)

years = ["2023", "2024", "2025", "TTM"]
rows = {}
for y in years:
    rows[y] = {
        "OCF": ocf[y], "SBC": sbc[y], "dep": dep[y], "capex": capex[y], "rp_wc": rp[y],
        "OE_at_DA": ocf[y] - sbc[y] - dep[y],
        "OE_at_capex": ocf[y] - sbc[y] - capex[y],
        "OE_at_capex_ex_rp": ocf[y] - rp[y] - sbc[y] - capex[y],
    }

def mean(keys, field):
    return sum(rows[k][field] for k in keys) / len(keys)

windows = {
    "3yr 2023-25": ["2023", "2024", "2025"],
    "2yr 2024-25": ["2024", "2025"],
    "FY2025": ["2025"],
    "TTM Jun-26": ["TTM"],
}
win = {}
for w, ks in windows.items():
    win[w] = {f: round(mean(ks, f), 1) for f in ("OE_at_DA", "OE_at_capex", "OE_at_capex_ex_rp")}
    win[w]["carveout_interest_paid"] = round(sum(int_paid[k] for k in ks) / len(ks), 1)

# standalone bridge -- each input is a named judgment in the run file
TAX = 0.26                      # mid of the company's guided medium-term ETR 25-27% (Investor Day p.97, IR rung)
coupons = 650 * 0.0505 + 650 * 0.0545 + 700 * 0.0605   # $M a year, 10-Q Note 4
standalone_lo, standalone_hi = 20, 26                   # Investor Day p.96 "$20-25M"; Q2 deck "~150bps" of $1,750M = 26
standup_lo, standup_hi = 75, 100                        # Investor Day p.97 one-time "~$75-100M", ~50% capitalised (Q2 deck)

def standup_annual(total):
    expensed = total * 0.5 * (1 - TAX)
    capitalised = total * 0.5
    return (expensed + capitalised) / 5.0               # spread over the five-year default window [E2-42, E5-33]

bridge = {
    "coupons_pretax": round(coupons, 2),
    "coupons_after_tax": round(coupons * (1 - TAX), 1),
    "standalone_after_tax_lo": round(standalone_lo * (1 - TAX), 1),
    "standalone_after_tax_hi": round(standalone_hi * (1 - TAX), 1),
    "standup_annual_lo": round(standup_annual(standup_lo), 1),
    "standup_annual_hi": round(standup_annual(standup_hi), 1),
}

def standalone(oe, carve_int, optimistic):
    add_back = carve_int * (1 - TAX)
    s_cost = bridge["standalone_after_tax_lo"] if optimistic else bridge["standalone_after_tax_hi"]
    s_up = bridge["standup_annual_lo"] if optimistic else bridge["standup_annual_hi"]
    return round(oe + add_back - bridge["coupons_after_tax"] - s_cost - s_up, 1)

stand = {}
for w in windows:
    stand[w] = {
        "optimistic (D&A c, rp in, low costs)": standalone(win[w]["OE_at_DA"], win[w]["carveout_interest_paid"], True),
        "conservative (capex c, rp out, high costs)": standalone(win[w]["OE_at_capex_ex_rp"], win[w]["carveout_interest_paid"], False),
    }

allv = [v for w in stand.values() for v in w.values()]
lo, hi = min(allv), max(allv)

price, shares = 20.16, 294_821_320
cap = price * shares / 1e6
sov = 5.35
q5 = {
    "cap_$M": round(cap, 1),
    "yield_lo_%": round(lo / cap * 100, 2), "yield_hi_%": round(hi / cap * 100, 2),
    "growth_needed_for_10pct_floor_lo_%": round(10 - hi / cap * 100, 2),
    "growth_needed_for_10pct_floor_hi_%": round(10 - lo / cap * 100, 2),
}
vals = {}
for g in (0.0, 0.03, 0.05, 0.06):
    for r, name in ((0.10, "floor10"), (sov / 100, "sov")):
        if r - g <= 0:
            continue
        vals[f"{name}_g{int(g*100)}"] = (round(lo * (1 + g) / (r - g) / shares * 1e6, 2),
                                         round(hi * (1 + g) / (r - g) / shares * 1e6, 2))
q5["value_per_share_lo_hi"] = vals

# leverage and coverage
debt = 2000.0
cash_jun26 = 186.0
q4 = {
    "gross_debt_over_2025_OCF": round(debt / ocf["2025"], 2),
    "net_debt_$M": debt - cash_jun26,
    "interest_cover_on_OE_before_interest": None,
}
oe_pre_interest_cons = lo + bridge["coupons_after_tax"]
q4["interest_cover_on_OE_before_interest"] = round(oe_pre_interest_cons / bridge["coupons_after_tax"], 2)
dividend = 0.06 * 4 * shares / 1e6
q4["dividend_annual_$M"] = round(dividend, 1)

out = {"rows": rows, "windows": win, "bridge": bridge, "standalone": stand, "range": [lo, hi], "q5": q5, "q4": q4}
json.dump(out, open("oe_out.json", "w"), indent=1)
print(json.dumps(out, indent=1))
