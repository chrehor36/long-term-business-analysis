import json
exec(open('bs.py').read().split("tags_i=")[0])
U=inst('LiabilityForClaimsAndClaimsAdjustmentExpense'); R=inst('ReinsuranceRecoverablesOnUnpaidLossesGross'); UE=inst('UnearnedPremiums'); P=inst('PrepaidReinsurancePremiums'); PR=inst('PremiumsReceivableAtCarryingValue'); D=inst('DeferredPolicyAcquisitionCosts'); E=inst('StockholdersEquity')
ay={k:v*1e6 for k,v in {2016:2063,2017:650,2018:927,2019:1623,2020:2998,2021:3257,2022:3626,2023:5075,2024:5169,2025:5395}.items()}
fa={};fc={}
for y in range(2015,2026):
    if y in R: fa[y]=(U[y]-R[y])+(UE[y]-P[y]); fc[y]=fa[y]-PR[y]-D[y]
for y in range(2016,2026):
    af=(fc[y]+fc.get(y-1,fc[y]))/2
    print(y, f"float A2 {fa[y]/1e6:,.0f}  float C1-ded {fc[y]/1e6:,.0f}  float/equity {fa[y]/E[y]:.2f}  AY UW {ay[y]/1e6:,.0f}  cost of float {-ay[y]/af:+.1%}")
for h,(a,b) in {'AY2016-2020':(2016,2020),'AY2021-2025':(2021,2025)}.items():
    uw=sum(ay[y] for y in range(a,b+1)); fl=sum(fc[y] for y in range(a,b+1))
    print(h, f"cost of float {-uw/fl:+.2%}")
