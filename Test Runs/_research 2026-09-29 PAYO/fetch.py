import sys, os, re, html
sys.path.insert(0, 'tools')
import sources as s
R = 'Test Runs/_research 2026-09-29 PAYO'
CIK = '1845815'
def totext(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    h = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>', '\n', h)
    h = re.sub(r'(?i)</td>|</th>', ' | ', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = html.unescape(h).replace('\xa0', ' ')
    h = re.sub(r'[ \t]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    return h
def get(acc, doc, name):
    out = os.path.join(R, name)
    if os.path.exists(out):
        return open(out, encoding='utf-8').read()
    url = f'https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace("-","")}/{doc}'
    t = totext(s._get(url, s.SEC_UA, None))
    open(out, 'w', encoding='utf-8').write(t)
    return t
if __name__ == '__main__':
    acc, doc, name = sys.argv[1:4]
    t = get(acc, doc, name)
    print(len(t))
