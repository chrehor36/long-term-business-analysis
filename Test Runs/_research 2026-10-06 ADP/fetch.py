"""Fetch an EDGAR document with a descriptive User-Agent, pause between calls, back off on 429,
and save the raw HTML plus a plain-text rendering under cache/ (gitignored).
Usage: python fetch.py URL NAME"""
import sys, time, re, html, urllib.request, urllib.error, pathlib

UA = "Long-Term Business Analysis research chrehor36@gmail.com"
url, name = sys.argv[1], sys.argv[2]
out = pathlib.Path(__file__).parent / "cache"
out.mkdir(exist_ok=True)
for attempt in range(8):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
        raw = urllib.request.urlopen(req, timeout=60).read()
        break
    except urllib.error.HTTPError as e:
        if e.code in (429, 503):
            wait = 15 * (attempt + 1)
            print(f"HTTP {e.code}, waiting {wait}s", file=sys.stderr)
            time.sleep(wait)
            continue
        raise
else:
    sys.exit("gave up")
(out / f"{name}.htm").write_bytes(raw)
t = raw.decode("utf-8", "replace")
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
t = re.sub(r"(?i)</td>|</th>", " | ", t)
t = re.sub(r"<[^>]+>", "", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
(out / f"{name}.txt").write_text(t)
print(name, len(raw), "bytes,", len(t.splitlines()), "lines")
time.sleep(1.5)
