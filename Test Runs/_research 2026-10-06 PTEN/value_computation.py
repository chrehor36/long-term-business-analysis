# COMPUTATION - NOT A CLEARANCE. Arithmetic only, from owner_cash.py rows.
import owner_cash as oc
SH=381.384874      # cover shares, 10-Q filed 2026-08-04 (0000889900-26-000056)
P=11.55            # close 2026-10-05, aggregator (live quote only)
R=0.0566           # UST 30-yr par yield 2026-10-05
NETDEBT=1234.2-203.2   # LTD (book) less cash+restricted, 2026-06-30 10-Q
INT=71.0           # interest expense 2025, 10-K FY2025
rows={}
for y,(o,s,c,p,d,ni,fl) in oc.D.items():
    rows[y]=dict(gross=o-s-c-fl, net=o-s-c-fl+p, dda=o-s-d)
REV={2007:1986,2008:2064,2009:782,2010:1463,2011:2566,2012:2723,2013:2716,2014:3182,2015:1891,2016:916,2017:2357,2018:3327,2019:2471,2020:1124,2021:1357,2022:2648,2023:4146,2024:5378,2025:4827}
CASHACQ={2007:29,2010:238,2014:176,2017:502,2018:14,2021:29,2023:65+357}
def mean(ys,k): return sum(rows[y][k] for y in ys)/len(ys)
five=range(2021,2026); whole=range(2007,2026)
print("market cap %.0f  net debt %.0f  EV %.0f"%(SH*P,NETDEBT,SH*P+NETDEBT))
for lab,ys in [("five-year 2021-25",five),("whole-cycle 2007-25",whole)]:
    for k in ["gross","net","dda"]:
        m=mean(ys,k)
        v_gov=m/R; v10=m/0.10
        print(f"{lab:20s} {k:5s} mean {m:7.1f}  value@gov {v_gov:8.0f} (${v_gov/SH:6.2f}/sh)  value@10% equity {v10:7.0f} (${v10/SH:5.2f})  @10% EV-basis ${((m+INT)/0.10-NETDEBT)/SH:5.2f}  yield at price {100*m/(SH*P):5.2f}%")
# whole-cycle margin on revenue scaled to 2025 revenue
ocsum=sum(rows[y]["gross"] for y in whole); rsum=sum(REV[y] for y in whole)
acq=sum(CASHACQ.values())
print("whole-cycle owner cash margin %.2f%%  (after cash acquisitions %.2f%%)"%(100*ocsum/rsum,100*(ocsum-acq)/rsum))
for lab,margin in [("margin x 2025 revenue",ocsum/rsum),("after cash acq x 2025 rev",(ocsum-acq)/rsum)]:
    m=margin*REV[2025]
    print(f"{lab:28s} owner cash {m:6.0f}  @gov ${m/R/SH:5.2f}  @10% ${m/0.10/SH:5.2f}")
print("sum whole-cycle owner cash gross %.0f, cash acquisitions %.0f, after %.0f"%(ocsum,acq,ocsum-acq))
