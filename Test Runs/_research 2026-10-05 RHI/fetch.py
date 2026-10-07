import sys, urllib.request, gzip, time, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out, tries=6):
    for k in range(tries):
        try:
            return _get(url,out)
        except Exception as e:
            if k==tries-1: raise
            time.sleep(5*(k+1))
def _get(url, out):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    open(out, "wb").write(data)
    time.sleep(0.2)
    return len(data)
if __name__ == "__main__":
    for i in range(1, len(sys.argv), 2):
        print(sys.argv[i+1], get(sys.argv[i], sys.argv[i+1]))
