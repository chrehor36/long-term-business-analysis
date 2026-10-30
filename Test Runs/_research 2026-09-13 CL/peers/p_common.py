"""Shared fetch helpers for the CL peer row. Fetch and strip only; no conclusions."""
import os, re, html, json, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}


def get(url, binary=False):
    last = None
    for k in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            data = urllib.request.urlopen(req, timeout=180).read()
            time.sleep(0.3)
            return data if binary else data.decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(2 + 3 * k)
    raise last


def strip(raw):
    t = re.sub(r"(?is)<(script|style|ix:header).*?</\1>", " ", raw)
    t = re.sub(r"(?i)</(td|th)>", " | ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t ​]+", " ", t)
    t = re.sub(r"( \| )+( ?\| ?)*", " | ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t


def jload(name):
    return json.load(open(os.path.join(HERE, name), encoding="utf-8"))


def jsave(obj, name):
    json.dump(obj, open(os.path.join(HERE, name), "w", encoding="utf-8"), indent=1)
