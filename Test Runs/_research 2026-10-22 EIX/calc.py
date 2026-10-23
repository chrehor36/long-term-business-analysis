"""EIX run 2026-10-22: Q7 COMPUTATION, NOT A CLEARANCE. Inputs transcribed from the 10-K cash-flow statements
(XBRL first/latest 10-K vintage, cross-checked 2023-2025 to the FY2025 10-K, acc. 0000827052-26-000012) and the
Q2 2026 10-Q (acc. 0000827052-26-000059). USD millions."""
yrs   = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
ocf   = [3597, 3177, -307, 1263,   11, 3216, 3401, 5014, 5800]
sbc   = [  23,   21,   29,   29,   39,   42,   46,   57,   57]
capex = [3844, 4509, 4877, 5484, 5505, 5778, 5448, 5707, 6515]
da    = [2115, 1940, 1803, 2029, 2288, 2633, 2635, 2866, 3237]
pref_sce = [125, 121, 121, 118, 106, 110, 117, 168, 136]   # SCE preference dividends paid (noncontrolling)
pref_eix = [  0,   0,   0,   0,  60,  74, 108,  88, 104]   # EIX preferred dividends
ltd_iss = [2233, 3237, 3696, 3073, 5412, 5971, 5121, 5256, 5133]
ltd_rep = [1285,  654,   82, 1099, 1037, 1085, 2498, 2701, 2052]
int_paid= [ 548,  595,  705,  836,  887, 1001, 1401, 1588, 1716]
ALLOWED_DEBT = 0.43          # CPUC authorized long-term debt share (10-K, Cost of Capital Application)
RECOV = {2025: 1600, 'woolsey_2026': 2000}   # 2017/2018 wildfire cost recoveries received through securitization
SOV = 0.0529; FLOOR = 0.10
SH = 384.813979; PRICE = 57.90
NET_DEBT_JUN26 = 1521 + 3797 + 37085 - 242   # short-term + current LTD + LTD - cash, 10-Q 2026-06-30
JULY_BONDS = 2000; PREF_JUN26 = 83 + 1564

def series():
    M, A, AE = [], [], []
    for i, y in enumerate(yrs):
        pref = pref_sce[i] + pref_eix[i]
        m = ocf[i] - sbc[i] - pref - da[i]                       # maintenance-only, equity-only
        credit = min(ltd_iss[i] - ltd_rep[i], ALLOWED_DEBT * capex[i])
        a = ocf[i] - sbc[i] - pref - capex[i] + credit           # all spending, debt credit to allowed share
        ae = ocf[i] - sbc[i] - da[i] + int_paid[i] * (1 - 0.28)  # all-equity, maintenance-only, before interest
        M.append(m); A.append(a); AE.append(ae)
    return M, A, AE
M, A, AE = series()
print("year   M(maint,eq-only)   A(all-spend+credit)   AE(all-equity maint)")
for i, y in enumerate(yrs):
    print(y, f"{M[i]:10.0f} {A[i]:14.0f} {AE[i]:14.0f}")
def avg(lst, idx): return sum(lst[i] for i in idx) / len(idx)
win = range(4, 9); epi = range(0, 9)
cases = {
 "episode 2017-2025, M, recoveries 3.6B": (sum(M) + 3600) / 9,
 "window 2021-2025, M, TKM 1.6B in window": (sum(M[i] for i in win) + 1600) / 5,
 "window 2021-2025, M, no recoveries": avg(M, win),
 "window 2021-2025, M, both recoveries": (sum(M[i] for i in win) + 3600) / 5,
 "episode 2017-2025, A, recoveries 3.6B": (sum(A) + 3600) / 9,
 "window 2021-2025, A, TKM 1.6B": (sum(A[i] for i in win) + 1600) / 5,
}
for k, v in cases.items():
    val = v / SOV
    print(f"{k:45s} base {v:8.0f}  no-growth value {val:9.0f}M  ${val/SH:7.2f}/sh  fair@10% ${v/FLOOR/SH:7.2f}/sh  yield at price {v/(PRICE*SH)*100:5.2f}%")
# halves test for growth (spec b): first and second halves of the series
fh = avg(M, range(0, 4)); sh_ = (M[5] + M[6] + M[7] + M[8] + 3600) / 4
print("episode halves M: 2017-2020", round(fh), " 2022-2025 (+recoveries)", round(sh_))
wf = avg(M, range(4, 6)); ws = (M[7] + M[8] + 1600) / 2
print("window halves M: 2021-2022", round(wf), " 2024-2025 (+TKM)", round(ws))
# all-equity beside
ae_epi = (sum(AE) + sum(pref_sce) * 0 + 3600) / 9
ev_claims = NET_DEBT_JUN26 + JULY_BONDS + PREF_JUN26
for lbl, base in [("episode", ae_epi), ("window", (sum(AE[i] for i in win) + 1600) / 5)]:
    v = base / SOV; f = base / FLOOR
    print(f"all-equity {lbl}: base {base:.0f}  value {v:.0f} less claims {ev_claims} = {(v-ev_claims)/SH:.2f}/sh ; fair {(f-ev_claims)/SH:.2f}/sh")
print("market cap", round(PRICE * SH), "net debt Jun-26", NET_DEBT_JUN26, "+July bonds", JULY_BONDS, "preferred", PREF_JUN26)
# coverage: (pre-tax income + interest expense) / interest expense
for y, pti, ie in [(2023, 1515, 1612), (2024, 1563, 1869), (2025, 5992, 1539)]:
    print(y, "coverage", round((pti + ie) / ie, 2))

# --- Whose tax (Q7 convention): owner cash at the statutory rate, shelter PV added at the long rate ---
book_tax = [281, -739, -278, -305, -136, -162, 108, 17, 1291]
cash_tax = [1, -135, -85, -34, -88, -49, 0, 51, 83]   # 2025: expense 1,291 less deferred 1,208 (10-K cash flow), no tag
adj_epi = (sum(book_tax) - sum(cash_tax)) / 9
adj_win = (sum(book_tax[i] for i in win) - sum(cash_tax[i] for i in win)) / 5
SHELTER = 3100; USE = 554     # 10-K: ~$3.1B tax-effected NOL and credits; 2025 GRC authorized income taxes $554M a year
n = SHELTER / USE
pv_shelter = USE * (1 - (1 + SOV) ** -n) / SOV
print(f"tax adj episode {adj_epi:.0f}/yr, window {adj_win:.0f}/yr; shelter used over {n:.1f} yrs, PV {pv_shelter:.0f}M = ${pv_shelter/SH:.2f}/sh")
final = {
 "CENTRAL episode 2017-2025, maint-only, eq-only": (sum(M) + 3600) / 9 - adj_epi,
 "beside: window 2021-2025, maint-only, TKM in window": (sum(M[i] for i in win) + 1600) / 5 - adj_win,
 "beside: window, maint-only, both recoveries": (sum(M[i] for i in win) + 3600) / 5 - adj_win,
 "beside: window, maint-only, no recoveries": avg(M, win) - adj_win,
 "beside: episode, all spending + debt credit": (sum(A) + 3600) / 9 - adj_epi,
 "beside: window, all spending + debt credit, TKM": (sum(A[i] for i in win) + 1600) / 5 - adj_win,
}
for k, b in final.items():
    v = b / SOV / SH + pv_shelter / SH
    f = b / FLOOR / SH + pv_shelter / SH
    r = b / (PRICE * SH - pv_shelter) * 100
    print(f"{k:52s} base {b:6.0f}  value ${v:7.2f}  fair ${f:7.2f}  no-growth return at price {r:5.2f}%")
