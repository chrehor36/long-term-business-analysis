import re,sys
for y in sys.argv[1:]:
    s=open('cache/tenk_%s.txt'%y,encoding='utf-8').read().replace('​',' ')
    s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\s+',' ',s)
    print('==',y)
    for m in re.finditer(r'(Net capital expenditures|Capital expenditures, gross|Capital expenditures)[^\d$]{0,160}\$? ?[\d,]+[\d,$() ]{0,80}',s):
        print('  ',m.group(0)[:330].encode('ascii','replace').decode())
