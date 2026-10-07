import re,sys
fn=sys.argv[1]
t='\n'.join(open(fn,encoding='utf-8').read().split('\n')[5:])
for m in re.finditer(r'Subscription and support', t):
    seg=t[max(0,m.start()-600):m.start()+2000]
    if 'Total cost of revenues' in seg and 'Income from operations' in seg:
        print(seg); print('~~~~~~~~~~~~~~~~'); break
