import re,sys
for y in sys.argv[1:]:
    s=open('cache/tenk_%s.txt'%y,encoding='utf-8').read().replace('​',' ')
    s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\s+',' ',s)
    for m in re.finditer(r'(IDENTIFIABLE ASSETS|Identifiable assets|TOTAL ASSETS BY SEGMENT|Segment assets|SEGMENT ASSETS)[^%]{0,400}',s):
        print('==',y,m.group(0)[:420].encode('ascii','replace').decode())
