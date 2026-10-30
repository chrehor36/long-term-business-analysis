import sys, os, re, html, json, urllib.request, time
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-13 BAM"
CIK = "1937926"

def totext(raw):
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
    t = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", t)
    t = re.sub(r"(?i)</(p|div|tr|li|h\d|table|br)>", "\n", t)
    t = re.sub(r"(?i)</t[dh]>", " | ", t)
    t = re.sub(r"(?i)<br[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t ]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t

def get(url):
    req = urllib.request.Request(url, headers=sources.SEC_UA)
    return urllib.request.urlopen(req, timeout=120).read()

def index(acc, cik=CIK):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/index.json"
    d = json.loads(get(url))
    return [(i["name"], i.get("size")) for i in d["directory"]["item"]]

def grab(acc, doc, name, cik=CIK):
    a = acc.replace("-", "")
    url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{a}/{doc}"
    raw = get(url).decode("utf-8", "replace")
    t = totext(raw)
    open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8").write(t)
    print(name, len(t), "chars ->", url)
    time.sleep(0.4)

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "index":
        for acc in sys.argv[2:]:
            print(acc, index(acc)); time.sleep(0.4)
    elif mode == "grab":
        grab(sys.argv[2], sys.argv[3], sys.argv[4], *(sys.argv[5:6]))
