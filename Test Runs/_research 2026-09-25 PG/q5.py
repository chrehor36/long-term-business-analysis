"""Q5 arithmetic. OE bands from oe.py; as-converted shares 2,391.1M; price $145.68 (2026-09-24 close); USD 30Y 5.47% (09/24/2026)."""
S=2391.1; P=145.68; CAP=S*P; SOV=5.47
lo,hi=14087,14746   # 5y default window, capex end / D&A end ($M)
adj_hi=15171        # D&A end with one-off taxes added back
print(f"cap {CAP:,.0f}M; yield {lo/CAP*100:.2f}-{hi/CAP*100:.2f}%; vs sovereign {lo/CAP*100-SOV:+.2f} to {hi/CAP*100-SOV:+.2f} pts")
print(f"growth to reach the bond (Gordon): {SOV-hi/CAP*100:.2f}-{SOV-lo/CAP*100:.2f}%; to reach 10% floor: {10-hi/CAP*100:.2f}-{10-lo/CAP*100:.2f}%")
for g in (0.0,0.030,0.0425):
    print(f"expectancy at g={g*100:.2f}%: {lo/CAP*100+g*100:.2f}-{hi/CAP*100+g*100:.2f}%")
    print(f"   value at 10% floor: ${lo/(0.10-g)/S:,.2f} - ${hi/(0.10-g)/S:,.2f} per share; most generous (adj D&A) ${adj_hi/(0.10-g)/S:,.2f}")
# OE growth record
m1217=(8943+10519+9750+10535+11786)/5; m2226=14087; m1721=11994
print(f"5y mean FY12-16 capex end {m1217:,.0f}; FY22-26 {m2226:,}; 10y CAGR {(m2226/m1217)**(1/10)*100-100:.2f}%; 5y CAGR vs FY17-21 {(m2226/m1721)**(1/5)*100-100:.2f}%")
print(f"diluted shares FY2024 2471.9 -> FY2026 2422.5: {(2422.5/2471.9)**0.5*100-100:.2f}%/yr")
