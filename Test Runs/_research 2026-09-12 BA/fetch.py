import sys, os, re, html, urllib.request, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-12 BA"

def grab(cik, acc, doc, name):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    raw = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
    open(os.path.join(OUT, name + ".htm"), "w", encoding="utf-8").write(raw)
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?i)</(p|div|tr|td|th|li|h\d|table|br)>", "\n", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8").write(t)
    print(name, len(t), "chars ->", url)

if __name__ == "__main__":
    for args in [
      ("12927","0001628280-26-004357","ba-20251231.htm","10K_FY2025"),
      ("12927","0001628280-26-050038","ba-20260630.htm","10Q_2026Q2"),
      ("12927","0001193125-26-096787","d39411ddef14a.htm","DEF14A_2026"),
      ("12927","0000012927-25-000015","ba-20241231.htm","10K_FY2024"),
    ]:
        try: grab(*args)
        except Exception as e: print("FAIL", args[-1], e)
        time.sleep(0.5)
