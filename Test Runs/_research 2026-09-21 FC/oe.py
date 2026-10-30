# All figures $000, transcribed BY HAND from the filed CONSOLIDATED STATEMENTS OF CASH FLOWS
# in seven 10-Ks (accessions in the run file). NOT from XBRL: capitalized curriculum
# development is tagged fc:PaymentsForCurriculumDevelopmentCosts, a company extension that
# SEC companyfacts does not carry at all.
# fy: (OCF, PPE, curriculum, content/license, SBC, D&A, curric_amort, NI, d_deferred_rev)
D = {
2008:( 7868, 4164, 4042,    0,  -259,  9533, 2124,   5527, None),
2009:( 5282, 2275, 1762,    0,   468,  8038, 2263, -10832, None),
2010:( 7024, 1384,  712,    0,  1099,  7429, 2083,   -518, None),
2011:(15643, 2326, 3097,    0,  2788,  7107, 1639,   4807, None),
2012:(15562, 2279, 2113,    0,  3835,  5698, 1816,   7841, None),
2013:(15528, 2174, 3224,    0,  3589,  6131, 1891,  14319, None),
2014:(18124, 3470, 7787,    0,  3534,  7326, 2824,  18067,  3287),
2015:(26190, 2446, 2166,    0,  2536,  7875, 4093,  11116,  2481),
2016:(32665, 3993, 2236,    0,  3121,  6943, 3865,   7016,  8112),
2017:(17357, 7187, 6466,  750,  3658,  7443, 3745,  -7172, 19142),
2018:(16861, 6528, 2998,    0,  2846, 10525, 5280,  -5887, 11613),
2019:(30452, 4153, 2688,    0,  4789, 11359, 4954,  -1023,  8828),
2020:(27563, 4183, 5082,    0,  -573, 11270, 3949,  -9435,  2806),
2021:(46177, 1602, 2504,    0,  8617, 11196, 3445,  13623, 19788),
2022:(52254, 3177, 2154,    0,  8286, 10169, 3354,  18430, 14245),
2023:(35738, 4515, 9035,    0, 12520,  8613, 3084,  17781,  8806),
2024:(60257, 3694, 6866,  750, 10142,  8153, 3172,  23402, 13458),
2025:(28977, 8253, 7561, 1074,  5805,  8458, 4440,   3068,  3151),
}
print(f"{'FY':>5} {'OCF':>7} {'capex':>7} {'D&A':>7} {'SBC':>6} | {'OE(c=D&A)':>9} {'OE(c=capex)':>11}")
rows={}
for fy,(ocf,ppe,cur,con,sbc,da,ca,ni,dr) in D.items():
    capex=ppe+cur+con; dda=da+ca
    lo=ocf-sbc-capex   # (c) = total capex  -> conservative end
    hi=ocf-sbc-dda     # (c) = D&A default [E3-44]
    rows[fy]=(lo,hi,ocf,capex,dda,sbc)
    print(f"{fy:>5} {ocf:>7} {capex:>7} {dda:>7} {sbc:>6} | {hi:>9} {lo:>11}")
import statistics as st
def win(a,b,i):
    v=[rows[f][i] for f in range(a,b+1)]
    return sum(v)/len(v)
print()
for (a,b) in [(2021,2025),(2022,2026-1),(2016,2025),(2011,2025),(2008,2025),(2013,2017),(2016,2020)]:
    if b>2025: continue
    print(f"  window {a}-{b} ({b-a+1}y):  OE c=D&A mean {win(a,b,1)/1000:7.2f}M   OE c=capex mean {win(a,b,0)/1000:7.2f}M   OCF mean {win(a,b,2)/1000:6.2f}M")
