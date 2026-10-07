import urllib.request, os, time, re, html
UA = {'User-Agent':'chrehor36@gmail.com research'}
D = os.path.dirname(os.path.abspath(__file__))
def raw(url):
    req = urllib.request.Request(url, headers=UA)
    for i in range(4):
        try:
            return urllib.request.urlopen(req, timeout=300).read()
        except Exception as e:
            print('retry', i, e); time.sleep(4)
    raise SystemExit('FAILED '+url)
def totext(b):
    s = b.decode('utf-8','replace')
    s = re.sub(r'(?is)<(script|style|ix:header)[^>]*>.*?</\1>', ' ', s)
    s = re.sub(r'(?is)<br[^>]*>', '\n', s)
    s = re.sub(r'(?is)</(p|div|tr|h1|h2|h3|li|table)>', '\n', s)
    s = re.sub(r'(?is)</t[dh]>', ' | ', s)
    s = re.sub(r'(?s)<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t\xa0]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s
def grab(acc, doc, out):
    p = os.path.join(D, out)
    if os.path.exists(p) and os.path.getsize(p) > 1000:
        print('have', out); return
    a = acc.replace('-','')
    url = 'https://www.sec.gov/Archives/edgar/data/51143/%s/%s' % (a, doc)
    b = raw(url)
    open(p, 'w', encoding='utf-8').write(totext(b))
    print('wrote', out, os.path.getsize(p))
grab('0000051143-26-000010','ibm-20251231.htm','10K_FY2025.txt')
grab('0000051143-26-000078','ibm-20260630.htm','10Q_2026Q2.txt')
grab('0000051143-25-000015','ibm-20241231.htm','10K_FY2024.txt')
grab('0001558370-22-001584','ibm-20211231x10k.htm','10K_FY2021.txt')
