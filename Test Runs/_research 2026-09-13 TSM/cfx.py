"""Print the consolidated cash-flow statement region of a stripped 20-F as joined text, and grep labels.
Usage: python cfx.py <file> <label regex> [<label regex> ...]"""
import re, sys
fn = sys.argv[1]
t = open(fn, encoding="utf-8").read()
i = t.find("CONSOLIDATED STATEMENTS OF CASH FLOWS")
# the audited statements follow the auditor report; take the first occurrence after 'REPORT OF INDEPENDENT'
j = t.find("REPORT OF INDEPENDENT REGISTERED")
if j > 0:
    k = t.find("CONSOLIDATED STATEMENTS OF CASH FLOWS", j)
    if k > 0:
        i = k
end = t.find("NOTES TO CONSOLIDATED FINANCIAL STATEMENTS", i + 100)
region = re.sub(r"\s*\|\s*", " ", t[i:end])
region = re.sub(r"\s+", " ", region)
for lab in sys.argv[2:]:
    for m in re.finditer(lab, region, flags=re.I):
        print("..", region[m.start():m.start() + 140])
