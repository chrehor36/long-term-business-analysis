# all from filed cash-flow statements (accessions in run file); $M
ocf ={2016:104.5,2017:82.7,2018:104.9,2019:161.6,2020:145.9,2021:93.2,2022:81.7,2023:207.3,2024:184.5,2025:138.3}
cap ={2016:16.5,2017:23.3,2018:28.9,2019:29.9,2020:29.7,2021:39.1,2022:39.6,2023:62.1,2024:41.4,2025:50.3}
sw  ={2016:0,2017:4.7+4.2,2018:1.2,2019:1.1,2020:0,2021:0,2022:2.7,2023:15.1,2024:20.9,2025:25.2}
proc={2016:0,2017:0,2018:0,2019:0,2020:0,2021:2.9,2022:0.2,2023:0.1,2024:0.5,2025:1.1}
sbc ={2016:3.3,2017:4.1,2018:4.9,2019:6.6,2020:5.8,2021:4.4,2022:6.7,2023:8.0,2024:8.5,2025:8.1}
da  ={2016:38.1,2017:50.4,2018:49.6,2019:47.6,2020:46.0,2021:42.7,2022:40.1,2023:39.3,2024:43.5,2025:43.6}
acq ={2016:197.4,2017:-2.6,2018:5.4,2019:0,2020:0,2021:0,2022:0,2023:34.7,2024:0.2,2025:0.7}
nint={2021:-1.5,2022:-1.1,2023:2.3,2024:9.3,2025:9.2}  # net interest income, pre-tax (filed)
oc={y:ocf[y]-cap[y]-sw[y]+proc[y]-sbc[y] for y in ocf}
dv={y:ocf[y]-sbc[y]-da[y] for y in ocf}
for y in ocf: print(y,'owner cash(capex)',round(oc[y],1),' depr variant',round(dv[y],1),' capex+sw/D&A',round((cap[y]+sw[y])/da[y],2))
a5=sum(oc[y] for y in range(2021,2026))/5; b5=sum(oc[y] for y in range(2016,2021))/5
d5=sum(dv[y] for y in range(2021,2026))/5
ii=sum(nint[y]*0.76 for y in nint)/5
print('avg 2021-25 owner cash',round(a5,1),' avg 2016-20',round(b5,1),' depr variant avg',round(d5,1),' after-tax net interest avg',round(ii,1))
print('acq 2021-25 per yr',round(sum(acq[y] for y in range(2021,2026))/5,1),' acq 2016-25 total',round(sum(acq.values()),1))
r=0.0563
def val(C,g,yrs=10):
    v=0;c=C
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    return v+c/r/(1+r)**yrs
sh=24.631047; cash=250.2; closure=64.7; pens=12.7
adj=cash-closure-pens
lo=a5-ii; hi=d5-ii
for lab,C,g in [('bottom: capex basis, no growth',lo,0),('top: depr basis, 3.3% op-income growth',hi,0.033),('capex basis at 3.3%',lo,0.033),('depr basis no growth',hi,0)]:
    V=val(C,g); print(lab,'C',round(C,1),'ops value',round(V),' equity/share',round((V+adj)/sh,2))
# fair price: after-tax floor 10%*(1-0.24)=7.6%; central C, g
C=(lo+hi)/2; g=0.015; P=C/(0.076-g)
print('central C',round(C,1),'fair ops value',round(P),' fair/share',round((P+adj)/sh,2))
print('market cap',round(98.17*sh,1),' owner cash yield',round(a5/(98.17*sh)*100,2))
