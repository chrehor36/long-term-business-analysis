import re, glob, sys, io, csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def norm(t):
    t = t.replace('​', '').replace('\xa0', ' ')
    t = re.sub(r'\s+', ' ', t)
    return t.lower()
corpus = ''
for f in glob.glob('flat/*.txt'):
    corpus += norm(open(f, encoding='utf-8').read()) + ' \n '
led = ' '.join(norm(r['quote_verbatim']) for r in csv.DictReader(open('../../principle_ledger.csv', encoding='utf-8-sig')))
fw = norm(open('../../Framework/THE FRAMEWORK v4.md', encoding='utf-8').read())
for body in sys.argv[1:]:
    s = open(body, encoding='utf-8').read()
    qs = re.findall(r'\*"(.+?)"\*', s)
    bad = 0
    for q in qs:
        parts = [p.strip() for p in re.split(r'\.\.\.|\[\.\.\.\]|…', q) if p.strip()]
        ok = True
        for p in parts:
            p2 = norm(re.sub(r'\[[^\]]*\]', '', p)).strip(' .,;:')
            if len(p2) < 4: continue
            if p2 not in corpus and p2 not in led and p2 not in fw:
                # try without trailing punctuation inside
                ok = False
        if not ok:
            bad += 1
            print('NOT FOUND:', q[:200])
    print(body, len(qs), 'quotes,', bad, 'not found')
