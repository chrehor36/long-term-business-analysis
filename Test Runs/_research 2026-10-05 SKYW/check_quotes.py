import csv,io,re,sys
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8-sig') as f:
    for r in csv.DictReader(f): rows[r['id']]=r['quote_verbatim']
t=io.open('Test Runs/2026-10-05 Run - SKYW SkyWest.md',encoding='utf-8').read()
norm=lambda s: re.sub(r'\s+',' ',s).strip()
ids=re.findall(r'\[([A-Z]\d{1,4}-\d{2,3})\]',t)
bad=[i for i in ids if i not in rows]
eids=[i for i in ids if i.startswith('E')]
print('ids cited',len(ids),'distinct',len(set(ids)),'missing',bad,'E-ids',eids)
# every "..." immediately before **[ID]** (allowing ' ... ' joins and short connectors)
fails=0;checked=0
for m in re.finditer(r'((?:"[^"]+"(?:\s*(?:\.\.\.|,|;|and|otherwise|:)?\s*)?)+)\s*(?:\n\s*)?\*\*\[([A-Z]\d{4}-\d{3})\]\*\*',t):
    block,i=m.group(1),m.group(2)
    for frag in re.findall(r'"([^"]+)"',block):
        checked+=1
        for piece in re.split(r'\s*\.\.\.\s*',frag):
            if piece and norm(piece) not in norm(rows[i]):
                fails+=1; print('FAIL',i,'|',piece[:120])
print('fragments checked',checked,'fails',fails)
