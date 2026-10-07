import json, os, sys, time, urllib.request, io
D = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def get(url, binary=False):
    for i in range(4):
        try:
            r = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(r, timeout=60) as f:
                b = f.read()
            return b if binary else b.decode("utf-8", "replace")
        except Exception as e:
            print("retry", i, url, e); time.sleep(2 + 3*i)
    raise RuntimeError("failed " + url)
def save(name, txt):
    p = os.path.join(D, name)
    io.open(p, "w", encoding="utf-8").write(txt)
    print("wrote", name, len(txt))
    return p
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sub":
        save("submissions.json", get("https://data.sec.gov/submissions/CIK0000789570.json"))
    elif cmd == "facts":
        save("companyfacts.json", get("https://data.sec.gov/api/xbrl/companyfacts/CIK0000789570.json"))
    elif cmd == "doc":
        # doc <accession-no-dashes> <filename> <outname>
        acc, fn, out = sys.argv[2], sys.argv[3], sys.argv[4]
        save(out, get(f"https://www.sec.gov/Archives/edgar/data/789570/{acc}/{fn}"))
    elif cmd == "idx":
        acc = sys.argv[2]
        save(f"idx_{acc}.json", get(f"https://www.sec.gov/Archives/edgar/data/789570/{acc}/index.json"))
