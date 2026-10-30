import sys; sys.path.insert(0,'../../tools')
import sources as S, urllib.request
url = S.USD_TREASURY.format(yr=2026)
print(url)
txt = urllib.request.urlopen(urllib.request.Request(url, headers=S.WEB_UA), timeout=45).read().decode()
rows=[r for r in txt.strip().split('\n') if r.strip()]
hdr=rows[0].split(','); i=[j for j,h in enumerate(hdr) if '30 Yr' in h][0]
for r in rows[1:6]: c=r.split(','); print(c[0], c[i])
