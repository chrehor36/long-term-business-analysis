import sys, urllib.request, re, html, os
url = sys.argv[1]; out = sys.argv[2]
r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read().decode('utf8', 'ignore')
links = sorted(set(m for m in re.findall(r'href="([^"]+)"', r) if any(k in m.lower() for k in ('.pdf', 'mb.cision', 'storage.mfn', 'attachment'))))
body = re.sub(r'(?is)<(script|style).*?</\1>', '', r)
body = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</li>|</h\d>', '\n', body)
body = re.sub(r'<[^>]+>', ' ', body)
body = html.unescape(body)
body = re.sub(r'[ \t]+', ' ', body); body = re.sub(r'\n\s*\n+', '\n', body)
open(out, 'w', encoding='utf8').write(url + '\n' + '\n'.join(links) + '\n\n' + body)
print(len(body)); print('\n'.join(links))
