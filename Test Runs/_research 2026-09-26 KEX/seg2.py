import re,glob
def norm(t):
    t=re.sub(r'[ \t]*\|[ \t]*',' | ',t); t=re.sub(r'(\|\s*)+','| ',t); return re.sub(r'\s+',' ',t)
for fn in sorted(glob.glob('tenk_*.txt')):
    t=norm(open(fn,encoding='utf-8').read())
    print('=====',fn)
    for m in re.finditer(r'Operating margins? \| [\d.]+ ?%[^A-Za-z]{0,80}',t):
        print('  ',t[max(0,m.start()-420):m.end()][-520:])
        break
    for m in re.finditer(r'Segment (operating )?profits?( \(loss\))?: \| Marine transportation[^A-Za-z]{0,120}(Distribution and services|Diesel engine services)[^A-Za-z]{0,120}',t):
        print(' SEG',m.group(0)[:400]); break
