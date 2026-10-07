import sys, os, re, html, urllib.request, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-13 AMZN"

def strip(raw):
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

def grab(cik, acc, doc, name):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    p = os.path.join(OUT, name + ".txt")
    if os.path.exists(p):
        print("have", name); return
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    raw = urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
    t = strip(raw)
    open(p, "w", encoding="utf-8").write(f"SOURCE: {url}\nACCESSION: {acc}\n\n" + t)
    print(name, len(t), "chars ->", url)

def index(cik, acc):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{acc}-index.htm"
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    docs = re.findall(r'href="(/Archives/edgar/data/[^"]+)"[^>]*>([^<]+)</a>\s*</td>\s*<td[^>]*>([^<]*)</td>', raw)
    return re.findall(r'<td[^>]*>([^<]*)</td>\s*<td[^>]*><a href="(/Archives/edgar/data/[^"]+)"', raw)

if __name__ == "__main__":
    C = "1018724"
    jobs = [
      ("0001018724-26-000026","amzn-20260630.htm","10Q_2026Q2"),
      ("0001018724-26-000014","amzn-20260331.htm","10Q_2026Q1"),
      ("0001104659-26-041026","tm261382-1_def14a.htm","DEF14A_2026"),
      ("0001104659-26-042891","tm2611746d2_425.htm","425_2026-04-14"),
      ("0001104659-26-042880","tm2611746d1_8k.htm","8K_2026-04-14"),
      ("0001104659-26-021050","tm267374d1_8k.htm","8K_2026-02-27"),
      ("0001104659-26-072140","tm2613616d4_8k.htm","8K_2026-06-10"),
      ("0001104659-26-098339","tm2617924-6_424b3.htm","424B3_2026-08-18"),
      ("0001018724-26-000036","amzn-20260908.htm","8K_2026-09-09"),
      ("0001104659-26-107122","tm2624614-3_424b5.htm","424B5_2026-09-11"),
    ]
    for acc, doc, name in jobs:
        try: grab(C, acc, doc, name)
        except Exception as e: print("FAIL", name, e)
        time.sleep(0.4)
    for acc in ["0001104659-26-042880","0001104659-26-021050","0001104659-26-072140","0001018724-26-000024","0001018724-26-000036","0001104659-26-042891"]:
        try: print(acc, index(C, acc))
        except Exception as e: print("FAIL idx", acc, e)
        time.sleep(0.3)
