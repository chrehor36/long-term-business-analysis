import os, sys
from fetch import strip, HERE

SRC = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-01 GM"
FILES = {
    "GM_10K_FY2025.htm": "0001467858-26-000013",
    "GM_10K_FY2024.htm": "0001467858-25-000032",
    "GM_10K_FY2023.htm": "0001467858-24-000031",
    "GM_10K_FY2022.htm": "0001467858-23-000029",
    "FORD_10K_FY2025.htm": "0000037996-26-000015",
    "HMC_20F_FY2026.htm": "0001193125-26-274991",
    "STLA_20F_FY2025.htm": "0001605484-26-000021",
    "TSLA_10K_FY2025.htm": "0001628280-26-003952",
}
for f, acc in FILES.items():
    h = open(os.path.join(SRC, f), encoding="utf-8", errors="replace").read()
    t = strip(h)
    name = f.replace(".htm", ".txt")
    open(os.path.join(HERE, name), "w", encoding="utf-8").write("LOCAL COPY OF: " + f + " (from _research 2026-09-01 GM)\nACCESSION: " + acc + "\n\n" + t)
    print(name, len(t))
