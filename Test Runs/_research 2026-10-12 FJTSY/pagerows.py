import sys, pymupdf
pdf, kw = sys.argv[1], sys.argv[2].upper()
n = int(sys.argv[3]) if len(sys.argv) > 3 else 2
d = pymupdf.open(pdf)
for pno in range(len(d)):
    p = d[pno]; t = p.get_text()
    if kw in t.upper()[:400] and 'CONTENTS' not in t.upper():
        lines = {}
        for w in p.get_text('words'):
            lines.setdefault(round((w[1]+w[3])/2/4), []).append(w)
        print('#### page', pno+1)
        for k in sorted(lines):
            print(' '.join(w[4] for w in sorted(lines[k], key=lambda w: w[0])))
        n -= 1
        if n == 0: break
