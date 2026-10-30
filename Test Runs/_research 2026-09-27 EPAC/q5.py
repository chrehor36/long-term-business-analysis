cap=1825.614; sh=51.137646; px=35.70; bond=0.0549
OE={'five-year capex':53.0,'five-year dep':53.7,'three-year capex':67.1,'three-year dep':70.0,'TTM capex':99.4,'TTM dep':100.1}
core=[1.04,0.80,1.05,1.11,1.08,1.02,1.01]
import math
g_core=math.prod(core)**(1/len(core))-1
g_ind=(380.0/278.7)**(1/10)-1
print('core compound FY2019-FY2025 %.2f%%, Industrial sales FY2007-FY2017 %.2f%%'%(100*g_core,100*g_ind))
for k,v in OE.items():
    y=v/cap
    print('%-17s OE %6.1f yield %5.2f%%  exp@0 %5.2f%% @%.1f%% %5.2f%% @%.1f%% %5.2f%% @5%% %5.2f%%  g needed for 10%% %5.2f%%  g at bond %5.2f%%'%(k,v,100*y,100*y,100*g_core,100*(y+g_core),100*g_ind,100*(y+g_ind),100*(y+0.05),100*(0.10-y),100*(bond-y)))
def val(oe,g,r=0.10): return oe/(r-g)/sh
print('\nprice at which expectancy = 10%:')
for k in ('five-year capex','five-year dep','TTM capex','TTM dep'):
    print('  %-16s g0 $%5.2f  g=%.1f%% $%5.2f  g=%.1f%% $%5.2f  g=5%% $%5.2f'%(k,val(OE[k],0),100*g_core,val(OE[k],g_core),100*g_ind,val(OE[k],g_ind),val(OE[k],0.05)))
print('at bond no growth: five-year $%.2f-%.2f, TTM $%.2f-%.2f'%(val(53.0,0,bond),val(53.7,0,bond),val(99.4,0,bond),val(100.1,0,bond)))
# SFE sensitivity: adj EBITDA 44, interest on 451.4 at 5.3%, tax 23%, capex+D&A unknown -> upper bound
inc=(44-0.053*451.4)*(1-0.23)
print('SFE upper-bound after-interest, after-tax, before capex and SBC: %.1f; TTM+SFE yield %.2f%%'%(inc,100*(100.1+inc)/cap))
