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

def index(acc):
    a = acc.replace('-', '')
    url = 'https://www.sec.gov/Archives/edgar/data/1744489/%s/' % a
    raw = sources._get(url + 'index.json', headers=sources.SEC_UA, cache_name='dis_idx_'+a, max_age_h=999)
    j = json.loads(raw)
    return url, [(i['name'], i.get('size')) for i in j['directory']['item']]

def grab(url, out):
    raw = sources._get(url, headers=sources.SEC_UA, cache_name='dis_'+out, max_age_h=999)
    open(os.path.join(D, out), 'w', encoding='utf-8').write(strip(raw))
    print('WROTE', out, len(raw))

if __name__ == '__main__':
    for acc in sys.argv[1:]:
        url, items = index(acc)
        print('==', acc)
        for n, s in items:
            print('   ', n, s)
