import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
R = 'Test Runs/_research 2026-09-29 PAYO/'
def norm(t): return re.sub(r'\s+', ' ', t.replace('​',' ').replace('\xa0',' '))
docs = {f: norm(open(R+f+'.txt', encoding='utf-8').read()) for f in ['s4a3','k2112','k2212','k2312','k2412','k2512','q2606']}
for p in sys.argv[1:]:
    print(p[:60], {f: t.count(norm(p)) for f, t in docs.items()})
