"""Owner cash for Arcadis N.V., EUR millions, from the filed consolidated cash flow statements.
Sources: AR2016 p153 (FY2016), AR2017 p83 (FY2017), AR2019 p182 (FY2018, FY2019), AR2021 p210 (FY2020 restated, FY2021),
AR2023 p174 (FY2022 as revised, FY2023), AR2025 p200 (FY2024, FY2025). Page numbers are PDF pages of the downloaded files."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
#        CFO     capex   proc   lease   sbc     ipaid   irec   acq_in   acq_out assoc_in assoc_out oth_in oth_out NR       GR
D={2016:(139.273,64.768,5.530,0,     11.384,32.928, 8.816, 9.685, 3.374,25.179,19.479,5.395,7.416,2467.972,3328.762),
   2017:(151.131,59.324,5.865,0,     10.838,33.771, 9.888, 5.141, 5.273,23.998, 9.464,4.869,6.553,2436.506,3218.889),
   2018:(214.173,68.764,3.640,0,      6.686,37.732,15.927, 9.964, 0.037,31.848, 1.923,2.640,5.999,2439.923,3255.574),
   2019:(217.760,48.461,2.726,74.808,11.545,30.547, 5.612, 7.299, 0.000,17.511, 0.000,7.000,4.714,2576.602,3473.370),
   2020:(429.011,25.203,2.577,82.888, 8.501,23.582, 3.565, 7.369,15.006,64.669, 0.000,3.956,6.267,2493.564,3303.208),
   2021:(329.462,34.783,8.218,68.850, 5.868,16.223, 4.095, 0.606, 0.000, 3.995, 0.000,6.414,3.987,2564.597,3378.486),
   2022:(284.024,40.138,0.677,70.610, 8.568,22.005, 7.657,799.605,0.784, 0.036, 0.000,4.561,7.904,3018.677,4028.935),
   2023:(308.722,40.571,1.039,79.251, 6.187,45.946,20.425, 3.231, 7.219, 0.093, 0.000,5.282,4.360,3759.248,5003.322),
   2024:(350,    45,     0,    78,     8,     52,      8,     2,     1,     0,     0,    2,    2,    3880,    4995),
   2025:(386,    25,     1,    74,     8,     79,     35,    84,     0,     0,     0,    2,    1,    3760,    4875)}
FACTORING_2025=19.0   # filer's own "non-organic 19 million cash amelioration derived from factoring facility" (AR2025 p186)
TAX=0.275             # five-year effective rate 2021-2025: income taxes / profit before tax, filed income statements
rows={}
for y,(cfo,cap,proc,lease,sbc,ip,ir,ai,ao,si,so,oi,oo,nr,gr) in D.items():
    oth=oi-oo
    oc=cfo-cap+proc-lease-sbc-oth           # equity basis, after interest and tax paid, before purchases
    if y==2025: oc-=FACTORING_2025
    netint=ip-ir
    ocu=oc+netint*(1-TAX)                    # all-equity basis: before interest, after the company's tax
    purch=(ai-ao)+(si-so)                    # businesses and associates/JVs, net
    rows[y]=dict(oc=oc,ocu=ocu,purch=purch,nr=nr,gr=gr,netint=netint)
print("year  OC_eq  OC_allEq  purchases  OC_allEq-purch  OC/NR   OCu/NR")
for y,r in rows.items():
    print(f"{y}  {r['oc']:6.1f}  {r['ocu']:7.1f}  {r['purch']:8.1f}  {r['ocu']-r['purch']:8.1f}   {r['oc']/r['nr']*100:5.1f}%  {r['ocu']/r['nr']*100:5.1f}%")
W=[2021,2022,2023,2024,2025]
avg=lambda k:sum(rows[y][k] for y in W)/5
print(f"\nWindow 2021-2025: avg OC_eq {avg('oc'):.1f}; avg OC_allEq {avg('ocu'):.1f}; avg purchases {avg('purch'):.1f}; avg OC_allEq after purchases {avg('ocu')-avg('purch'):.1f}")
print(f"sum purchases {sum(rows[y]['purch'] for y in W):.1f} vs half of OC_allEq before purchases {0.5*sum(rows[y]['ocu'] for y in W):.1f} (serial-acquirer test, all-equity) ; equity basis half {0.5*sum(rows[y]['oc'] for y in W):.1f}")
P=[2016,2017,2018,2019,2020]
print(f"Prior window 2016-2020: avg OC_eq {sum(rows[y]['oc'] for y in P)/5:.1f}; avg OC_allEq {sum(rows[y]['ocu'] for y in P)/5:.1f}; avg purchases {sum(rows[y]['purch'] for y in P)/5:.1f}")
g=lambda a,b,n:(b/a)**(1/n)-1
print(f"OC_allEq growth 2021->2025 (4 yrs): {g(rows[2021]['ocu'],rows[2025]['ocu'],4)*100:.2f}%  ; halves (avg 2021-22 vs avg 2024-25, 3 yrs): {g((rows[2021]['ocu']+rows[2022]['ocu'])/2,(rows[2024]['ocu']+rows[2025]['ocu'])/2,3)*100:.2f}%")
print(f"OC_eq growth 2021->2025: {g(rows[2021]['oc'],rows[2025]['oc'],4)*100:.2f}%")
print(f"Ten-year: avg OC_allEq 2016-20 vs 2021-25 growth over 5 yrs: {g(sum(rows[y]['ocu'] for y in P)/5, avg('ocu'),5)*100:.2f}%")
print(f"Net revenue growth 2021->2025: {g(rows[2021]['nr'],rows[2025]['nr'],4)*100:.2f}% ; gross {g(rows[2021]['gr'],rows[2025]['gr'],4)*100:.2f}%")
org=[0.089,0.090,0.045,-0.005]; c=1
for x in org: c*=1+x
print(f"Organic net revenue growth 2022-2025 compound (filer's figures): {(c**0.25-1)*100:.2f}%")
print(f"max OC_allEq/NR in years read: {max(r['ocu']/r['nr'] for r in rows.values())*100:.2f}%")
