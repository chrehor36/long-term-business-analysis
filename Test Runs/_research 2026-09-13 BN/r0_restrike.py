import sys, json, urllib.request, gzip
sys.path.insert(0, "tools")
import sources as S
print("SOVEREIGN", S.sovereign("USD"))
for t in ["BN", "BNT", "BAM", "BIP", "BEP", "BBUC"]:
    try:
        print("PRICE", t, S.price(t))
    except Exception as e:
        print("PRICE", t, "ERR", e)
print("SPLIT BN after 2026-08-13", S.split_factor_after("BN", "2026-08-13"))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
r = urllib.request.urlopen(urllib.request.Request("https://data.sec.gov/submissions/CIK0001001085.json", headers=UA), timeout=60)
b = r.read()
if r.headers.get("Content-Encoding") == "gzip":
    b = gzip.decompress(b)
d = json.loads(b)
rec = d["filings"]["recent"]
for i in range(len(rec["form"])):
    if rec["filingDate"][i] >= "2026-08-10":
        print("FILING", rec["filingDate"][i], rec["form"][i], rec["accessionNumber"][i], rec["primaryDocument"][i], rec.get("primaryDocDescription", [""]*999)[i])
