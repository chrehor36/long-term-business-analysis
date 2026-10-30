# Owner cash by year, yen billions, from the statements of cash flows in the annual tanshin (TDnet ids in the run file).
# Arithmetic only. FY = the company's fiscal year (FY2025 = year ended 2026-03-31).
import sys
sys.stdout.reconfigure(encoding='utf-8')
D={ # OCF, lease, nci_div, capex, capex_sale, invprop_net, eqm_net, biz_net, oth_net, int_paid, NI_parent, DA
2016:(583.004,0,19.722,160.055,26.924,-8.696+26.893,-139.747+98.475,-74.694+1.365,-117.283+135.994,64.797,440.293,201.117),
2017:(742.482,0,39.834,277.456,178.882,-7.624+9.252,-359.511+77.627,-32.264+25.201,-46.090+127.883,65.212,560.173,254.038),
2018:(652.681,56.017,53.800,315.514,96.934,-2.307+5.341,-398.191+111.556,-31.386+116.368,-62.481+143.528,82.331,590.737,250.509),
2019:(849.728,276.175,41.540,326.014,40.645,-0.229+4.091,-201.731+111.637,-319.364+89.333,-39.517+129.293,94.833,535.353,448.413),
2020:(1017.550,277.531,40.866,388.981,47.753,-0.425+1.344,-253.316+129.938,0.502+28.407,-43.009+187.756,67.731,172.550,523.830),
2021:(1055.844,279.784,54.047,393.833,27.888,-0.443+1.329,-157.003+246.455,-45.154+53.278,-26.990+142.987,64.444,937.529,545.043),
2022:(1930.138,308.946,56.348,454.954,20.276,-0.611+0.395,-181.025+284.129,-25.734+173.362,-62.425+116.835,134.224,1180.694,583.294),
2023:(1347.380,300.086,84.771,520.542,26.099,-1.296+65.738,-255.141+349.160,-12.715-15.852,-66.483+137.642,212.823,964.034,599.330),
2024:(1658.349,204.878,66.012,384.292,205.739,-1.285+0.209,-214.089+254.754,-15.343-343.222+408.756,-325.148+231.339,167.261,950.709,470.768),
2025:(1490.041,116.100,57.707,352.947,53.850,-5.240+0.314,-292.796+188.657,-73.080+17.133,-226.122+220.499,157.161,800.460,397.777),
}
T=0.3062 # CONVENTION of this run: Japan's effective statutory rate, used only to put interest after tax
rows={}
print('FY   OCF   lease  NCIdiv capexN  OC_before_purch  purch_net  OC_after_purch  +int(after tax) OCbp_allEq OCap_allEq  NI_parent')
for y,(ocf,ls,nci,cx,cxs,ip,eq,bz,ot,ip_,ni,da) in D.items():
    capn=cx-cxs-ip
    before=ocf-ls-nci-capn
    purch=-(eq+bz+ot)   # positive = net cash spent on businesses and investments
    after=before-purch
    addi=ip_*(1-T)
    rows[y]=(before,after,before+addi,after+addi,ni,cx,da,purch)
    print(y,f"{ocf:7.1f}{ls:7.1f}{nci:7.1f}{capn:7.1f}{before:12.1f}{purch:12.1f}{after:12.1f}{addi:12.1f}{before+addi:12.1f}{after+addi:12.1f}{ni:10.1f}")
def avg(ys,i): return sum(rows[y][i] for y in ys)/len(ys)
W=[2021,2022,2023,2024,2025]; C1=[2016,2017,2018,2019,2020]
for name,ys in (('window FY2021-25',W),('cycle FY2016-20',C1),('ten years FY2016-25',C1+W)):
    print(name,'avg before-purch %.1f after-purch %.1f | all-equity before %.1f after %.1f | NI %.1f | purch %.1f'%(avg(ys,0),avg(ys,1),avg(ys,2),avg(ys,3),avg(ys,4),avg(ys,7)))
