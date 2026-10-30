"""Strip an EDGAR HTML filing to plain text. Usage: python html2text.py IN.htm OUT.txt"""
import sys, re, html

raw = open(sys.argv[1], "rb").read().decode("utf-8", "replace")
raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", raw)
raw = re.sub(r"(?i)</td>", " | ", raw)
txt = re.sub(r"<[^>]+>", " ", raw)
txt = html.unescape(txt).replace("\xa0", " ")
txt = re.sub(r"[ \t]+", " ", txt)
txt = re.sub(r"\n\s*\n+", "\n", txt)
open(sys.argv[2], "w").write(txt)
print(len(txt))
