import sys,re
fn, pat, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
occ = int(sys.argv[4]) if len(sys.argv)>4 else -1
L = open(fn,encoding='utf-8').read().split('\n')
hits = [i for i,l in enumerate(L) if re.search(pat,l)]
print('hits',hits[:20])
if hits:
    i = hits[occ]
    print('\n'.join(L[i:i+n]))
