"""Field returns over the cycle: operating income, margin, and operating income on (total assets less cash),
from each filer's own 10-K XBRL facts (first-filed vintage). Transcription and arithmetic only."""
import sys
sys.path.insert(0, ".")
from xbrl import annual
from inst import inst
cos = {"RAIL": "cache/cf_0001320854.json", "TRN": "cache/cf_0000099780.json", "GBX": "cache/cf_0000923120.json"}
for name, p in cos.items():
    rev = annual(p, "Revenues"); oi = annual(p, "OperatingIncomeLoss"); a = inst(p, "Assets")
    c = inst(p, "CashAndCashEquivalentsAtCarryingValue")
    c2 = inst(p, "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents")
    print(name)
    rs = []
    for e in sorted(oi):
        if e < "2015": continue
        cash = (c.get(e) or c2.get(e) or (0,))[0]
        if rev.get(e) is None: continue
        A = a.get(e, (None,))[0]; R = rev.get(e, (None,))[0]; O = oi[e][0]
        cap = A - cash if A else None
        roc = O / cap * 100 if cap else None
        m = O / R * 100 if R else None
        rs.append((e, roc, m))
        print(f"  {e} rev {R/1e6 if R else float('nan'):8.1f} opinc {O/1e6:7.1f} margin {m if m is not None else float('nan'):6.1f}% "
              f"assets-cash {cap/1e6 if cap else float('nan'):8.1f} return {roc if roc is not None else float('nan'):6.1f}%  [{oi[e][2]}]")
    for lo, hi in (("2015", "2024"), ("2016", "2025")):
        sel = [r for r in rs if lo <= r[0][:4] <= hi and r[1] is not None]
        print(f"  mean return FY{lo}-FY{hi}: {sum(r[1] for r in sel)/len(sel):.1f}%  mean margin {sum(r[2] for r in sel)/len(sel):.1f}%  (n={len(sel)})")
