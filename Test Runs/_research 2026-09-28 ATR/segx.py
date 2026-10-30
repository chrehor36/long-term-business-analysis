import re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
# Print the segment note of each 10-K: every line from the segment-information heading
# that carries a label and numbers, so the Pharma rows (sales, segment income / Adjusted
# EBITDA, depreciation, assets) can be read as filed.
for p in sorted(glob.glob('cache/k_*.txt')):
    yr = p[8:12]
    if len(sys.argv) > 1 and yr not in sys.argv[1:]: continue
    L = open(p, encoding='utf-8').read().split('\n')
    hs = [i for i, l in enumerate(L) if re.search(r'SEGMENT INFORMATION', l) and not re.search(r'Note \d+ [—–-] Segment|see Note', l, re.I)]
    if not hs: print(yr, 'no heading'); continue
    i0 = hs[-1]
    # join wrapped lines: older filings put label and numbers on separate lines
    txt = ' '.join(x.strip() for x in L[i0:i0 + 700])
    txt = re.sub(r'\s*\|\s*', ' ', txt); txt = re.sub(r'\s+', ' ', txt)
    print('=====', yr, 'line', i0)
    print(txt[:9000])
    print()
