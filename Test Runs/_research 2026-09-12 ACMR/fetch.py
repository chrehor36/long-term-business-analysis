import urllib.request, os, sys, json, time
UA = {"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
OUT = "Test Runs/_research 2026-09-12 ACMR"
CIK = "1680062"
def get(u):
    for i in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        except Exception as e:
            print("retry", i, e); time.sleep(3)
    raise SystemExit("failed "+u)
def doc(acc, name, out):
    a = acc.replace("-","")
    u = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{name}"
    b = get(u)
    open(os.path.join(OUT,out),"wb").write(b)
    print(out, len(b))
    time.sleep(0.4)
jobs = [
 ("0001628280-26-013231","acmr-20251231.htm","10K_FY2025.htm"),
 ("0001628280-26-054832","acmr-20260630.htm","10Q_2026Q2.htm"),
 ("0001628280-26-032842","acmr-20260331.htm","10Q_2026Q1.htm"),
 ("0001628280-25-050152","acmr-20250930.htm","10Q_2025Q3.htm"),
 ("0001680062-25-000003","acmr-20241231.htm","10K_FY2024.htm"),
 ("0001680062-24-000008","acmr-20231231.htm","10K_FY2023.htm"),
 ("0001140361-23-009508","brhc10048521_10k.htm","10K_FY2022.htm"),
 ("0001628280-26-027358","acmr-2026proxystatements.htm","DEF14A_2026.htm"),
]
for a,n,o in jobs:
    doc(a,n,o)
