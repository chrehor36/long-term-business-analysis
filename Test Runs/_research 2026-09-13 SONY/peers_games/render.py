"""Render PDF pages matching a phrase to PNG so scrambled tables can be read off the page image.
usage: python render.py file.pdf "phrase" [maxpages]"""
import sys, os, pymupdf
pdf, phrase = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 3
doc = pymupdf.open(pdf)
n = 0
for i, p in enumerate(doc):
    if phrase.lower() in p.get_text().lower():
        out = "%s.p%d.png" % (os.path.splitext(pdf)[0], i + 1)
        p.get_pixmap(dpi=110).save(out)
        print(out)
        n += 1
        if n >= mx:
            break
