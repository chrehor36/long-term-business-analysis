import sys, re
p, which = sys.argv[1], sys.argv[2]
labels = sys.argv[3:]
t = open(p, encoding='utf-8').read()
ms = [m.start() for m in re.finditer(r'Consolidated Statements of '+which+r'[^\n]*\n[\s|]*(December 31|Year Ended)', t)]
i = ms[0]
seg = t[i:i+40000]
flat = re.sub(r'\s*\|\s*', ' ', seg)
flat = re.sub(r'\(\s*([\d,]+)\s*\)', r'-\1', flat)
flat = re.sub(r'\$', '', flat)
flat = re.sub(r'\s+', ' ', flat)
for L in labels:
    j = flat.find(L)
    print(L, '=>', flat[j+len(L):j+len(L)+45] if j>=0 else 'NOT FOUND')
