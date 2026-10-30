import json, sys, os, time, urllib.request
UA = {"User-Agent": "BRK research chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
OUT = os.path.dirname(os.path.abspath(__file__))
def get(url, dest=None, binary=False):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
                enc = r.headers.get("Content-Encoding", "")
                if enc == "gzip":
                    import gzip; data = gzip.decompress(data)
                elif enc == "deflate":
                    import zlib; data = zlib.decompress(data)
                break
        except Exception as e:
            print("retry", attempt, e); time.sleep(3)
    else:
        raise SystemExit("failed " + url)
    if dest:
        p = os.path.join(OUT, dest)
        with open(p, "wb") as f: f.write(data)
        print("wrote", p, len(data))
    return data
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "sub":
        get("https://data.sec.gov/submissions/CIK0001609253.json", "submissions.json")
    elif cmd == "facts":
        get("https://data.sec.gov/api/xbrl/companyfacts/CIK0001609253.json", "companyfacts.json")
    else:
        get(sys.argv[2], sys.argv[3])
