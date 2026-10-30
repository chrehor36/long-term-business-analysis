# Owner cash for ATO, FY2021-FY2025, from the filed cash-flow statements (USD millions).
# Sources: 10-K FY2025 (0000731802-25-000056) for FY2023-25; 10-K FY2022 (0000731802-22-000037) for FY2021-22.
Y = [2021, 2022, 2023, 2024, 2025]
OCF   = [-1084.251, 977.584, 3459.743, 1733.746, 2049.456]
URI   = [2080.311, 0.0, -2021.889, 0.0, 0.0]   # Winter Storm Uri reg-asset build (FY21) and securitization relief (FY23), filer's own lines
DEFTX = [155.355, 53.651, 108.215, 172.707, 268.606]  # deferred income taxes added back in OCF
SBC   = [21.035, 19.803, 21.588, 23.204, 30.504]      # employee stock-based compensation, equity statement
DA    = [477.977, 535.655, 604.327, 669.972, 734.745]
CAPEX = [1969.540, 2444.420, 2805.973, 2937.124, 3561.399]
INT   = [83.554, 102.811, 137.281, 190.632, 171.678]
REV   = [3407.490, 4201.662, 4275.357, 4165.187, 4702.755]
NI    = [665.563, 774.398, 885.862, 1042.895, 1198.754]
T = 0.21  # statutory federal rate for the interest shield (CONVENTION of this run)
rows = []
for i, y in enumerate(Y):
    ocfa = OCF[i] + URI[i]
    m_eq = ocfa - DEFTX[i] - SBC[i] - DA[i]          # maintenance = D&A, book tax, after interest
    m_ae = m_eq + INT[i] * (1 - T)                    # all-equity (before interest)
    a_eq = ocfa - DEFTX[i] - SBC[i] - CAPEX[i]        # all spending
    a_ae = a_eq + INT[i] * (1 - T)
    m_cash = ocfa - SBC[i] - DA[i] + INT[i]*(1-T)     # cash-tax variant, all-equity
    lit = OCF[i] - SBC[i] - DA[i]                     # literal window, D&A basis, no adjustments
    rows.append((y, ocfa, m_eq, m_ae, a_eq, a_ae, m_cash, lit, CAPEX[i]-DA[i]))
    print(f"FY{y}: OCF_adj {ocfa:8.1f}  maint/eq {m_eq:7.1f}  maint/AE {m_ae:7.1f}  allspend/eq {a_eq:8.1f}  allspend/AE {a_ae:8.1f}  maint/AE cash-tax {m_cash:7.1f}  literal D&A {lit:8.1f}  growth spend {CAPEX[i]-DA[i]:7.1f}  share of sales(maint/AE) {m_ae/REV[i]*100:4.1f}%")
avg = lambda k: sum(r[k] for r in rows) / 5
print("5-yr avg: maint/eq %.1f maint/AE %.1f allspend/eq %.1f allspend/AE %.1f cash-tax AE %.1f literal %.1f growth spend %.1f" % (avg(2), avg(3), avg(4), avg(5), avg(6), avg(7), avg(8)))
g = (rows[-1][3] / rows[0][3]) ** 0.25 - 1
print("shown growth maint/AE FY21->FY25: %.1f%%/yr" % (g * 100))
print("sales growth FY21->FY25: %.1f%%/yr" % (((REV[-1] / REV[0]) ** 0.25 - 1) * 100))
inc_ae = rows[-1][3] - rows[0][3]; inc_eq = rows[-1][2] - rows[0][2]
gs = sum(r[8] for r in rows[:4])
print("incremental return on growth spending FY21-24 (lagged): AE %.1f%%  eq %.1f%%  (spend %.0f)" % (inc_ae / gs * 100, inc_eq / gs * 100, gs))
