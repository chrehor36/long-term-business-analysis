import urllib.request, re, sys
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept":"text/html,*/*"}
pat=re.compile(r"https?://[A-Za-z0-9._~:/?#@!$&()*+,;=%-]+?\.pdf")
for url in sys.argv[1:]:
    try:
        r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60)
        h=r.read().decode("utf-8","replace")
        open("probe_"+re.sub(r"\W+","_",url)[-60:]+".html","w",encoding="utf-8").write(h)
        print("OK",url,r.status,len(h))
        for l in sorted(set(pat.findall(h))): print("  ",l)
        for l in sorted(set(re.findall(r'href="(/[^"]+)"',h)))[:80]: print("  href",l)
    except Exception as e:
        print("FAIL",url,repr(e))
