import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pf, sources
tm = json.loads(sources.ticker_map()) if isinstance(sources.ticker_map(), str) else sources.ticker_map()
for tk in ["TECK", "BHP", "CRN", "CODQL", "GLNCY", "NGLOY"]:
    try:
        print(tk, sources.cik_for(tk))
    except Exception as e:
        print(tk, "not in SEC ticker map:", e)
# Coronado by name
vals = tm.values() if isinstance(tm, dict) else tm
for v in vals:
    s = json.dumps(v)
    if "CORONADO" in s.upper() or "WHITEHAVEN" in s.upper() or "GLENCORE" in s.upper() or "ANGLO AMERICAN" in s.upper():
        print(s)
