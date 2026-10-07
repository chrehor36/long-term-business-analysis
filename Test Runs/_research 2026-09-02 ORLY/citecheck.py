import csv, re, sys
run = open(r"c:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-02 Run - ORLY OReilly Automotive.md",
           encoding="utf-8").read()
ids = set(re.findall(r"E\d-\d\d", run))
have = set()
with open(r"c:\Users\chreh\OneDrive\Documents\BRK\principle_ledger.csv", encoding="utf-8") as f:
    for row in csv.reader(f):
        for c in row[:3]:
            for m in re.findall(r"E\d-\d\d", c):
                have.add(m)
print("cited in run:", len(ids))
missing = sorted(ids - have)
print("PHANTOM (not in principle_ledger.csv):", missing if missing else "NONE")
print("resolved:", len(ids & have))
