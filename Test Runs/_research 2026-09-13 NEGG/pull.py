import json, os, sys, re, time, urllib.request
from bs4 import BeautifulSoup
HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = 1474627

def get(url):
    for i in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=90).read()
        except Exception as e:
            print("retry", url, e); time.sleep(2 + 3 * i)
    raise SystemExit("failed " + url)

def to_text(html):
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style"]):
        t.decompose()
    # table rows -> pipe separated
    for tr in soup.find_all("tr"):
        cells = [c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"])]
        cells = [c for c in cells if c]
        tr.replace_with(soup.new_string("\n| " + " | ".join(cells) + " |\n"))
    txt = soup.get_text("\n")
    txt = re.sub(r"[ \t\xa0]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    return txt

def pull(acc, label):
    base = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/"
    d = json.loads(get(base + "index.json"))
    for it in d["directory"]["item"]:
        n = it["name"]
        if n.lower().endswith((".htm", ".html")) and not n.startswith("R") and "index" not in n:
            out = os.path.join(HERE, f"{label}__{n.rsplit('.', 1)[0]}.txt")
            if os.path.exists(out):
                continue
            txt = to_text(get(base + n))
            with open(out, "w", encoding="utf-8") as f:
                f.write(txt)
            print("saved", os.path.basename(out), len(txt))
            time.sleep(0.3)

if __name__ == "__main__":
    args = sys.argv[1:]
    for i in range(0, len(args), 2):
        pull(args[i], args[i + 1])
