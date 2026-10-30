import re

def parse_13f_text(text):
    """Best-effort parser for pre-2013 fixed-width 13F text tables.
    Returns list of {issuer, cusip, value_thousands, shares}, summed across
    sub-rows (multiple managers) for the same issuer/cusip.
    """
    # stated total: take the FIRST (largest-context) match; some filings repeat
    # a spurious "$0" total later in an amendment/confidential-treatment section
    totals = [int(x.replace(",", "")) for x in re.findall(r"Value Total:\s*\$?\s*([\d,]+)", text)]
    stated_total = totals[0] if totals else None

    lines = text.split("\n")
    # find start of data: anchor on the header row containing "CUSIP" (robust
    # across the several header-wording variants used across 1998-2012),
    # then skip forward past whatever separator/tag/units-note line follows —
    # the per-line skip rules below handle those regardless of exact form.
    start = None
    for i, l in enumerate(lines):
        if re.search(r"CUSIP", l, re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return [], stated_total

    cusip_re = re.compile(r"([0-9A-Z]{6}\s?[0-9A-Z]{2}\s?[0-9A-Z])\s+([\d,]+)\s+([\d,]+)")
    data_only_re = re.compile(r"^\s*([\d,]+)\s+([\d,]+)\s+[A-Z]")

    holdings = {}
    order = []
    pending_name = []
    current_key = None

    signatures = ["</SEC-DOCUMENT>", "SIGNATURE", "This report"]
    for l in lines[start:]:
        stripped_check = l.strip()
        if any(sig in l for sig in signatures):
            break  # true end of the filing body
        if not stripped_check or stripped_check.startswith("<") or stripped_check.startswith("-"):
            continue  # blank line, any tag (<TABLE>,</TABLE>,<PAGE>,<S>,<C>,<CAPTION>), or dash separator/subtotal rule
        if re.fullmatch(r"[\d,]+", stripped_check):
            continue  # a lone page-subtotal number
        if (re.search(r"name of issuer|form 13f information table|berkshire hathaway|title of|principal\s+amount|shares?\s+or|voting authority|investment\s*$|discretion|other\s+managers|\(in thousands\)|\(x\$1000\)|sole\s+shared|entry total", l, re.IGNORECASE)
                or re.match(r"^\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d+,\s+\d{4}\s*$", l)
                or "Column" in l):
            continue  # repeated header/caption/units-note block (many wording variants across 1998-2012 filing agents)
        m = cusip_re.search(l)
        if m:
            cusip = m.group(1)
            value = int(m.group(2).replace(",", ""))
            shares = int(m.group(3).replace(",", ""))
            name_part = l[:m.start()].strip()
            pending_name.append(name_part)
            issuer = " ".join(pending_name).strip()
            issuer = re.sub(r"\s+", " ", issuer)
            key = cusip.replace(" ", "")
            if key not in holdings:
                holdings[key] = {"issuer": issuer, "cusip": key, "value": 0, "shares": 0}
                order.append(key)
            holdings[key]["value"] += value
            holdings[key]["shares"] += shares
            current_key = key
            pending_name = []
            continue
        m2 = data_only_re.match(l)
        if m2 and current_key:
            value = int(m2.group(1).replace(",", ""))
            shares = int(m2.group(2).replace(",", ""))
            holdings[current_key]["value"] += value
            holdings[current_key]["shares"] += shares
            continue
        # otherwise: likely a continuation of an issuer name (no numbers yet)
        stripped = l.strip()
        if stripped and not re.match(r"^[\d,\.\s]+$", stripped):
            pending_name.append(stripped)

    result = [holdings[k] for k in order]
    return result, stated_total

if __name__ == "__main__":
    text = open(r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad\sample_2010_13f.txt", encoding="utf-8", errors="ignore").read()
    holdings, stated_total = parse_13f_text(text)
    total = sum(h["value"] for h in holdings)
    print("stated total:", stated_total)
    print("parsed total:", total)
    print("n holdings:", len(holdings))
    for h in sorted(holdings, key=lambda h: -h["value"])[:15]:
        print(f"{h['issuer']:35} {h['cusip']:12} value=${h['value']:>12,}K  shares={h['shares']:>15,}")
