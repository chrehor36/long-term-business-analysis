# Assemble the BIRD run file from the section drafts in this folder; sections not yet written keep the template text.
import os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, "..")
tmpl = open(os.path.join(root, "_TEMPLATE - Company Run.md"), encoding="utf-8").read()
head = tmpl.split("## STEP 0")[0].replace("# Company Run — [COMPANY] ([TICKER]) — [DATE]", "# Company Run - Smartbird, Inc., formerly Allbirds, Inc. (BIRD) - 2026-09-19")
head = head.replace("## THE FOUR VERDICTS — every question returns exactly one", "## THE FOUR VERDICTS - every question returns exactly one").replace("**work order — not an answer**", "**work order - not an answer**").replace("protocol violation — it is UNRESEARCHED", "protocol violation - it is UNRESEARCHED")
order = [("_step0.md", "## Q1 —"), ("_q1.md", "## Q2 —"), ("_q2.md", "## Q3 —"), ("_q3.md", "## Q4 —"), ("_q4.md", "## Q5 —"), ("_q5q6.md", "## SELF-AUDIT"), ("_audit.md", "## REGISTER"), ("_register.md", None)]
out = head
nxt = "## STEP 0"
for fn, after in order:
    p = os.path.join(here, fn)
    if os.path.exists(p):
        out += open(p, encoding="utf-8").read().rstrip() + "\n\n"
        nxt = after
    else:
        break
if nxt:
    out += "---\n*(sections below not yet written: template text)*\n\n" + nxt + tmpl.split(nxt, 1)[1]
open(os.path.join(root, "2026-09-19 Run - BIRD Allbirds.md"), "w", encoding="utf-8").write(out)
print(len(out), "chars; next section:", nxt)
