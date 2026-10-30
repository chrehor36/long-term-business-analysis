# COMPUTATION, NOT A CLEARANCE: Q7 range arithmetic for the SKK/RNTZ run (US$000 unless stated)
ocf  ={2021:4208,2022:1757,2023:194,2024:3330,2025:-512}
sbc  ={2021:0,2022:0,2023:0,2024:0,2025:2399}
capex={2021:1480,2022:1170,2023:3042,2024:7814,2025:5136}
disp ={2021:0,2022:303,2023:703,2024:184,2025:684}
flp  ={2021:255,2022:744,2023:580,2024:361,2025:927}
da   ={2021:1093+62,2022:1142+58,2023:1208+91+3,2024:1373+89+13,2025:1493+91+1}
intr ={2021:188,2022:154,2023:221,2024:334,2025:481}
t=0.17  # Singapore statutory corporate rate, for the after-tax interest add-back
yrs=sorted(ocf)
allsp={y:ocf[y]-sbc[y]-capex[y]+disp[y]-flp[y] for y in yrs}
dep  ={y:ocf[y]-sbc[y]-da[y] for y in yrs}
unl  =lambda s:{y:s[y]+intr[y]*(1-t) for y in yrs}
avg  =lambda s:sum(s.values())/len(s)
for n,s in [('all spending, equity',allsp),('depreciation variant, equity',dep),('all spending, all-equity',unl(allsp)),('depreciation variant, all-equity',unl(dep))]:
    print(f'{n:34s}', ' '.join(f'{s[y]:7.0f}' for y in yrs), f' avg {avg(s):7.0f}')
netdebt=1955+6972+647+1750-732-81
print('net debt 2025-12-31', netdebt, ' related-party payable beside 6995; operating leases left out 580')
shares=60336487; price=4.53
ev=shares*price/1000+netdebt
top=avg(unl(dep))
print('EV at price $000', round(ev), ' best-case yield %', round(100*top/ev,3))
for r,lab in [(0.0241,'SGS 30y 2.41%'),(0.0543,'UST 30y 5.43%'),(0.10,'floor 10%')]:
    v=top/r  # zero growth for ten years and after: a level perpetuity
    eq=v-netdebt
    print(f'{lab:14s} top case whole-business {v:8.0f}  less net debt {eq:8.0f}  per share ${max(eq,0)*1000/shares:.4f}')
later=202+3434-759
v=top/0.0241-netdebt+later
print('with later-filed cash items (ATM 202, RDO 3434, cash paid at closing -759), before the 7,700 transaction costs:', round(v), f'${v*1000/shares:.4f} a share')
print('same, after the 7,700 estimated transaction costs:', round(v-7700))
print('revenue growth 2021-2025 %/yr', round(100*((12949/11917)**0.25-1),2))
