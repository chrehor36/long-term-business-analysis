# Verify every blockquoted line of PEERS.md against the saved source texts.
# Normalizes whitespace, quote marks, hyphen variants and table pipes only.
import sys, io, re, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def norm(s):
    s = s.replace('­', '').replace('‑', '-').replace('–', '-').replace('—', '-')
    s = re.sub(r'[“”"]', '"', s)
    s = re.sub(r"[‘’']", "'", s)
    s = re.sub(r'\s*\|\s*', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


srcs = [f for f in glob.glob('*.txt') if not f.endswith('.flat.txt')] + glob.glob('deezer/*.txt') + [
    '../../_research 2026-09-13 SONY/peers_music/UMG_AR_2025.cols.txt',
    '../../_research 2026-09-13 SONY/peers_music/UMG_AR_2024.cols.txt',
    '../../_research 2026-09-13 SONY/20F_FY2026.txt',
    '../20F_FY2025__ck0001639920-20251231.txt']
texts = [norm(open(f, encoding='utf-8').read()) for f in srcs]


def found(q):
    return any(q in t for t in texts)


md = open('PEERS.md', encoding='utf-8').read()
n = miss = 0
for line in md.splitlines():
    if not line.startswith('> "'):
        continue
    for s in re.split(r'" / "', line[3:]):
        j = s.rfind('"')
        q = s[:j] if j > 0 else s
        n += 1
        qn = norm(q).rstrip('.;,')
        if found(qn):
            continue
        pieces = [p.strip(' .,;') for p in qn.split('"') if len(p.strip()) > 15]
        ok = pieces and all(found(p) for p in pieces)
        miss += 1
        print('PIECES-OK' if ok else 'MISS', '::', q[:220])
print('checked', n, 'not found whole', miss)
