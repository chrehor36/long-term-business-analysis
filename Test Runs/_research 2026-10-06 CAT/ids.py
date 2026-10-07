"""v5 ledger helper. python ids.py show ID [ID...] | grep PATTERN | check RUNFILE"""
import csv, re, sys

ROWS = {r["﻿id"] if "﻿id" in r else r["id"]: r
        for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8"))}
cmd = sys.argv[1]
if cmd == "show":
    for i in sys.argv[2:]:
        r = ROWS.get(i)
        print(i, "MISSING" if r is None else f"{r['year']} | {r['quote_verbatim'][:600]}")
        print()
elif cmd == "grep":
    pat = re.compile(sys.argv[2], re.I)
    for i, r in ROWS.items():
        if pat.search(r["quote_verbatim"]):
            print(i, "|", r["quote_verbatim"][:400].replace("\n", " "))
            print()
elif cmd == "check":
    text = open(sys.argv[2], encoding="utf-8").read()
    ids = sorted(set(re.findall(r"\b([MLR]\d{4}-\d{3})\b", text)))
    missing = [i for i in ids if i not in ROWS]
    print(len(ids), "ids cited;", "missing:", missing)
