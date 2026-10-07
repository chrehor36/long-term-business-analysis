import re, glob, csv, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
files = sys.argv[1:]
def norm(t):
    t = unicodedata.normalize('NFKC', t)
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('�', "'")
    t = re.sub(r'[\s|]+', ' ', t)
    return t.lower()
corpus = ''
import os
for fn in glob.glob('cache/*.txt') + glob.glob('cache/peers/*.txt') + [x for x in ['sub_list.txt','series_out.txt','_BRIEF.md','runpy_out.txt','incst_out.txt','cover_shares_out.txt','step0_out.txt','../2026-09-07 Run - KLAC KLA.md'.replace('../','../'),'../../Test Runs/2026-09-07 Run - KLAC KLA.md'] if os.path.exists(x)]:
    corpus += norm(open(fn, encoding='utf-8', errors='ignore').read())
led = {r['id']: r for r in csv.DictReader(open('../../principle_ledger.csv', encoding='utf-8-sig'))}
corpus += norm(' '.join(r['quote_verbatim'] for r in led.values()))
for extra in ['../../Framework/THE FRAMEWORK v4.md', '../../Screens/SURVIVAL SHAPES - index.md', '../../Framework/v4/THE MANAGER STANDARD - Q3.md']:
    corpus += norm(open(extra, encoding='utf-8').read())
for f in files:
    s = open(f, encoding='utf-8').read()
    ids = set(re.findall(r'E\d-\d+', s))
    miss = [i for i in ids if i not in led]
    print(f, 'ids', len(ids), 'missing', miss)
    for q in re.findall(r'\*"(.+?)"\*', s):
        parts = [p.strip(' .,;') for p in re.split(r'\.\.\.|…|\[\.\.\.\]', q) if len(p.strip(' .,;')) > 3]
        bad = [p for p in parts if norm(p) not in corpus]
        if bad: print('  UNMATCHED:', q[:160], '||', bad[0][:80])
