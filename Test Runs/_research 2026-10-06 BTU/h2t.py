import sys, re, html
def h2t(s):
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?is)<ix:header>.*?</ix:header>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>', '\n', s)
    s = re.sub(r'(?i)</td>|</th>', ' | ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).replace('\xa0', ' ')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s
if __name__ == "__main__":
    for p in sys.argv[1:]:
        t = h2t(open(p, encoding='utf-8', errors='replace').read())
        open(p + '.txt', 'w', encoding='utf-8').write(t)
        print(p, len(t))
