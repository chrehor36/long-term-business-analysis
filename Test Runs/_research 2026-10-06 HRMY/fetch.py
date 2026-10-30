import json, sys, urllib.request, gzip, re, os, html
UA = {'User-Agent': 'Chris Hrehor chrehor36@gmail.com', 'Accept-Encoding': 'gzip, deflate'}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            data = gzip.decompress(data)
    return data
def text_of(htmlbytes):
    s = htmlbytes.decode('utf-8', errors='replace')
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', s)
    s = re.sub(r'(?i)</td>', ' | ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t\xa0]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'sub':
        cik = sys.argv[2].zfill(10); out = sys.argv[3]
        d = get(f'https://data.sec.gov/submissions/CIK{cik}.json')
        open(out,'wb').write(d)
    elif cmd == 'doc':
        url = sys.argv[2]; out = sys.argv[3]
        d = get(url)
        open(out,'w',encoding='utf-8').write(text_of(d))
        print(out, len(d))
    elif cmd == 'raw':
        url = sys.argv[2]; out = sys.argv[3]
        open(out,'wb').write(get(url))
