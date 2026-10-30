import json, os, re, time, urllib.request, html as htmlmod, datetime, csv

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
DOCS_CACHE = os.path.join(CACHE, "10k_docs")
os.makedirs(DOCS_CACHE, exist_ok=True)
UA = "BRK-Framework research chrehor36@gmail.com"
TARGET = datetime.date(2018, 6, 30)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read()

resolved = json.load(open(os.path.join(SCRATCH, "sp500_2013_resolved_ciks.json")))

rows = list(csv.DictReader(open(os.path.join(SCRATCH, "sp500_2013_coverage_gaps.csv"))))
need_price = [r["ticker"] for r in rows if r["reason"].startswith("NO_PRICE")]
print(f"{len(need_price)} tickers need price extraction")

DATE_RE = r"([A-Z][a-z]+\.?\s+\d{1,2},?\s*\d{4})"
DOLLAR_RE = r"\$\s*([\d,]+(?:\.\d+)?)\s*(million|billion)?"
SHARES_NUM_RE = r"([\d,]{6,})\s*shares"

def parse_date(s):
    s = re.sub(r"[,.]", "", s.replace(".", " ")).strip()
    s = re.sub(r"\s+", " ", s)
    for fmt in ("%B %d %Y",):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None

def find_amv(text):
    idx = text.lower().find("aggregate market value")
    if idx < 0:
        return None, None
    window = text[max(0, idx-300):idx+500]
    dm = re.search(DOLLAR_RE, window)
    dt = re.search(DATE_RE, window)
    if not dm or not dt:
        return None, None
    val = float(dm.group(1).replace(",", ""))
    mult = dm.group(2)
    if mult and mult.lower() == "billion":
        val *= 1_000_000_000
    elif mult and mult.lower() == "million":
        val *= 1_000_000
    d = parse_date(dt.group(1))
    return val, d

def find_shares(text):
    # try a few anchor phrases used across different filers
    for anchor in ["shares outstanding", "number of shares outstanding", "shares of common stock outstanding"]:
        idx = text.lower().find(anchor)
        if idx < 0:
            continue
        window = text[idx:idx+500]
        sm = re.search(SHARES_NUM_RE, window)
        dt = re.search(DATE_RE, window)
        if sm and dt:
            val = float(sm.group(1).replace(",", ""))
            d = parse_date(dt.group(1))
            if val > 1000:  # sanity check -- not a stray small number
                return val, d
    return None, None

def get_submissions(cik):
    fn = os.path.join(CACHE, f"subs_{cik}.json")
    if os.path.exists(fn):
        subs = json.load(open(fn))
    else:
        url = f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json"
        data = fetch(url)
        open(fn, "wb").write(data)
        subs = json.loads(data)
    # high-filing-count entities paginate older filings into separate files
    # not included in "recent" -- merge them in (same issue found earlier
    # this session with Berkshire's 13F history)
    for extra in subs["filings"].get("files", []):
        efn = os.path.join(CACHE, f"subs_{cik}_{extra['name']}")
        if os.path.exists(efn):
            edata = json.load(open(efn))
        else:
            try:
                edata = json.loads(fetch(f"https://data.sec.gov/submissions/{extra['name']}"))
                json.dump(edata, open(efn, "w"))
            except Exception:
                continue
        for key in subs["filings"]["recent"]:
            if key in edata:
                subs["filings"]["recent"][key] = subs["filings"]["recent"][key] + edata[key]
    return subs

def find_fy2018_10k(subs):
    # A 10-K's cover-page "aggregate market value" date is ~6 months BEFORE
    # its own fiscal year-end. So the filing whose AMV disclosure actually
    # covers our target date is the one whose YEAR-END comes ~6mo AFTER the
    # target -- not just whichever reportDate is numerically closest (which
    # wrongly treats an early year-end the same as a late one, and ties
    # break toward the wrong, earlier filing -- caught on Kellogg, which
    # has both a 2017-12-30 AND a 2018-12-29 10-K equidistant from the
    # target; only the latter's cover page actually describes June 2018).
    recent = subs["filings"]["recent"]
    after, before = [], []
    for i, form in enumerate(recent["form"]):
        if form not in ("10-K", "10-K/A"):
            continue
        rd = recent.get("reportDate", [None]*len(recent["form"]))[i]
        if not rd:
            continue
        try:
            rdate = datetime.date.fromisoformat(rd)
        except ValueError:
            continue
        if datetime.date(2017, 6, 1) <= rdate <= datetime.date(2019, 12, 31):
            entry = (rdate, recent["accessionNumber"][i], recent["primaryDocument"][i])
            (after if rdate >= TARGET else before).append(entry)
    if after:
        after.sort(key=lambda e: (e[0] - TARGET).days)
        return after[0]
    if before:
        before.sort(key=lambda e: (TARGET - e[0]).days)
        return before[0]
    return None

def extract_from_doc(text):
    amv, amv_date = find_amv(text)
    shares, shares_date = find_shares(text)
    return amv, amv_date, shares, shares_date

results = {}
failures = []
for i, t in enumerate(need_price):
    cik = resolved.get(t)
    if cik is None:
        failures.append((t, "NO_CIK"))
        continue
    try:
        subs = get_submissions(cik)
    except Exception as e:
        failures.append((t, f"SUBS_FETCH_FAIL {e}"))
        time.sleep(0.15)
        continue
    found = find_fy2018_10k(subs)
    if not found:
        failures.append((t, "NO_FY2018_10K_FOUND"))
        time.sleep(0.1)
        continue
    rdate, accn, primdoc = found
    accn_nodash = accn.replace("-", "")
    doc_fn = os.path.join(DOCS_CACHE, f"{t}.htm")
    if not os.path.exists(doc_fn):
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn_nodash}/{primdoc}"
        try:
            data = fetch(url)
            open(doc_fn, "wb").write(data)
        except Exception as e:
            failures.append((t, f"DOC_FETCH_FAIL {e}"))
            time.sleep(0.15)
            continue
        time.sleep(0.2)
    raw = open(doc_fn, encoding="utf-8", errors="ignore").read()
    text = re.sub(r"<[^>]+>", " ", raw)
    text = htmlmod.unescape(text)
    text = re.sub(r"\s+", " ", text)
    # only search the first ~15000 chars -- cover page is always near the top
    amv, amv_date, shares, shares_date = extract_from_doc(text[:15000])
    if amv is None or shares is None:
        failures.append((t, "NO_AMV_OR_SHARES_MATCH"))
        continue
    implied_price = amv / shares

    # Sanity check: cross-validate the extracted shares count against the
    # XBRL-reported share count for this company (any point in time -- just
    # checking order of magnitude). Cover pages for multi-class-share
    # companies (BRK.B, etc.) or dense tables can cause the regex to grab a
    # mismatched number; silently accepting that would corrupt the dataset
    # with a garbage price, which is worse than an honest coverage gap.
    facts_fn = os.path.join(CACHE, f"facts_{t}.json")
    xbrl_shares_values = []
    if os.path.exists(facts_fn):
        try:
            fd = json.load(open(facts_fn))
            dei = fd.get("facts", {}).get("dei", {})
            gaap = fd.get("facts", {}).get("us-gaap", {})
            for tagset, tag in [(dei, "EntityCommonStockSharesOutstanding"),
                                 (gaap, "CommonStockSharesOutstanding"),
                                 (gaap, "WeightedAverageNumberOfDilutedSharesOutstanding")]:
                if tag in tagset:
                    for x in tagset[tag]["units"].get("shares", []):
                        if x.get("val"):
                            xbrl_shares_values.append(x["val"])
        except Exception:
            pass
    if xbrl_shares_values:
        closest = min(xbrl_shares_values, key=lambda v: abs(v - shares))
        ratio = shares / closest if closest else 0
        if not (0.5 <= ratio <= 2.0):
            failures.append((t, f"SANITY_CHECK_FAILED (extracted shares {shares:,.0f} vs XBRL {closest:,.0f}, ratio {ratio:.2f})"))
            continue
    results[t] = {
        "amv": amv, "amv_date": amv_date.isoformat() if amv_date else None,
        "shares": shares, "shares_date": shares_date.isoformat() if shares_date else None,
        "implied_price": implied_price, "report_date": rdate.isoformat(),
    }
    if i % 10 == 0:
        print(f"[{i}/{len(need_price)}] {t}: AMV=${amv:,.0f} as of {amv_date}, "
              f"shares={shares:,.0f} as of {shares_date}, implied_px=${implied_price:.2f}")

print(f"\nExtracted: {len(results)} / {len(need_price)}")
print(f"Failed: {len(failures)}")
for t, reason in failures:
    print(" ", t, reason)

out_fn = os.path.join(SCRATCH, "10k_implied_prices.json")
prior = json.load(open(out_fn)) if os.path.exists(out_fn) else {}
prior.update(results)  # merge, never silently discard earlier verified results
json.dump(prior, open(out_fn, "w"), indent=1, default=str)
json.dump(failures, open(os.path.join(SCRATCH, "10k_extraction_failures.json"), "w"), indent=1)
