import json, os, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache", "failures")

NI_TAGS = ["NetIncomeLoss", "ProfitLoss"]

companies = {
    "SEARS_HOLDINGS": {"bankruptcy": "2018-10-15", "label": "Sears Holdings"},
    "EASTMAN_KODAK": {"bankruptcy": "2012-01-19", "label": "Eastman Kodak"},
    "BED_BATH_BEYOND": {"bankruptcy": "2023-04-23", "label": "Bed Bath & Beyond"},
    "RADIOSHACK": {"bankruptcy": "2015-02-05", "label": "RadioShack"},
}

def load_ni_facts(cik_data):
    gaap = cik_data.get("facts", {}).get("us-gaap", {})
    by_end = {}
    for tag in NI_TAGS:
        if tag not in gaap:
            continue
        for x in gaap[tag]["units"].get("USD", []):
            if x.get("form") not in ("10-K", "10-K/A"):
                continue
            start, end, filed = x.get("start"), x.get("end"), x.get("filed")
            if not (start and end and filed):
                continue
            sd, ed = datetime.date.fromisoformat(start), datetime.date.fromisoformat(end)
            if (ed - sd).days < 300 or (ed - sd).days > 380:
                continue
            fd = datetime.date.fromisoformat(filed)
            prev = by_end.get(ed)
            if prev is None or fd > prev[1]:
                by_end[ed] = (x["val"], fd, tag)
    return by_end

for key, info in companies.items():
    fn = os.path.join(CACHE, f"facts_{key}.json")
    if not os.path.exists(fn):
        print(f"{info['label']}: NO XBRL DATA")
        continue
    d = json.load(open(fn))
    ni_by_end = load_ni_facts(d)
    print(f"\n=== {info['label']} (Chapter 11 filed {info['bankruptcy']}) ===")
    print(f"{'FY End':12} {'NI ($M)':>12} {'Filed':12}")
    ends = sorted(ni_by_end.keys())
    for end in ends:
        val, filed, tag = ni_by_end[end]
        flag = " <-- LOSS" if val < 0 else ""
        print(f"{end.isoformat():12} {val/1e6:12,.1f} {filed.isoformat():12} [{tag}]{flag}")

    # worst-of-trailing-5-year NI evolution, as-of each year-end
    print("  worst-of-trailing-5yr NI, as of each fiscal year-end (point-in-time, filed<=that FY's own filed date):")
    for i, end in enumerate(ends):
        window = ends[max(0, i-4):i+1]
        if len(window) < 5:
            continue
        worst = min(ni_by_end[e][0] for e in window)
        neg_flag = "  <== NEGATIVE (range-anchoring auto-fail)" if worst < 0 else ""
        print(f"    as of {end.isoformat()}: worst-5yr = ${worst/1e6:,.1f}M{neg_flag}")
