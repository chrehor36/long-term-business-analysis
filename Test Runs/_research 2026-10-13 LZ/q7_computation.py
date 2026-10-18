# LZ owner cash and Q7 COMPUTATION, NOT A CLEARANCE. All figures USD millions from the filed cash-flow statements.
# Sources: 10-K FY2021 (0001286139-22-000048), FY2022 (0001286139-23-000036), FY2025 (0001286139-26-000012),
# 10-Q Q2 2026 (0001286139-26-000031).
T = 0.21  # CONVENTION of this run: interest income on the cash is removed after tax at the 21% federal statutory rate
yrs = {
 # year: OCF, SBC expensed, SBC capitalized, capex, interest paid (cash), interest income (net if positive)
 2019: (52.695, 5.181, 0.0, 18.349, None, None),
 2020: (93.049, 12.894, 0.046, 10.587, 27.864, 0.0),
 2021: (54.152, 112.596, 0.674, 11.740, 12.284, 0.0),
 2022: (73.837, 80.469, 2.526, 22.098, 0.0, 1.543),
 2023: (124.308, 66.015, 4.056, 31.593, 0.0, 9.307),
 2024: (135.639, 71.510, 5.967, 35.696, 0.0, 7.850),
 2025: (178.197, 113.708, 5.264, 30.277, 0.0, 7.569),
}
acq = {2021: 61.523, 2022: 2.532 + 6.299 - 0.307, 2023: 0.0, 2024: 0.0, 2025: 48.468}
rev = {2019: 408.380, 2020: 470.636, 2021: 575.080, 2022: 619.979, 2023: 660.727, 2024: 681.881, 2025: 756.043}
# LTM to 2026-06-30 = FY2025 - H1 2025 + H1 2026
ltm = dict(ocf=178.197 - 89.842 + 86.829, sbc=113.708 - 60.394 + 44.910, csbc=5.264 - 2.920 + 2.570,
           capex=30.277 - 16.908 + 12.165, ii=7.569 - 3.552 + 3.275)
oc_eq, oc_ae = {}, {}
for y, (ocf, sbc, csbc, cx, ip, ii) in yrs.items():
    eq = ocf - sbc - csbc - cx                     # equity-only: after interest, interest income kept
    ae = eq + (ip or 0) - (ii or 0) * (1 - T)       # all-equity: before interest paid, interest income removed
    oc_eq[y], oc_ae[y] = eq, ae
    print(f"{y}: rev {rev[y]:7.1f}  owner cash equity-only {eq:7.1f}  all-equity {ae:7.1f}  share of sales {ae/rev[y]*100:5.1f}%  acquisitions {acq.get(y,0):5.1f}")
l_eq = ltm['ocf'] - ltm['sbc'] - ltm['csbc'] - ltm['capex']
l_ae = l_eq - ltm['ii'] * (1 - T)
print(f"LTM 2026-06: owner cash equity-only {l_eq:.1f} all-equity {l_ae:.1f}")

price, shares = 6.05, 171.264812
cash, debt = 167.227, 0.0
netcash = cash - debt
mcap = price * shares
print(f"market cap {mcap:.1f}  net cash {netcash:.1f}  EV {mcap-netcash:.1f}")

def pv(base, g, r, n=10):
    s = sum(base * (1 + g) ** t / (1 + r) ** t for t in range(1, n + 1))
    term = base * (1 + g) ** n / r / (1 + r) ** n
    return s + term

def show(label, base, g, basis='ae'):
    out = []
    for r in (0.056, 0.10):
        v = pv(base, g, r)
        ps = (v + netcash) / shares if basis == 'ae' else v / shares
        out.append(ps)
    print(f"  {label:58s} base {base:7.2f} g {g*100:5.2f}%  value@5.60% ${out[0]:6.2f}  @10% ${out[1]:6.2f}")
    return out

avg = lambda d, ys: sum(d[y] for y in ys) / len(ys)
W = [2021, 2022, 2023, 2024, 2025]
print("\nLiteral window 2021-2025")
b = avg(oc_ae, W); print(f"  avg all-equity {b:.2f}; avg after acquisitions {(sum(oc_ae[y]-acq.get(y,0) for y in W))/5:.2f}; net purchases {sum(acq.get(y,0) for y in W):.1f}; owner cash before purchases sum {sum(oc_ae[y] for y in W):.1f}")
lit = show("literal, organic pair, no-growth (sign change)", b, 0.0)
lit_eq = show("literal, equity-only, no-growth", avg(oc_eq, W), 0.0, basis='eq')
W2 = [2022, 2023, 2024, 2025]
print("\nWindow 2022-2025 (2021 aberrational, IPO year)")
b2 = avg(oc_ae, W2); print(f"  avg {b2:.2f}; net purchases {sum(acq.get(y,0) for y in W2):.1f}; owner cash before purchases sum {sum(oc_ae[y] for y in W2):.1f}; avg after acq {(sum(oc_ae[y]-acq.get(y,0) for y in W2))/4:.2f}")
c2 = show("2022-25, organic pair, no-growth (sign change)", b2, 0.0)
c2e = show("2022-25, equity-only, no-growth", avg(oc_eq, W2), 0.0, basis='eq')
W3 = [2023, 2024, 2025]
org = ((rev[2025] - 33.2 - 18.2) / rev[2023]) ** 0.5 - 1
gsh = (oc_ae[2025] / oc_ae[2023]) ** 0.5 - 1
b3 = avg(oc_ae, W3)
print(f"\nWindow 2023-2025 beside: avg {b3:.2f}; owner-cash growth shown {gsh*100:.1f}% (includes Formation Nation); organic revenue growth {org*100:.2f}%")
print(f"  net purchases {sum(acq.get(y,0) for y in W3):.1f} vs half owner cash before purchases {sum(oc_ae[y] for y in W3)/2:.1f}; avg after acq {(sum(oc_ae[y]-acq.get(y,0) for y in W3))/3:.2f}")
a = show("2023-25 organic pair, no-growth end", b3, 0.0)
c = show("2023-25 organic pair, organic-growth end", b3, org)
d1 = show("2023-25 default pair (acq deducted), total growth end", (sum(oc_ae[y]-acq.get(y,0) for y in W3))/3, gsh)
print("\nLTM beside")
e = show("LTM, no growth", l_ae, 0.0)
f = show("LTM, organic growth", l_ae, org)
g = show("LTM, 2026 guided revenue growth 6% (company outlook, flagged)", l_ae, 0.06)
# solve growth at which LTM case earns 10% at the price
lo, hi = 0.0, 0.5
for _ in range(60):
    mid = (lo + hi) / 2
    if pv(l_ae, mid, 0.10) + netcash < mcap: lo = mid
    else: hi = mid
print(f"  growth needed on the LTM base for 10% at ${price}: {lo*100:.1f}% a year for ten years")
print(f"  expected yield at price, LTM all-equity owner cash / EV: {l_ae/(mcap-netcash)*100:.2f}%")
print("\nFair price (Part VII: each end valued at 10%, averaged)")
print(f"  central (2022-25 window, no-growth alone): all-equity ${c2[1]:.2f}  equity-only ${c2e[1]:.2f}")
print(f"  literal window: all-equity ${lit[1]:.2f}  equity-only ${lit_eq[1]:.2f}")
print(f"  2023-25 organic pair beside: ${(a[1]+c[1])/2:.2f}")
