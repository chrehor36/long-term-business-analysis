# usage: python fetch.py LABEL ACCESSION [ACCESSION ...]  -> writes LABEL_<acc6>__<doc>.txt (row-form text) for every htm doc in the filing
import sys, json, re, html
sys.path.insert(0, '.')
import edgar
CIK = 715153
def rows(h):
    h = re.sub(r'(?is)<(script|style).*?</\1>', ' ', h)
    out = []; pos = 0
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
                if c and c not in ('$', ')', '%', '¥', 'Yen'): cells.append(c)
            if cells:
                out.append(' | '.join(cells).replace('( ', '(').replace(' | )', ')'))
        pos = m.end()
    tail = h[pos:]
    tail = re.sub(r'(?i)</(p|div|h\d|li)>', '\n', tail)
    tail = html.unescape(re.sub(r'<[^>]+>', ' ', tail))
    for line in tail.split('\n'):
        line = re.sub(r'\s+', ' ', line).strip()
        if line: out.append(line)
    return out
