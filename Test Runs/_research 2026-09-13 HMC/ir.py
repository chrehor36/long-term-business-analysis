import urllib.request, re, sys, gzip
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36', 'Accept-Encoding': 'gzip'}
def get(url):
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
    d = r.read()
    if r.headers.get('Content-Encoding') == 'gzip': d = gzip.decompress(d)
    return d
if __name__ == '__main__':
    url = sys.argv[1]
    d = get(url)
    if len(sys.argv) > 2:
        open(sys.argv[2], 'wb').write(d); print('saved', len(d))
    else:
        t = d.decode('utf-8', 'replace')
        for m in sorted(set(re.findall(r'href="([^"]+)"', t))):
            print(m)
