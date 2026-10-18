import sys, urllib.request, gzip, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip"}
def get(url, out):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    with open(out, "wb") as f: f.write(data)
    time.sleep(0.2)
    return len(data)
if __name__ == "__main__":
    for i in range(1, len(sys.argv), 2):
        print(sys.argv[i+1], get(sys.argv[i], sys.argv[i+1]))
