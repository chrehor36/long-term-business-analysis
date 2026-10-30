"""Q7 arithmetic for the NDSN run of 2026-10-10. Same number sooner; every input is a filed figure ($ millions).
Window FY2021-FY2025 (10-K FY2022 0000072331-22-000185 for FY2021-2022 lines via SEC companyfacts, cross-checked for
FY2023-2025 against the filed FY2025 cash-flow statement 0000072331-25-000144). Net debt at 2026-07-31 from the 10-Q
0000072331-26-000054. Sovereign 5.60% (US Treasury 30-year par, 2026-10-09). Floor about 10% (Q7 CONVENTION)."""
R, FLOOR = 0.056, 0.10
YRS = [2021, 2022, 2023, 2024, 2025]
OCF = [545.9, 513.1, 641.3, 556.2, 719.2]      # net cash from operating activities (after interest and tax paid)
SBC = [22.8, 30.7, 22.7, 19.0, 18.9]           # non-cash stock compensation (added back in OCF; a real cost)
CAPEX = [38.3, 51.4, 34.6, 64.4, 58.1]         # additions to property, plant and equipment
FINL = [6.6, 5.4, 6.8, 6.1, 5.9]               # finance-lease principal (a capital payment outside capex)
INTPD = [27.1, 23.0, 54.7, 86.0, 98.7]         # interest paid (cash-flow supplement)
TAX = [119.8, 136.2, 127.8, 118.2, 113.2]      # income tax expense
PRETAX = [574.2, 649.3, 615.3, 585.5, 597.6]   # income before income taxes
ACQ = [0.0, 171.6, 1422.8, 790.0, -28.1]       # cash paid for businesses net of cash acquired, net of businesses sold
ORGANIC = {2022: 0.108, 2023: -0.014, 2024: -0.025, 2025: -0.025}  # total-company organic sales growth, MD&A of each 10-K
NET_DEBT = 192.0 + 10.0 + 1529.005 + 9.920 + 8.758 - 113.431  # ST debt + current LTD + LTD + finance leases - cash, 2026-07-31
SHARES, PRICE = 55.699366, 328.17

def pv(cfs, terminal_cf, r):
    """cfs for years 1..10, then terminal_cf every year after at zero growth."""
    v = sum(c / (1 + r) ** t for t, c in enumerate(cfs, 1))
    return v + terminal_cf / r / (1 + r) ** len(cfs)

def stream(base, g, deduct_share=0.0):
    """ten years of owner cash at growth g, less acquisition spending at deduct_share of owner cash;
    after year ten no growth, so no growth spending: terminal cash is owner cash before acquisitions."""
    oc = [base * (1 + g) ** t for t in range(1, 11)]
    return [c * (1 - deduct_share) for c in oc], oc[-1]

def report(label, after_interest):
    rows = []
    for i, y in enumerate(YRS):
        t = TAX[i] / PRETAX[i]
        oc = OCF[i] - SBC[i] - CAPEX[i] - FINL[i] + (0 if after_interest else INTPD[i] * (1 - t))
        rows.append(oc)
    base = sum(rows) / 5
    g_total = (rows[-1] / rows[0]) ** (1 / 4) - 1
    f = 1.0
    for v in ORGANIC.values(): f *= 1 + v
    g_org = f ** (1 / 4) - 1
    acq_share = (sum(ACQ) / 5) / base
    sub = 0 if after_interest else NET_DEBT
    print(f"\n== {label}")
    for y, v in zip(YRS, rows): print(f"   FY{y} owner cash {v:8.1f}")
    print(f"   five-year mean {base:.1f}; total growth (FY2021->FY2025, aggregate) {g_total*100:.2f}%; organic {g_org*100:.2f}%;"
          f" acquisitions net {sum(ACQ):.1f} (mean {sum(ACQ)/5:.1f}, {acq_share*100:.1f}% of mean owner cash)")
    cases = {}
    cfs, term = stream(base, 0.0); cases["no growth, no acquisitions (maintenance-only top/bottom)"] = (cfs, term)
    cfs, term = stream(base, g_total, acq_share); cases["total growth credited, acquisitions deducted (default pair)"] = (cfs, term)
    cfs, term = stream(base, g_org); cases["organic growth only, acquisitions left out (pair beside)"] = (cfs, term)
    out = {}
    for k, (cfs, term) in cases.items():
        v = pv(cfs, term, R); v10 = pv(cfs, term, FLOOR)
        ps = (v - sub) / SHARES; ps10 = (v10 - sub) / SHARES
        out[k] = (v, v10, ps, ps10)
        print(f"   {k:62s} value {v:9.1f}  per share ${ps:8.2f} | at the floor {v10:8.1f}  per share ${ps10:8.2f}")
    return base, g_total, g_org, out

if __name__ == "__main__":
    print(f"net debt 2026-07-31 {NET_DEBT:.1f}; price ${PRICE}; market cap {PRICE*SHARES:.1f}; EV {PRICE*SHARES+NET_DEBT:.1f}")
    for label, ai in [("ALL-EQUITY basis (owner cash before interest, after the company's tax; less net debt)", False),
                      ("EQUITY-ONLY basis (owner cash after interest; against the market value)", True)]:
        base, gt, go, out = report(label, ai)
        ks = list(out)
        lo = min(out[ks[0]][2], out[ks[1]][2]); hi = max(out[ks[0]][2], out[ks[1]][2])
        mid_floor = (out[ks[0]][3] + out[ks[1]][3]) / 2
        print(f"   DEFAULT RANGE ${lo:.2f} to ${hi:.2f} a share (ends: no-growth and shown-growth); width {hi/lo:.2f} to 1")
        lo2 = min(out[ks[0]][2], out[ks[2]][2]); hi2 = max(out[ks[0]][2], out[ks[2]][2])
        print(f"   ORGANIC PAIR RANGE ${lo2:.2f} to ${hi2:.2f} a share")
        print(f"   FAIR PRICE (midpoint of the default range's two cash streams discounted at the floor): ${mid_floor:.2f}")
        # yield at the price
        ev = PRICE * SHARES + (0 if ai else NET_DEBT)
        print(f"   owner-cash yield at the price on the five-year mean: {base/ev*100:.2f}%")

# ---- variants shown beside (not chosen): depreciation in place of capital spending; growth between window halves
if __name__ == "__main__":
    DEP = [53.3, 49.1, 52.2, 59.2, 71.3]
    rows = []
    for i in range(5):
        t = TAX[i] / PRETAX[i]
        rows.append(OCF[i] - SBC[i] - DEP[i] - FINL[i] + INTPD[i] * (1 - t))
    base = sum(rows) / 5; g = (rows[-1] / rows[0]) ** 0.25 - 1; share = (sum(ACQ) / 5) / base
    lo = (pv(*stream(base, 0.0), R) - NET_DEBT) / SHARES
    hi = (pv(*stream(base, g, share), R) - NET_DEBT) / SHARES
    print(f"\n== VARIANT all-equity, depreciation in place of capital spending: mean {base:.1f}, growth {g*100:.2f}%:"
          f" ${min(lo,hi):.2f} to ${max(lo,hi):.2f}")
    allq = []
    for i in range(5):
        t = TAX[i] / PRETAX[i]
        allq.append(OCF[i] - SBC[i] - CAPEX[i] - FINL[i] + INTPD[i] * (1 - t))
    h1 = (allq[0] + allq[1]) / 2; h2 = (allq[3] + allq[4]) / 2; gh = (h2 / h1) ** (1 / 3) - 1
    base = sum(allq) / 5; share = (sum(ACQ) / 5) / base
    hi = (pv(*stream(base, gh, share), R) - NET_DEBT) / SHARES
    print(f"== VARIANT all-equity, growth between the halves (FY2021-22 mean {h1:.1f} to FY2024-25 mean {h2:.1f}, three years):"
          f" {gh*100:.2f}%; top ${hi:.2f}")
    # literal: total growth credited with NO acquisition deduction (the pairing the convention forbids), shown only to size the deduction
    hi_nodeduct = (pv(*stream(base, (allq[-1]/allq[0])**0.25-1, 0.0), R) - NET_DEBT) / SHARES
    print(f"== NOT A CASE (forbidden pairing, shown to size the acquisition deduction): total growth, nothing deducted: ${hi_nodeduct:.2f}")
