import re, glob, sys
pats=[r'Reimbursed out-of-pocket (?:revenue|expenses) \| [0-9,]+ \| [0-9,]+',
r'Net new business awards were \$[0-9.,]+ (?:million|billion)[^.]*\.',
r'backlog (?:increased|decreased) by [^|]{0,200}',
r'[^.]{0,80}top (?:five|ten|20) customers[^.]*\.',
r'[^.]{0,200}competitive bidding[^.]*\.',
r'[^.]{0,200}favorable pricing terms[^.]*\.',
r'[^.]{0,200}cancellations? (?:were|was|of|totaled)[^.]*\.',
]
if len(sys.argv)>1: pats=[sys.argv[1]]
for f in sorted(glob.glob('filings/*_10-K_*')):
    t=open(f,encoding='utf-8').read(); t=re.sub(r'\s+',' ',t)
    print('===',f[8:30])
    for p in pats:
        for m in list(dict.fromkeys(re.findall(p,t)))[:3]: print('  ',m[:600])
