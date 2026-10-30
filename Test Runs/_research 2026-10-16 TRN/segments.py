# Segment table, transcribed from the segment notes and Leasing Group discussions (USD millions).
# FY2016-2017: 10-K FY2018 (0000099780-19-000019, recast to continuing operations); FY2018-2020: 10-K FY2020
# (0000099780-21-000012); FY2021-2022: 10-K FY2022 (0000099780-23-000013); FY2023: 10-K FY2025 recast (0000099780-26-000014;
# segments recast 2024 to move maintenance services into Leasing); FY2024-2025: 10-K FY2025. Segment assets: leasing segment
# total assets less 'Eliminations - Lease subsidiary' (2023 and 2024-25: less the whole eliminations line as filed).
lease_op={2016:360.1,2017:444.5,2018:351.1,2019:406.6,2020:353.7,2021:350.9,2022:423.3,2023:437.5,2024:464.0,2025:708.4}
one_off={2025:194.2}                       # Triumph divestiture gain, non-cash
sale_gain={2016:47.6,2017:103.2,2018:71.9,2019:91.9,2020:17.7,2021:54.1,2022:127.5,2023:82.8,2024:57.3,2025:91.4}
lm_op={2016:312.5,2017:341.3,2018:291.8,2019:314.7,2020:336.0,2021:296.8,2022:295.8}
rail_op={2016:449.4,2017:196.3,2018:167.6,2019:277.6,2020:36.3,2021:4.7,2022:59.1,2023:112.6,2024:189.4,2025:74.3}
rail_rev={2016:3027.8,2017:2044.0,2018:2412.9,2019:2974.8,2020:1609.5,2021:1264.8,2022:2074.7,2023:2479.4,2024:2431.1,2025:1419.5}
elim={2016:-180.7,2017:-96.5,2018:-95.1,2019:-164.7,2020:-35.2,2021:-17.2,2022:-65.2,2023:-27.0,2024:-31.9,2025:-21.9}
lease_assets={2017:6267.9-800.7,2018:7096.0-827.7,2019:8012.6-903.8,2020:6831.8,2021:7585.4-779.1,2022:7016.6,2023:7895.7-750.2,2024:8151.7-670.5,2025:7676.5-575.1}
impair={2020:396.4}
print('FY   lease_op  ex-one-off  sale_gain  L&M_op  lease_assets  pretax_on_assets  with_impairment | rail_op rail_margin')
r1=[];r2=[]
for y in range(2016,2026):
    lo=lease_op[y]-one_off.get(y,0)
    a=lease_assets.get(y)
    s=f'{y} {lease_op[y]:8.1f} {lo:9.1f} {sale_gain[y]:9.1f} {lm_op.get(y,float("nan")):7.1f}'
    if a:
        x=lo/a; z=(lo-impair.get(y,0))/a; r1.append(x); r2.append(z)
        s+=f' {a:10.1f} {x*100:9.1f}% {z*100:9.1f}%'
    else: s+=' '*34
    s+=f' | {rail_op[y]:6.1f} {rail_op[y]/rail_rev[y]*100:5.1f}%'
    print(s)
print(f'mean pre-tax on leasing assets FY2017-2025: {sum(r1)/len(r1)*100:.1f}% ; with the FY2020 impairment charged: {sum(r2)/len(r2)*100:.1f}%')
print(f'after 21% tax: {sum(r1)/len(r1)*79:.1f}% ; {sum(r2)/len(r2)*79:.1f}%')
print(f'mean Rail Products margin FY2016-2025: {sum(rail_op[y]/rail_rev[y] for y in rail_op)/10*100:.1f}%')
L5=sum(lease_op[y] for y in range(2021,2026)); R5=sum(rail_op[y] for y in range(2021,2026))
print(f'five-year segment operating profit FY2021-2025: Leasing {L5:.1f} ({L5/(L5+R5)*100:.0f}%), Rail Products {R5:.1f} ({R5/(L5+R5)*100:.0f}%); Leasing ex Triumph gain {L5-194.2:.1f} ({(L5-194.2)/(L5-194.2+R5)*100:.0f}%)')
