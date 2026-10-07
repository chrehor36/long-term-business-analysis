# Owner earnings [E2-23] from the filed continuing-operations cash-flow statements (thousands), newest vintage per year.
# OE = OCF(continuing) - SBC - (c); (c) at two ends: capex (all "Capital expenditures") and depreciation only
# (the [E3-44] default; amortization of bought intangibles is not maintenance, shown in the D&A column for reference).
# Sources: FY2017-FY2018 10-K FY2019 (0000006955-19-000033); FY2019-FY2020 10-K FY2021; FY2021 10-K FY2023; FY2022 10-K FY2024;
# FY2023-FY2025 10-K FY2025 (0000006955-25-000030); nine-month columns from the 10-Qs of 2025-07 and 2026-07-09.
S={
2017:dict(ocf=48092,sbc=14939,capex=17238,da=22925,dep=13800,acq=0,div=0),
2018:dict(ocf=71916,sbc=11333,capex=11021,da=20405,dep=11100,acq=23218+27718,div=8902),
2019:dict(ocf=40903,sbc=10882,capex=14923,da=20217,dep=11300,acq=0,div=0),
2020:dict(ocf=17999,sbc=9624,capex=12053,da=20720,dep=12400,acq=33300,div=221000),
2021:dict(ocf=54860,sbc=9215,capex=12019,da=21611,dep=13400,acq=0,div=0),
2022:dict(ocf=52246,sbc=13619,capex=8417,da=19600,dep=12300,acq=0,div=0),
2023:dict(ocf=78573,sbc=8574,capex=9400,da=16313,dep=11200,acq=0,div=20057),
2024:dict(ocf=84016,sbc=10931,capex=11411,da=13275,dep=10000,acq=1402+1133,div=0),
2025:dict(ocf=111284,sbc=13016,capex=19340,da=15674,dep=10100,acq=26661,div=0),
}
import json
x=json.load(open('xb_rows.json'))
for y in S:
    if str(y) in x.get('Dep',{}): S[y]['dep']=x['Dep'][str(y)]/1000
TTM=dict(ocf=111284-56030+69263,sbc=13016-9525+9394,capex=19340-16360+9241,da=15674-10706+13133)
TTM['dep']=TTM['da']-(5576-0)  # placeholder; replaced below from 10-Q amortization
cap=1825614
print('FY    OCF     SBC   capex    D&A    dep   OE@capex  OE@dep   acq/(div)')
for y in sorted(S):
    s=S[y]; s['a']=s['ocf']-s['sbc']-s['capex']; s['b']=s['ocf']-s['sbc']-s['dep']
    print('%d %7.1f %6.1f %6.1f %6.1f %6.1f %8.1f %8.1f   %6.1f / %6.1f'%(y,s['ocf']/1e3,s['sbc']/1e3,s['capex']/1e3,s['da']/1e3,s['dep']/1e3,s['a']/1e3,s['b']/1e3,s['acq']/1e3,s['div']/1e3))
json.dump({str(y):S[y] for y in S},open('oe_rows.json','w'),indent=0)
ys=sorted(S)
print('\nWindows ending FY2025 (mean OE $M; yield on cap $%.1fM):'%(cap/1e3))
for n in range(1,len(ys)+1):
    w=ys[-n:]; ma=sum(S[y]['a'] for y in w)/n; mb=sum(S[y]['b'] for y in w)/n
    lo,hi=min(ma,mb),max(ma,mb)
    print('  %d-yr FY%d-FY2025: %6.1f to %6.1f   %5.2f%% to %5.2f%%'%(n,w[0],lo/1e3,hi/1e3,100*lo/cap,100*hi/cap))
t=TTM; print('\nTTM to 2026-05-31: OCF %.1f SBC %.1f capex %.1f D&A %.1f'%(t['ocf']/1e3,t['sbc']/1e3,t['capex']/1e3,t['da']/1e3))
print('TTM OE @capex %.1f'%((t['ocf']-t['sbc']-t['capex'])/1e3))
cum=lambda k: sum(S[y][k] for y in ys)
print('\nCumulative FY2017-FY2025: OCF %.1f SBC %.1f (%.1f%% of OCF) capex %.1f OE@capex %.1f OE@dep %.1f acq %.1f div %.1f'%(cum('ocf')/1e3,cum('sbc')/1e3,100*cum('sbc')/cum('ocf'),cum('capex')/1e3,cum('a')/1e3,cum('b')/1e3,cum('acq')/1e3,cum('div')/1e3))
