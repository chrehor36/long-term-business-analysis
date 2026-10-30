import re, sys
sys.stdout.reconfigure(encoding="utf-8")
t = open("cache/CRN_0001562762-26-000094.flat.txt", encoding="utf-8").read()
t = re.sub(r"\s+", " ", t)
for m in re.finditer(r"(Australian Operations|U\.S\. Operations|Australia|United States)[^~]{0,200}?(Three|Six) Months Ended", t):
    pass
for m in re.finditer(r"Sales [Vv]olume \(MMt\)", t):
    print("...", t[max(0, m.start()-250): m.start()+1100], "\n")
