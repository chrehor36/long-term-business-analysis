# ABNB owner earnings - arithmetic only. Every input is from a filed statement named in the run file.
# $M. Newest vintage used where a later 10-K restated (FY2020 OCF -629.7 -> -740).
Y = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
OCF   = {2019: 222.7, 2020: -740, 2021: 2313, 2022: 3430, 2023: 3884, 2024: 4518, 2025: 4646}
SBC_CF= {2019: 97.5, 2020: 3003, 2021: 899, 2022: 930, 2023: 1120, 2024: 1407, 2025: 1592}   # cash-flow add-back
SBC_EQ= {2019: None, 2020: None, 2021: None, 2022: None, 2023: 1146, 2024: 1424, 2025: 1600}  # equity statement (incl. capitalised)
CAPEX = {2019: 125.5, 2020: 37, 2021: 25, 2022: 25, 2023: 47, 2024: 34, 2025: 33}
DA    = {2019: 114.2, 2020: 126, 2021: 138, 2022: 81, 2023: 44, 2024: 65, 2025: 91}
dUNE  = {2019: 176.3, 2020: -267, 2021: 496, 2022: 280, 2023: 242, 2024: 200, 2025: 122}   # unearned fees, in OCF
dFUNDS= {2019: 848.7, 2020: -1024, 2021: 1625, 2022: 1330, 2023: 936, 2024: 320, 2025: 401} # funds payable, in FINANCING
WHTAX = {2019: 0, 2020: 1527, 2021: 177, 2022: 607, 2023: 1224, 2024: 630, 2025: 561}      # financing
BUYB  = {2019: 0, 2020: 0, 2021: 0, 2022: 1500, 2023: 2252, 2024: 3430, 2025: 3789}
INTINC= {2019: 85.9, 2020: 27.1, 2021: 12.7, 2022: 186, 2023: 721, 2024: 818, 2025: 705}
REV   = {2019: 4805, 2020: 3378, 2021: 5992, 2022: 8399, 2023: 9917, 2024: 11102, 2025: 12241}
# year-end balances: own cash+marketable/short-term investments; funds receivable held for customers
OWN   = {2018: None, 2019: 3074, 2020: 6391, 2021: 8322, 2022: 9622, 2023: 10071, 2024: 10611, 2025: 11014}
FUNDS = {2019: 3145, 2020: 2181, 2021: 3715, 2022: 4783, 2023: 5869, 2024: 5931, 2025: 6959}
# quarter-end (letter Q2 2026, "Cash and other liquid assets" incl. restricted cash) for 2024-2025 five-point averages
OWNQ  = {2024: [10071+0, 11128, 11286, 11280, 10636], 2025: [10636, 11532, 11400, 11719, 11049]}
FUNDQ = {2024: [5869, 8737, 10342, 6573, 5931], 2025: [5931, 9175, 11067, 7209, 6959]}

def cust_share(y):
    if y in OWNQ:
        o = sum(OWNQ[y]) / 5; f = sum(FUNDQ[y]) / 5
    else:
        if y - 1 not in FUNDS or OWN.get(y - 1) is None:
            return None
        o = (OWN[y] + OWN[y - 1]) / 2; f = (FUNDS[y] + FUNDS[y - 1]) / 2
    return f / (f + o)

rows = {}
print("year   OCF    SBC   capex   D&A   dUnearn  custInt*  | OE_A capex  OE_A D&A | OE_B(-dUnearn) capex / D&A | OE_C(-custInt) capex / D&A | SBC/OCF")
for y in Y:
    s = cust_share(y)
    ci = INTINC[y] * s if s is not None else None
    a_cap = OCF[y] - SBC_CF[y] - CAPEX[y]
    a_da  = OCF[y] - SBC_CF[y] - DA[y]
    b_cap = a_cap - dUNE[y]; b_da = a_da - dUNE[y]
    c_cap = b_cap - ci if ci is not None else None
    c_da  = b_da - ci if ci is not None else None
    rows[y] = dict(a_cap=a_cap, a_da=a_da, b_cap=b_cap, b_da=b_da, c_cap=c_cap, c_da=c_da, ci=ci)
    sr = SBC_CF[y] / OCF[y] if OCF[y] > 0 else float('nan')
    print(f"{y} {OCF[y]:7.0f} {SBC_CF[y]:6.0f} {CAPEX[y]:6.0f} {DA[y]:6.0f} {dUNE[y]:7.0f}  {('%.0f (%.0f%%)' % (ci, 100*s)) if ci is not None else 'n/a':>10} | {a_cap:7.0f} {a_da:7.0f} | {b_cap:7.0f} {b_da:7.0f} | {(c_cap if c_cap is not None else float('nan')):7.0f} {(c_da if c_da is not None else float('nan')):7.0f} | {100*sr:6.1f}%")

# TTM to 2026-06-30 from FY2025 minus H1 2025 plus H1 2026
TT = dict(OCF=4646-2764+2978, SBC=1592-782+897, CAPEX=33-21+21, DA=91-(25+21)+(22+17), dUNE=122-1236+1085, INT=705-363+338)
tt_a_cap = TT['OCF']-TT['SBC']-TT['CAPEX']; tt_a_da = TT['OCF']-TT['SBC']-TT['DA']
print("TTM Jun-2026", TT, "OE_A capex", tt_a_cap, "OE_A D&A", tt_a_da, "OE_B", tt_a_cap-TT['dUNE'], tt_a_da-TT['dUNE'], "SBC/OCF %.1f%%" % (100*TT['SBC']/TT['OCF']))

def mean(keys, field):
    vals = [rows[k][field] for k in keys]
    if any(v is None for v in vals): return None
    return sum(vals) / len(vals)

W = {
 "5y 2021-2025 (ex-2020, corpus default)": [2021, 2022, 2023, 2024, 2025],
 "5y 2020-2024 (incl. 2020)":             [2020, 2021, 2022, 2023, 2024],
 "6y 2020-2025 (full listed history)":     [2020, 2021, 2022, 2023, 2024, 2025],
 "3y 2023-2025":                           [2023, 2024, 2025],
 "7y 2019-2025 (incl. pre-IPO 2019)":      Y,
}
print()
for name, ks in W.items():
    out = [name]
    for fld in ['a_cap', 'a_da', 'b_cap', 'b_da', 'c_cap', 'c_da']:
        m = mean(ks, fld); out.append(f"{fld}={m:,.0f}" if m is not None else f"{fld}=n/a")
    print("  ".join(out))

CAP = 170.19 * 589585682 / 1e6
print("\ncap $M", round(CAP, 1))
for name, ks in W.items():
    lo = min(mean(ks, 'a_cap'), mean(ks, 'a_da')); hi = max(mean(ks, 'a_cap'), mean(ks, 'a_da'))
    print(f"{name}: OE_A {lo:,.0f}..{hi:,.0f}  yield {100*lo/CAP:.2f}%..{100*hi/CAP:.2f}%")
    b = [mean(ks, 'b_cap'), mean(ks, 'b_da')]
    print(f"      OE_B {min(b):,.0f}..{max(b):,.0f}  yield {100*min(b)/CAP:.2f}%..{100*max(b)/CAP:.2f}%")
    c = [mean(ks, 'c_cap'), mean(ks, 'c_da')]
    if None not in c:
        print(f"      OE_C {min(c):,.0f}..{max(c):,.0f}  yield {100*min(c)/CAP:.2f}%..{100*max(c)/CAP:.2f}%")
print(f"TTM OE_A {min(tt_a_cap,tt_a_da):,.0f}..{max(tt_a_cap,tt_a_da):,.0f} yield {100*min(tt_a_cap,tt_a_da)/CAP:.2f}%..{100*max(tt_a_cap,tt_a_da)/CAP:.2f}%")

# SBC/OCF cumulative
def cum(ks, extra_sbc=0, extra_ocf=0):
    s = sum(SBC_CF[k] for k in ks) + extra_sbc; o = sum(OCF[k] for k in ks) + extra_ocf
    return s, o, 100 * s / o
print("\nSBC/OCF cumulative")
print(" 2020-2025", cum([2020, 2021, 2022, 2023, 2024, 2025]))
print(" 2020-H1 2026", cum([2020, 2021, 2022, 2023, 2024, 2025], 897, 2978))
print(" 2021-2025", cum([2021, 2022, 2023, 2024, 2025]))
print(" 2021-H1 2026", cum([2021, 2022, 2023, 2024, 2025], 897, 2978))
print(" 2019-2025", cum(Y))
print(" SBC % revenue", {y: round(100*SBC_CF[y]/REV[y], 1) for y in Y})

# cash to hold the count
print("\nbuybacks + withholding vs SBC")
for y in Y:
    print(y, "buyback", BUYB[y], "withhold", WHTAX[y], "sum", BUYB[y]+WHTAX[y], "SBC", SBC_CF[y], "sum/OCF %.0f%%" % (100*(BUYB[y]+WHTAX[y])/OCF[y]) if OCF[y] > 0 else '')
tb = sum(BUYB.values()) + 2139; tw = sum(WHTAX.values()) + 305
print("2020-H1 2026 buybacks", tb, "withholding", tw, "total", tb+tw)
tw21 = tw - 1527
print("2021-H1 2026 withholding", tw21, "buybacks", tb, "total", tb + tw21)
SH = {2020: 599.197, 2021: 633.524, 2022: 631, 2023: 638, 2024: 623, 2025: 602, '2026-06': 590, '2026-07-15 cover': 589.585682}
print("shares", SH)
print("net change Dec2020->Jul2026 %.1fM (%.1f%%)" % (589.585682-599.197, 100*(589.585682/599.197-1)))
print("net change Dec2021->Jul2026 %.1fM (%.1f%%)" % (589.585682-633.524, 100*(589.585682/633.524-1)))
print("net change Dec2022->Jul2026 %.1fM (%.1f%%)" % (589.585682-631, 100*(589.585682/631-1)))
spent22 = 1500+2252+3430+3789+2139 + 607+1224+630+561+305
print("cash 2022-H1 2026 on buybacks+withholding", spent22, "per share retired since Dec-2022 $%.0f" % (spent22/(631-589.585682)))
# Pay: cash OE after the cash cost of holding the share count flat, 2022-2025
for y in [2022, 2023, 2024, 2025]:
    print(y, "OCF - capex - buyback - withholding =", OCF[y]-CAPEX[y]-BUYB[y]-WHTAX[y])
