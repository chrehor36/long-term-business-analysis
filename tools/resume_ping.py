"""Local ping: resume the watchlist run queue. Local only, per the standing rule.

ONE-OFF FROM 2026-09-01, kept as history. It fired for waves 1 and 2 of the watchlist. The queue it
pointed at (Screens/queue.py and its RUN_QUEUE.json) is dead: the register under
'## COMPLETED FROM THE QUEUE' in Screens/WATCHLIST RUN QUEUE.md and the wave files in Screens/_daily/
replaced it, and the hourly BRK-overnight task does the resuming. Where to pick up is the last dated
section of Screens/RESUME STATE 2026-09-12 - Opus session, note for Fable.md.
(Docstring and the WHERE TO PICK UP lines corrected 2026-09-25; the message text below is otherwise
the 2026-09-01 original.)
"""
import ctypes, os
from datetime import datetime
ROOT = r"c:\Users\chreh\OneDrive\Documents\BRK"
msg = ("RESUME THE WATCHLIST RUN QUEUE\n\n"
       "Operator instruction: run EVERY business on the provided lists through the\n"
       "framework. ETFs excluded. Pre-run names excluded. Each run ends with a PRICE\n"
       "and a PASS/FAIL line.\n\n"
       "WHERE TO PICK UP:\n"
       "  Screens\\RESUME STATE 2026-09-12 ...md   the last dated section: state and next step\n"
       "  Screens\\WATCHLIST RUN QUEUE.md          the register, the waves and the output contract\n"
       "  Screens\\_daily\\_wave7_order.txt         the current order file (done file beside it)\n\n"
       "Run files on disk are the SOURCE OF TRUTH for what is done.\n\n"
       "Wave 1 launched 2026-09-01 ~21:30: GM, F, OXY, KR, AEO, PLAB.\n"
       "Wave 2: PINS, DG, NKE, AATC, UAL, QCOM.\n\n"
       "SEPARATE TRACK, do not fold into a wave: MINI BERK (L, WTM, MKL, BRK-A/B,\n"
       "HHH, GHC, BAM, BN). The project has not yet answered how owner earnings is\n"
       "computed for an insurer - float is not operating cash flow. Write that up\n"
       "BEFORE running them, not during.\n\n"
       "Standing: 11 businesses cleared Q1-Q4 and all 11 failed on price; BBWI and\n"
       "GIS then failed at Q2 despite clearing the floor on yield.")
ctypes.windll.user32.MessageBoxW(0, msg, "BRK - resume the run queue", 0x40 | 0x10000 | 0x40000)
os.makedirs(os.path.join(ROOT, "tools", "_cache"), exist_ok=True)
with open(os.path.join(ROOT, "tools", "_cache", "resume_pings.log"), "a", encoding="utf-8") as f:
    f.write(f"{datetime.now():%Y-%m-%d %H:%M} resume ping fired\n")
