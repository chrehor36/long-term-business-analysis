import sys, urllib.request, re, html, os, time
cik, acc, doc, out = sys.argv[1:5]
url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'
req = urllib.request.Request(url, headers={'User-Agent': 'BRK research chrehor36@gmail.com'})
raw = urllib.request.urlopen(req).read().decode('utf-8', 'replace')
raw = re.sub(r'(?is)<(script|style|ix:header).*?</\1>', ' ', raw)
def cell(c):
    c = re.sub(r'<[^>]+>', ' ', c); c = html.unescape(c)
    return re.sub(r'\s+', ' ', c).strip()
def table(m):
    rows = []
    for r in re.findall(r'(?is)<tr.*?</tr>', m.group(0)):
        cs = [cell(c) for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>', r)]
        cs = [c for c in cs if c not in ('', '$', 'R$', '%', ')')]
        if cs: rows.append(' | '.join(cs))
    return '\n[T] ' + '\n[T] '.join(rows) + '\n'
t = re.sub(r'(?is)<table.*?</table>', table, raw)
t = re.sub(r'(?i)</(p|div|li|h\d)>', '\n', t)
t = re.sub(r'(?i)<br\s*/?>', '\n', t)
t = re.sub(r'<[^>]+>', ' ', t)
t = html.unescape(t)
t = re.sub(r'[ \t\xa0]+', ' ', t)
t = re.sub(r'\n\s*\n+', '\n', t)
open(out, 'w', encoding='utf-8').write(t)
print(out, len(t))
time.sleep(0.3)
