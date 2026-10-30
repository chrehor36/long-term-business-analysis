"""Strip HTML filings to text (cache/ in, cache/ out). usage: python -I strip.py NAME [NAME ...]  (NAME without .htm)"""
import sys, re, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
for name in sys.argv[1:]:
    s = open(os.path.join(HERE, 'cache', name + '.htm'), encoding='utf-8', errors='replace').read()
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?is)<ix:header>.*?</ix:header>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', s)
    s = re.sub(r'(?i)</td>|</th>', ' | ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).replace('\xa0', ' ')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    open(os.path.join(HERE, 'cache', name + '.txt'), 'w', encoding='utf-8').write(s)
    print(name, len(s))
