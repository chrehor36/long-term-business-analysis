import urllib.request, re, html, os, sys
H = {"User-Agent": "Mozilla/5.0"}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "peers")
for nid in sys.argv[1:]:
    u = f"https://www.smics.com/en/site/news_read/{nid}"
    try:
        b = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60).read().decode("utf-8", "replace")
    except Exception as e:
        print(nid, "ERR", e); continue
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", b, flags=re.S)
    t = re.sub(r"</(p|tr|div|li|h\d)>", "\n", t); t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t); t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    open(os.path.join(out, f"SMIC_news_{nid}.txt"), "w", encoding="utf-8").write(t)
    i = t.find("SMIC REPORTS")
    print(nid, len(t), t[i:i+120].replace("\n", " "))
