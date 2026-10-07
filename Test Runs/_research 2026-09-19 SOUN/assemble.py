# Assemble the run file from the template head and the section files written as each question closes.
import os, re
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, "..", "..")
tmpl = open(os.path.join(root, "Test Runs", "_TEMPLATE - Company Run.md"), encoding="utf-8").read()
tmpl = tmpl.replace("—", "-")
head, rest = tmpl.split("## STEP 0", 1)
head = head.replace("# Company Run - [COMPANY] ([TICKER]) - [DATE]", "# Company Run - SoundHound AI, Inc. (SOUN) - 2026-09-19")
tail = "## Q1" + rest.split("## Q1", 1)[1]
parts = [head]
for name in ["_step0.md", "_q1.md", "_q2.md", "_q3.md", "_q4.md", "_q5q6.md", "_audit.md"]:
    p = os.path.join(here, name)
    if os.path.exists(p):
        parts.append(open(p, encoding="utf-8").read().rstrip() + "\n\n")
done = "".join(parts[1:])
# append the untouched template sections for questions not yet written
secs = re.split(r"(?m)^(?=## )", tail)
for s in secs:
    key = s.split("\n", 1)[0][:6]
    if key and key not in done:
        parts.append(s)
out = "".join(parts)
open(os.path.join(root, "Test Runs", "2026-09-19 Run - SOUN SoundHound AI.md"), "w", encoding="utf-8").write(out)
print(len(out), "chars;", out.count("\n"), "lines")
