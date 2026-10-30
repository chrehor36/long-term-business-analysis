import io
p="Test Runs/2026-09-12 Run - ACMR ACM Research.md"
s=io.open(p,encoding="utf-8").read()
new=io.open("Test Runs/_research 2026-09-12 ACMR/q56.md",encoding="utf-8").read()
new=new.replace("- [ ] **Corrections recorded here rather than by editing history","- [x] **Corrections recorded here rather than by editing history")
a=s.index("---\n⛔ **Q5 does not open")
s=s[:a]+new
io.open(p,"w",encoding="utf-8").write(s); print("ok", len(s))
