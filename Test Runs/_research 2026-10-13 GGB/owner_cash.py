# Owner cash for GGB from the filed consolidated cash flow statements (R$ thousands).
# Sources: 20-F FY2025 (acc 0001104659-26-027678) for 2023-25; FY2023 (0001104659-24-040516) for 2021-22;
# FY2021 (0001104659-22-041058) for 2019-20; FY2019 (0001104659-20-041231) for 2017-18; FY2017 (0001104659-18-022121) for 2015-16.
T = 0.34  # Brazilian statutory IRPJ+CSLL rate, used only for the interest shield (CONVENTION of this run)
cols = "cfo purch proc intpd leaseint tax capex intang procsale acq leaseprin intinc da rev".split()
D = {
2015:(7162318,1958522,3929971,946041,0,637394,2324718,126428,90942,61453,0,153631,2607909,43581241),
2016:(3516366,880436,1089972,1240165,0,168032,1323891,54044,308694,0,0,107980,2535955,37651667),
2017:(2076128,2390104,2905411,1330116,0,126023,873329,37939,554457,178670,0,75387,2092551,36917619),
2018:(1999683,1512123,1629595,1162364,0,298663,1194934,67388,4021251,375456,0,49745,1891814,46159478),
2019:(1642792,3676744,521616,945027,83620,254679,1746600,100313,21805,74343,161824,72784,2074295,39644010),
2020:(6407906,3224158,3924799,1079981,61727,621033,1650778,154250,61275,485324,247914,99359,2499104,43814661),
2021:(12516933,3010084,3595212,1100826,68789,2893120,3026023,166310,82635,-113595,275854,170671,2658561,78345081),
2022:(11150338,3588529,3434859,968851,88370,3355643,4291873,189382,48322,72904,310226,309782,2866699,82412210),
2023:(11138710,7223644,7908990,858301,127787,1560137,5209128,127195,40661,477179,388202,481624,3047212,68916447),
2024:(11381243,924686,3020432,946936,129137,1399513,5778381,168036,1559697,647630,459504,274291,3126247,67026656),
2025:(7987454,362906,616006,1461147,122321,1121328,6681620,171221,69729,790554,487784,166307,3683585,69858532),
}
LTIP={2015:48589,2016:46683,2017:35576,2018:41186,2019:43895,2020:62801,2021:65289,2022:104714,2023:157979,2024:152414,2025:149210}  # stock pay added back in CFO; deducted here
rows = {}
for y, v in D.items():
    d = dict(zip(cols, v))
    cfo_x = d["cfo"] + d["purch"] - d["proc"] - LTIP[y]  # securities taken out of operating cash; stock pay charged
    oc_eq = cfo_x - d["capex"] - d["intang"] - d["leaseprin"]   # equity basis, before purchases of businesses
    oc_eq_dep = cfo_x - d["da"] - d["leaseprin"]         # depreciation variant
    shield = (d["intpd"] - d["intinc"]) * (1 - T)
    oc_un = oc_eq + shield                               # all-equity basis
    netacq = d["acq"] - d["procsale"]                    # purchases of businesses net of disposals (proceeds incl. PP&E sales)
    rows[y] = dict(cfo_x=cfo_x, oc_eq=oc_eq, oc_un=oc_un, oc_eq_dep=oc_eq_dep, netacq=netacq,
                   capex=d["capex"]+d["intang"], da=d["da"], rev=d["rev"])
    print(f"{y} CFOx {cfo_x/1e3:9,.0f} capex {(d['capex']+d['intang'])/1e3:7,.0f} D&A {d['da']/1e3:6,.0f} "
          f"OCeq {oc_eq/1e3:8,.0f} OCun {oc_un/1e3:8,.0f} OCeq_dep {oc_eq_dep/1e3:8,.0f} netacq {netacq/1e3:7,.0f} "
          f"rev {d['rev']/1e3:8,.0f} OCun/rev {100*oc_un/d['rev']:5.1f}%")
import json; json.dump(rows, open("owner_cash.json","w"), indent=1)
for a,b in [(2021,2025),(2016,2020),(2015,2019),(2017,2021),(2018,2022)]:
    ys=range(a,b+1)
    print(a,b,"avg OCeq %.0f OCun %.0f netacq %.0f rev %.0f" % tuple(sum(rows[y][k] for y in ys)/len(ys)/1e3 for k in ["oc_eq","oc_un","netacq","rev"]))
