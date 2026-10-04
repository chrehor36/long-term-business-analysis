import json, urllib.request, time, os, re
import xml.etree.ElementTree as ET
from parse_13f_text import parse_13f_text

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache", "13f")
UA = "BRK-Framework research chrehor36@gmail.com"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def parse_xml_info_table(xml_bytes):
    text = xml_bytes.decode("utf-8", errors="ignore")
    text = re.sub(r'xmlns(:\w+)?="[^"]*"', '', text)
    text = re.sub(r'\b\w+:', '', text)  # strip namespace prefixes like ns1:
    root = ET.fromstring(text)
    holdings = []
    for info in root.iter("infoTable"):
        def gt(tag):
            e = info.find(tag)
            return e.text.strip() if e is not None and e.text else None
        issuer = gt("nameOfIssuer")
        cusip = gt("cusip")
        value = gt("value")
        shrs_el = info.find("shrsOrPrnAmt")
        shares = None
        if shrs_el is not None:
            sa = shrs_el.find("sshPrnamt")
            shares = sa.text.strip() if sa is not None and sa.text else None
        if issuer and value:
            holdings.append({"issuer": issuer, "cusip": cusip, "value": int(value), "shares": int(shares) if shares else 0})
    # merge duplicate issuer/cusip (multi-manager rows)
    merged = {}
    order = []
    for h in holdings:
        key = h["cusip"] or h["issuer"]
        if key not in merged:
            merged[key] = dict(h)
            order.append(key)
        else:
            merged[key]["value"] += h["value"]
            merged[key]["shares"] += h["shares"]
    return [merged[k] for k in order]

q4 = json.load(open(os.path.join(SCRATCH, "brk_13f_q4_list.json")))

all_years = {}
for r in q4:
    acc_nodash = r["accession"].replace("-", "")
    year = r["reportDate"][:4]
    idx_html = open(os.path.join(CACHE, f"idx_{year}.html"), encoding="utf-8", errors="ignore").read()
    hrefs = re.findall(r'href="(/Archives/edgar/data/1067983/' + acc_nodash + r'/[^"]+)"', idx_html)
    hrefs = [h for h in hrefs if not h.endswith("-index.html") and not h.endswith("-index-headers.html")]

    xml_docs = [h for h in hrefs if h.endswith(".xml") and "primary_doc" not in h]
    # the full-submission .txt always matches the accession number itself; the OTHER .txt is the info table
    other_txt = [h for h in hrefs if h.endswith(".txt") and r["accession"] not in h]
    if not xml_docs and not other_txt:
        # oldest filings (1998-99): only the full-submission .txt exists, and
        # it IS the info table (no separate secondary document was filed)
        other_txt = [h for h in hrefs if h.endswith(".txt")]

    holdings = None
    mode = None
    if xml_docs:
        fn = os.path.join(CACHE, f"raw_{year}.xml")
        if not os.path.exists(fn):
            data = fetch("https://www.sec.gov" + xml_docs[0])
            open(fn, "wb").write(data)
            time.sleep(0.2)
        holdings = parse_xml_info_table(open(fn, "rb").read())
        mode = "xml"
    elif other_txt:
        fn = os.path.join(CACHE, f"raw_{year}.txt")
        if not os.path.exists(fn):
            data = fetch("https://www.sec.gov" + other_txt[0])
            open(fn, "wb").write(data)
            time.sleep(0.2)
        text = open(fn, encoding="utf-8", errors="ignore").read()
        holdings, stated_total = parse_13f_text(text)
        parsed_total = sum(h["value"] for h in holdings)
        match = (stated_total == parsed_total) if stated_total else None
        mode = f"text (stated={stated_total}, parsed={parsed_total}, match={match})"
    else:
        print(year, "NO DOC FOUND", hrefs)
        continue

    total_val = sum(h["value"] for h in holdings)
    print(f"{year}: {mode} -- {len(holdings)} holdings, total ${total_val:,}K")
    all_years[year] = {"total_value_thousands": total_val, "holdings": sorted(holdings, key=lambda h: -h["value"])}

json.dump(all_years, open(os.path.join(SCRATCH, "brk_13f_all_years.json"), "w"), indent=1)
print("\nSaved", len(all_years), "years")
