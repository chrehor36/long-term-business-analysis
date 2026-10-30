import sys, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
f = sys.argv[1]
which = sys.argv[2]
pats = {
 'is': [r'Cost of sales', r'Gross profit', r'(?i)basic earnings per share|Basic'],
 'bs': [r'(?i)inventories', r'(?i)total equity', r'(?i)lease liabilit|borrowings|Trade and other payables'],
 'cf': [r'(?i)cash (generated|flows?) from operat', r'(?i)tangible|property, plant', r'(?i)dividends paid|Dividends'],
}[which]
pages = open(f, encoding='utf-8', errors='replace').read().split('\f')
for i, p in enumerate(pages):
    if all(re.search(x, p) for x in pats) and len(p) < 9000:
        print(f"===== page {i+1} =====")
        print("\n".join(l for l in p.splitlines() if l.strip()))
