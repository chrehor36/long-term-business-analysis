import re, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
files = sorted(glob.glob("10K_*.txt")) + sorted(glob.glob("10Q_*.txt")) + sorted(glob.glob("8k/*earnings*.txt"))
pats = [r"price increase", r"increas\w* (our )?(list )?prices", r"rais\w* (our )?prices", r"higher[- ]priced edition", r"pricing (change|increase|action)",
        r"price reduction", r"reduc\w* (our )?prices", r"lower (our )?prices", r"discipline over discounting", r"price[- ]performance", r"cut costs", r"lower (total )?cost",
        r"switching costs", r"lock in", r"less customer"]
out = [f"files swept: {len(files)}"]
for p in pats:
    hits = []
    for f in files:
        t = re.sub(r"\s+", " ", open(f, encoding="utf-8").read())
        for m in re.finditer(p, t, re.I):
            ctx = t[max(0, m.start()-160):m.end()+160]
            if "price reduction clauses" in ctx: continue
            hits.append(f"   {f}: ...{ctx}...")
    out.append(f"## /{p}/ : {len(hits)} hits")
    out += hits[:6]
open("price_sweep_out.txt", "w", encoding="utf-8").write("\n".join(out)); print("\n".join(out)[:9000])
