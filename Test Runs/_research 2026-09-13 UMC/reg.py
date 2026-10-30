import sys, re
fn, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(fn, encoding="utf-8").read().split("\n")[a-1:b]
s = " ".join(L)
s = re.sub(r"\s*\|\s*", " ", s)
s = re.sub(r"\$\s+", "", s)
s = re.sub(r"\(\s+", "(", s); s = re.sub(r"\s+\)", ")", s)
s = re.sub(r"\s+", " ", s)
# break before labels (capitalized word after a number)
s = re.sub(r"(\d|\)|—) ([A-Z][a-z])", r"\1\n\2", s)
print(s)
