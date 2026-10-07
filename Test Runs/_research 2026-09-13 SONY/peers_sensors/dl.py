import urllib.request, sys, os
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
for u in sys.argv[1:]:
    n = u.split("/")[-1]
    if os.path.exists(n): print("have", n); continue
    try:
        d = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        open(n,"wb").write(d); print("OK", n, len(d))
    except Exception as e: print("FAIL", u, e)
