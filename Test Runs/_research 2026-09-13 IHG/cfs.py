import re, sys
fn = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 3800
t = re.sub(r'\s+', ' ', open(fn, encoding='utf-8', errors='replace').read())
hits = [m.start() for m in re.finditer(r'Group statement of cash flows', t)]
for h in hits:
    seg = t[h:h+n]
    if 'Profit for the year' in seg[:400] or 'Cash flow from operations' in seg[:900]:
        print(seg); print('=====')
        break
for m in re.finditer(r'Reconciliation of profit for the year to cash flow from operations', t):
    print(t[m.start():m.start()+4200]); print('#####'); break
