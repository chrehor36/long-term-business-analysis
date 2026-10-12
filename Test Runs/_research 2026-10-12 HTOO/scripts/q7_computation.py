"""HTOO: COMPUTATION, NOT A CLEARANCE. Owner cash and the reporting figures, EUR thousands.
Inputs are the filed cash-flow statements (20-F FY2021 0001171843-22-003035, FY2022 0001171843-23-003359,
FY2023 0001171843-24-002345, FY2025 20-F/A 0001493152-26-045996 for 2025 and 2024)."""
# year: (OCF, PPE, development, intangibles_other, IP_payment, lease_principal, SBC_expense, interest_paid, acquisitions)
cf = {
 2021: (-14656, -16615, -1630, -19, -500, -470, 0,     0,    0),   # SBC was a credit of 841: not added back as a gain
 2022: (-29851, -8588,  -1771, -80, -250, -1314, -3509, -62,  0),
 2023: (-9182,  -8589,  -629,  -109, 0,   -1291, -1393, -549, 0),
 2024: (-8280,  -11,    -142,  -37,  0,   -752,  -2189, -314, 0),
 2025: (-8226,  -322,   0,     0,    0,   -184,  -1562, -172, -852),  # -852 payments to subsidiaries' shareholders
}
oc, oc_acq, oc_unlev = {}, {}, {}
for y, (ocf, ppe, dev, intg, ip, lease, sbc, intr, acq) in cf.items():
    oc[y] = ocf + ppe + dev + intg + ip + lease + sbc           # equity-only: after interest (interest is inside OCF)
    oc_acq[y] = oc[y] + acq                                      # acquisitions deducted
    oc_unlev[y] = oc_acq[y] - intr                               # all-equity: interest paid added back
for y in cf: print(y, 'owner cash', oc[y], ' with acquisitions', oc_acq[y], ' before interest', oc_unlev[y])
avg = lambda d: sum(d.values()) / len(d)
A_eq, A_all = avg(oc_acq), avg(oc_unlev)
print('five-year average, equity-only (acq deducted):', round(A_eq), ' all-equity:', round(A_all))
sov, r10 = 0.056, 0.10
shares = 7_516_259           # 424B3 2026-09-23, 0001493152-26-043811, as of 2026-09-10
eurusd = 1.1181              # ECB reference rate 2026-10-12
net_debt = 1757 + 281 - 575  # loans and borrowings + non-current lease liability - cash, 2025-12-31 restated
for label, A in (('all-equity', A_all), ('equity-only', A_eq)):
    v_sov = A / sov; v_10 = A / r10   # no-growth case: constant cash, perpetual (ten years flat then zero growth = flat)
    if label == 'all-equity':
        v_sov -= net_debt; v_10 -= net_debt
    print(label, 'no-growth value at 5.60%: EUR k', round(v_sov), ' per share USD', round(v_sov*1000/shares*eurusd, 2))
    print(label, 'fair price (both ends at 10%): EUR k', round(v_10), ' per share USD', round(v_10*1000/shares*eurusd, 2))
# FY2025 alone, the only year of the present business (beside, not central)
y25 = oc_unlev[2025]
print('FY2025 alone all-equity no-growth at 5.60% per share USD', round((y25/sov - net_debt)*1000/shares*eurusd, 2))
print('market cap USD m at 1.91:', round(shares*1.91/1e6, 2))
