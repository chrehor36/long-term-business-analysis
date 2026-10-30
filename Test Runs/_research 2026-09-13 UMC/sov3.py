import urllib.request, os, zipfile, io, re
H = {"User-Agent": "Mozilla/5.0"}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sov")
u = "https://www.tpex.org.tw/www/en-us/api/convertToOds?f=bond_zone/tradeinfo/govbond/2026/202609/Curve.20260911-E.xls"
b = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60).read()
open(os.path.join(out, "Curve.20260911-E.ods"), "wb").write(b)
z = zipfile.ZipFile(io.BytesIO(b))
x = z.read("content.xml").decode("utf-8")
for tab in re.findall(r"<table:table [^>]*table:name=\"([^\"]+)\"(.*?)</table:table>", x, flags=re.S):
    print("== sheet", tab[0])
    for row in re.findall(r"<table:table-row[^>]*>(.*?)</table:table-row>", tab[1], flags=re.S):
        cells = []
        for m in re.finditer(r"<table:table-cell([^>]*)/>|<table:table-cell([^>]*)>(.*?)</table:table-cell>", row, flags=re.S):
            attrs = m.group(1) or m.group(2) or ""
            rep = re.search(r'number-columns-repeated="(\d+)"', attrs)
            txt = re.sub(r"<[^>]+>", "", m.group(3) or "").strip()
            n = int(rep.group(1)) if rep else 1
            cells.extend([txt] * min(n, 3))
        if any(cells):
            print(" | ".join(cells))
