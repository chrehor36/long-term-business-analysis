# Q3: after-tax operating earnings before interest (net income + interest expense x (1-0.26)) over average capital
# (debt on the face: LTD noncurrent + current + short-term; plus shareholders' equity). XBRL first-filed vintages.
NI ={2016:653,2017:523,2018:815,2019:828,2020:871,2021:990,2022:1074,2023:1152,2024:1182,2025:1456}
INT={2016:382,2017:391,2018:401,2019:381,2020:419,2021:383,2022:486,2023:566,2024:663,2025:776}
DEBT={2015:None,2016:7834,2017:8419,2018:9036,2019:9797,2020:11576,2021:13612,2022:15095,2023:16506,2024:18722,2025:19830}
EQ={2016:7103,2017:7184,2018:7631,2019:8059,2020:8938,2021:9700,2022:10508,2023:11349,2024:12114,2025:13401}
T=0.26
out=[]
for y in range(2017,2026):
    nopat=NI[y]+INT[y]*(1-T)
    cap=(DEBT[y]+EQ[y]+DEBT[y-1]+EQ[y-1])/2
    out.append((y,nopat,cap,nopat/cap))
    print(y, round(nopat), round(cap), f"{nopat/cap*100:.2f}%", f"debt/(debt+eq) {DEBT[y]/(DEBT[y]+EQ[y])*100:.1f}%", f"pretax cover n/a")
print('mean', f"{sum(o[3] for o in out)/len(out)*100:.2f}%")
# incremental 2020->2025
n20=NI[2020]+INT[2020]*(1-T); n25=NI[2025]+INT[2025]*(1-T)
c20=DEBT[2020]+EQ[2020]; c25=DEBT[2025]+EQ[2025]
print('incremental 2020-2025', round(n25-n20), round(c25-c20), f"{(n25-n20)/(c25-c20)*100:.2f}%")
n16=NI[2016]+INT[2016]*(1-T); c16=DEBT[2016]+EQ[2016]
print('incremental 2016-2025', round(n25-n16), round(c25-c16), f"{(n25-n16)/(c25-c16)*100:.2f}%")
print('debt x', round(DEBT[2025]/DEBT[2016],2), 'equity x', round(EQ[2025]/EQ[2016],2))
