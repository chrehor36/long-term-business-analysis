import re,sys
def norm(t):
    t=re.sub(r'[ \t]*\|[ \t]*',' | ',t); t=re.sub(r'(\|\s*)+','| ',t); return re.sub(r'\s+',' ',t)
fn=sys.argv[1]
t=norm(open(fn,encoding='utf-8').read())
i=t.find('Cash flows from operating activities')
if i<0: i=t.find('Operating activities:')
print(t[i:i+4500])
