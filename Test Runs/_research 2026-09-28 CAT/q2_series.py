import json,sys
sys.stdout.reconfigure(encoding='utf-8')
R={int(k):v for k,v in json.load(open('supbs.json')).items()}
# newest vintage for op profit & sales: doc y+2 col idx0? columns: y,y-1,y-2 per block for docs>=2010; docs<2010: 3 cols too (sales 3 cols)
def ro(y,key,block):  # block 0 cons,1 met,2 fp
    for d in (y+2,y+1,y):
        if d in R and key in R[d]:
            off=d-y
            if off<=2: return R[d][key][block*3+off], d
    return None,None
def bs(y,key,block): # 2 cols per block
    for d in (y+1,y):
        if d in R and key in R[d]:
            off=d-y
            return R[d][key][block*2+off]
PR={2001:-275,2004:512,2005:1827,2006:1464,2007:932,2008:1352,2009:910,2010:954,2011:724,2012:1531,2013:82,2014:365,2015:5,2016:-760,2017:827,2018:601,2019:710,2020:-435,2021:932,2022:5179,2023:5596,2024:1238,2025:-817}
GW={}
IA={2007:475,2008:511,2009:465,2010:805,2011:4368,2012:4016,2013:3596,2014:3076,2015:2821,2016:2349,2017:2111,2018:1897,2019:1565,2020:1308,2021:1042,2022:758,2023:564,2024:399,2025:241}
cap={}
for y in range(2004,2026):
    eq=bs(y,'eq',0); fpeq=bs(y,'eq',2); debt=sum(bs(y,k,1) for k in ['stb','ltd1','ltd2']); cash=bs(y,'cash',1); gw=bs(y,'gw',1)
    cap[y]=(eq-fpeq+debt-cash, gw+IA.get(y,0), eq, fpeq, debt, cash)
print('year | ME&T sales | ME&T op profit | margin | price realization $M | % of prior-year ME&T sales | ME&T operating capital (equity ex FP + ME&T debt - ME&T cash) | pre-tax return on avg capital | on tangible (less goodwill and intangibles) | cons op profit')
for y in range(2005,2026):
    s,ds=ro(y,'sales',0); op,do=ro(y,'oprof',1); cop,_=ro(y,'oprof',0)
    ps,_=ro(y-1,'sales',0)
    c=(cap[y][0]+cap[y-1][0])/2; ct=c-(cap[y][1]+cap[y-1][1])/2
    pr=PR.get(y)
    print(y,'|',s,'|',op,f'(doc {do})','|',f'{op/s*100:.1f}%','|',pr,'|',f'{pr/ps*100:+.1f}%' if pr is not None and ps else '','|',round(cap[y][0]),'|',f'{op/c*100:.1f}%','|',f'{op/ct*100:.1f}%','|',cop)
print()
for y in sorted(cap): print(y,[round(x) for x in cap[y]])

print()
print('ME&T operating profit on ME&T assets less cash less the stake in Financial Products (pre-2020: FP equity; 2020+: the consolidating equity adjustment), average of year-ends; and less goodwill and intangibles')
for y in range(2005,2026):
    op,_=ro(y,'oprof',1)
    def base(z):
        ta=bs(z,'ta',1); cash=bs(z,'cash',1)
        stake=bs(z,'eq',2) if z<2019 else -bs(z,'eq',3)
        return ta-cash-stake
    b=(base(y)+base(y-1))/2; bt=b-(cap[y][1]+cap[y-1][1])/2
    print(y, round(base(y)), f'{op/b*100:.1f}%', f'{op/bt*100:.1f}%')
