import io
Q="Screens/WATCHLIST RUN QUEUE.md"
raw=io.open(Q,encoding="utf-8",newline="").read()
crlf = "\r\n" in raw
s=raw.replace("\r\n","\n")
entry=io.open("Test Runs/_research 2026-09-12 ALKT/fold_entry.md",encoding="utf-8").read().rstrip("\n")+"\n"
# 1. entry at head of COMPLETED
h="## COMPLETED FROM THE QUEUE\n"
assert s.count(h)==1
s=s.replace(h, h+entry,1)
# 2. strike roster
old="~~BA~~, ~~ACMR~~, ALKT, ~~INTC~~, ACVA, NEGG, FLNC"
assert s.count(old)==1
s=s.replace(old,"~~BA~~, ~~ACMR~~, ~~ALKT~~, ~~INTC~~, ACVA, NEGG, FLNC")
# 3a. dated note beside the SIGN CHANGE sub-class text (append after the ACMR note)
a="  **ALKT and ACVA remain live under this label — read them as unlabelled.**\n"
assert s.count(a)==1
note=("  **ALKT RUN 2026-09-12 — THE LABEL IS RIGHT ABOUT THE LINE IT MEASURED AND WRONG ABOUT THE OBJECT.** Operating\n"
"  cash does change sign (−$39.1M FY2019 … −$17.5M FY2023, then +$18.6M FY2024, +$42.9M FY2025), which is what\n"
"  `level_note` read; **owner earnings never do** — OCF less SBC is negative in all seven filed years (−$33.8M FY2025,\n"
"  −$10.9M TTM), which is what `level_note_oe` read. **86% of the FY2021-25 rise in operating cash ($71.9M) is the rise\n"
"  in stock compensation ($62.1M).** So there is no inflection to date on owner earnings, and every window is negative\n"
"  (−$71.5M to −$43.7M; TTM −$20.3M to −$16.4M). `oe_bottom -67` / `oe_top -57` again reproduce from **different\n"
"  windows and different (c) ends** (5y D&A-as-filed; 3y capex). Closed at **Q2 OUT on the business**, not on the\n"
"  arithmetic. **ACVA is now the last name live under this label — read it as unlabelled; two of three runs under it\n"
"  found the label describing a different series from the one the framework asks about.**\n")
s=s.replace(a,a+note)
# 3b. short dated parenthetical after the STILL LIVE line (appended, dated text untouched)
b="BA (third) WAS RUN 2026-09-12 and is struck.** Read every one of them as unlabelled."
assert s.count(b)==1
s=s.replace(b,b+" *(ALKT RUN 2026-09-12: struck - closed at Q2 on the business; the SIGN CHANGE it carried was operating cash, not owner earnings.)*")
if crlf: s=s.replace("\n","\r\n")
io.open(Q,"w",encoding="utf-8",newline="").write(s)
print("queue folded; crlf:",crlf)
