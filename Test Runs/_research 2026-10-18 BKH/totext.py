import sys, re, html
from bs4 import BeautifulSoup
src, out = sys.argv[1], sys.argv[2]
raw = open(src, 'rb').read().decode('utf-8', 'ignore')
soup = BeautifulSoup(raw, 'html.parser')
for t in soup(['script','style']): t.decompose()
for tr in soup.find_all('tr'):
    cells = [c.get_text(' ', strip=True) for c in tr.find_all(['td','th'])]
    cells = [c for c in cells if c]
    tr.replace_with(soup.new_string('\n' + ' | '.join(cells) + '\n'))
txt = soup.get_text('\n')
txt = re.sub(r'\n\s*\n+', '\n', txt)
open(out, 'w', encoding='utf-8').write(txt)
print(len(txt))
