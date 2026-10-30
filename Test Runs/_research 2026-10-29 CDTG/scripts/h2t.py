import sys, re, html, glob, os
d = sys.argv[1]
for f in glob.glob(os.path.join(d, '*.htm')):
    s = open(f, encoding='utf-8', errors='replace').read()
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?i)</(p|div|tr|br|h\d|li|table)>|<br\s*/?>', '\n', s)
    s = re.sub(r'(?i)</t[dh]>', ' | ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s).replace('\xa0', ' ')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    open(f[:-4] + '.txt', 'w', encoding='utf-8').write(s)
    print(f, len(s))
