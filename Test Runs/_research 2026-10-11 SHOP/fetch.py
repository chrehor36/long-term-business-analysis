import sys, urllib.request, gzip, os, time
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com", "Accept-Encoding": "gzip, deflate"}
def get(url, out):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    open(out, "wb").write(data)
    print(out, len(data))
    time.sleep(0.3)
for i in range(1, len(sys.argv), 2):
    get(sys.argv[i], sys.argv[i+1])
