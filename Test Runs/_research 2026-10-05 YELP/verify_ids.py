import csv,re,sys
RUN='../2026-10-05 Run - YELP Yelp.md'
s=open(RUN,encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
bad=0
e=re.findall(r'\[E\d+-\d+\]',s); print('E-ids:',e); bad+=len(e)
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s)
miss=[i for i in ids if i not in rows]; print('ids cited',len(ids),'distinct',len(set(ids)),'missing',miss); bad+=len(miss)
norm=lambda t:re.sub(r'\s+',' ',t.replace('’',"'").replace('“','"').replace('”','"'))
# for each id occurrence, take text since previous id (or paragraph start) and check every plain "..." quote
pos=0; checked=0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s):
    start=max(s.rfind('**[',0,m.start()-1) if s.rfind('**[',0,m.start()-1)>=pos else -1, s.rfind('\n\n',0,m.start()))
    seg=s[max(start,0):m.start()]
    # drop italic filing quotes *"..."*
    seg2=re.sub(r'\*"[^"]*"\*','',seg)
    for q in re.findall(r'"([^"\n]{3,}?)"',seg2.replace('\n',' ')):
        frags=[f.strip(' .,') for f in re.split(r'\[\.\.\.\]',q) if f.strip(' .,')]
        for f in frags:
            checked+=1
            if norm(f) not in norm(rows[m.group(1)].replace('\n',' ')):
                print('NOT IN ROW',m.group(1),'::',f[:120]); bad+=1
print('fragments checked',checked)
print('em dashes outside the label:', s.count('—')-s.count('COMPUTATION — NOT A CLEARANCE')-s.count('"COMPUTATION — NOT A\nCLEARANCE"'))
print('FAIL' if bad else 'PASS')
