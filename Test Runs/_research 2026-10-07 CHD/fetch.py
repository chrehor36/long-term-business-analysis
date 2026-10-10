import sys, re, html, urllib.request, os
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
def fetch(cik, acc, doc, out):
    if os.path.exists(out): return
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read().decode('utf-8','ignore')
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', raw)
    t = re.sub(r'(?is)<ix:header>.*?</ix:header>', ' ', t)
    t = re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', t)
    t = re.sub(r'(?i)</td>|</th>', ' | ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t).replace('\xa0',' ')
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    open(out,'w',encoding='utf-8').write(f"SOURCE {url}\nACCESSION {acc}\n"+t)
    print(out, len(t))
if __name__=='__main__':
    for line in sys.stdin:
        p=line.split()
        if len(p)==4: fetch(*p)
