"""Rows of a PDF page with span text; spans in fonts whose glyphs are offset (custom-encoded subset) decoded by +29/+31 trial.
Usage: summary_rows.py file.pdf pageindex(1-based) ..."""
import sys, warnings
warnings.filterwarnings('ignore')
import fitz
d = fitz.open(sys.argv[1])
def dec(s):
    # the report's label fonts map 'R'->'3' etc: add 31 to chars below 0x60
    return ''.join(chr(ord(c) + 29) if ord(c) < 0x60 and c not in ' ,.()-%' else c for c in s)
for pn in map(int, sys.argv[2:]):
    p = d[pn - 1]
    rows = {}
    for b in p.get_text('rawdict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                t = ''.join(c['c'] for c in s['chars'])
                if t.strip():
                    rows.setdefault(round(s['bbox'][1] / 4), []).append((s['bbox'][0], t, s['font']))
    print(f'===== page {pn}')
    for y in sorted(rows):
        print(' | '.join(t for x, t, f in sorted(rows[y])))
