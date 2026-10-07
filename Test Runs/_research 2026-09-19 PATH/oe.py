# Owner earnings from the FILED FACES ($M). Sources: FY2026 10-K (FY24-26), FY2024 10-K (FY22-23), FY2022 10-K (FY22 cap. software), Q2 FY2027 10-Q (H1s).
# Grant-date value = RSUs granted x weighted grant-date FV + options granted x weighted FV + PSUs granted x FV (equity-award notes).
Y = ["FY2022","FY2023","FY2024","FY2025","FY2026"]
ocf   = [-54.963, -9.981, 299.082, 320.565, 371.208]
sbc   = [515.583, 369.840, 371.955, 358.151, 290.676]
capex = [8.879+2.950, 23.815, 7.342, 14.923, 19.048]   # PP&E + capitalised software (FY2022 only; none after)
da    = [14.705, 18.723, 22.597, 17.232, 16.969]
acq   = [19.7, 0.0, 0.0, 0.0, 24.821]                  # cash acquisitions (FY2022 per 10-K MD&A; FY2026 Peak)
grant = [19.695*45.09 + 2.041*45.78, 30.039*15.85 + 5.027*12.23, 19.274*16.95 + 2.995*16.84 + 0.1*18.08,
         17.704*17.50 + 2.738*18.00, 16.822*11.36 + 3.004*10.90 + 0.7*11.23]
rows = []
print(f"{'year':8}{'OCF':>9}{'SBC':>9}{'grant':>9}{'capex':>8}{'D&A':>7}{'OE capex':>10}{'OE D&A':>9}{'OE maxSBC':>10}{'SBC/OCF':>9}")
for i, y in enumerate(Y):
    oc = ocf[i]-sbc[i]-capex[i]; od = ocf[i]-sbc[i]-da[i]; om = ocf[i]-max(sbc[i],grant[i])-capex[i]
    rows.append((oc, od, om))
    print(f"{y:8}{ocf[i]:9.1f}{sbc[i]:9.1f}{grant[i]:9.1f}{capex[i]:8.1f}{da[i]:7.1f}{oc:10.1f}{od:9.1f}{om:10.1f}{(sbc[i]/ocf[i]*100 if ocf[i]>0 else float('nan')):9.1f}")
def mean(L): return sum(L)/len(L)
for lab, sl in [("5y FY2022-26", slice(0,5)), ("3y FY2024-26", slice(2,5))]:
    r = rows[sl]
    print(lab, "capex end %.1f  D&A end %.1f  charge-or-grant max %.1f  with cash acquisitions (capex end) %.1f" % (
        mean([x[0] for x in r]), mean([x[1] for x in r]), mean([x[2] for x in r]), mean([x[0] for x in r]) - mean(acq[sl])))
print("5y SBC / 5y OCF = %.1f%%" % (sum(sbc)/sum(ocf)*100), " 3y = %.1f%%" % (sum(sbc[2:])/sum(ocf[2:])*100))
# TTM to 2026-07-31
tocf = 371.208 + 162.627 - 160.589; tsbc = 290.676 + 98.272 - 154.367; tcap = 19.048 + 4.073 - 12.832; tda = 16.969 + 16.514 - 7.483
h1grant = 9.803*11.89 + 1.893*12.09 + 0.8*11.02
print("TTM OCF %.1f SBC %.1f capex %.1f D&A %.1f -> OE capex %.1f, D&A %.1f; H1 FY2027 grant value %.1f (x2 = %.1f) -> OE at grant run-rate %.1f" % (
    tocf, tsbc, tcap, tda, tocf-tsbc-tcap, tocf-tsbc-tda, h1grant, 2*h1grant, tocf-2*h1grant-tcap))
cap = 13.39*521155409/1e6
print("cap $M %.1f ; cash+securities 1405 ; EV %.1f" % (cap, cap-1405))
for v in [mean([x[2] for x in rows]), mean([x[0] for x in rows]), mean([x[0] for x in rows[2:]]), tocf-tsbc-tcap, tocf-tsbc-tda]:
    print("  OE %.1f -> yield on cap %.2f%%, on EV %.2f%%" % (v, v/cap*100, v/(cap-1405)*100))
print("OE needed for 10%% on cap: %.0f ; on EV: %.0f ; for 5.34%% on cap: %.0f" % (0.10*cap, 0.10*(cap-1405), 0.0534*cap))
