import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
fn, pat, w, mx = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
t = open(fn, encoding='utf-8').read()
last=-1; n=0
for m in re.finditer(pat, t):
    if m.start()<last: continue
    pg = re.findall(r'=== pdf page (\d+)', t[:m.start()])
    print(f'--- pdf p.{pg[-1] if pg else "?"}:', t[max(0,m.start()-w):m.end()+w].replace('\n',' / '))
    last=m.end()+w; n+=1
    if n>=mx: break
