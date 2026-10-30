"""Fetch an EDGAR URL with the required User-Agent, cache raw under cache/, write a plain-text version beside it.
usage: python -I fetch.py URL NAME   -> prints path of text file"""
import sys, os, re, time, urllib.request, html
UA = "Chris Hrehor chrehor36@gmail.com"
here = os.path.dirname(os.path.abspath(__file__))
cache = os.path.join(here, "cache"); os.makedirs(cache, exist_ok=True)
url, name = sys.argv[1], sys.argv[2]
raw = os.path.join(cache, name + ".raw")
if not os.path.exists(raw):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    open(raw, "wb").write(data); time.sleep(0.2)
data = open(raw, "rb").read().decode("utf-8", "replace")
if name.endswith("json"):
    print(raw); sys.exit()
t = re.sub(r"(?is)<(script|style).*?</\1>", " ", data)
t = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", t)
t = re.sub(r"(?i)</t[dh]>", " | ", t)
t = re.sub(r"<[^>]+>", " ", t)
t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t)
t = re.sub(r"\n\s*\n+", "\n", t)
out = os.path.join(cache, name + ".txt")
open(out, "w", encoding="utf-8").write(t)
print(out, len(t))
