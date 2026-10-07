RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - MBGL Mobility Global.md"
s = open(RUN, encoding="utf-8").read()
old = """**Proposed
  FOURTEENTH shape, for the fold to register or reject: THE DOWRY**"""
new = """**Proposed
  shape, for the operator to register or reject: THE DOWRY** (it would be the FIFTEENTH: twelve are
  registered, SPOT's THE TENANT and GFS's THE PATRON are proposed and unregistered, both read in the
  reading list before this was written)"""
assert old in s, "anchor missing"
s = s.replace(old, new)
open(RUN, "w", encoding="utf-8").write(s)
print("ok")
