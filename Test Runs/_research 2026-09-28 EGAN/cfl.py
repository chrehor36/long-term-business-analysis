import re
keys=['Net cash provided by','Net cash (used in)','Net cash used in operating','Stock-based compensation |','Deferred revenue |','Purchases of property','Repurchases of common','Accounts receivable |','Capitalized','Issuance of common stock warrant','Proceeds from','Payments on','Borrowings','Repayment','related party']
for y in range(2006,2027):
    try: t=open(f'cache/k{y}.txt',encoding='utf-8').read().split('\n')
    except: continue
    s=[i for i,l in enumerate(t) if re.match(r'\s*Cash flows from operating activities',l)]
    if not s: print(y,'no CF'); continue
    i=s[0]; blk=t[i:i+75]
    print('=====',y)
    for l in blk:
        l=l.replace('​','').replace(' | ',' ').strip()
        if any(k.replace(' |','') in l for k in keys): print('  ',l[:170])
        if 'at end of' in l: break
