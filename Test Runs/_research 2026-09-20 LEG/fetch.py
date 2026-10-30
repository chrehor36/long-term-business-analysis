import urllib.request, json, sys, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def get(url, dest=None, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    if dest:
        with open(dest, "wb") as f:
            f.write(data)
    return data
if __name__ == "__main__":
    url = sys.argv[1]; dest = sys.argv[2] if len(sys.argv)>2 else None
    d = get(url, dest)
    print(len(d), "bytes ->", dest)
