# BAM figures for the competitor row, on the peer row's spec:
# rate bps = FY2025 fees / avg(YE2024, YE2025) fee-earning capital
fbc = {2023:456998.0, 2024:538541.0, 2025:602714.0}   # 10-K FY2025, Total Fee-Bearing Capital ($M)
avg = (fbc[2024]+fbc[2025])/2
print('avg FBC 24/25 $M', round(avg,1))
print('100%-basis base mgmt fees 4896 -> bps', round(4896/avg*10000,1))
print('100%-basis base+transaction 4896+30 -> bps', round(4926/avg*10000,1))
print('GAAP base mgmt & advisory 3384 -> bps', round(3384/avg*10000,1))
print('Fee Revenues 5487 -> bps', round(5487/avg*10000,1))
print('FBC CAGR 23-25', round(((fbc[2025]/fbc[2023])**0.5-1)*100,1),'%')
# fee rate by year, as in Q1
fbc22=417858.0  # check
for y,f in [(2023,3956),(2024,4233),(2025,4896)]:
    a=(fbc[y-1] if y-1 in fbc else fbc22); print(y, 'rate bps', round(f/((a+fbc[y])/2)*10000,1))
# H1 2026 annualised
print('H1-26 ann bps', round(2*2625/((602714+672159)/2)*10000,1))
print('FRE margin: 2995/5487', round(2995/5487*100,1), ' pre-attribution 3077/5487', round(3077/5487*100,1))
print('perp share 2026-06', round(293484/672159*100,1), ' YE2025', round(240512/602714*100,1))
