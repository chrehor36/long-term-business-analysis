"""Fetch an EDGAR document and save raw + stripped text under cache/. Usage: fetch.py URL name"""
import sys, re, html, urllib.request, os, time
UA = "Chris Hrehor chrehor36@gmail.com"
url, name = sys.argv[1], sys.argv[2]
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cache")
req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
data = urllib.request.urlopen(req, timeout=120).read()
open(os.path.join(out, name + ".raw"), "wb").write(data)
t = data.decode("utf-8", "replace")
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
t = re.sub(r"(?i)</td>|</th>", " | ", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
open(os.path.join(out, name + ".txt"), "w", encoding="utf-8").write(t)
print(name, len(data), "bytes;", len(t), "chars")
time.sleep(0.3)
