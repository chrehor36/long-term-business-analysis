import pymupdf, sys
d = pymupdf.open(sys.argv[1])
for pn in sys.argv[2:]:
    p = d[int(pn)-1]
    sys.stdout.buffer.write(("=== page %s\n" % pn).encode())
    rows = {}
    for w in p.get_text("words"):
        rows.setdefault(round((w[1]+w[3])/2/4), []).append(w)
    for k in sorted(rows):
        sys.stdout.buffer.write((" ".join(x[4] for x in sorted(rows[k], key=lambda x: x[0])) + "\n").encode("utf-8"))
