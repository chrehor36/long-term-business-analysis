import sys, json, os
sys.path.insert(0, r"C:/Projects/BRK/tools")
import sources as S
out = {}
px, d, c = S.price("PCG"); out["price"] = (px, d, c)
try:
    out["sov"] = S.sovereign("USD")
except Exception as e:
    out["sov"] = repr(e)
for t in ["EIX", "SRE", "XEL"]:
    try: out["px_"+t] = S.price(t)
    except Exception as e: out["px_"+t] = repr(e)
print(json.dumps(out, default=str, indent=1))
facts = S.sec_facts(1004980)
json.dump(facts, open(r"C:/Projects/BRK/Test Runs/_research 2026-10-26 PCG/cache/pcg_facts.json","w"))
print(len(facts["facts"]["us-gaap"]))
