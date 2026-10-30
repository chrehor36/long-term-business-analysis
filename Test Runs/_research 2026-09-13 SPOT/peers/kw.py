import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
fn = sys.argv[1]; pat = sys.argv[2]; w = int(sys.argv[3]) if len(sys.argv)>3 else 300; mx = int(sys.argv[4]) if len(sys.argv)>4 else 30
t = open(fn, encoding='utf-8').read()
n=0
for m in re.finditer(pat, t, flags=re.I):
    s = max(0, m.start()-w); e = min(len(t), m.end()+w)
    print(f'--- @{m.start()}:', t[s:e].replace('\n',' ¶ '))
    n+=1
    if n>=mx: break
print('TOTAL matches:', len(re.findall(pat,t,flags=re.I)))
