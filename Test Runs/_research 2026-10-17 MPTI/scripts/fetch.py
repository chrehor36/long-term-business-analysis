# Fetch an EDGAR primary document and strip it to text, into the given dir (gitignored cache/).
# Each table row is kept on one line.
import sys, re, html, time, urllib.request, os
UA = "Chris Hrehor chrehor36@gmail.com"
CIK = "1902314"
def strip(raw):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    def row(m):
        cells = re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", m.group(0))
        cells = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c)).replace("\xa0"," ")).strip() for c in cells]
        cells = [c for c in cells if c and c not in ("$", "%", ")")]
        return "\n" + " | ".join(cells) + "\n"
    t = re.sub(r"(?is)<tr[^>]*>.*?</tr>", row, t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</h\d>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
if __name__ == "__main__":
    out_dir = sys.argv[1]
    for spec in sys.argv[2:]:
        parts = spec.split("|")
        acc, doc, name = parts[:3]
        cik = parts[3] if len(parts) > 3 else CIK
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
        rawp = os.path.join(out_dir, name + ".htm")
        if not os.path.exists(rawp):
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            open(rawp, "wb").write(urllib.request.urlopen(req).read())
            time.sleep(0.3)
        raw = open(rawp, "rb").read().decode("utf-8", "replace")
        t = strip(raw)
        open(os.path.join(out_dir, name + ".txt"), "w", encoding="utf-8").write(t)
        print("got", name, len(t))
