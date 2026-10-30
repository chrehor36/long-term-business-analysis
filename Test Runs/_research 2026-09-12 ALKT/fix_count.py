import io
RUN="Test Runs/2026-09-12 Run - ALKT Alkami Technology.md"
s=io.open(RUN,encoding="utf-8").read()
reps=[
("against **the eleven competitors Q2 Holdings names for the\n  digital banking platform** (Candescent, Alkami, CSI, Backbase, Lumin Digital, Finastra, Bottomline,\n  Fiserv, Jack Henry, FIS, plus Q2 itself as the author).",
 "against **the ten companies Q2 Holdings names for its\n  digital banking platform** (Candescent, Alkami, CSI, Backbase, Lumin Digital, Finastra, Bottomline,\n  Fiserv, Jack Henry, FIS) — **ten substitutes for Alkami counting Q2 Holdings itself**."),
("names eleven competitors through its closest\nrival's filing,","is one of ten names in its closest\nrival's competitor list,"),
("fails: eleven named substitutes in the\n  competitor's 10-K,","fails: ten substitutes in the\n  competitor's 10-K (nine named beside Alkami, plus the author),"),
("the closest competitor's list of eleven substitutes and on","the closest competitor's list of ten substitutes and on"),
("the eleven named competitors listed, six unpriceable","the ten companies Q2 Holdings names listed, six unpriceable"),
("names it among eleven substitutes and Alkami calls every win a","names it among ten digital-banking vendors and Alkami calls every win a"),
("  4. **Net debt is $264.0M**","  5. **A count corrected in the fold (after commit `e9647bd`):** Q2 and the register said Q2 Holdings names *eleven*\n     substitutes. The sentence names **ten companies, Alkami among them** — nine substitutes plus Q2 Holdings itself makes\n     ten. Corrected in place; commit `e9647bd`'s message says \"eleven\" and stands as written, wrong by one.\n  4. **Net debt is $264.0M**"),
]
for a,b in reps:
    if a not in s: print("MISSING", a[:60]); continue
    s=s.replace(a,b)
io.open(RUN,"w",encoding="utf-8",newline="\n").write(s)
f="Test Runs/_research 2026-09-12 ALKT/fold_entry.md"; t=io.open(f,encoding="utf-8").read()
t=t.replace("names **Alkami among\n  eleven digital-banking substitutes** (Candescent, Alkami, CSI, Backbase, Lumin, Finastra, Bottomline, Fiserv, Jack\n  Henry, FIS)","names **Alkami among\n  ten digital-banking vendors** (Candescent, Alkami, CSI, Backbase, Lumin, Finastra, Bottomline, Fiserv, Jack\n  Henry, FIS)")
io.open(f,"w",encoding="utf-8").write(t); print("eleven left in entry:", t.count("eleven"))
