import sys, json, urllib.request, time, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def get(url, out=None):
    req = urllib.request.Request(url, headers=UA)
    raw = urllib.request.urlopen(req, timeout=60).read()
    if out:
        open(out, "wb").write(raw)
    time.sleep(0.2)
    return raw
if __name__ == "__main__":
    url, out = sys.argv[1], sys.argv[2]
    r = get(url, out)
    print(len(r), out)
