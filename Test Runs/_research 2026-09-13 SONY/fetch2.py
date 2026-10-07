import sys, re, html, os
sys.path.insert(0, '.')
import edgar
def totext(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    h = re.sub(r'(?i)<br\s*/?>', '\n', h)
    h = re.sub(r'(?i)</(p|div|tr|h\d|li|table)>', '\n', h)
    h = re.sub(r'(?i)</t[dh]>', ' | ', h)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t\xa0]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    return h
if __name__ != "__main__":
    pass
if __name__ == "__main__":
  docs = [a.split('|') for a in sys.argv[1:]]
  for name, acc, doc in docs:
    url = f"https://www.sec.gov/Archives/edgar/data/313838/{acc.replace('-','')}/{doc}"
    t = totext(edgar.get(url))
    open(name + '.txt', 'w', encoding='utf-8').write(t)
    print(name, len(t))
