import os, urllib.request, re, html
R = "Test Runs/_research 2026-09-20 CALM"
UA = {"User-Agent": "BRK research chrehor36@gmail.com"}
def get(url, path):
    if not os.path.exists(path):
        req = urllib.request.Request(url, headers=UA)
        open(path,'wb').write(urllib.request.urlopen(req, timeout=120).read())
    return open(path, 'rb').read().decode('utf-8', 'replace')

def totext(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    h = re.sub(r'(?i)</(p|div|tr|h[1-6]|li)>', '\n', h)
    h = re.sub(r'(?i)</t[dh]>', ' | ', h)
    h = re.sub(r'(?i)<br[^>]*>', '\n', h)
    h = re.sub(r'<[^>]+>', '', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    return h

docs = [
 ("0001562762-26-000080", "calm2026053010K.htm", "tenk_FY2026"),
 ("0001562762-26-000102", "calm-20260831_8K.htm", "8k_20260902_item101"),
 ("0001562762-26-000078", "8k20260722.htm", "8k_20260722_earnings"),
]
for acc, doc, name in docs:
    a = acc.replace('-','')
    url = f"https://www.sec.gov/Archives/edgar/data/16160/{a}/{doc}"
    h = get(url, f"{R}/{name}.htm")
    open(f"{R}/{name}.txt","w",encoding="utf-8").write(totext(h))
    print(name, len(h), "->", len(totext(h)))
