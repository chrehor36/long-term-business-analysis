import json, datetime
g = json.load(open("companyfacts.json", encoding="utf-8"))["facts"]["us-gaap"]
def inst(tag):
    d = {}
    for x in g.get(tag, {}).get("units", {}).get("USD", []):
        if x.get("form") == "10-K" and "start" not in x and x["end"][5:] == "12-31": d.setdefault(x["end"][:4], x["val"]/1e6)
    return d
def dur(tag):
    d = {}
    for x in g.get(tag, {}).get("units", {}).get("USD", []):
        if x.get("form") == "10-K" and "start" in x and 340 < (datetime.date.fromisoformat(x["end"])-datetime.date.fromisoformat(x["start"])).days < 380: d.setdefault(x["end"][:4], x["val"]/1e6)
    return d
se = inst("StockholdersEquity"); pref = inst("PreferredStockValue"); ni = dur("NetIncomeLossAvailableToCommonStockholdersBasic")
print("SE", {k: round(v) for k, v in sorted(se.items()) if k >= "2014"}); print("pref", {k: round(v) for k, v in sorted(pref.items())}); print("NI common", {k: round(v,1) for k, v in sorted(ni.items()) if k >= "2015"})
gains = {2015:94.6,2016:169.9,2017:40.4,2018:80.0,2019:335.1,2020:316.9,2021:1380.8,2022:176.8,2023:900.5,2024:595.8,2025:995.6}
prefv = {"2014":1134.4,"2015":1134.4,"2016":1249.6}   # filled from BS where tag missing; see note
for y in range(2016, 2026):
    k, p = str(y), str(y-1)
    ce = lambda z: se.get(z, float("nan")) - pref.get(z, prefv.get(z, 0))
    avg = (ce(k) + ce(p)) / 2
    print(y, "ROE common", f"{ni.get(k,float('nan'))/avg*100:.1f}%", "ex-gains", f"{(ni.get(k,float('nan'))-gains[y])/avg*100:.1f}%", "avg common equity", round(avg))
# dividends vs issuance FY2015-25
div = {2015:548.1,2016:605.4,2017:715.2,2018:930.8,2019:996.8,2020:1239.3,2021:1379.2,2022:1450.6,2023:1520.6,2024:1633.2,2025:1728.5}
iss = {2015:918.9,2016:1085.4,2017:405.4,2018:-3.9,2019:535.6,2020:1880.0,2021:172.1,2022:928.4,2023:2207.3,2024:3650.8,2025:1106.0}
red = {2016:287.5,2017:182.5,2019:365.1,2020:500.0,2021:201.3}
print("dividends+distributions FY2015-25", round(sum(div.values())), "cash equity raised (common+pref, net)", round(sum(iss.values())), "pref redeemed", round(sum(red.values())))
print("FY2021-25 div", round(sum(div[y] for y in range(2021,2026))), "issued", round(sum(iss[y] for y in range(2021,2026))))
