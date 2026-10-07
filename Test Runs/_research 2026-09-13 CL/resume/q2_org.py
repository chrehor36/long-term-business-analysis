"""Resume session 2026-09-13: volume, price, FX, organic sales and operating margin by region and year, each from that year's own 10-K MD&A.
Extraction and arithmetic only; no conclusion. Output: resume/q2_org_out.md"""
import re, sys, os
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(HERE)
N = r"(\d+\.\d)"
REG = {"Worldwide": r"Worldwide Net sales were", "North America": r"Net sales in North America (?:increased|decreased|were)",
       "Latin America": r"Net sales in Latin America (?:increased|decreased|were)", "Europe": r"Net sales in Europe (?:increased|decreased|were)",
       "Asia Pacific": r"Net sales in Asia Pacific (?:increased|decreased|were)", "Africa/Eurasia": r"Net sales in Africa/Eurasia (?:increased|decreased|were)",
       "Hill's": r"Net sales (?:for|in) (?:the )?Hill.s Pet Nutrition (?:segment )?(?:increased|decreased|were)",
       "OPHC": r"Net sales in the Oral, Personal and Home Care product segment were"}
ORG = {"Worldwide": r"Organic sales \(", "North America": r"Organic sales in North America", "Latin America": r"Organic sales in Latin America",
       "Europe": r"Organic sales in Europe", "Asia Pacific": r"Organic sales in Asia Pacific", "Africa/Eurasia": r"Organic sales in Africa/Eurasia",
       "Hill's": r"Organic sales (?:for|in) (?:the )?Hill.s Pet Nutrition", "OPHC": r"Organic sales in the Oral, Personal and Home Care product segment"}
def comp(s, word):
    m = re.search(r"(volume|net selling price|foreign exchange)[^%]{0,40}?%s" % N, s) if False else None
def grab(s):
    d = {}
    for key, pat in [("vol", r"volume (growth|declines|increases|decreases) of " + N), ("price", r"net selling price (increases|decreases) of " + N), ("fx", r"(positive|negative) foreign exchange of " + N)]:
        m = re.search(pat, s)
        if m: d[key] = ("-" if m.group(1) in ("declines", "decreases", "negative") else "+") + m.group(2)
    if "volume was flat" in s or "volume and foreign exchange were flat" in s or "volume and foreign exchange was flat" in s: d.setdefault("vol", "0.0")
    if "foreign exchange was flat" in s or "foreign exchange were flat" in s or "foreign exchange were flat" in s: d.setdefault("fx", "0.0")
    if "selling prices were flat" in s or "net selling prices were flat" in s.lower(): d.setdefault("price", "0.0")
    return d
rows = ["| FY | scope | volume | price | FX | organic | op. margin, current year (table above the sentence) | source sentence start |", "|---|---|---|---|---|---|---|---|"]
data = {}
for y in range(2016, 2026):
    t = re.sub(r"\s+", " ", open(os.path.join(R, f"10-K_FY{y}.txt"), encoding="utf-8").read())
    for reg, p in REG.items():
        hit = None
        for m in re.finditer(p, t):
            seg = t[m.start(): m.start() + 450]
            if re.search(r"(in %d to \$|\$[\d,]+ in %d)" % (y, y), seg[:120]):
                hit = m; break
        if not hit:
            rows.append(f"| {y} | {reg} | not found | | | | | |"); continue
        seg = t[hit.start(): hit.start() + 450]
        end = re.search(r"\d ?%? ?\. [A-Z]", seg); sent = seg[: end.end() - 2] if end else seg[:300]
        d = grab(sent)
        o = re.search(ORG[reg] + r".{0,120}?(increased|decreased|were flat|was flat)(?: (\d+\.\d)%%)? in %d" % y, t[hit.start(): hit.start() + 2500])
        org = "n/f" if not o else ("0.0" if "flat" in o.group(1) else ("-" if o.group(1) == "decreased" else "+") + o.group(2))
        back = t[max(0, hit.start() - 2500): hit.start()]
        mg = re.findall(r"% of Net sales \| ([\d.]+) \|", back)
        rows.append(f"| {y} | {reg} | {d.get('vol','?')} | {d.get('price','?')} | {d.get('fx','?')} | {org} | {mg[-1]+'%' if mg and reg not in ('Worldwide','OPHC') else ''} | {sent[:150]} |")
        data[(y, reg)] = (d, org, mg[-1] if mg else None)
open(os.path.join(HERE, "q2_org_out.md"), "w", encoding="utf-8").write("\n".join(rows))
print("\n".join(r[:230] for r in rows))
