"""Strip an EDGAR HTML filing in cache/ to plain text in cache/ (gitignored). Usage: python totext.py IN.htm OUT.txt"""
import sys, os, re, html
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
src = open(os.path.join(CACHE, sys.argv[1]), encoding="utf-8", errors="replace").read()
src = re.sub(r"(?is)<(script|style).*?</\1>", " ", src)
src = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", src)
src = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", src)
src = re.sub(r"(?i)</td>|</th>", " | ", src)
src = re.sub(r"<[^>]+>", " ", src)
src = html.unescape(src).replace("\xa0", " ")
lines = [re.sub(r"[ \t]+", " ", l).strip() for l in src.split("\n")]
out = "\n".join(l for l in lines if l and l != "|")
open(os.path.join(CACHE, sys.argv[2]), "w", encoding="utf-8").write(out)
print(sys.argv[2], len(out))
