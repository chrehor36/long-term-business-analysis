import sys, os, re, html, json
sys.path.insert(0, os.path.abspath('tools'))
import sources
D = os.path.abspath('Test Runs/_research 2026-09-19 DIS')

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

def grab(acc, doc, out):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/1744489/%s/%s' % (a, doc)
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='dis_'+out, max_age_h=999)
    open(os.path.join(D, out), 'w', encoding='utf-8').write(strip(raw))
    print(out, len(raw))

for acc, doc, out in [
    ('0001744489-25-000155','dis-20250927.htm','tenk_FY2025.txt'),
    ('0001744489-23-000216','dis-20230930.htm','tenk_FY2023.txt'),
    ('0001744489-21-000220','dis-20211002.htm','tenk_FY2021.txt'),
    ('0001744489-26-000057','dis-20260627.htm','tenq_2026Q3.txt'),
]:
    grab(acc, doc, out)
