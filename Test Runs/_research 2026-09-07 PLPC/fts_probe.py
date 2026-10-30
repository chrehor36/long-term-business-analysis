import urllib.request, urllib.error, json, time, sys

UA = "Chris Hrehor chrehor36@gmail.com"

def get(url, extra=None):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
    req.add_header("Accept-Encoding", "gzip, deflate")
    req.add_header("Host", url.split("/")[2])
    if extra:
        for k, v in extra.items():
            req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            raw = r.read()
            enc = r.headers.get("Content-Encoding", "")
            if enc == "gzip":
                import gzip
                raw = gzip.decompress(raw)
            elif enc == "deflate":
                import zlib
                raw = zlib.decompress(raw)
            return r.status, raw
    except urllib.error.HTTPError as e:
        body = e.read()
        try:
            enc = e.headers.get("Content-Encoding", "")
            if enc == "gzip":
                import gzip
                body = gzip.decompress(body)
        except Exception:
            pass
        return e.code, body
    except Exception as e:
        return -1, ("CONN ERROR: %r" % e).encode()

CANDIDATES = [
    ("1_search-index_plus", 'https://efts.sec.gov/LATEST/search-index?q=%22Preformed+Line+Products%22'),
    ("2_search-index_10K", 'https://efts.sec.gov/LATEST/search-index?q=%22Preformed%20Line%20Products%22&forms=10-K'),
    ("4_search-index_daterange", 'https://efts.sec.gov/LATEST/search-index?q=%22preformed+line+products%22&dateRange=custom&startdt=2019-01-01&enddt=2026-09-07'),
    ("5_efts_search", 'https://efts.sec.gov/LATEST/search-index?q=%22Preformed+Line+Products%22&forms=10-K&hits=10'),
    ("6_ui_json", 'https://www.sec.gov/cgi-bin/srqsb?text=preformed+line+products'),
    ("7_efts_plain", 'https://efts.sec.gov/LATEST/search-index?q="Preformed Line Products"'),
]

for label, url in CANDIDATES:
    st, body = get(url)
    print("=" * 70)
    print(label)
    print(url)
    print("STATUS:", st, "LEN:", len(body))
    print(body[:500].decode("utf-8", "replace"))
    time.sleep(0.4)
