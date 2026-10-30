import sys, io, urllib.request, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) BRK research chrehor36@gmail.com'}
for u in ['https://www.deezer-investors.com/fin/', 'https://www.deezer-investors.com/', 'https://newsroom-deezer.com/2026/04/deezer-2025-universal-registration-document/']:
    try:
        h = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60).read().decode('utf-8','replace')
        pdfs = sorted(set(re.findall(r'https?://[^"\'\s>]+\.pdf', h)))
        print(u, len(h)); [print('  ', p) for p in pdfs if re.search(r'URD|urd|niversal|enregistrement|2025|2026', p)]
    except Exception as e:
        print(u, 'ERR', e)
