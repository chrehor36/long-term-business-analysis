RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - MBGL Mobility Global.md"
s = open(RUN, encoding="utf-8").read()
old = "(`0002012383-26-003227`), a passive-holder form (13G, not 13D);"
new = ("(`0002012383-26-003227`) by **BlackRock, Inc.** (reporting-person type HC, event date 07/31/2026),\n"
       "  a passive-holder form (13G, not 13D);")
assert old in s
s = s.replace(old, new)
open(RUN, "w", encoding="utf-8").write(s)
print("ok")
