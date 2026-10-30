import sys, re, html
for p in sys.argv[1:]:
    t = open(p, encoding='utf-8', errors='replace').read()
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t)
    t = re.sub(r'(?i)<ix:header>.*?</ix:header>', ' ', t, flags=re.S)
    t = re.sub(r'(?i)</(p|div|tr|br|li|h\d)>', '\n', t)
    t = re.sub(r'(?i)<br\s*/?>', '\n', t)
    t = re.sub(r'(?i)</t[dh]>', ' | ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    open(p.replace('.htm', '.txt'), 'w', encoding='utf-8').write(t)
    print(p, len(t))
