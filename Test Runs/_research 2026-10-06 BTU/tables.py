import sys, re
from bs4 import BeautifulSoup
def rows_of(path):
    soup = BeautifulSoup(open(path, encoding='utf-8', errors='replace').read(), 'lxml')
    out = []
    for ti, t in enumerate(soup.find_all('table')):
        for tr in t.find_all('tr'):
            cells = [re.sub(r'\s+', ' ', td.get_text(' ', strip=True)) for td in tr.find_all(['td','th'])]
            cells = [c for c in cells if c and c not in ('$', ')', '%', ')%')]
            if cells:
                out.append((ti, cells))
    return out
if __name__ == "__main__":
    path, pat = sys.argv[1], sys.argv[2]
    rows = rows_of(path)
    tables = sorted({ti for ti, c in rows if re.search(pat, ' '.join(c), re.I)})
    for ti in tables:
        print(f"--- table {ti}")
        for t2, c in rows:
            if t2 == ti:
                print(' | '.join(c)[:220])
