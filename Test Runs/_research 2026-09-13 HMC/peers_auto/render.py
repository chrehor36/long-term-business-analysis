"""Render PDF pages to PNG for visual reading of chart slides. usage: python render.py PDF page[,page] [zoom]"""
import sys, os
import pymupdf

pdf, pages = sys.argv[1], [int(p) for p in sys.argv[2].split(",")]
zoom = float(sys.argv[3]) if len(sys.argv) > 3 else 1.6
doc = pymupdf.open(pdf)
for p in pages:
    pix = doc[p - 1].get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
    out = f"{os.path.splitext(pdf)[0]}_p{p}.png"
    pix.save(out)
    print(out)
