# parse "Unaudited Consolidated Statements of Cash Flows Divided into Non-financial Services Businesses and Finance Subsidiaries"
import fitz, glob, re, json, sys
NUM = re.compile(r'^\(?-?[\d,]+\)?$|^[－—-]$')
def val(s):
    s = s.strip()
    if s in ('－', '—', '-'): return 0
    neg = s.startswith('(')
    v = int(s.strip('()').replace(',', ''))
    return -v if neg else v
out = {}
for p in sorted(glob.glob('ir/pdf/*reference*.pdf')):
    d = fitz.open(p)
    for pg in d:
        t = pg.get_text()
        if 'Cash Flows' not in t or 'Divided into' not in t: continue
        lines = [l.strip() for l in t.split('\n') if l.strip()]
        # header years
        yrs = re.findall(r'(?:Year ended|Fiscal year ended)\s*(Mar(?:ch)?\.? 31, \d{4})', ' '.join(lines))
        rows = []; label = []; nums = []
        start = False
        for l in lines:
            if l.startswith('Cash flows from operating'): start = True
            if not start: continue
            if NUM.match(l):
                nums.append(val(l))
                if len(nums) == 8:
                    rows.append((' '.join(label), nums)); label = []; nums = []
            else:
                if nums:  # partial row -> reset
                    rows.append((' '.join(label), nums)); label = []; nums = []
                label.append(l)
        out[p] = {'years': yrs, 'rows': rows}
        print('=====', p, yrs)
        for lab, n in rows:
            print(f'{lab[:70]:70} | ' + ' '.join(f'{x:>11,}' for x in n))
json.dump(out, open('splitcf.json', 'w'), indent=1)
