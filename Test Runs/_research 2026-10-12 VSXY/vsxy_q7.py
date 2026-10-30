"""VSXY run 2026-10-12: owner cash and the Q7 COMPUTATION (arithmetic only, no verdict).
Every input is a filed figure (USD millions); sources in the comments. Prints the series, the range and the fair price."""

# fiscal year: (OCF, SBC, capex, D&A, interest paid (cash), NCI net income, purchases of businesses)
# FY2019, FY2020: carve-out (combined) figures from VS&Co's own FY2021 10-K (0001856437-22-000007), cash-flow statement;
#   FY2019 interest: no cash figure stated, the expense (8) used; FY2020: "no cash paid for interest in 2020" (FY2022 10-K).
# FY2021: FY2021 10-K (0001856437-22-000007) and FY2022 10-K (0001856437-23-000013); the first seven months are carve-out.
# FY2022: FY2022 10-K; purchases = Adore Me 369 (net of cash acquired) + Frankies Bikinis investment 18.
# FY2023-FY2025: FY2025 10-K (0001856437-26-000004) and FY2024 10-K (0001856437-25-000006);
#   FY2024 purchases = 161 deferred and contingent consideration for Adore Me (financing line); FY2025 = 4.
S = {
    2019: dict(ocf=315, sbc=38, capex=225, da=411, intr=8,  nci=0,   acq=0),
    2020: dict(ocf=674, sbc=25, capex=127, da=326, intr=0,  nci=0,   acq=0),
    2021: dict(ocf=851, sbc=33, capex=169, da=303, intr=18, nci=0,   acq=0),
    2022: dict(ocf=437, sbc=48, capex=164, da=274, intr=52, nci=-10, acq=387),
    2023: dict(ocf=389, sbc=56, capex=256, da=284, intr=87, nci=7,   acq=0),
    2024: dict(ocf=425, sbc=60, capex=178, da=258, intr=77, nci=4,   acq=161),
    2025: dict(ocf=499, sbc=55, capex=187, da=238, intr=66, nci=28,  acq=4),
}
TAX = 0.247          # 21.0% federal + 3.7% state, the FY2025 10-K rate reconciliation (statutory, combined)
R = 0.056            # US Treasury 30-year par yield, 2026-10-09 (tools/sources.py)
FLOOR = 0.10         # Q7 CONVENTION, the floor
NET_DEBT = 975 - 522 # debt 4 current + 971 long-term, less cash 522, at 2026-08-01 (10-Q 0001856437-26-000021); leases left out
SHARES = 79.764      # cover, 10-Q filed 2026-09-04
PRICE = 88.59        # 2026-10-12 close, aggregator (tools/run.py), flagged

def oc(y, basis="allequity", dep=False):
    d = S[y]
    spend = d["da"] if dep else d["capex"]
    x = d["ocf"] - d["sbc"] - spend - d["nci"]
    if basis == "allequity":
        x += d["intr"] * (1 - TAX)
    return x

def value(c0, g, r, purchases=0.0, before=None):
    """ten years at g, then zero nominal growth for ever, discounted at r.
    purchases: average purchase spending deducted in years 1-10 only (stops with growth after year ten)."""
    before = c0 if before is None else before
    v = 0.0
    for t in range(1, 11):
        v += (before * (1 + g) ** t - purchases) / (1 + r) ** t
    v += before * (1 + g) ** 10 / r / (1 + r) ** 10
    return v

def show():
    print("Owner cash (all-equity: OCF - SBC - capex - NCI share + interest paid after tax), before purchases")
    for y in S:
        print(y, round(oc(y), 1), " equity-only", round(oc(y, "equity"), 1), " D&A variant", round(oc(y, dep=True), 1), " purchases", S[y]["acq"])
    lit = [2021, 2022, 2023, 2024, 2025]
    cyc = [2019, 2020, 2021, 2022, 2023]
    for name, yrs in (("literal window FY2021-25", lit), ("cycle trough-to-trough FY2019-23", cyc)):
        base = sum(oc(y) for y in yrs) / 5
        base_eq = sum(oc(y, "equity") for y in yrs) / 5
        base_da = sum(oc(y, dep=True) for y in yrs) / 5
        acq = sum(S[y]["acq"] for y in yrs) / 5
        print(f"\n{name}: base {base:.1f}  equity-only {base_eq:.1f}  D&A variant {base_da:.1f}  avg purchases {acq:.1f}")
    # growth: halves of the literal window (FY2021-22 against FY2024-25, mid-points three years apart)
    h1 = (oc(2021) + oc(2022)) / 2; h2 = (oc(2024) + oc(2025)) / 2
    g_half = (h2 / h1) ** (1 / 3) - 1
    g_end = (oc(2025) / oc(2021)) ** (1 / 4) - 1
    print(f"\ngrowth, end years FY2021->FY2025: {g_end:.1%};  halves: {h1:.1f} -> {h2:.1f} = {g_half:.1%} a year")
    for name, yrs in (("CENTRAL: cycle base FY2019-23, halves growth", [2019, 2020, 2021, 2022, 2023]),
                      ("BESIDE: literal window FY2021-25, end-year growth", [2021, 2022, 2023, 2024, 2025])):
        g = g_half if name.startswith("CENTRAL") else g_end
        base = sum(oc(y) for y in yrs) / 5
        base_eq = sum(oc(y, "equity") for y in yrs) / 5
        acq = sum(S[y]["acq"] for y in yrs) / 5
        top = value(base, 0.0, R)                     # no growth, buys nothing
        bot = value(base, g, R, purchases=acq)        # negative growth, purchases deducted years 1-10
        print(f"\n{name}\n  EV range at {R:.2%}: bottom {bot:,.0f}  top {top:,.0f}  (ratio {top/bot:.2f})")
        print(f"  per share less net debt {NET_DEBT}: bottom ${(bot-NET_DEBT)/SHARES:.2f}  top ${(top-NET_DEBT)/SHARES:.2f}  vs price ${PRICE}")
        f_top = value(base, 0.0, FLOOR); f_bot = value(base, g, FLOOR, purchases=acq)
        fair = ((f_top + f_bot) / 2 - NET_DEBT) / SHARES
        e_top = value(base_eq, 0.0, FLOOR); e_bot = value(base_eq, g, FLOOR, purchases=acq)
        fair_eq = ((e_top + e_bot) / 2) / SHARES
        print(f"  each end at 10%: bottom {f_bot:,.0f}  top {f_top:,.0f}  -> FAIR PRICE (all-equity, less net debt) ${fair:.2f};  equity-only ${fair_eq:.2f}")
        ev_price = PRICE * SHARES + NET_DEBT
        print(f"  EV at price {ev_price:,.0f}; yield of base on EV {base/ev_price:.2%}; top case at 10% clears the price? {f_top >= ev_price}")
    # sensitivity: FY2025 with the IEEPA refund (148 received in FY2026, >95% of IEEPA tariffs paid) added back
    b2 = (sum(oc(y) for y in [2021, 2022, 2023, 2024]) + oc(2025) + 148) / 5
    print(f"\nSensitivity, literal window with the refund credited to FY2025: base {b2:.1f}; top at 10% {b2/FLOOR:,.0f} vs EV at price {PRICE*SHARES+NET_DEBT:,.0f}")

if __name__ == "__main__":
    show()
