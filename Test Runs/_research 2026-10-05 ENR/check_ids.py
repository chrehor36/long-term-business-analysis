import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
P='Test Runs/2026-10-05 Run - ENR Energizer.md'
t=open(P,encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
print('em dashes:',t.count('—'),' en dashes:',t.count('–'))
print('E-ids:',re.findall(r'\bE[1-5]-\d{2}\b',t))
ids=set(re.findall(r'\b[MLR](?:19|20)\d{2}-\d{3}\b',t)); miss=[i for i in ids if i not in rows]
print('distinct ids',len(ids),'missing',miss)
bad=0;n=0
for m in re.finditer(r'"([^"]+)"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,i=m.group(1),m.group(2); n+=1
    for part in re.split(r'\s*\[\.\.\.\]\s*',frag):
        p=re.sub(r'\s+',' ',part).strip().rstrip('.')
        if p and p not in re.sub(r'\s+',' ',rows[i]):
            bad+=1; print('NOT IN ROW',i,'|',part)
print('quote-id pairs',n,'bad',bad)
# ids not directly after a quote: list for manual review
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    pre=t[max(0,m.start()-6):m.start()]
    if '"' not in pre and ')' not in pre: print('id not after quote:',m.group(1),'|',t[max(0,m.start()-90):m.start()].replace('\n',' '))
