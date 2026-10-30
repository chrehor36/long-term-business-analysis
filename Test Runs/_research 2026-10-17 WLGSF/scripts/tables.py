"""Print filed HTML tables whose text matches a pattern, as compact rows. Usage: tables.py FILE.htm PATTERN [maxtables]"""
import sys, re, html
f, pat = sys.argv[1], sys.argv[2]; mx = int(sys.argv[3]) if len(sys.argv) > 3 else 5
s = open(f, encoding='utf-8', errors='replace').read()
n = 0
for t in re.finditer(r'(?is)<table.*?</table>', s):
    tb = t.group(0)
    txt = re.sub(r'<[^>]+>', ' ', tb); txt = html.unescape(txt)
    if not re.search(pat, txt, re.I): continue
    n += 1
    print('=' * 20, 'table', n)
    for r in re.finditer(r'(?is)<tr.*?</tr>', tb):
        cells = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', c))).strip() for c in re.findall(r'(?is)<t[dh].*?</t[dh]>', r.group(0))]
        cells = [c for c in cells if c not in ('', '$', 'US$', ')', '%')]
        if cells: print(' | '.join(cells))
    if n >= mx: break
