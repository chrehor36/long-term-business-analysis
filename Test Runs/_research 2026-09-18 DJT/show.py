import re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for fn in sys.argv[1:]:
    t = open(fn, encoding="utf-8").read()
    t = re.sub(r"\s*\|\s*", " ", t); t = re.sub(r"\s+", " ", t).replace("\ufffd","'")
    i = max(t.find("Item "), 0)
    print("=====", fn, len(t)); print(t[i:])
