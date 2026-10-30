import subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
docs = [
    ("0001193125-26-264811", "d101983d20f.htm", "20F_FY2026"),
    ("0001193125-25-142326", "d925022d20f.htm", "20F_FY2025"),
    ("0001193125-24-167462", "d807954d20f.htm", "20F_FY2024"),
    ("0001193125-23-179181", "d360541d20f.htm", "20F_FY2023"),
    ("0001193125-22-179197", "d696693d20f.htm", "20F_FY2022"),
    ("0001193125-21-197902", "d12243d20f.htm", "20F_FY2021"),
    ("0001193125-24-024814", "d743563d20fa.htm", "20FA_2024-02-06_FY2023"),
    ("0001193125-24-024795", "d743563d20fa.htm", "20FA_2024-02-06_FY2017"),
]
for acc, doc, out in docs:
    if os.path.exists(os.path.join(HERE, out + ".txt")):
        continue
    subprocess.run([sys.executable, os.path.join(HERE, "get.py"), "doc", acc, doc, out])
