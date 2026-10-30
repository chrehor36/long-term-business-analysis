"""Dump PDF pages as rows; decode text whose font has a +31 shifted encoding. Usage: decode_pages.py file.pdf page1 page2 ..."""
import sys, warnings
warnings.filterwarnings('ignore')
import fitz
f = sys.argv[1]; pages = [int(x) for x in sys.argv[2:]]
d = fitz.open(f)
def dec(s):
    out = []
    for c in s:
        o = ord(c)
        out.append(chr(o + 31) if o < 0x60 else c)
    return ''.join(out)
for pn in pages:
    p = d[pn - 1]
    print(f'===== page {pn}')
    rows = {}
    for b in p.get_text('rawdict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                txt = ''.join(ch['c'] for ch in s['chars'])
                if not txt.strip():
                    continue
                y = round(s['bbox'][1] / 3)
                rows.setdefault(y, []).append((s['bbox'][0], txt, s['font']))
    for y in sorted(rows):
        print(' | '.join(f"{dec(t) if not any(ch.isdigit() for ch in t) and any(c.isupper() for c in t) and '+' not in font else t}" for x, t, font in sorted(rows[y])))
