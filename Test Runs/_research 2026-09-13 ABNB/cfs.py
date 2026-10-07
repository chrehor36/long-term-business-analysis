import sys, re
for fn in sys.argv[1:]:
    L = open(fn, encoding='utf-8').read().split('\n')
    idx = [i for i,l in enumerate(L) if 'Cash flows from operating activities' in l]
    print('=====', fn, idx[:5])
    for i in idx:
        # take the one followed within 40 lines by 'Net cash provided by'
        blk = L[i-8:i+75]
        if any('investing activities' in b for b in blk):
            for b in blk:
                print(b[:230])
                if 'end of year' in b or 'end of period' in b: break
            break
