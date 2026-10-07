import sys, os, re, html, json, time, urllib.request
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sources
HERE = os.path.dirname(os.path.abspath(__file__))
CIK = 1734722

def get(url):
    last = None
    for k in range(4):
        try:
            req = urllib.request.Request(url, headers=sources.SEC_UA)
            return urllib.request.urlopen(req, timeout=180).read().decode("utf-8", "replace")
        except Exception as e:
            last = e; time.sleep(2 + 3 * k)
    raise last

def strip(raw):
    t = re.sub(r"(?is)<(script|style|ix:header).*?</\1>", " ", raw)
    t = re.sub(r"(?i)</(td|th)>", " | ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u00a0\u200b]+", " ", t)
    t = re.sub(r"( \| )+( ?\| ?)*", " | ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

def grab(acc, doc, name, cik=CIK):
    path = os.path.join(HERE, name + ".txt")
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        print("have", name); return path
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{doc}"
    raw = get(url); t = strip(raw)
    open(path, "w", encoding="utf-8").write(t)
    print(name, len(t), "chars", url); time.sleep(0.4)
    return path

def exhibits(acc, cik=CIK):
    a = acc.replace("-", "")
    idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json"))
    return [i["name"] for i in idx["directory"]["item"]]
