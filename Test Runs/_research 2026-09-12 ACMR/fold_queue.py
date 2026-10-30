import io
p="Screens/WATCHLIST RUN QUEUE.md"
s=io.open(p,encoding="utf-8").read()
entry=io.open("Test Runs/_research 2026-09-12 ACMR/fold_entry.md",encoding="utf-8").read()
# 1. completed entry at top
h="## COMPLETED FROM THE QUEUE\n"
assert s.count(h)==1
s=s.replace(h, h+entry, 1)
# 2. strike in tier-3 roster
old_r="SWK, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ~~ROKU~~, RGTI, ~~ORCL~~, ~~BA~~, ACMR, ALKT,"
if old_r not in s:
    # SWK may have been struck concurrently
    old_r="~~SWK~~, ~~ARM~~, ~~CALX~~, ~~BE~~, ~~MU~~, ~~ROKU~~, RGTI, ~~ORCL~~, ~~BA~~, ACMR, ALKT,"
assert s.count(old_r)==1, "roster line not found"
s=s.replace(old_r, old_r.replace(" ACMR,"," ~~ACMR~~,"),1)
# 3. dated annotation beside the SIGN CHANGE label (added, not edited)
lab="- **SIGN CHANGE — recoveries (ACMR, ALKT, ACVA):** early years loss-making, recent years\n  positive, so the multi-year mean is averaging two different businesses [E4-25]. The run\n  must date the inflection and refuse the blended mean."
assert s.count(lab)==1
note=("\n  **ACMR RUN 2026-09-12 — THE LABEL IS WRONG IN DIRECTION, NOT JUST WIDTH.** On the rebuilt series\n"
"  the POSITIVE years are the EARLY ones (FY2018 +$3.1M, FY2019 +$5.0M at the D&A end); FY2020-23 are\n"
"  negative, FY2024 is the single positive recent year (on a +$67.1M customer prepayment that reversed\n"
"  by -$60.8M in FY2025), and FY2025 and the TTM are negative again. **There was no recovery, so there\n"
"  is no inflection to date**; the blended mean is refused because every window is negative. And\n"
"  `oe_bottom -92` / `oe_top -26` reproduce from **two different windows** (5y capex, 3y D&A) — the\n"
"  BA/INTC defect, now found in this sub-class too. Rebuilt: -$104.2M to -$26.0M consolidated.\n"
"  **ALKT and ACVA remain live under this label — read them as unlabelled.**")
s=s.replace(lab, lab+note,1)
io.open(p,"w",encoding="utf-8").write(s); print("queue folded")
