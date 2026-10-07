import pymupdf, sys
d = pymupdf.open(sys.argv[1]); pno = int(sys.argv[2]) - 1
p = d[pno]
for w in sorted(p.get_text("words"), key=lambda w: (round(w[1]), w[0])):
    if w[1] > float(sys.argv[3]) and w[1] < float(sys.argv[4]):
        sys.stdout.buffer.write(("%6.1f %6.1f %s\n" % (w[1], w[0], w[4])).encode("utf-8"))
