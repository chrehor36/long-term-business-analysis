import re,glob,sys
for fn in sorted(glob.glob('tenk_*.txt')):
    t=open(fn,encoding='utf-8').read()
    t=re.sub(r'[ \t]*\|[ \t]*',' | ',t); t=re.sub(r'(\|\s*)+','| ',t); t=re.sub(r'\s+',' ',t)
    i=t.find('Segment operating profit')
    if i<0: i=t.find('segment operating profit')
    j=t.find('Revenues: | Marine transportation')
    if j<0: j=t.find('Revenues: Marine transportation')
    print('=====',fn); print(t[j:j+900] if j>=0 else 'NOREV')
