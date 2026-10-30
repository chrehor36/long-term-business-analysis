"""Search PDF pages (fitz text) for a regex; print page and context. Usage: find.py file.pdf regex [width]"""
import sys, re, warnings
warnings.filterwarnings('ignore')
import fitz
d = fitz.open(sys.argv[1]); rx = re.compile(sys.argv[2], re.I); w = int(sys.argv[3]) if len(sys.argv) > 3 else 200
for i, p in enumerate(d):
    t = ' '.join(p.get_text().split())
    for m in rx.finditer(t):
        print(f'[p{i+1}] ...{t[max(0,m.start()-w):m.end()+w]}...')
