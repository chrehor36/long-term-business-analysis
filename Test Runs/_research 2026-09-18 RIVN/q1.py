# Q1 unit economics from the filed faces ($M); segment data FY2023-25 (FY2025 10-K Note 18), H1 2026 (10-Q Note 15)
rows = {
 # yr: (total rev, auto rev, auto cost, credits, S&S rev, S&S GP, JV rev, total GP, op loss, deliveries)
 "FY2021": (55, None, None, 0, None, None, 0, -465, -4220, 920),
 "FY2022": (1658, None, None, 0, 104, None, 0, -3123, -6856, 20332),
 "FY2023": (4434, 4132, 6150, 73, 302, -12, 0, -2030, -5739, 50122),
 "FY2024": (4970, 4486, 5693, 333, 484, 7, 73, -1200, -4689, 51579),
 "FY2025": (5387, 3830, 4262, 197, 1557, 576, 836, 144, -3585, 42247),
 "H1 2026": (3039, 2051, 2149, 167, 988, 396, 590, 298, -1717, 22559),
}
for y,(tr,ar,ac,cr,sr,sg,jv,gp,ol,d) in rows.items():
    out=[y, f"rev/deliv {tr/d*1000:,.1f}k" ]
    if ar:
        out += [f"auto rev/deliv {ar/d*1000:.1f}k", f"auto cost/deliv {ac/d*1000:.1f}k", f"auto GP {ar-ac}", f"auto GP less credits {ar-ac-cr}", f"auto GP/deliv {(ar-ac)/d*1000:.1f}k"]
    out += [f"GP less JV rev {gp-jv}", f"op margin {ol/tr*100:.0f}%", f"op loss/deliv {ol/d*1000:.1f}k"]
    print(" | ".join(out))
