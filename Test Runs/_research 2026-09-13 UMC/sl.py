import sys, re
fn, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
L = open(fn, encoding="utf-8").read().split("\n")[a-1:b]
s = "\n".join(L)
s = re.sub(r"[ \t]*\|[ \t]*\n", " | ", s)
s = re.sub(r"\n\s*\|\s*", " | ", s)
s = re.sub(r"(\|\s*)+", "| ", s)
print(s)
