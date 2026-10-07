# SOUN fold: register entry (prepended under the heading line), wave 5 strike, dated note after the LCID note,
# reading-list narrative appended, survival-shapes index updated. All three files are CRLF; read and written without translation.
import io
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
HERE = ROOT + r"\Test Runs\_research 2026-09-19 SOUN"
def rd(p): return io.open(p, encoding="utf-8", newline="").read()
def wr(p, s): io.open(p, "w", encoding="utf-8", newline="").write(s)
def crlf(t): return t.replace("\r\n", "\n").replace("\n", "\r\n")

# 1-2. queue file
P = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
s = rd(P)
row_old = "| cap rejected as a broken input: read the cover | ~~HBB~~, ~~LCID~~, SOUN, BIRD |"
assert s.count(row_old) == 1
s = s.replace(row_old, row_old.replace(" SOUN,", " ~~SOUN~~,"))
note = crlf(rd(HERE + r"\_wave5note.md").strip())
i = s.index("*Dated note, 2026-09-19 (the LCID run), left beside the table")
j = s.index("\r\n", i)
s = s[:j + 2] + "\r\n" + note + "\r\n" + s[j + 2:]
reg = crlf(rd(HERE + r"\_register.md").rstrip() + "\n")
h = "\r\n## COMPLETED FROM THE QUEUE\r\n"
assert s.count(h) == 1
k = s.index(h) + len(h)
s = s[:k] + reg + s[k:]
wr(P, s)

# 3. reading list
R = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
r = rd(R)
if not r.endswith("\r\n"): r += "\r\n"
r += crlf(rd(HERE + r"\_readinglist.md"))
wr(R, r)

# survival shapes index
S = ROOT + r"\Screens\SURVIVAL SHAPES - index.md"
x = rd(S)
a8 = "its preferred claim growing about 18% a year ahead of the common) |"
assert x.count(a8) == 1
x = x.replace(a8, "its preferred claim growing about 18% a year ahead of the common), SOUN (2026-09-19, the mechanism, with #2 as a feature and #21 proposed: TTM revenue $203.2M against about $404M of operating costs, the gap filled by equity every year and the liquidity plan naming the ATM; common 200.0M to about 485M since FY2022) |")
a2 = "PUBM (2026-09-19, a feature: stock pay 47-51% of operating cash FY2024-25, grant value above the charge FY2021-24; #11 the mechanism) |"
assert x.count(a2) == 1
x = x.replace(a2, "PUBM (2026-09-19, a feature: stock pay 47-51% of operating cash FY2024-25, grant value above the charge FY2021-24; #11 the mechanism), SOUN (2026-09-19, a feature: stock pay 47.7% of FY2025 revenue on the charge, RSU grant value $168.2M against an $83.1M charge; operating cash negative, so no ratio to it; #8 the mechanism) |")
row20 = "| 20 | **The wave** *(proposed, pending the operator)* | AEHR (2026-09-18) |"
i = x.index(row20); j = x.index("\r\n", i)
row21 = "| 21 | **The roll-up** *(proposed, pending the operator)* | SOUN (2026-09-19) | the reported growth is bought with the acquirer's own shares from the owners and creditors of shrinking businesses, while the businesses owned throughout shrink; it lasts as long as the quote will buy the next one, and earn-outs and creditor settlements are paid in the same currency | |"
x = x[:j + 2] + row21 + "\r\n" + x[j + 2:]
old = "**All eight are listed so briefs count correctly; none is settled.**"
assert x.count(old) == 1
x = x.replace(old, "SOUN proposed THE ROLL-UP (2026-09-19), arguing it is neither #8 nor #10: #8 describes how the losses are funded, #21 how the revenue line is made (SoundHound's reported revenue $45.9M to $168.9M FY2023-25 while the filer's own pro forma for the businesses it owned fell $153.6M to $143.5M and $225.6M to $211.7M, then LivePerson, revenue down 53% since FY2022, bought largely with 36.9M shares paid to its creditors), and unlike #10 there is no strong leg whose cash is recycled, only a share price. **All nine are listed so briefs count correctly; none is settled.**")
wr(S, x)
print("ok")
