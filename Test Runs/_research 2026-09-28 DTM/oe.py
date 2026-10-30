# Owner earnings beneath the close. COMPUTATION - NOT A CLEARANCE.
# OE = operating cash flow (filed) - stock compensation (filed) - (c)
# (c) low end = D&A less acquired-intangible amortization (tagged AmortizationOfIntangibleAssets)
# (c) high end = total plant and equipment expenditures (filed; includes growth)
OCF ={2019:390,2020:597,2021:572,2022:725,2023:798,2024:763,2025:867}
SBC ={2019:6,2020:6,2021:12,2022:17,2023:20,2024:23,2025:26}
DA  ={2019:93,2020:152,2021:166,2022:170,2023:182,2024:209,2025:258}
AMI ={2019:24,2020:55,2021:58,2022:57,2023:57,2024:57,2025:60}
CAPX={2019:211,2020:518,2021:140,2022:338,2023:772,2024:350,2025:426}
MGMT_MAINT={2021:34,2022:22,2023:29,2024:30,2025:62}
PREPAY={2023:97,2024:23,2025:26}  # contract liabilities change in OCF
CAP=122.28*102015296/1e6
BOND=5.49
print(f'cap ${CAP:,.1f}M  bond {BOND}%')
print('year  OCF  SBC  DAexAm  capex  OE_hi(DA)  OE_lo(capex)  OE_mgmt')
for y in sorted(OCF):
    hi=OCF[y]-SBC[y]-(DA[y]-AMI[y]); lo=OCF[y]-SBC[y]-CAPX[y]
    mg=OCF[y]-SBC[y]-MGMT_MAINT[y] if y in MGMT_MAINT else None
    print(y,OCF[y],SBC[y],DA[y]-AMI[y],CAPX[y],hi,lo,mg, f'SBC/OCF {100*SBC[y]/OCF[y]:.1f}%')
print('\nwindows ending 2025 (mean of each end), yield on cap')
ys=sorted(OCF)
res=[]
for n in range(1,8):
    w=ys[-n:]
    hi=sum(OCF[y]-SBC[y]-(DA[y]-AMI[y]) for y in w)/n
    lo=sum(OCF[y]-SBC[y]-CAPX[y] for y in w)/n
    res.append((n,w[0],lo,hi))
    print(f'{n}y {w[0]}-2025: ${lo:,.0f}M to ${hi:,.0f}M  = {100*lo/CAP:.2f}% to {100*hi/CAP:.2f}%')
# TTM to 2026-06-30
ocf=867-432+502; sbc=26-12+12; capx=426-152+183; da=258-126+137; ami=60
print(f'TTM to 2026-06-30: OCF {ocf} SBC {sbc} capex {capx} D&A {da} (amort ~{ami}, annual 2025 figure, flagged)')
print(f'  OE ${ocf-sbc-capx}M to ${ocf-sbc-(da-ami)}M = {100*(ocf-sbc-capx)/CAP:.2f}% to {100*(ocf-sbc-(da-ami))/CAP:.2f}%')
# prepayment-normalized five-year
w=ys[-5:]
adj=sum(PREPAY.get(y,0) for y in w)/5
print(f'five-year less customer prepayments ({adj:.0f}/yr): shifts both ends by -{adj:.0f}')
allv=[r[2] for r in res]+[r[3] for r in res]+[ocf-sbc-capx, ocf-sbc-(da-ami)]
print(f'every window and TTM: ${min(allv):,.0f}M to ${max(allv):,.0f}M = {100*min(allv)/CAP:.2f}% to {100*max(allv)/CAP:.2f}%')
