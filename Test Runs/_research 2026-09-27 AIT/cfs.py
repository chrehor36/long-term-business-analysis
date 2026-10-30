import re, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
out = open('cfs_blocks.txt', 'w', encoding='utf-8')
files = sorted(glob.glob('flat/*_EX13_*.txt')) + sorted(glob.glob('flat/*_10-K_*.txt')) + sorted(glob.glob('flat/*_10-K405_*.txt'))
for f in sorted(files, key=lambda x: x.split('/')[-1][:10]):
    s = open(f, encoding='utf-8').read().split('\n')
    idx = [i for i, l in enumerate(s) if re.search(r'Cash Flows from Operating Activities', l, re.I)]
    if not idx:
        out.write(f'== {f} NO CFS\n'); continue
    best = None
    for i in idx:
        blk = s[i:i + 80]
        if any(re.search(r'Net cash|Cash provided by', x, re.I) for x in blk[:40]):
            best = i; break
    if best is None: continue
    out.write(f'== {f}\n')
    for l in s[max(0, best - 5):best + 70]:
        out.write('   ' + l.strip()[:260] + '\n')
        if re.search(r'Cash and Cash Equivalents at End', l, re.I): break
out.close()
