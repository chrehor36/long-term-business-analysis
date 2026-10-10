import sys, os, json, time, re, urllib.request, gzip
UA = {'User-Agent': 'Chris Hrehor chrehor36@gmail.com', 'Accept-Encoding': 'gzip'}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                d = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    d = gzip.decompress(d)
                return d
        except Exception as e:
            print('retry', e, file=sys.stderr); time.sleep(2)
    raise SystemExit('fail ' + url)
def text(html):
    html = re.sub(r'(?is)<(script|style).*?</\1>', ' ', html)
    html = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>', '\n', html)
    html = re.sub(r'(?i)</td>', ' | ', html)
    t = re.sub(r'<[^>]+>', ' ', html)
    import html as h
    t = h.unescape(t)
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t
if __name__ == '__main__':
    url, out = sys.argv[1], sys.argv[2]
    d = get(url)
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    if out.endswith('.txt'):
        open(out, 'w', encoding='utf-8').write(text(d.decode('utf-8', 'replace')))
    else:
        open(out, 'wb').write(d)
    print(out, len(d))
