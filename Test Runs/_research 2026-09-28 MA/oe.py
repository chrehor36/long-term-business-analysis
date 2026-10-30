# owner earnings by year, $M, from the filed faces (latest-filed vintage of OCF); SBC = expense in full
Y   =[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
OCF =[2684,2948,4135,3407,4101,4637,5664,6223,8183,7224,9463,11195,11980,14780,17648]
SBC =[79,88,121,111,122,148,176,196,250,254,273,295,460,526,597]
PPE =[77,96,155,175,177,215,300,330,422,339,407,442,371,474,489]
SW  =[100,122,144,159,165,167,123,174,306,369,407,655,717,720,726]
DA  =[194,230,258,321,366,373,436,459,522,580,726,750,799,897,1143]
REV =[6714,7391,8346,9473,9667,10776,12497,14950,16883,15301,18884,22237,25098,28167,32791]
ACQ =[460,70,0,525,584,0,1175,0,1440,989,4436,313,0,2511,0]
LIT =[770,20,95,0,61,117,15,1128,0,73,94,356,539,680,504]
LITPAY=[303,65,0,28,124,101,47,260,668,149,98,114,929,496,647]
cap=497801.4; sov=5.49
oe_c={}; oe_d={}
print('FY | OCF | SBC | PPE+SW | DA | OE capex | OE DA | OE/rev')
for i,y in enumerate(Y):
    c=OCF[i]-SBC[i]-PPE[i]-SW[i]; d=OCF[i]-SBC[i]-DA[i]
    oe_c[y]=c; oe_d[y]=d
    print(y, OCF[i], SBC[i], PPE[i]+SW[i], DA[i], c, d, f"{c/REV[i]*100:.1f}%")
# TTM to 2026-06-30
ocf=17648+6772-6983; sbc=597+326-308; ppe=489+445-199; sw=726+368-367; da=1143+608-556
tc=ocf-sbc-ppe-sw; td=ocf-sbc-da
print('TTM', ocf, sbc, ppe+sw, da, tc, td)
def mean(d,a,b): v=[d[y] for y in range(a,b+1)]; return sum(v)/len(v)
print('\nwindow | capex end | yield | DA end | yield')
for n in (1,3,5,7,10,15):
    a=2025-n+1
    mc=mean(oe_c,a,2025); md=mean(oe_d,a,2025)
    print(f"{n}y FY{a}-25 | {mc:,.0f} | {mc/cap*100:.2f}% | {md:,.0f} | {md/cap*100:.2f}%")
print(f"TTM | {tc:,.0f} | {tc/cap*100:.2f}% | {td:,.0f} | {td/cap*100:.2f}%")
print('\nrolling 5y capex end:')
for b in range(2015,2026):
    print(b-4,b, round(mean(oe_c,b-4,b)))
import math
def cagr(a,b,n): return (b/a)**(1/n)-1
print('\nOE capex-end CAGR FY2016-25', f"{cagr(oe_c[2016],oe_c[2025],9)*100:.1f}%", 'FY2020-25', f"{cagr(oe_c[2020],oe_c[2025],5)*100:.1f}%", 'FY2019-25', f"{cagr(oe_c[2019],oe_c[2025],6)*100:.1f}%", 'FY2011-25', f"{cagr(oe_c[2011],oe_c[2025],14)*100:.1f}%")
print('rev CAGR FY2016-25', f"{cagr(REV[5],REV[14],9)*100:.1f}%", 'FY2019-25', f"{cagr(REV[8],REV[14],6)*100:.1f}%",'FY2011-25', f"{cagr(REV[0],REV[14],14)*100:.1f}%")
print('sum OE FY2016-25 capex end', sum(oe_c[y] for y in range(2016,2026)), 'acq', sum(ACQ[5:]))
print('best-year share: FY2025 of 5y sum', f"{oe_c[2025]/sum(oe_c[y] for y in range(2021,2026))*100:.1f}%")
print('SBC/OCF FY2025', f"{597/17648*100:.1f}%", 'FY2016-25 sum', f"{sum(SBC[5:])/sum(OCF[5:])*100:.1f}%")
print('lit provisions FY2016-25', sum(LIT[5:]), 'paid', sum(LITPAY[5:]))
