import re, sys, os, html, glob
def conv(p, out):
    s = open(p, encoding='utf-8', errors='replace').read()
    s = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', s)
    # table cells -> pipe separated ; rows -> newline
    s = re.sub(r'(?i)</t[dh]>', ' | ', s)
    s = re.sub(r'(?i)</tr>', '\n', s)
    s = re.sub(r'(?i)</(p|div|br|li|h[1-6]|table)>', '\n', s)
    s = re.sub(r'(?i)<br[^>]*>', '\n', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = s.replace('\u00a0',' ').replace('\u2019',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2014','--').replace('\u2013','-')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\|\s*(\n|$)', '\n', s)
    s = re.sub(r'(\|\s*)+\|', '| ', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    lines=[l.strip() for l in s.split('\n')]
    open(out,'w',encoding='utf-8').write('\n'.join(l for l in lines if l and l != '|'))
for p in glob.glob('docs/*.htm'):
    o = p.replace('docs/','txt/').replace('.htm','.txt')
    os.makedirs('txt', exist_ok=True)
    conv(p,o)
    print(o, os.path.getsize(o))
