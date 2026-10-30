CAP=187.23*36.432564; SH=36.432564; SOV=0.0556
W={'5y FY2021-25':(73.2,72.4),'3y FY2023-25':(137.4,140.8),'10y FY2016-25':(55.2,50.8),'25y FY2001-25':(26.9,30.3),'TTM to 2026-06-30':(238.7,242.4)}
print('cap',round(CAP,1))
for k,(a,b) in W.items():
    lo,hi=min(a,b),max(a,b)
    print(f'{k}: OE {lo}-{hi}; yield {lo/CAP*100:.2f}-{hi/CAP*100:.2f}%; vs sov {lo/CAP*100-5.56:+.2f} to {hi/CAP*100-5.56:+.2f} pts; per share at 10% floor no growth ${lo/0.10/SH:.1f}-{hi/0.10/SH:.1f}; at sovereign ${lo/SOV/SH:.1f}-{hi/SOV/SH:.1f}; perpetual growth needed for 10% {(0.10*CAP-hi)/(CAP+hi)*100:.2f}-{(0.10*CAP-lo)/(CAP+lo)*100:.2f}%')
print('net cash less customer advances $M', 633.561-466.362, 'per share', round((633.561-466.362)/SH,2))
print('screen: yield_bottom 72/6272', round(72/6272*100,3), ' growth_required 10-1.15', round(10-72/6272*100,2), ' vs_sov', round(72/6272*100-5.35,2), ' spread (140.8-72.4)/72.4', round((140.8-72.4)/72.4,3))
