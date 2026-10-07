"""The NVDA fold, steps 3-4: the reading-list narrative (appended) and the survival-shape index (NVDA as a later instance of #1 and #18)."""
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
rl = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
t = open(rl, encoding="utf-8").read()
assert "UPDATE 2026-09-13 - NVDA" not in t
add = open(ROOT + r"\Test Runs\_research 2026-09-13 NVDA\fold_narrative.md", encoding="utf-8").read()
if not t.endswith("\n"):
    t += "\n"
open(rl, "w", encoding="utf-8").write(t + add)

sx = ROOT + r"\Screens\SURVIVAL SHAPES - index.md"
s = open(sx, encoding="utf-8").read()
r1 = "| BA (a feature), AMZN (beside #18) |"
r18 = "and borrows to build the capacity they have committed to buy | |"
assert r1 in s and r18 in s
s = s.replace(r1, "| BA (a feature), AMZN (beside #18), NVDA ($279bn of supply commitments, beside #18) |")
s = s.replace(r18, "and borrows to build the capacity they have committed to buy | NVDA (from the vendor's side: stakes in, "
              "buy-backs for and guarantees of the laboratories and AI clouds that buy its systems; the loss lands on inventory, supply, receivables and "
              "guarantees rather than plant) |")
r12 = "| UMC (second) |"
assert r12 in s
s = s.replace(r12, "| UMC (second), NVDA (through its foundry; carried as exposure, not its death) |")
open(sx, "w", encoding="utf-8").write(s)
print("reading list and shape index updated")
