"""Convert EDGAR .htm filings to plain text beside them (raw dumps are gitignored)."""
import sys, re, html
for f in sys.argv[1:]:
    s = open(f, encoding='utf-8', errors='replace').read()
    s = re.sub(r'(?is)<(script|style).*?</\1>', '', s)
    s = re.sub(r'(?is)<ix:header>.*?</ix:header>', '', s)
    s = re.sub(r'(?i)</(p|div|tr|li|h\d)>|<br\s*/?>', '\n', s)
    s = re.sub(r'(?i)</t[dh]>', ' | ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).replace('\xa0', ' ')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    open(f.rsplit('.', 1)[0] + '.txt', 'w', encoding='utf-8').write(s)
