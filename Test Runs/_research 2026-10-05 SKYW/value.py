# COMPUTATION - NOT A CLEARANCE. Q7-convention range for SKYW, arithmetic only.
SH=38.828325; P=96.06; R=0.0566
def pv(C,g,r,years=10):
    v=0;c=C
    for t in range(1,years+1):
        c=C*(1+g)**t; v+=c/(1+r)**t
    return v + (C*(1+g)**years)/r/(1+r)**years   # then zero nominal growth
rev21,rev25,rev16=2713.491,4058.202,3063.7
g5=(rev25/rev21)**(1/4)-1; g10=(rev25/rev16)**(1/9)-1
print('revenue growth 2021-25 %.2f%%, 2016-25 %.2f%%'%(g5*100,g10*100))
gcap=min(g5,R-0.0006)   # Q3 cap: no rate run past the discount rate
cases={'5yr capex basis':124.1,'5yr D&A basis':214.5,'10yr D&A basis (whole cycle)':216.0,'3yr 2023-25 capex basis':310.5}
for k,C in cases.items():
    lo=pv(C,0,R); hi5=pv(C,gcap,R); hi10=pv(C,g10,R)
    print(f'{k:32s} C={C:6.1f}  no-growth ${lo/SH:7.2f}  shown(5yr,capped {gcap*100:.2f}%) ${hi5/SH:7.2f}  shown(10yr {g10*100:.2f}%) ${hi10/SH:7.2f}  ratio5 {hi5/lo:.2f}')
# fair price: PV at 10% pre-tax of central case; pre-tax = owner cash + cash taxes (5yr mean 11.4)
cashtax=(6.6+1.2+13.6+18.6+16.9)/5
for k,C in (('5yr capex basis',124.1),('5yr D&A basis',214.5),('3yr capex basis',310.5)):
    Cp=C+cashtax
    gmid=gcap/2
    fair=pv(Cp,gmid,0.10); cheap=Cp/0.15
    print(f'{k:20s} pre-tax C={Cp:6.1f} fair(10%,g={gmid*100:.2f}% 10y) ${fair/SH:7.2f}  cheap(no growth,15%) ${cheap/SH:7.2f}')
print('market cap %.0f'%(SH*P), 'yield 5yr capex %.2f%% DA %.2f%%'%(124.1/(SH*P)*100,214.5/(SH*P)*100))
