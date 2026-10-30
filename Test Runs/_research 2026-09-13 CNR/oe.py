# Pro forma owner earnings for Core Natural Resources, built by ADDING the two companies' own filed
# cash-flow statements. All figures in $ thousands, transcribed from the filed statements named in
# the run file (CONSOL/Core 10-Ks FY2021, FY2022, FY2024, FY2025; 10-Q 2026-06-30; Arch 10-Ks FY2021,
# FY2023; Arch 10-Q 2024-09-30). FL = payments on finance lease obligations (financing section).
# ARO_FUND = Arch "Contribution to fund for asset retirement obligations" (inside Arch OCF).
C = {  # CONSOL / Core: OCF, SBC, CAPEX, DA, FL, REV(total revenue & other income or revenues), NI
 2019: dict(ocf=244566, sbc=12760, capex=169739, da=207097, fl=18549),
 2020: dict(ocf=129331, sbc=11579, capex=86004,  da=210760, fl=28295),
 2021: dict(ocf=305569, sbc=6632,  capex=132752, da=224583, fl=27447),
 2022: dict(ocf=650990, sbc=7890,  capex=171506, da=226878, fl=24511),
 2023: dict(ocf=857949, sbc=10046, capex=167791, da=241317, fl=25335),
 2024: dict(ocf=476390, sbc=11350, capex=177988, da=223526, fl=10518),
}
A = {  # Arch
 2019: dict(ocf=419714, sbc=21989, capex=266356, da=111621, fl=0, fund=0),
 2020: dict(ocf=61106,  sbc=17435, capex=285821, da=121552, fl=0, fund=0),
 2021: dict(ocf=238284, sbc=20539, capex=245440, da=120327, fl=0, fund=20000),
 2022: dict(ocf=1209540,sbc=27383, capex=172728, da=133300, fl=0, fund=115993),
 2023: dict(ocf=635374, sbc=25443, capex=176037, da=146418, fl=0, fund=6273),
}
A9m24 = dict(ocf=212359, sbc=15819, capex=126888, da=118149, fund=5667)
A9m23 = dict(ocf=453818, sbc=19699, capex=121030, da=108273, fund=4421)
# Arch four quarters to 2024-09-30 = FY2023 - 9M2023 + 9M2024 (filed figures; misaligned one quarter vs CONSOL FY2024)
A[2024] = {k: A[2023][k] - A9m23[k] + A9m24[k] for k in ("ocf","sbc","capex","da","fund")}; A[2024]["fl"] = 0
CORE = {
 2025: dict(ocf=305752, sbc=32918, capex=284581, da=621067, fl=12554),
}
H25 = dict(ocf=110523, sbc=32027, capex=154007, da=290819, fl=5628)
H26 = dict(ocf=369847, sbc=8635,  capex=174998, da=313057, fl=16346)
TTM = {k: CORE[2025][k] - H25[k] + H26[k] for k in H25}

def oe(d, fund_back=False):
    add = d.get("fund", 0) if fund_back else 0
    base = d["ocf"] - d["sbc"] + add
    return dict(capex_fl=base - d["capex"] - d.get("fl", 0), capex=base - d["capex"], da=base - d["da"])

rows = {}
for y in range(2019, 2025):
    comb = {k: C[y].get(k, 0) + A[y].get(k, 0) for k in ("ocf","sbc","capex","da","fl")}
    comb["fund"] = A[y].get("fund", 0)
    rows[y] = comb
rows[2025] = CORE[2025]; rows["TTM 2026-06"] = TTM

print(f'{"year":<12}{"OCF":>9}{"SBC":>8}{"capex":>9}{"FL":>7}{"D&A":>8} | {"OE capex+FL":>11}{"OE capex":>10}{"OE D&A":>9} | {"fund addback":>12}')
for y, d in rows.items():
    o = oe(d)
    print(f'{str(y):<12}{d["ocf"]/1e3:>9.1f}{d["sbc"]/1e3:>8.1f}{d["capex"]/1e3:>9.1f}{d.get("fl",0)/1e3:>7.1f}{d["da"]/1e3:>8.1f} | {o["capex_fl"]/1e3:>11.1f}{o["capex"]/1e3:>10.1f}{o["da"]/1e3:>9.1f} | {d.get("fund",0)/1e3:>12.1f}')
print("\nstandalone components:")
for y in range(2019, 2025):
    print(y, "CONSOL", {k: round(v/1e3,1) for k,v in oe(C[y]).items()}, "ARCH", {k: round(v/1e3,1) for k,v in oe(A[y]).items()})

def mean(keys, col, fund_back=False):
    v = [oe(rows[k], fund_back)[col] for k in keys]
    return sum(v)/len(v)/1e3
W = {
 "PF 5y pre-close 2019-23": [2019,2020,2021,2022,2023],
 "PF 3y pre-close 2021-23": [2021,2022,2023],
 "PF 5y 2020-24": [2020,2021,2022,2023,2024],
 "PF 5y 2021-25 (spans close)": [2021,2022,2023,2024,2025],
 "PF 3y 2023-25 (spans close)": [2023,2024,2025],
 "2024-25 + TTM? no: PF 2024 & 2025": [2024,2025],
 "post-close FY2025": [2025],
 "post-close TTM 2026-06": ["TTM 2026-06"],
 "trough-to-date: 2024,2025,TTM": [2024,2025,"TTM 2026-06"],
 "PF 7y 2019-25": [2019,2020,2021,2022,2023,2024,2025],
}
print("\nwindow means ($M): capex+FL | capex only | D&A | (capex+FL with Arch fund added back)")
for n, ks in W.items():
    print(f'{n:<38}{mean(ks,"capex_fl"):>9.1f}{mean(ks,"capex"):>9.1f}{mean(ks,"da"):>9.1f}{mean(ks,"capex_fl",True):>9.1f}')
cap = 49636257*97.47/1e3
print("\ncap $M", round(cap/1e3,1))
