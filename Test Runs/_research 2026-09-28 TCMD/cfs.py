import re,glob
for fn in sorted(glob.glob('cache/k_*.txt'))+sorted(glob.glob('cache/q_2026-06-30.txt')):
    t=open(fn,encoding='utf-8').read()
    # find cash flow statement: the occurrence of "Cash flows from operating activities" followed by "Net cash provided by"
    idx=[m.start() for m in re.finditer(r'(?i)cash flows? from operating activities',t)]
    best=None
    for i in idx:
        seg=t[i:i+6000]
        if re.search(r'(?i)net cash (provided by|used in|\(used in\) provided by|provided by \(used in\))',seg) and re.search(r'(?i)depreciation',seg):
            best=i;break
    print('=====',fn)
    if best is None: print('NOT FOUND'); continue
    j=t.find('Supplemental',best)
    end=min(best+9000, j+1500 if j>0 else best+9000)
    print(t[best-600:end])
