# re-run only the passers-list regeneration of tools/v5_rerun_fold.py, after the dispatcher corrected the WAB register head
# (a parenthesis in the company name kept the tool's regex from reading the line); no other step repeated
import json, os, re, sys
src = open(r"C:\Users\chreh\OneDrive\Documents\BRK\tools\v5_rerun_fold.py", encoding="utf-8").read()
pre = src.split('B = json.load')[0]
regen = src.split("# regenerate the passers list")[1]
g = {}
exec(pre, g)
g["R"] = g["ROOT"] + r"\Screens\WATCHLIST RUN QUEUE.md"; g["D"] = g["ROOT"] + r"\Screens\_daily\_v5_rerun_done.txt"
g["d"] = json.load(open(g["ROOT"] + r"\tools\alerts.json", encoding="utf-8")); g["runs"] = []; g["tag"] = "regen only"; g["ret"] = 0
exec(regen, g)
