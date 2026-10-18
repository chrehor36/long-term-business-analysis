import sys
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
lines = open(sys.argv[1], encoding="utf-8").read().split("\n")[int(sys.argv[2]):int(sys.argv[3])]
num = re.compile(r"^\(?-?[\d,\.]+\)?%?$|^—$")
out = []
for ln in lines:
    if num.match(ln) and out:
        out[-1] += "  " + ln
    else:
        out.append(ln[:300])
print("\n".join(out))
