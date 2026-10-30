import sys
run = "C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-13 Run - HRIBF Horiba.md"
src = open(sys.argv[1], encoding="utf-8").read()
with open(run, "a", encoding="utf-8") as f:
    f.write("\n" + src)
print("appended", len(src))
