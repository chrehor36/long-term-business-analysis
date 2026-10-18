import sys, re, html
def conv(src, dst):
    t = open(src, encoding='utf-8', errors='replace').read()
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t)
    t = re.sub(r'(?is)<ix:header>.*?</ix:header>', ' ', t)
    t = re.sub(r'(?i)<br\s*/?>', '\n', t)
    t = re.sub(r'(?i)</(p|div|tr|li|h\d|table)>', '\n', t)
    t = re.sub(r'(?i)</t[dh]>', ' | ', t)
    t = re.sub(r'(?s)<[^>]+>', '', t)
    t = html.unescape(t).replace('\xa0', ' ')
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    open(dst, 'w', encoding='utf-8').write(t)
for i in range(1, len(sys.argv), 2): conv(sys.argv[i], sys.argv[i+1]); print(sys.argv[i+1])
