# COMPUTATION, NOT A CLEARANCE. SCWO owner cash and the Q7 arithmetic after the Q1 stop.
# Inputs transcribed from the filed cash-flow statements (accessions in the run file).
rows = {  # year: (OCF, SBC, stock issued for services, capex, intangibles)
 2021: (-1840950, 204217, 0, 1190, 0),        # stock for services 2021 not tagged; read as 0, said so
 2022: (-4948996, 610741, 0, 144567, 0),      # stock for services 2022 not tagged; read as 0, said so
 2023: (-9034987, 925181, 71200, 105990, 0),
 2024: (-10589735, 1215624, 383879, 554942, 98602),
 2025: (-14326205, 3546646, 290872, 1898212, 0),
}
oc = {y: o - s - sv - c - i for y, (o, s, sv, c, i) in rows.items()}
for y in oc: print(y, f"{oc[y]:,.0f}")
avg = sum(oc.values()) / 5
print("five-year average owner cash", f"{avg:,.0f}")
h1 = (oc[2021] + oc[2022]) / 2; h2 = (oc[2024] + oc[2025]) / 2
print("halves", f"{h1:,.0f}", f"{h2:,.0f}", "(both negative: growth meaningless, specific (b))")
sov = 0.0537
shares = 17_718_161
price = 2.53
net_debt = 2_960_000 + 60_000 + 8_725 + 30_400 + 10_159 - 1_776_259  # 6/30/2026 + July note
print("net debt", f"{net_debt:,.0f}")
ng_ev = avg / sov
print("no-growth whole business at sovereign", f"{ng_ev:,.0f}", "per share", f"{(ng_ev - net_debt)/shares:,.2f}")
fair_ev = avg / 0.10
print("fair (no-growth case at 10%)", f"{fair_ev:,.0f}", "per share all-equity", f"{(fair_ev - net_debt)/shares:,.2f}")
print("equity-only (owner cash after interest; interest in window nil)", f"{fair_ev/shares:,.2f}")
mcap = price * shares
print("market cap", f"{mcap:,.0f}", "EV", f"{mcap+net_debt:,.0f}")
