import sys, os, re, html, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
D = os.path.abspath('Test Runs/_research 2026-09-19 CB')
CIK = '896159'

def strip(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    h = re.sub(r'(?is)<br\s*/?>', '\n', h)
    h = re.sub(r'(?is)</(p|div|tr|h[1-6]|li)>', '\n', h)
    h = re.sub(r'(?is)</t[dh]>', ' | ', h)
    h = re.sub(r'(?s)<[^>]+>', '', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0]+', ' ', h)
    h = re.sub(r'\n\s*\n\s*\n+', '\n\n', h)
    return h

def grab(acc, doc, out, cik=CIK):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/%s' % (cik, a, doc)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='cb_'+out, max_age_h=999)
    if not isinstance(raw, str): raw = raw.decode('utf-8', 'replace')
    open(os.path.join(D, out), 'w', encoding='utf-8').write(strip(raw))
    print(out, len(raw))

def index(acc, cik=CIK):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/%s/%s/' % (cik, a)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='cbidx_'+acc, max_age_h=999)
    if not isinstance(raw, str): raw = raw.decode('utf-8','replace')
    return re.findall(r'href="([^"]+\.(?:htm|txt))"', raw)

if __name__ == '__main__':
    for acc, doc, out in [
        ('0000896159-26-000005','cb-20251231.htm','tenk_FY2025.txt'),
        ('0000896159-24-000003','cb-20231231.htm','tenk_FY2023.txt'),
        ('0000896159-22-000005','cb-20211231.htm','tenk_FY2021.txt'),
        ('0000896159-26-000017','cb-20260630.htm','tenq_2026Q2.txt'),
    ]:
        grab(acc, doc, out)
