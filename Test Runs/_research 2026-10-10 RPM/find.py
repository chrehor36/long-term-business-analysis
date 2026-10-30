"""Search cached filings with whitespace normalized. Usage: python find.py FILE PATTERN [width]"""
import re, sys
t = re.sub(r'\s+', ' ', open(sys.argv[1], encoding='utf-8', errors='replace').read())
w = int(sys.argv[3]) if len(sys.argv) > 3 else 300
for m in list(re.finditer(sys.argv[2], t, re.I))[:6]:
    print('...', t[max(0,m.start()-w):m.end()+w], '...\n')
