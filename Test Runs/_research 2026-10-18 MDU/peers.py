# Return on equity and on assets, FY2017-2025, from the filers' own 10-K XBRL facts (companyfacts, earliest-filed value)
import json
from datetime import date
def ann(f,tag):
    out={}
    for x in f["facts"]["us-gaap"].get(tag,{}).get("units",{}).get("USD",[]):
        if x.get("form")!="10-K" or not x["end"].endswith("12-31"): continue
        if "start" in x and not 340<(date.fromisoformat(x["end"])-date.fromisoformat(x["start"])).days<380: continue
        k=int(x["end"][:4])
        if k not in out or x["filed"]<out[k][1]: out[k]=(x["val"]/1e6,x["filed"],x["accn"])
    return out
P={"BKH":["0001130464"],"AVA":["0000104918"],"NWE":["0000073088","0001993004"]}
res={}
for n,cs in P.items():
    ni,eq,ta={},{},{}
    for c in cs:
        f=json.load(open(f"cache/CIK{c}.json"))
        for d,t in ((ni,"NetIncomeLoss"),(eq,"StockholdersEquity"),(ta,"Assets")):
            for k,v in ann(f,t).items(): d.setdefault(k,v)
    roe={y:ni[y][0]/((eq[y][0]+eq[y-1][0])/2) for y in range(2017,2026)}
    roa={y:ni[y][0]/((ta[y][0]+ta[y-1][0])/2) for y in range(2017,2026)}
    res[n]=(roe,roa)
    print(n,"ROE",{y:round(100*v,1) for y,v in roe.items()},"avg %.1f"%(100*sum(roe.values())/9))
    print(n,"ROA",{y:round(100*v,2) for y,v in roa.items()},"avg %.2f"%(100*sum(roa.values())/9))
# MDU three utility segments: segment net income over year-end segment assets (10-K segment notes)
ni={2017:49.366+32.225+20.620,2018:47.000+37.732+26.905,2019:54.763+39.517+28.255,2020:55.601+44.049+35.453+1.559,
    2021:51.906+51.596+39.583+1.313,2022:57.077+45.171+36.253-0.059,2023:71.559+48.520+47.375,2024:74.793+46.937+68.042,2025:64.896+56.052+68.178}
assets={2016:None,2017:1470.922+2201.081+566.295,2018:1613.822+2375.871+616.959,2019:1680.194+2574.965+677.482,
    2020:2123.693+2302.770+703.377,2021:1810.695+2929.519+913.945,2022:1856.258+3214.452+961.893,
    2023:1955.644+3532.142+1045.704,2024:1976.912+3730.532+1151.317,2025:2367.067+3909.046+1196.959}
roa={y:ni[y]/((assets[y]+assets[y-1])/2) for y in range(2018,2026)}
print("MDU utility segments NI/avg segment assets",{y:round(100*v,2) for y,v in roa.items()},"avg %.2f"%(100*sum(roa.values())/len(roa)))
gas={2017:32.225/2201.081,2025:56.052/3909.046}
print("MDU gas distribution NI/segment assets 2017 %.2f%% 2025 %.2f%%"%(100*gas[2017],100*gas[2025]))
print("MDU consolidated ROE 2025 (pure utility): %.1f%%"%(100*191.407/((2690.574+2772.917)/2)))
