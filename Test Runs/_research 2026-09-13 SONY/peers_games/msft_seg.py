"""Flatten the MSFT segment-note table in each 10-K vintage on disk and print the MPC rows.
Reads the stripped primary-document text saved by the 2026-09-06 MSFT run."""
import os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_research 2026-09-06 MSFT")
for fy in (2023, 2024, 2025, 2026):
    t = open(os.path.join(D, "MSFT_FY%d_10K.txt" % fy), encoding="utf-8").read()
    acc = re.search(r"ACCESSION: (\S+)", t).group(1)
    i = max(t.rfind("Segment revenue and operating income were as follows"),
            t.rfind("Segment revenue, cost of revenue, operating expenses, and operating income were as follows"))
    flat = re.sub(r"[\s|]+", " ", t[i:i + 6000])
    j = flat.find("No sales to an individual customer")
    print("== FY%d 10-K acc %s" % (fy, acc))
    print(flat[:j if j > 0 else 2500])
    print()
