import pymupdf, sys
d = pymupdf.open(sys.argv[1])
out = sys.stdout.buffer
for i, p in enumerate(d):
    if sys.argv[2] in p.get_text():
        out.write(("=== page %d\n" % (i+1)).encode())
        rows = {}
        for w in p.get_text("words"):
            rows.setdefault(round(w[3]/3), []).append(w)
        for k in sorted(rows):
            out.write((" ".join(x[4] for x in sorted(rows[k], key=lambda x: x[0])) + "\n").encode("utf-8"))
