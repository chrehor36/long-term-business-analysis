import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
for fn in sys.argv[1:]:
    t=open(fn,encoding='utf-8').read()
    i=t.find('Operating Income (Loss) by Business Segment')
    if i<0: i=t.find('Operating Income by Business Segment')
    j=t.rfind('Net Sales by Business Segment',0,i)
    if j<0 or i-j>6000: j=i-3000
    seg=t[j:i+900]
    flat=re.sub(r'[|$\n\u200b]',' ',seg); flat=re.sub(r'\s+',' ',flat); flat=re.sub(r'\(\s+','(',flat); flat=re.sub(r'\s+\)',')',flat)
    print('==',fn); print(flat[:1400])
