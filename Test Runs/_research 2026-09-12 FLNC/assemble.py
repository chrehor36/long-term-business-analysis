import os, re
D = os.path.dirname(os.path.abspath(__file__))
tm = open(os.path.join(D, "_tmpl_rest.md"), encoding="utf-8").read()
# template chunks keyed by section
marks = ["## Q1 ", "## Q2 ", "## Q3 ", "## Q4 ", "## Q5 ", "## Q6 ", "## SELF-AUDIT", "## REGISTER"]
pos = [tm.find(m) for m in marks] + [len(tm)]
chunks = {marks[i]: tm[pos[i]:pos[i+1]] for i in range(len(marks))}
order = [("_q1.md","## Q1 "),("_q2.md","## Q2 "),("_q3.md","## Q3 "),("_q4.md","## Q4 "),("_q5.md","## Q5 "),("_q6.md","## Q6 "),("_audit.md","## SELF-AUDIT"),("_register.md","## REGISTER")]
out = [open(os.path.join(D, "_head.md"), encoding="utf-8").read()]
for f, m in order:
    p = os.path.join(D, f)
    if os.path.exists(p):
        out.append(open(p, encoding="utf-8").read())
    else:
        out.append(chunks[m])
run = os.path.join(os.path.dirname(D), "2026-09-12 Run - FLNC Fluence Energy.md")
open(run, "w", encoding="utf-8").write("".join(out))
print("wrote", run, sum(len(x) for x in out))
