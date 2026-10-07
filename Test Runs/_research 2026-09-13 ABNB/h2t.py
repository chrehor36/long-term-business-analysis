import sys, re, html
def h2t(s):
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>', '\n', s)
    s = re.sub(r'(?i)</td>|</th>', ' | ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = s.replace('\xa0', ' ').replace(chr(0x200b), '')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s
for src, dst in zip(sys.argv[1::2], sys.argv[2::2]):
    t = h2t(open(src, encoding='utf-8', errors='replace').read())
    open(dst, 'w', encoding='utf-8').write(t)
    print(dst, len(t))
