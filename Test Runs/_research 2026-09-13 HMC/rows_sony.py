import sys, re, html
sys.path.insert(0, '.')
import edgar
def rows(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    out = []
    # split into blocks: tables to rows, text elsewhere
    pos = 0
    for m in re.finditer(r'(?is)<table.*?</table>', h):
        pre = h[pos:m.start()]
        pre = re.sub(r'(?i)</(p|div|h\d|li)>', '\n', pre)
        pre = html.unescape(re.sub(r'<[^>]+>', ' ', pre))
        for line in pre.split('\n'):
            line = re.sub(r'\s+', ' ', line).strip()
            if line: out.append(line)
        for tr in re.findall(r'(?is)<tr.*?</tr>', m.group(0)):
            cells = []
            for td in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>', tr):
                c = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', td))).strip()
                if c and c not in ('$', ')', '%'): cells.append(c)
            if cells:
                out.append(' | '.join(cells).replace('( ', '(').replace(' | )', ')'))
        pos = m.end()
    return out
if __name__ == '__main__':
    for name, acc, doc in [a.split('|') for a in sys.argv[1:]]:
        url = f"https://www.sec.gov/Archives/edgar/data/313838/{acc.replace('-','')}/{doc}"
        r = rows(edgar.get(url))
        open(name + '.rows.txt', 'w', encoding='utf-8').write('\n'.join(r))
        print(name, len(r))
