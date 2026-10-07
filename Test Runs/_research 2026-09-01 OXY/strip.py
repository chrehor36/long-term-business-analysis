import re, sys, html
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8', errors='replace').read()
t = re.sub(r'(?is)<(script|style|head)[^>]*>.*?</\1>', ' ', t)
t = re.sub(r'(?is)<br[^>]*>', '\n', t)
t = re.sub(r'(?is)</(p|div|tr|h1|h2|h3|h4|li|table)>', '\n', t)
t = re.sub(r'(?is)</t[dh]>', ' | ', t)
t = re.sub(r'(?is)<[^>]+>', '', t)
t = html.unescape(t)
t = t.replace('\u00a0', ' ').replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2014','--').replace('\u2013','-')
t = re.sub(r'[ \t]+', ' ', t)
t = re.sub(r'\n\s*\n+', '\n', t)
lines = [l.strip() for l in t.split('\n')]
lines = [l for l in lines if l and l != '|']
open(dst,'w',encoding='utf-8').write('\n'.join(lines))
print(dst, len(lines), 'lines')
