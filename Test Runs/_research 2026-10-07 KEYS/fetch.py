import sys, os, time, urllib.request, gzip, re, html, json
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
def get(url, out=None):
    if out and os.path.exists(out):
        return open(out, 'rb').read()
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=60); data = r.read()
            if r.headers.get('Content-Encoding') == 'gzip': data = gzip.decompress(data)
            break
        except Exception as e:
            print('retry', e, file=sys.stderr); time.sleep(2)
    else: raise SystemExit('fail '+url)
    time.sleep(0.15)
    if out:
        os.makedirs(os.path.dirname(out) or '.', exist_ok=True); open(out, 'wb').write(data)
    return data
def strip(htmlb):
    t = htmlb.decode('utf-8', 'ignore')
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', t)
    t = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', t)
    t = re.sub(r'(?i)</t[dh]>', ' | ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return t
if __name__ == '__main__':
    url, out = sys.argv[1], sys.argv[2]
    d = get(url, out)
    if len(sys.argv) > 3:
        open(sys.argv[3], 'w', encoding='utf-8').write(strip(d))
