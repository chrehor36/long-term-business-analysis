import os
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
R = os.path.join(ROOT, "Test Runs", "_research 2026-09-18 RIVN")
RUN = os.path.join(ROOT, "Test Runs", "2026-09-18 Run - RIVN Rivian.md")
reps = [
 ("The reported FY2024-25 improvement in operating cash is about half the Volkswagen prepayment.",
  "About half of the FY2024 improvement in operating cash ($3,150M better than FY2023) is the prepayment: the line gave\n  $1,470M more than in FY2023."),
 ("and most of the improvement in its FY2024-25 operating cash came from Volkswagen paying in advance for engineering work\nthat ends in 2028;",
  "and about half of its FY2024 improvement in operating cash came from Volkswagen paying in advance for engineering work\nthat ends in 2028;"),
 ("Rivian's FY2025 consolidated gross profit ($144M) and half of its FY2024-25 operating-cash\nimprovement were Volkswagen paying in advance",
  "Rivian's FY2025 consolidated gross profit ($144M) and about half of its FY2024 operating-cash\nimprovement were Volkswagen paying in advance"),
 ("**The FY2024 operating-cash improvement is half a partner's prepayment**",
  "**About half of the FY2024 operating-cash improvement is a partner's prepayment**"),
]
for fn in [RUN, os.path.join(R, "_q3_to_end.md"), os.path.join(R, "_audit.md"), os.path.join(R, "_fold_narrative.md")]:
    s = open(fn, encoding="utf-8").read(); n = 0
    for a, b in reps:
        if a in s:
            s = s.replace(a, b); n += 1
    open(fn, "w", encoding="utf-8").write(s)
    print(os.path.basename(fn), n)
