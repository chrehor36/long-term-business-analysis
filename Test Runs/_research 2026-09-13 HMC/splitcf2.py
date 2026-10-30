import fitz, glob, re
out = open('splitcf_rows.txt', 'w', encoding='utf-8')
for p in sorted(glob.glob('ir/pdf/*reference*.pdf')):
    d = fitz.open(p)
    for pg in d:
        t = pg.get_text()
        if 'Cash Flows' not in t or 'Divided into' not in t: continue
        words = pg.get_text('words')  # x0,y0,x1,y1,word,block,line,wordno
        rows = {}
        for w in words:
            y = round((w[1] + w[3]) / 2 / 3)  # bucket 3pt
            rows.setdefault(y, []).append(w)
        out.write(f'===== {p} page {pg.number+1}\n')
        prev = None
        for y in sorted(rows):
            ws = sorted(rows[y], key=lambda w: w[0])
            line = ''
            lastx = None
            for w in ws:
                if lastx is not None and w[0] - lastx > 12: line += ' | '
                elif lastx is not None: line += ' '
                line += w[4]; lastx = w[2]
            out.write(line + '\n')
out.close()
