# Owner cash for Ambu A/S, DKKm, fiscal years to 30 September. Figures typed from the filed
# consolidated cash flow statements and notes 2.4 (annual reports named in the run file).
# Arithmetic only; no judgment here.
FY   = ["15/16","16/17","17/18","18/19","19/20","20/21","21/22","22/23","23/24","24/25"]
rev  = [2084, 2355, 2606, 2820, 3567, 4013, 4444, 4775, 5391, 6037]
cfo  = [369, 462, 554, 533, 295, 328, 95, 518, 813, 791]
capx = [84, 141, 233, 259, 428, 573, 553, 326, 289, 384]      # intangibles + tangibles, net of disposals
leas = [1, 4, 3, 8, 32, 44, 52, 63, 65, 63]                    # lease / finance-lease principal repaid
sbc  = [None, None, 26, 12, 19, 11, 12, 17, 26, 31]            # share-based payment added back in CFO
intp = [29, 32, 44, 20, 28, 15, 29, 63, 16, 13]                # interest paid net of interest received
acq  = [155, 0, 928, 2, 2, 301, 5, 0, 0, 0]                    # acquisitions of enterprises and technology
# maintenance guess: depreciation of PP&E (ex right-of-use) + amortisation of own development and IT
maint= {"20/21": 74+56, "21/22": 77+100, "22/23": 77+137, "23/24": 75+154, "24/25": 82+182}
TAX = 0.22   # Danish statutory rate
print("FY     rev   CFO  capex lease SBC  owner(all)  owner(maint)  +int(after tax)  acq")
oc_all, oc_m, ia = [], [], []
for i,f in enumerate(FY):
    s = sbc[i] or 0
    a = cfo[i]-capx[i]-leas[i]-s
    m = cfo[i]-maint[f]-leas[i]-s if f in maint else None
    it = round(intp[i]*(1-TAX),1)
    print(f"{f} {rev[i]:6} {cfo[i]:5} {capx[i]:5} {leas[i]:4} {s:4} {a:9} {m if m is not None else '':>12} {it:12} {acq[i]:6}")
    if i>=5: oc_all.append(a); oc_m.append(m); ia.append(it)
avg = lambda x: sum(x)/len(x)
A, M, I = avg(oc_all), avg(oc_m), avg(ia)
print(f"\n5y avg FY21-25: all-spending {A:.1f}, maintenance {M:.1f}, interest after tax {I:.1f}")
R, F = 0.035, 0.10
NETCASH = 705-19-(300-123.6)    # 30.06.26 cash less credit institutions, less buyback paid after 30.06.26
SH = (269_294_389-8_641_687)/1e6
P, FX = 76.20, 6.6803
print(f"net cash {NETCASH:.1f}  shares {SH:.3f}m  mcap {SH*P:.0f}  EV {SH*P-NETCASH:.0f}")
for name, oc in [("maintenance (central)", M), ("all-spending (beside)", A)]:
    ae = oc + I
    v  = (ae/R + NETCASH)/SH; vf = (ae/F + NETCASH)/SH
    eo = (oc/R)/SH;           eof = (oc/F)/SH
    print(f"{name}: all-equity owner cash {ae:.1f}; value/share {v:.2f} (USD {v/FX:.2f}); fair@10% {vf:.2f} (USD {vf/FX:.2f}); equity-only value {eo:.2f}, fair {eof:.2f}; yield on EV {ae/(SH*P-NETCASH)*100:.2f}%")
# beside, not a case: the most generous stream the conventions could allow -- FY24/25 maintenance owner cash
# grown at the business's own sales growth FY19/20-FY24/25 for ten years, then flat. Expected return at the price.
g = (rev[-1]/rev[4])**(1/5)-1
base = (cfo[-1]-maint["24/25"]-leas[-1]-sbc[-1]) + ia[-1]
EV = SH*P-NETCASH
def pv(r):
    s=0; c=base
    for t in range(1,11):
        c*=1+g; s+=c/(1+r)**t
    return s + c/r/(1+r)**10
lo,hi=0.001,0.5
for _ in range(100):
    mid=(lo+hi)/2
    if pv(mid)>EV: lo=mid
    else: hi=mid
print(f"\nbeside: sales CAGR FY20-25 {g*100:.1f}%; FY25 maintenance owner cash all-equity {base:.1f}; expected return at the price on that stream {mid*100:.2f}%")
# 10-year sales growth FY16-25 for reference
print(f"sales CAGR FY16-FY25 {((rev[-1]/rev[0])**(1/9)-1)*100:.1f}%")

# Default pair (acquisitions deducted, total growth credited): the window's net purchases spread over the five years.
ACQ = sum(acq[5:])/5
print(f"\nnet purchases FY21-25 {sum(acq[5:])}, per year {ACQ:.1f}; half of maintenance owner cash before purchases over window {sum(oc_m)/2:.1f}; half of all-spending {sum(oc_all)/2:.1f}")
for name, oc in [("maintenance less acquisitions (central, default pair)", M-ACQ), ("all-spending less acquisitions (beside)", A-ACQ)]:
    ae = oc + I
    v  = (ae/R + NETCASH)/SH; vf = (ae/F + NETCASH)/SH
    eo = (oc/R)/SH; eof = (oc/F)/SH
    print(f"{name}: all-equity owner cash {ae:.1f}; value/share {v:.2f} (USD {v/FX:.2f}); fair@10% {vf:.2f} (USD {vf/FX:.2f}); equity-only value {eo:.2f} (USD {eo/FX:.2f}), fair {eof:.2f} (USD {eof/FX:.2f}); yield on EV {ae/EV*100:.2f}%")
print(f"price DKK {P} = USD {P/FX:.2f}; FY25 maintenance all-equity yield on EV {base/EV*100:.2f}%")

# Q7(c): purchases stop after year ten with growth. No-growth case: owner cash before purchases in perpetuity,
# less the window's average purchases for years 1-10 only.
ann = lambda r: (1-(1+r)**-10)/r
print("\nno-growth, purchases deducted years 1-10 only:")
for name, oc in [("maintenance (central)", M), ("all-spending (beside)", A)]:
    ae = oc + I
    v  = (ae/R - ACQ*ann(R) + NETCASH)/SH; vf = (ae/F - ACQ*ann(F) + NETCASH)/SH
    eo = (oc/R - ACQ*ann(R))/SH; eof = (oc/F - ACQ*ann(F))/SH
    print(f"{name}: value/share {v:.2f} (USD {v/FX:.2f}); fair@10% {vf:.2f} (USD {vf/FX:.2f}); equity-only value {eo:.2f} (USD {eo/FX:.2f}), fair {eof:.2f} (USD {eof/FX:.2f})")
