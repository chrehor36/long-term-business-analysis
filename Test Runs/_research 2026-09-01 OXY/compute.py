# All reserve quantities MMBoe; all dollars $ millions. Gas at 6 Mcf = 1 Boe.
def boe(oil, ngl, gas_bcf, syn=0.0):
    return oil + ngl + syn + gas_bcf/6.0

D = {}

# ---------------- CHEVRON (consolidated companies) ----------------
cvx_ed  = {2023: boe(225, 92, 743), 2024: boe(241,124,1114), 2025: boe(247,103,1544)}
cvx_ir  = {2023: boe(11,0,2),       2024: boe(11,0,2),       2025: boe(3,0,0)}
cvx_pr  = {2023: boe(443,113,2607), 2024: boe(466,143,2767), 2025: boe(521,164,2861)}
cvx_pd  = {2023: boe(2133,690,20407,598), 2024: boe(2121,683,19166), 2025: boe(2605,904,19146)}
D['CVX (consolidated cos.)'] = dict(
    ed=cvx_ed, ir=cvx_ir, prod=cvx_pr, pd=cvx_pd,
    expl={2023:1008,2024:1014,2025:1236}, dev={2023:12920,2024:13333,2025:14538},
    dda_og=16415)
# Chevron incl. affiliates (secondary)
cvx_ed_t = {2023: boe(225,92,743), 2024: boe(241,124,1114), 2025: boe(247,103,1544)}
cvx_ir_t = {2023: boe(11,0,2), 2024: boe(11,0,2), 2025: boe(4,0,0)}
cvx_pr_t = {2023: boe(546,122,2827), 2024: boe(571,152,2990), 2025: boe(667,174,3108)}
cvx_pd_t = {2023: boe(2614,770,21792,598), 2024: boe(2786,765,20954), 2025: boe(3321,979,20737)}
D['CVX (incl. affiliates)'] = dict(
    ed=cvx_ed_t, ir=cvx_ir_t, prod=cvx_pr_t, pd=cvx_pd_t,
    expl={2023:1008,2024:1014,2025:1236},
    dev={2023:12920+2364,2024:13333+1487,2025:14538+598}, dda_og=16415+4621+179)

# ---------------- CONOCOPHILLIPS ----------------
D['COP (consolidated ops.)'] = dict(
    ed={2023:381,2024:96,2025:189}, ir={2023:0,2024:0,2025:0},
    prod={2023:596,2024:649,2025:796}, pd={2023:3749,2024:4509,2025:4239},
    expl={2023:708,2024:988,2025:928}, dev={2023:9781,2024:10542,2025:11174},
    dda_og=11208)
D['COP (incl. equity affil.)'] = dict(
    ed={2023:391,2024:316,2025:200}, ir={2023:0,2024:0,2025:0},
    prod={2023:678,2024:732,2025:877}, pd={2023:4424,2024:5115,2025:4830},
    expl={2023:708+46,2024:988+18,2025:928+9}, dev={2023:9781+416,2024:10542+323,2025:11174+439},
    dda_og=11208+447)

# ---------------- EOG ----------------
D['EOG'] = dict(
    ed={2023:607,2024:580,2025:336}, ir={2023:0,2024:0,2025:0},
    prod={2023:361,2024:391,2025:452}, pd={2023:2349,2024:2566,2025:3346},
    expl={2023:437,2024:429,2025:513}, dev={2023:5358,2024:4942,2025:5511},
    dda_og=4202)

# ---------------- DIAMONDBACK (MBOE -> MMBoe) ----------------
D['FANG'] = dict(
    ed={2023:355.874,2024:278.808,2025:578.919}, ir={2023:0,2024:0,2025:0},
    prod={2023:163.413,2024:218.972,2025:336.178},
    pd={2023:1496.530,2024:2384.798,2025:2521.028},
    expl={2023:768,2024:194,2025:212}, dev={2023:1962,2024:2992,2025:3613},
    dda_og=4943)

# ---------------- DEVON ----------------
D['DVN'] = dict(
    ed={2023:322,2024:340,2025:443}, ir={2023:0,2024:0,2025:0},
    prod={2023:240,2024:270,2025:307}, pd={2023:1425,2024:1715,2025:1844},
    expl={2023:534,2024:690,2025:581}, dev={2023:3160,2024:2856,2025:3057},
    dda_og=3479)

YRS=[2023,2024,2025]
print(f"{'Company':26} {'Prod25':>7} {'RRR25':>8} {'RRR3y':>8} {'F&D25':>8} {'F&D3y':>8} {'DDA/Boe':>8} {'PDlife':>7}")
print('-'*90)
rows={}
for k,v in D.items():
    add25 = v['ed'][2025]+v['ir'][2025]
    add3  = sum(v['ed'][y]+v['ir'][y] for y in YRS)
    p25   = v['prod'][2025]; p3 = sum(v['prod'][y] for y in YRS)
    rrr25 = add25/p25*100; rrr3 = add3/p3*100
    fd25  = (v['expl'][2025]+v['dev'][2025])/add25
    fd3   = sum(v['expl'][y]+v['dev'][y] for y in YRS)/add3
    dda   = v['dda_og']/p25
    life  = v['pd'][2025]/p25
    rows[k]=(p25,rrr25,rrr3,fd25,fd3,dda,life,add25,add3,p3,
             v['expl'][2025]+v['dev'][2025], sum(v['expl'][y]+v['dev'][y] for y in YRS))
    print(f"{k:26} {p25:7.1f} {rrr25:7.1f}% {rrr3:7.1f}% {fd25:8.2f} {fd3:8.2f} {dda:8.2f} {life:7.2f}")

print()
print("ARITHMETIC DETAIL")
for k,(p25,rrr25,rrr3,fd25,fd3,dda,life,add25,add3,p3,ed25,ed3) in rows.items():
    v=D[k]
    print(f"\n== {k}")
    print(f"  2025 adds {add25:.1f} / prod {p25:.1f} = {rrr25:.1f}%")
    print(f"  3yr  adds {add3:.1f} / prod {p3:.1f} = {rrr3:.1f}%")
    print(f"  2025 F&D ({v['expl'][2025]}+{v['dev'][2025]}={ed25}) / {add25:.1f} = ${fd25:.2f}/Boe")
    print(f"  3yr  F&D {ed3} / {add3:.1f} = ${fd3:.2f}/Boe")
    print(f"  DD&A {v['dda_og']} / {p25:.1f} = ${dda:.2f}/Boe")
    print(f"  PD life {v['pd'][2025]:.1f} / {p25:.1f} = {life:.2f} yr")
