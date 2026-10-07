import sys, os, re, html, json, urllib.request, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-13 CNR"

def totext(raw):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

def get(url):
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    err = None
    for k in range(3):
        try:
            return urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
        except Exception as e:
            err = e; time.sleep(2)
    raise err

def grab(cik, acc, doc, name):
    p = os.path.join(OUT, name + ".txt")
    if os.path.exists(p):
        print("have", name); return
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    raw = get(url)
    t = totext(raw)
    open(p, "w", encoding="utf-8").write(t)
    print(name, len(t), "chars ->", url)
    time.sleep(0.4)

def exhibits(cik, acc):
    a = acc.replace("-", "")
    idx = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/index.json")
    items = json.loads(idx)["directory"]["item"]
    out = []
    for it in items:
        n = it["name"]
        if n.lower().endswith((".htm", ".html", ".txt")) and "index" not in n:
            print("  ", acc, n, it.get("size"))
            out.append(n)
    return out

C = "1710366"; A = "1037676"
MAIN = [
 (C,"0001710366-26-000007","cnr-20251231.htm","10K_FY2025"),
 (C,"0001710366-26-000054","cnr-20260630.htm","10Q_2026-06-30"),
 (C,"0001710366-25-000010","ceix-20241231.htm","CEIX_10K_FY2024"),
 (C,"0001710366-24-000006","ceix-20231231.htm","CEIX_10K_FY2023"),
 (C,"0001710366-23-000005","ceix-20221231.htm","CEIX_10K_FY2022"),
 (C,"0001437749-22-003140","ceix20211231_10k.htm","CEIX_10K_FY2021"),
 (C,"0001193125-25-007135","d836647d8k.htm","8K_2025-01-15_close"),
 (C,"0001193125-25-028132","d900101d8ka.htm","8KA_2025-02-18"),
 (C,"0001710366-26-000017","cnr-20260316.htm","DEF14A_2026"),
 (A,"0001558370-24-001229","arch-20231231x10k.htm","ARCH_10K_FY2023"),
 (A,"0001558370-23-001458","arch-20221231x10k.htm","ARCH_10K_FY2022"),
 (A,"0001558370-22-001243","arch-20211231x10k.htm","ARCH_10K_FY2021"),
 (A,"0001558370-24-014411","arch-20240930x10q.htm","ARCH_10Q_2024-09-30"),
]
if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "main":
        for args in MAIN:
            try: grab(*args)
            except Exception as e: print("FAIL", args[-1], e)
    elif mode == "idx":
        cik = sys.argv[2]
        for acc in sys.argv[3:]:
            exhibits(cik, acc); time.sleep(0.3)
    elif mode == "one":
        grab(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
