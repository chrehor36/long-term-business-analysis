#!/usr/bin/env python3
"""Fetch Paymentus (PAY) filings from EDGAR into cache/ (git-ignored). Reuses tools/sources.py."""
import sys, os, json, re, html, time
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources as S

CACHE = os.path.join(HERE, "cache")
os.makedirs(CACHE, exist_ok=True)
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}

def get(url, binary=False):
    import urllib.request
    for i in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
            return r if binary else r.decode("utf-8", "replace")
        except Exception as e:
            last = e; time.sleep(1.5*(i+1))
    raise last

def strip(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", h)
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h

cik = S.cik_for("PAY")
if isinstance(cik, (tuple, list)):
    cik = cik[0]
cik = int(str(cik).lstrip("0"))
print("CIK", cik)
cik10 = str(cik).zfill(10)
sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik10}.json"))
json.dump(sub, open(os.path.join(CACHE, "submissions.json"), "w"))
facts = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json"))
json.dump(facts, open(os.path.join(CACHE, "companyfacts.json"), "w"))
print("facts tags:", len(facts["facts"].get("us-gaap", {})))

rf = sub["filings"]["recent"]
rows = list(zip(rf["form"], rf["filingDate"], rf["accessionNumber"], rf["primaryDocument"], rf["reportDate"]))
want = {"10-K", "10-Q", "8-K", "DEF 14A", "S-1", "S-1/A", "424B4", "10-K/A", "10-Q/A"}
idx = [r for r in rows if r[0] in want]
with open(os.path.join(HERE, "filing_index.md"), "w", encoding="utf-8") as f:
    f.write("# PAY filing index (from data.sec.gov submissions, fetched 2026-09-11)\n\n| form | filed | period | accession | primary doc |\n|---|---|---|---|---|\n")
    for r in idx:
        f.write(f"| {r[0]} | {r[1]} | {r[4]} | `{r[2]}` | {r[3]} |\n")
print("indexed", len(idx))

def fetch_doc(acc, doc, name):
    accn = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}/{doc}"
    out = os.path.join(CACHE, name + ".txt")
    if os.path.exists(out):
        return out
    h = get(url)
    open(os.path.join(CACHE, name + ".htm"), "w", encoding="utf-8").write(h)
    open(out, "w", encoding="utf-8").write(strip(h))
    print("fetched", name, len(h))
    time.sleep(0.4)
    return out

# 10-Ks: all of them
for r in idx:
    if r[0] == "10-K":
        fetch_doc(r[2], r[3], f"10-K_FY{r[4][:4]}_{r[2]}")
# latest three 10-Qs
q = [r for r in idx if r[0] == "10-Q"][:3]
for r in q:
    fetch_doc(r[2], r[3], f"10-Q_{r[4]}_{r[2]}")
# DEF 14A: latest two
for r in [r for r in idx if r[0] == "DEF 14A"][:2]:
    fetch_doc(r[2], r[3], f"DEF14A_{r[1]}_{r[2]}")
# S-1 and 424B4 (prospectus) - the earliest years
for r in [r for r in idx if r[0] in ("424B4",)][:1]:
    fetch_doc(r[2], r[3], f"424B4_{r[1]}_{r[2]}")
# 8-Ks: find the EX-99.1 in the latest earnings 8-Ks (need the filing index)
n8 = 0
for r in [r for r in idx if r[0] == "8-K"]:
    if n8 >= 6: break
    accn = r[2].replace("-", "")
    try:
        ix = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}/")
    except Exception as e:
        print("8-K index fail", r[2], e); continue
    m = re.findall(r'href="([^"]+ex99[^"]*\.htm)"', ix, flags=re.I)
    if m:
        doc = m[0].split("/")[-1]
        fetch_doc(r[2], doc, f"8-K_EX99_{r[1]}_{r[2]}")
        n8 += 1
    time.sleep(0.4)
print("done")
