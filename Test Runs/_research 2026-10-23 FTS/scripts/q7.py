"""Q7 arithmetic for FTS (C$ millions). Inputs: table10.json (XBRL transcription, checked against the filed statements)."""
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
t = json.load(open('table10.json'))
Y = [2021, 2022, 2023, 2024, 2025]
def v(tag, y): return t[tag].get(f"{y}-12-31", 0) / 1e6
r = 0.0419      # Bank of Canada long-term benchmark bond yield, 2026-10-21
FLOOR = 0.10
shares = 510.9 + 4.365256   # 30 Jun 2026 interim balance sheet + issued 1 Jul to 4 Sep 2026 (prospectus supplement)
price = 80.99
mcap = price * shares
net_debt_pf = 35610   # pro forma 30 Jun 2026, prospectus supplement capitalization table (after the Sept 2026 notes and changes to 4 Sep)
prefs = 1623
DEBT_SHARE = (13.9*40.0 + 8.4*45.7 + 3.7*52.0 + 6.5*55.0 + 4.7*63.0 + 1.8*59.0 + 3.4*58.0) / 42.4 / 100
rows = []
for y in Y:
    ocf = v('NetCashProvidedByUsedInOperatingActivities', y)
    ppe = v('PaymentsToAcquirePropertyPlantAndEquipment', y); ia = v('PaymentsToAcquireIntangibleAssets', y)
    ciac = v('ProceedsFromContributionInAidOfConstruction', y); oth = v('PaymentsForProceedsFromOtherInvestingActivities', y)
    pref = v('PaymentsOfDividendsPreferredStockAndPreferenceStock', y); nci = v('PaymentsOfDividendsMinorityInterest', y)
    dda = v('DepreciationDepletionAndAmortization', y)
    # long-term debt raised only (Q7, The regulated utility: "the long-term debt raised over the window"); committed credit
    # facility borrowings are classified as long-term debt by the filer (Note 14), so they count; borrowings maturing in
    # three months or less are left out (checked 2026-10-23 on resume; the first draft counted them)
    debt = (v('ProceedsFromIssuanceOfLongTermDebt', y) - v('RepaymentsOfLongTermDebtAndCapitalSecurities', y)
            + v('ProceedsFromLinesOfCredit', y) - v('RepaymentsOfLinesOfCredit', y))
    divest = v('ProceedsFromDivestitureOfBusinessesNetOfCashDivested', y)
    intpaid = v('InterestPaidNet', y)
    pt = v('ProfitLoss', y) + v('IncomeTaxExpenseBenefit', y); tax = v('IncomeTaxExpenseBenefit', y) / pt
    spend = ppe + ia - ciac + oth
    rows.append(dict(y=y, ocf=ocf, spend=spend, divest=divest, dda=dda, growth=spend - dda, pref=pref, nci=nci, debt=debt, intpaid=intpaid, tax=tax,
                     rev=v('Revenues', y),
                     allsp=ocf - spend + divest - pref - nci, maint=ocf - dda - pref - nci))
print(f"allowed debt share (rate-base weighted, 2025 midyear rate base, Note 2 equity ratios): {DEBT_SHARE:.3f}")
print("year | OCF | spend net CIAC incl other | D&A | growth spend | pref | NCI div | LT debt raised | int paid | eff tax | all-spend OC | maint OC | revenue")
for d in rows:
    print(f"{d['y']} | {d['ocf']:,.0f} | {d['spend']:,.0f} | {d['dda']:,.0f} | {d['growth']:,.0f} | {d['pref']:,.0f} | {d['nci']:,.0f} | {d['debt']:,.0f} | {d['intpaid']:,.0f} | {d['tax']:.3f} | {d['allsp']:,.0f} | {d['maint']:,.0f} | {d['rev']:,.0f}")
S = lambda k: sum(d[k] for d in rows)
debt_tot = S('debt')
capA = DEBT_SHARE * S('spend'); creditA = min(debt_tot, capA)
capB = DEBT_SHARE * S('growth'); creditB = min(debt_tot, capB)
print(f"\nnet debt raised 2021-25: {debt_tot:,.0f}; cap on all spending {capA:,.0f} -> credit {creditA:,.0f}; cap on growth spending {capB:,.0f} -> credit {creditB:,.0f}")
def pv(c0, g, rate, gcost0=0.0):
    """ten years at g, then no growth; gcost0 = growth spending charged in years 1-10, growing at g, stopping after year ten"""
    tot = 0.0
    for k in range(1, 11):
        tot += (c0 * (1+g)**k - gcost0 * (1+g)**k) / (1+rate)**k
    tot += c0 * (1+g)**10 / rate / (1+rate)**10
    return tot
def ps(x, nd=0.0): return (x - nd) / shares
# literal per-year series for case A (utility paragraph: all spending charged, debt credited) -- credit spread pro rata to each year's debt raised
serA = [d['allsp'] + d['debt'] * creditA / debt_tot for d in rows]
avgA = sum(serA)/5; gA = (serA[-1]/serA[0])**0.25 - 1
print("\nCASE A, all spending charged, debt credited (utility paragraph, literal):", [round(x) for x in serA], f"avg {avgA:,.0f}, CAGR {gA*100:.2f}%")
A_ng = ps(pv(avgA, 0, r)); A_g = ps(pv(avgA, gA, r))
print(f"  ends at the sovereign: no-growth {A_ng:.2f}, end-to-end growth {gA*100:.2f}% case {A_g:.2f}; range {min(A_ng,A_g):.2f} to {max(A_ng,A_g):.2f}")
gH = ((serA[3]+serA[4])/2 / ((serA[0]+serA[1])/2))**(1/3) - 1   # (b): halves of the window, 2021-22 against 2024-25
A_h = ps(pv(avgA, gH, r))
print(f"  growth between halves (2021-22 vs 2024-25) {gH*100:.2f}%: case {A_h:.2f}")
fA_ng = ps(pv(avgA, 0, FLOOR)); fA_g = ps(pv(avgA, gA, FLOOR)); fA_h = ps(pv(avgA, gH, FLOOR))
print(f"  at 10%: no-growth {fA_ng:.2f}, end-to-end growth {fA_g:.2f}, halves growth {fA_h:.2f}; fair (end-to-end pair) {(fA_ng+fA_g)/2:.2f}, (halves pair) {(fA_ng+fA_h)/2:.2f}")
# Case B, maintenance central (e): maintenance guessed at D&A, growth spending (net of debt credited up to allowed share) charged against the growth it buys
M = [d['maint'] for d in rows]; M0 = sum(M)/5; gM = (M[-1]/M[0])**0.25 - 1
sales_g = (rows[-1]['rev']/rows[0]['rev'])**0.25 - 1
share_hi = max(d['maint']/d['rev'] for d in rows)
# filings read: the ten years transcribed (2016-2025); highest maintenance-case share of sales over all ten
Y10 = range(2016, 2026)
sh10 = {y: (v('NetCashProvidedByUsedInOperatingActivities', y) - v('DepreciationDepletionAndAmortization', y)
            - v('PaymentsOfDividendsPreferredStockAndPreferenceStock', y) - v('PaymentsOfDividendsMinorityInterest', y)) / v('Revenues', y) for y in Y10}
print('maintenance-case owner cash as share of sales, 2016-2025:', {y: round(x*100, 1) for y, x in sh10.items()})
share_hi = max(share_hi, max(sh10.values()))
share_10 = M0*(1+gM)**10 / (rows[-1]['rev']*(1+sales_g)**10)
print(f"\nCASE B maint series {[round(x) for x in M]}, avg {M0:,.0f}, shown CAGR {gM*100:.2f}%; sales CAGR {sales_g*100:.2f}%; highest share of sales {share_hi*100:.1f}%; share in year 10 at shown rate on sales at sales growth {share_10*100:.1f}%")
g_use = sales_g if share_10 > share_hi else gM
G0 = (S('growth') - creditB - S('divest')) / 5   # (c): businesses sold net against the spending
G0_nodiv = (S('growth') - creditB) / 5
print(f"  growth carried {g_use*100:.2f}% (cap (f) {'applied' if g_use==sales_g else 'not needed'}); equity-funded growth spending avg {G0:,.0f}")
B_ng = pv(M0, 0, r); B_g = pv(M0, g_use, r, G0)
lo, hi = sorted([ps(B_ng), ps(B_g)])
print(f"  no-growth {ps(B_ng):.2f}; growth case {ps(B_g):.2f}; range {lo:.2f} to {hi:.2f}; width {hi/lo:.2f}x; price {price}")
f_ng = ps(pv(M0, 0, FLOOR)); f_g = ps(pv(M0, g_use, FLOOR, G0))
print(f"  at 10%: no-growth {f_ng:.2f}, growth {f_g:.2f}; FAIR (equity-only, central) {(f_ng+f_g)/2:.2f}")
print(f"  yield at price, no-growth case: {M0/mcap*100:.2f}%")
# return at price of growth case: solve rate
def solve(c0, g, gc):
    lo_, hi_ = 0.001, 0.5
    for _ in range(100):
        mid = (lo_+hi_)/2
        if pv(c0, g, mid, gc) > mcap: lo_ = mid
        else: hi_ = mid
    return mid
print(f"  beside, divestiture proceeds not netted: growth case {ps(pv(M0, g_use, r, G0_nodiv)):.2f}; fair {(f_ng + ps(pv(M0, g_use, FLOOR, G0_nodiv)))/2:.2f}")
print(f"  return implied at price: no-growth {M0/mcap*100:.2f}%, growth case {solve(M0, g_use, G0)*100:.2f}%")
# all-equity beside (maintenance case): add back pref dividends and after-tax interest; deduct pro forma net debt and prefs
AE = [d['maint'] + d['pref'] + d['intpaid']*(1-d['tax']) for d in rows]; AE0 = sum(AE)/5; gAE = (AE[-1]/AE[0])**0.25-1
share10ae = AE0*(1+gAE)**10/(rows[-1]['rev']*(1+sales_g)**10); shhi = max(a/d['rev'] for a, d in zip(AE, rows))
gae_use = sales_g if share10ae > shhi else gAE
G0ae = (S('growth') - S('divest'))/5   # all-equity: no debt credit; businesses sold netted
nd = net_debt_pf + prefs
print(f"\nALL-EQUITY beside: series {[round(x) for x in AE]}, avg {AE0:,.0f}, CAGR {gAE*100:.2f}% carried {gae_use*100:.2f}%; growth spend {G0ae:,.0f}; net debt+prefs {nd:,.0f}")
a_ng = ps(pv(AE0, 0, r), nd); a_g = ps(pv(AE0, gae_use, r, G0ae), nd)
print(f"  range {min(a_ng,a_g):.2f} to {max(a_ng,a_g):.2f}")
fa = (ps(pv(AE0, 0, FLOOR), nd) + ps(pv(AE0, gae_use, FLOOR, G0ae), nd))/2
print(f"  fair at 10%: no-growth {ps(pv(AE0,0,FLOOR),nd):.2f}, growth {ps(pv(AE0,gae_use,FLOOR,G0ae),nd):.2f}; FAIR all-equity {fa:.2f}")
print(f"\nshares {shares:.2f}M; market cap {mcap:,.0f}")
# literal window shown beside: depreciation variant without the debt credit is case B no-growth; all spending no credit:
nc = [d['allsp'] for d in rows]; print('divestiture proceeds by year:', [round(d['divest']) for d in rows]); print(f"all spending, no debt credit: {[round(x) for x in nc]}, avg {sum(nc)/5:,.0f} (negative: no value on this basis)")
# bounds for the floor test (written 2026-10-23 on resume)
nospend = [d['ocf'] - d['pref'] - d['nci'] for d in rows]; N0 = sum(nospend)/5
print(f"\nBOUND: operating cash after preference and minority dividends, no capital spending charged at all: avg {N0:,.0f}; at 10% no growth {ps(N0/FLOOR):.2f} a share; yield at price {N0/mcap*100:.2f}%")
print(f"case A yield at price, no growth: {avgA/mcap*100:.2f}%")
ev = mcap + nd
print(f"all-equity: EV {ev:,.0f}; maintenance case yield on EV {AE0/ev*100:.2f}%")
print(f"DRIP issue prices against the central range bottom {lo:.2f}: 2024 {481/8.7:.2f}, 2025 {523/8.0:.2f}, Jul-Sep 2026 {331/4.365256:.2f}")
