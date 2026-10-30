import csv,sys
ids=set(sys.argv[2].split(','))
for r in csv.DictReader(open(sys.argv[1],encoding='utf-8')):
    if r[list(r.keys())[0]] in ids:
        k=list(r.keys())
        print(r[k[0]], '|', r.get('year',''), '|', [r[x] for x in k if 'quote' in x.lower() or 'text' in x.lower()][:1])
