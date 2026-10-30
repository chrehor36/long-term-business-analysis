import sys
sys.stdout.reconfigure(encoding="utf-8")
H = "Test Runs/_research 2026-09-19 HBB/"
p = "Screens/WATCHLIST RUN QUEUE.md"
s = open(p, encoding="utf-8").read()
assert "- **HBB (" not in s, "already entered"
L = s.split("\n")
i = [k for k, l in enumerate(L) if l.strip() == "## COMPLETED FROM THE QUEUE"][0]
assert L[i + 1].startswith("- **BZFD")
e = open(H + "_register.md", encoding="utf-8").read().rstrip("\n").split("\n")
L = L[:i + 1] + e + L[i + 1:]
s = "\n".join(L)
old = "| cap rejected as a broken input: read the cover | HBB, LCID, SOUN, BIRD |"
assert s.count(old) == 1
s = s.replace(old, "| cap rejected as a broken input: read the cover | ~~HBB~~, LCID, SOUN, BIRD |")
anchor = "\n*SPOT and SPGI had runs on 2026-07-15"
assert s.count(anchor) == 1
note = open(H + "_wave5note.md", encoding="utf-8").read().strip("\n")
s = s.replace(anchor, "\n" + note + "\n" + anchor, 1)
open(p, "w", encoding="utf-8").write(s)
print("queue ok")
