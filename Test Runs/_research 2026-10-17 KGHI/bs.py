import sys, fitz
for f in sys.argv[1:]:
    d = fitz.open(f)
    for pno in range(min(4, len(d))):
        p = d[pno]
        t = p.get_text()
        if 'BALANCE SHEETS' not in t.upper(): continue
        words = p.get_text('words')
        rows = {}
        for w in words:
            key = round(w[1] / 4)
            rows.setdefault(key, []).append(w)
        print('=====', f, 'page', pno + 1)
        for k in sorted(rows):
            ws = sorted(rows[k], key=lambda w: w[0])
            print(' '.join(w[4] for w in ws))
        break
