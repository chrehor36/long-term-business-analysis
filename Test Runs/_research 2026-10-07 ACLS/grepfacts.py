import re,sys
sys.stdout.reconfigure(encoding='utf-8')
pats=[r'[Bb]acklog[^.]{0,60}was \$[0-9.,]+ million[^.]{0,140}', r'Bookings in the quarter[^.]{0,200}', r'(CS&I|aftermarket)[^.]{0,80}\$[0-9.]+ million[^.]{0,160}', r'top ten customers accounted for [0-9.]+%[^.]{0,100}', r'one customer accounted for[^.]{0,100}', r'(two|three) customers[^.]{0,30}accounted[^.]{0,120}']
for f in sys.argv[1:]:
    t=re.sub(r'\s+',' ',open(f,encoding='utf-8').read())
    print('==',f)
    for p in pats:
        for m in list(re.finditer(p,t))[:2]: print('  ',m.group(0)[:330])
