# R$ millions, from the filed cash flow statements (20-F FY2025, FY2022, FY2019; XBRL rows checked against them)
Y=list(range(2016,2026))
CFO   ={2016:276,2017:572,2018:2208,2019:4872,2020:9577,2021:14793,2022:2043,2023:7293,2024:8651,2025:-973}
CAPEX ={2016:1632,2017:1060,2018:1319,2019:2217,2020:1684,2021:2865,2022:3352,2023:4408,2024:5494,2025:5936}
INT   ={2016:3050,2017:2635,2018:2142,2019:2039,2020:1922,2021:2138,2022:2316,2023:3429,2024:4052,2025:4268}
ADV   ={2016:0,2017:0,2018:0,2019:2525,2020:-10,2021:-697,2022:-221,2023:4844,2024:6968,2025:-510}   # customer advances inside CFO
FORF  ={2016:0,2017:0,2018:0,2019:0,2020:-497,2021:3816,2022:1269,2023:-1500,2024:-1328,2025:5}       # forfaiting inside CFO
ACQ   ={2016:0,2017:0,2018:219-1670,2019:210,2020:132,2021:296+673+264,2022:663+7342,2023:339,2024:32,2025:24+23+213+54+22-43}  # Gramperfil, Estrela, Galvacolor, Global Dot net, less sale of equity assets 43  # net cash for businesses/shares
D_A   ={2016:1322,2017:1453,2018:1273,2019:1519,2020:2522,2021:2218,2022:2878,2023:3379,2024:3791,2025:4150}
REV   ={2016:17149,2017:18525,2018:22969,2019:25436,2020:30064,2021:47912,2022:44362,2023:45438,2024:43687,2025:44798}
T=0.34
rows=[]
print("year  CFO   capex  adv  forf  OC_eq_asfiled OC_eq_recast  OC_alleq_recast  acq  OC_alleq_recast_lessacq  D&A  rev")
for y in Y:
    eq_asf=CFO[y]-CAPEX[y]
    eq_rec=CFO[y]-ADV[y]-FORF[y]-CAPEX[y]
    ae_rec=eq_rec+INT[y]*(1-T)
    print(y, CFO[y], CAPEX[y], ADV[y], FORF[y], eq_asf, eq_rec, round(ae_rec), ACQ[y], round(ae_rec-ACQ[y]), D_A[y], REV[y])
    rows.append((y,eq_asf,eq_rec,ae_rec,ae_rec-ACQ[y],eq_rec-ACQ[y]))
def avg(i,ys): return sum(r[i] for r in rows if r[0] in ys)/len(ys)
for lab,ys in (("2021-2025 window",range(2021,2026)),("2016-2025 cycle",range(2016,2026)),("2016-2020 half",range(2016,2021)),("2021-2025 half",range(2021,2026))):
    print(lab, "eq as filed %.0f | eq recast %.0f | eq recast less acq %.0f | all-eq recast %.0f | all-eq recast less acq %.0f" % (avg(1,ys),avg(2,ys),avg(5,ys),avg(3,ys),avg(4,ys)))
