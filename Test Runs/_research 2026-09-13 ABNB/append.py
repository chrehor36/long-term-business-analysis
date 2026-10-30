import sys
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - ABNB Airbnb.md"
src = sys.argv[1]
text = open(src, encoding="utf-8").read()
cur = open(RUN, encoding="utf-8").read()
if text.strip()[:80] in cur:
    print("ALREADY PRESENT - not appended")
    sys.exit(1)
with open(RUN, "a", encoding="utf-8") as f:
    if not cur.endswith("\n"):
        f.write("\n")
    f.write(text)
print("appended", len(text), "chars; run file now", len(cur) + len(text))
