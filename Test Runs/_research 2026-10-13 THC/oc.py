# Owner cash for THC, 2021-2025, from the filed cash-flow statements (FY2023 and FY2025 10-Ks). USD millions.
Y=[2021,2022,2023,2024,2025]
OCF={2021:1568,2022:1083,2023:2374,2024:2047,2025:3540}
# aberrational items the filer itself describes (FY2022 10-K: MAPP repaid/recouped in OCF; deferred payroll tax paid)
COVID={2021:512+128,2022:880+128,2023:0,2024:0,2025:0}
# 2024 income taxes on the divestiture gains: FY2025 10-K MD&A says 2025 tax payments were $821M lower than 2024 (guess: the excess is the tax on the gains)
DIVTAX={2021:0,2022:0,2023:0,2024:821,2025:0}
SBC={2021:56,2022:56,2023:66,2024:67,2025:104}
CAPEX={2021:658,2022:762,2023:751,2024:931,2025:1010}
DA={2021:855,2022:841,2023:870,2024:818,2025:863}
NCI={2021:423,2022:560,2023:594,2024:681,2025:809}
FL={2021:140,2022:118,2023:107,2024:87,2025:62}
BUY={2021:1220,2022:234,2023:224,2024:571,2025:308}      # purchases of businesses or JV interests
BUYNCI={2021:27,2022:100,2023:167,2024:200,2025:92}     # purchases of NCI
SELL={2021:1248,2022:210,2023:71,2024:4981,2025:38}     # proceeds from sales of facilities and other assets
SELLNCI={2021:25,2022:27,2023:43,2024:23,2025:42}
SELLX={2024:4981}  # the 2024 divestiture of 14 hospitals, treated as aberrational (shown literal beside)
INT={2021:937,2022:848,2023:882,2024:851,2025:865}      # interest paid
TAX=0.24   # CONVENTION of this run: 21% federal plus about 3% state (2025 rate reconciliation, state 2.9%)
REV={2021:19485,2022:19174,2023:20548,2024:20665,2025:21310}
rows=[]
for y in Y:
    ocf=OCF[y]+COVID[y]+DIVTAX[y]
    pre=ocf-SBC[y]-CAPEX[y]-NCI[y]-FL[y]          # owner cash to common before purchases, after all capex
    preDA=ocf-SBC[y]-DA[y]-NCI[y]-FL[y]
    sell=SELL[y]-SELLX.get(y,0)
    acq=BUY[y]+BUYNCI[y]-sell-SELLNCI[y]
    lit=BUY[y]+BUYNCI[y]-SELL[y]-SELLNCI[y]
    eq=pre-acq; eqlit=OCF[y]-SBC[y]-CAPEX[y]-NCI[y]-FL[y]-lit
    ae=eq+INT[y]*(1-TAX); aepre=pre+INT[y]*(1-TAX)
    rows.append((y,ocf,pre,preDA,acq,eq,eqlit,aepre,ae))
    print(y,f"OCFadj {ocf:6} pre-purch {pre:6} (D&A var {preDA:6}) netacq {acq:6} EQ {eq:6} literal {eqlit:6} | AE pre {aepre:7.0f} AE {ae:7.0f} | AE/rev {ae/REV[y]:.3f}")
import statistics as s
for i,n in [(2,'pre'),(3,'preDA'),(5,'EQ'),(6,'EQlit'),(7,'AEpre'),(8,'AE')]:
    print(n,'5yr mean',round(s.mean(r[i] for r in rows)))
