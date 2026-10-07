# -*- coding: utf-8 -*-
"""Independent verification of all six fold steps, read back from disk."""
import io, os, re, subprocess, json
B = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ok = True
def chk(n, cond, msg):
    global ok
    print(("PASS " if cond else "FAIL ") + str(n) + ". " + msg)
    if not cond: ok = False

# 1 register
lines = io.open(os.path.join(B,"Screens","WATCHLIST RUN QUEUE.md"),encoding="utf-8").read().split("\n")
h=[i for i,l in enumerate(lines) if l.strip()=="## COMPLETED FROM THE QUEUE"]
t=[i for i,l in enumerate(lines) if l.strip().startswith("## THE WRITE-EARLY PROTOCOL")]
ents=[l for l in lines[h[0]:t[0]] if re.match(r"^- \*\*",l)]
chk(1, len(h)==1 and len(t)==1, "heading and tail are line-exact and unique")
chk(1, len(ents)==157, "register holds 157 entries (was 156); MGM is entry 157")
chk(1, ents[0].startswith("- **MGM (MGM Resorts International)"), "MGM is the FIRST entry")
body="\n".join(lines[h[0]:h[0]+90])
for f in ["$38.59","251,592,756","0000789570-26-000076","$9,709M","5.34%","FAIL at Q2"]:
    chk(1, f in body, "register entry carries "+f)

# 2 roster
r=[l for l in io.open(os.path.join(B,"Screens","_daily","_wave7_done.txt"),encoding="utf-8").read().split("\n") if l.strip()]
chk(2, len(r)==25 and r[-1].strip()=="MGM", "wave7_done has 25 lines with MGM last (was 24)")

# 3 narrative
rl=io.open(os.path.join(B,"Screens","2026-08-31 PREPPED READING LIST (operator lists).md"),encoding="utf-8").read()
chk(3, "## UPDATE 2026-09-21 - MGM" in rl, "narrative fold present in the PREPPED READING LIST")
for f in ["guarantor","deal_note","People Incorporated","Shape #13 THE TENANT","quotecheck.py"]:
    chk(3, f in rl.split("## UPDATE 2026-09-21 - MGM")[1], "narrative carries "+f)

# 4 no band, no portfolio row
al=io.open(os.path.join(B,"tools","alerts.json"),encoding="utf-8").read()
pf=io.open(os.path.join(B,"PORTFOLIO.md"),encoding="utf-8").read()
chk(4, '"MGM"' not in al and "'MGM'" not in al, "tools/alerts.json has NO MGM band")
chk(4, not re.search(r"\bMGM\b", pf), "PORTFOLIO.md has NO MGM row")
g=subprocess.run(["git","log","--oneline","-40","--","tools/alerts.json","PORTFOLIO.md"],cwd=B,capture_output=True,text=True).stdout
chk(4, "MGM" not in g, "neither file was touched by any MGM commit")

# 5 acceptance test
p=subprocess.run(["python","tools/check_framework.py"],cwd=B,capture_output=True,text=True)
chk(5, "PASS" in p.stdout, "tools/check_framework.py returns PASS")

# 6 commits / cleanliness
st=subprocess.run(["git","status","--porcelain"],cwd=B,capture_output=True,text=True).stdout
mine=[l for l in st.split("\n") if l.strip() and not l.startswith("??")]
chk(6, not mine, "working tree has no uncommitted TRACKED changes left")
big=subprocess.run(["git","ls-tree","-r","-l","HEAD","--","Test Runs/_research 2026-09-21 MGM"],cwd=B,capture_output=True,text=True).stdout
sizes=[int(l.split()[3]) for l in big.strip().split("\n") if l.strip()]
chk(6, max(sizes) < 200000, "largest tracked research file is now %d bytes" % max(sizes))

# the run file itself
rf=io.open(os.path.join(B,"Test Runs","2026-09-21 Run - MGM MGM Resorts International.md"),encoding="utf-8").read()
chk(0, "[x] OUT" in rf, "run file records Q2 OUT")
chk(0, rf.count("VERDICT: NOT TAKEN")==4, "Q3, Q4, Q5 and Q6 each record NOT TAKEN (4 found: %d)" % rf.count("VERDICT: NOT TAKEN"))
chk(0, "# COMPUTATION \u2014 NOT A CLEARANCE" in rf, "Q5 carries the required heading verbatim")
chk(0, rf.count("\u2014")==3, "em dashes in run file = 3 (2 blockquote attributions + the required heading); found %d" % rf.count("\u2014"))
print()
print("ALL SIX FOLD STEPS VERIFIED" if ok else "*** SOMETHING FAILED ***")
