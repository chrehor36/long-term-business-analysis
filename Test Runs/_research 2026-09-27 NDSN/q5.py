# Q5 arithmetic. Inputs from oe_out.txt (owner earnings, $M), Step 0 (cap, shares), q2 organic series.
CAP=18145.182; SH=55.699366; SOV=5.49
OE={'5y dep':515.3,'5y capex':523.0,'3y dep':557.8,'3y capex':566.3,'TTM dep':681.2,'TTM capex':700.8}
G={'g=0':0.0,'g=2.6% (organic FY2016-FY2025)':0.026,'g=3.5% (organic FY2003-FY2025)':0.035,'g=3.8% (organic FY2003-FY2025 plus share decline FY2016-FY2025)':0.038,'g=5% (E4-44 ceiling)':0.05}
for k,v in OE.items():
    y=100*v/CAP
    print('%-10s OE %6.1f  yield %.2f%%  vs sovereign %+.2f pts  growth needed for 10%%: %.2f%%  at bond rate: %.2f%%'%(k,v,y,y-SOV,10-y,SOV-y))
    for gk,g in G.items():
        print('      %-62s expectancy %.2f%%  value at 10%% floor $%.0f/share'%(gk,y+100*g,v/(0.10-g)/SH))
print('floor band  $%.2f (5y dep end, g=2.6%%)'%(515.3/(0.10-0.026)/SH))
print('rerun band  $%.2f (TTM capex end, g=3.8%%)'%(700.8/(0.10-0.038)/SH))
