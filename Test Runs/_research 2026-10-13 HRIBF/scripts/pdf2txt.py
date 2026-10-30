import sys, fitz
for p in sys.argv[1:]:
    d = fitz.open(p)
    out = p[:-4] + ".mu.txt"
    with open(out, "w", encoding="utf-8") as f:
        for pg in d:
            f.write(pg.get_text("text", sort=True)); f.write("\n\f\n")
    print(out, len(d))
