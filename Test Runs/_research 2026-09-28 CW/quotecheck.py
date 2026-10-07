import re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
t = open('../2026-09-28 Run - CW Curtiss-Wright.md', encoding='utf-8').read()
qs = re.findall(r'\*"(.+?)"\*', t)
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', s).strip().lower()
corpus = ''
for p in glob.glob('cache/*.txt') + ['../../principle_ledger.csv', '../../Framework/THE FRAMEWORK v4.md']:
    corpus += norm(open(p, encoding='utf-8', errors='ignore').read()) + ' '
corpus_nospace = corpus.replace(' ', '')
miss = []
for q in qs:
    parts = [x for x in re.split(r'\.\.\.|\[\.\.\.\]|\[[^\]]*\]', q) if len(x.strip()) > 12]
    ok = all(norm(x).replace(' ', '') in corpus_nospace for x in parts) if parts else True
    if not ok: miss.append(q)
print('quotes', len(qs), 'unmatched', len(miss))
for m in miss: print(' -', m[:200])
