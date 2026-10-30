import urllib.request, os, json, time
UA = {"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
OUT = "Test Runs/_research 2026-09-12 ALKT"
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        except Exception as e: print("retry", i, u, e); time.sleep(3)
    raise SystemExit("failed "+u)
b = get("https://data.sec.gov/api/xbrl/companyfacts/CIK0001529274.json")
open(os.path.join(OUT,"companyfacts.json"),"wb").write(b); print("companyfacts", len(b))
for acc,tag in [("0000950142-26-000686","13DA_20260311"),("0000902664-26-001830","13D_20260401"),("0000950142-26-001331","13DA_20260507"),("0000902664-26-002393","13DA_20260512"),("0000950142-26-001426","13DA_20260515"),("0000902664-26-002944","13D_20260629"),("0000950142-25-002245","13D_20250820"),("0001214659-26-010345","13GA_20260814")]:
    a=acc.replace("-","")
    try:
        j=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/1529274/{a}/index.json")); time.sleep(0.3)
        names=[x["name"] for x in j["directory"]["item"]]
        print(tag, names)
        for n in names:
            if n.endswith(".xml") or (n.endswith(".htm") and "index" not in n):
                bb=get(f"https://www.sec.gov/Archives/edgar/data/1529274/{a}/{n}"); open(os.path.join(OUT,f"{tag}__{n}"),"wb").write(bb); print(" ",n,len(bb)); time.sleep(0.3)
    except SystemExit as e: print(e)
