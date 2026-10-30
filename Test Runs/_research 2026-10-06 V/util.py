"""Small reading helpers for the cached filings.
python util.py idx FILE.json             list a filing index
python util.py find FILE.txt REGEX [N]   print matches with N chars of context (default 300)
python util.py span FILE.txt START LEN   print a character span"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def p(name):
    return name if os.path.isabs(name) else os.path.join(HERE, "cache", name)


cmd = sys.argv[1]
if cmd == "idx":
    d = json.load(open(p(sys.argv[2])))
    for i in d["directory"]["item"]:
        print(i["name"], i.get("size"))
elif cmd == "find":
    t = open(p(sys.argv[2])).read()
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 300
    for m in re.finditer(sys.argv[3], t, re.I):
        print("@%d: ...%s..." % (m.start(), t[max(0, m.start() - n): m.end() + n].replace("\n", " / ")))
        print("-" * 60)
elif cmd == "span":
    t = open(p(sys.argv[2])).read()
    s = int(sys.argv[3]); print(t[s: s + int(sys.argv[4])])
