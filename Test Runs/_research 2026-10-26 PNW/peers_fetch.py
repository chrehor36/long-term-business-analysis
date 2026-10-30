"""Fetch peer utility figures from SEC EDGAR XBRL companyfacts and build peers.md.

Usage:
  python -I peers_fetch.py fetch      # download companyfacts + submissions into cache\
  python -I peers_fetch.py build      # extract, compute, write peers.md and peers_data.json
  python -I peers_fetch.py text       # download FY2025 10-K primary docs, print ROE sentences
"""
import json, os, re, sys, time, html, urllib.request
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
UA = "Chris Hrehor chrehor36@gmail.com"
YEARS = list(range(2016, 2026))

COS = [
    ("PNW", "Pinnacle West Capital", 764622),
    ("IDA", "IDACORP", 1057877),
    ("POR", "Portland General Electric", 784977),
    ("XEL", "Xcel Energy", 72903),
    ("TEP", "Tucson Electric Power", 100122),
]

CONCEPTS = {
    # ProfitLoss only as last resort (POR after 2016: no noncontrolling interest, so equals NI to common)
    "ni": ["NetIncomeLoss", "NetIncomeLossAvailableToCommonStockholdersBasic", "ProfitLoss"],
    # total operating revenues first; RevenueFromContract... (excludes alternative revenue) only as fallback
    "rev": ["Revenues", "RegulatedAndUnregulatedOperatingRevenue", "SalesRevenueNet",
            "ElectricUtilityRevenue", "RevenueFromContractWithCustomerExcludingAssessedTax"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
           "DepreciationAmortizationAndAccretionNet", "Depreciation"],
}


# Hand-curated from `text` mode output (FY2025 10-K primary documents, quotes trimmed only).
NOTES = """## Allowed ROE and equity ratio, last state order (from FY2025 10-K text)

| Company (utility) | Allowed ROE | Equity ratio in order | Order | FY2025 10-K accession |
|---|---|---|---|---|
| PNW (APS, ACC) | 9.55% | not stated in 10-K text | ACC approval of 2022 Rate Case ROO, 22 Feb 2024 | 0000764622-26-000011 |
| IDA (Idaho Power, IPUC) | 9.6% | not specified ("filed cost of debt and capital structure") | IPUC approval of 2025 Settlement Stipulation, Dec 2025, rates eff. 1 Jan 2026 | 0001057877-26-000028 |
| POR (PGE, OPUC) | 9.34% | not stated in 10-K text (company target ~50%) | OPUC 2025 GRC order (UE 435), 20 Dec 2024; reaffirmed in Order 25-417, 21 Oct 2025 | 0001193125-26-052750 |
| XEL (NSP-Minnesota, MPUC electric) | 9.25% | 52.5% | MPUC approval, July 2023 (2022-2024 multi-year plan) | 0000072903-26-000009 |
| TEP (ACC) | not stated in 10-K text | not stated in 10-K text | 2023 Rate Order, rates effective 1 Sep 2023 | 0000100122-26-000006 |

Quotes:

- PNW: "On February 22, 2024, the ACC approved the 2022 Rate Case ROO with certain amendments that resulted in, among other things, (i) an approximately $491.7 million increase in the annual base revenue requirement, (ii) a 9.55% return on equity, ..." The 10-K also states APS's actual common equity ratio (ACC definition) was 52% at 31 Dec 2025 and the ACC dividend floor is 40%. The pending 2025 Rate Case requests 10.70% ROE on 52.35% equity.
- IDA: "In December 2025, the IPUC approved a settlement stipulation (2025 Settlement Stipulation) related to the Idaho general rate case that Idaho Power had filed in May 2025, with new rates effective January 1, 2026." Terms: "a 9.6 percent return on equity and a 7.41 percent authorized rate of return based on the filed cost of debt and capital structure, applied to an Idaho-jurisdictional rate base of approximately $4.9 billion".
- POR: "PGE's authorized ROE was 9.34 % for 2025 and 9.5 % for 2024." The 2025 GRC order is referred to as "its Order issued December 20, 2024 related to PGE's 2025 GRC (OPUC Docket UE 435)".
- XEL: "In July 2023, the MPUC approved a three-year rate increase of approximately $332 million for 2022-2024, based on a ROE of 9.25% and an equity ratio of 52.5%." (2024 Minnesota electric case pending: requested 10.3% ROE, 52.5% equity.)
- TEP: the FY2025 10-K says "TEP's last rate case proceeding was finalized in 2023" but gives no ROE or capital structure for the 2023 Rate Order. Pending 2025 Rate Case: "a return on equity of 10.50% ... a capital structure for ratemaking purposes of approximately 55% common equity and 45% long-term debt".

## Tagging notes

- TEP is still an SEC filer: FY2025 10-K filed 12 Feb 2026 (accession 0000100122-26-000006).
- PNW tags net income to common only as NetIncomeLossAvailableToCommonStockholdersBasic (NetIncomeLoss last used FY2010). Revenue is SalesRevenueNet for FY2016-17.
- POR tags ProfitLoss from FY2017 (no noncontrolling interest after 2016) and equity only as StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest; with no NCI these equal common figures. POR's FY2025 10-K was filed under a filing agent accession (0001193125-...). It also carries a stray LongTermDebt fact dated 2025-10-27 ($68m), excluded.
- PNW current maturities of LT debt are tagged OtherLongTermDebtCurrent through FY2023, LongTermDebtCurrent from FY2024.
- TEP has no combined D&A tag: D&A = Depreciation + OtherDepreciationAndAmortization (income statement lines). FY2016 TEP LT debt is noncurrent only (current not tagged).
- XEL D&A is DepreciationAmortizationAndAccretionNet (cash flow statement); XEL LT debt for FY2016-24 includes capital/finance lease obligations.
- Revenue concept switches at ASC 606 (FY2018) for most filers; totals used throughout, not RevenueFromContractWithCustomer.
- Figures for parents (PNW, IDA, XEL) are consolidated; companyfacts excludes the subsidiary registrant (APS, Idaho Power, NSP etc.) data in combined filings.
"""


def get(url, path):
    if os.path.exists(path):
        return
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    with open(path, "wb") as f:
        f.write(data)
    time.sleep(0.2)


def fetch():
    for t, _, cik in COS:
        c = f"{cik:010d}"
        get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json", os.path.join(CACHE, f"facts_{t}.json"))
        get(f"https://data.sec.gov/submissions/CIK{c}.json", os.path.join(CACHE, f"subs_{t}.json"))
        print("fetched", t)


def load(t, kind):
    with open(os.path.join(CACHE, f"{kind}_{t}.json"), encoding="utf-8") as f:
        return json.load(f)


def days(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days


def pick(facts, concept, year, instant):
    """Value for fiscal `year` as reported in the 10-K for that fiscal year (fy == year)."""
    node = facts.get("us-gaap", {}).get(concept)
    if not node:
        return None
    cands = []
    for f in node.get("units", {}).get("USD", []):
        if not f.get("form", "").startswith("10-K") or f.get("fp") != "FY" or f.get("fy") != year:
            continue
        if int(f["end"][:4]) != year or f["end"][5:7] != "12":  # all five have Dec 31 year ends
            continue
        if instant:
            if "start" in f:
                continue
        else:
            if "start" not in f or not (350 <= days(f["start"], f["end"]) <= 380):
                continue
        cands.append(f)
    if not cands:
        return None
    cands.sort(key=lambda f: (f["form"] != "10-K", f["filed"]))
    f = cands[0]
    return {"val": f["val"], "accn": f["accn"], "concept": concept, "form": f["form"], "filed": f["filed"]}


def first(facts, names, year, instant=False):
    for n in names:
        r = pick(facts, n, year, instant)
        if r:
            return r
    return None


def equity(facts, year):
    r = pick(facts, "StockholdersEquity", year, True)
    if r:
        return r
    tot = pick(facts, "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", year, True)
    if tot:
        nci = pick(facts, "MinorityInterest", year, True)
        v = tot["val"] - (nci["val"] if nci else 0)
        return dict(tot, val=v, concept="StockholdersEquityIncl...NCI less MinorityInterest" if nci else
                    "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest (no NCI tagged)")
    return None


def ltd(facts, year):
    tot = pick(facts, "LongTermDebt", year, True)
    if tot:
        return dict(tot, concept="LongTermDebt (incl. current)")
    nc = first(facts, ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations"], year, True)
    # PNW tagged its current-maturities line as OtherLongTermDebtCurrent through FY2023
    cur = first(facts, ["LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent",
                        "OtherLongTermDebtCurrent"], year, True)
    if nc:
        v = nc["val"] + (cur["val"] if cur else 0)
        return dict(nc, val=v, concept=nc["concept"] + (" + " + cur["concept"] if cur else " (current not tagged)"))
    return None


def build():
    out = {}
    for t, name, cik in COS:
        facts = load(t, "facts")["facts"]
        rows = {}
        for y in [2015] + YEARS:
            row = {"eq": equity(facts, y)}
            if y >= 2016:
                for k, names in CONCEPTS.items():
                    row[k] = first(facts, names, y)
                if row["da"] and row["da"]["concept"] == "Depreciation":
                    # TEP reports depreciation and amortization on separate lines
                    am = pick(facts, "OtherDepreciationAndAmortization", y, False)
                    if am:
                        row["da"] = dict(row["da"], val=row["da"]["val"] + am["val"],
                                         concept="Depreciation + OtherDepreciationAndAmortization")
                row["ltd"] = ltd(facts, y)
            rows[y] = row
        out[t] = rows
    with open(os.path.join(HERE, "peers_data.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    write_md(out)


def v(cell):
    return None if cell is None else cell["val"]


def m(x):
    return "not tagged" if x is None else f"{x/1e6:,.0f}"


def write_md(out):
    L = ["# Peer utilities: SEC EDGAR XBRL figures, FY2016 to FY2025", "",
         "Source: data.sec.gov companyfacts API, fetched 2026-10-26. Values in USD millions. "
         "Each value is the one reported in the 10-K for that fiscal year (fact fy equals the fiscal year, "
         "form 10-K, fp FY, 12-month duration for flows). ROE = net income / average of opening and closing "
         "common equity. Script: peers_fetch.py; raw JSON in cache\\.", ""]
    summary = []
    for t, name, cik in COS:
        rows = {int(k): r for k, r in out[t].items()}
        L += [f"## {name} ({t}, CIK {cik})", "",
              "| FY | Net income | Common equity (YE) | ROE | Revenue | OCF | Capex | D&A | LT debt | 10-K accession |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        roes, fcf, cap, da = [], 0, 0, 0
        fcf_ok = cap_ok = True
        used = {}
        for y in YEARS:
            r, p = rows[y], rows[y - 1]
            ni, e1, e0 = v(r["ni"]), v(r["eq"]), v(p["eq"])
            roe = ni / ((e0 + e1) / 2) if None not in (ni, e0, e1) else None
            if roe is not None:
                roes.append(roe)
            o, c, d = v(r["ocf"]), v(r["capex"]), v(r["da"])
            if o is None or c is None:
                fcf_ok = False
            else:
                fcf += o - c
            if c is None or d is None:
                cap_ok = False
            else:
                cap += c; da += d
            accn = next((r[k]["accn"] for k in ("ni", "eq", "rev", "ocf") if r.get(k)), "not found")
            for k in ("ni", "eq", "rev", "capex", "da", "ltd"):
                if r.get(k):
                    used.setdefault(k, {}).setdefault(r[k]["concept"], []).append(y)
            L.append(f"| {y} | {m(ni)} | {m(e1)} | {'n/a' if roe is None else f'{roe*100:.1f}%'} | {m(v(r['rev']))} | "
                     f"{m(o)} | {m(c)} | {m(d)} | {m(v(r['ltd']))} | {accn} |")
        L.append("")
        lab = {"ni": "Net income", "eq": "Equity", "rev": "Revenue", "capex": "Capex", "da": "D&A", "ltd": "LT debt"}
        L.append("Concepts used:")
        L.append("")
        for k, s in used.items():
            parts = [f"{c} ({ys[0]}-{ys[-1]})" if len(ys) > 1 else f"{c} ({ys[0]})" for c, ys in s.items()]
            L.append(f"- {lab[k]}: " + "; ".join(parts))
        L.append("")
        r0, r1 = v(rows[2016]["rev"]), v(rows[2025]["rev"])
        cagr = (r1 / r0) ** (1 / 9) - 1 if r0 and r1 else None
        summary.append((t, name, sum(roes) / len(roes) if roes else None, len(roes),
                        fcf if fcf_ok else None, cap / da if cap_ok and da else None, cagr))
    L += ["## Summary, FY2016 to FY2025", "",
          "| Company | Avg ROE (10 yrs) | Sum OCF minus capex ($m) | Capex / D&A | Revenue CAGR 2016-2025 |",
          "|---|---|---|---|---|"]
    for t, name, aroe, n, fcf, cd, cagr in summary:
        L.append(f"| {name} ({t}) | {'n/a' if aroe is None else f'{aroe*100:.1f}%'}{'' if n == 10 else f' ({n} yrs)'} | "
                 f"{m(fcf) if fcf is not None else 'incomplete'} | {'incomplete' if cd is None else f'{cd:.2f}x'} | "
                 f"{'n/a' if cagr is None else f'{cagr*100:.1f}%'} |")
    L.append("")
    L += [NOTES]
    with open(os.path.join(HERE, "peers.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print("\n".join(L))


def text():
    for t, name, cik in COS:
        subs = load(t, "subs")["filings"]["recent"]
        idx = [i for i, fm in enumerate(subs["form"]) if fm == "10-K"]
        print(f"== {t}: latest 10-K filings:",
              [(subs["reportDate"][i], subs["filingDate"][i], subs["accessionNumber"][i]) for i in idx[:3]])
        if not idx:
            continue
        i = idx[0]
        accn, doc = subs["accessionNumber"][i], subs["primaryDocument"][i]
        path = os.path.join(CACHE, f"10k_{t}_{accn}.htm")
        get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn.replace('-', '')}/{doc}", path)
        raw = open(path, encoding="utf-8", errors="ignore").read()
        txt = html.unescape(re.sub(r"<[^>]+>", " ", raw))
        txt = re.sub(r"\s+", " ", txt)
        sents = re.split(r"(?<=[.;])\s+(?=[A-Z])", txt)
        print(f"-- {accn} {doc} report {subs['reportDate'][i]}")
        for s in sents:
            if re.search(r"return on equity|\bROE\b", s, re.I) and "%" in s and len(s) < 900:
                print(" *", s.strip())


if __name__ == "__main__":
    {"fetch": fetch, "build": build, "text": text}[sys.argv[1]]()
