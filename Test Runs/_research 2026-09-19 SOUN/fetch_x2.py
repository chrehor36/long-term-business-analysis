from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
for acc, doc, name in [("0001213900-26-097712","ea030469101ex99-1.htm","EX991_2026-09-04_close"),
  ("0001213900-26-097412","ea0304633-s4mef_sound.htm","S4MEF_2026-09-04"),
  ("0001213900-26-097412","ea030463301ex-fee.htm","S4MEF_fee"),
  ("0001213900-26-097474","ea0304183-s8_soundhound.htm","S8_2026-09-04"),
  ("0001213900-26-045987","ea028711701ex99-1.htm","EX991_2026-04-21_deal"),
  ("0001213900-26-045987","ea028711701ex10-1.htm","EX101_2026-04-21_notesrestr")]:
    grab(acc, doc, name)
