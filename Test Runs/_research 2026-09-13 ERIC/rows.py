# usage: python rows.py URL OUT  -> row-form text (one table row per line)
import sys, re, html
sys.path.insert(0, '.')
import edgar
def rows(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    h = re.sub(r'(?is)<ix:header>.*?</ix:header>', ' ', h)
    out = []; pos = 0
    def text(seg):
        seg = re.sub(r'(?i)<br[^>]*>', '\n', seg)
        seg = re.sub(r'(?i)</(p|div|h\d|li)>', '\n', seg)
        seg = html.unescape(re.sub(r'<[^>]+>', ' ', seg)).replace('\xa0', ' ')
        for line in seg.split('\n'):
            line = re.sub(r'\s+', ' ', line).strip()
            if line: out.append(line)
    for m in re.finditer(r'(?is)<table.*?</table>', h):
        text(h[pos:m.start()])
        for tr in re.findall(r'(?is)<tr.*?</tr>', m.group(0)):
            cells = []
            for td in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>', tr):
                c = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', td)).replace('\xa0', ' ')).strip()
                if c and c not in ('$', ')', '%'): cells.append(c)
            if cells:
                out.append(' | '.join(cells).replace('( ', '(').replace(' | )', ')'))
        pos = m.end()
    text(h[pos:])
    return out
if __name__ == '__main__':
    h = edgar.get(sys.argv[1])
    o = rows(h)
    open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(o))
    print(sys.argv[2], len(o), 'lines')
