"""Read labelled lines from the filed consolidated cash-flow statements of each 20-F (three years each). Transcription only."""
import re, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LABELS = {
 "ocf": r"Net cash provided by operating activities",
 "dep": r"Depreciation",
 "amort": r"Amortization(?! of deferred)",
 "sbc": r"Share-based payment",
 "capex": r"Acquisition of property, plant and equipment",
 "intang": r"Acquisition of intangible assets",
 "grants": r"Government grants related to assets acquisition",
 "ppe_disp": r"Proceeds from disposal of property, plant and equipment",
 "div_recd": r"Dividend received",
 "int_recd": r"Interest received",
 "int_paid": r"Interest paid",
 "tax_paid": r"Income tax paid",
 "div_paid": r"Cash dividends",
 "treasury": r"(?:Purchase|Acquisition) of treasury stock",
 "gdep_inc": r"Increase in guarantee deposits",
 "gdep_dec": r"Decrease in guarantee deposits",
 "bonds": r"Proceeds from bonds issued",
 "pretax": r"Net income before tax",
}
NUM = r"\(?-?[\d,]+\)?|—|-"
def region(t):
    j = t.find("REPORT OF INDEPENDENT REGISTERED")
    i = t.find("CONSOLIDATED STATEMENTS OF CASH FLOWS", j if j > 0 else 0)
    k = t.find("NOTES TO CONSOLIDATED FINANCIAL STATEMENTS", i + 100)
    r = re.sub(r"\s*\|\s*", " ", t[i:k]); r = re.sub(r"\$\s+", "", r)
    r = re.sub(r"\(\s+", "(", r); r = re.sub(r"\s+\)", ")", r)
    return re.sub(r"\s+", " ", r)
def val(s):
    if s in ("—", "-"): return 0.0
    neg = s.startswith("(")
    v = float(s.strip("()").replace(",", ""))
    return -v if neg else v
out = {}
for fy in sys.argv[1:]:
    t = open(os.path.join(HERE, f"20F_FY{fy}.txt"), encoding="utf-8").read()
    r = region(t)
    yrs = [str(int(fy) - 2), str(int(fy) - 1), fy]
    for k, lab in LABELS.items():
        m = re.search(lab + r"\s+((?:(?:" + NUM + r")\s+){3})", r)
        if not m:
            print(fy, k, "NOT FOUND"); continue
        vals = [val(x) for x in m.group(1).split()[:3]]
        for y, v in zip(yrs, vals):
            out.setdefault(k, {}).setdefault(y, {})[fy] = v / 1000.0
json.dump(out, open(os.path.join(HERE, "cfread_out.json"), "w"), indent=1)
for k in LABELS:
    print(f"{k:10s}", {y: d for y, d in sorted(out.get(k, {}).items())})
