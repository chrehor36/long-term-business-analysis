import sys
run = "Test Runs/2026-10-12 Run - ADRZY Andritz.md"
tail = open("Test Runs/_research 2026-10-12 ADRZY/draft_tail.md", encoding="utf-8").read()
s = open(run, encoding="utf-8").read().rstrip("\n") + "\n" + tail
open(run, "w", encoding="utf-8").write(s)
print("appended", len(tail))
