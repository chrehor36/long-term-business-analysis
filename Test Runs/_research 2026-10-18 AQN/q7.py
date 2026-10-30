# Q7 arithmetic for AQN, run 2026-10-18. All inputs typed from the filed statements (sources in comments).
# US$ millions. Continuing business (Regulated Services + Hydro + Corporate), 2021-2025.
# Run: python -I q7.py

R = 0.0543          # USD 30y par yield, US Treasury, 2026-10-16 (tools/sources.py)
FLOOR = 0.10        # framework CONVENTION, Q7 floor
TAX = 96.2 / 370.8  # company's own tax: Regulated Services Group FY2025 provision / pre-tax (note 19, FY2025 40-F)
SH = 769.747684     # common shares, 2026-06-30 (Q2 2026 6-K note 9(a))
PRICE = 5.25

yrs = [2021, 2022, 2023, 2024, 2025]
# EBIT_adj = segment EBT + segment interest, corporate investment income (Atlantica) removed, FX loss added back.
# RSG EBT + interest (segment notes FY2021 40-F, FY2023 40-F for 2022, FY2024 40-F for 2023, FY2025 40-F for 2024-25)
rsg = {2021: 300.247 + 93.411, 2022: 352.936 + 113.482, 2023: 229.146 + 160.999, 2024: 249.1 + 191.8, 2025: 370.8 + 141.4}
# Hydro EBT + interest, reported apart from FY2023; 2021-2022 inside the sold Renewable Energy Group:
hyd_rep = {2023: 13.419 + 1.177, 2024: 19.3 + 0.9, 2025: 19.1 + 0.9}
hyd_avg = sum(hyd_rep.values()) / 3
hyd = {2021: hyd_avg, 2022: hyd_avg, **hyd_rep}          # CONVENTION of this run, said in the file
# Corporate: EBT + interest - income from long-term investments + FX loss
corp = {2021: -186.255 + 44.545 - (-128.809) + 4.371,
        2022: -636.933 + 100.807 - (-502.344) + 13.833,
        2023: -304.680 + 146.264 - (-128.891) + 13.659,
        2024: -91.2 + 170.9 - 101.6 + 3.5,
        2025: -178.9 + 140.2 - 14.7 + 18.4}
da = {2021: 280.452 + 1.097 + 6.659, 2022: 317.300 + 1.017 + 6.659, 2023: 346.188 + 6.659 + 1.232,
      2024: 386.8 + 6.8 + 2.1, 2025: 392.1 + 7.3 + 0.9}
# all capital spending (segment notes) + acquisitions (2022 PP&E acquired, MD&A FY2023: 609.3)
capex_all = {2021: 998.855 + 7.553 + 6.659, 2022: 908.676 + 6.659 + 609.3, 2023: 740.768 + 6.659 + 1.232,
             2024: 763.8, 2025: 608.8}
# sustaining (MD&A FY2025: RSG sustaining 610.5 (2024), 499.7 (2025); hydro 6.6, 5.3)
ratio = (610.5 / 386.8 + 499.7 / 392.1) / 2           # sustaining / RSG depreciation, 2024-2025
sust = {2021: 280.452 * ratio + 6.659, 2022: 317.300 * ratio + 6.659, 2023: 346.188 * ratio + 6.659,
        2024: 610.5 + 6.6, 2025: 499.7 + 5.3}
# increase in working capital (XBRL IncreaseDecreaseInOperatingCapital, consolidated; 2021 = Storm Uri year)
dwc_lit = {2021: 522.0, 2022: 221.6, 2023: -86.3, 2024: 139.5, 2025: 45.7}
other4 = [dwc_lit[y] for y in yrs if y != 2021]
dwc_c = dict(dwc_lit); dwc_c[2021] = sum(other4) / 4                 # (d): event year at the other years' intensity
interest = {2021: 209.6, 2022: 278.6, 2023: 308.4, 2024: 363.6, 2025: 282.5}  # interest expense (XBRL/statements)

def oc(case, dwc):
    out = {}
    for y in yrs:
        ebit = rsg[y] + hyd[y] + corp[y]
        nopat = ebit * (1 - TAX)
        spend = {'maint': sust[y], 'all': capex_all[y], 'dep': da[y]}[case]
        out[y] = nopat + da[y] - spend - dwc[y]
    return out

def pv(base, g, r, years=10):
    v, c = 0.0, base
    for t in range(1, years + 1):
        c = c * (1 + g); v += c / (1 + r) ** t
    return v + c / r / (1 + r) ** years       # no growth after year ten (zero nominal)

# claims ahead of the common at 2026-06-30 (Q2 2026 balance sheet)
net_debt = 520.6 + 6115.1 - 55.0
pref = 184.3
nci = 356.3
claims = net_debt + pref + nci
ev = PRICE * SH + claims

print(f"tax {TAX:.4f}  sust/dep ratio {ratio:.3f}  hydro avg {hyd_avg:.1f}")
print(f"market cap {PRICE*SH:.1f}  net debt {net_debt:.1f}  pref {pref}  NCI {nci}  claims {claims:.1f}  EV {ev:.1f}")
for y in yrs:
    e = rsg[y] + hyd[y] + corp[y]
    print(y, f"EBIT_adj {e:7.1f} NOPAT {e*(1-TAX):7.1f} D&A {da[y]:6.1f} sust {sust[y]:6.1f} capex_all {capex_all[y]:7.1f} dWC {dwc_lit[y]:6.1f}")

# sales growth cap (f): RSG revenue + other revenue, 2021 -> 2025 (segment notes)
s21 = 1944.171 + 53.441; s25 = 2333.7 + 60.7
g_sales = (s25 / s21) ** (1 / 4) - 1
print(f"sales growth 2021-2025 {g_sales*100:.2f}%/yr")

res = {}
for case in ['maint', 'all', 'dep']:
    for wc_name, dwc in [('central-wc', dwc_c), ('literal-wc', dwc_lit)]:
        o = oc(case, dwc)
        avg = sum(o.values()) / 5
        first = (o[2021] + o[2022]) / 2; second = (o[2024] + o[2025]) / 2
        if first > 0 and second > 0:
            g_shown = (second / first) ** (1 / 3) - 1
        else:
            g_shown = None
        g = None if g_shown is None else min(g_shown, g_sales, R - 1e-9)   # (f) cut
        gg = g if g is not None else 0.0
        # (e): in the maintenance and depreciation cases the growth spending is charged against the growth it buys,
        # for ten years, stopping with growth; the all-spending case already carries it
        gspend = (sum(capex_all[y] - (sust[y] if case == 'maint' else da[y]) for y in yrs) / 5) if case != 'all' else 0.0
        ann = lambda r: sum(gspend / (1 + r) ** t for t in range(1, 11))
        top_case = pv(avg, gg, R) - (ann(R) if gg > 0 else 0.0)
        no_g = avg / R
        lo, hi = sorted([no_g, top_case])
        fair = (avg / FLOOR + pv(avg, gg, FLOOR) - (ann(FLOOR) if gg > 0 else 0.0)) / 2
        avg_int = sum(interest.values()) / 5 * (1 - TAX)
        eq_avg = avg - avg_int
        eq_fair = (eq_avg / FLOOR + pv(eq_avg, gg, FLOOR) - (ann(FLOOR) if gg > 0 else 0.0)) / 2 - pref - nci
        # floor test: expected return at the price on the best case = rate r* at which pv(case) = EV
        def irr(base, gg):
            lo_r, hi_r = 0.001, 0.5
            for _ in range(200):
                m = (lo_r + hi_r) / 2
                if pv(base, gg, m) > ev: lo_r = m
                else: hi_r = m
            return m
        best_irr = max(irr(avg, 0.0), irr(avg, gg)) if avg > 0 else float('nan')  # growth spending ignored: the most generous case
        res[(case, wc_name)] = (avg, g_shown, g, lo, hi, fair, eq_fair)
        print(f"\n[{case} | {wc_name}] yearly " + ", ".join(f"{y}:{o[y]:.1f}" for y in yrs))
        print(f"  5y avg owner cash {avg:.1f}; halves {first:.1f} -> {second:.1f}; shown growth {('n/a' if g_shown is None else f'{g_shown*100:.1f}%')}; carried {('0 (no-growth alone)' if g is None else f'{g*100:.2f}%')}")
        print(f"  growth spending charged (avg/yr, 10y) {gspend:.1f}")
        print(f"  whole-business value no-growth {no_g:.1f}, growth case (net of growth spending) {top_case:.1f}")
        print(f"  per share: {(lo-claims)/SH:.2f} to {(hi-claims)/SH:.2f}  (price {PRICE})")
        print(f"  most generous expected return at the price (growth spending ignored; rate equating value to EV {ev:.0f}): {best_irr*100:.2f}%")
        print(f"  FAIR PRICE all-equity {(fair-claims)/SH:.2f}/share; equity-only (owner cash after after-tax interest {eq_avg:.1f}; pref and NCI deducted) {eq_fair/SH:.2f}/share")

# --- serial-acquirer check and the organic pair (specific (c), CONVENTION of 2026-10-12) ---
o = oc('maint', dwc_c)
purch = 609.3
before = sum(o.values())          # central owner cash already excludes the purchase (sustaining only)
print(f"\nserial-acquirer test: purchases {purch} vs half of owner cash before purchases {before/2:.1f} -> {'ORGANIC PAIR CENTRAL' if purch > before/2 else 'default'}")
avg = before / 5
g = g_sales                        # filer reports no organic growth; total sales growth used as its upper bound
gsp = sum(capex_all[y] - sust[y] for y in yrs) / 5 - purch / 5
annR = sum(gsp / (1 + R) ** t for t in range(1, 11)); annF = sum(gsp / (1 + FLOOR) ** t for t in range(1, 11))
no_g = avg / R; gro = pv(avg, g, R) - annR
lo, hi = sorted([no_g, gro])
print(f"organic pair: growth spending ex-purchase {gsp:.1f}/yr; no-growth {no_g:.1f}; growth case {gro:.1f}; per share {(lo-claims)/SH:.2f} to {(hi-claims)/SH:.2f}")
fair = (avg / FLOOR + pv(avg, g, FLOOR) - annF) / 2
eq_avg = avg - sum(interest.values()) / 5 * (1 - TAX)
eq_fair = (eq_avg / FLOOR + pv(eq_avg, g, FLOOR) - annF) / 2 - pref - nci
print(f"organic pair FAIR all-equity {(fair-claims)/SH:.2f}/share; equity-only {eq_fair/SH:.2f}/share")
