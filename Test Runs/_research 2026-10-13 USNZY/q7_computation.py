# COMPUTATION, NOT A CLEARANCE. Usiminas owner cash and the Q7 range/fair price by the v5 conventions.
# All figures R$ million, from CVM DFP structured data (consolidated DFC, DMPL) and DFP notes; see notes.md.
yrs  = list(range(2016, 2026))
cfo  = [-310.3, 877.0, 509.6, 1971.8, 3759.4, 5296.6, 997.1, 4568.1, 989.2, 2179.4]
capx = [207, 208, 405, 646, 769, 1390, 2027, 2930, 924, 1050]        # 6.02.03 purchases of PP&E
intg = [16, 8, 28, 35, 30, 94, 65, 54, 71, 121]                       # purchases of intangibles
sale = [6, 9, 40, 9, 121, 105, 88, 20, 15, 59]                        # proceeds from PP&E sold
leas = [0, 0, 0, 0, 0, 0, 56, 46, 46, 34]                             # lease principal (not shown 2016-2021)
parc = [2, 4, 0, 0, 0, 0, 0, 0, 21, 25]                               # instalment tax payments (financing)
nci  = [21.9, 23.8, 80.1, 69.8, 171.6, 348.2, 351.4, 295.2, 41.2, 83.5]  # DMPL dividends to non-controlling
intp = [897, 764, 534, 364, 337, 344, 584, 555, 548, 840]             # interest paid (in CFO)
inti = [147.7, 173.9, 64.3, 73.5, 40.9, 5.7, 548.4, 622.2, 527.5, 604.8]  # income on financial investments (notes)
da   = [1216, 1172, 1030, 992, 1000, 983, 903, 1062, 1226, 1275]
sales= [8454, 10734, 13737, 14949, 16088, 33737, 32471, 27638, 25870, 26263]
T = 0.34   # CONVENTION of this run: Brazilian statutory IRPJ+CSLL rate for the interest tax shield
oc = [c - k - i + s - l - p - n for c,k,i,s,l,p,n in zip(cfo,capx,intg,sale,leas,parc,nci)]
ocu = [o + (ip - ii) * (1 - T) for o, ip, ii in zip(oc, intp, inti)]
for y,o,u,d,k,i in zip(yrs,oc,ocu,da,capx,intg): print(y, f'OC equity {o:8.0f}  OC all-equity {u:8.0f}  capex+intang {k+i:6.0f}  D&A {d}')
avg = lambda a: sum(a)/len(a)
base_e, base_u = avg(oc), avg(ocu)
h1e, h2e = avg(oc[:5]), avg(oc[5:]); h1u, h2u = avg(ocu[:5]), avg(ocu[5:])
g_e = (h2e/h1e)**(1/5)-1; g_u = (h2u/h1u)**(1/5)-1
print(f'cycle base 2016-2025: equity {base_e:.0f}, all-equity {base_u:.0f}')
print(f'literal window 2021-2025: equity {avg(oc[5:]):.0f}, all-equity {avg(ocu[5:]):.0f}')
print(f'halves: equity {h1e:.0f} -> {h2e:.0f} g={g_e*100:.2f}%/yr ; all-equity {h1u:.0f} -> {h2u:.0f} g={g_u*100:.2f}%/yr')
print(f'capex+intangibles 10y {sum(capx)+sum(intg)} vs D&A 10y {sum(da)}; max OC/sales {max(o/s for o,s in zip(oc,sales))*100:.1f}%')
def value(c0, g, r, n=10):
    v, c = 0.0, c0
    for t in range(1, n+1):
        c *= (1+g); v += c/(1+r)**t
    return v + (c/r)/(1+r)**n          # zero nominal growth after year ten
SH = 1230.942660   # shares outstanding, m (ITR 2026-06-30 capital composition, issued less treasury)
NETCASH = 499.0    # company's net debt (499) negative at 2026-06-30, ITR 2Q26 release: cash and investments 6,823 less gross debt 6,324
FORF = 570.1 - 393.0  # forfaiting balance estimate at 2026-06-30 (570.1 at 2025-12-31 less H1 2026 outflow 393)
RF = 0.1257        # NTN-F 2037, Tesouro Nacional, 2026-10-09
PRICE = 7.15
for lab, b, g, add in [('all-equity', base_u, g_u, NETCASH), ('equity-only', base_e, g_e, 0.0)]:
    top = value(b, 0.0, RF); bot = value(b, min(g, 0.0), RF)
    t10 = value(b, 0.0, 0.10); b10 = value(b, min(g, 0.0), 0.10)
    ps = lambda v: (v + add) / SH
    print(f'{lab}: range R$ {ps(bot):.2f} to {ps(top):.2f} per share; fair price (ends at 10%, averaged) R$ {(ps(b10)+ps(t10))/2:.2f}')
    ev = PRICE*SH - add
    print(f'   implied cash yield at price on no-growth case: {b/ev*100:.2f}%')
    if lab == 'all-equity':
        print(f'   with forfaiting {FORF:.0f} counted as debt: fair R$ {((b10+t10)/2 + add - FORF)/SH:.2f}, top R$ {(top+add-FORF)/SH:.2f}')
# check: the declining all-equity case valued at ten percent, per share
print(f'declining all-equity case at 10%: R$ {(value(base_u, g_u, 0.10) + NETCASH)/SH:.2f}')
