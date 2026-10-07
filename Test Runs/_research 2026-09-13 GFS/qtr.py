"""Quarterly summary tables from the earnings-release exhibits (6-K EX-99.1): quarter headers and the first three
numeric cells of chosen rows. Transcription only; prints what the releases file."""
import os, re, glob, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = ["Net revenue", "Revenue", "Gross margin", "Gross profit", "Wafer shipments", "Adjusted EBITDA", "Non-IFRS adjusted EBITDA",
        "Net income", "Cash provided by operating activities", "Adjusted free cash flow", "Non-IFRS adjusted free cash flow",
        "Operating margin", "Diluted EPS"]
num = re.compile(r"\(?-?\$?\s*[0-9][0-9,]*\.?[0-9]*\s*%?\)?")
out = {}
files = sorted(glob.glob(os.path.join(HERE, "k", "EX_*earn*.txt")) + glob.glob(os.path.join(HERE, "k", "EX_*reportsfi*.txt"))
               + glob.glob(os.path.join(HERE, "k", "EX_2021-11-30*dex991.txt")))
for f in files:
    t = open(f, encoding="utf-8").read()
    flat = re.sub(r"\s+", " ", t)
    m = re.search(r"\|\s*(Q[1-4]'?\s?\d{2,4}|Q[1-4] \d{4})\s*\|\s*\|\s*(Q[1-4]'?\s?\d{2,4}|Q[1-4] \d{4})\s*\|\s*\|\s*(Q[1-4]'?\s?\d{2,4}|Q[1-4] \d{4})", flat)
    hdr = m.groups() if m else None
    rec = {"hdr": hdr}
    start = m.start() if m else 0
    seg = flat[start:start + 6000]
    for r in ROWS:
        mm = re.search(re.escape(r) + r"[^|]{0,60}\|(.{0,300})", seg)
        if mm:
            cells = [c.strip() for c in mm.group(1).split("|")]
            vals = [c for c in cells if re.fullmatch(r"\(?-?[0-9][0-9,]*\.?[0-9]*\)?%?", c)]
            rec[r] = vals[:3]
    out[os.path.basename(f)] = rec
    print(os.path.basename(f)[:40], rec)
json.dump(out, open(os.path.join(HERE, "qtr_out.json"), "w"), indent=1)
