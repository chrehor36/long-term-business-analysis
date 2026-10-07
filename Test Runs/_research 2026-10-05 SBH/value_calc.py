# COMPUTATION - NOT A CLEARANCE. Inputs: XBRL first-filed values (facts_table.txt), cover shares, Treasury 30y.
ocf  ={2016:351.0,2017:344.4,2018:372.7,2019:320.4,2020:426.9,2021:381.9,2022:156.5,2023:249.3,2024:246.5,2025:274.8}
sbc  ={2016:12.6,2017:10.5,2018:10.5,2019:9.2,2020:8.4,2021:11.7,2022:9.9,2023:15.9,2024:17.2,2025:19.2}
capex={2016:148.7,2017:89.7,2018:86.5,2019:107.8,2020:110.9,2021:73.9,2022:99.2,2023:90.7,2024:101.2,2025:102.1}
da   ={2016:99.7,2017:112.3,2018:108.8,2019:107.7,2020:106.8,2021:102.2,2022:99.9,2023:102.4,2024:109.7,2025:99.9}
intr ={2016:144.2,2017:132.9,2018:98.2,2019:96.3,2020:98.8,2021:93.5,2022:93.5,2023:73.0,2024:76.4,2025:64.4}
oe={y:ocf[y]-sbc[y]-capex[y] for y in ocf}; oed={y:ocf[y]-sbc[y]-da[y] for y in ocf}
for y in sorted(oe): print(y, f"OE capex {oe[y]:7.1f}  OE D&A {oed[y]:7.1f}")
m5=sum(oe[y] for y in range(2021,2026))/5; m5d=sum(oed[y] for y in range(2021,2026))/5
m10=sum(oe.values())/10; first5=sum(oe[y] for y in range(2016,2021))/5
print(f"5yr mean capex {m5:.1f} D&A {m5d:.1f}; 10yr mean {m10:.1f}; FY16-20 mean {first5:.1f}")
g_half=(m5/first5)**(1/5)-1
g_end=(oe[2025]/oe[2021])**(1/4)-1
t=0.25; tax=67.539/263.417
ul1=first5+ (sum(intr[y] for y in range(2016,2021))/5)*(1-t); ul2=m5+(sum(intr[y] for y in range(2021,2026))/5)*(1-t)
print(f"growth: endpoint FY21->FY25 {g_end*100:.1f}%/yr (FY21 abnormal base); half-decade means {g_half*100:.1f}%/yr; unlevered half-decade {((ul2/ul1)**0.2-1)*100:.1f}%/yr")
r=0.0566; sh=93.622; price=16.06
def pv(base,g,years=10,r=r):
    v=0; cf=base
    for i in range(1,years+1):
        cf=cf*(1+g); v+=cf/(1+r)**i
    v+= cf/r/(1+r)**years  # zero nominal growth after year 10
    return v
for label,base in [("5yr capex",m5),("5yr D&A",m5d),("10yr whole-cycle",m10)]:
    top=pv(base,0.0); bot=pv(base,g_half)
    print(f"{label:16s} no-growth {top:7.0f}M ${top/sh:6.2f}  shown-decline({g_half*100:.1f}%) {bot:7.0f}M ${bot/sh:6.2f}  ratio {top/bot:.2f}")
# fair price: central case clears 10% pre-tax on equity. pre-tax owner cash = OE/(1-tax)
for g in (0.0,-0.02,g_half):
    pre=m5/(1-tax)
    fair=pre/(0.10-g)
    print(f"tax {tax:.3f}; central g {g*100:.1f}%: pre-tax OE {pre:.1f}M; fair cap {fair:.0f}M = ${fair/sh:.2f}")
pre=m5/(1-tax)
print(f"at ${price}: cap {price*sh:.0f}M; after-tax OE yield {m5/(price*sh)*100:.1f}%; pre-tax {pre/(price*sh)*100:.1f}%")
