# Check: no E-ids; every M/L/R id in the ledger; every quoted fragment adjacent to an id is in that row (normalized).
import re,csv,sys,io,unicodedata
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
run=open(sys.argv[1],encoding='utf-8').read()
R={r['﻿id']:r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2],encoding='utf-8'))}
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('’',"'"),('‘',"'"),('“','"'),('”','"'),('—','-'),('–','-'),('�','')]: s=s.replace(a,b)
    s=s.replace('"','').replace("'",'')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
e=re.findall(r'\[E\d+-\d+\]',run)
if e: print('E-ids found',e); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in R: print('MISSING id',i); bad+=1
# fragments: a "quoted" span followed within 40 chars by **[ID]** (possibly several ids)
checked=0
for m in re.finditer(r'"([^"\n]{12,}?)"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    frag,i=m.group(1),m.group(2); checked+=1
    parts=[p for p in re.split(r'\[\.\.\.\]|\.\.\.',frag) if p.strip()]
    if i in R and not all(norm(p) in norm(R[i]) for p in parts):
        print('FRAGMENT NOT IN ROW',i,'::',frag[:120]); bad+=1
print('ids',len(set(ids)),'fragments checked',checked,'problems',bad)
# broader pass: for each id, the last quoted span within 250 chars before it (same paragraph) is reported if not in the row
print('--- broad pass (review by hand; a quote from a filing near an id is expected to show here) ---')
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    i=m.group(1); pre=run[max(0,m.start()-250):m.start()]
    pre=pre.split('\n\n')[-1]
    qs=re.findall(r'"([^"]{8,}?)"',pre)
    if not qs: continue
    q=qs[-1]; parts=[p for p in re.split(r'\[\.\.\.\]',q) if p.strip()]
    if not all(norm(p) in norm(R.get(i,'')) for p in parts):
        print(i,'::',q[:110])
