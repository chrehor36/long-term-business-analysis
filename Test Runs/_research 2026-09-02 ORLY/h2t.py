#!/usr/bin/env python3
"""HTML -> text, preserving table row structure. Fetch/convert only."""
import re, sys, os, html

def conv(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        s = f.read()
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?is)<br[^>]*>", "\n", s)
    s = re.sub(r"(?is)</t[dh]>", " | ", s)
    s = re.sub(r"(?is)</tr>", "\n", s)
    s = re.sub(r"(?is)</(p|div|h[1-6]|table|li)>", "\n", s)
    s = re.sub(r"(?is)<[^>]+>", "", s)
    s = html.unescape(s)
    s = s.replace(" ", " ").replace("’", "'").replace("—", "-")
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'")
    s = s.replace("–", "-")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\|\s*(?=\n)", "\n", s)
    s = re.sub(r"(\|\s*)+\|", "| ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    lines = [l.rstrip() for l in s.split("\n")]
    out = []
    for l in lines:
        t = l.strip().strip("|").strip()
        if t:
            out.append(l.strip())
    return "\n".join(out)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        t = conv(p)
        o = os.path.splitext(p)[0] + ".txt"
        with open(o, "w", encoding="utf-8") as f:
            f.write(t)
        print(o, len(t))
