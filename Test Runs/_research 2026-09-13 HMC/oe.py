# Owner earnings, non-financial services perimeter, JPY millions.
# Sources: "CONSOLIDATED FINANCIAL SUMMARY 3 - Unaudited Consolidated Statements of Cash Flows Divided into
# Non-financial Services Businesses and Finance Subsidiaries" (results releases FY3/19-FY3/26, ir/pdf/*reference*),
# segment note D&A (20-Fs), consolidated cash-flow statement (lease repayments), Note 17 provisions (FY3/26).
import json

Y = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
nfs_ocf   = dict(zip(Y, [1138346, 1055023, 1050956, 1051818, 1352796, 2288129, 1883139, 1681944]))
fs_div    = dict(zip(Y, [60927, 69679, 65931, 175335, 213276, 225018, 305047, 96248]))   # reconciling item, dividends line
capex_ppe = dict(zip(Y, [420446, 370268, 318338, 267972, 475097, 354196, 515302, 640298]))
capex_int = dict(zip(Y, [184430, 227539, 228621, 178821, 154421, 257085, 333256, 280413]))
# segment-note D&A, Motorcycle + Automobile + Power products & other (excludes FS operating-lease depreciation, excludes impairment)
da = dict(zip(Y, [66680+603124+14198, 67512+555153+14742, 68258+515241+15644, 65423+510755+17018,
                  65746+600617+21571, 72590+655250+17400, 72443+642506+16356, 74343+601267+16055]))
lease_rep = dict(zip(Y, [47088, 78659, 67628, 80165, 78297, 80513, 78137, 80222]))    # consolidated, financing section
nfs_div_total = dict(zip(Y, [236169, 255419, 257036, 368882, 458175, 383107, 431386, 186327]))
eq_income = dict(zip(Y, [228827, 164203, 272734, 202512, 117445, 110817, 982, -162080]))
SBC = 3000            # upper bound per year: BIP + ESOP trusts, ~4.94M shares over three fiscal years (20-F Item 6.B)
EV_PROV_UNPAID = {2026: 667366 - 82954}   # Note 17: EV-related provisions added less written off in FY3/26

rows = {}
for y in Y:
    ind_ocf = nfs_ocf[y] - fs_div[y]
    ev = EV_PROV_UNPAID.get(y, 0)
    capex = capex_ppe[y] + capex_int[y]
    base = ind_ocf - ev - lease_rep[y] - SBC
    rows[y] = dict(ind_ocf=ind_ocf, ev_adj=ev, lease=lease_rep[y], capex=capex, da=da[y],
                   oe_capex=base - capex, oe_da=base - da[y],
                   oe_capex_noev=ind_ocf - lease_rep[y] - SBC - capex,
                   fs_div=fs_div[y], aff_div=nfs_div_total[y] - fs_div[y], eq_inc=eq_income[y],
                   undistributed=eq_income[y] - (nfs_div_total[y] - fs_div[y]))

def mean(ys, k):
    return sum(rows[y][k] for y in ys) / len(ys)

print(f"{'FY3/':6}{'ind OCF':>10}{'EVprov':>9}{'lease':>8}{'capex':>9}{'D&A':>8}{'OE(c=cpx)':>11}{'OE(c=DA)':>10}{'OE cpx noEV':>12}{'FS div':>8}{'undistr':>9}")
for y in Y:
    r = rows[y]
    print(f"{y:<6}{r['ind_ocf']:>10,}{r['ev_adj']:>9,}{r['lease']:>8,}{r['capex']:>9,}{r['da']:>8,}{r['oe_capex']:>11,}{r['oe_da']:>10,}{r['oe_capex_noev']:>12,}{r['fs_div']:>8,}{r['undistributed']:>9,}")

windows = {'3y FY3/24-26': [2024, 2025, 2026], '5y FY3/22-26 (default)': [2022, 2023, 2024, 2025, 2026],
           '8y FY3/19-26': Y, '5y FY3/21-25 (pre-write-off)': [2021, 2022, 2023, 2024, 2025]}
out = {'rows': rows, 'windows': {}}
print()
for name, ys in windows.items():
    w = {k: round(mean(ys, k)) for k in ['oe_capex', 'oe_da', 'oe_capex_noev', 'fs_div', 'undistributed', 'capex', 'da', 'ind_ocf']}
    out['windows'][name] = w
    print(f"{name:32} OE c=capex {w['oe_capex']:>9,}  c=D&A {w['oe_da']:>9,}  c=capex no EV adj {w['oe_capex_noev']:>9,}  FS div {w['fs_div']:>8,}  undistributed eq {w['undistributed']:>9,}  capex {w['capex']:>9,} D&A {w['da']:>8,}")
json.dump(out, open('oe_out.json', 'w'), indent=1)

CAP = 1664 * 3893016583 / 1e6   # JPY millions
print(f"\ncap JPY {CAP:,.0f}M")
for name, w in out['windows'].items():
    for lab, v in [('c=capex', w['oe_capex']), ('c=D&A', w['oe_da']), ('c=capex + FS div', w['oe_capex'] + w['fs_div']),
                   ('c=capex + FS div + undistributed', w['oe_capex'] + w['fs_div'] + w['undistributed'])]:
        print(f"  {name:32} {lab:34} {v:>10,.0f}  yield {100*v/CAP:5.2f}%")
