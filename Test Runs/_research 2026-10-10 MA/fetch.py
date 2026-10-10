import sys, os, json, time, urllib.request, gzip, re, html
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")
os.makedirs(C, exist_ok=True)
def get(url, name=None):
    name = name or re.sub(r'[^A-Za-z0-9._-]', '_', url.split('/')[-1])
    p = os.path.join(C, name)
    if os.path.exists(p): return open(p, 'rb').read()
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=60); d = r.read()
            if r.headers.get('Content-Encoding') == 'gzip': d = gzip.decompress(d)
            open(p, 'wb').write(d); time.sleep(0.2); return d
        except Exception as e:
            print('retry', url, e, file=sys.stderr); time.sleep(2)
    raise SystemExit('fail ' + url)
def text(d):
    s = d.decode('utf-8', 'ignore')
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>', '\n', s)
    s = re.sub(r'(?i)</td>', ' | ', s)
    s = re.sub(r'<[^>]+>', ' ', s); s = html.unescape(s)
    s = re.sub(r'[ \t\xa0]+', ' ', s); s = re.sub(r'\n\s*\n+', '\n', s)
    return s
if __name__ == '__main__':
    url, name = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else None)
    d = get(url, name)
    if name and name.endswith('.txt') and not url.endswith('.txt'):
        pass
    print(len(d))
