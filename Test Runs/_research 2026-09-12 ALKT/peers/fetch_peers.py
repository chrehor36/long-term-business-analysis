import urllib.request, json, time, os
UA = {"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        except Exception as e: print("retry",i,u,e); time.sleep(3)
    raise SystemExit("fail "+u)
tk=json.loads(get("https://www.sec.gov/files/company_tickers.json"))
want={"QTWO":None,"JKHY":None,"FISV":None,"FI":None,"NCNO":None,"VYX":None,"MLNK":None,"BLND":None,"FIS":None}
for v in tk.values():
    if v["ticker"] in want: want[v["ticker"]]=str(v["cik_str"]).zfill(10)
print(want)
for t,c in want.items():
    if not c: continue
    sub=json.loads(get(f"https://data.sec.gov/submissions/CIK{c}.json")); time.sleep(0.3)
    r=sub["filings"]["recent"]
    ks=[(f,d,rd,a,p) for f,d,rd,a,p in zip(r["form"],r["filingDate"],r["reportDate"],r["accessionNumber"],r["primaryDocument"]) if f in("10-K","10-Q")][:3]
    print(t, sub["name"], ks)
    k=[x for x in ks if x[0]=="10-K"]
    if k and t in ("QTWO","JKHY","FISV","FI","NCNO"):
        f,d,rd,a,p=k[0]
        fn=f"{t}_10K_{rd}.htm"
        if not os.path.exists(fn):
            b=get(f"https://www.sec.gov/Archives/edgar/data/{int(c)}/{a.replace('-','')}/{p}"); open(fn,"wb").write(b); print("  saved",fn,len(b)); time.sleep(0.4)
        cf=f"{t}_companyfacts.json"
        if not os.path.exists(cf):
            open(cf,"wb").write(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json")); time.sleep(0.4)
