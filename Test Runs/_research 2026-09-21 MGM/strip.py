import re, io, sys, html
def strip(h):
    h = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', h)
    h = re.sub(r'(?i)<br\s*/?>', '\n', h)
    h = re.sub(r'(?i)</(p|div|tr|h[1-6]|li)>', '\n', h)
    h = re.sub(r'(?i)</t[dh]>', ' | ', h)
    h = re.sub(r'(?s)<[^>]+>', '', h)
    h = html.unescape(h)
    h = h.replace('\u00a0', ' ').replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"')
    h = re.sub(r'[ \t]+', ' ', h)
    h = re.sub(r'\n\s*\n+', '\n', h)
    lines = [l.strip() for l in h.split('\n')]
    return '\n'.join(l for l in lines if l and l != '|')
if __name__ == '__main__':
    t = io.open(sys.argv[1], encoding='utf-8', errors='replace').read()
    io.open(sys.argv[2], 'w', encoding='utf-8').write(strip(t))
    print('wrote', sys.argv[2])
