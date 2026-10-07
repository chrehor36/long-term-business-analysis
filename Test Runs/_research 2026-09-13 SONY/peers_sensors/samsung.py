import urllib.request, re, html, sys, os
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
urls = sys.argv[1:]
def totext(h):
    h = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", h)
    h = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h).replace("\xa0", " ")
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in h.split("\n")]
    return "\n".join(l for l in lines if l and l.strip("| "))
for u in urls:
    name = "SSNG_" + u.rstrip("/").split("/")[-1][:70] + ".txt"
    try:
        raw = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read().decode("utf-8","replace")
    except Exception as e:
        print("FAIL", u, e); continue
    open(name, "w", encoding="utf-8").write("SOURCE: " + u + "\nFETCHED: 2026-09-13\n" + totext(raw))
    print("OK", name, len(raw))
