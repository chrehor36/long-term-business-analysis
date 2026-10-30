import re, sys, io, csv, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
R = 'Test Runs/_research 2026-09-29 PAYO/'
def norm(t):
    t = t.replace('​',' ').replace('\xa0',' ').replace('�',' ')
    t = t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.sub(r'\s+', ' ', t).strip()
run = open('Test Runs/2026-09-29 Run - PAYO Payoneer Global.md', encoding='utf-8').read()
srcs = [f for f in glob.glob(R+'*.txt') if not f.endswith('_msg.txt')] + [R+'px_1y.json']
corpus = ' '.join(norm(open(f, encoding='utf-8', errors='replace').read()) for f in srcs)
corpus += ' ' + norm(open('principle_ledger.csv', encoding='utf-8').read())
corpus += ' ' + norm(open('Framework/THE FRAMEWORK v4.md', encoding='utf-8').read()).replace('**','')
corpus += ' ' + norm(open('Screens/WATCHLIST RUN QUEUE.md', encoding='utf-8').read())
corpus += ' ' + norm(open('Screens/2026-09-02 MASTER RUN QUEUE (corrected).csv', encoding='utf-8', errors='replace').read())
quotes = re.findall(r'\*"(.+?)"\*', run)
miss = 0
for q in quotes:
    parts = [p.strip() for p in re.split(r'\s*(?:\.\.\.|…|\[\.\.\.\])\s*', norm(q)) if p.strip()]
    if not all(p in corpus for p in parts):
        miss += 1; print('UNMATCHED:', q[:160])
print(len(quotes), 'quotations,', miss, 'unmatched')
ids = sorted(set(re.findall(r'E\d-\d{2}', run)))
led = {r['﻿id'] if '﻿id' in r else r['id'] for r in csv.DictReader(open('principle_ledger.csv', encoding='utf-8'))}
print(len(ids), 'ledger ids cited; missing:', [i for i in ids if i not in led])
