# Check the LONKF run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that
# directly precedes an id (within the same clause) is found in that row (elisions [...] split the fragment).
import csv,re,sys
RUN="Test Runs/2026-10-13 Run - LONKF Lonking Holdings.md"
rows={}
for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig')): rows[r['id']]=r['quote_verbatim']
s=open(RUN,encoding='utf-8').read()
def norm(t):
    t=t.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\ufffd','')
    t=t.replace('**','')
    return re.sub(r'\s+',' ',t).strip().lower()
bad=0
eids=re.findall(r'\[E\d-\d+\]',s)
if eids: print('E-ids found:',eids); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# quoted fragment immediately before an id: pattern "...." then up to 40 non-quote chars then **[ID]**
n=0
for m in re.finditer(r'"([^"]{3,600})"([^"\n]{0,60}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s,flags=re.S):
    frag,mid,i=m.group(1),m.group(2),m.group(3)
    if '**[' in mid: continue
    row=norm(rows.get(i,''))
    for piece in re.split(r'\[\.\.\.\]',frag):
        piece=norm(piece).strip(' .,;:')
        if piece and piece not in row:
            print(f'FRAGMENT NOT IN {i}: "{piece[:120]}"'); bad+=1
    n+=1
print(f'{len(set(ids))} distinct ids, {len(ids)} citations, {n} quoted fragments checked; problems: {bad}')
sys.exit(1 if bad else 0)
