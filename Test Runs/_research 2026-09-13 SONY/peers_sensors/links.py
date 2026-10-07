import urllib.request, re, sys
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
for u in sys.argv[1:]:
    try:
        raw = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read().decode("utf-8","replace")
    except Exception as e:
        print("FAIL", u, e); continue
    print("OK", u, len(raw))
    for m in sorted(set(re.findall(r'(?:href|data-[a-z-]+)="([^"]+\.(?:pdf|PDF)[^"]*)"', raw))):
        print("  ", m)
