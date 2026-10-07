# COMPUTATION - NOT A CLEARANCE. HRMY 2026-10-06 run. USD millions.
ocf  = {2021:98.557,2022:144.466,2023:219.387,2024:219.821,2025:348.199}
sbc  = {2021:15.659,2022:26.173,2023:31.705,2024:42.602,2025:44.895}
capx = {2021:0.298,2022:0.172,2023:0.312,2024:1.153,2025:0.310}
# investing-section payments for licences, milestones and acquisitions (capital)
wakix_ms = {2021:100.0,2022:40.0,2023:0,2024:0,2025:0}          # WAKIX licence milestones (2017 LCA)
pipe     = {2021:0,2022:0,2023:36.967,2024:33.069+1.0+25.5,2025:19.25+15.0}
oc_all = {y: ocf[y]-sbc[y]-capx[y]-wakix_ms[y]-pipe[y] for y in ocf}
oc_ex  = {y: ocf[y]-sbc[y]-capx[y]-pipe[y] for y in ocf}
oc_da  = {y: ocf[y]-sbc[y]-{2021:18.84,2022:23.385,2023:24.359,2024:24.112,2025:25.335}[y]-pipe[y] for y in ocf}
for name,d in [('owner cash, all capital',oc_all),('owner cash, ex WAKIX milestones',oc_ex),('D&A variant (D&A in place of capex and WAKIX milestones)',oc_da)]:
    print(name, {y:round(v,1) for y,v in d.items()}, 'mean', round(sum(d.values())/5,1))
avg = sum(oc_all.values())/5
shares = 58.236393
price = 39.92
netcash = 549.769+118.022+294.668-20.0-133.961
print('net cash', round(netcash,1), 'per share', round(netcash/shares,2))
sov = 0.0566
t = 0.262   # filer's 2025 effective tax rate (10-K)
floor_after = 0.10*(1-t)
# timing: valuation date 2026-10-06; cash at mid-period; Q4 2026 = 0.25 yr
def pv(stream, r):
    return sum(cf/(1+r)**tm for tm,cf in stream)
def streams(base, g, tail1, tail2):
    s=[(0.125, 0.25*base*(1+g))]
    c=base*(1+g)
    for k,yr in enumerate([2027,2028,2029]):
        c=c*(1+g); s.append((0.25+k+0.5, c))
    last=c
    s.append((3.75, tail1*last)); s.append((4.75, tail2*last))
    return s
low  = streams(avg, 0.0, 0.30, 0.10)
high = streams(oc_all[2025], 0.15, 0.40, 0.15)
cent = [(a[0],(a[1]+b[1])/2) for a,b in zip(low,high)]
for nm,s in [('low',low),('high',high),('central',cent)]:
    print(nm,[ (round(tm,2),round(cf,1)) for tm,cf in s])
for nm,s in [('low',low),('high',high),('central',cent)]:
    v_sov=(pv(s,sov)+netcash)/shares; v_fl=(pv(s,floor_after)+netcash)/shares
    print(f'{nm}: value at sovereign {v_sov:.2f}/sh; at floor (10% pre-tax = {floor_after:.4f} after tax) {v_fl:.2f}/sh')
lo_v=(pv(low,sov)+netcash)/shares; hi_v=(pv(high,sov)+netcash)/shares
print('range width top/bottom', round(hi_v/lo_v,2))
fair=(pv(cent,floor_after)+netcash)/shares
cheap=(pv(low,floor_after)+netcash)/shares/1.5
print('FAIR', round(fair,2), 'CHEAP', round(cheap,2), 'PRICE', price)
# implied: what the price pays for beyond net cash
print('price less net cash per share', round(price-netcash/shares,2), 'EV $M', round(price*shares-netcash,1))
# IRR of central stream at price (pre-tax equivalent)
import math
def irr(s, P):
    lo,hi=-0.9,2.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(s,m)+netcash > P: lo=m
        else: hi=m
    return m
for nm,s in [('low',low),('central',cent),('high',high)]:
    r=irr(s, price*shares); print(nm,'after-tax IRR on price', round(r*100,2),'% ; pre-tax equiv', round(r/(1-t)*100,2),'%')
