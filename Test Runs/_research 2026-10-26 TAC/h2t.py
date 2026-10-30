# html to text: python -I h2t.py in.htm out.txt
import sys, re, html
s = open(sys.argv[1], encoding='utf-8', errors='replace').read()
s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
s = re.sub(r'(?i)<br\s*/?>|</(p|div|tr|li|h\d|table)>', '\n', s)
s = re.sub(r'(?i)</t[dh]>', ' | ', s)
s = re.sub(r'<[^>]+>', ' ', s)
s = html.unescape(s).replace('\xa0', ' ')
s = re.sub(r'[ \t]+', ' ', s)
s = re.sub(r'(\s*\|\s*)+\n', '\n', s)
s = re.sub(r'\n\s*\n+', '\n', s)
open(sys.argv[2], 'w', encoding='utf-8').write(s)
