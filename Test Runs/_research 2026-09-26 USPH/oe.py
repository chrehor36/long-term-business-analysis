"""USPH owner earnings, the corpus's way [E2-23]: OCF - SBC - (c), then the partners' share. ARITHMETIC ONLY, NO CONCLUSION.
Every input typed from the filed Consolidated Statements of Cash Flows (in thousands), extracted to cf_FY*_flat.txt
from the 10-Ks FY2010 (2008-10), FY2013 (2011-13), FY2016 (2014-16, 2014-15 as restated), FY2019 (2017-19),
FY2022 (2020-22), FY2025 (2023-25).
(c) band: the smaller and larger of cash-flow D&A (which includes amortisation of acquired intangibles) and purchase of fixed assets.
Partners: 'distributions to non-controlling interests' (financing). In 2014-2017 distributions to the mandatorily
redeemable partners sat inside OCF already (FY2016 10-K Note 5 roll-forward), so the same subtraction is consistent.
Buyouts: purchases of partner interests (investing) plus payments to settle mandatorily redeemable NCI (financing, 2014-18),
less proceeds from sales of partner interests and notes repaid on them. Shown apart, as a disclosed choice.
Relief Funds (CARES Act, other income inside OCF): 2020 $13.5M, 2021 $4.6M (FY2022 10-K), removed in the normalised line [E4-41]."""
# year: OCF, SBC, capex, D&A, dist_NCI, buyouts_net, acquisitions
D = {
2008:(30172,1574,4299,5966,7295,1096,19589),
2009:(30944,1573,3876,5897,9438,2329,1178),
2010:(30521,1292,3673,5667,9580,682,18197),
2011:(32655,2032,3222,5449,9767,20439,9451),
2012:(39249,2102,4234,5287,9332,2244-239,7929),
2013:(44795,2743,4637,5562,9164,1876-233,46628),
2014:(41391,3363,5167,6740,5963,227+5233,12270),
2015:(37520,4491,6263,7952,5892,968+6115,18965),
2016:(51050,4962,8260,8779,5718,670+1262,23623),
2017:(56526,5032,7095,9710,5572,2361-121,36682),
2018:(73005,5939,7193,9755,15646,350+265,16367),
2019:(62448,6985,10189,10095,16235,8651+428-207,30597),
2020:(99995,7917,7639,10533,18331,20385+238-127,23907),
2021:(76406,7867,8201,11591,16931,28465+1274-69-131,86823),
2022:(58537,7264,8248,14743,15348,14987+280-402,59788),
2023:(81978,7236,9294,15695,16100,10986+281-102-875-510,26582),
2024:(74940,7823,9186,18681,14711,8052+1004-26-79-551,133087),
2025:(75058,8270,14071,22391,19269,9917+273-30-186-531,15674),
}
RELIEF={2020:13500,2021:4600}
CAP=1266.0  # $M, Step 0: 14,922,698 x $84.84
R={}
print('| FY | OCF | SBC | capex | D&A | consolidated OE (c=max..min) | to partners | **USPH OE low..high** | net partner buyouts | after buyouts low..high | acquisitions |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for y,(ocf,sbc,cx,da,dist,bo,acq) in D.items():
    ocf_n=ocf-RELIEF.get(y,0)
    hi_c,lo_c=max(cx,da),min(cx,da)
    cl,ch=ocf_n-sbc-hi_c, ocf_n-sbc-lo_c
    ul,uh=cl-dist,ch-dist
    bl,bh=ul-bo,uh-bo
    R[y]=(ul,uh,bl,bh,acq)
    tag=' (relief removed)' if y in RELIEF else ''
    print(f'| {y}{tag} | {ocf/1e3:,.1f} | {sbc/1e3:,.1f} | {cx/1e3:,.1f} | {da/1e3:,.1f} | {cl/1e3:,.1f}..{ch/1e3:,.1f} | {dist/1e3:,.1f} | **{ul/1e3:,.1f}..{uh/1e3:,.1f}** | {bo/1e3:,.1f} | {bl/1e3:,.1f}..{bh/1e3:,.1f} | {acq/1e3:,.1f} |')
print()
def w(a,b):
    ys=range(a,b+1); n=len(ys)
    ul=sum(R[y][0] for y in ys)/n/1e3; uh=sum(R[y][1] for y in ys)/n/1e3
    bl=sum(R[y][2] for y in ys)/n/1e3; bh=sum(R[y][3] for y in ys)/n/1e3
    aq=sum(R[y][4] for y in ys)/n/1e3
    print(f'| FY{a}-{b} ({n}y) | ${ul:,.1f}M..${uh:,.1f}M | {ul/CAP:.2%}..{uh/CAP:.2%} | ${bl:,.1f}M..${bh:,.1f}M | {bl/CAP:.2%}..{bh/CAP:.2%} | ${aq:,.1f}M a year |')
print('| window | USPH OE (mean) | yield on $1,266.0M | after net partner buyouts | yield | acquisitions paid in the window |')
print('|---|---|---|---|---|---|')
for a,b in [(2023,2025),(2021,2025),(2016,2020),(2016,2025),(2011,2015),(2008,2025)]: w(a,b)
