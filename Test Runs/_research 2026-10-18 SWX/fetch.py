"""Fetch an EDGAR document and save raw + text into cache/. Usage: python -I fetch.py URL NAME"""
import sys, re, html, urllib.request, os
url, name = sys.argv[1], sys.argv[2]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
req = urllib.request.Request(url, headers={'User-Agent': 'Chris Hrehor chrehor36@gmail.com'})
raw = urllib.request.urlopen(req, timeout=120).read().decode('utf-8', 'replace')
open(os.path.join(out, name + '.htm'), 'w', encoding='utf-8').write(raw)
t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', raw)
t = re.sub(r'(?i)<ix:header>.*?</ix:header>', ' ', t, flags=re.S)
t = re.sub(r'(?i)</(p|div|tr|li|h\d|table)>', '\n', t)
t = re.sub(r'(?i)<br\s*/?>', '\n', t)
t = re.sub(r'(?i)</t[dh]>', ' | ', t)
t = re.sub(r'<[^>]+>', ' ', t)
t = html.unescape(t).replace('\xa0', ' ')
t = re.sub(r'[ \t]+', ' ', t)
t = re.sub(r'\n\s*\n+', '\n', t)
open(os.path.join(out, name + '.txt'), 'w', encoding='utf-8').write(t)
print(name, len(raw), len(t))
