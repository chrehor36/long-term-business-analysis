"""One-off: write the Q7 section and the Q6 write-back into the run file (resume of 2026-10-11)."""
import sys
p = r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-10 Run - SBUX Starbucks.md'
s = open(p, encoding='utf-8').read()
start = s.index("## Q7 — WHAT IS IT WORTH? STOP.")
end = s.index("## Q8 — IS IT BETTER")
new = open(sys.argv[1], encoding='utf-8').read()
s = s[:start] + new + "\n" + s[end:]
a = "*The test against the bottom of the\n  Q7 range is written back here from Q7 (below).*"
assert a in s
b = ("**Written back from Q7 (committed with Q7):** the bottom of the central Q7 range is $45.46 a share on the all-equity\n"
     "  basis ($50.71 equity-only), \"the bottom boundary of our estimate\" **[L2013-012]**. Every price paid, about $55 to $110,\n"
     "  sits above it, and the FY2022 purchases at about $110 sit above the top ($99.49). The purchases are therefore not\n"
     "  cleared by what they did, and the programme with no stated price weighs against **[L2016-002]**: \"If you’re\n"
     "  repurchasing shares above a rationally calculated intrinsic value, you are harming your shareholders\" **[M1996-013]**.")
s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print("written")
