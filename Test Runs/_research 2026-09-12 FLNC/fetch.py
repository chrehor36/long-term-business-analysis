import sys, os, re, html, json, urllib.request, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-12 FLNC"
CIK = "1868941"

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
    for k in range(3):
        try:
            return urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
        except Exception as e:
            err = e; time.sleep(2)
    raise err

def grab(acc, doc, name):
    p = os.path.join(OUT, name + ".txt")
    if os.path.exists(p):
        print("have", name); return
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{doc}"
    raw = get(url)
    t = totext(raw)
    open(p, "w", encoding="utf-8").write(t)
    print(name, len(t), "chars ->", url)
    time.sleep(0.4)

def exhibits(acc, name):
    a = acc.replace("-", "")
    idx = get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json")
    items = json.loads(idx)["directory"]["item"]
    for it in items:
        n = it["name"]
        if n.lower().endswith((".htm", ".html", ".txt")) and not n.endswith("index.htm") and "-index" not in n:
            print("  ", acc, n, it.get("size"))
    return [it["name"] for it in items]

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "main":
        for args in [
          ("0001868941-25-000081","flnc-20250930.htm","10K_FY2025"),
          ("0001868941-26-000029","flnc-20260630.htm","10Q_2026-06-30"),
          ("0001104659-26-056304","flnc-20260331x10q.htm","10Q_2026-03-31"),
          ("0001868941-26-000005","flnc-20251231.htm","10Q_2025-12-31"),
          ("0001140361-26-002380","ny20057461x1_def14a.htm","DEF14A_2026"),
          ("0001868941-24-000070","flnc-20240930.htm","10K_FY2024"),
          ("0001868941-23-000085","flnc-20230930.htm","10K_FY2023"),
          ("0001868941-22-000120","flnc-20220930.htm","10K_FY2022"),
          ("0001868941-21-000012","fluenceenergyllc10-k2021.htm","10K_FY2021"),
          ("0001104659-25-036111","flnc-20241231x10ka.htm","10KA_FY2024"),
          ("0001104659-26-039628","tm2610909d1_8k.htm","8K_2026-04-03_item101"),
          ("0001868941-26-000012","flnc-20260331.htm","8KA_2026-04-06_item101"),
          ("0001104659-26-062654","tm2614667d1_8k.htm","8K_2026-05-15_item302"),
          ("0001104659-26-059052","tm2613150-1_s3asr.htm","S3ASR_2026-05-12"),
          ("0001868941-26-000037","flnc-20260827.htm","8K_2026-09-01_item502"),
        ]:
            try: grab(*args)
            except Exception as e: print("FAIL", args[-1], e)
    elif mode == "idx":
        for acc in sys.argv[2:]:
            exhibits(acc, "")
            time.sleep(0.3)
    elif mode == "one":
        grab(sys.argv[2], sys.argv[3], sys.argv[4])
