"""Dump every HTML table of a filing whose text matches all given keywords, as clean rows.
usage: python tables.py <file.htm> <outfile> kw1 [kw2 ...]
Transcription only: prints cell text, no computation."""
import sys, re, html as H
from lxml import etree, html

src, out, kws = sys.argv[1], sys.argv[2], sys.argv[3:]
doc = html.fromstring(open(src, "rb").read())
res = []
for ti, t in enumerate(doc.iter("table")):
    rows = []
    for tr in t.iter("tr"):
        cells = []
        for td in tr:
            if td.tag not in ("td", "th"):
                continue
            s = " ".join(td.itertext())
            s = H.unescape(s).replace("\xa0", " ")
            s = re.sub(r"\s+", " ", s).strip()
            if s:
                cells.append(s)
        if cells:
            # glue "(" "1,234" ")" fragments
            j = " | ".join(cells)
            j = re.sub(r"\( \| ", "(", j)
            j = re.sub(r" \| \)", ")", j)
            j = re.sub(r"\(\s+", "(", j)
            j = re.sub(r"\s+\)", ")", j)
            rows.append(j)
    txt = "\n".join(rows)
    if all(k.lower() in txt.lower() for k in kws):
        res.append(f"### TABLE {ti}\n" + txt)
open(out, "w", encoding="utf-8").write("\n\n".join(res))
print(len(res), "tables ->", out)
