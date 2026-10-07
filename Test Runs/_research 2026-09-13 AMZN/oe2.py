# oe2.py - owner earnings for Amazon, AUDITED rebuild of the killed session's oe.py (2026-09-13 resume).
# Every input below was re-read against the filed cash-flow statement, the supplemental cash-flow table,
# the property-and-equipment note or the segment note (see the run file, Q4, for accessions).
# Changes from oe.py: (1) BTS 2021 corrected 5,846 -> 5,616 (FY2021 10-K supplemental table; oe.py did not use
# BTS in any construction, so no oe.py output changes); (2) BTS 2022 = 3,220 from the FY2022 10-K segment
# footnote ($3.2 billion + $20 million, rounded in the filing; the supplemental line was discontinued);
# (3) BTS for TTM not disclosed in the 10-Q footnotes -> 0, flagged; (4) two constructions added:
# "screen" (gross capex + finance-lease additions = current floor_screen.capital_acquired) and
# "net+leases" (capex - proceeds + finance-lease additions + build-to-suit additions, the MSFT-run convention);
# (5) the working-capital lines by year for the 30%-of-OCF flag; (6) the window excluding 2021-22.
Y    = ["2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","TTM2Q26"]
OCF  = [17203,18365,30723,38514,66064,46327,46752,84946,115877,139514,161403]
SBC  = [2975,4215,5418,6864,9208,12757,19621,24023,22011,19467,19314]
CAPEX= [7804,11955,13427,16861,40140,61053,63645,52729,82999,131819,173028]
PROC = [1067,1897,2104,4172,5096,5657,5324,4596,5341,3499,4021]
FLADD= [5704,9637,10615,13723,11588,7061,675,642,854,2911,4048]
BTS  = [1209,3541,3641,1362,2267,5616,3220,357,97,441,0]
FLREP= [3860,4799,7449,9628,10642,11163,7941,4384,2043,1557,1599]
FOREP= [147,200,337,27,53,162,248,271,669,328,308]
TNA  = [13585,29783,25068,30018,57976,72325,60836,48344,85752,142352,142352-58210+118648]
DEP  = [6400,8831,12138,15150,16239,22909,24924,30225,32067,41860,41860-18822+26703]
REV  = [135987,177866,232887,280522,386064,469822,513983,574785,637959,716924,716924-323369+382125]
# working-capital lines (changes in operating assets and liabilities), newest vintage available on disk
WC = {
 "2016": {"inventories":-1426,"AR and other":-3436,"AP":5030,"accrued":1724,"unearned":1955},
 "2017": {"inventories":-3583,"AR and other":-4780,"AP":7100,"accrued":283,"unearned":738},
 "2018": {"inventories":-1314,"AR and other":-4615,"AP":3263,"accrued":472,"unearned":1151},
 "2019": {"inventories":-3278,"AR and other":-7681,"AP":8193,"accrued":-1383,"unearned":1711},
 "2020": {"inventories":-2849,"AR and other":-8169,"AP":17480,"accrued":5754,"unearned":1265},
 "2021": {"inventories":-9487,"AR and other":-18163,"AP":3602,"accrued":2123,"unearned":2314},
 "2022": {"inventories":-2592,"AR and other":-21897,"AP":2945,"accrued":-1558,"unearned":2216},
 "2023": {"inventories":1449,"AR and other":-8348,"other assets":-12265,"AP":5473,"accrued":-2428,"unearned":4578},
 "2024": {"inventories":-1884,"AR and other":-3249,"other assets":-14483,"AP":2972,"accrued":-2904,"unearned":4007},
 "2025": {"inventories":-3002,"AR and other":-7333,"other assets":-15632,"AP":11231,"accrued":-5019,"unearned":-214},
 "TTM2Q26": {"inventories":2078,"AR and other":-21409,"other assets":-17787,"AP":13921,"accrued":-6069,"unearned":-749},
}
C = {  # the (c) constructions
 "gross capex (run.py)":            lambda i: CAPEX[i],
 "gross capex + FL adds (screen)":  lambda i: CAPEX[i]+FLADD[i],
 "net capex + FL + BTS adds":       lambda i: CAPEX[i]-PROC[i]+FLADD[i]+BTS[i],
 "cash plant (net capex + lease principal)": lambda i: CAPEX[i]-PROC[i]+FLREP[i]+FOREP[i],
 "formation (TNA)":                 lambda i: TNA[i],
 "1.3x P&E D&A":                    lambda i: 1.3*DEP[i],
 "P&E D&A (default)":               lambda i: DEP[i],
}
rows = []
for i, y in enumerate(Y):
    base = OCF[i]-SBC[i]
    r = {"y": y, "base": base, "dep": DEP[i], "sbc_ocf": SBC[i]/OCF[i], "tna_dep": TNA[i]/DEP[i]}
    for k, f in C.items():
        r[k] = base - f(i)
    rows.append(r)
print("| year | OCF | SBC | OCF-SBC | " + " | ".join(C) + " | TNA/D&A | SBC/OCF |")
print("|" + "---|"*(len(C)+6))
for r, i in zip(rows, range(len(Y))):
    print(f"| {r['y']} | {OCF[i]:,} | {SBC[i]:,} | {r['base']:,} | " + " | ".join(f"{r[k]:,.0f}" for k in C) + f" | {r['tna_dep']:.2f}x | {r['sbc_ocf']*100:.1f}% |")
W = {"5-yr 2021-25 (default)": ["2021","2022","2023","2024","2025"],
     "3-yr 2023-25": ["2023","2024","2025"],
     "10-yr 2016-25": Y[:10],
     "5-yr 2016-20": ["2016","2017","2018","2019","2020"],
     "5-yr to TTM (2022-25 + TTM, overlaps H2 2025)": ["2022","2023","2024","2025","TTM2Q26"],
     "TTM to 2026-06-30": ["TTM2Q26"],
     "8-yr 2016-25 excluding 2021-22": [y for y in Y[:10] if y not in ("2021","2022")],
     "3-yr 2023-25 (no 2021-22 in it)": ["2023","2024","2025"]}
def mean(k, ys):
    v = [r[k] for r in rows if r["y"] in ys]; return sum(v)/len(v)
print()
print("| window | " + " | ".join(C) + " |")
print("|" + "---|"*(len(C)+1))
for w, ys in W.items():
    print(f"| {w} | " + " | ".join(f"{mean(k, ys):,.0f}" for k in C) + " |")
print()
for w, ys in [("10-yr 2016-25", Y[:10]), ("5-yr 2021-25", W["5-yr 2021-25 (default)"]), ("TTM", ["TTM2Q26"])]:
    idx = [Y.index(y) for y in ys]
    print(f"{w}: cumulative SBC/OCF = {100*sum(SBC[i] for i in idx)/sum(OCF[i] for i in idx):.1f}%")
print()
print("WORKING-CAPITAL FLAG (a single line moving by more than 30% of the year's OCF):")
for i, y in enumerate(Y):
    for k, v in WC[y].items():
        if abs(v) > 0.30*OCF[i]:
            print(f"  FIRES {y}: {k} {v:+,} = {100*v/OCF[i]:+.1f}% of OCF {OCF[i]:,}")
    s = sum(WC[y].values())
    print(f"  {y}: sum of working-capital lines {s:+,} ({100*s/OCF[i]:+.1f}% of OCF)")
# renewal at current scale, CONVENTION: gross P&E by class / midpoint of filed useful life (FY2025 10-K Note 3)
gross25 = {"land and buildings":(155121,40),"servers and networking":(172492,5.5),"heavy equipment":(65545,11.5),"other equipment":(63376,6.5)}
ren = sum(v/l for v,l in gross25.values())
print()
print(f"Renewal at 2025 year-end scale (gross/life, land included in buildings, fully depreciated assets included): {ren:,.0f} vs 2025 P&E D&A 41,860 = {ren/41860:.2f}x")
