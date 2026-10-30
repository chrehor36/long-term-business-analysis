from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
L = [l.split() for l in open("filings_list.txt")]
def acc_of(date, form):
    for x in L:
        if x[0]==date and x[1]==form: return x[2], x[3]
jobs = [("2026-09-18","8-K","8K_2026-09-18"),("2026-08-27","DEF","DEF14C_2026"),("2026-08-11","8-K","8K_2026-08-11"),
        ("2026-05-06","10-Q","10Q_2026Q1"),("2025-11-06","10-Q","10Q_2025Q3"),("2025-02-14","10-K","10K_FY2024"),
        ("2024-02-20","10-K","10K_FY2023"),("2023-02-27","10-K","10K_FY2022"),("2026-04-20","DEF","DEF14A_2026"),
        ("2025-10-02","8-K","8K_2025-10-02"),("2025-06-02","8-K","8K_2025-06-02"),("2025-05-06","8-K","8K_2025-05-06_101"),
        ("2025-05-27","8-K","8K_2025-05-27"),("2025-05-28","8-K","8K_2025-05-28"),("2026-06-12","8-K","8K_2026-06-12")]
for d, form, name in jobs:
    cands = [x for x in L if x[0]==d and x[1].startswith(form)]
    if form=="DEF": cands=[x for x in L if x[0]==d and x[1]=="DEF" ]
    if not cands:
        cands=[x for x in L if x[0]==d and form in x[1]]
    if name=="8K_2025-05-06_101": cands=[x for x in L if x[0]==d and x[2].startswith("0001140361")]
    if not cands: print("MISSING", d, form); continue
    x = cands[0]
    try: grab(x[2], x[3], name)
    except Exception as e: print("ERR", name, e)
