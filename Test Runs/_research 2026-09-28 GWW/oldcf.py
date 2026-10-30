import glob,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
labs=['Net cash provided by operating activities','Additions to property, buildings,? and equipment','Additions to property, buildings, equipment and capitalized software','Capital expenditures','Property, buildings,? and equipment','Intangibles and goodwill','Goodwill and other intangibles','Capitalized software','Stock-based compensation','Stock based compensation','Net cash paid for business acquisitions?','Cash paid for business acquisitions?','Net earnings','Depreciation and amortization','Amortization of restricted stock','Restricted stock','pro forma']
NUM=r'\(?-?[\d,]+(?:\.\d+)?\)?'
for y in range(1993,2009):
    fs=[f for f in glob.glob(f'cache/k{y}_*.txt') if 'xex' not in f]
    fs.sort(key=lambda f: ('exhibit13' not in f, f))
    f=fs[0]
    t=open(f,encoding='utf-8').read()
    i=t.lower().find('cash flows from operating activities')
    idxs=[m.start() for m in re.finditer(r'(?i)cash flows from operating activities',t)]
    # choose the occurrence followed by 'Net earnings' within 400 chars
    st=None
    for k in idxs:
        if re.search(r'(?i)net earnings',t[k:k+600]): st=k
    if st is None: print(y,'no CF'); continue
    blk=t[st:st+9000]
    blk=re.sub(r'[\s|$]+',' ',blk); blk=re.sub(r'\.{2,}',' ',blk); blk=re.sub(r'\( (\d)',r'(\1',blk); blk=re.sub(r'(\d) \)',r'\1)',blk)
    print('=====',y,f)
    for lab in labs:
        for m in re.finditer('(?i)'+lab+r'[^0-9(]{0,60}?((?:'+NUM+r' ){2,3}'+NUM+r'?)',blk):
            print('  ',lab[:40],'->',m.group(1)[:60])
