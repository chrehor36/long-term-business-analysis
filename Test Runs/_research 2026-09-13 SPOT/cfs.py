import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
lab = sys.argv[1]; what = sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv)>3 else 5000
t = open(f'20F_{lab}.txt', encoding='utf-8').read()
idx = [m.start() for m in re.finditer(what, t)]
# take the last match that is followed by 'Operating activities' or numbers
start = idx[-1] if idx else None
print(lab, 'matches', len(idx))
for i in idx:
    print('--', i)
if start is not None:
    s=t[start:start+n]; s=re.sub(r'\s*\|\s*',' | ',s)
    print(s.replace('\n',' / '))
