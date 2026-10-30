"""Append the Q7 draft to the run file and write the Q7 lines back into Q6 (2026-10-23)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-23 Run - FTS Fortis.md"
DRAFT = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-10-23 FTS\drafts\q7.md"
s = open(RUN, encoding="utf-8").read()
reps = [
("""- **Buybacks.** None in the window; none announced. The test is idle here, and the bottom of Q7's range is written back
  below for the record **[L1999-023]**.""",
"""- **Buybacks.** None in the window; none announced. The test is idle here, and the bottom of Q7's range is written back
  below for the record **[L1999-023]**. *Written back at Q7 (committed with Q7):* the bottom of the range is **C$72.41** a
  share (equity-only, central, at the 4.19% sovereign); there are no purchases to read against it."""),
("""at Q7. Serial issuance **[L2014-015]**""",
"""at Q7. *Written back at Q7:* the 2024 and 2025 issues, at about C$55.29 and C$65.38, were below the bottom of the range
  (C$72.41), so shares were issued beneath the value computed at the government rate, which harms the continuing owners
  **[M1996-013]**; the 2026 issues, at about C$75.83, sat inside the range. At the owner's floor every issue was well above
  value (fair C$28.96). Serial issuance **[L2014-015]**"""),
("""The
  intrinsic leg, which the rows require beside it because the market leg alone misleads **[R2009-002]**: written back at Q7.""",
"""The
  intrinsic leg, which the rows require beside it because the market leg alone misleads **[R2009-002]**: *written back at
  Q7:* at the 4.19% government rate the growth case is worth more than the no-growth case (C$97.93 against C$72.41), so the
  dollars retained add value at the yardstick rate; at the ten percent floor the growth case is worth less (C$27.59 against
  C$30.34), so they earn less than the owner's minimum. The leg passes at the yardstick and fails at the floor."""),
]
for a, b in reps:
    assert a in s, a[:60]
    s = s.replace(a, b)
if "## Q7:" not in s:
    s = s.rstrip("\n") + "\n\n" + open(DRAFT, encoding="utf-8").read()
open(RUN, "w", encoding="utf-8").write(s)
print("ok")
