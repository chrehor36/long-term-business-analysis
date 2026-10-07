# Owner earnings from the FILED FACES ($M). Sources: FY2025 10-K (FY23-25 faces), FY2023 10-K (FY21-22 faces), FY2022 10-K,
# Q2 2026 10-Q (H1 2026 and H1 2025). Grant value = options granted x weighted grant-date FV + RSUs granted x weighted grant-date FV
# (equity-award notes of each 10-K). capSBC = "Stock-based compensation capitalized as internal use software costs" (supplemental).
Y     = ["FY2021","FY2022","FY2023","FY2024","FY2025"]
ocf   = [88.681, 87.212, 81.121, 73.425, 81.059]
sbc   = [14.107, 20.646, 28.862, 37.676, 38.378]
capsbc= [0.903, 1.475, 2.462, 3.076, 3.474]
ppe   = [30.432, 35.869, 10.601, 17.592, 14.345]
sw    = [8.929, 13.024, 17.687, 20.936, 20.511]
da    = [23.073, 34.249, 44.770, 45.352, 43.769]
hwdep = [15.7, 23.6, 28.5, 24.8, 19.0]
acq   = [0.0, 28.085, 0.0, 0.0, 0.0]
wc    = [-67.405+68.301, -24.408+29.763, -75.716+79.687, -49.345+38.096, 66.574-42.397]   # AR + AP lines of the face
grant = [0.660466*20.30 + 0.582259*35.24, 0.450153*13.70 + 1.587930*25.01, 1.375*8.58 + 2.573*15.98,
         1.544*8.78 + 2.465*16.49, 0.986*8.83 + 2.047*14.39]
rows=[]
print(f"{'year':7}{'OCF':>8}{'SBC':>7}{'capSBC':>7}{'grant':>7}{'capex':>7}{'D&A':>7}{'AR+AP':>7}{'OEcapex':>9}{'OE D&A':>8}{'OEgrant':>9}{'OE exWC':>9}{'SBC/OCF':>8}")
for i,y in enumerate(Y):
    cx = ppe[i]+sw[i]
    oc = ocf[i]-sbc[i]-capsbc[i]-cx          # capex end: charge + capitalised SBC + cash capex
    od = ocf[i]-sbc[i]-da[i]                 # D&A end: D&A already carries amortised capitalised SBC
    og = ocf[i]-max(sbc[i]+capsbc[i], grant[i])-cx
    ox = oc - wc[i]
    rows.append((oc,od,og,ox))
    print(f"{y:7}{ocf[i]:8.1f}{sbc[i]:7.1f}{capsbc[i]:7.1f}{grant[i]:7.1f}{cx:7.1f}{da[i]:7.1f}{wc[i]:7.1f}{oc:9.1f}{od:8.1f}{og:9.1f}{ox:9.1f}{sbc[i]/ocf[i]*100:8.1f}")
m=lambda L: sum(L)/len(L)
for lab, sl in [("5y FY2021-25", slice(0,5)), ("3y FY2023-25", slice(2,5))]:
    r=rows[sl]
    print(lab, "capex end %.1f | D&A end %.1f | larger of charge/grant %.1f | capex end ex AR/AP swing %.1f | capex end with cash acquisitions %.1f" % (
        m([x[0] for x in r]), m([x[1] for x in r]), m([x[2] for x in r]), m([x[3] for x in r]), m([x[0] for x in r]) - m(acq[sl])))
print("5y SBC/OCF %.1f%%  3y %.1f%%" % (sum(sbc)/sum(ocf)*100, sum(sbc[2:])/sum(ocf[2:])*100))
print("5y capex (cash) %.1f vs D&A %.1f ; hardware capex vs hardware depreciation FY2023-25: %.1f vs %.1f" % (sum(ppe)+sum(sw), sum(da), sum(ppe[2:]), sum(hwdep[2:])))
# TTM to 2026-06-30 = FY2025 + H1 2026 - H1 2025
t_ocf = 81.059+37.505-30.526; t_sbc = 38.378+16.835-19.499; t_cs = 3.474+1.808-1.779
t_cx = 34.856 + (2.966+10.171) - (2.781+11.180); t_da = 43.769+19.995-23.537
t_wc = (66.574-42.397) + (-24.957+36.558) - (41.412-25.865)
oc = t_ocf-t_sbc-t_cs-t_cx; od = t_ocf-t_sbc-t_da
print("TTM to 2026-06-30: OCF %.1f SBC %.1f capSBC %.1f capex %.1f D&A %.1f AR+AP %.1f -> OE capex end %.1f, D&A end %.1f, capex end ex swing %.1f" % (t_ocf,t_sbc,t_cs,t_cx,t_da,t_wc,oc,od,oc-t_wc))
h1grant_rsu = 3.448*6.64
print("H1 2026 RSU grant value %.1f (options 485K granted at a $6.29 weighted exercise price; FV not in the 10-Q)" % h1grant_rsu)
print("TTM OE at H1 2026 RSU grant run-rate (x2) instead of charge: %.1f" % (t_ocf - 2*h1grant_rsu - t_cx))
cap = 17.55*45550061/1e6; cash = 137.507
print("cap $M %.1f ; cash+securities %.1f ; EV %.1f" % (cap, cash, cap-cash))
for lab,v in [("5y larger measure", m([x[2] for x in rows])),("5y capex end", m([x[0] for x in rows])),("5y D&A end", m([x[1] for x in rows])),("3y capex end", m([x[0] for x in rows[2:]])),("3y D&A end", m([x[1] for x in rows[2:]])),("TTM capex end", oc),("TTM D&A end", od)]:
    print("  %-20s OE %6.1f -> yield on cap %5.2f%%, on EV %5.2f%%" % (lab, v, v/cap*100, v/(cap-cash)*100))
print("OE needed for 10%% on cap: %.0f ; on EV: %.0f ; for 5.34%% on cap: %.0f" % (0.10*cap, 0.10*(cap-cash), 0.0534*cap))
