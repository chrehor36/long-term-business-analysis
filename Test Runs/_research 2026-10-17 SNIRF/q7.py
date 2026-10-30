# Q7 COMPUTATION for SNIRF (Senior plc). All figures GBP m from the annual reports (see notes.md).
yrs=list(range(2016,2026))
ncfo={2016:100.3,2017:110.9,2018:100.7,2019:115.9,2020:48.9,2021:27.0,2022:57.7,2023:41.4,2024:49.4,2025:56.9}
intrec={2016:0.2,2017:0.4,2018:0.4,2019:0.2,2020:0.2,2021:0.1,2022:0.7,2023:4.3,2024:6.6,2025:6.5}
disp={2016:0.8,2017:1.8,2018:0.5,2019:0.7,2020:0.5,2021:0.2,2022:0.5,2023:0.7,2024:0.1,2025:0.3}
ppe={2016:50.7,2017:52.3,2018:54.6,2019:63.0,2020:25.2,2021:20.2,2022:28.7,2023:33.7,2024:41.5,2025:32.0}
intang={2016:2.1,2017:2.5,2018:1.7,2019:1.8,2020:1.6,2021:1.1,2022:1.8,2023:2.2,2024:1.7,2025:0.6}
lease={2016:0.8,2017:0.5,2018:0.3,2019:7.8,2020:7.9,2021:8.4,2022:9.1,2023:10.2,2024:10.0,2025:6.4}
sbc={2016:2.2,2017:1.9,2018:3.4,2019:1.8,2020:3.0,2021:3.5,2022:4.3,2023:4.1,2024:4.5,2025:4.7}
intpaid={2016:10.2,2017:10.0,2018:9.3,2019:11.2,2020:10.8,2021:8.1,2022:9.7,2023:17.2,2024:21.2,2025:20.6}
leaseint={2016:0,2017:0,2018:0,2019:3.5,2020:3.0,2021:2.6,2022:2.5,2023:2.9,2024:1.8,2025:2.2}
T=0.25
eq={};ae={}
for y in yrs:
    eq[y]=ncfo[y]+intrec[y]+disp[y]-ppe[y]-intang[y]-lease[y]-sbc[y]
    ae[y]=eq[y]+(intpaid[y]-leaseint[y]-intrec[y])*(1-T)
    print(y,'equity-basis %.1f'%eq[y],' all-equity %.1f'%ae[y])
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
W=range(2021,2026); C=yrs; H1=range(2016,2021)
for name,d in (('all-equity',ae),('equity-only',eq)):
    print(name,'window 2021-25 avg %.1f'%avg(d,W),' cycle 2016-25 avg %.1f'%avg(d,C),' 2016-20 avg %.1f'%avg(d,H1), ' 2025 %.1f'%d[2025])
r=0.0572; shares=412.086; nd=89.4; price=297.5
def pv(base,g,rate,yrs10=10):
    v=0;c=base
    for t in range(1,yrs10+1):
        c=c*(1+g); v+=c/(1+rate)**t
    v+= c/rate/(1+rate)**yrs10   # zero nominal growth after year ten
    return v
g_dec=(avg(ae,W)/avg(ae,H1))**(1/5)-1
g_dec_eq=(avg(eq,W)/avg(eq,H1))**(1/5)-1
print('decline rate halves all-equity %.1f%%  equity-only %.1f%%'%(g_dec*100,g_dec_eq*100))
for label,base in (('cycle base 2016-25',avg(ae,C)),('literal window 2021-25',avg(ae,W)),('continuing 2025 alone',ae[2025])):
    top=pv(base,0,r); bot=pv(base,g_dec,r)
    t10=pv(base,0,0.10); b10=pv(base,g_dec,0.10)
    print('%-24s EV top %.0f bottom %.0f | per share top %.0fp bottom %.0fp | fair(10%%) EV %.0f -> %.0fp | yield at price %.2f%%'%(label,top,bot,(top-nd)/shares*100,(bot-nd)/shares*100,(t10+b10)/2,((t10+b10)/2-nd)/shares*100, base/(price/100*shares+nd)*100))
for label,base in (('EQ cycle base',avg(eq,C)),('EQ window',avg(eq,W)),('EQ 2025',eq[2025])):
    t10=pv(base,0,0.10); b10=pv(base,g_dec_eq,0.10)
    print('%-14s equity-only fair %.0fp ; top at gilt %.0fp ; yield at price %.2f%%'%(label,(t10+b10)/2/shares*100, pv(base,0,r)/shares*100, base/(price/100*shares)*100))
print('market cap at 297.5p: %.0f ; EV with pre-IFRS16 net debt %.0f'%(price/100*shares, price/100*shares+nd))
print('owner cash needed for 10%% on EV: %.0f'%((price/100*shares+nd)*0.10))
