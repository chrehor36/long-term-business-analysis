import sys, os, re, time, urllib.request, html
UA = {'User-Agent': 'Chris Hrehor chrehor36@gmail.com'}


def get(url, out):
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=60).read()
    open(out, 'wb').write(data)
    time.sleep(0.3)


def totext(src, dst):
    s = open(src, 'rb').read().decode('utf-8', 'ignore')
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?is)<ix:header>.*?</ix:header>', ' ', s)
    s = re.sub(r'[\r\n]+', ' ', s)
    # inside a cell, block breaks become spaces
    s = re.sub(r'(?is)<td[^>]*>.*?</td>',
               lambda m: re.sub(r'(?i)<br\s*/?>|</p>|</div>', ' ', m.group(0)), s)
    s = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', s)
    s = re.sub(r'(?i)</td>|</th>', '\t', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'[ \xa0]+', ' ', s)
    s = re.sub(r'(\s*\t\s*)+', ' | ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    open(dst, 'w', encoding='utf-8').write(s)


if __name__ == '__main__':
    cik, acc, doc, name = sys.argv[1:5]
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}"
    out = os.path.join(sys.argv[5] if len(sys.argv) > 5 else 'cache', name)
    get(url, out + '.htm')
    totext(out + '.htm', out + '.txt')
    print(out + '.txt', os.path.getsize(out + '.txt'))
