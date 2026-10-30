import re,sys
fn=sys.argv[1]; needle=sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 9000
t=open(fn,encoding='utf-8').read()
lines=t.split('\n')
t='\n'.join(lines[5:])
j=t.find('Business Combinations')
while j>0:
    seg=t[j:j+n]
    if 'consideration transferred' in seg and needle in seg:
        print(seg); break
    j=t.find('Business Combinations', j+10)
else:
    print('NOT FOUND via BC header; falling back to needle search')
    k=t.find(needle)
    print(t[k-200:k+n])
