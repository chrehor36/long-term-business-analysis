"""Strip EDGAR .htm files to text (table cells tab-separated). Usage: python -I htm2txt.py in.htm [in2.htm ...]
Writes in.txt beside each input."""
import sys, re
from html.parser import HTMLParser


class P(HTMLParser):
    def __init__(s):
        super().__init__()
        s.out = []
        s.skip = False

    def handle_starttag(s, t, a):
        if t in ('script', 'style'):
            s.skip = True
        if t in ('p', 'div', 'br', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'table'):
            s.out.append('\n')
        if t in ('td', 'th'):
            s.out.append('\t')

    def handle_endtag(s, t):
        if t in ('script', 'style'):
            s.skip = False

    def handle_data(s, d):
        if not s.skip:
            s.out.append(d)


for f in sys.argv[1:]:
    p = P()
    p.feed(open(f, encoding='utf-8', errors='replace').read())
    t = ''.join(p.out).replace('\xa0', ' ')
    t = re.sub(r'[ \t]*\t[ \t]*', '\t', t)
    t = re.sub(r'\t+', '\t', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    open(re.sub(r'\.htm$', '.txt', f), 'w', encoding='utf-8').write(t)
