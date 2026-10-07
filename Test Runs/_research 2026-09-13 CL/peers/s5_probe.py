"""Probe companyfacts tags for gaps found by s5_xbrl.py."""
import sys, re
from p_common import jload
sys.stdout.reconfigure(encoding="utf-8")
t, pat = sys.argv[1], re.compile(sys.argv[2], re.I)
endpat = sys.argv[3] if len(sys.argv) > 3 else ""
cf = jload(f"{t}_companyfacts.json")["facts"]
for ns in cf:
    for tag, v in cf[ns].items():
        if not pat.search(tag):
            continue
        for u, fs in v["units"].items():
            fs = [f for f in fs if f.get("form") == "10-K" and f["end"] >= "2020-01-01" and endpat in f["end"]]
            if fs:
                print(ns, tag, u, len(fs))
                for f in fs[-12:]:
                    print("   ", f.get("start"), f["end"], f["val"], f["accn"], f["fy"], f["fp"], f.get("frame"))
