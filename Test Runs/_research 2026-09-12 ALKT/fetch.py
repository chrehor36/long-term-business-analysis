import urllib.request, os, sys, json, time, re
UA = {"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
OUT = "Test Runs/_research 2026-09-12 ALKT"
CIK = "1529274"
def get(u):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        except Exception as e:
            print("retry", i, u, e); time.sleep(3)
    raise SystemExit("failed "+u)
def index(acc):
    a = acc.replace("-","")
    j = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json"))
    time.sleep(0.3)
    return [x["name"] for x in j["directory"]["item"]]
def doc(acc, name, out):
    if os.path.exists(os.path.join(OUT,out)): print("have", out); return
    a = acc.replace("-","")
    b = get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{name}")
    open(os.path.join(OUT,out),"wb").write(b); print(out, len(b)); time.sleep(0.35)
primary = [
 ("0001529274-26-000009","alk-20251231.htm","10K_FY2025.htm"),
 ("0001529274-25-000031","alk-20241231.htm","10K_FY2024.htm"),
 ("0001529274-24-000029","alk-20231231.htm","10K_FY2023.htm"),
 ("0001529274-23-000037","alk-20221231.htm","10K_FY2022.htm"),
 ("0001529274-22-000034","alk-20211231.htm","10K_FY2021.htm"),
 ("0001529274-26-000052","alk-20260630.htm","10Q_2026Q2.htm"),
 ("0001529274-26-000032","alk-20260331.htm","10Q_2026Q1.htm"),
 ("0001529274-25-000162","alk-20250930.htm","10Q_2025Q3.htm"),
 ("0001529274-26-000023","alk-20260407.htm","DEF14A_2026.htm"),
]
for a,n,o in primary: doc(a,n,o)
# 8-Ks with exhibits
eightks = {
 "0001529274-26-000036":"8K_20260501_item101",
 "0001529274-26-000049":"8K_20260729_Q2",
 "0001529274-26-000028":"8K_20260423_Q1",
 "0001529274-26-000005":"8K_20260225_Q4",
 "0001529274-25-000159":"8K_20251029_Q3",
 "0001529274-26-000014":"8K_20260331_502",
 "0001529274-26-000043":"8K_20260519_507",
 "0001529274-25-000040":"8K_20250310_mantl_agmt",
 "0001529274-25-000044":"8K_20250317_mantl_close",
 "0001529274-25-000028":"8K_20250227_Q4_101",
 "0001529274-22-000067":"8K_20220425_segmint_close",
 "0001529274-21-000057":"8K_20210910_mkd",
}
for acc, tag in eightks.items():
    names = index(acc)
    print(tag, names)
    for n in names:
        if re.search(r"\.(htm|html|txt)$", n) and not n.endswith("-index.htm") and not n.endswith("-index-headers.html") and "R" not in n[:1]:
            if n.endswith(".txt") and acc.replace("-","") in n.replace("-",""): continue
            doc(acc, n, f"{tag}__{n}")
