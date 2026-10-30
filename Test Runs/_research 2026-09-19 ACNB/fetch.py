import sys, os, re, urllib.request, json
sys.path.insert(0, 'C:/Users/chreh/OneDrive/Documents/BRK/tools')
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = "715579"

def get(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req).read()

def strip(html):
    s = html.decode('utf-8', 'ignore')
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?is)<br\s*/?>', '\n', s)
    s = re.sub(r'(?is)</(p|div|tr|h1|h2|h3|li|table)>', '\n', s)
    s = re.sub(r'(?is)</t[dh]>', ' | ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    import html as H
    s = H.unescape(s)
    s = re.sub(r'[ \t\xa0]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s

def doc(accession, primary, out):
    a = accession.replace('-', '')
    url = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{primary}"
    raw = get(url)
    open(out + '.htm', 'wb').write(raw)
    open(out + '.txt', 'w', encoding='utf-8').write(strip(raw))
    print(out, len(raw), '->', os.path.getsize(out + '.txt'))

if __name__ == '__main__':
    for acc, prim, out in [
        ('0001628280-26-017229', 'acnb-20251231.htm', 'tenk_2025'),
        ('0000715579-25-000030', 'acnb-20241231.htm', 'tenk_2024'),
        ('0000715579-24-000028', 'acnb-20231231.htm', 'tenk_2023'),
        ('0000715579-23-000015', 'acnb-20221231.htm', 'tenk_2022'),
        ('0000715579-22-000018', 'acnb-20211231.htm', 'tenk_2021'),
        ('0001628280-26-054143', 'acnb-20260630.htm', 'tenq_2026Q2'),
    ]:
        try:
            doc(acc, prim, out)
        except Exception as e:
            print('FAIL', out, e)
