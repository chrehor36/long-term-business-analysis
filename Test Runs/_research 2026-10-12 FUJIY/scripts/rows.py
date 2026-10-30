"""Print PDF page text as rows (words grouped by y). Usage: rows.py file.pdf keyword [keyword2]"""
import sys, warnings
warnings.filterwarnings('ignore')
import fitz
f, kws = sys.argv[1], sys.argv[2:]
d = fitz.open(f)
for i, p in enumerate(d):
    t = p.get_text()
    if all(k in t for k in kws):
        print(f'===== page {i+1}')
        rows = {}
        for w in p.get_text('words'):
            rows.setdefault(round(w[1] / 4), []).append(w)
        for y in sorted(rows):
            print(' '.join(w[4] for w in sorted(rows[y], key=lambda w: w[0])))
