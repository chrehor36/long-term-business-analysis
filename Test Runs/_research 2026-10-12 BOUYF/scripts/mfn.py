"""Fetch an mfn.se release iframe and print plain text plus attachment links. Usage: python -I mfn.py URL OUT"""
import sys, re, html, urllib.request
req = urllib.request.Request(sys.argv[1], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0'})
t = urllib.request.urlopen(req, timeout=60).read().decode('utf8', 'replace')
links = re.findall(r'href="(https://[^"]*(?:Download|\.pdf)[^"]*)"', t)
body = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', t)
body = re.sub(r'(?i)</(p|div|tr|li|h\d)>|<br\s*/?>', '\n', body)
body = re.sub(r'(?i)</t[dh]>', ' | ', body)
body = html.unescape(re.sub(r'<[^>]+>', '', body))
body = re.sub(r'[ \t\xa0]+', ' ', body); body = re.sub(r'\n\s*\n+', '\n', body)
open(sys.argv[2], 'w', encoding='utf8').write(body + '\nLINKS:\n' + '\n'.join(links))
print(len(body), links[:5])
