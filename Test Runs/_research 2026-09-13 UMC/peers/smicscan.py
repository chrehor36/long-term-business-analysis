import urllib.request, re, time, sys
H={"User-Agent":"Mozilla/5.0"}
lo, hi, step = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
for nid in range(lo, hi, step):
    try:
        b=urllib.request.urlopen(urllib.request.Request(f"https://www.smics.com/en/site/news_read/{nid}",headers=H),timeout=30).read().decode("utf-8","replace")
        m=re.search(r"<title>([^<]*)</title>", b)
        ti = m.group(1) if m else ""
        if "QUARTER RESULTS" in ti.upper() or step > 1:
            print(nid, ti.encode("ascii","replace").decode())
    except Exception as e:
        print(nid, "ERR", str(e)[:60])
    time.sleep(0.2)
