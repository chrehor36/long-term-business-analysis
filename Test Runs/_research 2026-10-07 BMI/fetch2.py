"""Fetch an EDGAR document; tables rendered one row per line. Usage: python fetch2.py CIK ACCESSION DOC OUTNAME"""
import sys, re, html, urllib.request, time
cik, acc, doc, out = sys.argv[1:5]
url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"
req = urllib.request.Request(url, headers={"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "identity"})
raw = urllib.request.urlopen(req, timeout=180).read().decode("utf-8", "replace")
raw = re.sub(r"(?is)<(script|style|ix:header).*?</\1>", " ", raw)
def clean(s):
    s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s).replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()
def table(m):
    rows = []
    for tr in re.findall(r"(?is)<tr.*?</tr>", m.group(0)):
        cells = [clean(c) for c in re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", tr)]
        cells = [c for c in cells if c not in ("", "$", ")", "%")]
        if cells: rows.append(" | ".join(cells))
    return "\n<<TABLE>>\n" + "\n".join(rows) + "\n<</TABLE>>\n"
raw = re.sub(r"(?is)<table.*?</table>", table, raw)
t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h\d>", "\n", raw)
t = re.sub(r"<[^>]+>", " ", t); t = html.unescape(t).replace("\xa0", " ")
t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
open(out, "w", encoding="utf-8").write(f"SOURCE {url}\nACCESSION {acc}\n\n" + t)
print(out, len(t)); time.sleep(0.3)
