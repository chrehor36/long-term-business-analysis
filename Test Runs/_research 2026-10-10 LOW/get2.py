import fetch,json
T={"LOW":60667,"HD":354950,"FND":1507079,"TSCO":916365,"WMT":104169,"AMZN":1018724}
for t,c in T.items():
    b=fetch.get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json",f"facts_{t}.json")
    print(t,len(b),flush=True)
