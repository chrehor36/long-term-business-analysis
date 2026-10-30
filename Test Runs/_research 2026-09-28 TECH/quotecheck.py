import re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
t = open('../2026-09-28 Run - TECH Bio-Techne.md', encoding='utf-8').read()
qs = re.findall(r'\*"(.+?)"\*', t)
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('\xa0', ' ')
    s = s.replace('​', ' ')
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'(\|\s*)+\|', '|', s)
    return s.strip().lower()
corpus = ''
for p in glob.glob('cache/*.txt') + glob.glob('cache/peers/*.txt') + glob.glob('*_out.txt') + glob.glob('sub_list.txt') + glob.glob('_BRIEF.md') + ['../../principle_ledger.csv', '../../Framework/THE FRAMEWORK v4.md', '../../tools/alerts.json']:
    corpus += norm(open(p, encoding='utf-8', errors='ignore').read()) + ' '
corpus_nospace = corpus.replace(' ', '')
miss = []
for q in qs:
    parts = [x for x in re.split(r'\.\.\.|\[\.\.\.\]|\[[^\]]*\]', q) if len(x.strip()) > 12]
    ok = all(norm(x).replace(' ', '') in corpus_nospace for x in parts) if parts else True
    if not ok: miss.append(q)
print('quotes', len(qs), 'unmatched', len(miss))
for m in miss: print(' -', m[:200])
