# COMPUTATION, NOT A CLEARANCE. Figures in USD millions from the filed statements (accessions in the run file).
yrs=[2021,2022,2023,2024,2025]
ocf  ={2021:-80.476,2022:-132.2,2023:-104.6,2024:-108.099,2025:-56.167}
capex={2021:13.2,2022:33.9,2023:41.2,2024:25.849,2025:9.844}
intan={2021:1.5,2022:0.6,2023:0.2,2024:1.768,2025:0.337}
sbc  ={2021:9.7,2022:9.4,2023:11.0,2024:7.456,2025:6.339}
lease={2021:2.8,2022:3.3,2023:4.0,2024:3.327,2025:3.043}
inv  ={2021:4.043,2022:19.606,2023:43.340,2024:36.885,2025:24.534}
oc={y:ocf[y]-capex[y]-intan[y]-sbc[y]-lease[y] for y in yrs}
ocx={y:oc[y]-inv[y] for y in yrs}
for y in yrs: print(y, round(oc[y],1), round(ocx[y],1))
a=sum(oc.values())/5; b=sum(ocx.values())/5
print('avg equity-only',round(a,1),'avg all-equity',round(b,1))
r=0.0543; f=0.10
fx=400/301.1
cash=502.102+3.046; lti=42.030; paid=82.5*fx; ndebt=(301.1-275.0)*fx
net=cash+lti-paid-ndebt
sh=301.506494+49.584212+1.084540
print('fx',round(fx,4),'paid',round(paid,1),'gp net debt',round(ndebt,1),'net cash',round(net,1),'shares',round(sh,2))
for lab,c,n in (('all-equity',b,net),('equity-only',a,0.0)):
    v=c/r+n; fp=c/f+n
    print(lab,'value $M',round(v,0),'per sh',round(v/sh,2),'| fair at 10%',round(fp,0),'per sh',round(fp/sh,2))
# sensitivities beside: 2025 alone; H1 2026 annualised (OCF -19.205, capex 1.424, H1)
for lab,c in (('2025 all-equity',ocx[2025]),('2025 equity-only',oc[2025])):
    n=net if 'all' in lab else 0
    print(lab, round((c/r+n)/sh,2))
px=1.57; print('mkt cap',round(px*sh,1),'EV',round(px*sh-net,1))
# sales and owner-cash: highest share of sales
