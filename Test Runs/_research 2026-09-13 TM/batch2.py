import subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [l.split() for l in open(os.path.join(HERE, "filings_list.txt"), encoding="utf-8") if l[:4].isdigit()]
done = set(f.split("__")[0] for f in os.listdir(HERE) if "__" in f)
for r in rows:
    date, form, acc = r[0], r[1], r[2]
    if form in ("6-K", "6-K/A", "SCHEDULE", "SD", "F-3ASR", "424B2") and date >= "2025-03-01":
        prefix = f"{form.replace('/', '')}_{date}_{acc[-6:]}"
        if prefix in done:
            continue
        subprocess.run([sys.executable, os.path.join(HERE, "get.py"), "all", acc, prefix])
