import json, time, os, re, html
import requests
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
os.makedirs("cache", exist_ok=True)
def get(url):
    for i in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=90); r.raise_for_status(); return r
        except Exception as e:
            print("retry", url, e); time.sleep(2)
    raise RuntimeError(url)
def strip(h):
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)</(p|div|tr|li|h\d|table|br)\s*>", "\n", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</t[dh]\s*>", " | ", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    h = h.replace("\xa0"," ")
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h
def doc(cik, acc, primary, name):
    accn = acc.replace("-","")
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}/{primary}"
    raw = f"cache/{name}.htm"
    if not os.path.exists(raw):
        r = get(url); open(raw,"w",encoding="utf-8").write(r.text); time.sleep(0.3)
    txt = strip(open(raw,encoding="utf-8").read())
    open(f"{name}.txt","w",encoding="utf-8").write(txt)
    print(name, len(txt))
def index(cik, acc):
    accn = acc.replace("-","")
    r = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}/index.json"); time.sleep(0.3)
    return [it["name"] for it in r.json()["directory"]["item"]]
C=909832
doc(C,"0000909832-25-000101","cost-20250831.htm","COST_10K_FY2025")
doc(C,"0000909832-26-000051","cost-20260510.htm","COST_10Q_Q3FY2026")
doc(C,"0000909832-25-000159","cost-20251204.htm","COST_DEF14A_2025")
# older 10-Ks for the span
sub=json.load(open("edgar/COST_sub.json"))["filings"]["recent"]
for form,dt,acc,prim in zip(sub["form"],sub["filingDate"],sub["accessionNumber"],sub["primaryDocument"]):
    if form=="10-K" and dt[:4] in ("2016","2019","2022"):
        doc(C,acc,prim,f"COST_10K_filed{dt[:4]}")
# 8-Ks with exhibits
for acc in ["0000909832-26-000084","0000909832-26-000060","0000909832-26-000016","0000909832-25-000164"]:
    items = index(C, acc)
    print(acc, items)
    for it in items:
        if it.lower().endswith(".htm") and ("ex99" in it.lower() or "ex-99" in it.lower() or it.startswith("cost-")):
            doc(C, acc, it, f"COST_8K_{acc[-6:]}_{it.replace('.htm','')}")
# competitors' latest 10-K
comp = {"WMT":(104169,"0000104169-26-000055","wmt-20260131.htm"),
        "BJ":(1531152,"0001531152-26-000007","bj-20260131.htm"),
        "TGT":(27419,"0000027419-26-000016","tgt-20260131.htm"),
        "KR":(56873,"0001104659-26-037723","kr-20260131x10k.htm"),
        "AMZN":(1018724,"0001018724-26-000004","amzn-20251231.htm"),
        "PSMT":(1041803,"0001041803-25-000060","psmt-20250831.htm")}
os.makedirs("peers", exist_ok=True)
for t,(cik,acc,prim) in comp.items():
    doc(cik,acc,prim,f"peers/{t}_10K_latest")
