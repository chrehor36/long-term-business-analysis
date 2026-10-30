#!/usr/bin/env python3
"""Fetch CORT primary filings from EDGAR into this research folder as stripped text.
Dumps are named *10-K*.txt / *10-Q*.txt / *8-K*.txt / *DEF14A*.txt so the repo's
.gitignore patterns exclude them (operator instruction: commit analysis only)."""
import io, json, os, re, sys, time, urllib.request, html
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = 1088856  # Corcept Therapeutics

def get(url, tries=4):
    last = None
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
        except Exception as e:
            last = e; time.sleep(2 * (i + 1))
    raise last

def strip(raw):
    t = raw.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</li>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>|</th>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

def submissions():
    d = json.loads(get(f"https://data.sec.gov/submissions/CIK{CIK:010d}.json"))
    r = d["filings"]["recent"]
    rows = [dict(form=r["form"][i], filed=r["filingDate"][i], period=r["reportDate"][i],
                 acc=r["accessionNumber"][i], doc=r["primaryDocument"][i])
            for i in range(len(r["form"]))]
    # older pages
    for f in d["filings"].get("files", []):
        dd = json.loads(get("https://data.sec.gov/submissions/" + f["name"]))
        for i in range(len(dd["form"])):
            rows.append(dict(form=dd["form"][i], filed=dd["filingDate"][i], period=dd["reportDate"][i],
                             acc=dd["accessionNumber"][i], doc=dd["primaryDocument"][i]))
    return d.get("name"), d.get("sic"), d.get("sicDescription"), rows

def save(name, raw):
    p = os.path.join(HERE, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(strip(raw))
    print(f"  wrote {name} ({os.path.getsize(p)//1024} KB)")

def filing_index(acc):
    a = acc.replace("-", "")
    idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json"))
    return [x["name"] for x in idx["directory"]["item"]]

def main():
    name, sic, sicd, rows = submissions()
    print(name, sic, sicd, len(rows), "filings")
    with open(os.path.join(HERE, "filing_index.json"), "w") as f:
        json.dump(rows, f, indent=1)
    want = sys.argv[1:] or ["10-K", "10-Q", "8-K", "DEF 14A"]
    tenk = [r for r in rows if r["form"] == "10-K"]
    print("10-Ks:", [(r["filed"], r["period"], r["acc"]) for r in tenk])
    # every 10-K from FY2008 onward (17-18 years)
    if "10-K" in want:
        for r in tenk:
            fy = r["period"][:4]
            if int(fy) >= 2008:
                fn = f"10-K-FY{fy}.txt"
                if os.path.exists(os.path.join(HERE, fn)): continue
                a = r["acc"].replace("-", "")
                save(fn, get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{r['doc']}"))
                time.sleep(0.3)
    if "10-Q" in want:
        tq = [r for r in rows if r["form"] == "10-Q"][:6]
        for r in tq:
            fn = f"10-Q-{r['period']}.txt"
            if os.path.exists(os.path.join(HERE, fn)): continue
            a = r["acc"].replace("-", "")
            save(fn, get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{r['doc']}"))
            time.sleep(0.3)
    if "DEF 14A" in want:
        for r in [x for x in rows if x["form"] == "DEF 14A"][:3]:
            fn = f"DEF14A-{r['filed']}.txt"
            if os.path.exists(os.path.join(HERE, fn)): continue
            a = r["acc"].replace("-", "")
            save(fn, get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{r['doc']}"))
            time.sleep(0.3)
    if "8-K" in want:
        eks = [r for r in rows if r["form"] == "8-K" and r["filed"] >= "2023-01-01"]
        print(f"{len(eks)} 8-Ks since 2023")
        for r in eks:
            fn = f"8-K-{r['filed']}.txt"
            if os.path.exists(os.path.join(HERE, fn)): continue
            a = r["acc"].replace("-", "")
            try:
                files = filing_index(r["acc"])
            except Exception as e:
                print("  index fail", r["acc"], e); continue
            parts = []
            main_doc = r["doc"]
            parts.append(("MAIN " + main_doc, get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{main_doc}")))
            for fnm in files:
                if re.search(r"ex[-_]?99|ex99|exhibit99", fnm, re.I) and fnm.lower().endswith((".htm", ".html")):
                    parts.append(("EXHIBIT " + fnm, get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{fnm}")))
            txt = ""
            for lab, raw in parts:
                txt += f"\n\n===== {lab} | acc {r['acc']} | filed {r['filed']} =====\n" + strip(raw)
            with open(os.path.join(HERE, fn), "w", encoding="utf-8") as f:
                f.write(txt)
            print(f"  wrote {fn} ({len(txt)//1024} KB, {len(parts)} parts)")
            time.sleep(0.3)

if __name__ == "__main__":
    main()
