import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(HERE, sys.argv[1])
dst = os.path.join(os.path.dirname(HERE), "peers_moto.md")
with open(src, encoding="utf-8") as f:
    t = f.read()
with open(dst, "a", encoding="utf-8") as f:
    f.write(t if t.endswith("\n") else t + "\n")
print("appended", len(t), "chars from", sys.argv[1])
