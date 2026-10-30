import re, glob, sys, io, csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
run = open(r'..\2026-09-27 Run - AIT Applied Industrial Technologies.md', encoding='utf-8').read()
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('\xa0', ' ').replace('�', "'")
    s = re.sub(r'\s*\|\s*', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()
corpus = ''
for f in glob.glob('flat/*.txt') + glob.glob('filings/*.txt'):
    corpus += norm(open(f, encoding='utf-8').read()) + ' '
corpus += norm(open(r'..\_research 2026-09-26 GPC\k25_gpc-20251231.htm.txt', encoding='utf-8').read())
for r in csv.reader(open(r'..\..\principle_ledger.csv', encoding='utf-8-sig')):
    corpus += ' ' + norm(r[2])
corpus += ' ' + norm(open(r'..\..\Framework\THE FRAMEWORK v4.md', encoding='utf-8').read())
qs = re.findall(r'\*"(.+?)"\*', run)
bad = 0
for q in qs:
    parts = [p.strip() for p in re.split(r'\s*(?:\.\.\.|\[\.\.\.\]|…)\s*', q) if p.strip()]
    ok = all(norm(p).strip(' .,;') in corpus for p in parts)
    if not ok:
        bad += 1; print('NOT FOUND:', q[:200])
print(len(qs), 'quotes,', bad, 'not found')
