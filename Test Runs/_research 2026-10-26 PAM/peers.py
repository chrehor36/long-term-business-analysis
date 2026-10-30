"""Operating income / total assets and operating margin by year from SEC company facts (transcription; flagged)."""
import json
d = json.load(open("cache/peers_facts.json"))
for t, cur in (("PAM", "USD"), ("VIST", "USD"), ("YPF", "USD"), ("TGS", "ARS"), ("CEPU", "ARS")):
    f = d[t]
    rev = f.get(f"Revenue|{cur}", {}); op = f.get(f"ProfitLossFromOperatingActivities|{cur}", {}); a = f.get(f"Assets|{cur}", {})
    out = []
    for y in range(2017, 2026):
        k = f"CY{y}"; ka = f"CY{y}Q4I"
        if k in op and ka in a and k in rev:
            out.append(f"{y}: OI/A {op[k]/a[ka]:6.1%} OM {op[k]/rev[k]:6.1%}")
    print(t, cur); [print("   ", o) for o in out]
