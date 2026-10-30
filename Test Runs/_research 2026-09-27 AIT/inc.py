import re, glob, json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def nums(s):
    s = s.replace('|', ' ')
    s = re.sub(r'\(\s*([\d,\.]+)\s*\)?', r'()', s)
    s = s.replace('—', ' 0 ')
    toks = re.findall(r'\(?\$?\s?[\d][\d,]*\)?', s)
    out = []
    for t in toks:
        neg = t.startswith('(')
        v = re.sub(r'[^\d]', '', t)
        if v == '': continue
        out.append(-int(v) if neg else int(v))
    return out
LAB = {'sales': r'^\s*net sales\s*\|?\s*\$', 'cogs': r'^\s*cost of sales\s*\|?\s*[\$\d]', 'gp': r'^\s*gross profit\s*\|?\s*[\$\d]',
       'sda': r'^\s*selling, distribution,? and administrative[^|]*\|?\s*[\$\d]', 'oi': r'^\s*operating income\s*\|?\s*[\$\d]'}
out = {}
files = sorted(glob.glob('flat/*_EX13_*.txt') + glob.glob('flat/*_10-K_*.txt') + glob.glob('flat/*_10-K405_*.txt'), key=lambda x: x.replace(chr(92), '/').split('/')[-1][:10])
for f in files:
    s = open(f, encoding='utf-8').read().split('\n')
    fy = int(f.replace(chr(92), '/').split('/')[-1][:4])
    got = {}
    for l in s:
        for k, p in LAB.items():
            if k in got: continue
            if re.search(p, l, re.I):
                v = nums(l.split('$', 1)[1] if '$' in l else re.split(r'[a-z]\s', l, flags=re.I)[-1])
                if len(v) >= 3 and abs(v[0]) > 1000: got[k] = v[:3]
    if got:
        for i, y in enumerate((fy, fy - 1, fy - 2)):
            for k, v in got.items():
                out.setdefault(y, {})[k] = v[i]
json.dump(out, open('inc.json', 'w'), indent=0)
for y in sorted(out):
    d = out[y]; s_ = d.get('sales')
    if not s_: continue
    gp = d.get('gp') or (s_ - d['cogs'] if 'cogs' in d else None)
    oi = d.get('oi')
    print(y, s_, gp, oi, f"GM {gp/s_*100:.1f}%" if gp else '', f"OM {oi/s_*100:.1f}%" if oi else '')
