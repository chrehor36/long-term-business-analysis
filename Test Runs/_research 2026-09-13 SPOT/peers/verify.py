# Search every blockquoted "..." string of PEERS.md in the source texts (normalized whitespace/quotes/hyphens).
import sys, io, re, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
def norm(s):
    s = s.replace('­','').replace('‑','-').replace('‑','-').replace('–','-').replace('—','-')
    s = re.sub(r'[“”"]', '"', s); s = re.sub(r"[‘’']", "'", s)
    s = re.sub(r'\s*\|\s*', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()
srcs = [f for f in glob.glob('*.txt') if not f.endswith('.flat.txt')] + glob.glob('deezer/*.txt') + \
       ['../../_research 2026-09-13 SONY/peers_music/UMG_AR_2025.cols.txt','../../_research 2026-09-13 SONY/peers_music/UMG_AR_2024.cols.txt',
        '../../_research 2026-09-13 SONY/20F_FY2026.txt','../20F_FY2025__ck0001639920-20251231.txt']
texts = {f: norm(open(f, encoding='utf-8').read()) for f in srcs}
md = open('PEERS.md', encoding='utf-8').read()
n=miss=0
for line in md.splitlines():
    if not line.startswith('>'): continue
    for q in re.findall(r'"(.{25,}?)"(?=\s*(?:\(|$|/|\.|,))', line):
        n+=1
        qn = norm(q).rstrip('.')
        # split at ellipsis-free chunks
        hit = [f for f,t in texts.items() if qn in t]
        if not hit:
            # try shorter: first 60 and last 60 chars
            a, b = qn[:60], qn[-60:]
            part = [f for f,t in texts.items() if a in t and b in t]
            miss+=1
            print('MISS' if not part else 'PARTIAL(ends found)', '::', q[:160], '::', part[:2])
print('quotes checked', n, 'not found whole', miss)
