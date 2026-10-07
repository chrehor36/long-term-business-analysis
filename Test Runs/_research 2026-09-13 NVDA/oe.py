"""Q4 owner earnings for the NVDA run, built by hand from the FILED consolidated statements of cash flows (companyfacts carries
no capex for FY2013-FY2021, Step 0). Newest vintage used where a year appears in two 10-Ks (none differed on these lines).
Sources: FY2017-FY2019 from the FY2019 10-K (0001045810-19-000023 per submissions; FY2017 also in the FY2017 10-K, matched);
FY2020 from the FY2022 10-K (0001045810-22-000036); FY2021-FY2023 from the FY2023 10-K (0001045810-23-000017); FY2024-FY2026 from
the FY2026 10-K (0001045810-26-000021); H1 FY2026 and H1 FY2027 from the Q2 FY2027 10-Q (0001045810-26-000075), H1 FY2026 also
matched on the Q2 FY2026 10-Q. Depreciation (P&E only) and intangible amortization from the 10-K notes. $M. Arithmetic only."""
Y = ["FY2017", "FY2018", "FY2019", "FY2020", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025", "FY2026"]
ocf = [1672, 3502, 3743, 4761, 5822, 9108, 5641, 28090, 64089, 102718]
sbc = [247, 391, 557, 844, 1397, 2004, 2709, 3549, 4737, 6386]
capex = [176, 593, 600, 489, 1128, 976, 1833, 1069, 3236, 6042]          # "Purchases related to property and equipment and intangible assets"
princ = [0, 0, 0, 0, 17, 83, 58, 74, 129, 101]                           # "Principal payments on property and equipment (and intangible assets)", financing
dep = [118, 144, 233, 355, 486, 611, 844, 894, 1300, 2355]               # Note: "Depreciation expense"; FY2025 note rounds to $1.3bn; FY2026 = D&A 2,843 - amortization 488
amort = [68, 55, 29, 25, 612, 563, 699, 614, 593, 488]
acq = [0, 0, 0, 4, 8524, 263, 49, 83, 1007, 1535 + 13000]                # "Acquisitions, net of cash acquired" (+ "Groq, Inc." investing line FY2026)
grant = [None, None, None, None, None, 3492, 4505, 5316, 7834, 9389]     # grant-date fair value of awards granted (10-K stock comp note)
prov = [None, None, None, None, 116, 354, 2170, 2200, 3700, 7200]        # provisions for inventory and excess purchase obligations (MD&A), gross
# TTM = FY2026 - H1 FY2026 + H1 FY2027
h1_26 = dict(ocf=42779, sbc=3099, capex=3122, princ=73, dep=1280 - 243, amort=243, acq=677)
h1_27 = dict(ocf=74421, sbc=3954, capex=4434, princ=92, dep=2124 - 470, amort=470, acq=298 + 2944)   # Groq deferred consideration paid in financing
T = {k: v for k, v in dict(ocf=ocf[-1], sbc=sbc[-1], capex=capex[-1], princ=princ[-1], dep=dep[-1], amort=amort[-1], acq=1535 + 13000).items()}
ttm = {k: T[k] - h1_26[k] + h1_27[k] for k in T}

def row(o, s, c, p, d):
    return dict(ocf_sbc=o - s, capex_end=o - s - c - p, dep_end=o - s - d, renew_end=o - s - 1.25 * d)

print("| year | OCF | SBC | OCF-SBC | capex (P&E and intangibles) + financed principal | P&E depreciation | capex / depreciation | OE, (c)=capex+principal | OE, (c)=P&E depreciation (default) | acquisitions incl. Groq |")
print("|---|---|---|---|---|---|---|---|---|---|")
rows = []
for i, y in enumerate(Y):
    r = row(ocf[i], sbc[i], capex[i], princ[i], dep[i]); rows.append(r)
    print(f"| {y} | {ocf[i]:,} | {sbc[i]:,} | {r['ocf_sbc']:,} | {capex[i]+princ[i]:,} | {dep[i]:,} | {(capex[i]+princ[i])/dep[i]:.2f}x | {r['capex_end']:,} | {r['dep_end']:,} | {acq[i]:,} |")
rt = row(ttm['ocf'], ttm['sbc'], ttm['capex'], ttm['princ'], ttm['dep'])
print(f"| TTM to 2026-07-26 | {ttm['ocf']:,} | {ttm['sbc']:,} | {rt['ocf_sbc']:,} | {ttm['capex']+ttm['princ']:,} | {ttm['dep']:,} | {(ttm['capex']+ttm['princ'])/ttm['dep']:.2f}x | {rt['capex_end']:,} | {rt['dep_end']:,} | {ttm['acq']:,} |")

def mean(idx, key):
    return sum(rows[i][key] for i in idx) / len(idx)

W = {"5-yr FY2022-FY2026 (default [E2-42])": range(5, 10), "3-yr FY2024-FY2026": range(7, 10), "10-yr FY2017-FY2026 (crosses Mellanox)": range(0, 10),
     "5-yr FY2017-FY2021 (crosses Mellanox)": range(0, 5), "4-yr FY2022-FY2025 + TTM (TTM overlaps H2 FY2026, stated)": None}
print("\n| window | OE, (c)=capex+principal | OE, (c)=depreciation | OE, capex end less acquisitions (Mellanox, Groq) | OE, capex end, SBC at grant-date value [E3-70] |")
print("|---|---|---|---|---|")
out = {}
for name, idx in W.items():
    if idx is None:
        vals = [rows[i] for i in range(6, 10)] + [rt]
        acqs = [acq[i] for i in range(6, 10)] + [ttm['acq']]
        ce = sum(v['capex_end'] for v in vals) / 5; de = sum(v['dep_end'] for v in vals) / 5
        print(f"| {name} | {ce:,.0f} | {de:,.0f} | {ce - sum(acqs)/5:,.0f} | n/a |")
        continue
    ce, de = mean(idx, 'capex_end'), mean(idx, 'dep_end')
    ca = ce - sum(acq[i] for i in idx) / len(idx)
    g = [i for i in idx if grant[i]]
    gs = (ce - sum(grant[i] - sbc[i] for i in g) / len(idx)) if len(g) == len(idx) else None
    out[name] = (ce, de, ca, gs)
    print(f"| {name} | {ce:,.0f} | {de:,.0f} | {ca:,.0f} | {'' if gs is None else f'{gs:,.0f}'} |")
print(f"| TTM to 2026-07-26 | {rt['capex_end']:,} | {rt['dep_end']:,} | {rt['capex_end']-ttm['acq']:,} | {rt['capex_end'] - (9389/6386 - 1)*ttm['sbc']:,.0f} (FY2026 grant/charge ratio 1.47x applied, CONVENTION) |")

# sensitivities for the (c) question beyond plant (disclosed judgments, shown both ways; nothing here is chosen)
print("\nTTM working capital lines (from the two cash-flow statements):")
wc26 = dict(ar=-15399, inv=-11324, prep=577, ap=3096, accr=5257, oltl=1844)
h126 = dict(ar=-4743, inv=-4880, prep=946, ap=2255, accr=3075, oltl=979)
h127 = dict(ar=-24590, inv=-10204, prep=-6480, ap=4125, accr=8015, oltl=1970)
wct = {k: wc26[k] - h126[k] + h127[k] for k in wc26}
print("  ", wct, "sum", sum(wct.values()), f"({sum(wct.values())/ttm['ocf']*100:.1f}% of TTM OCF)")
flags = [("FY2017 inventories", -375, 1672), ("FY2019 inventories", -776, 3743), ("FY2022 prepaid and other (supply prepayments $1.87bn)", -1715, 9108),
         ("FY2023 inventories", -2554, 5641), ("FY2023 prepaid and other", -1517, 5641), ("FY2024 accounts receivable", -6172, 28090),
         ("FY2025 accounts receivable", -13063, 64089), ("FY2026 accounts receivable", -15399, 102718), ("FY2026 inventories", -11324, 102718),
         ("H1 FY2027 accounts receivable", -24590, 74421), ("H1 FY2027 inventories", -10204, 74421)]
for n, v, o in flags:
    print(f"   {n}: {v:,} = {abs(v)/o*100:.1f}% of that period's OCF{'  <- fires (>30%)' if abs(v)/o > 0.30 else ''}")
eq_net_h127 = 42404 - 7241
print(f"equity purchases net of sales: FY2026 non-marketable {17502-84:,} (plus public equity inside 'purchases of marketable securities', not separable on the FY2026 face); H1 FY2027 {eq_net_h127:,}")
print(f"AI cloud agreements $36bn over ~6 years = ~{36000/6:,.0f} a year from FY2028; cloud service agreements $29bn (R&D capacity) ~{(8+7+6)/3*1000:,.0f} a year FY2028-30")
print(f"provisions gross, 5-yr FY2022-26 mean {sum(prov[5:10])/5:,.0f}; FY2023 provisions / (opening inventory 2,605 + opening obligations 9,000) = {2170/(2605+9000)*100:.1f}%")
print(f"same ratio on 2026-07-26 exposure (inventory 31,575 + supply and capacity 279,000): {0.187*(31575+279000):,.0f}")
