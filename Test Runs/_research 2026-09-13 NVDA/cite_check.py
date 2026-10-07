"""Every [Exx-nn] cited in the NVDA run file must exist in principle_ledger.csv (run files are outside check_framework.py's DOCS)."""
import csv, re, sys
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
ids = {r["id"] for r in csv.DictReader(open(ROOT + r"\principle_ledger.csv", encoding="utf-8-sig"))}
text = open(ROOT + r"\Test Runs\2026-09-13 Run - NVDA NVIDIA.md", encoding="utf-8").read()
cited = sorted(set(re.findall(r"\bE[1-5]-\d{2}\b", text)))
missing = [c for c in cited if c not in ids]
print(len(cited), "distinct ids cited;", "MISSING:" if missing else "none missing", missing)
em = [i + 1 for i, l in enumerate(text.split("\n")) if "\u2014" in l]
print("lines carrying an em dash:", em)
