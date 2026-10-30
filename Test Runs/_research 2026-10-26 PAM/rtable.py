"""Print an XBRL-viewer R page (R*.htm) as one row per line. Usage: python -I rtable.py path [path...]"""
import sys, re, html

for p in sys.argv[1:]:
    s = open(p, "rb").read().decode("utf-8", "ignore")
    print("=====", p)
    for tr in re.findall(r"(?is)<tr.*?</tr>", s):
        cells = re.findall(r"(?is)<t[hd][^>]*>(.*?)</t[hd]>", tr)
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip() for c in cells]
        cells = cells if any(cells) else []
        if cells and cells[0] == "X":
            break
        if cells:
            print(" | ".join(cells))
