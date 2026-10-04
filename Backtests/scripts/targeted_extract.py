import json, os, re, time, urllib.request, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
DOCS_CACHE = os.path.join(CACHE, "10k_docs")
UA = "BRK-Framework research chrehor36@gmail.com"
TARGET = datetime.date(2018, 6, 30)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read()

def get_submissions(cik):
    fn = os.path.join(CACHE, f"subs_{cik}.json")
    if os.path.exists(fn):
        subs = json.load(open(fn))
    else:
        data = fetch(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")
        open(fn, "wb").write(data)
        subs = json.loads(data)
    for extra in subs["filings"].get("files", []):
        efn = os.path.join(CACHE, f"subs_{cik}_{extra['name']}")
        if os.path.exists(efn):
            edata = json.load(open(efn))
        else:
            try:
                edata = json.loads(fetch(f"https://data.sec.gov/submissions/{extra['name']}"))
                json.dump(edata, open(efn, "w"))
                time.sleep(0.15)
            except Exception:
                continue
        for key in subs["filings"]["recent"]:
            if key in edata:
                subs["filings"]["recent"][key] = subs["filings"]["recent"][key] + edata[key]
    return subs

def find_fy2018_10k(subs):
    # A 10-K's cover-page "aggregate market value" date is ~6 months BEFORE
    # its own fiscal year-end (the "last business day of the 2nd fiscal
    # quarter"). So the filing whose AMV disclosure covers our target date
    # is the one whose YEAR-END comes ~6mo AFTER the target -- not just
    # whichever reportDate is numerically closest (that wrongly treats a
    # year-end 6mo early the same as one 6mo late, and ties break toward
    # the wrong, earlier one).
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
            if rdate >= TARGET:
                after.append(entry)
            else:
                before.append(entry)
    if after:
        after.sort(key=lambda e: (e[0] - TARGET).days)
        return after[0]
    if before:
        before.sort(key=lambda e: (TARGET - e[0]).days)
        return before[0]
    return None

resolved = json.load(open(os.path.join(SCRATCH, "sp500_2013_resolved_ciks.json")))
targets = ["AET", "CA", "DISCA", "HOT", "K", "PBCT", "TWC", "TWX", "TYC", "WYN"]

for t in targets:
    cik = resolved.get(t)
    subs = get_submissions(cik)
    found = find_fy2018_10k(subs)
    if not found:
        print(t, "NO FILING FOUND")
        continue
    rdate, accn, primdoc = found
    accn_nodash = accn.replace("-", "")
    doc_fn = os.path.join(DOCS_CACHE, f"{t}.htm")
    if os.path.exists(doc_fn):
        os.remove(doc_fn)
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accn_nodash}/{primdoc}"
    try:
        data = fetch(url)
        open(doc_fn, "wb").write(data)
        time.sleep(0.2)
    except Exception as ex:
        print(t, "FETCH FAIL", ex)
        continue
    print(t, "report_date:", rdate, "doc:", primdoc)
