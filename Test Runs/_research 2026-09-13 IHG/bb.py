import re, glob, json
rows = {}
for fn in sorted(glob.glob('k/*.txt')):
    t = re.sub(r'\s+', ' ', open(fn, encoding='utf-8').read())
    for m in re.finditer(r'Date of purchase: \| (.*?) \|.*?Aggregate number of ordinary shares purchased: \| ([\d,]+) \|.*?Average price paid per share: \| ([$£€]?) ?([\d,.]+)p? ?\|(.*?)Following the above transaction, the Company has ([\d,]+) ordinary shares in issue \(excluding ([\d,]+) held in treasury\)', t):
        d, n, cur, px, mid, out, tr = m.groups()
        rows[d] = dict(n=int(n.replace(',', '')), cur=cur or 'p?', px=float(px.replace(',', '')), out=int(out.replace(',', '')), tr=int(tr.replace(',', '')), src=fn)
from datetime import datetime
def key(d):
    for f in ('%d %B %Y', '%d %b %Y'):
        try: return datetime.strptime(d.strip(), f)
        except: pass
    return datetime(1900,1,1)
ks = sorted(rows, key=key)
for k in ks[-12:]: print(k, rows[k])
print(len(ks), ks[0], rows[ks[0]])
json.dump({k: rows[k] for k in ks}, open('bb_out.json', 'w'), indent=1)
tot = {}
for k in ks:
    y = key(k).year
    tot.setdefault(y, [0, 0.0]); tot[y][0] += rows[k]['n']; tot[y][1] += rows[k]['n'] * rows[k]['px']
print(tot)
