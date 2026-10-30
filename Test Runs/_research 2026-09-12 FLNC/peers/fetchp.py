import sys, os, re, html, urllib.request, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools")); sys.path.insert(0, "Test Runs/_research 2026-09-12 FLNC")
import sources
from fetch import totext
OUT = "Test Runs/_research 2026-09-12 FLNC/peers"
def grab(cik, acc, doc, name):
    p = os.path.join(OUT, name + ".txt")
    if os.path.exists(p): print("have", name); return
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=sources.SEC_UA), timeout=120).read().decode("utf-8","replace")
    open(p,"w",encoding="utf-8").write(totext(raw)); print(name, "ok"); time.sleep(0.5)
for a in [("1318605","0001628280-26-003952","tsla-20251231.htm","peer_TSLA_tenk_2025"),
          ("1318605","0001628280-26-049270","tsla-20260630.htm","peer_TSLA_tenq_2026-06"),
          ("1805077","0001628280-26-011961","eose-20251231.htm","peer_EOSE_tenk_2025"),
          ("1758766","0001758766-26-000016","stem-20251231.htm","peer_STEM_tenk_2025"),
          ("1819438","0001819438-26-000012","ghw-20251231.htm","peer_GWH_tenk_2025"),
          ("874761","0000874761-26-000063","aes-20251231.htm","peer_AES_tenk_2025"),
          ("1474735","0001437749-26-004568","gnrc20251231_10k.htm","peer_GNRC_tenk_2025")]:
    try: grab(*a)
    except Exception as e: print("FAIL", a[-1], e)
