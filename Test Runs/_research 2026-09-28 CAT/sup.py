import re,sys
sys.stdout.reconfigure(encoding='utf-8')
def doc(y):
    f=f'cache/x13_{y}.txt' if y<=2014 else f'cache/k_{y}.txt'
    return open(f,encoding='utf-8').read()
rows=['Net cash provided by (used for) operating activities','Capital expenditures','Expenditures for equipment leased to others','Depreciation and amortization','Profit of consolidated and affiliated companies','Undistributed profit','Dividends paid','Profit after tax']
num=r'(?:\(?\$?\s?[\d,]+\s?\)?|—|-)'
for y in range(int(sys.argv[1]),int(sys.argv[2])+1):
    t=doc(y)
    t=re.sub(r'[\s|$]+',' ',t)
    idxs=[m.start() for m in re.finditer(r'Supplemental [Dd]ata for (?:Statement of )?[Cc]ash [Ff]low',t)]
    print('=====',y,len(idxs))
    for i in idxs[:1]:
        blk=t[i:i+20000]
        print(' HDR',blk[:420])
        for r in rows:
            m=re.search(re.escape(r)+r'[^0-9(—]{0,120}((?:'+num+r' ){4,12})',blk)
            if m: print('   ',r[:45],'::',m.group(1))
