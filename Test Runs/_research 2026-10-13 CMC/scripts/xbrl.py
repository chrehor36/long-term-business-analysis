"""Annual values from XBRL companyfacts. Transcription only; check against filed statements."""
import json, sys, os
from datetime import date
BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
def load(cik):
    return json.load(open(os.path.join(BASE, f"facts_{cik}.json")))
def annual(facts, tag, ns="us-gaap", unit=None, instant=False, latest=True, forms=("10-K","10-K/A","20-F","20-F/A")):
    try:
        t = facts["facts"][ns][tag]["units"]
    except KeyError:
        return {}
    u = unit or list(t.keys())[0]
    out = {}
    for f in t.get(u, []):
        if f.get("form") not in forms: continue
        end = f["end"]
        if not instant:
            if "start" not in f: continue
            d = (date.fromisoformat(end) - date.fromisoformat(f["start"])).days
            if d < 350 or d > 380: continue
        key = end
        prev = out.get(key)
        if prev is None or (latest and f["filed"] > prev[1]) or (not latest and f["filed"] < prev[1]):
            out[key] = (f["val"], f["filed"], f.get("accn"))
    return {k: v[0] for k, v in sorted(out.items())}
def first(facts, tags, **kw):
    res = {}
    for tg in tags:
        a = annual(facts, tg, **kw)
        for k, v in a.items():
            res.setdefault(k, v)
    return dict(sorted(res.items()))
