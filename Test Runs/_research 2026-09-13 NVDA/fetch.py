"""Fetch NVIDIA primary documents from EDGAR (SEC User-Agent, throttled) and write .htm and .txt beside this script.
For 8-Ks, every exhibit in the filing index is also fetched."""
import sys, os, re, html, json, urllib.request, time
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources
OUT = os.path.dirname(os.path.abspath(__file__))
CIK = 1045810


def get(url):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=sources.SEC_UA)
            return urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
        except Exception as e:
            print("  retry", i, e)
            time.sleep(2 + 2 * i)
    raise RuntimeError("failed " + url)


def to_text(raw):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)</(td|th)>", " | ", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t


def grab(acc, doc, name):
    txtp = os.path.join(OUT, name + ".txt")
    if os.path.exists(txtp):
        print("have", name)
        return
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{doc}"
    raw = get(url)
    open(txtp, "w", encoding="utf-8").write(to_text(raw))
    print(name, "->", url)
    time.sleep(0.4)


def exhibits(acc, prefix):
    a = acc.replace("-", "")
    idx = get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{acc}-index.htm")
    time.sleep(0.4)
    rows = re.findall(r'(?is)<tr[^>]*>(.*?)</tr>', idx)
    for r in rows:
        m = re.search(r'href="(/Archives/edgar/data/[^"]+)"', r)
        typ = re.findall(r'(?is)<td[^>]*>(.*?)</td>', r)
        if not m or len(typ) < 4:
            continue
        t = re.sub(r"<[^>]+>", "", typ[3]).strip()
        fn = m.group(1).split("/")[-1]
        if not fn.lower().endswith((".htm", ".html", ".txt")):
            continue
        if t.startswith("EX-") or t == "8-K":
            name = f"{prefix}_{t.replace('/', '')}"
            txtp = os.path.join(OUT, name + ".txt")
            if os.path.exists(txtp):
                continue
            raw = get("https://www.sec.gov" + m.group(1))
            open(txtp, "w", encoding="utf-8").write(to_text(raw))
            print(name, "->", fn)
            time.sleep(0.4)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "core"
    if what == "core":
        for acc, doc, name in [
            ("0001045810-26-000075", "nvda-20260726.htm", "10Q_FY27Q2"),
            ("0001045810-26-000052", "nvda-20260426.htm", "10Q_FY27Q1"),
            ("0001045810-26-000021", "nvda-20260125.htm", "10K_FY2026"),
            ("0001045810-25-000023", "nvda-20250126.htm", "10K_FY2025"),
            ("0001045810-24-000029", "nvda-20240128.htm", "10K_FY2024"),
            ("0001045810-23-000017", "nvda-20230129.htm", "10K_FY2023"),
            ("0001045810-22-000036", "nvda-20220130.htm", "10K_FY2022"),
            ("0001045810-21-000010", "nvda-20210131.htm", "10K_FY2021"),
            ("0001045810-26-000036", "nvda-20260512.htm", "DEF14A_2026"),
        ]:
            try:
                grab(acc, doc, name)
            except Exception as e:
                print("FAIL", name, e)
    elif what == "8k":
        for acc, prefix in [
            ("0001045810-26-000073", "8K_2026-08-26"),
            ("0001045810-26-000051", "8K_2026-05-20"),
            ("0001045810-26-000019", "8K_2026-02-25"),
            ("0001045810-25-000228", "8K_2025-11-19"),
            ("0001045810-25-000207", "8K_2025-08-27"),
            ("0001045810-25-000115", "8K_2025-05-28"),
            ("0001045810-26-000069", "8K_2026-08-17"),
            ("0001045810-26-000078", "8K_2026-09-03"),
            ("0001193125-26-275783", "8K_2026-06-18"),
            ("0001045810-25-000082", "8K_2025-04-15"),
            ("0001045810-25-000007", "8K_2025-01-17"),
            ("0001045810-22-000151", "8K_2022-09-01"),
            ("0001045810-22-000146", "8K_2022-08-31"),
            ("0001045810-22-000005", "8K_2022-02-08"),
            ("0001045810-23-000217", "8K_2023-10-17"),
            ("0001045810-23-000221", "8K_2023-10-24"),
        ]:
            try:
                exhibits(acc, prefix)
            except Exception as e:
                print("FAIL", prefix, e)
    else:
        # ad hoc: acc doc name
        grab(sys.argv[2], sys.argv[3], sys.argv[4])
